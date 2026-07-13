# paypal-transaction-data

_Nessuna descrizione su GitHub._

- **Repository**: [alesop95/paypal-transaction-data](https://github.com/alesop95/paypal-transaction-data)
- **Linguaggi**: Python, PowerShell, Shell, JavaScript
- **Data di inizio**: 2026-06
- **Ultimo aggiornamento**: 2026-07-06
- **Cartella locale**: `paypal-transaction-data`

Uno strumento a riga di comando in Python che estrae lo storico delle transazioni dalla API REST di PayPal e lo sincronizza con un Google Sheet, mantenendo un registro continuo a scopo di contabilità. Estrae i campi rilevanti per la riconciliazione contabile, come identificativi di transazione e di riferimento, importi lordi e netti, commissioni, valuta, stato e dettagli del pagatore, e li scrive in un foglio formattato saltando i record già sincronizzati in precedenza. Esiste anche un percorso di esportazione separato verso Excel, accanto a quello per Google Sheets.

Lo strumento supporta sia la modalità sandbox sia quella live di PayPal e può essere eseguito come sincronizzazione una tantum, come sincronizzazione su un intervallo di date specifico, oppure come job pianificato a un intervallo configurabile, con un sottocomando di stato per verificare la connettività alla API. Le credenziali sia di PayPal sia di Google restano fuori dal controllo di versione tramite variabili d'ambiente e un file di credenziali OAuth. È un'utility personale di contabilità costruita per eliminare il lavoro manuale di copiare gli estratti conto PayPal in un foglio di calcolo, non un prodotto finanziario general-purpose: il repository contiene intenzionalmente solo il codice e le istruzioni di setup, non dati di transazione reali.
