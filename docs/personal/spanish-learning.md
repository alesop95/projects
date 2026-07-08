# spanish-learning

_Nessuna descrizione su GitHub._

- **Repository**: [alesop95/spanish-learning](https://github.com/alesop95/spanish-learning)
- **Linguaggio principale**: Python
- **Ultimo aggiornamento**: 2026-07-07
- **Cartella locale**: `spanish-learning`

Non si tratta di un'applicazione software ma di un sistema agentico di tutoraggio di spagnolo costruito sopra Claude Code. Tre livelli disaccoppiati svolgono il lavoro: una knowledge base locale assemblata da uno script di ingestion a costo LLM zero che percorre una libreria personale di libri e documenti (PDF, DOCX, PPTX, XLSX, HTML, con un fallback OCR per i volumi scansionati) e produce una cache Markdown con un indice per documento; un motore di ripetizione dilazionata pensato per funzionare tramite il bridge `ankimcp/anki-mcp-server` verso un'installazione locale di Anki; e uno strato di orchestrazione di tre subagent Claude, tutor, kb-retriever ed examiner, collegati a comandi slash (`/profile`, `/learn`, `/review`) che costruiscono un profilo dell'apprendente e una roadmap pedagogica, erogano lezioni fondate solo su materiale sorgente citato, e chiudono ogni sessione con una verifica ad active recall prima di segnare un modulo come completato.

Un artefatto concreto gia' generato e' un mazzo Anki personalizzato di falsi amici italiano-spagnolo, prodotto da un piccolo script a partire da una lista di parole curata a mano, poiche' nessun mazzo pubblico copre questo specifico pattern di interferenza. Secondo il tracker di stato del progetto stesso, la knowledge base e il primo profilo dell'apprendente sono costruiti, ma Anki desktop e AnkiConnect non sono ancora collegati live e nessuna lezione e' stata effettivamente erogata end-to-end, quindi questo progetto si legge meglio come uno scaffold funzionante per un workflow di apprendimento personale piuttosto che come uno strumento finito.
