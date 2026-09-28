# Migration of a legacy management software to a supported operating system

**Sector**: language services and professional translation company

**Period**: 02/2026 - ongoing

**Role**: IT Manager, systems administrator

**Technologies**: Ubuntu 10.04 LTS → Ubuntu 24.04 LTS, Docker, separate containers for production and testing, relational database, Proxmox VE

## Context

The management software the company used for day-to-day work until 2021, a web application from the mid-2000s, now serves as an archive: it is consulted internally for historical data. It ran on an Ubuntu 10.04 LTS server, a distribution out of support for many years, inside the company's virtualized infrastructure.

## What was done

The software was rebuilt on a new Ubuntu 24.04 LTS virtual machine on the Proxmox infrastructure, with the application and its database in containers. The same machine runs two independent instances, one for production and one for testing, each with its own database, so that changes can be tried out before touching the archive users consult. The migration was led as IT Manager, with contributions from the team.

## Result

The historical data can be consulted from an instance running on a supported operating system, with a testing environment separate from production. The work is ongoing: the old server is still running and its decommissioning remains to be completed.
