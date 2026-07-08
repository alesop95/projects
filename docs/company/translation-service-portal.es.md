# Scenia®: portal SaaS multilingüe para un servicio de traducción

!!! tip "Producto público y marca registrada"
    Scenia® está en producción en [scenia.it](https://scenia.it/) y es una marca registrada de la
    empresa: a diferencia de los demás proyectos de esta sección, el nombre del producto y la
    dirección pública no están anonimizados. Solo permanece genérica la información interna
    (integraciones con terceros, procesos) que no aparece ya en el sitio público.

**Sector**: empresa de servicios lingüísticos y traducción profesional

**Periodo**: 10/2024 - en curso

**Rol**: IT Manager, desarrollador full-stack

**Tecnologías**: Next.js (App Router), React, TypeScript strict, Prisma con adaptador para
MariaDB, Zod, bcrypt, JWT, Tailwind CSS, MJML para los correos transaccionales, subidas en
streaming, pnpm workspace, despliegue en VPS con PM2 y Nginx

## Contexto

El servicio de traducción dirigido a los clientes necesitaba un portal SaaS propio, con un modelo
de acceso de varios niveles (cliente final, gestor de proyecto, administrador,
super-administrador) y un flujo completo de gestión de encargos de traducción, desde la solicitud
de presupuesto hasta la subida de archivos y la finalización, en lugar de depender de
comunicaciones manuales dispersas entre correo y hojas de cálculo.

## Qué se hizo

Arquitectura domain-driven con una separación clara entre el dominio (`core`, lógica de negocio
independiente del framework) y la infraestructura (`infra`, implementaciones concretas contra la
base de datos y los servicios externos), conectadas mediante interfaces de repositorio y una
única raíz de composición que ensambla los servicios en cada solicitud. La autorización se basa
en cuatro roles (usuario final, gestor de proyecto, administrador, super-administrador), con las
reglas de visibilidad de datos aplicadas en la capa de servicio y no en las rutas individuales,
de modo que la lógica de alcance vive en un único lugar en vez de duplicarse página por página.

El concepto central del dominio es el encargo de traducción: cada encargo tiene su propio flujo
de estados, los archivos adjuntos de entrada y los archivos de salida vinculados, uno o más pares
de idioma origen y destino, y un análisis automático que genera una estimación preliminar antes
de la asignación. La facturación a los clientes funciona con créditos prepagados, con un registro
de transacciones que permite un modelo de autoservicio en lugar de la facturación manual a
posteriori. El concepto de "consumer" unifica a los clientes corporativos y particulares bajo una
única abstracción, de modo que el resto del dominio no necesita distinguir entre ambos casos.
Borrado lógico con columnas de auditoría en todas las entidades principales, para conservar un
historial incluso de los registros eliminados.

Las integraciones externas (un motor de memoria de traducción, un sistema ERP/CRM para el
registro de empresas y contactos, un servicio de estimación de precio) se instancian de forma
diferida desde la raíz de composición, de modo que la aplicación no bloquea toda la solicitud si
una integración externa responde con lentitud o no responde. Las subidas de archivos se
transmiten en streaming sin almacenar en memoria los adjuntos de gran tamaño, con el
almacenamiento fuera de la raíz web: poner esto en producción también requirió un ajuste en Nginx
para desactivar el buffering del proxy en las rutas de la API, de lo contrario las subidas de
archivos grandes fallaban en silencio. La internacionalización de la interfaz está implementada
desde cero, sin librería de terceros, resolviendo el idioma primero por la cookie de sesión,
luego por la cabecera del navegador y por último con un valor por defecto: una decisión técnica
que refleja, a nivel de producto, la naturaleza multilingüe del servicio que representa el portal.

## Resultado

Un punto de acceso de autoservicio en producción en [scenia.it](https://scenia.it/), con
autorización de varios niveles, facturación basada en créditos que reduce el trabajo manual de
facturación a posteriori, y una estimación automática de presupuesto que acorta el tiempo entre
la solicitud del cliente y la asignación del encargo.
