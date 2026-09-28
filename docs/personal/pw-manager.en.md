# pw-manager

A complete 24/7 workflow for personal password management, secrets, authenticator with vaultwarden and enteAuth

- **Repository**: [alesop95/pw-manager](https://github.com/alesop95/pw-manager)
- **Technologies**: Vaultwarden, Caddy, Docker Compose, deSEC (DNS dinamico)
- **Period**: 06/2026, paused

A self-hosted password manager stack based on Vaultwarden, an open-source server compatible with the Bitwarden APIs, to avoid depending on a vault provider. Caddy acts as reverse proxy with automatic TLS, and a small container updates the deSEC dynamic DNS with the machine's address every five minutes. The stack runs on an Oracle Cloud Always Free VM, with database backups encrypted with age and copied to Object Storage with rclone. Ente Auth, a TOTP authenticator app independent of the vault, is used as the second factor.

The public repository contains only the deployment artifacts, namely the compose file, the Caddyfile, the backup and status scripts and the variables template; hostnames, tokens and instance values stay out of git.
