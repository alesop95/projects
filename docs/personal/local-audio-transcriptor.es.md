# local-audio-transcriptor

- **Repositorio**: [alesop95/local-audio-transcriptor](https://github.com/alesop95/local-audio-transcriptor)
- **Tecnologías**: Python, WhisperX (faster-whisper), yt-dlp, ffmpeg, pyannote, Ollama
- **Periodo**: 06/2026 - 07/2026, en pausa

Una herramienta sin conexión y multiplataforma, con línea de comandos e interfaz Gradio, que convierte audio, vídeo y listas de reproducción de YouTube en texto buscable y consultable. La transcripción usa WhisperX, basado en faster-whisper y CTranslate2, con detección automática de GPU o CPU, diarización opcional de hablantes con pyannote y VAD de Silero para reducir las alucinaciones de Whisper en audio ruidoso o silencioso. Sobre las transcripciones construye un índice de texto completo SQLite FTS5 con marcas de tiempo, un modo de preguntas y respuestas que cita los pasajes de origen y resúmenes por archivo o un resumen consolidado de toda una lista de reproducción, con un LLM local a través de Ollama o un endpoint compatible con OpenAI. La traducción se hace sin conexión con argos-translate y conserva las marcas de tiempo en los subtítulos SRT bilingües.

Se distribuye como CLI instalable (`transcribe`) mediante `uv tool`, con un comando `doctor` que diagnostica ffmpeg, el backend de ASR, la GPU y la accesibilidad del LLM, un comando `folder` para transcribir en bloque una carpeta y CI de GitHub Actions en Linux y Windows. El resumen consolidado reutiliza los resúmenes ya producidos y el tamaño de contexto del modelo de Ollama es configurable. Quedan por construir la recuperación semántica con embeddings, la exportación a PDF/EPUB y un modo servidor.
