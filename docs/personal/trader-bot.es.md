# trader-bot

_Sin descripción en GitHub._

- **Repositorio**: [alesop95/trader-bot](https://github.com/alesop95/trader-bot)
- **Lenguaje principal**: Python
- **Última actualización**: 2026-07-06
- **Carpeta local**: `trader-bot`

Un bot de trading algorítmico para Interactive Brokers, construido en torno a `ib-async` y un patrón de estrategia limpio de seis interfaces (filtro de universo, generador de señales, dimensionamiento de posiciones, asignador de cartera, algoritmo de ejecución, lógica de salida) ensambladas por un composer, de modo que una nueva estrategia solo tiene que implementar esos roles. La única estrategia actualmente conectada opera sobre un cruce alcista EMA9/EMA21 confirmado por RSI e histograma MACD, dimensiona cada posición como una fracción fija del capital de la estrategia, omite los símbolos que van a ex-dividendo dentro de una ventana configurable, ejecuta mediante órdenes limit ligeramente agresivas, y sale ya sea por un cruce bajista o por un umbral de drawdown desde el pico de sesión de la posición. Alrededor de ese núcleo hay un circuit breaker y un risk manager, un job impulsado por APScheduler para ventanas de sesión separadas de la UE y EE. UU., notificaciones de Telegram, métricas de Prometheus y un endpoint de health-check, y persistencia en PostgreSQL mediante SQLAlchemy y migraciones de Alembic.

El proyecto se lee como una pieza de infraestructura de trading genuinamente desarrollada y no como un script de juguete, con una arquitectura real de inyección de dependencias y una dependencia de backtesting solo para desarrollo (vectorbt) mantenida fuera del contenedor de producción. No se encontraron credenciales ni datos de cuenta en el código; la descripción anterior cubre solo la estrategia y la arquitectura del sistema, no resultados de trading en vivo, que no están presentes en el repositorio.
