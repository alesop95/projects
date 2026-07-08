# Toolkit di esportazione e archiviazione caselle di posta

**Settore**: azienda di servizi linguistici e traduzione professionale

**Periodo**: 06/2026 - in corso

**Ruolo**: IT Manager, sistemista

**Tecnologie**: PowerShell, Microsoft 365 / Exchange Online, Microsoft Purview eDiscovery,
Outlook, checksum per la verifica di integrità

## Contesto

Due caselle di posta condivise avevano raggiunto la saturazione completa, sia sulla casella
primaria sia sull'archivio online collegato. Prima di liberare spazio serviva un'esportazione
statica e verificabile del contenuto verso una risorsa di rete, con la garanzia che nessun
messaggio andasse perso o corrotto nel passaggio.

## Cosa è stato fatto

Toolkit operativo riusabile per l'esportazione statica delle caselle verso una risorsa di rete
di archiviazione. Il metodo di riferimento individuato è l'export PST lato server tramite
Microsoft Purview eDiscovery; in assenza della licenza necessaria sull'operatore, il processo è
stato adattato a un export equivalente lato client da Outlook classico. Il toolkit include script
PowerShell di verifica preliminare in sola lettura e uno step di archiviazione con calcolo di
checksum per garantire l'integrità dei file esportati. Gli script operano volutamente in sola
lettura ed esportazione: nessuna cancellazione delle caselle è automatizzata, quella fase resta
un'azione separata e autorizzata esplicitamente solo a export verificato.

## Risultato

Percorso di archiviazione ripetibile e verificabile per liberare caselle sature senza rischio di
perdita dati, documentato abbastanza da poter essere riapplicato ad altre caselle in futuro senza
dover reinventare il processo.
