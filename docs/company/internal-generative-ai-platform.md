# Piattaforma interna di intelligenza artificiale generativa

**Settore**: azienda di servizi linguistici e traduzione professionale

**Periodo**: 03/2025 - in corso

**Ruolo**: IT Manager, sviluppatore full-stack, R&D

**Tecnologie**: Ollama con modelli open source su GPU dedicata, RAG con Qdrant ed embedding bge-m3, n8n per l'orchestrazione dei workflow, backend Node.js, frontend React, Nginx come reverse proxy, Docker Compose, autenticazione con l'identità aziendale (SSO), Model Context Protocol (MCP) nell'ambiente di test

## Contesto

L'azienda voleva un assistente interno che rispondesse sulla documentazione aziendale senza inviare i documenti a servizi di intelligenza artificiale esterni, su hardware già disponibile. La domanda tecnica era se una sola GPU su una macchina riutilizzata bastasse a servire un'applicazione aziendale con tempi di risposta accettabili.

## Cosa è stato fatto

La prima versione, avviata nel 2025, usava n8n, un database vettoriale locale e un modello eseguito su CPU, con latenze alte sui modelli più grandi. Nel 2026 l'applicazione è stata riscritta con un backend Node.js, un frontend React e Qdrant come database vettoriale, in container dietro un reverse proxy, con l'inferenza affidata a Ollama su un host della rete interna con GPU dedicata. Il flusso in produzione è una chat RAG: la domanda viene trasformata in embedding, Qdrant restituisce i passaggi pertinenti e un agente n8n genera la risposta con quel contesto; un secondo flusso indicizza i PDF caricati dagli amministratori. L'accesso passa per l'identità aziendale.

In un ambiente di test separato, oggi non in esercizio, esiste un server MCP che espone strumenti filtrati per reparto, pensato per un primo caso d'uso nella preparazione di bozze di email commerciali; non fa parte dello stack di produzione. In parallelo è stato condotto un benchmark fra CPU e GPU e fra modelli di taglia diversa, su cui è in preparazione un whitepaper.

## Risultato

La chat su documenti aziendali è in produzione, con inferenza e archivio documentale sulla rete interna; l'autenticazione passa invece da un servizio di identità esterno. L'estensione con strumenti tramite MCP è ancora in fase di test, e i risultati del benchmark saranno pubblicati con il whitepaper.
