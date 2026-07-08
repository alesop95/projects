# Portal de gestión de activos de TI y cumplimiento ISO/IEC 27001

**Sector**: empresa de servicios lingüísticos y traducción profesional, que también opera como
MSP para activos de TI de clientes en gestión delegada

**Periodo**: 05/2025 - en curso

**Rol**: IT Manager, product owner y desarrollador full-stack

**Tecnologías**: Node.js 22, Fastify, TypeScript strict, React 19, Vite, React Router v7, TanStack
Query, Zustand, Tailwind CSS, Radix UI, PostgreSQL, Drizzle ORM, Redis, BullMQ, Keycloak, Caddy,
Zod, Vitest, Playwright, Docker

## Contexto

La aplicación operativa de la certificación ISO/IEC 27001:2022 requiere un inventario de activos
de TI siempre actualizado, un ciclo de vida trazable para cada activo, gestión estructurada de
incidentes y vulnerabilidades, revisiones periódicas y un mapeo vivo hacia los controles del
estándar. Hacerlo con hojas de cálculo o herramientas genéricas debilita el rastro de auditoría y
hace que el mapeo a los controles sea manual y propenso a errores, más aún con activos de
clientes gestionados en delegación además de los internos.

## Qué se hizo

Aplicación full-stack diseñada como herramienta de trabajo diario para el rol de IT Manager, con
roles secundarios seleccionables para referentes técnicos internos y externos, y un modelo
multi-tenant que separa los activos internos de los de cada cliente gestionado en delegación.
Funcionalidades principales: inventario de activos con un ciclo de vida de siete estados y
auditoría de cada transición, gestión de incidentes y vulnerabilidades, planificación de
revisiones periódicas, mapeo en vivo hacia los 93 controles del Annex A del estándar, y un rastro
de auditoría de solo adición con cadena de hash firmada para garantizar que el historial no pueda
alterarse a posteriori. Stack backend Node.js/Fastify con validación en tiempo de ejecución de
cada entrada, frontend React con gestión de datos vía TanStack Query, base de datos PostgreSQL
con ORM de esquema tipado, autenticación centralizada vía Keycloak, pruebas unitarias/de
integración y end-to-end en los flujos críticos.

## Resultado

Traslada la gestión del cumplimiento ISO/IEC 27001 de un proceso manual y disperso en varias
herramientas a un único sistema con rastro de auditoría verificable y mapeo a los controles
siempre actualizado, reduciendo el esfuerzo de preparación para las auditorías periódicas y
haciendo que la gestión de los activos de clientes en delegación sea trazable al mismo nivel que
la interna.
