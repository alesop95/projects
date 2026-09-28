# Containerized deployment of an open-source project management platform

**Sector**: language services and professional translation company

**Period**: 10/2025, installed and not in use

**Role**: IT Manager, systems administrator

**Technologies**: self-hosted OpenProject with Docker Compose, Ubuntu 24.04 on Proxmox VE, PostgreSQL

## Context

Planning activities with dependencies and deadlines called for evaluating a tool with Gantt charts. A comparison of four alternatives, including desktop applications, text-based tools and a spreadsheet add-in, led to trying OpenProject, an open-source project management project.

## What was done

Containerized deployment of OpenProject with the official Docker Compose setup on an internal virtual machine, with the network configuration needed to reach it from workstations and outgoing mail for notifications. After the disk ran out of space, the machine was resized.

## Result

A working instance of the platform on the internal network. It is not in use for now: the work documented here is the installation, not the adoption of the tool.
