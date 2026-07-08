# pw-manager

A complete 24/7 workflow for personal password management, secrets, authenticator with vaultwarden and enteAuth

- **Repository**: [alesop95/pw-manager](https://github.com/alesop95/pw-manager)
- **Linguaggio principale**: PowerShell
- **Ultimo aggiornamento**: 2026-07-06
- **Cartella locale**: `pw-manager`

Uno stack di password manager self-hosted costruito attorno a Vaultwarden, un server open-source che implementa la API di Bitwarden, in modo che le credenziali non dipendano mai da un fornitore di vault di terze parti. Caddy sta davanti come reverse proxy che gestisce il TLS automatico, un piccolo container interroga periodicamente (ogni pochi minuti) la API DNS dinamico di deSEC per mantenere l'hostname pubblico puntato sulla connessione domestica, ed Ente Auth gira in parallelo come autenticatore TOTP indipendente. L'intero stack è definito in un unico file docker-compose, con la configurazione del reverse proxy, lo script di backup e uno script di status-check mantenuti come artefatti di deployment versionati.

Gira su un'istanza Oracle Cloud "Always Free", con backup cifrati del database inviati a Oracle Object Storage. Il repository è pubblico ma versiona deliberatamente solo gli strumenti di deployment (Caddyfile, file compose, script di backup/status); gli hostname reali, i token e gli altri valori specifici dell'istanza sono tenuti in una cartella di note locale esclusa da git, così che il codice pubblico documenti l'architettura senza esporre il deployment live.
