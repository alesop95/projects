# gesture_glove_harmonizer

- **Repositorio**: [alesop95/gesture_glove_harmonizer](https://github.com/alesop95/gesture_glove_harmonizer)
- **Tecnologías**: JavaScript, Web Audio API, Web Bluetooth, Vue.js, Three.js, MATLAB
- **Periodo**: 2019, finalizado

Aplicación web que añade armónicos a las notas tocadas en un teclado MIDI, eligiéndolos según el movimiento de la mano detectado por un BBC micro:bit llevado como guante y conectado por Bluetooth Low Energy. El roll y el pitch de la mano seleccionan el intervalo y la octava del armónico, un modelo 3D en Three.js sigue el movimiento en tiempo real, y el sonido se sintetiza en el navegador con un oscilador por armónico, sin muestras: la aplicación funciona también sin guante, solo con el teclado.

La interfaz está en Vue.js, con envolvente ADSR, selección del timbre y espectro de la señal. Un script de MATLAB analizó muestras de instrumentos reales para decidir cuántos armónicos reproducir para cada timbre, y los valores están escritos en el sintetizador.
