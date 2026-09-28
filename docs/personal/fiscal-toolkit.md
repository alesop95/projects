# fiscal-toolkit

- **Repository**: [alesop95/fiscal-toolkit](https://github.com/alesop95/fiscal-toolkit)
- **Tecnologie**: Node.js, TypeScript, SQLite (node:sqlite), Vitest
- **Periodo**: 07/2026 - in corso

Strumento personale per capire la fiscalità di un lavoratore dipendente in Italia: dal lordo annuo (RAL) al netto, con il peso di IRPEF, detrazioni, cuneo fiscale, contributi INPS e addizionali. Il calcolo è deterministico e spiegabile: ogni voce del risultato porta il parametro usato e la norma da cui viene. I parametri stanno in file versionati per anno d'imposta, aggiornati a mano a ogni Legge di Bilancio, e si verificano contro il testo di legge indicizzato dal progetto legal-consultant.

Stato: il motore di calcolo per il 2025 e il 2026 è completo e coperto da test, con una CLI e una prima interfaccia locale che mostrano la composizione della retribuzione e il confronto fra anni. Il confronto fra lavoro dipendente e partita IVA è previsto ma non ancora implementato. La fase successiva, la lettura dei documenti fiscali reali (Certificazione Unica, cedolini), non è iniziata. Non è consulenza fiscale.
