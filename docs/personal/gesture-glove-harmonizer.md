# gesture_glove_harmonizer

- **Repository**: [alesop95/gesture_glove_harmonizer](https://github.com/alesop95/gesture_glove_harmonizer)
- **Tecnologie**: JavaScript, Web Audio API, Web Bluetooth, Vue.js, Three.js, MATLAB
- **Periodo**: 2019, concluso

Web app che aggiunge armoniche alle note suonate da una tastiera MIDI, scegliendole in base al movimento della mano rilevato da un BBC micro:bit indossato come guanto e collegato in Bluetooth Low Energy. Roll e pitch della mano selezionano l'intervallo e l'ottava dell'armonica, un modello 3D in Three.js segue il movimento in tempo reale, e il suono è sintetizzato nel browser con un oscillatore per armonica, senza campioni: l'app funziona anche senza guanto, dalla sola tastiera.

L'interfaccia è in Vue.js, con inviluppo ADSR, scelta del timbro e spettro del segnale. Uno script MATLAB ha analizzato campioni di strumenti reali per decidere quante armoniche riprodurre per ciascun timbro, e i valori sono scritti nel sintetizzatore.
