# Company website migration and containerization

**Sector**: language services and professional translation company

**Period**: to be confirmed

**Role**: IT Manager, systems administrator

**Technologies**: WordPress, containerization, DNS, hosting on internal infrastructure

## Context

The company website, built on WordPress, was hosted with an external hosting provider: the
company decided to bring its infrastructure in-house, moving it onto the internal network under
its own direct control instead of depending on an external provider.

## What was done

1:1 migration of the company's WordPress website from external hosting to a virtual machine on
the internal network, containerizing the application for isolation and portability, with DNS
redirection to serve it on the LAN while preserving continuity of access for users.

## Result

Company website entirely under internal control, containerized for simpler management of updates
and backups, with no perceived service disruption during the migration.
