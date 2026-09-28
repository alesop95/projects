# Integration backend for a translation service

**Sector**: language services and professional translation company

**Period**: 11/2025 - ongoing

**Role**: IT Manager, security review and fixes to the credit calculation

**Technologies**: Python, FastAPI, SQLite for the project context, parsing of Excel reports and XLIFF bilingual files, integration with a third-party translation project management system, an artificial intelligence based machine translation engine and a public machine translation service as fallback

## Context

The client-facing translation service relies on a third-party project management system to assign work and on a machine translation engine for the first draft. The two systems do not talk to each other natively in the flow the company needs: an integration layer was required to connect the client portal to both, calculate quotes and cover the cases where the main engine does not return a translation.

## What was built

A Python/FastAPI REST backend that connects the client portal to the project management system and the translation engine. The flow is split into three independent calls. The first creates an analysis-only project, reads its report and calculates the quote in credits; the second creates the actual translation project; the third starts, in the background, the export of the bilingual files, has the AI engine translate only the missing segments, falls back to the public service for those the engine does not return, re-imports the files and closes the tasks, leaving the review to the project manager when the client has chosen additional services. Since the three calls do not share a session, the backend keeps a project context with the parameters the third phase needs.

The backend is team work, mostly developed by colleagues. I created the repository, carried out its security review and cleanup, and fixed the preprocessing credit calculation, which was charged once per target language instead of once on the source text.

## Result

The handover between portal, project management and translation engine is automatic from the quote to the delivery of the first draft, with human intervention only where the service calls for it.
