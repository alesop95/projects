# paypal-transaction-data

- **Repositorio**: [alesop95/paypal-transaction-data](https://github.com/alesop95/paypal-transaction-data)
- **Tecnologías**: Python, API REST di PayPal, Google Sheets, Excel
- **Periodo**: 06/2026, en pausa

Una herramienta Python de línea de comandos que descarga el historial de transacciones desde la API REST de PayPal y lo sincroniza con una hoja de Google o, como alternativa, con un archivo Excel, para llevar un registro contable sin copiar a mano los extractos. Extrae los campos útiles para la conciliación, es decir identificadores de transacción y de referencia, importes brutos y netos, comisiones, moneda, estado y pagador, y omite los registros ya sincronizados.

Funciona en modo sandbox y live, como sincronización única, sobre un rango de fechas o como tarea periódica, con un subcomando que comprueba la conexión con la API. El repositorio contiene solo código e instrucciones, ningún dato de transacciones.
