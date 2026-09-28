# Migración y gestión del ciclo de vida de licencias de software

**Sector**: empresa de servicios lingüísticos y traducción profesional

**Periodo**: 01/2025 - 03/2025

**Rol**: IT Manager, responsable de la migración y administrador de sistemas

**Tecnologías**: Windows Server 2012 R2 → Windows Server 2022, Proxmox VE, gestores de licencias de red de uso concurrente, instalación administrativa desde un recurso compartido de red

## Contexto

Una herramienta de reconocimiento óptico de caracteres (OCR) y una herramienta de traducción asistida (CAT) usan licencias de red, que un gestor de licencias en un servidor reparte a los puestos de trabajo. El gestor del OCR funcionaba en una máquina virtual Windows Server 2012 R2 alojada en el antiguo host de virtualización, que a principios de 2025 se estaba sustituyendo por un nuevo servidor con Proxmox: el gestor tenía que pasar a un nuevo Windows Server 2022 sin dejar los puestos sin licencia.

## Qué se hizo

El trabajo lo planteó y lo dirigió el IT Manager, que decidió el orden de los pasos, las comprobaciones y las decisiones sobre el perímetro de las licencias, con la ayuda de un compañero presente solo por las mañanas; el proveedor interviene únicamente cuando cambia el suministro de licencias. Las licencias del OCR son perpetuas pero sin contrato de mantenimiento, así que la asistencia del proveedor se limitaba a activaciones y paquetes de instalación. El primer paquete descargable por cuenta propia instalaba un gestor de una versión posterior, incompatible con las licencias adquiridas, y se descartó en favor del paquete de la versión correcta; la versión de la herramienta OCR no cambió. La activación sin conexión no funcionó y copiar a mano las carpetas de licencias desde el servidor antiguo resultó inútil, porque la configuración no reside en archivos copiables: el nuevo gestor se activó en línea. En ese momento el gestor antiguo y el nuevo exponían el mismo número de serie, y la concurrencia real habría superado el número de licencias compradas; por eso se decidió reinstalar rápidamente los puestos y desmantelar el gestor antiguo. Para la reinstalación se preparó en el nuevo servidor un punto de instalación administrativa compartido en red, y un error de instalación causado por datos residuales de la instalación anterior se resolvió eliminando sus carpetas antes de volver a lanzarla.

## Resultado

El gestor de licencias del OCR funciona en Windows Server 2022 en la nueva infraestructura, con la misma versión de la herramienta y el primer puesto reinstalado leyendo correctamente la licencia desde el nuevo servidor. Las licencias de la herramienta CAT siguen siendo licencias de red, servidas por un servidor y distribuidas en unos dieciocho puestos.
