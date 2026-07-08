#!/usr/bin/env python3
"""Rileva quali cartelle progetto sotto D:\\ sono cambiate dall'ultima esecuzione.

Uso:
    python scripts/check_company_changes.py [--source D:\\]

Vincolo di riservatezza: questo script non legge e non pubblica MAI il contenuto dei file dei
progetti aziendali. Calcola solo un'impronta di metadati per ogni cartella (l'hash del commit
HEAD se e' un repository git, altrimenti una firma di nome+dimensione+data di modifica dei file
di primo livello) e la confronta con l'esecuzione precedente salvata in
data/company_manifest.json. Segnala quali cartelle sono nuove, cambiate o sparite: il testo
anonimizzato di ciascuna va poi scritto a mano in docs/company/, usando _template.md come guida.
Questo script non scrive mai in docs/company/.
"""
import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

EXCLUDE_NAMES = {
    "$RECYCLE.BIN", "System Volume Information", ".claude", ".pnpm-store",
}

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
MANIFEST_PATH = REPO_ROOT / "data" / "company_manifest.json"


def git_head_hash(folder):
    try:
        result = subprocess.run(
            ["git", "-C", str(folder), "rev-parse", "HEAD"],
            capture_output=True, text=True, timeout=10,
        )
    except (subprocess.TimeoutExpired, OSError):
        return None
    if result.returncode != 0:
        return None
    return result.stdout.strip()


def fallback_fingerprint(folder):
    """Firma di nome+dimensione+mtime dei soli file di primo livello, mai del contenuto."""
    digest = hashlib.sha256()
    try:
        entries = sorted(folder.iterdir(), key=lambda p: p.name)
    except OSError:
        return None
    for entry in entries:
        try:
            stat = entry.stat()
        except OSError:
            continue
        digest.update(f"{entry.name}:{stat.st_size}:{int(stat.st_mtime)}".encode("utf-8"))
    return digest.hexdigest()


def fingerprint_folder(folder):
    git_dir = folder / ".git"
    if git_dir.exists():
        head = git_head_hash(folder)
        if head:
            return f"git:{head}"
    fallback = fallback_fingerprint(folder)
    return f"meta:{fallback}" if fallback else None


def load_manifest():
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return {}


def save_manifest(manifest):
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", default=r"D:\\", help="Cartella da scandire (default D:\\)")
    args = parser.parse_args()

    source_dir = Path(args.source)
    if not source_dir.exists():
        print(f"[check_company_changes] Cartella non trovata: {source_dir}", file=sys.stderr)
        return 1

    previous = load_manifest()
    current = {}

    for entry in sorted(source_dir.iterdir()):
        if not entry.is_dir() or entry.name in EXCLUDE_NAMES or entry.name.startswith("[TBC]"):
            continue
        fingerprint = fingerprint_folder(entry)
        if fingerprint is None:
            continue
        current[entry.name] = fingerprint

    new_folders = sorted(set(current) - set(previous))
    removed_folders = sorted(set(previous) - set(current))
    changed_folders = sorted(
        name for name in (set(current) & set(previous))
        if current[name] != previous[name]
    )

    print("[check_company_changes] Confronto metadati D:\\ (nessun contenuto letto o pubblicato)")
    if new_folders:
        print(f"\nNuove cartelle ({len(new_folders)}): da valutare per una voce anonimizzata:")
        for name in new_folders:
            print(f"  + {name}")
    if changed_folders:
        print(f"\nCartelle cambiate dall'ultima esecuzione ({len(changed_folders)}): verificare se la voce va aggiornata:")
        for name in changed_folders:
            print(f"  ~ {name}")
    if removed_folders:
        print(f"\nCartelle non piu' presenti ({len(removed_folders)}):")
        for name in removed_folders:
            print(f"  - {name}")
    if not (new_folders or changed_folders or removed_folders):
        print("\nNessuna variazione rispetto all'ultima esecuzione.")

    save_manifest(current)
    print(f"\n[check_company_changes] Manifesto aggiornato: {MANIFEST_PATH.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
