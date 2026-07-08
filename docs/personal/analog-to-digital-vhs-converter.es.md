# analog-to-digital-VHS-converter

A personal project to collect memories coming from tapes

- **Repositorio**: [alesop95/analog-to-digital-VHS-converter](https://github.com/alesop95/analog-to-digital-VHS-converter)
- **Lenguaje principal**: PowerShell
- **Última actualización**: 2026-07-06
- **Carpeta local**: `analog-to-digital-VHS-converter`

Este repositorio es un proyecto de documentación, no una aplicación: describe el flujo de trabajo de hardware y software para digitalizar cintas VHS en un máster digital de calidad de conservación. Documenta una cadena de señal específica (una videograbadora Daewoo ST220 PAL, a través de un adaptador de SCART a compuesto, hasta una tarjeta de captura StarTech SVID2USB232 con chipset EM28xx), la configuración de captura de OBS Studio y el razonamiento detrás de ella, en particular la decisión de preservar ambos campos entrelazados (50 por segundo) en lugar de desentrelazar ya durante la captura, ya que los dongles de captura de consumo suelen descartar un campo y perderlo de forma irrecuperable. El formato máster definido es AVI con audio sin comprimir y vídeo MJPEG intra-frame a 720x576, elegido porque MJPEG tolera mejor el ruido analógico impredecible que los códecs inter-frame, y AVI acepta flujos PCM entrelazados sin imponer un contenedor de streaming.

Según su propia checklist de estado, el proyecto ha validado la cadena de hardware y la configuración de OBS, pero todavía no ha producido una primera captura completa del máster, y siguen pendientes tanto el paso de escalado con IA (mediante Topaz Video AI) como el flujo de entrega al cliente. Se presenta como un runbook técnico para un servicio personal de conversión de VHS a digital todavía en fase de puesta a punto, no como un pipeline terminado.
