# my-wedding-day

Customized wedding planner app

- **Repositorio**: [alesop95/my-wedding-day](https://github.com/alesop95/my-wedding-day)
- **Lenguajes**: TypeScript, PowerShell, Shell, Python
- **Fecha de inicio**: 2026-04
- **Última actualización**: 2026-07-13
- **Carpeta local**: `my-wedding-day`

Una aplicación de una sola página en React 18 y TypeScript construida para gestionar la logística de cara a los invitados de una boda real, desplegada como sitio estático en Firebase Hosting con Firestore y Cloud Functions como backend, en lugar de un servidor propio. Los invitados navegan por secciones dedicadas para la confirmación de asistencia (RSVP), la información de hotel y lugar de celebración, el programa de la velada, una lista de regalos, un libro de visitas colaborativo, la compartición de fotos, y una función de lista de reproducción/sugerencia de canciones que se integra con la API de Spotify mediante un script de configuración OAuth dedicado. Un área de administración protegida por contraseña, separada de la aplicación de cara a los invitados, cubre la gestión de la lista de invitados con agrupación por familias, la asignación de mesas/asientos del restaurante, la edición del menú, la moderación de las entradas del libro de visitas y de las sugerencias de canciones, el seguimiento de proveedores y una vista de informes, mientras que las Cloud Functions se encargan de aspectos del lado del servidor como la autenticación del personal, los recordatorios programados de RSVP por correo electrónico, y los scripts de limpieza y migración de los registros de invitados.

Técnicamente, la aplicación favorece un modelo de estado basado en átomos con Jotai frente a Redux o Context, fp-ts para el manejo de errores al estilo Option/Either, y Framer Motion junto con Lottie para el encabezado animado y las transiciones; las plantillas de correo electrónico se escriben en MJML y se compilan a TypeScript en tiempo de compilación en lugar de renderizarse en tiempo de ejecución. La propia documentación del proyecto fija este stack de forma deliberada (descartando explícitamente Next.js, Redux, Tailwind y alternativas similares), lo que indica una construcción meditada y desde cero en lugar de una demo montada rápidamente, aunque su alcance sea un único evento real y no un producto reutilizable.
