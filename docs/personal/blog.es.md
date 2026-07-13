# blog

_Sin descripción en GitHub._

- **Repositorio**: [alesop95/blog](https://github.com/alesop95/blog)
- **Lenguajes**: TypeScript, PowerShell, Shell, Python
- **Fecha de inicio**: 2026-05
- **Última actualización**: 2026-07-06
- **Carpeta local**: `blog-alessio`

Este es el blog personal y la plataforma de escritura de Alessio Sopranzi: un sitio estático bilingüe (inglés/italiano) construido a mano sobre Next.js 16, React 19 y Tailwind v4, exportado de forma estática y desplegado en GitHub Pages mediante GitHub Actions. El contenido se basa en archivos en lugar de en un CMS: cada artículo es un archivo MDX bajo content/posts/{en,it}/, con los pares traducidos vinculados mediante un campo compartido articleId en el frontmatter y segmentos de URL específicos por idioma (por ejemplo /en/posts/x frente a /it/articoli/x).

Más allá del proceso de escritura, el proyecto cuenta con un conjunto de herramientas notablemente completo para un blog personal: generación de imágenes Open Graph en tiempo de build con Satori, búsqueda de texto completo mediante Pagefind, KaTeX para matemáticas y Shiki para resaltado de código, una integración con abcjs para notación musical, y un pipeline de verificación que combina TypeScript, lint/formato con Biome, pruebas unitarias con Vitest, pruebas end-to-end con Playwright con controles de accesibilidad mediante axe-core, y Lighthouse CI. Los propios architecture decision record del proyecto documentan por qué se eligió el modo project-site de GitHub Pages en lugar de un dominio personalizado, lo que sugiere una configuración de publicación deliberadamente documentada y de bajo mantenimiento, más que un experimento en curso.
