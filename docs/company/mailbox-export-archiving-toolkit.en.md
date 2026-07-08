# Mailbox export and archiving toolkit

**Sector**: language services and professional translation company

**Period**: 06/2026 - ongoing

**Role**: IT Manager, system administrator

**Technologies**: PowerShell, Microsoft 365 / Exchange Online, Microsoft Purview eDiscovery,
Outlook, checksums for integrity verification

## Context

Two shared mailboxes had reached full saturation, both on the primary mailbox and on the linked
online archive. Before freeing up space, a static and verifiable export of the content to a
network resource was needed, with the guarantee that no message would be lost or corrupted in
the process.

## What was built

A reusable operational toolkit for the static export of mailboxes to an archiving network
resource. The reference method identified is server-side PST export via Microsoft Purview
eDiscovery; in the absence of the required license on the operator, the process was adapted to an
equivalent client-side export from classic Outlook. The toolkit includes read-only PowerShell
verification scripts and an archiving step with checksum calculation to guarantee the integrity
of the exported files. The scripts deliberately operate in read-only and export mode only: no
mailbox deletion is automated, that step remains a separate action, explicitly authorized only
once the export has been verified.

## Result

A repeatable and verifiable archiving path for freeing up saturated mailboxes without risk of
data loss, documented well enough to be reapplied to other mailboxes in the future without having
to reinvent the process.
