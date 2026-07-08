# Portale di gestione asset IT e conformità ISO/IEC 27001

**Settore**: azienda di servizi linguistici e traduzione professionale, operante anche come MSP
per asset IT di clienti in delega

**Periodo**: 05/2025 - in corso

**Ruolo**: IT Manager, product owner e sviluppatore full-stack

**Tecnologie**: Node.js 22, Fastify, TypeScript strict, React 19, Vite, React Router v7, TanStack
Query, Zustand, Tailwind CSS, Radix UI, PostgreSQL, Drizzle ORM, Redis, BullMQ, Keycloak, Caddy,
Zod, Vitest, Playwright, Docker

## Contesto

L'attuazione operativa della certificazione ISO/IEC 27001:2022 richiede un inventario degli asset
IT sempre aggiornato, un ciclo di vita tracciabile per ciascun asset, gestione strutturata di
incidenti e vulnerabilità, revisioni periodiche e un mapping vivo verso i controlli dello standard.
Farlo su fogli di calcolo o strumenti generici rende l'audit trail debole e il mapping ai controlli
manuale e soggetto a errore, tanto più con asset di clienti gestiti in delega oltre a quelli
interni.

## Cosa è stato fatto

Applicazione full-stack disegnata come strumento di lavoro quotidiano per il ruolo di IT Manager,
con ruoli secondari selezionabili per referenti tecnici interni ed esterni, e un modello
multi-tenant che separa gli asset interni da quelli dei singoli clienti gestiti in delega.
Funzionalità principali: inventario degli asset con ciclo di vita a sette stati e audit di ogni
transizione, gestione di incidenti e vulnerabilità, pianificazione delle revisioni periodiche,
mapping live verso i 93 controlli dell'Annex A dello standard, e un audit trail append-only con
catena hash firmata per garantire che lo storico non sia alterabile a posteriori. Stack backend
Node.js/Fastify con validazione runtime su ogni input, frontend React con gestione dati via
TanStack Query, database PostgreSQL con ORM a schema tipizzato, autenticazione centralizzata via
Keycloak, test unitari/integrazione e end-to-end sui flussi critici.

## Risultato

Sposta la gestione della conformità ISO/IEC 27001 da un processo manuale e disperso su più
strumenti a un unico sistema con audit trail verificabile e mapping ai controlli sempre
aggiornato, riducendo lo sforzo di preparazione agli audit periodici e rendendo la gestione degli
asset dei clienti in delega tracciabile allo stesso livello di quella interna.
