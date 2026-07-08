# gps-time-synchronization-arduino-stm32

Bachelor degree project

- **Repositorio**: [alesop95/gps-time-synchronization-arduino-stm32](https://github.com/alesop95/gps-time-synchronization-arduino-stm32)
- **Lenguaje principal**: C
- **Última actualización**: 2026-06-23
- **Carpeta local**: `gps-time-synchronization-arduino-stm32`

Este repositorio contiene el trabajo experimental de una tesis de grado en Ingeniería Electrónica/Informática que mide y compara la deriva del reloj (clock drift) en dos plataformas embebidas frente al tiempo GPS como referencia absoluta. Un Arduino Uno, que se apoya en su contador por software millis(), y un STM32 Nucleo (familia STM32L1), que controla su RTC por hardware con un cristal externo de 32.768 kHz, reciben ambos tramas NMEA del mismo módulo GPS y registran el desfase entre su propio reloj y el tiempo GPS a lo largo de adquisiciones de varias horas.

En el lado de Arduino, un sketch basado en SoftwareSerial analiza el campo de hora de la trama $GPGGA y transmite el tiempo GPS junto con millis() por USB a un logger en Python (2.7, pySerial) que escribe archivos CSV para su análisis offline. El firmware de STM32, construido sobre Contiki OS y STM32 HAL, configura los prescalers async/sync del RTC para un tick de 1 Hz derivado del oscilador LSE y compara periódicamente el tiempo del RTC con una nueva fijación GPS. En una ejecución de unas cuatro horas, los resultados muestran que el reloj por software del Arduino deriva unos 5 segundos frente a aproximadamente 1,6 segundos del RTC por hardware del STM32, una demostración concreta y medida de por qué un RTC controlado por cristal supera a un contador de milisegundos por software para la medición del tiempo de larga duración.
