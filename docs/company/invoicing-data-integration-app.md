# Applicazione di integrazione con il gestionale e parsing dati di fatturazione

**Settore**: azienda di servizi linguistici e traduzione professionale

**Periodo**: 11/2024 - in corso

**Ruolo**: IT Manager: presa in carico, documentazione e messa in esercizio su macchina virtuale

**Tecnologie**: Next.js e React, Python con Flask, XML-RPC verso un gestionale ERP open source, elaborazione di file Excel, Ubuntu su macchina virtuale

## Contesto

Per un grande cliente la fatturazione mensile richiede un report che il gestionale non produce da solo: i dati che il cliente chiede, cioè quantità e tariffe per ogni ordine, stanno sulle righe degli ordini e non sulla testata, e ricostruirli a mano ogni mese era lento e soggetto a errori.

## Cosa è stato fatto

L'applicazione è stata sviluppata da un ex collega; io l'ho presa in carico, l'ho documentata passo per passo e l'ho messa in esercizio su una macchina virtuale interna, dove prima girava su una singola postazione. Il frontend Next.js e il backend Python Flask ricevono il riepilogo mensile inviato dal cliente in Excel, leggono dal gestionale via XML-RPC le righe degli ordini corrispondenti e restituiscono il report completo, da cui parte la fatturazione.

## Risultato

La rendicontazione mensile per il cliente è una procedura di caricamento e scaricamento invece di una ricostruzione manuale, e non dipende più dal computer di una singola persona.
