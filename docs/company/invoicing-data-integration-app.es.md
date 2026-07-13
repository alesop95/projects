# Aplicación de integración con el ERP y parsing de datos de facturación

**Sector**: empresa de servicios lingüísticos y traducción profesional

**Periodo**: por confirmar

**Rol**: IT Manager, desarrollador full-stack

**Tecnologías**: React, XML-RPC, integración con un sistema ERP/CRM de código abierto, parsing de
datos estructurados

## Contexto

Los datos de facturación de la empresa residen en un sistema ERP que expone una interfaz
XML-RPC: se necesitaba una aplicación propia capaz de consultar ese sistema y extraer los datos
de facturación en un formato utilizable por otros procesos internos, con un entorno de pruebas
separado del de producción.

## Qué se hizo

Aplicación React que se comunica vía XML-RPC con un sistema ERP/CRM de código abierto para
extraer los datos de facturación, con un parsing avanzado para normalizar e interpretar los datos
estructurados devueltos por el sistema. Adopta un flujo de gestión de pruebas/producción con su
propia filosofía de promoción de cambios desde el entorno de desarrollo hasta producción,
distinta de la de otros proyectos internos.

## Resultado

Una capa de integración dedicada entre el sistema ERP y los procesos que consumen los datos de
facturación, con un entorno de pruebas aislado que permite validar los cambios antes de su
publicación.
