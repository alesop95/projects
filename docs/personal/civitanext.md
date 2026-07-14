# civitanext

_Nessuna descrizione su GitHub._

- **Repository**: [alesop95/civitanext](https://github.com/alesop95/civitanext)
- **Linguaggi**: JavaScript, HTML, PowerShell, Shell
- **Data di inizio**: 2026-07
- **Ultimo aggiornamento**: 2026-07-14
- **Cartella locale**: `civitanext`

CivitaNext è la piattaforma di partecipazione civica pensata per i giovani residenti di Civitanova Marche: un calendario eventi, quiz civici, un forum di discussione, proposte con voto, un profilo utente con tessera digitale, un pannello di amministrazione e sezioni di comunità e città come il mentoring, una mappa degli spazi civici e un archivio documentale. Il repository ha attraversato due fasi distinte: prima una consegna di design ad alta fedeltà (il prototipo in `design_handoff_civitanext/`), poi, a partire dalla Fase 0 di sviluppo, la ricostruzione reale in Next.js alla radice del repository stesso.

Il codice alla radice è un'applicazione Next.js 16 (React 19, TypeScript) vera, non un mockup: i token visivi e i componenti base del design system (Logo, Waves, Starburst, Chip, Btn, Tag, Avatar) sono stati riportati dal prototipo dentro il codice dell'app, e la homepage li mostra come vetrina, dichiarando esplicitamente di non avere ancora nessuna feature collegata al database. In parallelo esiste già lo schema dati reale (Prisma, target PostgreSQL): utenti con ruolo e tesseramento opzionale, autenticazione via NextAuth con sessioni JWT, eventi, forum a thread, proposte con voto e un modello di voto polimorfico condiviso tra sondaggi, thread e proposte. In sintesi: fondamenta di design system e schema dati sono reali e in repository, ma nessuna funzionalità è ancora cablata a dati veri. Il prototipo di design originale resta in repository come riferimento di sola lettura, non codice di produzione.
