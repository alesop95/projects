# paypal-transaction-data

_Sin descripción en GitHub._

- **Repositorio**: [alesop95/paypal-transaction-data](https://github.com/alesop95/paypal-transaction-data)
- **Lenguaje principal**: Python
- **Última actualización**: 2026-07-06
- **Carpeta local**: `paypal-transaction-data`

Una herramienta de línea de comandos en Python que extrae el historial de transacciones desde la API REST de PayPal y lo sincroniza con una Google Sheet, manteniendo un libro contable continuo con fines de contabilidad. Extrae los campos relevantes para la conciliación contable, como identificadores de transacción y de referencia, importes brutos y netos, comisiones, moneda, estado y datos del pagador, y los escribe en una hoja formateada, omitiendo los registros que ya se habían sincronizado antes. Existe también una ruta de exportación independiente a Excel, junto a la de Google Sheets.

La herramienta admite tanto el modo sandbox como el modo live de PayPal y puede ejecutarse como una sincronización puntual, como una sincronización sobre un rango de fechas específico, o como un trabajo programado a un intervalo configurable, con un subcomando de estado para comprobar la conectividad con la API. Las credenciales tanto de PayPal como de Google se mantienen fuera del control de versiones mediante variables de entorno y un archivo de credenciales OAuth. Es una utilidad personal de contabilidad creada para eliminar el trabajo manual de copiar los extractos de PayPal en una hoja de cálculo, no un producto financiero de propósito general: el repositorio contiene intencionadamente solo el código y las instrucciones de configuración, no datos de transacciones reales.
