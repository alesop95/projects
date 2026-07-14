# holiday-template

A free-customized interactive holiday tracker

- **Repository**: [alesop95/holiday-template](https://github.com/alesop95/holiday-template)
- **Linguaggi**: JavaScript, Python, HTML, PowerShell
- **Data di inizio**: 2026-06
- **Ultimo aggiornamento**: 2026-07-14
- **Cartella locale**: `holiday-template`

Un template riutilizzabile per costruire progressive web app di pianificazione viaggi condivisa, nato da un progetto reale di vacanza di coppia (un viaggio nel Cilento del 2026 vive sotto `trips/` come prima istanza). Il design separa deliberatamente uno shell HTML/JS canonico, che gestisce rendering, stato e collegamento a Firebase e non viene mai modificato per singolo viaggio, da un unico file `trip.config.js` per viaggio che contiene itinerario, lista ristoranti, marker sulla mappa e checklist. Ogni nuova vacanza si crea copiando lo shell in una nuova cartella sotto `trips/` e scrivendo solo quel file di configurazione, mentre tutti i viaggi condividono un unico progetto Firebase e sono separati in Firestore tramite un prefisso `TRIP_ID`, così la sincronizzazione in tempo reale della checklist tra i dispositivi di due persone continua a funzionare senza bisogno di configurare un backend per ogni viaggio.

Oltre al planner statico, il repository contiene anche `services/flight-search`, un piccolo servizio FastAPI documentato esplicitamente come uno scaffold iniziale piuttosto che una funzionalità completa: espone un unico endpoint di ricerca appoggiato a due adapter per i dati sui voli (uno scraper di Google Flights via `fast-flights` e le API Kiwi Tequila), senza ancora alcun livello di caching. Le note del progetto registrano che un terzo adapter, costruito sulle API Amadeus, era stato scritto, testato e poi rimosso deliberatamente dopo che Amadeus ha annunciato la chiusura del proprio portale sviluppatori self-service.
