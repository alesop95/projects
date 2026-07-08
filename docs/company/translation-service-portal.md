# Scenia®: portale SaaS multilingua per un servizio di traduzione

!!! tip "Prodotto pubblico e marchio registrato"
    Scenia® è live su [scenia.it](https://scenia.it/) ed è un marchio registrato dell'azienda: a
    differenza degli altri progetti in questa sezione, il nome del prodotto e l'indirizzo pubblico
    non sono soggetti ad anonimizzazione. Restano generiche solo le informazioni interne
    (integrazioni con sistemi terzi, processi) che non compaiono già sul sito pubblico.

**Settore**: azienda di servizi linguistici e traduzione professionale

**Periodo**: 10/2024 - in corso

**Ruolo**: IT Manager, sviluppatore full-stack

**Tecnologie**: Next.js (App Router), React, TypeScript strict, Prisma con adapter MariaDB, Zod,
bcrypt, JWT, Tailwind CSS, MJML per le email transazionali, upload in streaming, pnpm workspace,
deployment su VPS con PM2 e Nginx

## Contesto

Il servizio di traduzione rivolto ai clienti aveva bisogno di un portale SaaS proprio, con un
modello di accesso su più livelli (cliente finale, project manager, amministratore,
super-amministratore) e un flusso completo di gestione degli incarichi di traduzione, dalla
richiesta di preventivo al caricamento dei file fino al completamento, invece di dipendere da
comunicazioni manuali sparse tra email e fogli di calcolo.

## Cosa è stato fatto

Architettura domain-driven con separazione netta tra dominio (`core`, logica di business
indipendente dal framework) e infrastruttura (`infra`, implementazioni concrete verso database e
servizi esterni), collegate tramite interfacce di repository e un composition root unico che
assembla i servizi per ogni richiesta. Autorizzazione basata su quattro ruoli (utente finale,
project manager, amministratore, super-amministratore), con le regole di visibilità dei dati
applicate nel livello di servizio e non nelle singole rotte, così che la logica di scoping resti
in un solo posto invece di essere duplicata pagina per pagina.

Il dominio centrale è l'incarico di traduzione: ogni incarico ha un proprio workflow di stato, i
file allegati in ingresso e i file di output collegati, una o più coppie di lingua sorgente e
lingua di destinazione, e un'analisi automatica che genera una stima preliminare prima
dell'assegnazione. La fatturazione ai clienti funziona a crediti prepagati, con un registro delle
transazioni che permette un modello self-service invece della fatturazione manuale a consuntivo.
Il concetto di "consumer" unifica clienti aziendali e clienti privati sotto un'unica astrazione, in
modo che il resto del dominio non debba distinguere i due casi. Cancellazione soft con colonne di
audit su tutte le entità principali, per mantenere uno storico anche dei record rimossi.

Le integrazioni esterne (un motore di memoria di traduzione, un gestionale ERP/CRM per
l'anagrafica di aziende e contatti, un servizio di stima prezzo) sono istanziate in modo lazy dal
composition root, così l'applicazione non blocca l'intera richiesta se un'integrazione esterna è
lenta o non risponde. Il caricamento dei file avviene in streaming, senza bufferizzare in memoria
gli allegati di grandi dimensioni, con lo storage tenuto fuori dalla web root: l'introduzione di
questo meccanismo in produzione ha richiesto anche un intervento di tuning su Nginx per disattivare
il buffering del proxy sulle rotte API, altrimenti gli upload di file grandi fallivano in silenzio.
L'internazionalizzazione dell'interfaccia è implementata da zero, senza libreria di terze parti,
con risoluzione della lingua per cookie di sessione, poi header del browser, poi lingua di
default: una scelta tecnica che rispecchia a livello di prodotto la natura multilingua del
servizio che il portale rappresenta.

## Risultato

Un punto di accesso self-service in produzione su [scenia.it](https://scenia.it/), con
autorizzazione a più livelli, fatturazione a crediti che riduce il lavoro manuale di
fatturazione a consuntivo, e una stima automatica del preventivo che accorcia il tempo tra la
richiesta del cliente e l'assegnazione dell'incarico.
