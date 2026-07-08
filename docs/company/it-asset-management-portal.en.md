# IT asset management portal and ISO/IEC 27001 compliance

**Sector**: language services and professional translation company, also operating as an MSP
for clients' IT assets under delegated management

**Period**: 05/2025 - ongoing

**Role**: IT Manager, product owner and full-stack developer

**Technologies**: Node.js 22, Fastify, TypeScript strict, React 19, Vite, React Router v7, TanStack
Query, Zustand, Tailwind CSS, Radix UI, PostgreSQL, Drizzle ORM, Redis, BullMQ, Keycloak, Caddy,
Zod, Vitest, Playwright, Docker

## Context

Operationalizing ISO/IEC 27001:2022 certification requires a constantly updated IT asset
inventory, a traceable lifecycle for each asset, structured incident and vulnerability
management, periodic reviews, and a live mapping to the standard's controls. Doing this with
spreadsheets or generic tools makes the audit trail weak and the mapping to controls manual and
error-prone, even more so with client assets managed under delegation alongside internal ones.

## What was built

A full-stack application designed as a daily working tool for the IT Manager role, with
selectable secondary roles for internal and external technical contacts, and a multi-tenant
model that separates internal assets from those of individual clients managed under delegation.
Main features: asset inventory with a seven-state lifecycle and an audit trail for every
transition, incident and vulnerability management, scheduling of periodic reviews, live mapping
to the standard's 93 Annex A controls, and an append-only audit trail with a signed hash chain to
guarantee that the history cannot be altered after the fact. Node.js/Fastify backend stack with
runtime validation on every input, React frontend with data management via TanStack Query,
PostgreSQL database with a typed-schema ORM, centralized authentication via Keycloak, unit/
integration and end-to-end tests on critical flows.

## Result

Moves ISO/IEC 27001 compliance management from a manual process scattered across multiple tools
to a single system with a verifiable audit trail and an always-current control mapping, reducing
the effort required to prepare for periodic audits and making the management of delegated client
assets traceable to the same standard as internal ones.
