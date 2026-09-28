# Compilazione assistita dei questionari di sicurezza e privacy

**Settore**: azienda di servizi linguistici e traduzione professionale

**Periodo**: 08/2026 - in corso

**Ruolo**: IT Manager, sviluppatore

**Tecnologie**: Python, openpyxl, python-docx, pypdf, pytest

## Contesto

Nella qualifica fornitori i clienti inviano questionari di sicurezza e privacy e documenti contrattuali da compilare: questionari in Excel, checklist in Word sul trattamento dei dati per conto del cliente, nomine, moduli per la notifica delle violazioni. Le domande si ripetono da un cliente all'altro con formulazioni diverse, e ogni risposta va data in modo coerente con quelle già fornite e con la postura di sicurezza reale dell'azienda.

## Cosa è stato fatto

Una pipeline in Python che riconosce da sola la struttura del documento ricevuto, Excel o Word, cerca le risposte in una base di conoscenza di coppie domanda-risposta e produce una bozza compilata che conserva formattazione, stili e celle del file originale; le risposte validate tornano poi nella base di conoscenza. Il motore di corrispondenza fra domande è scritto in Python puro, e le dipendenze sono ridotte alle librerie per leggere e scrivere i formati d'ufficio. Codice e dati sono separati per costruzione: il repository contiene solo l'impianto, mentre la base di conoscenza e i documenti dei clienti stanno fuori, in una radice dichiarata nella configurazione locale, e un controllo automatico verifica che nessun contenuto di un cliente entri nei file versionati. Le prove girano su documenti inventati.

## Risultato

La compilazione di un questionario parte da una bozza coerente con le risposte già date invece che da un foglio vuoto. Il ramo Excel è in uso; il ramo Word ha superato le prove su documenti reali in alcune parti, e la prova completa su un documento reale resta da fare.
