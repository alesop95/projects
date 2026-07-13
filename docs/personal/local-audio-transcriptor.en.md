# local-audio-transcriptor

_No description on GitHub._

- **Repository**: [alesop95/local-audio-transcriptor](https://github.com/alesop95/local-audio-transcriptor)
- **Languages**: Python, PowerShell, Shell, JavaScript
- **Start date**: 2026-06
- **Last updated**: 2026-07-06
- **Local folder**: `local-audio-transcriptor`

A fully offline, cross-platform command-line and Gradio-based tool that turns audio and YouTube video/playlists into searchable, queryable text. Transcription runs on WhisperX (built on faster-whisper/CTranslate2) with automatic GPU/CPU detection, optional speaker diarization via pyannote, and Silero VAD to cut down on Whisper's hallucinations on noisy or silent audio. Beyond raw transcription, the tool builds a local SQLite FTS5 full-text index for keyword search with timestamps, offers a retrieval-augmented question-answering mode that cites source passages, and can summarize individual files or produce a single consolidated digest across an entire playlist, all through a local LLM via Ollama or any OpenAI-compatible endpoint. Translation is handled offline too, through argos-translate, preserving subtitle timestamps in bilingual SRT output.

The project is packaged as an installable CLI (`transcribe`) via `uv tool`, ships a `doctor` command to diagnose the local environment (ffmpeg, ASR backend, GPU, LLM reachability), and has GitHub Actions CI covering both Linux and Windows. The README frames several open-source Whisper-based projects it studied as references for future work, and lists semantic (embedding-based) retrieval, PDF/EPUB export and a server/API mode as roadmap items not yet built, which places this as a working personal tool with a clearly scoped feature set rather than a finished product.
