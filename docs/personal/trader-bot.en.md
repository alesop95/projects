# trader-bot

- **Repository**: [alesop95/trader-bot](https://github.com/alesop95/trader-bot)
- **Technologies**: Python, vectorbt, Docker, IB Gateway, PostgreSQL, Prometheus, Grafana
- **Period**: 06/2026, paused

An algorithmic trading bot for Interactive Brokers, built on `ib-async` and on a six-interface strategy pattern (universe filter, signal generator, position sizer, portfolio allocator, execution algorithm, exit logic) assembled by a composer, so that a new strategy only implements those roles. The one strategy wired in enters on a bullish EMA9/EMA21 crossover confirmed by RSI and the MACD histogram, sizes each position as a fixed fraction of the strategy's capital, skips symbols going ex-dividend within a configurable window, executes with slightly aggressive limit orders, and exits on a bearish crossover or on a drawdown threshold from the position's session peak. Around the core sit a circuit breaker and a risk manager, APScheduler jobs for the European and US session windows, Telegram notifications, Prometheus metrics with a health-check endpoint, and PostgreSQL persistence with SQLAlchemy and Alembic migrations.

The architecture uses dependency injection and keeps the backtesting library (vectorbt) out of the production container. The code is complete, with 40 unit tests, a Docker stack with IB Gateway, PostgreSQL, Prometheus and Grafana, and a deploy workflow over SSH. The operational phase, which includes a paper-trading period before real use, is planned, but the bot has not been put into operation yet, so there are no trading results.
