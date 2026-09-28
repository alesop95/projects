# legal-consultant

Local-first project to navigate through Italian legislation with a simple MCP server

- **Repositorio**: [alesop95/legal-consultant](https://github.com/alesop95/legal-consultant)
- **Tecnologías**: Python, server MCP, SQLite FTS5 (BM25), Claude Desktop, API Open Data di Normattiva
- **Periodo**: 06/2026 - 08/2026, en pausa

Un servidor MCP (Model Context Protocol) local que convierte Claude Desktop en un asistente de investigación sobre derecho italiano. El razonamiento ocurre en Claude Desktop con la suscripción existente, sin API de pago por uso, y el servidor expone tres herramientas: la búsqueda de texto completo BM25 sobre SQLite FTS5 con extractos citables, la lectura del texto íntegro de un artículo por URN y la información sobre el corpus. No hacen falta GPU ni embeddings. Un instalador de Windows de un solo clic prepara git y uv, construye el índice, registra el servidor en Claude Desktop y programa la actualización diaria de los datos.

El corpus parte de un clon local del proyecto italia-corpus, completado con los códigos civil, penal y de procedimiento civil descargados de Normattiva. Una auditoría de julio de 2026 midió que al clon le faltaban 9.313 de las 13.730 leyes ordinarias no derogadas, 1.584 de los 1.636 decretos-ley y la Constitución, porque refleja solo las colecciones predefinidas de Normattiva. Las lagunas se cubren ahora desde la API Open Data oficial de Normattiva, con una exportación masiva en Akoma Ntoso repartida en varios días, y un control de completitud señala los actos que siguen ausentes. A finales de julio el código penal se actualizó a la vigencia tras la sentencia constitucional 108/2026.

En agosto una auditoría por materia sobre la compraventa de vivienda verificó diecisiete actos: de las tres lagunas encontradas se cubrieron dos, mientras que la tercera, la ley 448/1998, no la devuelve la fuente y sigue declarada como ausente. La integración de la jurisprudencia se ha evaluado en un estudio de viabilidad y no está implementada. Es una herramienta informativa y no asesoramiento legal, y la búsqueda léxica no garantiza que un artículo esté vigente sin comprobarlo en Normattiva.
