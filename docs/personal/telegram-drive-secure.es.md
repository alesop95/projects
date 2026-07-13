# telegram-drive-secure

A customization from the https://github.com/caamer20/Telegram-Drive repo without forking it.

- **Repositorio**: [alesop95/telegram-drive-secure](https://github.com/alesop95/telegram-drive-secure)
- **Lenguajes**: TypeScript, Rust, PowerShell, Python
- **Fecha de inicio**: 2026-07
- **Última actualización**: 2026-07-02
- **Carpeta local**: `telegram-drive-secure-fork`

Esto es una personalización de la aplicación de escritorio de código abierto caamer20/Telegram-Drive, no un proyecto escrito de forma independiente ni un fork formal de GitHub: el código upstream (Tauri, Rust, React, que usa los propios servidores de Telegram como backend de archivos, con los canales haciendo las veces de carpetas) se importó en un commit upstream fijado sin preservar su historial de commits original, una decisión registrada explícitamente en las propias notas del proyecto. El objetivo declarado es añadir cifrado de extremo a extremo del lado del cliente para los archivos antes de subirlos y un endurecimiento general de la superficie de ataque sobre la aplicación importada, pero, a fecha de los últimos commits, solo han aterrizado realmente dos cambios: la importación limpia en sí, y un pase que elimina las referencias al autor original del identificador de la app y del nombre del producto, además de una revisión del workflow de CI heredado. El módulo de cifrado y el trabajo de hardening más amplio siguen planificados, no implementados.

Algo a tener en cuenta para quien lea el código: el README upstream declara una licencia MIT, pero no había ningún archivo `LICENSE` en el árbol de fuentes importado, una discrepancia que la propia documentación del proyecto marca como sin resolver en lugar de pasarla por alto. El valor de este proyecto ahora mismo está sobre todo en los documentos de planificación, el threat model y la hoja de ruta por fases que arrastra desde la decisión de fork, no en funciones de seguridad ya entregadas.
