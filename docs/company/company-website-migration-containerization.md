# Migrazione, containerizzazione ed evoluzione del sito aziendale

**Settore**: azienda di servizi linguistici e traduzione professionale

**Periodo**: da confermare - in corso

**Ruolo**: IT Manager, architettura degli ambienti, sistemista

**Tecnologie**: WordPress, Docker Compose, Caddy, Proxmox VE, Next.js, Payload CMS, PostgreSQL, GitHub Actions

## Contesto

Il sito aziendale, basato su WordPress, era ospitato da un provider esterno, e un rifacimento commissionato a un'agenzia esterna non era arrivato a un risultato pubblicabile. L'azienda ha deciso di riportare il sito sotto il proprio controllo diretto, prima mettendo in sicurezza ciò che esisteva, poi ricostruendolo internamente su uno stack proprio.

## Cosa è stato fatto

La prima fase è la migrazione: il sito WordPress è stato portato 1:1 dall'hosting esterno a una macchina virtuale sulla rete interna, containerizzato (web server, database e reverse proxy in container separati) e servito in LAN con redirect DNS. Questa copia resta come ambiente di riferimento, in sola lettura, per la migrazione dei contenuti.

La seconda fase, in corso, è la ricostruzione. Il nuovo sito si sviluppa su Next.js con Payload come CMS e PostgreSQL come database, con uno schema dei contenuti progettato da zero invece di ereditare la struttura di WordPress. Gli ambienti sono separati per funzione: sviluppo e staging su una macchina virtuale interna raggiungibile solo dalla LAN, produzione su un server cloud dedicato e già messo in sicurezza (accesso SSH solo a chiave, firewall ristretto ai servizi pubblici), che non compila niente ma esegue l'immagine container prodotta dalla pipeline di build. Sono pianificati backup cifrati con copia off-site e una prova di ripristino prima della messa in produzione.

## Risultato

Il sito esistente è oggi interamente sotto controllo interno e containerizzato. L'infrastruttura del nuovo sito è pronta sui due ambienti, e lo sviluppo applicativo è in corso: la pubblicazione non è ancora avvenuta.
