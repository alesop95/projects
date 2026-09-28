# harmonic-tension-vst3

- **Repository**: [alesop95/harmonic-tension-vst3](https://github.com/alesop95/harmonic-tension-vst3)
- **Tecnologie**: C++, JUCE, VST3
- **Periodo**: 03/2019 - 08/2019, concluso

Plugin VST3 in C++ su JUCE che analizza in tempo reale il MIDI in ingresso e trasforma l'armonia in un segnale di controllo per le luci di scena invece che per il suono. Implementa lo Spiral Array Model di Elaine Chew, una rappresentazione geometrica dell'armonia tonale: dalle note suonate e dalla loro durata calcola tensione armonica, diametro della nuvola e tensile strain, e stima la tonalità corrente come il punto della spirale più vicino al centro di effetto delle note.

Il sistema è stato provato dal vivo al festival di musica elettronica Festivalle, nella Valle dei Templi, ad agosto 2019, con la tensione mappata su luminosità e pattern delle luci ([video della demo](https://www.youtube.com/watch?v=wB-U9s4ASQo)). Il [documento sul modello](https://drive.proton.me/urls/KHMJ76J6RR#cSM_oJpX6Ky4) descrive la geometria e il caso d'uso più in dettaglio.
