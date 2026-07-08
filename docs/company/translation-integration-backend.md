# Backend di integrazione per un servizio di traduzione

**Settore**: azienda di servizi linguistici e traduzione professionale

**Periodo**: 03/2025 - in corso

**Ruolo**: IT Manager, sviluppatore backend

**Tecnologie**: Python, FastAPI, integrazione con un sistema di gestione progetti di traduzione
di terze parti, un motore di traduzione automatica basato su intelligenza artificiale, un
servizio di traduzione automatica pubblico come fallback

## Contesto

Il servizio di traduzione rivolto ai clienti si appoggia a un sistema di gestione progetti di
terze parti per l'assegnazione del lavoro e a un motore di traduzione automatica per la
prima bozza. I due sistemi non comunicano nativamente nel flusso richiesto dall'azienda: serviva
un livello di integrazione che orchestrasse le chiamate tra i due, con una copertura di
continuità quando il motore principale non è disponibile o non copre una combinazione linguistica.

## Cosa è stato fatto

Backend REST in Python/FastAPI che fa da ponte tra il sistema di gestione progetti e il motore di
traduzione, con un servizio di traduzione automatica pubblico usato come fallback quando il
motore principale non risponde o non copre la lingua richiesta. Il flusso è organizzato in tre
fasi (recupero del progetto, invio al motore di traduzione, raccolta e normalizzazione del
risultato), con gestione degli errori e retry sul livello di integrazione. Documentazione tecnica
strutturata per la ripresa del lavoro tra sessioni non consecutive.

## Risultato

Automatizza un passaggio che prima richiedeva intervento manuale per instradare ogni progetto tra
i due sistemi, riducendo il tempo di attesa tra l'apertura di un progetto di traduzione e la
disponibilità della prima bozza automatica.
