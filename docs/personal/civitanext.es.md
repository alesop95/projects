# civitanext

_Sin descripción en GitHub._

- **Repositorio**: [alesop95/civitanext](https://github.com/alesop95/civitanext)
- **Lenguajes**: JavaScript, HTML, PowerShell, Shell
- **Fecha de inicio**: 2026-07
- **Última actualización**: 2026-07-15
- **Carpeta local**: `civitanext`

CivitaNext es la plataforma de participación cívica pensada para los jóvenes residentes de Civitanova Marche: un calendario de eventos, cuestionarios cívicos, un foro de discusión, propuestas con votación, un perfil de miembro con carné digital, un panel de administración y secciones de comunidad y ciudad como mentoría, un mapa de espacios cívicos y un archivo documental. El repositorio ha atravesado dos fases distintas: primero una entrega de diseño de alta fidelidad (el prototipo en `design_handoff_civitanext/`), luego, a partir de la Fase 0 de desarrollo, la reconstrucción real en Next.js en la raíz del propio repositorio.

El código en la raíz es una aplicación Next.js 16 (React 19, TypeScript) real, no una maqueta: los tokens visuales y los componentes base del sistema de diseño (Logo, Waves, Starburst, Chip, Btn, Tag, Avatar) se trasladaron del prototipo al código de la app, y la página de inicio los muestra como escaparate, declarando explícitamente que aún no hay ninguna función conectada a la base de datos. En paralelo ya existe el esquema de datos real (Prisma, con PostgreSQL como destino): usuarios con rol y afiliación opcional, autenticación vía NextAuth con sesiones JWT, eventos, foro con hilos, propuestas con votación y un modelo de voto polimórfico compartido entre encuestas, hilos y propuestas. En resumen: los cimientos del sistema de diseño y el esquema de datos son reales y están en el repositorio, pero ninguna funcionalidad está aún conectada a datos reales. El prototipo de diseño original permanece en el repositorio como referencia de solo lectura, no como código de producción.
