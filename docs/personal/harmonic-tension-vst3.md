# harmonic-tension-vst3

_Nessuna descrizione su GitHub._

- **Repository**: [alesop95/harmonic-tension-vst3](https://github.com/alesop95/harmonic-tension-vst3)
- **Linguaggio principale**: C++
- **Ultimo aggiornamento**: 2026-06-23
- **Cartella locale**: `harmonic-tension-vst3`

Questo è un plugin audio VST3, costruito in C++ sul framework JUCE, che ascolta il MIDI in ingresso in tempo reale e trasforma l'analisi armonica in un segnale di controllo live per l'illuminazione del palco anziché per il suono. Implementa lo Spiral Array Model di Elaine Chew, una rappresentazione geometrica dell'armonia tonale, calcolando metriche come tensione armonica, diametro della nuvola (cloud diameter) e tensile strain a partire dalla sequenza di note suonate e dalla loro tempistica, per poi stimare la tonalità corrente trovando il punto più vicino sulla spirale al centro di effetto delle note. L'idea è stata dimostrata dal vivo, mappando i valori di tensione derivati su variazioni di luminosità e pattern delle luci di scena, all'evento di musica elettronica Festivalle nella Valle dei Templi nell'agosto 2019.

La classe processore stessa si chiama ancora `ProgettoProvaAudioProcessor` ("test project" in italiano) nel codice sorgente, un residuo di denominazione dello scaffolding di progetto di JUCE che segnala come questo sia rimasto un prototipo funzionante piuttosto che una release rifinita e rinominata. Il PDF allegato nel repository documenta il modello geometrico sottostante e il caso d'uso dell'illuminazione intelligente più in profondità di quanto facciano i commenti nel codice.
