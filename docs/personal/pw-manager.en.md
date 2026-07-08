# pw-manager

A complete 24/7 workflow for personal password management, secrets, authenticator with vaultwarden and enteAuth

- **Repository**: [alesop95/pw-manager](https://github.com/alesop95/pw-manager)
- **Main language**: PowerShell
- **Last updated**: 2026-07-06
- **Local folder**: `pw-manager`

A self-hosted password manager stack built around Vaultwarden, an open-source server implementing the Bitwarden API, so that credentials never depend on a third-party vault provider. Caddy sits in front as a reverse proxy handling automatic TLS, a small container polls the deSEC dynamic DNS API every few minutes to keep the public hostname pointed at the home connection, and Ente Auth runs alongside as an independent TOTP authenticator. The whole stack is defined in a single docker-compose file with the reverse proxy config, backup script and a status-check script kept as versioned deployment artifacts.

It runs on an Oracle Cloud "Always Free" instance, with encrypted database backups pushed to Oracle Object Storage. The repository is public but deliberately version-controls only the deployment tooling (Caddyfile, compose file, backup/status scripts); actual hostnames, tokens and other instance-specific values are kept in a local, gitignored notes folder, so the public code documents the architecture without exposing the live deployment.
