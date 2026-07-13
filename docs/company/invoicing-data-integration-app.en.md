# ERP integration application and invoicing data parsing

**Sector**: language services and professional translation company

**Period**: to be confirmed

**Role**: IT Manager, full-stack developer

**Technologies**: React, XML-RPC, integration with an open-source ERP/CRM system, structured
data parsing

## Context

The company's invoicing data lives in an ERP system that exposes an XML-RPC interface: a
proprietary application was needed to query that system and extract invoicing data in a format
usable by other internal processes, with a test environment kept separate from production.

## What was done

React application that communicates via XML-RPC with an open-source ERP/CRM system to extract
invoicing data, with advanced parsing to normalize and interpret the structured data returned by
the system. It adopts a test/production management workflow with its own approach to promoting
changes from the development environment to production, distinct from that used by other
internal projects.

## Result

A dedicated integration layer between the ERP system and the processes that consume invoicing
data, with an isolated test environment that allows changes to be validated before release.
