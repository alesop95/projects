# blog

- **Repository**: [alesop95/blog](https://github.com/alesop95/blog)
- **Tecnologie**: Next.js 16, React 19, Tailwind 4, MDX
- **Periodo**: 05/2026 - in corso

Blog personale bilingue (inglese e italiano), costruito a mano su Next.js 16, React 19 e Tailwind 4, esportato come sito statico e pubblicato su GitHub Pages con GitHub Actions all'indirizzo [alesop95.github.io/blog](https://alesop95.github.io/blog). Ogni articolo è un file MDX in `content/posts/{en,it}/`; le due traduzioni sono collegate da un campo `articleId` nel frontmatter e hanno URL propri per lingua.

Il sito genera in fase di build le immagini Open Graph (Satori) e l'indice di ricerca (Pagefind), usa KaTeX per la matematica, Shiki per il codice e abcjs per gli spartiti, e ha componenti interattivi per armonia ed equalizzazione, commenti Giscus, newsletter Buttondown, le pagine `/uses` e `/now` e pagine per argomento. La verifica combina TypeScript, Biome, Vitest, Playwright con controlli di accessibilità axe-core e Lighthouse CI. Le decisioni di impianto sono registrate come ADR, fra cui la pubblicazione come project site invece che su dominio proprio.
