# Mailbox and chat export and archiving toolkit

**Sector**: language services and professional translation company

**Period**: 06/2026, completed

**Role**: IT Manager, systems administrator

**Technologies**: PowerShell, Exchange Online PowerShell, Microsoft Graph, classic Outlook (COM automation), PST files, SHA-256, Microsoft Word (COM automation)

## Context

Two shared mailboxes had a full online archive. Before freeing up space, a static and verified copy of the entire content, primary mailbox and archive, was needed on a network archive. In the same period a related need came up for the company chats: extracting channel and conversation messages in a form that could be consulted for audits and searches.

## What was done

The planned method for the mail was server-side export through eDiscovery; the current version of the tool, however, requires an enterprise-level license for anyone working on cases, and the decision was not to buy it. The export was therefore run from classic Outlook, splitting the largest folders by date range, because long streams from the online archive kept breaking off. Completeness was proven by counting the items of each exported file folder by folder and comparing them with the server-side counts, excluding the system folders that cannot be exported, since the size of a file that has stopped growing does not prove that the export has finished. The files were copied to the network archive with SHA-256 verification. The PowerShell scripts only read and export; deleting the content is a separate step, described in a separate guide and not automated.

For the chats, a PowerShell script was written that reads channel and conversation messages through Microsoft Graph, with a registered application holding only read permissions granted by the administrator. The filters can be combined: senders, date and time window, keywords with several matching modes, mentions, attachments and importance. The export is incremental thanks to a checkpoint with a delta token, it handles request throttling with progressive waits and downloads inline images; the output is a CSV or JSON file with statistics per user and per day. A second script converts the export into a Word document in chronological order, with the images embedded in the text.

## Result

The content of the two mailboxes is archived on the network with matching counts per folder and verified checksums, and the runbook and scripts are parametric and reusable on other mailboxes. The mailboxes have not been emptied yet. The chat script is used whenever an extraction for an audit or a search is needed.
