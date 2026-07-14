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
3. Per ciascun repository trovato, interroga l'API REST di GitHub (nessuna scrittura, solo
   lettura di dati gia' pubblici) per metadati, la ripartizione dei linguaggi (endpoint
   /languages, non solo il singolo linguaggio dominante di /repos) e un estratto del README.
   Legge anche la data del primo commit locale (git log sulla cartella sotto --source) come
   approssimazione della data di inizio del progetto: richiesta esplicita dell'utente
   (2026-07-09), a differenza dei progetti aziendali dove questa euristica si e' rivelata
   inaffidabile (vedi ARCHITECTURE.md) e le date restano corrette a mano.
4. Genera tre pagine Markdown per progetto (docs/personal/<slug>.md per l'italiano,
   <slug>.en.md per l'inglese, <slug>.es.md per lo spagnolo, secondo la struttura a suffisso di
   mkdocs-static-i18n) e rigenera i tre index.md/index.en.md/index.es.md con la tabella
   riassuntiva nella lingua corrispondente. Non tocca docs/company/.
5. Se esiste data/personal_overrides/<slug>.<lang>.md, il suo contenuto sostituisce l'estratto
   README nella pagina generata di quella lingua: e' li' che vive il testo lungo scritto a mano
   (o da un agente a partire dal codice reale), perche' sopravviva alle rigenerazioni di questo
   script. Se manca la traduzione in una lingua, si ripiega sulla versione inglese (la lingua in
   cui questi override sono stati scritti per la prima volta) invece di lasciare la pagina vuota.
   La descrizione breve e i topics, che arrivano da GitHub, non vengono tradotti: sono citazioni
   dirette di un campo esterno, non prosa di questo sito.

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
    "my-cv", "skills", "projects", "template-claude-developing", "lettore-doc", "prova",
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
    "local-audio-transcriptor": "ai_agents",
    "spanish-learning": "ai_agents",
    # Sicurezza e infrastruttura self-hosted.
    "home-lab-cybersec-networking": "security_infra",
    "pw-manager": "security_infra",
    "telegram-drive-secure": "security_infra",
    # Finanza personale e automazione trading.
    "fiscal-toolkit": "finance_trading",
    "paypal-transaction-data": "finance_trading",
    "trader-bot": "finance_trading",
    # Hardware, embedded e personalizzazione dispositivi.
    "analog-to-digital-vhs-converter": "hardware_embedded",
    "gps-time-synchronization-arduino-stm32": "hardware_embedded",
    "sony-xperia-1-iii-customization": "hardware_embedded",
    # Giochi, hobby e strumenti da collezione.
    "crosswords": "games_hobbies",
    "pok-collecting-update-collection": "games_hobbies",
    "pok-competitive-teambuilder": "games_hobbies",
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

LANGS = ("it", "en", "es")
# "it" e' la lingua di default nella struttura a suffisso di mkdocs-static-i18n: i suoi file
# non hanno suffisso (<slug>.md), le altre due lingue si scrivono come <slug>.en.md/<slug>.es.md.
LANG_SUFFIX = {"it": "", "en": ".en", "es": ".es"}

LABELS = {
    "it": {
        "no_description": "_Nessuna descrizione su GitHub._",
        "fork_note": "personalizzazione/estensione, non codebase originale",
        "fork_of": "Fork di",
        "repository": "Repository",
        "languages": "Linguaggi",
        "topics": "Topics",
        "start_date": "Data di inizio",
        "updated": "Ultimo aggiornamento",
        "local_folder": "Cartella locale",
        "from_readme": "Dal README",
        "index_title": "Personal projects",
        "index_intro": (
            "Generata automaticamente da `scripts/update_personal_projects.py` a partire dai "
            "repository GitHub pubblici collegati alle cartelle progetto locali. Non modificare "
            "questo file a mano: verra' sovrascritto alla prossima esecuzione dello script."
        ),
        "col_project": "Progetto",
        "col_description": "Descrizione",
        "col_language": "Linguaggi",
        "col_updated": "Aggiornato",
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
        "no_description": "_No description on GitHub._",
        "fork_note": "customization/extension, not the original codebase",
        "fork_of": "Fork of",
        "repository": "Repository",
        "languages": "Languages",
        "topics": "Topics",
        "start_date": "Start date",
        "updated": "Last updated",
        "local_folder": "Local folder",
        "from_readme": "From the README",
        "index_title": "Personal projects",
        "index_intro": (
            "Automatically generated by `scripts/update_personal_projects.py` from the public "
            "GitHub repositories linked to the local project folders. Do not edit this file by "
            "hand: it gets overwritten on the next run of the script."
        ),
        "col_project": "Project",
        "col_description": "Description",
        "col_language": "Languages",
        "col_updated": "Updated",
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
        "no_description": "_Sin descripción en GitHub._",
        "fork_note": "personalización/extensión, no el código original",
        "fork_of": "Fork de",
        "repository": "Repositorio",
        "languages": "Lenguajes",
        "topics": "Topics",
        "start_date": "Fecha de inicio",
        "updated": "Última actualización",
        "local_folder": "Carpeta local",
        "from_readme": "Del README",
        "index_title": "Personal projects",
        "index_intro": (
            "Generada automáticamente por `scripts/update_personal_projects.py` a partir de los "
            "repositorios públicos de GitHub asociados a las carpetas de proyecto locales. No "
            "modificar este archivo a mano: se sobrescribe en la siguiente ejecución del script."
        ),
        "col_project": "Proyecto",
        "col_description": "Descripción",
        "col_language": "Lenguajes",
        "col_updated": "Actualizado",
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


def format_languages(languages, max_count=4):
    """languages e' il dict {nome: byte} dell'endpoint /repos/{owner}/{repo}/languages.
    A differenza del singolo 'language' dominante di /repos, questo riflette davvero tutti i
    linguaggi usati: restituisce i primi max_count per byte, separati da virgola."""
    if not languages:
        return None
    ranked = sorted(languages.items(), key=lambda kv: kv[1], reverse=True)
    return ", ".join(name for name, _ in ranked[:max_count])


def git_first_commit_date(folder):
    """Approssima la data di inizio del progetto con la data del primo commit locale. Richiesta
    esplicita dell'utente per i progetti personali (2026-07-09): a differenza dei progetti
    aziendali, dove questa euristica si e' rivelata inaffidabile (il tracciamento git spesso
    inizia molto dopo il lavoro reale, vedi ARCHITECTURE.md), per i repository personali il primo
    commit e' in genere anche l'inizio effettivo del progetto."""
    try:
        roots = subprocess.run(
            ["git", "-C", str(folder), "rev-list", "--max-parents=0", "HEAD"],
            capture_output=True, text=True, timeout=10,
        )
        if roots.returncode != 0 or not roots.stdout.strip():
            return None
        root_hash = roots.stdout.strip().splitlines()[0]
        date_result = subprocess.run(
            ["git", "-C", str(folder), "log", "-1", "--format=%ad", "--date=format:%Y-%m", root_hash],
            capture_output=True, text=True, timeout=10,
        )
        if date_result.returncode != 0:
            return None
        return date_result.stdout.strip() or None
    except (subprocess.TimeoutExpired, OSError):
        return None


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


def build_project_page(lang, folder_name, owner, repo, meta, languages_str, start_date, readme_excerpt, override_text):
    labels = LABELS[lang]
    lines = [f"# {meta.get('name', repo)}", ""]
    if meta.get("fork"):
        parent = meta.get("parent", {})
        parent_full = parent.get("full_name", "sconosciuto")
        lines.append(
            f"> {labels['fork_of']} [{parent_full}](https://github.com/{parent_full}): {labels['fork_note']}."
        )
        lines.append("")
    description = meta.get("description") or labels["no_description"]
    lines.append(description)
    lines.append("")
    lines.append(f"- **{labels['repository']}**: [{owner}/{repo}]({meta.get('html_url')})")
    if languages_str:
        lines.append(f"- **{labels['languages']}**: {languages_str}")
    if meta.get("topics"):
        lines.append(f"- **{labels['topics']}**: {', '.join(meta['topics'])}")
    if start_date:
        lines.append(f"- **{labels['start_date']}**: {start_date}")
    if meta.get("pushed_at"):
        lines.append(f"- **{labels['updated']}**: {meta['pushed_at'][:10]}")
    lines.append(f"- **{labels['local_folder']}**: `{folder_name}`")
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

    for folder_name, owner, repo in projects:
        meta = github_request(f"{API_ROOT}/repos/{owner}/{repo}", args.token)
        if meta is None:
            print(f"  SKIP  {folder_name} -> {owner}/{repo} (non trovato su GitHub, forse privato)")
            continue
        default_branch = meta.get("default_branch", "main")
        readme_raw = github_raw(f"https://raw.githubusercontent.com/{owner}/{repo}/{default_branch}/README.md")
        excerpt = extract_readme_excerpt(readme_raw)
        languages = github_request(f"{API_ROOT}/repos/{owner}/{repo}/languages", args.token)
        languages_str = format_languages(languages) or meta.get("language") or "-"
        start_date = git_first_commit_date(Path(args.source) / folder_name)

        slug = slugify(repo)
        for lang in LANGS:
            override_text = load_override(slug, lang)
            page_path = PERSONAL_DIR / f"{slug}{LANG_SUFFIX[lang]}.md"
            page_path.write_text(
                build_project_page(lang, folder_name, owner, repo, meta, languages_str, start_date, excerpt, override_text),
                encoding="utf-8",
            )
            generated_files.add(page_path.name)
        print(f"  OK    {folder_name} -> {slug}.md (it/en/es)")

        category = PROJECT_CATEGORIES.get(slug)
        if category is None:
            category = "uncategorized"
            print(
                f"  WARN  {slug} non e' presente in PROJECT_CATEGORIES: assegnato a "
                f"'uncategorized', aggiungere la voce nello script.",
                file=sys.stderr,
            )
        index_rows.append({
            "title": meta.get("name", repo),
            "slug": slug,
            "description": (meta.get("description") or "").replace("|", "/"),
            "language": languages_str,
            "updated": (meta.get("pushed_at") or "")[:10],
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

    # Raggruppa per categoria secondo CATEGORY_ORDER; dentro ogni gruppo l'ordinamento resta per
    # data di aggiornamento decrescente, come nella tabella piatta precedente. Un gruppo senza
    # righe (es. nessun progetto scoperto in questa corsa ricade in "uncategorized") non produce
    # un'intestazione vuota nell'index.
    rows_by_category = {key: [] for key in CATEGORY_ORDER}
    for row in index_rows:
        rows_by_category.setdefault(row["category"], []).append(row)
    for rows in rows_by_category.values():
        rows.sort(key=lambda row: row["updated"], reverse=True)

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
                f"| {labels['col_project']} | {labels['col_description']} | {labels['col_language']} | {labels['col_updated']} |"
            )
            index_lines.append("|---|---|---|---|")
            for row in rows:
                index_lines.append(
                    f"| [{row['title']}]({row['slug']}.md) | {row['description']} | {row['language']} | {row['updated']} |"
                )
            index_lines.append("")
        index_path = PERSONAL_DIR / f"index{LANG_SUFFIX[lang]}.md"
        index_path.write_text("\n".join(index_lines).rstrip() + "\n", encoding="utf-8")
    print(f"[update_personal_projects] Aggiornati gli index (it/en/es) con {len(index_rows)} progetti.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
