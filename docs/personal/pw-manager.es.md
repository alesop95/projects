# pw-manager

A complete 24/7 workflow for personal password management, secrets, authenticator with vaultwarden and enteAuth

- **Repositorio**: [alesop95/pw-manager](https://github.com/alesop95/pw-manager)
- **Tecnologías**: Vaultwarden, Caddy, Docker Compose, deSEC (DNS dinamico)
- **Periodo**: 06/2026, en pausa

Un stack de gestor de contraseñas autoalojado basado en Vaultwarden, servidor de código abierto compatible con las API de Bitwarden, para no depender de un proveedor de bóveda. Caddy actúa como proxy inverso con TLS automático y un pequeño contenedor actualiza cada cinco minutos el DNS dinámico de deSEC con la dirección de la máquina. El stack funciona en una VM Oracle Cloud Always Free, con copias de seguridad de la base de datos cifradas con age y copiadas a Object Storage con rclone. Como segundo factor se usa Ente Auth, una app autenticadora TOTP independiente de la bóveda.

El repositorio público contiene solo los artefactos de despliegue, es decir el archivo compose, el Caddyfile, los scripts de copia de seguridad y de estado y la plantilla de variables; los nombres de host, los tokens y los valores de la instancia quedan fuera de git.
