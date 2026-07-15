# gps-time-synchronization-arduino-stm32

Bachelor degree project

- **Repository**: [alesop95/gps-time-synchronization-arduino-stm32](https://github.com/alesop95/gps-time-synchronization-arduino-stm32)
- **Linguaggi**: C, C++, Python
- **Data di inizio**: 2026-01
- **Ultimo aggiornamento**: 2026-07-14
- **Cartella locale**: `gps-time-synchronization-arduino-stm32`

Questo repository contiene il lavoro sperimentale per una tesi di laurea triennale in Ingegneria Elettronica/Informatica che misura e confronta la deriva dell'orologio (clock drift) su due piattaforme embedded rispetto al tempo GPS come riferimento assoluto. Un Arduino Uno, basato sul contatore software millis(), e uno STM32 Nucleo (famiglia STM32L1), che pilota il proprio RTC hardware con un cristallo esterno da 32.768 kHz, ricevono entrambi frasi NMEA dallo stesso modulo GPS e registrano lo scarto tra il proprio orologio e il tempo GPS durante acquisizioni di più ore.

Sul lato Arduino, uno sketch basato su SoftwareSerial esegue il parsing del campo orario nella frase $GPGGA e trasmette il tempo GPS abbinato a millis() via USB a un logger Python (2.7, pySerial) che scrive file CSV per l'analisi offline. Il firmware STM32, costruito su Contiki OS e STM32 HAL, configura i prescaler async/sync dell'RTC per un tick a 1 Hz derivato dall'oscillatore LSE e confronta periodicamente il tempo dell'RTC con un fix GPS aggiornato. Su un'esecuzione di circa quattro ore, i risultati mostrano l'orologio software dell'Arduino derivare di circa 5 secondi contro circa 1,6 secondi per l'RTC hardware dello STM32, una dimostrazione concreta e misurata del perché un RTC pilotato da cristallo sia superiore a un contatore software in millisecondi per la cronometria su lunga durata.
