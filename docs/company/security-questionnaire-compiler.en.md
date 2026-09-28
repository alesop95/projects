# Assisted filling of security and privacy questionnaires

**Sector**: language services and professional translation company

**Period**: 08/2026 - ongoing

**Role**: IT Manager, developer

**Technologies**: Python, openpyxl, python-docx, pypdf, pytest

## Context

During supplier qualification, clients send security and privacy questionnaires and contractual documents to fill in: Excel questionnaires, Word checklists on processing data on the client's behalf, appointments, data breach notification forms. The questions repeat from one client to the next with different wording, and every answer must be consistent with those already given and with the company's actual security posture.

## What was done

A Python pipeline that recognizes the structure of the incoming document on its own, Excel or Word, looks up answers in a knowledge base of question-answer pairs and produces a filled draft that preserves the formatting, styles and cells of the original file; validated answers then flow back into the knowledge base. The question-matching engine is written in pure Python, and dependencies are limited to the libraries needed to read and write office formats. Code and data are separated by design: the repository holds only the machinery, while the knowledge base and the clients' documents live outside it, under a root declared in the local configuration, and an automated check verifies that no client content enters versioned files. Tests run on invented documents.

## Outcome

Filling a questionnaire starts from a draft consistent with previous answers instead of a blank sheet. The Excel path is in use; the Word path has passed tests on real documents in some parts, and the full test on a real document is still to be done.
