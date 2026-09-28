# trader-bot

- **Repository**: [alesop95/trader-bot](https://github.com/alesop95/trader-bot)
- **Tecnologie**: Python, vectorbt, Docker, IB Gateway, PostgreSQL, Prometheus, Grafana
- **Periodo**: 06/2026, fermo

Un bot di trading algoritmico per Interactive Brokers, costruito su `ib-async` e su un pattern di strategia a sei interfacce (filtro dell'universo, generatore di segnali, dimensionamento delle posizioni, allocatore di portafoglio, algoritmo di esecuzione, logica di uscita) assemblate da un composer, così che una nuova strategia implementi solo quei ruoli. L'unica strategia collegata entra su un incrocio rialzista EMA9/EMA21 confermato da RSI e istogramma MACD, dimensiona ogni posizione come frazione fissa del capitale della strategia, salta i simboli che vanno ex-dividendo entro una finestra configurabile, esegue con ordini limit leggermente aggressivi ed esce su un incrocio ribassista o su una soglia di drawdown dal picco di sessione della posizione. Attorno al nucleo ci sono un circuit breaker e un risk manager, job APScheduler per le finestre di sessione europea e statunitense, notifiche Telegram, metriche Prometheus con un endpoint di health check e persistenza PostgreSQL con SQLAlchemy e migrazioni Alembic.

L'architettura usa la dependency injection e tiene la libreria di backtesting (vectorbt) fuori dal container di produzione. Il codice è completo, con 40 test unitari, uno stack Docker con IB Gateway, PostgreSQL, Prometheus e Grafana e un workflow di deploy via SSH. La fase operativa, che prevede un periodo di paper trading prima dell'uso reale, è pianificata, ma il bot non è ancora messo in esercizio e non ci sono quindi risultati di trading.
