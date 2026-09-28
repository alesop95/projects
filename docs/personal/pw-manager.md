# pw-manager

A complete 24/7 workflow for personal password management, secrets, authenticator with vaultwarden and enteAuth

- **Repository**: [alesop95/pw-manager](https://github.com/alesop95/pw-manager)
- **Tecnologie**: Vaultwarden, Caddy, Docker Compose, deSEC (DNS dinamico)
- **Periodo**: 06/2026, fermo

Uno stack di password manager self-hosted basato su Vaultwarden, server open source compatibile con le API di Bitwarden, per non dipendere da un fornitore di vault. Caddy fa da reverse proxy con TLS automatico e un piccolo container aggiorna ogni cinque minuti il DNS dinamico di deSEC con l'indirizzo della macchina. Lo stack gira su una VM Oracle Cloud Always Free, con backup del database cifrati con age e copiati su Object Storage con rclone. Come secondo fattore si usa Ente Auth, un'app autenticatore TOTP indipendente dal vault.

Il repository pubblico contiene solo gli artefatti di deployment, cioè il file compose, il Caddyfile, gli script di backup e di stato e il modello delle variabili; hostname, token e valori dell'istanza restano fuori da git.
