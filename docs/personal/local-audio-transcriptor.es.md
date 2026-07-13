# local-audio-transcriptor

_Sin descripción en GitHub._

- **Repositorio**: [alesop95/local-audio-transcriptor](https://github.com/alesop95/local-audio-transcriptor)
- **Lenguajes**: Python, PowerShell, Shell, JavaScript
- **Fecha de inicio**: 2026-06
- **Última actualización**: 2026-07-06
- **Carpeta local**: `local-audio-transcriptor`

Una herramienta completamente sin conexión y multiplataforma, de línea de comandos y basada en Gradio, que convierte audio y vídeos/listas de reproducción de YouTube en texto buscable y consultable. La transcripción se ejecuta sobre WhisperX (construido sobre faster-whisper/CTranslate2) con detección automática de GPU/CPU, diarización opcional de hablantes mediante pyannote, y VAD de Silero para reducir las alucinaciones de Whisper en audio ruidoso o silencioso. Más allá de la transcripción en bruto, la herramienta construye un índice local de texto completo SQLite FTS5 para búsqueda por palabras clave con marcas de tiempo, ofrece un modo de preguntas y respuestas con recuperación aumentada que cita los pasajes de origen, y puede resumir archivos individuales o producir un único resumen consolidado de toda una lista de reproducción, todo ello mediante un LLM local a través de Ollama o cualquier endpoint compatible con OpenAI. La traducción también se gestiona sin conexión, mediante argos-translate, conservando las marcas de tiempo de los subtítulos en la salida SRT bilingüe.

El proyecto se empaqueta como una CLI instalable (`transcribe`) mediante `uv tool`, incluye un comando `doctor` para diagnosticar el entorno local (ffmpeg, backend de ASR, GPU, accesibilidad del LLM), y cuenta con CI de GitHub Actions que cubre tanto Linux como Windows. El README presenta varios proyectos de código abierto basados en Whisper que estudió como referencias para trabajo futuro, y enumera la recuperación semántica (basada en embeddings), la exportación a PDF/EPUB y un modo servidor/API como elementos de la hoja de ruta todavía no construidos, lo que sitúa esto como una herramienta personal funcional con un conjunto de funcionalidades de alcance claramente delimitado, más que como un producto terminado.
