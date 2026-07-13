# legal-consultant

Local-first project to navigate through Italian legislation with a simple MCP server

- **Repository**: [alesop95/legal-consultant](https://github.com/alesop95/legal-consultant)
- **Languages**: Python, PowerShell, Shell, JavaScript
- **Start date**: 2026-06
- **Last updated**: 2026-07-06
- **Local folder**: `legal-consultant`

A local MCP (Model Context Protocol) server that turns Claude Desktop into an Italian-law research assistant without any pay-as-you-go API cost: all the reasoning happens in Claude Desktop itself, which calls tools exposed by this server, so it runs on an existing Claude subscription rather than metered API usage. The legal corpus is a local clone of the community-maintained `italia-corpus` project, kept current with `git pull` and incremental reindexing, plus a handful of foundational codes (civil, penal, civil procedure) fetched directly from Normattiva because their full text is missing from that corpus. Search is deliberately lightweight: BM25 full-text search over SQLite FTS5, with no GPU and no embeddings, which keeps indexing fast and the whole tool runnable on ordinary hardware.

Three tools are exposed to the model: a BM25 search returning citable excerpts, a lookup that retrieves the full text of a given article by its URN, and a corpus-info tool. A one-click Windows installer bootstraps git and uv, builds the index, registers the MCP server in Claude Desktop, and sets up a daily scheduled task to refresh the corpus. The README is explicit that this is an informational tool, not legal advice, and that lexical BM25 search cannot guarantee an article is still in force without checking Normattiva directly.
