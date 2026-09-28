# spanish-learning

- **Repositorio**: [alesop95/spanish-learning](https://github.com/alesop95/spanish-learning)
- **Tecnologías**: Claude Code, Anki, base di conoscenza locale
- **Periodo**: 07/2026, en pausa

Un sistema agéntico de tutoría de español construido sobre Claude Code, sin una aplicación propia. El trabajo se divide en tres capas desacopladas: una base de conocimiento local ensamblada por un script de ingesta de coste LLM cero, que recorre una biblioteca personal de libros y documentos (PDF, DOCX, PPTX, XLSX, HTML, con OCR para los volúmenes escaneados) y produce una caché en Markdown con un índice por documento; un motor de repetición espaciada pensado para funcionar a través del puente `ankimcp/anki-mcp-server` hacia una instalación local de Anki; y tres subagentes de Claude, tutor, kb-retriever y examiner, conectados a comandos slash que construyen una hoja de ruta pedagógica, imparten lecciones basadas solo en material de origen citado y cierran cada sesión con una verificación de recuerdo activo antes de marcar un módulo como completado.

La base de conocimiento está construida y la primera lección, sobre saludos y presentaciones, se ha impartido y consolidado en dos pasadas con la verificación final del examiner. La segunda lección, sobre los falsos amigos italiano-español, está preparada pero no impartida, y la conexión en vivo con Anki todavía no está activa.
