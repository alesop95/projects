# civitanext

_No description on GitHub._

- **Repository**: [alesop95/civitanext](https://github.com/alesop95/civitanext)
- **Languages**: JavaScript, HTML, PowerShell, Shell
- **Start date**: 2026-07
- **Last updated**: 2026-07-15
- **Local folder**: `civitanext`

CivitaNext is the civic-participation platform built for young residents of Civitanova Marche: an event calendar, civic quizzes, a discussion forum, proposals with voting, a member profile with digital card, an admin panel, and community and city sections such as mentorship, a civic-spaces map, and a document archive. The repository has gone through two distinct phases: first a hi-fidelity design handoff (the prototype under `design_handoff_civitanext/`), then, starting from development Phase 0, a real rebuild in Next.js at the repository root.

The code at the root is a genuine Next.js 16 application (React 19, TypeScript), not a mockup: the design system's visual tokens and base components (Logo, Waves, Starburst, Chip, Btn, Tag, Avatar) were ported from the prototype into the app's own code, and the homepage displays them as a showcase while explicitly stating no feature is wired to the database yet. In parallel, the real data schema already exists (Prisma, targeting PostgreSQL): users with role and optional membership, NextAuth authentication with JWT sessions, events, threaded forum discussions, proposals with voting, and a polymorphic vote model shared across polls, threads, and proposals. In short: the design-system foundation and data schema are real and committed, but no feature is wired to live data yet. The original design prototype remains in the repository as a read-only reference, not production code.
