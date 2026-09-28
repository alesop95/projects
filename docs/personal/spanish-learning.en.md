# spanish-learning

- **Repository**: [alesop95/spanish-learning](https://github.com/alesop95/spanish-learning)
- **Technologies**: Claude Code, Anki, base di conoscenza locale
- **Period**: 07/2026, paused

An agentic Spanish-tutoring system built on top of Claude Code, with no application of its own. The work is split into three decoupled layers: a local knowledge base assembled by a zero-LLM-cost ingestion script, which walks a personal library of books and documents (PDF, DOCX, PPTX, XLSX, HTML, with OCR for scanned volumes) and produces a Markdown cache with a per-document index; a spaced-repetition engine meant to run through the `ankimcp/anki-mcp-server` bridge to a local Anki install; and three Claude subagents, tutor, kb-retriever and examiner, wired to slash commands that build a pedagogical roadmap, deliver lessons grounded only in cited source material and close each session with an active-recall check before marking a module complete.

The knowledge base is built, and the first lesson, on greetings and introductions, has been delivered and consolidated in two passes with the examiner's final check. The second lesson, on Italian-Spanish false friends, is prepared but not delivered, and the live connection to Anki is not active yet.
