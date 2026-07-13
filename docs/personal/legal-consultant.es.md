# legal-consultant

Local-first project to navigate through Italian legislation with a simple MCP server

- **Repositorio**: [alesop95/legal-consultant](https://github.com/alesop95/legal-consultant)
- **Lenguajes**: Python, PowerShell, Shell, JavaScript
- **Fecha de inicio**: 2026-06
- **Última actualización**: 2026-07-06
- **Carpeta local**: `legal-consultant`

Un servidor MCP (Model Context Protocol) local que convierte Claude Desktop en un asistente de investigación sobre derecho italiano sin ningún coste de API de pago por uso: todo el razonamiento ocurre en el propio Claude Desktop, que llama a las herramientas expuestas por este servidor, por lo que funciona sobre una suscripción de Claude existente en lugar de sobre un uso de API medido. El corpus jurídico es un clon local del proyecto `italia-corpus` mantenido por la comunidad, mantenido al día con `git pull` y reindexación incremental, más un puñado de códigos fundamentales (civil, penal, procedimiento civil) obtenidos directamente de Normattiva porque su texto completo falta en ese corpus. La búsqueda es deliberadamente ligera: búsqueda de texto completo BM25 sobre SQLite FTS5, sin GPU y sin embeddings, lo que mantiene la indexación rápida y permite ejecutar toda la herramienta en hardware ordinario.

Al modelo se le exponen tres herramientas: una búsqueda BM25 que devuelve extractos citables, una consulta que recupera el texto completo de un artículo dado mediante su URN, y una herramienta de corpus-info. Un instalador de Windows de un solo clic prepara git y uv, construye el índice, registra el servidor MCP en Claude Desktop y configura una tarea programada diaria para actualizar el corpus. El README deja explícito que se trata de una herramienta informativa, no de asesoramiento legal, y que la búsqueda léxica BM25 no puede garantizar que un artículo siga vigente sin comprobarlo directamente en Normattiva.
