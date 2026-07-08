# pw-manager

A complete 24/7 workflow for personal password management, secrets, authenticator with vaultwarden and enteAuth

- **Repositorio**: [alesop95/pw-manager](https://github.com/alesop95/pw-manager)
- **Lenguaje principal**: PowerShell
- **Última actualización**: 2026-07-06
- **Carpeta local**: `pw-manager`

Un stack de gestor de contraseñas autoalojado construido en torno a Vaultwarden, un servidor de código abierto que implementa la API de Bitwarden, de modo que las credenciales nunca dependen de un proveedor de vault de terceros. Caddy se sitúa delante como proxy inverso que gestiona el TLS automático, un pequeño contenedor consulta periódicamente (cada pocos minutos) la API de DNS dinámico de deSEC para mantener el nombre de host público apuntando a la conexión doméstica, y Ente Auth se ejecuta en paralelo como autenticador TOTP independiente. Todo el stack está definido en un único archivo docker-compose, con la configuración del proxy inverso, el script de backup y un script de comprobación de estado mantenidos como artefactos de despliegue versionados.

Se ejecuta en una instancia Oracle Cloud "Always Free", con copias de seguridad cifradas de la base de datos enviadas a Oracle Object Storage. El repositorio es público, pero versiona deliberadamente solo las herramientas de despliegue (Caddyfile, archivo compose, scripts de backup/estado); los nombres de host reales, los tokens y otros valores específicos de la instancia se mantienen en una carpeta de notas local excluida de git, de modo que el código público documenta la arquitectura sin exponer el despliegue en producción.
