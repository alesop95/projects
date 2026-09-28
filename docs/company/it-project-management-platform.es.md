# Despliegue en contenedores de una plataforma de gestión de proyectos de código abierto

**Sector**: empresa de servicios lingüísticos y traducción profesional

**Periodo**: 10/2025, instalada y sin uso

**Rol**: IT Manager, administrador de sistemas

**Tecnologías**: OpenProject autoalojado con Docker Compose, Ubuntu 24.04 sobre Proxmox VE, PostgreSQL

## Contexto

Para planificar actividades con dependencias y plazos había que evaluar una herramienta con diagramas de Gantt. Una comparación entre cuatro alternativas, entre ellas aplicaciones de escritorio, herramientas basadas en texto y un complemento para hojas de cálculo, llevó a probar OpenProject, un proyecto de código abierto de gestión de proyectos.

## Qué se hizo

Despliegue en contenedores de OpenProject con el Docker Compose oficial en una máquina virtual interna, con la configuración de red necesaria para acceder desde los puestos de trabajo y el correo saliente para las notificaciones. Tras agotarse el espacio en disco, la máquina se redimensionó.

## Resultado

Una instancia operativa de la plataforma en la red interna. Por ahora no está en uso: el trabajo documentado aquí es la instalación, no la adopción de la herramienta.
