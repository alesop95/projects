# IT asset management portal and ISO/IEC 27001 compliance

**Sector**: language services and professional translation company

**Period**: 06/2026 - ongoing

**Role**: IT Manager, product owner and full-stack developer

**Technologies**: Node.js and Fastify, React and Vite, TypeScript strict, PostgreSQL with Drizzle ORM, Redis and BullMQ, Keycloak, Caddy, Zod, Vitest and Playwright, Docker

## Context

Putting ISO/IEC 27001:2022 certification into practice requires an always up-to-date IT asset inventory, a traceable lifecycle for each asset, structured handling of incidents and vulnerabilities, periodic reviews and a mapping to the standard's controls. Keeping all of this in spreadsheets leaves a weak history and a manual mapping to the controls.

## What was built

A full-stack application that I designed and developed. The asset inventory follows a seven-state lifecycle, from planned to disposed, and every transition is recorded; alongside the inventory there is incident and vulnerability management, scheduling of periodic reviews and a mapping to the 93 controls of the standard's Annex A. The audit log is append-only, with a signed hash chain that makes any later alteration detectable. The Node.js backend with Fastify validates every input at runtime, the frontend is built in React, the data live in PostgreSQL with a typed-schema ORM, authentication is centralized on Keycloak, and the critical flows have unit, integration and end-to-end tests. The portal currently runs as an internal pilot on the company network; external exposure is not active.

## Result

A single application where inventory, asset lifecycle, incidents, vulnerabilities and mapping to the standard's controls sit together, with a history that cannot be altered. The goal is to reduce the work of preparing for audits; the portal is in its pilot phase and the effect has not yet been measured.
