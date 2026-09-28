# analog-to-digital-VHS-converter

A personal project to collect memories coming from tapes

- **Repositorio**: [alesop95/analog-to-digital-VHS-converter](https://github.com/alesop95/analog-to-digital-VHS-converter)
- **Tecnologías**: OBS Studio, StarTech SVID2USB232, Topaz Video AI (previsto)
- **Periodo**: 06/2026, en pausa

Documentación operativa de la cadena para digitalizar cintas VHS en un máster de conservación; el repositorio no contiene una aplicación. La cadena es una videograbadora Daewoo ST220 PAL, un adaptador de SCART a compuesto y una tarjeta de captura StarTech SVID2USB232 (chipset EM28xx), con captura en OBS Studio. El máster es AVI con vídeo MJPEG intra-frame a 720x576 y audio PCM 48 kHz sin comprimir, y conserva ambos campos entrelazados (50 por segundo) en lugar de desentrelazar durante la captura, porque los dongles de consumo tienden a descartar uno de forma irrecuperable. Se elige MJPEG porque tolera el ruido analógico mejor que los códecs inter-frame.

Estado: cadena de hardware, driver y configuración de OBS verificados con una captura de prueba. Faltan la primera captura máster con los ajustes definitivos, el paso de escalado con Topaz Video AI y el flujo de entrega (formatos, precios).
