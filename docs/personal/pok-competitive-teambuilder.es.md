# pok--competitive-teambuilder

A customizable tool for building competitive teams for pokèmon champions

- **Repositorio**: [alesop95/pok--competitive-teambuilder](https://github.com/alesop95/pok--competitive-teambuilder)
- **Lenguaje principal**: TypeScript
- **Última actualización**: 2026-07-06
- **Carpeta local**: `pokè-competitive-teambuilder`

Una herramienta local en Node.js y TypeScript que genera propuestas de equipos Pokémon competitivos para el formato Pokémon Champions, a partir del roster disponible en una temporada. Razona sobre la composición del equipo mediante etiquetado y puntuación deterministas, no mediante simulación de combate: los roles se infieren a partir de estadísticas, habilidades y movepools, los Pokémon candidatos se puntúan por sinergia y cobertura de tipos frente a los metadatos actuales, y la salida incluye una justificación, las debilidades esperadas y los counters probables para cada equipo propuesto. Los datos del juego, la tabla de tipos y los cálculos de daño provienen del ecosistema de código abierto Pokémon Showdown (`@pkmn/dex`, `@smogon/calc`), y las reglas específicas del formato se derivan del mod Champions mantenido por la comunidad de Showdown.

El diseño mantiene separados la lógica del juego y los datos de temporada, de modo que una nueva temporada puede admitirse actualizando archivos de datos JSON/YAML sin tocar el código del motor. Un backend Fastify sirve tanto un modo CLI de generación de informes como una pequeña interfaz web; un segundo nivel opcional puede mejorar el texto de la justificación mediante la API de Claude cuando hay una clave configurada, recurriendo en caso contrario al texto determinista sin conexión. Según su propia hoja de ruta, el proyecto todavía está en una fase temprana: el scaffold, las herramientas de roster y el motor principal ya están listos, mientras que la interfaz web y una puntuación refinada del cálculo de daño están marcadas explícitamente como inacabadas.
