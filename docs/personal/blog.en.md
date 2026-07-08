# blog

_No description on GitHub._

- **Repository**: [alesop95/blog](https://github.com/alesop95/blog)
- **Main language**: TypeScript
- **Last updated**: 2026-07-06
- **Local folder**: `blog-alessio`

This is Alessio Sopranzi's personal blog and writing platform: a hand-built, bilingual (English/Italian) static site on Next.js 16, React 19, and Tailwind v4, statically exported and deployed to GitHub Pages via GitHub Actions. Content is file-based rather than backed by a CMS: each post is an MDX file under content/posts/{en,it}/, with translated pairs linked through a shared articleId frontmatter field and locale-specific URL segments (for example /en/posts/x versus /it/articoli/x).

Beyond the writing pipeline, the project has a noticeably complete tooling setup for a personal blog: build-time Open Graph image generation with Satori, full-text search via Pagefind, KaTeX for math and Shiki for code highlighting, an abcjs integration for musical notation, and a verification pipeline combining TypeScript, Biome lint/format, Vitest unit tests, Playwright end-to-end tests with accessibility checks via axe-core, and Lighthouse CI. The project's own architecture decision records document why GitHub Pages project-site mode was chosen over a custom domain, suggesting a deliberately documented, low-maintenance publishing setup rather than an experiment in progress.
