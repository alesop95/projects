# template-claude-developing

A customized Claude code setup for starting a project from scratch (or.... boosting it!)

- **Repositorio**: [alesop95/template-claude-developing](https://github.com/alesop95/template-claude-developing)
- **Tecnologías**: Claude Code, Markdown, Python, PowerShell
- **Periodo**: 06/2026 - en curso

Sistema portátil de contexto, documentación y control de versiones para proyectos desarrollados con Claude Code y Codex. Se instala en la carpeta `.claude` de un proyecto y hace que el estado siga siendo recuperable desde el repositorio en todo momento: la sesión de chat se pierde al cerrarse, mientras que la memoria del proyecto, las fichas técnicas y el registro de decisiones están en disco y se releen en cada nueva sesión. Dos prompts fijos lo instancian en un proyecto nuevo o lo aplican a posteriori a un proyecto existente, reconstruyendo la memoria a partir del historial de commits sin reescribirlo.

Cada ficha técnica lleva un bloque de metadatos que la ancla a un commit y a las rutas del código que describe, y la skill `sync-context` compara esas rutas con el estado actual y propone actualizaciones puntuales en lugar de regenerar los documentos. Alrededor de este núcleo hay reglas modulares sobre estilo, identidad de git, permisos, uso del contexto y fiabilidad de las pruebas, herramientas Python para la convención Markdown y la tipografía italiana, y un catálogo de paquetes opcionales dividido en diez sectores, que una skill propone según los sectores reconocidos en el proyecto. El commit y el push siguen siendo siempre manuales.

La plantilla está en desarrollo continuo desde junio de 2026 y la usan una treintena de repositorios personales, entre ellos la mayoría de los proyectos descritos en este sitio; las correcciones que nacen en un proyecto se generalizan en la plantilla y luego se propagan a los demás.
