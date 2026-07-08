# local-audio-transcriptor

_Nessuna descrizione su GitHub._

- **Repository**: [alesop95/local-audio-transcriptor](https://github.com/alesop95/local-audio-transcriptor)
- **Linguaggio principale**: Python
- **Ultimo aggiornamento**: 2026-07-06
- **Cartella locale**: `local-audio-transcriptor`

Uno strumento completamente offline e multipiattaforma, a riga di comando e basato su Gradio, che trasforma audio e video/playlist YouTube in testo ricercabile e interrogabile. La trascrizione gira su WhisperX (costruito su faster-whisper/CTranslate2) con rilevamento automatico GPU/CPU, diarizzazione opzionale degli speaker via pyannote, e VAD Silero per ridurre le allucinazioni di Whisper su audio rumoroso o silenzioso. Oltre alla trascrizione grezza, lo strumento costruisce un indice full-text locale SQLite FTS5 per la ricerca per parole chiave con timestamp, offre una modalità di question-answering retrieval-augmented che cita i passaggi sorgente, e può riassumere singoli file o produrre un unico digest consolidato su un'intera playlist, tutto tramite un LLM locale via Ollama o qualsiasi endpoint compatibile con OpenAI. Anche la traduzione è gestita offline, tramite argos-translate, preservando i timestamp dei sottotitoli nell'output SRT bilingue.

Il progetto è confezionato come una CLI installabile (`transcribe`) via `uv tool`, include un comando `doctor` per diagnosticare l'ambiente locale (ffmpeg, backend ASR, GPU, raggiungibilità dell'LLM), e ha una CI GitHub Actions che copre sia Linux sia Windows. Il README inquadra diversi progetti open source basati su Whisper studiati come riferimenti per lavori futuri, ed elenca il retrieval semantico (basato su embedding), l'export PDF/EPUB e una modalità server/API come voci di roadmap non ancora costruite, il che colloca questo strumento come uno strumento personale funzionante con un set di funzionalità dall'ambito chiaramente definito piuttosto che come un prodotto finito.
