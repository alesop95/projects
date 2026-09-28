# gps-time-synchronization-arduino-stm32

Bachelor degree project

- **Repositorio**: [alesop95/gps-time-synchronization-arduino-stm32](https://github.com/alesop95/gps-time-synchronization-arduino-stm32)
- **Tecnologías**: Arduino (C++), STM32 HAL, Contiki OS, Python 2.7 (pySerial)
- **Periodo**: 2017, finalizado

Trabajo experimental de la tesis de grado en Ingeniería Electrónica: mide la deriva del reloj de dos plataformas embebidas usando el tiempo GPS como referencia. Un Arduino Uno, que cuenta el tiempo con el contador por software millis(), y un STM32 Nucleo de la familia L1, que usa su propio RTC por hardware con un cristal externo de 32,768 kHz, reciben las tramas NMEA del mismo módulo GPS y registran el desfase durante varias horas.

En Arduino un sketch lee la hora de la trama $GPGGA y la envía junto con millis() a un logger en Python que escribe CSV. El firmware del STM32, sobre Contiki OS y HAL, configura los prescalers del RTC para un tick de 1 Hz desde el oscilador LSE y lo compara periódicamente con el GPS. En unas cuatro horas el Arduino deriva unos 5 segundos y el STM32 unos 1,6: el RTC de cristal es unas tres veces más estable.
