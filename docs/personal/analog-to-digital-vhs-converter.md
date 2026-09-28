# analog-to-digital-VHS-converter

A personal project to collect memories coming from tapes

- **Repository**: [alesop95/analog-to-digital-VHS-converter](https://github.com/alesop95/analog-to-digital-VHS-converter)
- **Tecnologie**: OBS Studio, StarTech SVID2USB232, Topaz Video AI (previsto)
- **Periodo**: 06/2026, fermo

Documentazione operativa della catena per digitalizzare videocassette VHS in un master da conservazione; il repository non contiene un'applicazione. La catena è un videoregistratore Daewoo ST220 PAL, un adattatore da SCART a composito e una scheda di acquisizione StarTech SVID2USB232 (chipset EM28xx), con cattura in OBS Studio. Il master è AVI con video MJPEG intra-frame a 720x576 e audio PCM 48 kHz non compresso, e conserva entrambi i campi interlacciati (50 al secondo) invece di deinterlacciare in cattura, perché i dongle consumer tendono a scartarne uno in modo irrecuperabile. MJPEG è scelto perché tollera il rumore analogico meglio dei codec inter-frame.

Stato: catena hardware, driver e configurazione di OBS verificati con una cattura di prova. Mancano la prima cattura master con le impostazioni definitive, il passaggio di upscaling con Topaz Video AI e il workflow di consegna (formati, prezzi).
