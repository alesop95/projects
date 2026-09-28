# Scenia®: multilingual SaaS portal for a translation service

!!! tip "Public product and registered trademark"
    Scenia® is in production at [scenia.it](https://scenia.it/) and is a registered trademark of the company: unlike the other projects in this section, the product name and public address are not anonymized. Only internal information (third-party integrations, processes) that does not already appear on the public site stays generic.

**Sector**: language services and professional translation company

**Period**: 10/2024 - ongoing

**Role**: IT Manager, development of the integration with the company ERP

**Technologies**: Next.js (App Router), React, TypeScript strict, Prisma on MariaDB, Zod, bcrypt, JWT, Tailwind CSS, MJML for transactional email, streaming uploads, pnpm workspace, deployment on a VPS with PM2 and Nginx

## Context

The client-facing translation service needed its own SaaS portal, with a multi-tier access model and a complete translation job management flow, from the quote request to file upload through to completion.

## What was built

The portal is a team product: most of the code is written by colleagues, and I have followed the project as IT Manager since it started. My direct code contribution, from 2026 onwards, is the integration with the company ERP, described in the last paragraph.

The architecture is domain-driven, with a clean split between the domain (`core`, business logic independent of the framework) and the infrastructure (`infra`, concrete implementations against the database and external services), connected through repository interfaces and a single composition root that assembles services per request. Authorization is based on five roles (end user, team leader, project manager, admin, super-admin), with data-visibility rules enforced in the service layer rather than in individual routes, so the scoping logic lives in one place.

The central domain concept is the translation job: each job has its own status workflow, incoming and outgoing files, one or more language pairs, and an automatic analysis that estimates the cost before the job starts. Client billing runs on prepaid credits of two kinds, standard and premium, with a transaction ledger; since 2026 premium credits are calculated inside the portal instead of in the external service. The "consumer" concept brings individual clients, companies and teams under a single abstraction, and the team leader role, added to the original four, lets a client company distribute credits and projects across its own working groups.

External integrations, namely the project and translation-memory management system and the calculation and orchestration backend, are lazily instantiated by the composition root, so a slow dependency does not block the whole request. File uploads are streamed without buffering large attachments in memory, with storage outside the web root; in production this required disabling Nginx proxy buffering on the API routes, without which large uploads failed with no error. The portal also accepts folders and archives with several target languages. The interface, in Italian and English, has an internationalization layer written without third-party libraries, resolving the language from the cookie, then the browser header, then a default.

My code contribution is the integration with the company ERP: automatic creation of sales orders when a job starts, with mapping of clients and services. The integration was developed on a dedicated branch, was withdrawn from the staging environment in July 2026 and is currently on hold.

## Result

A self-service portal in production at [scenia.it](https://scenia.it/), through which business clients upload documents, receive a credit estimate and start the job without going through a manual request.
