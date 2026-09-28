# Migrazione del software di rilevazione presenze

**Settore**: azienda di servizi linguistici e traduzione professionale

**Periodo**: 02/2025, concluso

**Ruolo**: IT Manager, sistemista

**Tecnologie**: Windows Server 2012 → Windows Server 2022, VMware vSphere → Proxmox VE, IIS, MariaDB, lettori biometrici di rete, diagnosi di rete su VLAN

## Contesto

Il sistema di rilevazione presenze e controllo accessi, due lettori biometrici con il loro software di gestione su una macchina virtuale Windows Server 2012, doveva lasciare il vecchio host di virtualizzazione, sostituito da un nuovo server con Proxmox. Nello stesso mese il lettore d'ingresso ha smesso di sincronizzare le timbrature, mentre quello d'uscita, collegato al primo su linea seriale RS-485 in configurazione master e slave, continuava a funzionare.

## Cosa è stato fatto

Il lavoro, dal software alla configurazione alla rete fino alla migrazione della macchina virtuale e dei servizi, è stato svolto dall'IT Manager; restano fuori l'aggiornamento del firmware del nuovo lettore, gestito a parte, e il montaggio a parete, eseguito dall'elettricista. La diagnosi del lettore ha escluso cavi e switch e ha mostrato un sintomo di segmentazione: le risposte arrivavano dal gateway di un'altra VLAN e non dal dispositivo, perché la postazione di prova stava su una rete diversa da quella del lettore, senza instradamento fra le due. Un ripristino delle impostazioni di rete lo ha riportato in funzione per un giorno; il guasto si è poi ripresentato in una forma non risolvibile via software e il lettore è stato sostituito con un nuovo apparato. Lo spostamento diretto della macchina virtuale sul nuovo virtualizzatore la bloccava in un ciclo di riavvii, così i servizi, cioè l'applicazione web su IIS e i database su MariaDB, sono stati migrati su una nuova macchina Windows Server 2022 invece di recuperare la vecchia.

## Risultato

Rilevazione presenze e controllo accessi girano su Windows Server 2022 sulla nuova infrastruttura virtualizzata, e il vecchio host è stato rimosso dall'inventario. La migrazione si è chiusa entro febbraio 2025.
