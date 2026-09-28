# my-wedding-day

- **Repository**: privato, non consultabile
- **Tecnologie**: React 18, TypeScript, Firebase (Firestore, Authentication, Cloud Functions, Hosting)
- **Periodo**: 04/2026 - in corso

Applicazione web per organizzare un matrimonio reale, dalla conferma di partecipazione degli invitati fino alla serata. È una single page application in React 18 e TypeScript con backend interamente Firebase (Firestore, Authentication, Cloud Functions, Hosting), senza un server proprio. Gli invitati accedono con credenziali personali e trovano la conferma di partecipazione, le informazioni logistiche, il programma, la lista nozze, il guestbook, le proposte per la scaletta musicale e la condivisione delle foto. Da un pannello di amministrazione si gestiscono famiglie e invitati, disposizione dei tavoli, menù, fornitori e moderazione dei contenuti, e staff di sala, band e fotografo hanno ciascuno una vista dedicata.

Ogni sessione nasce da una Cloud Function di login che verifica le credenziali lato server e restituisce un token con il ruolo, letto dalle regole di sicurezza di Firestore. Lo stato è gestito con Jotai, gli errori con fp-ts, le email sono template MJML compilati in fase di build e l'interfaccia è in italiano e inglese. Il progetto ha una pipeline CI a quattro job, test end-to-end con Playwright su emulatori Firebase, monitoraggio con Sentry, rate limiting e App Check. Il codice è privato perché contiene dati reali, ed è prevista una repository pubblica con la sola documentazione tecnica, ripulita dai dati personali.
