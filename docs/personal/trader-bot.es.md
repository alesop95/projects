# trader-bot

- **Repositorio**: [alesop95/trader-bot](https://github.com/alesop95/trader-bot)
- **Tecnologías**: Python, vectorbt, Docker, IB Gateway, PostgreSQL, Prometheus, Grafana
- **Periodo**: 06/2026, en pausa

Un bot de trading algorítmico para Interactive Brokers, construido sobre `ib-async` y sobre un patrón de estrategia de seis interfaces (filtro del universo, generador de señales, dimensionamiento de posiciones, asignador de cartera, algoritmo de ejecución, lógica de salida) ensambladas por un composer, de modo que una nueva estrategia implemente solo esos roles. La única estrategia conectada entra con un cruce alcista EMA9/EMA21 confirmado por el RSI y el histograma MACD, dimensiona cada posición como fracción fija del capital de la estrategia, omite los símbolos que van a ex-dividendo dentro de una ventana configurable, ejecuta con órdenes limit ligeramente agresivas y sale con un cruce bajista o con un umbral de drawdown desde el máximo de sesión de la posición. Alrededor del núcleo hay un circuit breaker y un risk manager, jobs de APScheduler para las ventanas de sesión europea y estadounidense, notificaciones de Telegram, métricas de Prometheus con un endpoint de health check y persistencia en PostgreSQL con SQLAlchemy y migraciones de Alembic.

La arquitectura usa inyección de dependencias y mantiene la librería de backtesting (vectorbt) fuera del contenedor de producción. El código está completo, con 40 pruebas unitarias, un stack Docker con IB Gateway, PostgreSQL, Prometheus y Grafana y un workflow de despliegue por SSH. La fase operativa, que prevé un periodo de paper trading antes del uso real, está planificada, pero el bot todavía no se ha puesto en funcionamiento y por eso no hay resultados de trading.
