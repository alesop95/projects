# pok--competitive-teambuilder

A customizable tool for building competitive teams for pokèmon champions

- **Repository**: [alesop95/pok--competitive-teambuilder](https://github.com/alesop95/pok--competitive-teambuilder)
- **Linguaggi**: TypeScript, PowerShell, Shell, Python
- **Data di inizio**: 2026-06
- **Ultimo aggiornamento**: 2026-07-06
- **Cartella locale**: `pokè-competitive-teambuilder`

Uno strumento locale in Node.js e TypeScript che genera proposte di squadre Pokémon competitive per il formato Pokémon Champions, a partire dal roster disponibile in una stagione. Ragiona sulla composizione della squadra tramite tagging e scoring deterministici, non tramite simulazione di combattimento: i ruoli vengono dedotti da statistiche, abilità e movepool, i Pokémon candidati vengono valutati per sinergia e copertura dei tipi rispetto ai metadati correnti, e l'output include una motivazione, le debolezze previste e i probabili counter per ciascuna squadra proposta. I dati di gioco, la tabella dei tipi e i calcoli del danno provengono dall'ecosistema open-source Pokémon Showdown (`@pkmn/dex`, `@smogon/calc`), e le regole specifiche del formato derivano dalla mod Champions mantenuta dalla community di Showdown.

Il design tiene separati la logica di gioco e i dati di stagione, così che una nuova stagione possa essere supportata aggiornando i file di dati JSON/YAML senza toccare il codice del motore. Un backend Fastify serve sia una modalità CLI di generazione report sia una piccola interfaccia web; un secondo livello opzionale può arricchire il testo della motivazione tramite la API di Claude quando è configurata una chiave, ricadendo altrimenti sul testo deterministico offline. Secondo la sua stessa roadmap il progetto è ancora in una fase iniziale: lo scaffold, gli strumenti per il roster e il motore principale sono a posto, mentre l'interfaccia web e uno scoring del calcolo danni raffinato sono esplicitamente segnati come non completati.
