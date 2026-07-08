# Scenia®: multilingual SaaS portal for a translation service

!!! tip "Public product and registered trademark"
    Scenia® is live at [scenia.it](https://scenia.it/) and is a registered trademark of the
    company: unlike the other projects in this section, the product name and public address are
    not anonymized. Only internal information (third-party integrations, processes) that does
    not already appear on the public site stays generic.

**Sector**: language services and professional translation company

**Period**: 10/2024 - ongoing

**Role**: IT Manager, full-stack developer

**Technologies**: Next.js (App Router), React, TypeScript strict, Prisma with MariaDB adapter,
Zod, bcrypt, JWT, Tailwind CSS, MJML for transactional email, streaming uploads, pnpm workspace,
deployment on a VPS with PM2 and Nginx

## Context

The client-facing translation service needed its own SaaS portal, with a multi-tier access model
(end customer, project manager, admin, super-admin) and a complete translation job management
flow, from the quote request to file upload through to completion, instead of relying on manual
communication scattered across email and spreadsheets.

## What was built

Domain-driven architecture with a clean split between the domain (`core`, business logic
independent of the framework) and the infrastructure (`infra`, concrete implementations against
the database and external services), connected through repository interfaces and a single
composition root that assembles services per request. Authorization is based on four roles (end
user, project manager, admin, super-admin), with data-visibility rules enforced in the service
layer rather than in individual routes, so the scoping logic lives in one place instead of being
duplicated page by page.

The central domain concept is the translation job: each job has its own status workflow, the
incoming attached files and the linked output files, one or more source/target language pairs,
and an automatic analysis that produces a preliminary estimate before assignment. Client billing
runs on prepaid credits, with a transaction ledger that enables a self-service model instead of
manual after-the-fact invoicing. The "consumer" concept unifies corporate and individual clients
under a single abstraction, so the rest of the domain does not need to special-case either kind.
Soft deletion with audit columns on all the main entities keeps a history even of removed records.

External integrations (a translation-memory engine, an ERP/CRM system for company and contact
records, a price-estimation service) are lazily instantiated by the composition root, so the
application does not block the whole request if an external integration is slow or unresponsive.
File uploads stream through the system without buffering large attachments in memory, with
storage kept outside the web root: rolling this out in production also required an Nginx tuning
change to disable proxy buffering on the API routes, otherwise large file uploads would silently
fail. The interface's internationalization is implemented from scratch, without a third-party
library, resolving the language from the session cookie, then the browser header, then a default:
a technical choice that mirrors, at the product level, the multilingual nature of the service the
portal represents.

## Result

A self-service entry point in production at [scenia.it](https://scenia.it/), with multi-tier
authorization, credit-based billing that reduces manual after-the-fact invoicing work, and an
automatic quote estimate that shortens the time between a customer's request and job assignment.
