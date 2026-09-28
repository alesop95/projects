#!/usr/bin/env python3
"""Aggiorna docs/personal/ a partire dai repository GitHub pubblici sotto E:\\.

Uso:
    python scripts/update_personal_projects.py [--source E:\\] [--token TOKEN]

Il token e' opzionale: senza autenticazione l'API GitHub concede 60 richieste/ora, sufficienti
per una singola esecuzione con il numero di progetti attuale (ogni progetto costa 2 richieste:
metadati + README), ma non per esecuzioni ripetute ravvicinate. Con un token (anche senza scope,
solo per alzare il rate limit) si sale a 5000 richieste/ora. Il token si passa con --token o con
la variabile d'ambiente GITHUB_TOKEN, non va mai scritto in questo file.

Cosa fa, in ordine:
1. Elenca le cartelle di primo livello sotto --source (default E:\\), escludendo quelle non
   pertinenti (vedi EXCLUDE_NAMES) e quelle con prefisso "[TBC]" (convenzione del progetto per
   "non ancora pronto", vedi .claude/context/roadmap.md di my-cv).
2. Per ciascuna cartella rimasta, se e' un repository git con remote "origin" su github.com,
   estrae owner/repo dall'URL (gestisce sia HTTPS sia SSH, incluso l'alias "github-personal").
3. Per ciascun repository trovato, interroga l'API REST di GitHub (nessuna scrittura) per i
   metadati e un estratto del README. Un repository privato non si pubblica mai per caso: con un
   token l'API restituisce anche i privati, quindi si guarda il campo private, e la pagina di un
   privato esiste solo se data/personal_meta.json lo dichiara con "privato": true, nel qual caso
   esce senza collegamento e senza nulla preso dal repository.
4. Tecnologie, periodo, stato e descrizione breve nelle tre lingue si leggono da
   data/personal_meta.json, scritto a mano. Fino al 2026-09-24 si ricavavano da GitHub e da git,
   e misuravano la cosa sbagliata: i linguaggi contavano gli strumenti del template propagati in
   ogni repository, le date erano quelle di caricamento o di propagazione e non quelle del lavoro.
5. Genera tre pagine Markdown per progetto (docs/personal/<slug>.md per l'italiano,
   <slug>.en.md per l'inglese, <slug>.es.md per lo spagnolo, secondo la struttura a suffisso di
   mkdocs-static-i18n) e rigenera i tre index.md/index.en.md/index.es.md con la tabella
   riassuntiva nella lingua corrispondente. Non tocca docs/company/.
6. Se esiste data/personal_overrides/<slug>.<lang>.md, il suo contenuto sostituisce l'estratto
   README nella pagina generata di quella lingua: è lì che vive il testo lungo, perché sopravviva
   alle rigenerazioni di questo script. Se manca la traduzione in una lingua, si ripiega sulla
   versione inglese invece di lasciare la pagina vuota.

Le correzioni al contenuto delle pagine personali si fanno quindi in data/personal_meta.json e in
data/personal_overrides/, mai in docs/personal/, che questo script sovrascrive.

Non modifica nulla sotto E:\\: e' un'operazione di sola lettura sui progetti locali, in scrittura
solo sui file di questo sito (docs/personal/).
"""
import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

EXCLUDE_NAMES = {
    "my-cv", "skills", "projects", "prova",
    "windows-status",  # tooling di sistema, non un "progetto" da vetrina
    "$RECYCLE.BIN", "System Volume Information", ".pnpm-store", ".claude",
}

# Categorizzazione statica dei progetti personali per lo slug (lo stesso usato per i nomi dei
# file generati in docs/personal/). Assegnata a mano leggendo data/personal_overrides/, non
# derivata da nessun campo GitHub (topics/language), perche' i topics non sono popolati in modo
# uniforme su tutti i repository. Ogni slug compare in esattamente una categoria. Un progetto
# scoperto da discover_projects() ma assente da questa mappa finisce nel bucket "uncategorized"
# (vedi CATEGORY_ORDER) invece di far fallire lo script: e' un segnale per aggiungere la voce qui
# alla prossima revisione, non un errore bloccante.
PROJECT_CATEGORIES = {
    # Audio ed elaborazione musicale: DSP, acustica, hardware audio, teoria musicale.
    "diy-2way-monitors-home": "audio_music",
    "feature-based-characterization-loudspeakers": "audio_music",
    "gesture-glove-harmonizer": "audio_music",
    "harmonic-tension-vst3": "audio_music",
    "harmony-book": "audio_music",
    "home-recording-training-mixing-setup": "audio_music",
    "rodrainaudio-reverse-eng": "audio_music",
    # Agenti AI e strumenti local-first: orchestrazione LLM/agenti, architetture offline-first.
    "legal-consultant": "ai_agents",
    "lettore-doc": "ai_agents",
    "template-claude-developing": "ai_agents",
    "local-audio-transcriptor": "ai_agents",
    "spanish-learning": "ai_agents",
    # Sicurezza e infrastruttura self-hosted.
    "home-lab-cybersec-networking": "security_infra",
    "pw-manager": "security_infra",
    "telegram-drive-secure": "security_infra",
    # Finanza personale e automazione trading.
    "fiscal-toolkit": "finance_trading",
    "paypal-transaction-data": "finance_trading",
    "real-estate": "finance_trading",
    "trader-bot": "finance_trading",
    # Hardware, embedded e personalizzazione dispositivi.
    "analog-to-digital-vhs-converter": "hardware_embedded",
    "gps-time-synchronization-arduino-stm32": "hardware_embedded",
    "sony-xperia-1-iii-customization": "hardware_embedded",
    # Giochi, hobby e strumenti da collezione.
    "crosswords": "games_hobbies",
    "pok-collecting-update-collection": "games_hobbies",
    "pok-competitive-teambuilder": "games_hobbies",
    "retrogame-mod-pok-dev": "games_hobbies",
    "totocalcio": "games_hobbies",
    # App personali e bot: strumenti/webapp per un evento o un uso personale specifico.
    "app-cross-training": "personal_apps",
    "blog": "personal_apps",
    "civitanext": "personal_apps",
    "discoteca-api": "personal_apps",
    "holiday-template": "personal_apps",
    "my-wedding-day": "personal_apps",
    "telegram-bot": "personal_apps",
}

# Ordine di visualizzazione dei gruppi nell'index generato. "uncategorized" resta per ultimo e
# compare solo se qualche slug scoperto non e' presente in PROJECT_CATEGORIES.
CATEGORY_ORDER = [
    "audio_music",
    "ai_agents",
    "security_infra",
    "finance_trading",
    "hardware_embedded",
    "games_hobbies",
    "personal_apps",
    "uncategorized",
]

API_ROOT = "https://api.github.com"
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
PERSONAL_DIR = REPO_ROOT / "docs" / "personal"
OVERRIDES_DIR = REPO_ROOT / "data" / "personal_overrides"
# Campi scritti a mano per ogni progetto: tecnologie, periodo, stato, descrizione breve nelle tre
# lingue, e se il repository e' privato. Sostituiscono i campi che prima si ricavavano da GitHub
# e da git, che misuravano la cosa sbagliata: i linguaggi contavano gli strumenti del template
# propagati in ogni repository, e le date erano quelle di caricamento o di propagazione, non
# quelle del lavoro (passata di revisione del 2026-09-24).
META_PATH = REPO_ROOT / "data" / "personal_meta.json"

LANGS = ("it", "en", "es")
# "it" e' la lingua di default nella struttura a suffisso di mkdocs-static-i18n: i suoi file
# non hanno suffisso (<slug>.md), le altre due lingue si scrivono come <slug>.en.md/<slug>.es.md.
LANG_SUFFIX = {"it": "", "en": ".en", "es": ".es"}

LABELS = {
    "it": {
        "fork_note": "personalizzazione/estensione, non codebase originale",
        "fork_of": "Fork di",
        "repository": "Repository",
        "technologies": "Tecnologie",
        "topics": "Topics",
        "period": "Periodo",
        "private_repo": "privato, non consultabile",
        "state_in_corso": "in corso",
        "state_fermo": "fermo",
        "state_concluso": "concluso",
        "state_sospeso": "sospeso",
        "from_readme": "Dal README",
        "index_title": "Personal projects",
        "index_intro": (
            "I progetti personali, raggruppati per area. Per ciascuno la pagina riporta "
            "tecnologie, periodo e stato, e il collegamento al repository quando è pubblico."
        ),
        "col_project": "Progetto",
        "col_description": "Descrizione",
        "col_technologies": "Tecnologie",
        "col_period": "Periodo",
        "cat_audio_music": "Audio ed elaborazione musicale",
        "cat_ai_agents": "Agenti AI e strumenti local-first",
        "cat_security_infra": "Sicurezza e infrastruttura self-hosted",
        "cat_finance_trading": "Finanza personale e automazione trading",
        "cat_hardware_embedded": "Hardware, embedded e personalizzazione dispositivi",
        "cat_games_hobbies": "Giochi, hobby e strumenti da collezione",
        "cat_personal_apps": "App personali e bot",
        "cat_uncategorized": "Da categorizzare",
    },
    "en": {
        "fork_note": "customization/extension, not the original codebase",
        "fork_of": "Fork of",
        "repository": "Repository",
        "technologies": "Technologies",
        "topics": "Topics",
        "period": "Period",
        "private_repo": "private, not browsable",
        "state_in_corso": "ongoing",
        "state_fermo": "paused",
        "state_concluso": "completed",
        "state_sospeso": "on hold",
        "from_readme": "From the README",
        "index_title": "Personal projects",
        "index_intro": (
            "Personal projects, grouped by area. Each page lists technologies, period and "
            "status, and links the repository when it is public."
        ),
        "col_project": "Project",
        "col_description": "Description",
        "col_technologies": "Technologies",
        "col_period": "Period",
        "cat_audio_music": "Audio & music engineering",
        "cat_ai_agents": "AI agents & local-first tools",
        "cat_security_infra": "Security & self-hosted infrastructure",
        "cat_finance_trading": "Personal finance & trading automation",
        "cat_hardware_embedded": "Hardware, embedded & device customization",
        "cat_games_hobbies": "Games, hobbies & collecting tools",
        "cat_personal_apps": "Personal apps & bots",
        "cat_uncategorized": "Uncategorized",
    },
    "es": {
        "fork_note": "personalización/extensión, no el código original",
        "fork_of": "Fork de",
        "repository": "Repositorio",
        "technologies": "Tecnologías",
        "topics": "Topics",
        "period": "Periodo",
        "private_repo": "privado, no consultable",
        "state_in_corso": "en curso",
        "state_fermo": "en pausa",
        "state_concluso": "finalizado",
        "state_sospeso": "suspendido",
        "from_readme": "Del README",
        "index_title": "Personal projects",
        "index_intro": (
            "Proyectos personales, agrupados por área. Cada página indica tecnologías, periodo "
            "y estado, y enlaza el repositorio cuando es público."
        ),
        "col_project": "Proyecto",
        "col_description": "Descripción",
        "col_technologies": "Tecnologías",
        "col_period": "Periodo",
        "cat_audio_music": "Ingeniería de audio y música",
        "cat_ai_agents": "Agentes de IA y herramientas local-first",
        "cat_security_infra": "Seguridad e infraestructura autoalojada",
        "cat_finance_trading": "Finanzas personales y automatización de trading",
        "cat_hardware_embedded": "Hardware, embebidos y personalización de dispositivos",
        "cat_games_hobbies": "Juegos, aficiones y herramientas de colección",
        "cat_personal_apps": "Apps personales y bots",
        "cat_uncategorized": "Sin categorizar",
    },
}


def github_request(url, token):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return None
        raise


def github_raw(url):
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError:
        return None


def parse_github_remote(remote_url):
    """Estrae (owner, repo) da un URL remote git verso GitHub.

    Copre sia l'host letterale "github.com" (HTTPS o SSH) sia gli alias SSH definiti in
    ~/.ssh/config secondo la convenzione del progetto (github-personal, github-corp: vedi
    .claude/rules/git-identity-and-repo.md di my-cv), che nell'URL remote non contengono ".com"
    perche' sono nomi host locali che l'SSH client risolve verso github.com.
    """
    remote_url = remote_url.strip()
    match = re.search(r"github[\w.-]*[:/]([^/]+)/([^/.]+?)(?:\.git)?/?$", remote_url)
    if match:
        return match.group(1), match.group(2)
    return None


def discover_projects(source_dir):
    """Ritorna una lista di (folder_name, owner, repo) per ogni progetto valido sotto source_dir."""
    found = []
    for entry in sorted(Path(source_dir).iterdir()):
        if not entry.is_dir():
            continue
        if entry.name in EXCLUDE_NAMES or entry.name.startswith("[TBC]"):
            continue
        git_dir = entry / ".git"
        if not git_dir.exists():
            continue
        try:
            remote = subprocess.run(
                ["git", "-C", str(entry), "remote", "get-url", "origin"],
                capture_output=True, text=True, timeout=10,
            )
        except (subprocess.TimeoutExpired, OSError):
            continue
        if remote.returncode != 0:
            continue
        parsed = parse_github_remote(remote.stdout)
        if not parsed:
            continue
        found.append((entry.name, parsed[0], parsed[1]))
    return found


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def load_meta():
    if not META_PATH.exists():
        return {}
    data = json.loads(META_PATH.read_text(encoding="utf-8"))
    return {k: v for k, v in data.items() if not k.startswith("_")}


def format_month(value):
    """'2026-06' -> '06/2026'; '2019' resta '2019'."""
    if not value:
        return None
    parts = value.split("-")
    return f"{parts[1]}/{parts[0]}" if len(parts) == 2 else value


def format_period(lang, entry):
    """Periodo leggibile dai campi inizio, fine e stato di data/personal_meta.json."""
    if not entry or not entry.get("inizio"):
        return None
    labels = LABELS[lang]
    start = format_month(entry["inizio"])
    end = format_month(entry.get("fine"))
    state = entry.get("stato")
    if state == "in_corso" and not end:
        return f"{start} - {labels['state_in_corso']}"
    text = start if not end or end == start else f"{start} - {end}"
    if state and state != "in_corso":
        text += f", {labels['state_' + state]}"
    return text


def load_override(slug, lang):
    """Testo lungo scritto a mano (o da un agente, a partire dal codice reale o in traduzione)
    per questo progetto in questa lingua: vive in data/personal_overrides/<slug>.<lang>.md, fuori
    da docs/, cosi' questo script puo' sovrascrivere liberamente docs/personal/ a ogni esecuzione
    senza mai perdere il testo curato. Se la traduzione in questa lingua non esiste ancora, ripiega
    sull'inglese (la lingua in cui questi testi sono stati scritti la prima volta) invece di
    lasciare la pagina senza descrizione lunga."""
    for candidate_lang in (lang, "en"):
        override_path = OVERRIDES_DIR / f"{slug}.{candidate_lang}.md"
        if override_path.exists():
            return override_path.read_text(encoding="utf-8").strip()
    return None


def build_project_page(lang, title, owner, repo, meta, entry, readme_excerpt, override_text):
    labels = LABELS[lang]
    entry = entry or {}
    lines = [f"# {title}", ""]
    if meta.get("fork"):
        parent = meta.get("parent", {})
        parent_full = parent.get("full_name", "sconosciuto")
        lines.append(
            f"> {labels['fork_of']} [{parent_full}](https://github.com/{parent_full}): {labels['fork_note']}."
        )
        lines.append("")
    description = (entry.get("descrizione") or {}).get(lang) or meta.get("description")
    if description:
        lines.append(description)
        lines.append("")
    if entry.get("privato"):
        lines.append(f"- **{labels['repository']}**: {labels['private_repo']}")
    else:
        lines.append(f"- **{labels['repository']}**: [{owner}/{repo}]({meta.get('html_url')})")
    if entry.get("tecnologie"):
        lines.append(f"- **{labels['technologies']}**: {entry['tecnologie']}")
    if meta.get("topics"):
        lines.append(f"- **{labels['topics']}**: {', '.join(meta['topics'])}")
    period = format_period(lang, entry)
    if period:
        lines.append(f"- **{labels['period']}**: {period}")
    lines.append("")
    if override_text:
        lines.append(override_text)
        lines.append("")
    elif readme_excerpt:
        lines.append(f"## {labels['from_readme']}")
        lines.append("")
        lines.append(readme_excerpt)
        lines.append("")
    return "\n".join(lines)


MARKDOWN_LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")


def extract_readme_excerpt(readme_text, max_chars=600):
    if not readme_text:
        return None
    # Salta l'eventuale titolo H1 iniziale (gia' usato come titolo pagina) e badge/immagini.
    body_lines = []
    for line in readme_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        if stripped.startswith("[![") or stripped.startswith("!["):
            continue
        # Sostituisce i link Markdown con il solo testo: un estratto troncato a meta' non deve
        # portarsi dietro ancore (es. indici puntati a sezioni del README) che nella pagina
        # generata non esistono e finirebbero per essere link rotti.
        stripped = MARKDOWN_LINK_RE.sub(r"\1", stripped)
        if stripped:
            body_lines.append(stripped)
        if sum(len(l) for l in body_lines) > max_chars:
            break
    excerpt = " ".join(body_lines)
    if len(excerpt) > max_chars:
        excerpt = excerpt[:max_chars].rsplit(" ", 1)[0] + "…"
    return excerpt or None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", default=r"E:\\", help="Cartella da scandire (default E:\\)")
    parser.add_argument("--token", default=os.environ.get("GITHUB_TOKEN"), help="Token GitHub opzionale per alzare il rate limit")
    args = parser.parse_args()

    PERSONAL_DIR.mkdir(parents=True, exist_ok=True)

    projects = discover_projects(args.source)
    if not projects:
        print("[update_personal_projects] Nessun progetto trovato.", file=sys.stderr)
        return 1

    print(f"[update_personal_projects] Trovati {len(projects)} progetti con remote GitHub.")

    index_rows = []
    generated_files = set()
    metas = load_meta()

    for folder_name, owner, repo in projects:
        slug = slugify(repo)
        entry = metas.get(slug)
        if entry is None:
            print(f"  WARN  {slug} manca in data/personal_meta.json: tecnologie, periodo e stato non compariranno.", file=sys.stderr)
        meta = github_request(f"{API_ROOT}/repos/{owner}/{repo}", args.token)
        # Un repository privato non si pubblica per caso. Con un token l'API restituisce anche i
        # privati, quindi "trovato" non vuol dire "pubblico": si guarda il campo private. La pagina
        # di un privato esiste solo se personal_meta.json lo dichiara con privato: true, e in quel
        # caso esce senza collegamento e senza nulla preso dal repository.
        is_private = meta is None or bool(meta.get("private"))
        if is_private and not (entry and entry.get("privato")):
            print(f"  SKIP  {folder_name} -> {owner}/{repo} (privato o non trovato, e non dichiarato privato in personal_meta.json)")
            continue
        if is_private:
            meta, excerpt = {}, None
        else:
            default_branch = meta.get("default_branch", "main")
            readme_raw = github_raw(f"https://raw.githubusercontent.com/{owner}/{repo}/{default_branch}/README.md")
            excerpt = extract_readme_excerpt(readme_raw)
        title = (entry or {}).get("titolo") or meta.get("name") or repo

        for lang in LANGS:
            override_text = load_override(slug, lang)
            page_path = PERSONAL_DIR / f"{slug}{LANG_SUFFIX[lang]}.md"
            page_path.write_text(
                build_project_page(lang, title, owner, repo, meta, entry, excerpt, override_text),
                encoding="utf-8",
            )
            generated_files.add(page_path.name)
        print(f"  OK    {folder_name} -> {slug}.md (it/en/es){' [privato]' if is_private else ''}")

        category = PROJECT_CATEGORIES.get(slug)
        if category is None:
            category = "uncategorized"
            print(
                f"  WARN  {slug} non è presente in PROJECT_CATEGORIES: assegnato a "
                f"'uncategorized', aggiungere la voce nello script.",
                file=sys.stderr,
            )
        index_rows.append({
            "title": title,
            "slug": slug,
            "entry": entry or {},
            "gh_description": meta.get("description") or "",
            "category": category,
        })

    # Rimuove le pagine di progetti che non esistono piu' tra quelli scoperti ora (es. rinominati
    # o rimossi), senza toccare gli index ne' _template.md ne' altri file non generati da questo
    # script in una corsa precedente.
    index_names = {f"index{LANG_SUFFIX[lang]}.md" for lang in LANGS}
    for existing in PERSONAL_DIR.glob("*.md"):
        if existing.name in index_names or existing.name.startswith("_"):
            continue
        if existing.name not in generated_files:
            existing.unlink()
            print(f"  RM    {existing.relative_to(REPO_ROOT)} (progetto non piu' trovato)")

    # Raggruppa per categoria secondo CATEGORY_ORDER; dentro ogni gruppo l'ordinamento è per data
    # di inizio decrescente, presa da personal_meta.json. Un gruppo senza
    # righe (es. nessun progetto scoperto in questa corsa ricade in "uncategorized") non produce
    # un'intestazione vuota nell'index.
    rows_by_category = {key: [] for key in CATEGORY_ORDER}
    for row in index_rows:
        rows_by_category.setdefault(row["category"], []).append(row)
    for rows in rows_by_category.values():
        rows.sort(key=lambda row: row["entry"].get("inizio") or "", reverse=True)

    for lang in LANGS:
        labels = LABELS[lang]
        index_lines = [
            f"# {labels['index_title']}",
            "",
            labels["index_intro"],
            "",
        ]
        for category_key in CATEGORY_ORDER:
            rows = rows_by_category.get(category_key) or []
            if not rows:
                continue
            category_label = labels.get(f"cat_{category_key}", category_key)
            index_lines.append(f"## {category_label}")
            index_lines.append("")
            index_lines.append(
                f"| {labels['col_project']} | {labels['col_description']} | {labels['col_technologies']} | {labels['col_period']} |"
            )
            index_lines.append("|---|---|---|---|")
            for row in rows:
                entry = row["entry"]
                description = ((entry.get("descrizione") or {}).get(lang) or row["gh_description"]).replace("|", "/")
                technologies = (entry.get("tecnologie") or "").replace("|", "/")
                period = format_period(lang, entry) or ""
                index_lines.append(
                    f"| [{row['title']}]({row['slug']}.md) | {description} | {technologies} | {period} |"
                )
            index_lines.append("")
        index_path = PERSONAL_DIR / f"index{LANG_SUFFIX[lang]}.md"
        index_path.write_text("\n".join(index_lines).rstrip() + "\n", encoding="utf-8")
    print(f"[update_personal_projects] Aggiornati gli index (it/en/es) con {len(index_rows)} progetti.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
