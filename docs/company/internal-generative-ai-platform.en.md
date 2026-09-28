# Internal generative artificial intelligence platform

**Sector**: language services and professional translation company

**Period**: 03/2025 - ongoing

**Role**: IT Manager, full-stack developer, R&D

**Technologies**: Ollama with open-source models on a dedicated GPU, RAG with Qdrant and bge-m3 embeddings, n8n for workflow orchestration, Node.js backend, React frontend, Nginx as reverse proxy, Docker Compose, authentication through the company identity provider (SSO), Model Context Protocol (MCP) in the test environment

## Context

The company wanted an internal assistant able to answer questions on company documentation without sending the documents to external artificial intelligence services, on hardware it already had. The technical question was whether a single GPU on a repurposed machine could serve a business application with acceptable response times.

## What was done

The first version, started in 2025, used n8n, a local vector database and a model running on CPU, with high latency on the larger models. In 2026 the application was rewritten with a Node.js backend, a React frontend and Qdrant as the vector database, in containers behind a reverse proxy, with inference handled by Ollama on a separate host on the internal network with a dedicated GPU. The flow in production is a RAG chat: the question is turned into an embedding, Qdrant returns the relevant passages and an n8n agent generates the answer with that context; a second flow indexes the PDFs uploaded by administrators. Access goes through the company identity provider.

A separate test environment, not in service today, contains an MCP server that exposes tools filtered by department, intended for a first use case in drafting sales emails; it is not part of the production stack. In parallel, a benchmark was run between CPU and GPU and across models of different sizes, and a whitepaper on it is in preparation.

## Result

The chat over company documents is in production, with inference and the document store on the internal network; authentication, on the other hand, goes through an external identity service. Extending the assistant with tools through MCP is still at the testing stage, and the benchmark results will be published with the whitepaper.
