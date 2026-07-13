# discoteca-api

_Nessuna descrizione su GitHub._

- **Repository**: [alesop95/discoteca-api](https://github.com/alesop95/discoteca-api)
- **Linguaggi**: PowerShell, Shell, Python, TypeScript
- **Data di inizio**: 2025-05
- **Ultimo aggiornamento**: 2026-07-06
- **Cartella locale**: `discoteca-api`

Un piccolo backend TypeScript, costruito con Express 5 e Prisma su SQLite, per una lista ospiti in stile discoteca: un unico endpoint POST accetta nome ed email, crea o riutilizza un record User indicizzato per email, genera un'immagine con codice QR che codifica id, nome ed email dell'utente, e la invia via email all'ospite tramite Nodemailer, in modo che possa essere scansionata all'ingresso. L'input è validato con Zod. Il modello dati è volutamente minimale, un'unica tabella User senza ruoli, eventi o gestione della capienza, ed esiste un frontend complementare in Vite e React che consiste in poco più di un componente di form di registrazione che chiama l'API.

Si presenta come un progetto personale in fase iniziale piuttosto che come un sistema in produzione: non ci sono test automatizzati, lo schema non versiona eventi o liste ospiti al di là della tabella utenti piatta, e le note stesse del repository menzionano che node_modules era stato commesso per errore ed è stato aggiunto a gitignore solo di recente. È una prova di concetto funzionante per l'idea di lista ospiti con codice QR, non un servizio consolidato.
