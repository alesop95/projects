# gesture_glove_harmonizer

_Nessuna descrizione su GitHub._

- **Repository**: [alesop95/gesture_glove_harmonizer](https://github.com/alesop95/gesture_glove_harmonizer)
- **Linguaggi**: JavaScript, CSS, HTML, MATLAB
- **Data di inizio**: 2019-03
- **Ultimo aggiornamento**: 2026-06-23
- **Cartella locale**: `gesture_glove_harmonizer`

Questa web app basata su browser sovrappone armoniche generate automaticamente alle note suonate da una tastiera MIDI, scegliendo quali armoniche aggiungere in base al movimento della mano rilevato da un BBC micro:bit indossato come un guanto e collegato via Bluetooth Low Energy. Le rotazioni di roll e pitch della mano selezionano l'intervallo armonico e la sua ottava, un modello 3D della mano renderizzato con Three.js rispecchia il movimento in tempo reale, e l'audio stesso è sintetizzato interamente lato client anziché basarsi su campioni preregistrati, quindi l'app funziona anche senza il guanto collegato, pilotata dalla sola tastiera.

L'interfaccia è costruita con Vue.js per i controlli reattivi (slider dell'inviluppo ADSR disegnati come SVG, selezione del timbro, un display dello spettro del segnale generato), mentre il motore audio vero e proprio gestisce gli eventi MIDI note-on e note-off e pilota un oscillatore per ogni armonica attiva tramite la Web Audio API. Uno script MATLAB separato è stato usato offline per analizzare campioni reali di strumenti registrati e decidere, per ciascun timbro, quante armoniche possono essere riprodotte in modo convincente in un contesto web; i conteggi di armoniche risultanti sono cablati (hard-coded) nel synth JavaScript. Il README documenta questo come un progetto costruito per esplorare la sintesi sonora controllata da gesti nel browser, elencando onestamente anche sviluppi futuri, come lo pitch shifting in tempo reale, che non sono mai stati implementati.
