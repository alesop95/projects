# Piattaforma interna di intelligenza artificiale generativa

!!! tip "Progetto di punta, in continua evoluzione"
    Il più significativo tra i progetti interni descritti in questa sezione, in sviluppo attivo:
    tocca AI generativa, infrastruttura GPU dedicata, orchestrazione di agenti e integrazione con
    l'identità aziendale. Questa pagina verrà approfondita ulteriormente quando il lavoro si
    stabilizzerà.

**Settore**: azienda di servizi linguistici e traduzione professionale

**Periodo**: da confermare -- in corso

**Ruolo**: IT Manager, sviluppatore full-stack, R&D

**Tecnologie**: Ollama (LLM self-hosted su GPU dedicata), RAG (retrieval-augmented generation),
Qdrant (database vettoriale), n8n (orchestrazione di workflow AI agentica), autenticazione SSO
aziendale, reverse proxy su LAN protetta, Model Context Protocol (MCP), frontend proprietario

## Contesto

L'azienda voleva un assistente conversazionale interno basato su intelligenza artificiale
generativa, con accesso al contesto documentale aziendale, senza dipendere da servizi cloud di
terze parti per ogni interazione e con pieno controllo su dati e infrastruttura. Serviva inoltre un
modo per estendere le capacità dell'assistente con strumenti personalizzati, non limitarsi a una
semplice interfaccia di chat.

## Cosa è stato fatto

Piattaforma interna di AI generativa costruita attorno a Ollama come motore di inferenza
self-hosted su hardware dedicato con GPU, con benchmark e test di R&D per validare le scelte di
modello e hardware. Un sistema RAG con Qdrant come database vettoriale fornisce il contesto
documentale aziendale al modello. Agenti AI orchestrano flussi di lavoro personalizzati tramite
n8n, con la possibilità di comporre workflow diversi in base al profilo di chi accede. L'accesso
avviene tramite lo stesso sistema di identità aziendale (SSO) usato per gli altri servizi, così che
l'assistente riconosca l'utente e ne applichi il contesto appropriato. Il frontend è stato scritto
da zero con l'identità visiva aziendale, e funge anche da client MCP (Model Context Protocol) sulla
rete interna verso server MCP personalizzati, sia centralizzati sia distribuiti su singoli
endpoint. L'infrastruttura è esposta sulla rete interna tramite reverse proxy protetto, con
ambienti di test e produzione separati.

## Risultato

Un assistente AI interno personalizzato sul contesto aziendale, con dati e inferenza sotto
controllo diretto dell'azienda invece che affidati interamente a servizi cloud di terze parti, e
un'architettura estensibile che permette di aggiungere nuovi strumenti e flussi senza dover
riscrivere il frontend.
