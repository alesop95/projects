# Migrazione di un gestionale legacy a un sistema operativo supportato

**Settore**: azienda di servizi linguistici e traduzione professionale

**Periodo**: 02/2026 - in corso

**Ruolo**: IT Manager, sistemista

**Tecnologie**: Ubuntu 10.04 LTS → Ubuntu 24.04 LTS, Docker, contenitori separati per esercizio e collaudo, database relazionale, Proxmox VE

## Contesto

Il gestionale che l'azienda ha usato per il lavoro quotidiano fino al 2021, un'applicazione web della metà degli anni 2000, oggi serve come archivio: lo si consulta internamente per i dati storici. Girava su un server Ubuntu 10.04 LTS, una distribuzione fuori supporto da molti anni, dentro l'infrastruttura virtualizzata aziendale.

## Cosa è stato fatto

Il gestionale è stato ricostruito su una nuova macchina virtuale Ubuntu 24.04 LTS sull'infrastruttura Proxmox, con l'applicazione e il suo database in contenitori. Sulla stessa macchina girano due istanze indipendenti, una di esercizio e una di collaudo, ciascuna con il proprio database, così che le modifiche si provino prima di toccare l'archivio consultato dagli utenti. La migrazione è stata condotta come IT Manager, con il contributo del gruppo di lavoro.

## Risultato

I dati storici sono consultabili da un'istanza che gira su un sistema operativo supportato, con un ambiente di collaudo separato da quello di esercizio. Il lavoro è in corso: il vecchio server è ancora acceso e la sua dismissione resta da completare.
