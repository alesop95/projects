# Scenia®: portal SaaS multilingüe para un servicio de traducción

!!! tip "Producto público y marca registrada"
    Scenia® está en producción en [scenia.it](https://scenia.it/) y es una marca registrada de la empresa: a diferencia de los demás proyectos de esta sección, el nombre del producto y la dirección pública no están anonimizados. Solo permanece genérica la información interna (integraciones con terceros, procesos) que no aparece ya en el sitio público.

**Sector**: empresa de servicios lingüísticos y traducción profesional

**Periodo**: 10/2024 - en curso

**Rol**: IT Manager, desarrollo de la integración con el ERP de la empresa

**Tecnologías**: Next.js (App Router), React, TypeScript strict, Prisma sobre MariaDB, Zod, bcrypt, JWT, Tailwind CSS, MJML para los correos transaccionales, subida de archivos en streaming, pnpm workspace, despliegue en VPS con PM2 y Nginx

## Contexto

El servicio de traducción orientado a los clientes necesitaba un portal SaaS propio, con un modelo de acceso en varios niveles y un flujo completo de gestión de los encargos de traducción, desde la solicitud de presupuesto hasta la subida de archivos y la finalización.

## Qué se hizo

El portal es un producto de equipo: el código lo escriben en gran parte compañeros, y yo sigo el proyecto como IT Manager desde su inicio. Mi contribución directa al código, desde 2026, es la integración con el ERP de la empresa, descrita en el último párrafo.

La arquitectura es domain-driven, con una separación clara entre el dominio (`core`, lógica de negocio independiente del framework) y la infraestructura (`infra`, implementaciones concretas hacia la base de datos y los servicios externos), conectados mediante interfaces de repositorio y un composition root único que ensambla los servicios en cada petición. La autorización se basa en cinco roles (usuario final, jefe de equipo, project manager, administrador, superadministrador), con las reglas de visibilidad de los datos aplicadas en la capa de servicio y no en cada ruta, de modo que la lógica de scoping está en un solo lugar.

El concepto central del dominio es el encargo de traducción: cada encargo tiene su propio flujo de estados, los archivos de entrada y de salida, uno o varios pares de idiomas y un análisis automático que estima el coste antes del inicio. La facturación a los clientes funciona con créditos prepagados de dos tipos, estándar y premium, con un registro de transacciones; desde 2026 el cálculo de los créditos premium se hace dentro del portal en lugar del servicio externo. El concepto de "consumer" reúne bajo una misma abstracción a clientes particulares, empresas y equipos, y el rol de jefe de equipo, añadido a los cuatro iniciales, permite a una empresa cliente repartir créditos y proyectos entre sus propios grupos de trabajo.

Las integraciones externas, es decir, el sistema de gestión de proyectos y memorias de traducción y el backend de cálculo y orquestación, se instancian de forma lazy desde el composition root, así una dependencia lenta no bloquea toda la petición. La subida de archivos se hace en streaming, sin cargar en memoria los adjuntos grandes, con el almacenamiento fuera de la web root; en producción obligó a desactivar el buffering del proxy Nginx en las rutas de la API, sin lo cual las subidas grandes fallaban sin ningún error. El portal acepta también carpetas y archivos comprimidos con varios idiomas de destino. La interfaz, en italiano e inglés, tiene una internacionalización escrita sin bibliotecas de terceros, que resuelve el idioma por cookie, luego por la cabecera del navegador y luego por un idioma predeterminado.

Mi contribución de código es la integración con el ERP de la empresa: la creación automática de los pedidos de venta al iniciarse un encargo, con el mapeo de clientes y servicios. La integración se desarrolló en una rama dedicada, se retiró del entorno de pruebas en julio de 2026 y hoy está suspendida.

## Resultado

Un portal de autoservicio en producción en [scenia.it](https://scenia.it/), con el que los clientes empresariales suben los documentos, reciben una estimación en créditos e inician el encargo sin pasar por una solicitud manual.
