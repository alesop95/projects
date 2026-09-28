# template-claude-developing

A customized Claude code setup for starting a project from scratch (or.... boosting it!)

- **Repository**: [alesop95/template-claude-developing](https://github.com/alesop95/template-claude-developing)
- **Tecnologie**: Claude Code, Markdown, Python, PowerShell
- **Periodo**: 06/2026 - in corso

Sistema portabile di contesto, documentazione e version control per progetti sviluppati con Claude Code e Codex. Si installa nella cartella `.claude` di un progetto e fa in modo che lo stato resti recuperabile dal repository in ogni momento: la sessione di chat si perde alla chiusura, mentre memoria di progetto, schede tecniche e registro delle decisioni stanno su disco e si rileggono a ogni nuova sessione. Due prompt fissi lo istanziano su un progetto nuovo oppure lo applicano a posteriori a un progetto esistente, ricostruendo la memoria dalla storia dei commit senza riscriverla.

Ogni scheda tecnica porta un blocco di metadati che la ancora a un commit e ai percorsi del codice che descrive, e la skill `sync-context` confronta quei percorsi con lo stato attuale e propone aggiornamenti mirati invece di rigenerare i documenti. Attorno a questo nucleo ci sono regole modulari su stile, identità git, permessi, uso del contesto e affidabilità delle prove, strumenti Python per la convenzione Markdown e la tipografia italiana, e un catalogo di pacchetti opzionali diviso in dieci settori, che una skill propone in base ai settori riconosciuti nel progetto. Commit e push restano sempre manuali.

Il template è in sviluppo continuo da giugno 2026 ed è adottato da una trentina di repository personali, fra cui gran parte dei progetti descritti in questo sito; le correzioni nate in un progetto vengono generalizzate nel template e poi propagate agli altri.
