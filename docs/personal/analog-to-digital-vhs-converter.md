# analog-to-digital-VHS-converter

A personal project to collect memories coming from tapes

- **Repository**: [alesop95/analog-to-digital-VHS-converter](https://github.com/alesop95/analog-to-digital-VHS-converter)
- **Linguaggi**: PowerShell, Shell, Python, JavaScript
- **Data di inizio**: 2026-06
- **Ultimo aggiornamento**: 2026-07-06
- **Cartella locale**: `analog-to-digital-VHS-converter`

Questo repository è un progetto di documentazione, non un'applicazione: descrive il workflow hardware e software per digitalizzare videocassette VHS in un master digitale di qualità da conservazione. Documenta una catena di segnale specifica (un videoregistratore Daewoo ST220 PAL, attraverso un adattatore da SCART a composito, fino a una scheda di acquisizione StarTech SVID2USB232 con chipset EM28xx), le impostazioni di cattura di OBS Studio e le motivazioni che le giustificano, in particolare la scelta di preservare entrambi i campi interlacciati (50 al secondo) invece di deinterlacciare già in fase di cattura, poiché i dongle di acquisizione consumer scartano spesso un campo, perdendolo in modo irrecuperabile. Il formato master definito è AVI con audio non compresso e video MJPEG intra-frame a 720x576, scelto perché MJPEG tollera meglio il rumore analogico imprevedibile rispetto ai codec inter-frame, e AVI accetta flussi PCM interlacciati senza imporre un contenitore da streaming.

Secondo la propria checklist di stato, il progetto ha validato la catena hardware e la configurazione di OBS, ma non ha ancora prodotto una prima cattura completa del master, e restano ancora aperti sia il passaggio di upscaling con l'IA (tramite Topaz Video AI) sia il workflow di consegna al cliente. Si presenta come un runbook tecnico per un servizio personale di conversione da VHS a digitale ancora in fase di allestimento, non come una pipeline conclusa.
