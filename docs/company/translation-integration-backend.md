# Backend di integrazione per un servizio di traduzione

**Settore**: azienda di servizi linguistici e traduzione professionale

**Periodo**: 11/2025 - in corso

**Ruolo**: IT Manager, revisione di sicurezza e correzioni sul calcolo dei crediti

**Tecnologie**: Python, FastAPI, SQLite per il contesto di progetto, parsing di report Excel e di file bilingui XLIFF, integrazione con un sistema di gestione progetti di traduzione di terze parti, un motore di traduzione automatica basato su intelligenza artificiale e un servizio pubblico di traduzione automatica come fallback

## Contesto

Il servizio di traduzione rivolto ai clienti si appoggia a un sistema di gestione progetti di terze parti per l'assegnazione del lavoro e a un motore di traduzione automatica per la prima bozza. I due sistemi non comunicano nativamente nel flusso richiesto dall'azienda: serviva un livello di integrazione che collegasse il portale clienti a entrambi, calcolasse i preventivi e coprisse i casi in cui il motore principale non restituisce una traduzione.

## Cosa è stato fatto

Backend REST in Python/FastAPI che collega il portale clienti al sistema di gestione progetti e al motore di traduzione. Il flusso è diviso in tre chiamate indipendenti. La prima crea un progetto di sola analisi, ne legge il report e calcola il preventivo in crediti; la seconda crea il progetto di traduzione vero e proprio; la terza avvia in background l'esportazione dei file bilingui, fa tradurre dal motore AI i soli segmenti mancanti, ricorre al servizio di fallback per quelli che il motore non restituisce, reimporta i file e chiude i task, lasciando al project manager la revisione quando il cliente ha scelto servizi aggiuntivi. Poiché le tre chiamate non condividono una sessione, il backend conserva un contesto di progetto con i parametri che servono alla terza fase.

Il backend è un lavoro di squadra, sviluppato in gran parte da colleghi. Ho creato il repository, ne ho fatto la revisione di sicurezza e la pulizia, e ho corretto il calcolo dei crediti di preprocessing, che veniva addebitato una volta per ogni lingua di destinazione invece che una volta sola sul testo sorgente.

## Risultato

Il passaggio fra portale, gestione progetti e motore di traduzione è automatico dal preventivo alla consegna della prima bozza, con intervento umano solo dove il servizio lo prevede.
