# Portal de gestión de activos de TI y cumplimiento ISO/IEC 27001

**Sector**: empresa de servicios lingüísticos y traducción profesional

**Periodo**: 06/2026 - en curso

**Rol**: IT Manager, product owner y desarrollador full-stack

**Tecnologías**: Node.js y Fastify, React y Vite, TypeScript strict, PostgreSQL con Drizzle ORM, Redis y BullMQ, Keycloak, Caddy, Zod, Vitest y Playwright, Docker

## Contexto

La aplicación operativa de la certificación ISO/IEC 27001:2022 requiere un inventario de activos de TI siempre actualizado, un ciclo de vida trazable para cada activo, una gestión estructurada de incidentes y vulnerabilidades, revisiones periódicas y un mapeo hacia los controles de la norma. Llevar todo esto en hojas de cálculo deja un historial débil y un mapeo manual a los controles.

## Qué se hizo

Aplicación full-stack que diseñé y desarrollé. El inventario de activos sigue un ciclo de vida de siete estados, de planificado a eliminado, y cada transición queda registrada; junto al inventario están la gestión de incidentes y vulnerabilidades, la planificación de las revisiones periódicas y el mapeo hacia los 93 controles del Anexo A de la norma. El registro de auditoría es append-only, con una cadena de hashes firmada que hace detectable cualquier alteración posterior. El backend Node.js con Fastify valida cada entrada en tiempo de ejecución, el frontend está hecho en React, los datos residen en PostgreSQL con un ORM de esquema tipado, la autenticación está centralizada en Keycloak, y los flujos críticos tienen pruebas unitarias, de integración y end-to-end. El portal funciona hoy como piloto interno en la red de la empresa; la exposición hacia el exterior no está activa.

## Resultado

Una única aplicación en la que inventario, ciclo de vida de los activos, incidentes, vulnerabilidades y mapeo a los controles de la norma están juntos, con un historial no alterable. El objetivo es reducir el trabajo de preparación de las auditorías; el portal está en fase piloto y el efecto aún no se ha medido.
