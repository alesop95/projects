# harmony-book

The technical under the hood of my book writing

- **Repositorio**: [alesop95/harmony-book](https://github.com/alesop95/harmony-book)
- **Lenguajes**: PowerShell, Shell, Python, JavaScript
- **Fecha de inicio**: 2026-06
- **Última actualización**: 2026-07-06
- **Carpeta local**: `harmony-book`

Este repositorio no es un proyecto de software sino la cadena de herramientas de publicación para un libro de armonía occidental (teoría musical): versiona el método tipográfico y el pipeline de compilación, no el manuscrito en sí. La composición usa LuaLaTeX con la clase memoir para Unicode y fuentes OpenType nativas, LilyPond incorporado mediante lilypond-book para los ejemplos musicales, biblatex/biber para la bibliografía e imakeidx/glossaries para el índice y el glosario; todo el entorno TeX es una instalación de TinyTeX reproducible y local al usuario, descrita mediante un manifiesto de paquetes, de modo que la compilación es portable entre Windows y Linux.

Los capítulos reales, los ejemplos musicales y la bibliografía del libro viven en una carpeta `manuscript/` deliberadamente incluida en gitignore y mantenida fuera de este repositorio público, ya que ese contenido está destinado a la venta y no a la publicación; aquí solo se incluye un documento mínimo `sample/` para demostrar que la cadena de compilación funciona de extremo a extremo. Lo que es público, en otras palabras, es la estructura reutilizable, las macros y los scripts de compilación para autopublicar un libro fuertemente maquetado y denso en notación musical con LaTeX, no el texto terminado.
