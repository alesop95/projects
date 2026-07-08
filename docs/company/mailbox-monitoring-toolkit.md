# Toolkit di monitoraggio caselle di posta aziendali

**Settore**: azienda di servizi linguistici e traduzione professionale

**Periodo**: 06/2026 - in corso

**Ruolo**: IT Manager, sistemista

**Tecnologie**: Python, PowerShell, Microsoft 365 / Exchange Online, scheduled task di Windows,
report in Excel

## Contesto

Il monitoraggio dello stato delle caselle di posta aziendali (spazio occupato, soglie critiche,
andamento nel tempo) veniva fatto a mano, senza un punto di raccolta storico su cui basare
decisioni di capacity planning o allarmi tempestivi prima che una casella diventasse piena.

## Cosa è stato fatto

Toolkit di monitoraggio e reportistica eseguito periodicamente via scheduled task di Windows: uno
script Python interroga lo stato delle caselle Exchange Online e genera alert quando una casella
supera una soglia critica, un secondo script produce report e trend storici in Excel. Il layer di
lancio ed esecuzione pianificata è in PowerShell. Credenziali e dati reali delle caselle restano
esclusivamente locali, mai versionati.

## Risultato

Alert automatico sulle caselle a rischio saturazione prima che diventino un problema operativo, e
uno storico dei trend che prima non esisteva, utile per pianificare interventi di pulizia o
ridimensionamento con anticipo invece che in emergenza.
