# Toolkit de monitorización de buzones de correo corporativos

**Sector**: empresa de servicios lingüísticos y traducción profesional

**Periodo**: 06/2026 - en curso

**Rol**: IT Manager, administrador de sistemas

**Tecnologías**: Python, PowerShell, Microsoft 365 / Exchange Online, tareas programadas de
Windows, informes en Excel

## Contexto

La monitorización del estado de los buzones de correo corporativos (espacio ocupado, umbrales
críticos, evolución en el tiempo) se hacía de forma manual, sin un punto de recopilación
histórico en el que basar decisiones de capacity planning o alertas oportunas antes de que un
buzón se llenara.

## Qué se hizo

Toolkit de monitorización e informes ejecutado periódicamente mediante tareas programadas de
Windows: un script de Python consulta el estado de los buzones de Exchange Online y genera
alertas cuando un buzón supera un umbral crítico, un segundo script produce informes y tendencias
históricas en Excel. La capa de lanzamiento y ejecución programada está en PowerShell. Las
credenciales y los datos reales de los buzones permanecen exclusivamente locales, nunca
versionados.

## Resultado

Alerta automática sobre los buzones en riesgo de saturación antes de que se conviertan en un
problema operativo, y un histórico de tendencias que antes no existía, útil para planificar
intervenciones de limpieza o redimensionamiento con antelación en lugar de en emergencia.
