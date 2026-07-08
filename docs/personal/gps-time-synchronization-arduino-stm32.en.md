# gps-time-synchronization-arduino-stm32

Bachelor degree project

- **Repository**: [alesop95/gps-time-synchronization-arduino-stm32](https://github.com/alesop95/gps-time-synchronization-arduino-stm32)
- **Main language**: C
- **Last updated**: 2026-06-23
- **Local folder**: `gps-time-synchronization-arduino-stm32`

This repository contains the experimental work for a Bachelor's thesis in Electronic/Computer Engineering that measures and compares clock drift on two embedded platforms against GPS time as an absolute reference. An Arduino Uno, relying on its software-based millis() counter, and an STM32 Nucleo (STM32L1 family), driving its hardware RTC from an external 32.768 kHz crystal, both receive NMEA sentences from the same GPS module and log the offset between their own clock and GPS time over multi-hour acquisitions.

On the Arduino side, a SoftwareSerial-based sketch parses the $GPGGA sentence for the time field and streams GPS time paired with millis() over USB to a Python (2.7, pySerial) logger that writes CSV files for offline analysis. The STM32 firmware, built on Contiki OS and the STM32 HAL, configures the RTC's async/sync prescalers for a 1 Hz tick from the LSE oscillator and periodically compares RTC time against a fresh GPS fix. Over a roughly four-hour run the results show the Arduino's software clock drifting about 5 seconds versus about 1.6 seconds for the STM32 hardware RTC, a concrete, measured demonstration of why a crystal-driven RTC beats a software millisecond counter for long-duration timekeeping.
