# Migrazione e gestione del ciclo di vita di licenze software

**Settore**: azienda di servizi linguistici e traduzione professionale

**Periodo**: 01/2025 - 03/2025

**Ruolo**: IT Manager, responsabile della migrazione e sistemista

**Tecnologie**: Windows Server 2012 R2 → Windows Server 2022, Proxmox VE, gestori di licenze di rete a utenza concorrente, installazione amministrativa da condivisione di rete

## Contesto

Uno strumento di riconoscimento ottico dei caratteri (OCR) e uno strumento di traduzione assistita (CAT) usano licenze di rete, distribuite alle postazioni da un gestore di licenze su server. Il gestore dell'OCR girava su una macchina virtuale Windows Server 2012 R2 ospitata dal vecchio host di virtualizzazione, che all'inizio del 2025 veniva sostituito da un nuovo server con Proxmox: il gestore andava quindi spostato su un nuovo Windows Server 2022 senza lasciare le postazioni senza licenza.

## Cosa è stato fatto

Il lavoro è stato impostato e condotto dall'IT Manager, che ne ha deciso l'ordine dei passi, le verifiche e le scelte sul perimetro delle licenze, con l'aiuto di un collega presente solo al mattino; il fornitore interviene soltanto quando cambia la fornitura. Le licenze dell'OCR sono perpetue ma senza contratto di manutenzione, quindi l'assistenza del fornitore si limitava ad attivazioni e pacchetti di installazione. Il primo pacchetto scaricabile in autonomia installava un gestore di versione successiva, incompatibile con le licenze possedute, ed è stato scartato a favore del pacchetto della versione corretta; la versione dello strumento OCR è rimasta la stessa. L'attivazione offline non andava a buon fine e la copia a mano delle cartelle di licenza dal vecchio server si è rivelata inutile, perché la configurazione non vive in file copiabili: il nuovo gestore è stato attivato online. A quel punto vecchio e nuovo gestore esponevano lo stesso seriale, e la concorrenza effettiva avrebbe superato il numero di licenze acquistate; si è quindi deciso di reinstallare rapidamente le postazioni e di dismettere il vecchio gestore. Per la reinstallazione è stato preparato sul nuovo server un punto di installazione amministrativa condiviso in rete, e un errore di setup dovuto a dati residui della vecchia installazione è stato risolto rimuovendone le cartelle prima di rilanciare.

## Risultato

Il gestore delle licenze OCR gira su Windows Server 2022 sulla nuova infrastruttura, con la stessa versione dello strumento e la prima postazione reinstallata che legge correttamente la licenza dal nuovo server. Le licenze dello strumento CAT restano licenze di rete, servite da un server e distribuite su circa diciotto postazioni.
