# Scenia®: portale SaaS multilingua per un servizio di traduzione

!!! tip "Prodotto pubblico e marchio registrato"
    Scenia® è in produzione su [scenia.it](https://scenia.it/) ed è un marchio registrato dell'azienda: a differenza degli altri progetti in questa sezione, il nome del prodotto e l'indirizzo pubblico non sono soggetti ad anonimizzazione. Restano generiche solo le informazioni interne (integrazioni con sistemi terzi, processi) che non compaiono già sul sito pubblico.

**Settore**: azienda di servizi linguistici e traduzione professionale

**Periodo**: 10/2024 - in corso

**Ruolo**: IT Manager, sviluppo dell'integrazione con il gestionale aziendale

**Tecnologie**: Next.js (App Router), React, TypeScript strict, Prisma su MariaDB, Zod, bcrypt, JWT, Tailwind CSS, MJML per le email transazionali, upload in streaming, pnpm workspace, deployment su VPS con PM2 e Nginx

## Contesto

Il servizio di traduzione rivolto ai clienti aveva bisogno di un portale SaaS proprio, con un modello di accesso su più livelli e un flusso completo di gestione degli incarichi di traduzione, dalla richiesta di preventivo al caricamento dei file fino al completamento.

## Cosa è stato fatto

Il portale è un prodotto di squadra: il codice è scritto in gran parte da colleghi, e io seguo il progetto come IT Manager dal suo avvio. Il mio contributo diretto al codice, dal 2026, riguarda l'integrazione con il gestionale aziendale, descritta nell'ultimo capoverso.

L'architettura è domain-driven, con separazione netta tra dominio (`core`, logica di business indipendente dal framework) e infrastruttura (`infra`, implementazioni concrete verso database e servizi esterni), collegate tramite interfacce di repository e un composition root unico che assembla i servizi per ogni richiesta. L'autorizzazione si basa su cinque ruoli (utente finale, capo team, project manager, amministratore, super-amministratore), con le regole di visibilità dei dati applicate nel livello di servizio e non nelle singole rotte, così la logica di scoping resta in un solo posto.

Il dominio centrale è l'incarico di traduzione: ogni incarico ha un proprio workflow di stato, i file in ingresso e in uscita, una o più coppie di lingue e un'analisi automatica che stima il costo prima dell'avvio. La fatturazione ai clienti funziona a crediti prepagati di due tipi, standard e premium, con un registro delle transazioni; dal 2026 il calcolo dei crediti premium avviene dentro il portale invece che nel servizio esterno. Il concetto di "consumer" unifica sotto un'unica astrazione clienti privati, aziende e team, e il ruolo di capo team, aggiunto ai quattro iniziali, permette a un'azienda cliente di distribuire crediti e progetti fra i propri gruppi di lavoro.

Le integrazioni esterne, cioè il sistema di gestione progetti e memorie di traduzione e il backend di calcolo e orchestrazione, sono istanziate in modo lazy dal composition root, così una dipendenza lenta non blocca l'intera richiesta. Il caricamento dei file avviene in streaming, senza bufferizzare in memoria gli allegati grandi, con lo storage fuori dalla web root; in produzione ha richiesto di disattivare il buffering del proxy Nginx sulle rotte API, senza il quale gli upload grandi fallivano senza errori. Il portale accetta anche cartelle e archivi con più lingue di destinazione. L'interfaccia, in italiano e inglese, ha un'internazionalizzazione scritta senza librerie di terze parti, con risoluzione della lingua per cookie, poi header del browser, poi lingua predefinita.

Il mio contributo di codice è l'integrazione con il gestionale aziendale: la creazione automatica degli ordini di vendita all'avvio di un incarico, con la mappatura di clienti e servizi. L'integrazione è stata sviluppata su un ramo dedicato, è stata ritirata dall'ambiente di collaudo a luglio 2026 e oggi è sospesa.

## Risultato

Un portale self-service in produzione su [scenia.it](https://scenia.it/), con cui i clienti aziendali caricano i documenti, ricevono una stima in crediti e avviano l'incarico senza passare da una richiesta manuale.
