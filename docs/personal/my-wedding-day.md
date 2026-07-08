# my-wedding-day

Customized wedding planner app

- **Repository**: [alesop95/my-wedding-day](https://github.com/alesop95/my-wedding-day)
- **Linguaggio principale**: TypeScript
- **Ultimo aggiornamento**: 2026-07-07
- **Cartella locale**: `my-wedding-day`

Un'applicazione single-page in React 18 e TypeScript costruita per gestire la logistica lato invitati di un matrimonio reale, distribuita come sito statico su Firebase Hosting con Firestore e Cloud Functions come backend, invece di un server dedicato. Gli invitati navigano attraverso sezioni dedicate per la conferma di partecipazione (RSVP), le informazioni su hotel e location, il programma della serata, una lista regali, un guestbook collaborativo, la condivisione di foto, e una funzionalità di playlist/suggerimento canzoni che si integra con l'API Spotify tramite uno script di setup OAuth dedicato. Un'area di amministrazione protetta da password, separata dall'app lato invitati, copre la gestione della lista invitati con raggruppamento per famiglie, l'assegnazione di tavoli/posti al ristorante, la modifica del menu, la moderazione delle voci del guestbook e dei suggerimenti musicali, il tracciamento dei fornitori e una vista di reportistica, mentre le Cloud Functions gestiscono gli aspetti lato server come l'autenticazione dello staff, i promemoria email RSVP pianificati e gli script di pulizia e migrazione dei record degli invitati.

Dal punto di vista tecnico, l'app privilegia un modello di stato basato su atomi con Jotai rispetto a Redux o Context, fp-ts per la gestione degli errori in stile Option/Either, e Framer Motion insieme a Lottie per l'header animato e le transizioni; i template email sono scritti in MJML e compilati in TypeScript in fase di build invece che renderizzati a runtime. La documentazione stessa del progetto fissa questo stack in modo deliberato (escludendo esplicitamente Next.js, Redux, Tailwind e alternative simili), indicando una costruzione ponderata e da zero piuttosto che una demo assemblata rapidamente, anche se il suo ambito è un singolo evento reale piuttosto che un prodotto riutilizzabile.
