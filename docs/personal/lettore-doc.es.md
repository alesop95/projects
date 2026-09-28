# lettore-doc

- **Repositorio**: [alesop95/lettore-doc](https://github.com/alesop95/lettore-doc)
- **Tecnologías**: Python, PowerShell, graphify, MkDocs
- **Periodo**: 05/2026 - en curso

Pipeline que lee documentación técnica local en formato .docx, .txt y .md y obtiene de ella dos productos independientes. El primero es un vault de Obsidian privado, con una nota por documento, un grafo ponderado de relaciones y resúmenes narrativos, que no sale de la máquina. El segundo alimenta la taxonomía pública de competencias, publicada como sitio MkDocs en GitHub Pages: de los documentos se extraen nodos de evidencia, se clasifican frente a las páginas de competencia existentes y se inserta un bloque de evidencia anonimizado en la página adecuada, sin publicar nunca los documentos.

El trabajo determinista lo hacen scripts de Python: parsing a niveles de detalle crecientes, extracción de entidades con regex y NER local de spaCy, construcción del grafo, clasificación de los nodos y exportación al sitio. En el flujo hacia el sitio el único paso interactivo, y el único que consume tokens, es la extracción del grafo de conocimiento con graphify dentro de Claude Code. Antes de graphify un control previo neutraliza los nombres de archivo que la herramienta descartaría en silencio, y antes de la exportación una compuerta obligatoria elimina del diff los restos de datos sensibles; el diff pasa de todos modos por una revisión humana.

A finales de julio de 2026 la taxonomía tenía ocho dominios, treinta y una páginas de competencia y 239 bloques de evidencia publicados. En septiembre empezó un nuevo ciclo de extracción, todavía en curso.
