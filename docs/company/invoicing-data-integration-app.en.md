# ERP integration application and invoicing data parsing

**Sector**: language services and professional translation company

**Period**: 11/2024 - ongoing

**Role**: IT Manager: takeover, documentation and deployment on a virtual machine

**Technologies**: Next.js and React, Python with Flask, XML-RPC to an open-source ERP, Excel file processing, Ubuntu on a virtual machine

## Context

For a large client, monthly invoicing requires a report that the ERP does not produce on its own: the data the client asks for, namely quantities and rates for each order, sit on the order lines rather than on the order header, and rebuilding them by hand every month was slow and error-prone.

## What was done

The application was developed by a former colleague; I took it over, documented it step by step and put it into service on an internal virtual machine, whereas it previously ran on a single workstation. The Next.js frontend and the Python Flask backend take the monthly summary sent by the client in Excel, read the matching order lines from the ERP over XML-RPC and return the complete report from which invoicing starts.

## Result

Monthly reporting for the client is an upload-and-download procedure instead of a manual reconstruction, and it no longer depends on one person's computer.
