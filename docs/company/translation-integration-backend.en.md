# Integration backend for a translation service

**Sector**: language services and professional translation company

**Period**: 03/2025 - ongoing

**Role**: IT Manager, backend developer

**Technologies**: Python, FastAPI, integration with a third-party translation project management
system, an AI-based machine translation engine, a public machine translation service as fallback

## Context

The translation service offered to clients relies on a third-party project management system for
work assignment and on a machine translation engine for the first draft. The two systems do not
communicate natively in the flow required by the company: an integration layer was needed to
orchestrate the calls between them, with continuity coverage for when the primary engine is
unavailable or does not cover a language pair.

## What was built

REST backend in Python/FastAPI that bridges the project management system and the translation
engine, with a public machine translation service used as fallback when the primary engine does
not respond or does not cover the requested language. The flow is organized into three phases
(project retrieval, submission to the translation engine, collection and normalization of the
result), with error handling and retries at the integration layer. Technical documentation
structured to allow work to resume across non-consecutive sessions.

## Result

Automates a step that previously required manual intervention to route each project between the
two systems, reducing the waiting time between the opening of a translation project and the
availability of the first automatic draft.
