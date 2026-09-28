# Automazioni per la produzione linguistica

**Settore**: azienda di servizi linguistici e traduzione professionale

**Periodo**: 10/2024 - in corso

**Ruolo**: IT Manager, sviluppatore di script

**Tecnologie**: PowerShell, AutoHotkey, Utilità di pianificazione di Windows, Python, spaCy, NLTK, openpyxl

## Contesto

Il lavoro dei project manager e dei traduttori passa per strumenti che non espongono sempre un'interfaccia programmabile, e per materiali da preparare prima della traduzione: siti scaricati, PDF, file XML, documenti Word ed Excel. Una parte di queste operazioni si ripeteva a mano per ogni progetto, e il backup delle memorie di traduzione dipendeva da un'esportazione manuale.

## Cosa è stato fatto

Due gruppi di strumenti. Il primo, del 2024 e 2025, è una raccolta di script Python per preparare il materiale da tradurre: estrazione del testo da HTML, PDF, XML, Word ed Excel, suddivisione di file Excel grandi, riduzione a campione di una memoria di traduzione, estrazione di n-grammi con spaCy e NLTK per individuare la terminologia ricorrente, controllo delle righe troppo lunghe, e flussi che estraggono il testo da uno scheletro HTML e lo reinseriscono dopo la traduzione. Il secondo, del novembre 2025, è il backup giornaliero delle memorie di traduzione dal server di condivisione dello strumento CAT: uno script PowerShell crea la cartella datata, prepara il file di configurazione del lavoro, pilota con AutoHotkey lo strumento di esportazione del fornitore, che non ha un'interfaccia programmabile, applica una politica di conservazione e gira come attività pianificata.

## Risultato

Le memorie di traduzione hanno un backup giornaliero automatico con conservazione controllata, in esercizio da novembre 2025. Gli script di preparazione del materiale sono stati usati nei progetti del 2024 e 2025 e oggi non sono più sviluppati.
