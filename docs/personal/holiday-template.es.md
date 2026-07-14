# holiday-template

A free-customized interactive holiday tracker

- **Repositorio**: [alesop95/holiday-template](https://github.com/alesop95/holiday-template)
- **Lenguajes**: JavaScript, Python, HTML, PowerShell
- **Fecha de inicio**: 2026-06
- **Última actualización**: 2026-07-14
- **Carpeta local**: `holiday-template`

Una plantilla reutilizable para construir progressive web apps de planificación de viajes compartida, nacida de un proyecto real de vacaciones en pareja (un viaje al Cilento de 2026 vive bajo `trips/` como primera instancia). El diseño separa deliberadamente un shell HTML/JS canónico, que gestiona el renderizado, el estado y la conexión con Firebase y que nunca se modifica por viaje, de un único archivo `trip.config.js` por viaje que contiene el itinerario, la lista de restaurantes, los marcadores del mapa y la checklist. Cada nueva vacación se crea copiando el shell en una nueva carpeta bajo `trips/` y escribiendo solo ese archivo de configuración, mientras que todos los viajes comparten un único proyecto de Firebase y se organizan en Firestore mediante un prefijo `TRIP_ID`, de modo que la sincronización en tiempo real de la checklist entre los dispositivos de dos personas sigue funcionando sin necesidad de configurar un backend por cada viaje.

Además del planificador estático, el repositorio también contiene `services/flight-search`, un pequeño servicio FastAPI documentado explícitamente como un scaffold inicial y no como una funcionalidad terminada: expone un único endpoint de búsqueda respaldado por dos adaptadores de datos de vuelos (un scraper de Google Flights vía `fast-flights` y la API Kiwi Tequila), sin ninguna capa de caché todavía. Las propias notas del proyecto registran que se escribió y probó un tercer adaptador construido sobre la API de Amadeus, que después se eliminó deliberadamente tras que Amadeus anunciara el cierre de su portal de desarrolladores self-service.
