# Migrazione e containerizzazione del sito aziendale

**Settore**: azienda di servizi linguistici e traduzione professionale

**Periodo**: da confermare

**Ruolo**: IT Manager, sistemista

**Tecnologie**: WordPress, containerizzazione, DNS, hosting su infrastruttura interna

## Contesto

Il sito aziendale, basato su WordPress, era ospitato su un provider di hosting esterno: l'azienda
ha deciso di internalizzarne l'infrastruttura, portandolo sulla rete interna sotto il proprio
controllo diretto invece di dipendere da un fornitore esterno.

## Cosa è stato fatto

Migrazione 1:1 del sito WordPress aziendale da un hosting esterno a una macchina virtuale sulla
rete interna, containerizzando l'applicazione per isolamento e portabilità, con redirect DNS per
servirlo sulla LAN mantenendo la continuità di accesso per gli utenti.

## Risultato

Sito aziendale interamente sotto controllo interno, containerizzato per una gestione più semplice
di aggiornamenti e backup, senza discontinuità di servizio percepita durante la migrazione.
