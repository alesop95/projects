# legal-consultant

Local-first project to navigate through Italian legislation with a simple MCP server

- **Repository**: [alesop95/legal-consultant](https://github.com/alesop95/legal-consultant)
- **Tecnologie**: Python, server MCP, SQLite FTS5 (BM25), Claude Desktop, API Open Data di Normattiva
- **Periodo**: 06/2026 - 08/2026, fermo

Un server MCP (Model Context Protocol) locale che fa di Claude Desktop un assistente di ricerca sul diritto italiano. Il ragionamento avviene in Claude Desktop sull'abbonamento esistente, senza API a consumo, e il server espone tre strumenti: la ricerca full-text BM25 su SQLite FTS5 con estratti citabili, la lettura del testo integrale di un articolo per URN e le informazioni sul corpus. Non servono GPU né embedding. Un installer Windows a un clic prepara git e uv, costruisce l'indice, registra il server in Claude Desktop e pianifica l'aggiornamento giornaliero dei dati.

Il corpus parte da un clone locale del progetto italia-corpus, integrato con i codici civile, penale e di procedura civile scaricati da Normattiva. Un audit di luglio 2026 ha misurato che il clone non conteneva 9.313 delle 13.730 leggi ordinarie non abrogate, 1.584 dei 1.636 decreti-legge e la Costituzione, perché rispecchia le sole collezioni predefinite di Normattiva. Le lacune si colmano ora dall'API Open Data ufficiale di Normattiva, con un export massivo in Akoma Ntoso distribuito su più giorni, e un controllo di completezza segnala gli atti ancora assenti. A fine luglio il codice penale è stato allineato alla vigenza dopo la sentenza costituzionale 108/2026.

Ad agosto un audit per materia sulla compravendita immobiliare ha verificato diciassette atti: delle tre lacune trovate due sono state colmate, mentre la terza, la legge 448/1998, non è restituita dalla fonte e resta dichiarata assente. L'integrazione della giurisprudenza è stata valutata con uno studio di fattibilità e non è implementata. È uno strumento informativo e non una consulenza legale, e la ricerca lessicale non garantisce che un articolo sia in vigore senza una verifica su Normattiva.
