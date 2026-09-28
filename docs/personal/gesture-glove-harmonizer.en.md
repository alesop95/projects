# gesture_glove_harmonizer

- **Repository**: [alesop95/gesture_glove_harmonizer](https://github.com/alesop95/gesture_glove_harmonizer)
- **Technologies**: JavaScript, Web Audio API, Web Bluetooth, Vue.js, Three.js, MATLAB
- **Period**: 2019, completed

Web app that adds harmonics to the notes played on a MIDI keyboard, choosing them from the hand movement detected by a BBC micro:bit worn as a glove and connected over Bluetooth Low Energy. Roll and pitch of the hand select the interval and octave of the harmonic, a 3D model in Three.js follows the movement in real time, and the sound is synthesized in the browser with one oscillator per harmonic, without samples: the app also works without the glove, from the keyboard alone.

The interface is in Vue.js, with an ADSR envelope, timbre selection and a spectrum of the signal. A MATLAB script analyzed samples of real instruments to decide how many harmonics to reproduce for each timbre, and the values are written into the synthesizer.
