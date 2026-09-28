# Deploy containerizzato di una piattaforma open source di project management

**Settore**: azienda di servizi linguistici e traduzione professionale

**Periodo**: 10/2025, installata e non in uso

**Ruolo**: IT Manager, sistemista

**Tecnologie**: OpenProject self-hosted con Docker Compose, Ubuntu 24.04 su Proxmox VE, PostgreSQL

## Contesto

Per pianificare attività con dipendenze e scadenze serviva valutare uno strumento con diagrammi di Gantt. Un confronto fra quattro alternative, fra cui soluzioni desktop, strumenti testuali e un componente aggiuntivo per fogli di calcolo, ha portato a provare OpenProject, progetto open source di project management.

## Cosa è stato fatto

Deploy containerizzato di OpenProject con il Docker Compose ufficiale su una macchina virtuale interna, con la configurazione di rete per raggiungerlo dalle postazioni e la posta in uscita per le notifiche. Dopo un esaurimento dello spazio disco la macchina è stata ridimensionata.

## Risultato

Un'istanza funzionante della piattaforma sulla rete interna. Per ora non è in uso: il lavoro documentato qui è l'installazione, non l'adozione dello strumento.
