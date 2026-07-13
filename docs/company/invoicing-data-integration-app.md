# Applicazione di integrazione con il gestionale e parsing dati di fatturazione

**Settore**: azienda di servizi linguistici e traduzione professionale

**Periodo**: da confermare

**Ruolo**: IT Manager, sviluppatore full-stack

**Tecnologie**: React, XML-RPC, integrazione con un gestionale ERP/CRM open source, parsing di
dati strutturati

## Contesto

I dati di fatturazione aziendale vivono in un gestionale ERP che espone un'interfaccia XML-RPC:
serviva un'applicazione proprietaria capace di interrogare quel gestionale ed estrarre i dati di
fatturazione in un formato utilizzabile da altri processi interni, con un ambiente di test separato
da quello di produzione.

## Cosa è stato fatto

Applicazione React che comunica via XML-RPC con un gestionale ERP/CRM open source per estrarre i
dati di fatturazione, con un parsing avanzato per normalizzare e interpretare i dati strutturati
restituiti dal gestionale. Adotta un flusso di gestione test/produzione con una propria filosofia
di promozione delle modifiche dall'ambiente di sviluppo a quello di produzione, distinta da quella
di altri progetti interni.

## Risultato

Un livello di integrazione dedicato tra il gestionale e i processi che consumano i dati di
fatturazione, con un ambiente di test isolato che permette di validare le modifiche prima del
rilascio.
