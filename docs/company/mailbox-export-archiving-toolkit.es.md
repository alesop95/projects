# Toolkit de exportación y archivado de buzones de correo

**Sector**: empresa de servicios lingüísticos y traducción profesional

**Periodo**: 06/2026 - en curso

**Rol**: IT Manager, administrador de sistemas

**Tecnologías**: PowerShell, Microsoft 365 / Exchange Online, Microsoft Purview eDiscovery,
Outlook, checksums para la verificación de integridad

## Contexto

Dos buzones de correo compartidos habían alcanzado la saturación completa, tanto en el buzón
principal como en el archivo online vinculado. Antes de liberar espacio hacía falta una
exportación estática y verificable del contenido hacia un recurso de red, con la garantía de que
ningún mensaje se perdiera o corrompiera en el proceso.

## Qué se hizo

Toolkit operativo reutilizable para la exportación estática de los buzones hacia un recurso de
red de archivado. El método de referencia identificado es la exportación PST del lado del
servidor mediante Microsoft Purview eDiscovery; ante la falta de la licencia necesaria en el
operador, el proceso se adaptó a una exportación equivalente del lado del cliente desde Outlook
clásico. El toolkit incluye scripts de PowerShell de verificación preliminar de solo lectura y un
paso de archivado con cálculo de checksum para garantizar la integridad de los archivos
exportados. Los scripts operan deliberadamente solo en modo de lectura y exportación: ninguna
eliminación de los buzones está automatizada, esa fase sigue siendo una acción separada y
autorizada explícitamente solo una vez verificada la exportación.

## Resultado

Un procedimiento de archivado repetible y verificable para liberar buzones saturados sin riesgo
de pérdida de datos, documentado con detalle suficiente para poder reaplicarlo a otros buzones en
el futuro sin tener que reinventar el proceso.
