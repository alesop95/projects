# my-wedding-day

- **Repositorio**: privado, no consultable
- **Tecnologías**: React 18, TypeScript, Firebase (Firestore, Authentication, Cloud Functions, Hosting)
- **Periodo**: 04/2026 - en curso

Aplicación web para organizar una boda real, desde la confirmación de asistencia de los invitados hasta la velada. Es una single page application en React 18 y TypeScript con backend íntegramente en Firebase (Firestore, Authentication, Cloud Functions, Hosting), sin servidor propio. Los invitados acceden con credenciales personales y encuentran la confirmación de asistencia, la información logística, el programa, la lista de bodas, el libro de visitas, las propuestas para la lista de canciones y el intercambio de fotos. Desde un panel de administración se gestionan familias e invitados, la distribución de las mesas, el menú, los proveedores y la moderación de los contenidos, y el personal de sala, la banda y el fotógrafo tienen cada uno una vista propia.

Cada sesión nace de una Cloud Function de inicio de sesión que verifica las credenciales en el servidor y devuelve un token con el rol, que leen las reglas de seguridad de Firestore. El estado se gestiona con Jotai, los errores con fp-ts, los correos son plantillas MJML compiladas en tiempo de compilación y la interfaz está en italiano e inglés. El proyecto tiene una pipeline de CI de cuatro jobs, pruebas end-to-end con Playwright sobre emuladores de Firebase, monitorización con Sentry, rate limiting y App Check. El código es privado porque contiene datos reales, y está previsto un repositorio público solo con la documentación técnica, depurada de datos personales.
