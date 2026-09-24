# Company website migration, containerization and evolution

**Sector**: language services and professional translation company

**Period**: to be confirmed - ongoing

**Role**: IT Manager, environment architecture, systems administrator

**Technologies**: WordPress, Docker Compose, Caddy, Proxmox VE, Next.js, Payload CMS, PostgreSQL, GitHub Actions

## Context

The company website, built on WordPress, was hosted by an external provider, and a redesign commissioned to an outside agency had not reached a publishable result. The company decided to bring the site back under its direct control, first by securing what already existed, then by rebuilding it in-house on its own stack.

## What was done

The first phase is the migration: the WordPress site was moved 1:1 from external hosting to a virtual machine on the internal network, containerized (web server, database and reverse proxy in separate containers) and served on the LAN through a DNS redirect. This copy remains as a read-only reference environment for the content migration.

The second phase, in progress, is the rebuild. The new site is developed on Next.js with Payload as the CMS and PostgreSQL as the database, with a content schema designed from scratch instead of inheriting the WordPress structure. Environments are separated by function: development and staging on an internal virtual machine reachable only from the LAN, production on a dedicated, already hardened cloud server (key-only SSH access, firewall restricted to public services), which builds nothing and runs the container image produced by the build pipeline. Encrypted backups with an off-site copy and a restore test are planned before go-live.

## Outcome

The existing site is now fully under internal control and containerized. The infrastructure for the new site is ready on both environments, and application development is in progress: the site has not been published yet.
