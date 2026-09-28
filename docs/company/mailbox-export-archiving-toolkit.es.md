# Toolkit de exportación y archivado de buzones de correo y chats

**Sector**: empresa de servicios lingüísticos y traducción profesional

**Periodo**: 06/2026, concluido

**Rol**: IT Manager, administrador de sistemas

**Tecnologías**: PowerShell, Exchange Online PowerShell, Microsoft Graph, Outlook clásico (automatización COM), archivos PST, SHA-256, Microsoft Word (automatización COM)

## Contexto

Dos buzones compartidos tenían el archivo en línea lleno. Antes de liberar espacio hacía falta una copia estática y verificada de todo el contenido, buzón principal y archivo, en un almacenamiento de red. En el mismo periodo surgió una necesidad parecida con los chats de la empresa: extraer mensajes de canales y conversaciones en una forma consultable para auditorías y búsquedas.

## Qué se hizo

El método previsto para el correo era la exportación del lado del servidor mediante eDiscovery; sin embargo, la versión actual de la herramienta exige una licencia de nivel enterprise para quien trabaje en los casos, y se decidió no comprarla. La exportación se hizo por tanto desde Outlook clásico, dividiendo por intervalos de fechas las carpetas más grandes, porque los flujos largos desde el archivo en línea se interrumpían. La completitud se comprobó contando los elementos de cada archivo exportado carpeta por carpeta y comparándolos con los recuentos del servidor, sin contar las carpetas de sistema que no se pueden exportar, ya que el tamaño de un archivo que ha dejado de crecer no prueba que la exportación haya terminado. Los archivos se copiaron al almacenamiento de red con verificación SHA-256. Los scripts de PowerShell solo leen y exportan; el borrado del contenido es una fase aparte, descrita en una guía separada y no automatizada.

Para los chats se escribió un script de PowerShell que lee mensajes de canales y conversaciones mediante Microsoft Graph, con una aplicación registrada que solo tiene permisos de lectura concedidos por el administrador. Los filtros se combinan entre sí: remitentes, ventana de fechas y horas, palabras clave con varios modos de comparación, menciones, adjuntos e importancia. La exportación es incremental gracias a un punto de control con delta token, gestiona la limitación de peticiones con esperas progresivas y descarga las imágenes insertadas; la salida es un archivo CSV o JSON con estadísticas por usuario y por día. Un segundo script convierte la exportación en un documento de Word en orden cronológico, con las imágenes incrustadas en el texto.

## Resultado

El contenido de los dos buzones está archivado en red con recuentos coincidentes por carpeta y sumas de verificación comprobadas, y el runbook y los scripts son paramétricos y reutilizables en otros buzones. Los buzones todavía no se han vaciado. El script de los chats se usa cuando hace falta una extracción para una auditoría o una búsqueda.
