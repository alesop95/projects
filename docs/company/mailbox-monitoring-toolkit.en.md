# Corporate mailbox monitoring toolkit

**Sector**: language services and professional translation company

**Period**: 05/2026 - ongoing

**Role**: IT Manager, systems administrator

**Technologies**: PowerShell, Microsoft Graph, Exchange Online PowerShell, registered application with certificate authentication, Python, openpyxl, SQLite, Windows Task Scheduler

## Context

The company mailboxes filled up without warning, and a full primary mailbox stops receiving mail. There was no history of mailbox usage on which to assess the growth of individual mailboxes.

## What was done

A PowerShell script, run every morning by a scheduled task, reads all mailboxes through Microsoft Graph and Exchange Online, collects 22 metrics for each one (usage and quota of the primary mailbox and of the archive, growth over the last 30 days, inactivity, automatic forwarding, legal holds) and stores them in a SQLite database that keeps the history with no expiry. The same script evaluates the thresholds and sends the alerts. Authentication uses a registered application with a certificate, so the run needs no interactive sign-in. Primary mailbox and online archive are treated as two separate problems: when 80% or 95% is exceeded, the IT department receives a summary and the mailbox owner a personal notification, with a different text for each of the two thresholds, while room and equipment mailboxes are excluded. Python has a limited role: two scripts produce the daily Excel reports, split between licensed and functional mailboxes, and a weekly trend report.

## Result

The toolkit has been in daily operation since May 2026 and has built up a daily history of the usage of every mailbox, with the weekly trend reports generated automatically.
