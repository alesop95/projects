# spanish-learning

_No description on GitHub._

- **Repository**: [alesop95/spanish-learning](https://github.com/alesop95/spanish-learning)
- **Main language**: Python
- **Last updated**: 2026-07-07
- **Local folder**: `spanish-learning`

This is not a software application but an agentic Spanish-tutoring system built on top of Claude Code. Three decoupled layers do the work: a local knowledge base assembled by a zero-LLM-cost ingestion script that walks a personal library of books and documents (PDF, DOCX, PPTX, XLSX, HTML, with an OCR fallback for scanned volumes) and produces a Markdown cache with a per-document index; a spaced-repetition engine meant to run through the `ankimcp/anki-mcp-server` bridge to a local Anki install; and an orchestration layer of three Claude subagents, tutor, kb-retriever, and examiner, wired to slash commands (`/profile`, `/learn`, `/review`) that build a learner profile and pedagogical roadmap, deliver lessons grounded only in cited source material, and close each session with active-recall verification before marking a module complete.

One concrete artifact already generated is a custom Anki deck of Italian-Spanish false friends, produced by a small script from a curated word list since no public deck covers that specific interference pattern. Per the project's own status tracker, the knowledge base and first learner profile are built, but Anki desktop and AnkiConnect are not yet live-connected and no lesson has actually been delivered end to end, so this is best read as a working scaffold for a personal learning workflow rather than a finished tool.
