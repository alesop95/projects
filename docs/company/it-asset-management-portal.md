# Portale di gestione asset IT e conformità ISO/IEC 27001

**Settore**: azienda di servizi linguistici e traduzione professionale

**Periodo**: 06/2026 - in corso

**Ruolo**: IT Manager, product owner e sviluppatore full-stack

**Tecnologie**: Node.js e Fastify, React e Vite, TypeScript strict, PostgreSQL con Drizzle ORM, Redis e BullMQ, Keycloak, Caddy, Zod, Vitest e Playwright, Docker

## Contesto

L'attuazione operativa della certificazione ISO/IEC 27001:2022 richiede un inventario degli asset IT sempre aggiornato, un ciclo di vita tracciabile per ciascun asset, una gestione strutturata di incidenti e vulnerabilità, revisioni periodiche e un mapping verso i controlli dello standard. Tenere tutto questo su fogli di calcolo rende lo storico debole e il mapping ai controlli manuale.

## Cosa è stato fatto

Applicazione full-stack che ho progettato e sviluppato. L'inventario degli asset segue un ciclo di vita a sette stati, da pianificato a eliminato, e ogni transizione viene registrata; accanto all'inventario ci sono la gestione di incidenti e vulnerabilità, la pianificazione delle revisioni periodiche e il mapping verso i 93 controlli dell'Annex A dello standard. Il registro di audit è append-only, con una catena hash firmata che rende rilevabile qualunque alterazione a posteriori. Il backend Node.js con Fastify valida ogni input a runtime, il frontend è in React, i dati stanno in PostgreSQL con un ORM a schema tipizzato, l'autenticazione è centralizzata su Keycloak, e i flussi critici hanno test unitari, di integrazione e end-to-end. Il portale gira oggi come pilota interno sulla rete aziendale; l'esposizione verso l'esterno non è attiva.

## Risultato

Un'unica applicazione in cui inventario, ciclo di vita degli asset, incidenti, vulnerabilità e mapping ai controlli dello standard stanno insieme, con uno storico non alterabile. L'obiettivo è ridurre il lavoro di preparazione agli audit; il portale è in fase pilota e l'effetto non è ancora misurato.
