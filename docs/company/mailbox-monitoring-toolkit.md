# Toolkit di monitoraggio caselle di posta aziendali

**Settore**: azienda di servizi linguistici e traduzione professionale

**Periodo**: 05/2026 - in corso

**Ruolo**: IT Manager, sistemista

**Tecnologie**: PowerShell, Microsoft Graph, Exchange Online PowerShell, applicazione registrata con autenticazione a certificato, Python, openpyxl, SQLite, Utilità di pianificazione di Windows

## Contesto

Le caselle di posta aziendali si riempivano senza preavviso, e una casella principale piena smette di ricevere posta. Non esisteva uno storico dell'occupazione su cui valutare la crescita delle singole caselle.

## Cosa è stato fatto

Uno script PowerShell eseguito ogni mattina da un'attività pianificata legge tutte le caselle tramite Microsoft Graph ed Exchange Online, raccoglie 22 metriche per ciascuna (occupazione e quota della casella principale e dell'archivio, crescita negli ultimi 30 giorni, inattività, inoltri automatici, blocchi legali) e le salva in un database SQLite che conserva lo storico senza scadenza. Lo stesso script calcola le soglie e invia gli avvisi. L'autenticazione usa un'applicazione registrata con certificato, quindi l'esecuzione non richiede accessi interattivi. Casella principale e archivio online sono trattati come due problemi distinti: al superamento dell'80% o del 95% il reparto IT riceve un riepilogo e il titolare della casella una notifica personale, con un testo diverso per ciascuna delle due soglie, mentre le caselle di sale e attrezzature sono escluse. Python ha un ruolo circoscritto: due script producono i report Excel giornalieri, separati fra caselle con licenza e caselle funzionali, e un report settimanale di trend.

## Risultato

Il toolkit è in esercizio quotidiano da maggio 2026 e ha accumulato uno storico giornaliero dell'occupazione di tutte le caselle, con i report settimanali di trend generati in automatico.
