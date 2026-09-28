# telegram-drive-secure

A customization from the https://github.com/caamer20/Telegram-Drive repo without forking it.

- **Repositorio**: [alesop95/telegram-drive-secure](https://github.com/alesop95/telegram-drive-secure)
- **Tecnologías**: Tauri, Rust, React (fork)
- **Periodo**: 07/2026, en pausa

Una personalización de la aplicación de escritorio de código abierto caamer20/Telegram-Drive, escrita en Tauri, Rust y React, que usa los servidores de Telegram como almacén de archivos con los canales en lugar de las carpetas. El código original se importó en el commit `8715927` (v1.9.7) sin su historial y sin un fork de GitHub, una elección registrada en las decisiones del proyecto. El objetivo es añadir cifrado de extremo a extremo de los archivos en el cliente antes de subirlos y un refuerzo general de la aplicación importada.

Hasta ahora han llegado la importación limpia y una pasada que quita las referencias al autor original del identificador y del nombre del producto, junto con la revisión del workflow de CI heredado. El cifrado en el cliente se aplaza hasta que la máquina de desarrollo tenga un toolchain de Rust para compilarlo y probarlo. El README original declara una licencia MIT, pero el árbol importado no contiene un archivo `LICENSE`: la discrepancia está señalada como sin resolver.
