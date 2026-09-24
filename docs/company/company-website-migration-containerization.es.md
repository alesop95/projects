# Migración, containerización y evolución del sitio web corporativo

**Sector**: empresa de servicios lingüísticos y traducción profesional

**Periodo**: por confirmar - en curso

**Rol**: IT Manager, arquitectura de los entornos, administrador de sistemas

**Tecnologías**: WordPress, Docker Compose, Caddy, Proxmox VE, Next.js, Payload CMS, PostgreSQL, GitHub Actions

## Contexto

El sitio web corporativo, basado en WordPress, estaba alojado en un proveedor externo, y un rediseño encargado a una agencia externa no había llegado a un resultado publicable. La empresa decidió devolver el sitio a su control directo, primero asegurando lo que ya existía y después reconstruyéndolo internamente sobre un stack propio.

## Qué se hizo

La primera fase es la migración: el sitio WordPress se trasladó 1:1 del hosting externo a una máquina virtual en la red interna, containerizado (servidor web, base de datos y reverse proxy en contenedores separados) y servido en la LAN mediante una redirección DNS. Esta copia se mantiene como entorno de referencia, de solo lectura, para la migración de los contenidos.

La segunda fase, en curso, es la reconstrucción. El nuevo sitio se desarrolla con Next.js, Payload como CMS y PostgreSQL como base de datos, con un esquema de contenidos diseñado desde cero en lugar de heredar la estructura de WordPress. Los entornos están separados por función: desarrollo y staging en una máquina virtual interna accesible solo desde la LAN, producción en un servidor cloud dedicado y ya protegido (acceso SSH solo con clave, firewall limitado a los servicios públicos), que no compila nada y ejecuta la imagen de contenedor producida por la pipeline de build. Están previstos backups cifrados con copia off-site y una prueba de restauración antes de la puesta en producción.

## Resultado

El sitio existente está hoy totalmente bajo control interno y containerizado. La infraestructura del nuevo sitio está lista en ambos entornos y el desarrollo de la aplicación está en curso: el sitio aún no se ha publicado.
