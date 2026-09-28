# Automation for language production

**Sector**: language services and professional translation company

**Period**: 10/2024 - ongoing

**Role**: IT Manager, script developer

**Technologies**: PowerShell, AutoHotkey, Windows Task Scheduler, Python, spaCy, NLTK, openpyxl

## Context

The work of project managers and translators goes through tools that do not always expose a programmable interface, and through material that has to be prepared before translation: downloaded websites, PDFs, XML files, Word and Excel documents. Part of these operations was repeated by hand for every project, and the backup of translation memories depended on a manual export.

## What was done

Two groups of tools. The first, from 2024 and 2025, is a collection of Python scripts to prepare material for translation: text extraction from HTML, PDF, XML, Word and Excel, splitting of large Excel files, sampling down a translation memory, n-gram extraction with spaCy and NLTK to spot recurring terminology, detection of overlong lines, and flows that extract the text from an HTML skeleton and put it back after translation. The second, from November 2025, is the daily backup of translation memories from the CAT tool's sharing server: a PowerShell script creates the dated folder, prepares the job configuration file, drives the vendor's export tool with AutoHotkey, since it has no programmable interface, applies a retention policy and runs as a scheduled task.

## Outcome

Translation memories have an automatic daily backup with controlled retention, in operation since November 2025. The material preparation scripts were used in the 2024 and 2025 projects and are no longer being developed.
