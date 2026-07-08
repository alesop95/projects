# telegram-bot

_Sin descripción en GitHub._

- **Repositorio**: [alesop95/telegram-bot](https://github.com/alesop95/telegram-bot)
- **Lenguaje principal**: Python
- **Última actualización**: 2026-07-06
- **Carpeta local**: `telegram-bot`

Un bot de Telegram construido sobre python-telegram-bot con un backend de persistencia dual, SQLite para ejecuciones locales y PostgreSQL para el despliegue en la nube, seleccionado mediante puntos de entrada separados (`main.py` frente a `main_cloud.py`) en lugar de un único interruptor en tiempo de ejecución. Alrededor de su capa de handlers ofrece mensajes personalizados con formato y botones inline, plantillas reutilizables, cinco temas de chat seleccionables, ajustes por usuario (notificaciones, idioma, zona horaria), y estadísticas de uso tanto personales como orientadas al administrador, con el objetivo de replicar una parte de las funciones de personalización de Telegram Premium sin la suscripción. Incluye un pequeño endpoint de salud al estilo FastAPI, archivos de Docker y docker-compose, y configuraciones de despliegue para Railway y Render junto con un workflow de GitHub Actions.

La propia lista de comandos del bot marca la entrega de mensajes programados como todavía "en desarrollo", por lo que el conjunto de funciones descrito en su README está solo parcialmente completo y no plenamente activo. A nivel estructural es un bot sencillo y de propósito único más que un framework: los handlers, los gestores de base de datos y la configuración están claramente separados, pero no existe un sistema de plugins ni una orquestación multi-bot más allá de lo que ofrecen los dos puntos de entrada.
