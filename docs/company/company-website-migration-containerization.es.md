# Migración y containerización del sitio web corporativo

**Sector**: empresa de servicios lingüísticos y traducción profesional

**Periodo**: por confirmar

**Rol**: IT Manager, administrador de sistemas

**Tecnologías**: WordPress, containerización, DNS, hosting en infraestructura interna

## Contexto

El sitio web corporativo, basado en WordPress, estaba alojado en un proveedor de hosting externo:
la empresa decidió internalizar su infraestructura, trasladándolo a la red interna bajo su propio
control directo en lugar de depender de un proveedor externo.

## Qué se hizo

Migración 1:1 del sitio WordPress corporativo desde un hosting externo a una máquina virtual en
la red interna, containerizando la aplicación para aislamiento y portabilidad, con redirección
DNS para servirlo en la LAN manteniendo la continuidad de acceso para los usuarios.

## Resultado

Sitio web corporativo completamente bajo control interno, containerizado para una gestión más
sencilla de actualizaciones y copias de seguridad, sin discontinuidad de servicio percibida
durante la migración.
