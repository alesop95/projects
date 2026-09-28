# Toolkit di esportazione e archiviazione di caselle di posta e chat

**Settore**: azienda di servizi linguistici e traduzione professionale

**Periodo**: 06/2026, concluso

**Ruolo**: IT Manager, sistemista

**Tecnologie**: PowerShell, Exchange Online PowerShell, Microsoft Graph, Outlook classico (automazione COM), file PST, SHA-256, Microsoft Word (automazione COM)

## Contesto

Due caselle di posta condivise avevano l'archivio online pieno. Prima di liberare spazio serviva una copia statica e verificata dell'intero contenuto, casella primaria e archivio, su un archivio di rete. Nello stesso periodo è emersa un'esigenza affine sulle chat aziendali: estrarre messaggi di canali e conversazioni in una forma consultabile per audit e ricerca.

## Cosa è stato fatto

Il metodo previsto per la posta era l'export lato server tramite eDiscovery; la versione attuale dello strumento richiede però una licenza di livello enterprise per chiunque lavori ai casi, e si è scelto di non acquistarla. L'export è stato quindi eseguito da Outlook classico, spezzando per intervallo di date le cartelle più grandi, perché i flussi lunghi dall'archivio online si interrompevano. La completezza è stata provata contando gli elementi di ogni file esportato cartella per cartella e confrontandoli con i conteggi lato server, al netto delle cartelle di sistema non esportabili, dato che il peso di un file fermo non prova che l'export sia finito. I file sono stati copiati sull'archivio di rete con verifica SHA-256. Gli script PowerShell si limitano a leggere ed esportare; la cancellazione del contenuto è una fase separata, descritta in una guida a parte e non automatizzata.

Per le chat è stato scritto uno script PowerShell che legge messaggi di canali e conversazioni tramite Microsoft Graph, con un'applicazione registrata che ha soli permessi di lettura concessi dall'amministratore. I filtri si combinano fra loro: mittenti, finestra di date e ore, parole chiave con diverse modalità di confronto, menzioni, allegati e importanza. L'esportazione è incrementale grazie a un checkpoint con delta token, gestisce la limitazione delle richieste con attese progressive e scarica le immagini inline; l'uscita è un file CSV o JSON con le statistiche per utente e per giorno. Un secondo script converte l'export in un documento Word in ordine cronologico, con le immagini incorporate nel testo.

## Risultato

Il contenuto delle due caselle è archiviato su rete con conteggi coincidenti per cartella e checksum verificati, e il runbook e gli script sono parametrici e riutilizzabili su altre caselle. Lo svuotamento delle caselle non è ancora stato eseguito. Lo script delle chat si usa quando serve un'estrazione per audit o ricerca.
