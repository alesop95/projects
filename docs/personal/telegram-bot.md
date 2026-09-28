# telegram-bot

- **Repository**: [alesop95/telegram-bot](https://github.com/alesop95/telegram-bot)
- **Tecnologie**: Python, API Bot di Telegram
- **Periodo**: 09/2025 - 06/2026, fermo

Un bot Telegram costruito su python-telegram-bot con due backend di persistenza, SQLite per le esecuzioni locali e PostgreSQL per il deployment cloud, scelti tramite entry point separati (`main.py` e `main_cloud.py`) invece di uno switch a runtime. Offre messaggi personalizzati formattati con bottoni inline, template riutilizzabili, cinque temi di chat selezionabili, impostazioni per utente (notifiche, lingua, fuso orario) e statistiche d'uso personali e per l'amministratore, con l'obiettivo di replicare una parte delle funzioni di personalizzazione di Telegram Premium senza abbonamento. Include un piccolo endpoint di health check, file Docker e docker-compose, configurazioni di deployment per Railway e Render e un workflow GitHub Actions.

La programmazione dei messaggi è indicata dal bot stesso come in sviluppo, quindi il set di funzioni del README è attivo solo in parte. Handler, accesso al database e configurazione sono separati.
