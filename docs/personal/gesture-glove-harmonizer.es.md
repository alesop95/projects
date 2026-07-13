# gesture_glove_harmonizer

_Sin descripción en GitHub._

- **Repositorio**: [alesop95/gesture_glove_harmonizer](https://github.com/alesop95/gesture_glove_harmonizer)
- **Lenguajes**: JavaScript, CSS, HTML, MATLAB
- **Fecha de inicio**: 2019-03
- **Última actualización**: 2026-06-23
- **Carpeta local**: `gesture_glove_harmonizer`

Esta aplicación web basada en navegador superpone armónicos generados automáticamente a las notas tocadas desde un teclado MIDI, eligiendo qué armónicos añadir según el movimiento de la mano captado por un BBC micro:bit llevado como un guante y conectado por Bluetooth Low Energy. Las rotaciones de roll y pitch de la mano seleccionan el intervalo armónico y su octava, un modelo 3D de la mano renderizado con Three.js refleja el movimiento en vivo, y el propio audio se sintetiza enteramente en el lado del cliente en lugar de depender de muestras pregrabadas, de modo que la aplicación también funciona sin el guante conectado, controlada solo desde el teclado.

La interfaz está construida con Vue.js para los controles reactivos (deslizadores de envolvente ADSR dibujados como SVG, selección de timbre, una visualización del espectro de la señal generada), mientras que el motor de sonido propiamente dicho gestiona los eventos MIDI note-on y note-off e impulsa un oscilador por cada armónico activo a través de la Web Audio API. Un script de MATLAB independiente se usó offline para analizar muestras reales de instrumentos grabados y decidir, por cada timbre, cuántos armónicos se pueden reproducir de forma convincente en un contexto web; los conteos de armónicos resultantes están codificados de forma fija (hard-coded) en el sintetizador JavaScript. El README documenta esto como un proyecto construido para explorar la síntesis de sonido controlada por gestos en el navegador, incluyendo de forma honesta trabajo futuro pendiente, como el pitch shifting en vivo, que nunca llegó a implementarse.
