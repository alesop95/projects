# Internal generative artificial intelligence platform

!!! tip "Flagship project, continuously evolving"
    The most significant among the internal projects described in this section, under active
    development: it touches on generative AI, dedicated GPU infrastructure, agent orchestration and
    integration with the company identity system. This page will be expanded further once the work
    stabilizes.

**Sector**: language services and professional translation company

**Period**: to be confirmed - ongoing

**Role**: IT Manager, full-stack developer, R&D

**Technologies**: Ollama (self-hosted LLM on dedicated GPU), RAG (retrieval-augmented generation),
Qdrant (vector database), n8n (agentic AI workflow orchestration), company SSO authentication,
reverse proxy on protected LAN, Model Context Protocol (MCP), proprietary frontend

## Context

The company wanted an internal conversational assistant based on generative artificial
intelligence, with access to the company's document context, without depending on third-party
cloud services for every interaction and with full control over data and infrastructure. There was
also a need for a way to extend the assistant's capabilities with custom tools, rather than being
limited to a simple chat interface.

## What was done

Internal generative AI platform built around Ollama as a self-hosted inference engine on dedicated
GPU hardware, with R&D benchmarks and tests to validate model and hardware choices. A RAG system
with Qdrant as the vector database supplies the company's document context to the model. AI agents
orchestrate custom workflows through n8n, with the ability to compose different workflows depending
on the profile of the person accessing the system. Access happens through the same company identity
system (SSO) used for other services, so that the assistant recognizes the user and applies the
appropriate context. The frontend was written from scratch with the company's visual identity, and
also acts as an MCP (Model Context Protocol) client on the internal network toward custom MCP
servers, both centralized and distributed across individual endpoints. The infrastructure is exposed
on the internal network through a protected reverse proxy, with separate test and production
environments.

## Result

An internal AI assistant customized to the company's context, with data and inference under the
company's direct control instead of being entirely entrusted to third-party cloud services, and an
extensible architecture that allows new tools and flows to be added without having to rewrite the
frontend.
