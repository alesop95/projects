# trader-bot

_Nessuna descrizione su GitHub._

- **Repository**: [alesop95/trader-bot](https://github.com/alesop95/trader-bot)
- **Linguaggi**: Python, PowerShell, Shell, JavaScript
- **Data di inizio**: 2026-06
- **Ultimo aggiornamento**: 2026-07-06
- **Cartella locale**: `trader-bot`

Un bot di trading algoritmico per Interactive Brokers, costruito attorno a `ib-async` e a un pulito pattern di strategia a sei interfacce (filtro dell'universo, generatore di segnali, dimensionamento delle posizioni, allocatore di portafoglio, algoritmo di esecuzione, logica di uscita) assemblate da un composer, cosi' che una nuova strategia debba implementare solo quei ruoli. L'unica strategia attualmente collegata opera su un incrocio rialzista EMA9/EMA21 confermato da RSI e istogramma MACD, dimensiona ogni posizione come frazione fissa del capitale della strategia, salta i simboli che vanno ex-dividendo entro una finestra configurabile, esegue tramite ordini limit leggermente aggressivi, ed esce sia su un incrocio ribassista sia su una soglia di drawdown dal picco di sessione della posizione. Attorno a questo nucleo si trovano un circuit breaker e un risk manager, un job guidato da APScheduler per finestre di sessione separate EU e US, notifiche Telegram, metriche Prometheus e un endpoint di health-check, e persistenza PostgreSQL tramite SQLAlchemy e migrazioni Alembic.

Il progetto si presenta come un pezzo di infrastruttura di trading effettivamente sviluppato, non uno script giocattolo, con un'architettura reale a dependency injection e una dipendenza di backtesting solo per lo sviluppo (vectorbt) tenuta fuori dal container di produzione. Nel codice non sono state trovate credenziali ne' dati di account; la descrizione qui sopra copre solo la strategia e l'architettura di sistema, non risultati di trading dal vivo, che non sono presenti nel repository.
