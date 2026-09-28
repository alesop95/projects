# Toolkit de monitorización de buzones de correo corporativos

**Sector**: empresa de servicios lingüísticos y traducción profesional

**Periodo**: 05/2026 - en curso

**Rol**: IT Manager, administrador de sistemas

**Tecnologías**: PowerShell, Microsoft Graph, Exchange Online PowerShell, aplicación registrada con autenticación por certificado, Python, openpyxl, SQLite, Programador de tareas de Windows

## Contexto

Los buzones de la empresa se llenaban sin previo aviso, y un buzón principal lleno deja de recibir correo. No existía un histórico de ocupación con el que valorar el crecimiento de cada buzón.

## Qué se hizo

Un script de PowerShell, ejecutado cada mañana por una tarea programada, lee todos los buzones mediante Microsoft Graph y Exchange Online, recoge 22 métricas de cada uno (ocupación y cuota del buzón principal y del archivo, crecimiento en los últimos 30 días, inactividad, reenvíos automáticos, retenciones legales) y las guarda en una base de datos SQLite que conserva el histórico sin caducidad. El mismo script evalúa los umbrales y envía los avisos. La autenticación usa una aplicación registrada con certificado, así que la ejecución no requiere inicios de sesión interactivos. El buzón principal y el archivo en línea se tratan como dos problemas distintos: al superar el 80% o el 95%, el departamento de TI recibe un resumen y el titular del buzón una notificación personal, con un texto distinto para cada uno de los dos umbrales, mientras que los buzones de salas y equipos quedan excluidos. Python tiene un papel acotado: dos scripts generan los informes diarios en Excel, separados entre buzones con licencia y buzones funcionales, y un informe semanal de tendencias.

## Resultado

El toolkit está en funcionamiento diario desde mayo de 2026 y ha acumulado un histórico diario de la ocupación de todos los buzones, con los informes semanales de tendencias generados automáticamente.
