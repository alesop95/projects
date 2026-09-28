# local-audio-transcriptor

- **Repository**: [alesop95/local-audio-transcriptor](https://github.com/alesop95/local-audio-transcriptor)
- **Technologies**: Python, WhisperX (faster-whisper), yt-dlp, ffmpeg, pyannote, Ollama
- **Period**: 06/2026 - 07/2026, paused

An offline, cross-platform tool, with a command line and a Gradio interface, that turns audio, video and YouTube playlists into searchable, queryable text. Transcription uses WhisperX, built on faster-whisper and CTranslate2, with automatic GPU or CPU detection, optional speaker diarization with pyannote and Silero VAD to reduce Whisper's hallucinations on noisy or silent audio. On top of the transcripts it builds a SQLite FTS5 full-text index with timestamps, a question-answering mode that cites the source passages, and summaries per file or a consolidated digest of a whole playlist, through a local LLM via Ollama or an OpenAI-compatible endpoint. Translation runs offline with argos-translate and keeps the timestamps in bilingual SRT subtitles.

It is packaged as an installable CLI (`transcribe`) via `uv tool`, with a `doctor` command that diagnoses ffmpeg, the ASR backend, the GPU and LLM reachability, a `folder` command to transcribe a whole folder in batch, and GitHub Actions CI on Linux and Windows. The digest reuses summaries already produced and the context size of the Ollama model is configurable. Semantic retrieval with embeddings, PDF/EPUB export and a server mode are still to be built.
