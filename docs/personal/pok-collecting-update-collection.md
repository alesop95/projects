# pok-collecting_update_collection

Just a personal project to update my collection

- **Repository**: [alesop95/pok-collecting_update_collection](https://github.com/alesop95/pok-collecting_update_collection)
- **Tecnologie**: Python, xlwings, openpyxl, SQLite, API REST di CardTrader
- **Periodo**: 05/2026 - 06/2026, fermo

Un compagno di price-tracking per una collezione personale di carte Pokémon TCG tenuta in una cartella di lavoro Excel. Lo script tratta il foglio di calcolo come fonte di verità: legge le carte possedute direttamente dalla cartella di lavoro tramite automazione COM (xlwings), recupera i prezzi di mercato correnti dall'API REST CardTrader v2 e scrive una cache di lookup con formule pronte da incollare, così che Excel mostri prezzi aggiornati attraverso ricerche in stile XLOOKUP. Un database SQLite conserva uno storico dei prezzi in sola aggiunta, così che le tendenze non si perdano fra un'esecuzione e l'altra.

È nato dopo la chiusura dell'API pubblica dei prezzi di Cardmarket, avvenuta intorno al 2024 secondo la documentazione del progetto, che ha lasciato CardTrader come fonte dei dati. Uno script di discovery associa per fuzzy matching i nomi dei fogli della cartella di lavoro al catalogo delle espansioni dell'API, perché i nomi dei fogli non corrispondono agli identificativi dell'API. Le formule di lookup sono generate in sintassi Excel italiana, con il punto e virgola come separatore e i nomi di funzione localizzati.
