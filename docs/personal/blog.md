# blog

_Nessuna descrizione su GitHub._

- **Repository**: [alesop95/blog](https://github.com/alesop95/blog)
- **Linguaggio principale**: TypeScript
- **Ultimo aggiornamento**: 2026-07-06
- **Cartella locale**: `blog-alessio`

Questo è il blog personale e la piattaforma di scrittura di Alessio Sopranzi: un sito statico bilingue (inglese/italiano) costruito a mano su Next.js 16, React 19 e Tailwind v4, esportato staticamente e distribuito su GitHub Pages tramite GitHub Actions. I contenuti sono basati su file piuttosto che su un CMS: ogni articolo è un file MDX sotto content/posts/{en,it}/, con le coppie tradotte collegate tramite un campo condiviso articleId nel frontmatter e segmenti di URL specifici per lingua (per esempio /en/posts/x contro /it/articoli/x).

Oltre alla pipeline di scrittura, il progetto ha una dotazione di strumenti sorprendentemente completa per un blog personale: generazione di immagini Open Graph in fase di build con Satori, ricerca full-text tramite Pagefind, KaTeX per la matematica e Shiki per l'evidenziazione del codice, un'integrazione con abcjs per la notazione musicale, e una pipeline di verifica che combina TypeScript, lint/formattazione con Biome, test unitari con Vitest, test end-to-end con Playwright comprensivi di controlli di accessibilità tramite axe-core, e Lighthouse CI. Gli architecture decision record del progetto documentano perché sia stata scelta la modalità project-site di GitHub Pages invece di un dominio personalizzato, a suggerire un impianto di pubblicazione deliberatamente documentato e a bassa manutenzione, più che un esperimento in corso.
