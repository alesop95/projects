# Backend de integración para un servicio de traducción

**Sector**: empresa de servicios lingüísticos y traducción profesional

**Periodo**: 11/2025 - en curso

**Rol**: IT Manager, revisión de seguridad y correcciones en el cálculo de los créditos

**Tecnologías**: Python, FastAPI, SQLite para el contexto de proyecto, parsing de informes Excel y de archivos bilingües XLIFF, integración con un sistema de gestión de proyectos de traducción de terceros, un motor de traducción automática basado en inteligencia artificial y un servicio público de traducción automática como respaldo

## Contexto

El servicio de traducción orientado a los clientes se apoya en un sistema de gestión de proyectos de terceros para la asignación del trabajo y en un motor de traducción automática para el primer borrador. Los dos sistemas no se comunican de forma nativa en el flujo que necesita la empresa: hacía falta una capa de integración que conectara el portal de clientes con ambos, calculara los presupuestos y cubriera los casos en que el motor principal no devuelve una traducción.

## Qué se hizo

Backend REST en Python/FastAPI que conecta el portal de clientes con el sistema de gestión de proyectos y con el motor de traducción. El flujo se divide en tres llamadas independientes. La primera crea un proyecto solo de análisis, lee su informe y calcula el presupuesto en créditos; la segunda crea el proyecto de traducción propiamente dicho; la tercera lanza en segundo plano la exportación de los archivos bilingües, hace traducir al motor de IA solo los segmentos que faltan, recurre al servicio de respaldo para los que el motor no devuelve, reimporta los archivos y cierra las tareas, dejando la revisión al project manager cuando el cliente ha elegido servicios adicionales. Como las tres llamadas no comparten una sesión, el backend conserva un contexto de proyecto con los parámetros que necesita la tercera fase.

El backend es un trabajo de equipo, desarrollado en gran parte por compañeros. Creé el repositorio, hice su revisión de seguridad y su limpieza, y corregí el cálculo de los créditos de preprocesamiento, que se cobraba una vez por cada idioma de destino en lugar de una sola vez sobre el texto de origen.

## Resultado

El paso entre el portal, la gestión de proyectos y el motor de traducción es automático desde el presupuesto hasta la entrega del primer borrador, con intervención humana solo donde el servicio lo prevé.
