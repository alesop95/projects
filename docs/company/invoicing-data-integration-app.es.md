# Aplicación de integración con el ERP y parsing de datos de facturación

**Sector**: empresa de servicios lingüísticos y traducción profesional

**Periodo**: 11/2024 - en curso

**Rol**: IT Manager: traspaso, documentación y puesta en servicio en una máquina virtual

**Tecnologías**: Next.js y React, Python con Flask, XML-RPC hacia un ERP de código abierto, procesamiento de archivos Excel, Ubuntu en máquina virtual

## Contexto

Para un gran cliente, la facturación mensual requiere un informe que el ERP no produce por sí solo: los datos que pide el cliente, es decir, cantidades y tarifas de cada pedido, están en las líneas de los pedidos y no en la cabecera, y reconstruirlos a mano cada mes era lento y propenso a errores.

## Qué se hizo

La aplicación la desarrolló un antiguo compañero; yo me hice cargo de ella, la documenté paso a paso y la puse en servicio en una máquina virtual interna, cuando antes funcionaba en un solo puesto de trabajo. El frontend Next.js y el backend Python Flask reciben el resumen mensual que el cliente envía en Excel, leen del ERP por XML-RPC las líneas de pedido correspondientes y devuelven el informe completo del que parte la facturación.

## Resultado

La rendición de cuentas mensual para el cliente es un procedimiento de subida y descarga en lugar de una reconstrucción manual, y ya no depende del ordenador de una sola persona.
