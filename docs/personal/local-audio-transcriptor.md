# local-audio-transcriptor

- **Repository**: [alesop95/local-audio-transcriptor](https://github.com/alesop95/local-audio-transcriptor)
- **Tecnologie**: Python, WhisperX (faster-whisper), yt-dlp, ffmpeg, pyannote, Ollama
- **Periodo**: 06/2026 - 07/2026, fermo

Uno strumento offline e multipiattaforma, con riga di comando e interfaccia Gradio, che trasforma audio, video e playlist YouTube in testo ricercabile e interrogabile. La trascrizione usa WhisperX, basato su faster-whisper e CTranslate2, con rilevamento automatico di GPU o CPU, diarizzazione opzionale degli speaker con pyannote e VAD Silero per ridurre le allucinazioni di Whisper su audio rumoroso o silenzioso. Sulle trascrizioni costruisce un indice full-text SQLite FTS5 con timestamp, una modalità di domanda e risposta che cita i passaggi sorgente e sintesi per singolo file o un digest consolidato di un'intera playlist, con un LLM locale via Ollama o un endpoint compatibile con OpenAI. La traduzione avviene offline con argos-translate e conserva i timestamp nei sottotitoli SRT bilingui.

È confezionato come CLI installabile (`transcribe`) via `uv tool`, con un comando `doctor` che diagnostica ffmpeg, backend ASR, GPU e raggiungibilità dell'LLM, un comando `folder` per trascrivere in blocco una cartella e una CI GitHub Actions su Linux e Windows. Il digest riusa le sintesi già prodotte e la dimensione del contesto del modello Ollama è configurabile. Restano da costruire il retrieval semantico con embedding, l'export PDF/EPUB e una modalità server.
