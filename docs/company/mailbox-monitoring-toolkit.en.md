# Corporate mailbox monitoring toolkit

**Sector**: language services and professional translation company

**Period**: 06/2026 - ongoing

**Role**: IT Manager, system administrator

**Technologies**: Python, PowerShell, Microsoft 365 / Exchange Online, Windows scheduled tasks,
Excel reporting

## Context

Monitoring the state of corporate mailboxes (space used, critical thresholds, trends over time)
was done manually, with no historical collection point to base capacity planning decisions on or
to raise timely alerts before a mailbox became full.

## What was built

A monitoring and reporting toolkit run periodically via Windows scheduled tasks: a Python script
queries the state of Exchange Online mailboxes and generates alerts when a mailbox exceeds a
critical threshold, a second script produces historical reports and trends in Excel. The launch
and scheduled-execution layer is in PowerShell. Credentials and real mailbox data remain strictly
local and are never versioned.

## Result

Automatic alerts on mailboxes at risk of saturation before they become an operational problem,
and a history of trends that did not exist before, useful for planning cleanup or resizing
interventions in advance instead of in an emergency.
