# legal-consultant

Local-first project to navigate through Italian legislation with a simple MCP server

- **Repository**: [alesop95/legal-consultant](https://github.com/alesop95/legal-consultant)
- **Linguaggio principale**: Python
- **Ultimo aggiornamento**: 2026-07-06
- **Cartella locale**: `legal-consultant`

Un server MCP (Model Context Protocol) locale che trasforma Claude Desktop in un assistente di ricerca sul diritto italiano senza alcun costo di API a consumo: tutto il ragionamento avviene in Claude Desktop stesso, che chiama gli strumenti esposti da questo server, quindi funziona su un abbonamento Claude esistente invece che su un uso di API a misurazione. Il corpus giuridico è un clone locale del progetto `italia-corpus` mantenuto dalla community, tenuto aggiornato con `git pull` e reindicizzazione incrementale, più una manciata di codici fondamentali (civile, penale, procedura civile) recuperati direttamente da Normattiva perché il loro testo integrale manca in quel corpus. La ricerca è deliberatamente leggera: ricerca full-text BM25 su SQLite FTS5, senza GPU e senza embedding, il che mantiene veloce l'indicizzazione e rende l'intero strumento eseguibile su hardware ordinario.

Al modello sono esposti tre strumenti: una ricerca BM25 che restituisce estratti citabili, una lookup che recupera il testo integrale di un dato articolo tramite il suo URN, e uno strumento di corpus-info. Un installer Windows a un clic prepara git e uv, costruisce l'indice, registra il server MCP in Claude Desktop e imposta un'attività pianificata giornaliera per aggiornare il corpus. Il README dichiara esplicitamente che si tratta di uno strumento informativo, non di consulenza legale, e che la ricerca lessicale BM25 non può garantire che un articolo sia ancora in vigore senza verificare direttamente su Normattiva.
