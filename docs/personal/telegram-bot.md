# telegram-bot

_Nessuna descrizione su GitHub._

- **Repository**: [alesop95/telegram-bot](https://github.com/alesop95/telegram-bot)
- **Linguaggio principale**: Python
- **Ultimo aggiornamento**: 2026-07-06
- **Cartella locale**: `telegram-bot`

Un bot Telegram costruito su python-telegram-bot con un backend di persistenza duale, SQLite per le esecuzioni locali e PostgreSQL per il deployment cloud, selezionato tramite entry point separati (`main.py` contro `main_cloud.py`) invece di uno switch unico a runtime. Attorno al suo livello di handler offre messaggi personalizzati formattati con bottoni inline, template riutilizzabili, cinque temi di chat selezionabili, impostazioni per utente (notifiche, lingua, fuso orario), e statistiche d'uso sia personali sia rivolte all'amministratore, con l'obiettivo di replicare una fetta delle funzionalita' di personalizzazione di Telegram Premium senza l'abbonamento. Include un piccolo health endpoint in stile FastAPI, file Docker e docker-compose, e configurazioni di deployment per Railway e Render insieme a un workflow GitHub Actions.

La stessa lista dei comandi del bot segnala la consegna di messaggi programmati come ancora "in sviluppo", quindi l'insieme di funzionalita' descritto nel README e' solo parzialmente completo, non pienamente attivo. Dal punto di vista strutturale e' un bot semplice e monouso piuttosto che un framework: handler, gestori del database e configurazione sono nettamente separati, ma non esiste un sistema di plugin ne' un'orchestrazione multi-bot oltre a quanto offerto dai due entry point.
