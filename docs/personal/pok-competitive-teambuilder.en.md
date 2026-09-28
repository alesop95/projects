# pok--competitive-teambuilder

A customizable tool for building competitive teams for pokèmon champions

- **Repository**: [alesop95/pok--competitive-teambuilder](https://github.com/alesop95/pok--competitive-teambuilder)
- **Technologies**: Node.js 20, TypeScript, Fastify, Vite
- **Period**: 06/2026, paused

A Node.js and TypeScript tool that generates competitive Pokémon team proposals for the Pokémon Champions format, starting from the roster available in a season. It reasons about team composition with deterministic tagging and scoring, without simulating battles: roles are inferred from stats, abilities and movepools, candidates are scored for synergy and type coverage against the current metadata, and the output gives each team a rationale, expected weaknesses and likely counters. Game data, the type chart and damage calculation come from the open-source Pokémon Showdown ecosystem (`@pkmn/dex`, `@smogon/calc`), and format rules from the Champions mod maintained by the Showdown community.

Game logic is kept separate from season data, so a new season is supported by updating JSON and YAML files without touching the engine. The tagging and generation engine runs from the CLI and, for local use, behind a Fastify server; an optional second tier enriches the rationale through the Claude API when a key is configured, and otherwise the deterministic text is kept. A static web version built with Vite runs the engine entirely in the browser, stores team history in IndexedDB and is set up for hosting on GitHub Pages. Refined damage-calc scoring is still to be completed, and a manual team-building mode, with engine suggestions for the empty slots, is designed but not built.
