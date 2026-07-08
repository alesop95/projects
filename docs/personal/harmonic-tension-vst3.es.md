# harmonic-tension-vst3

_Sin descripción en GitHub._

- **Repositorio**: [alesop95/harmonic-tension-vst3](https://github.com/alesop95/harmonic-tension-vst3)
- **Lenguaje principal**: C++
- **Última actualización**: 2026-06-23
- **Carpeta local**: `harmonic-tension-vst3`

Este es un plugin de audio VST3, construido en C++ sobre el framework JUCE, que escucha el MIDI entrante en tiempo real y convierte el análisis armónico en una señal de control en vivo para la iluminación del escenario en lugar de para el sonido. Implementa el Spiral Array Model de Elaine Chew, una representación geométrica de la armonía tonal, calculando métricas como la tensión armónica, el diámetro de la nube (cloud diameter) y el tensile strain a partir de la secuencia de notas tocadas y su temporización, para luego estimar la tonalidad actual encontrando el punto más cercano en la espiral al centro de efecto de las notas. La idea se demostró en vivo, mapeando los valores de tensión obtenidos a cambios de brillo y patrones en las luces del escenario, en el evento de música electrónica Festivalle en el Valle de los Templos en agosto de 2019.

La propia clase del procesador todavía se llama `ProgettoProvaAudioProcessor` ("proyecto de prueba" en italiano) en el código fuente, un resto de nomenclatura del scaffolding de proyecto de JUCE que indica que esto siguió siendo un prototipo funcional en lugar de una versión pulida y renombrada. El PDF que acompaña al repositorio documenta el modelo geométrico subyacente y el caso de uso de iluminación inteligente con más profundidad de la que ofrecen los comentarios del código.
