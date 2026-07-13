# pok--competitive-teambuilder

A customizable tool for building competitive teams for pokèmon champions

- **Repository**: [alesop95/pok--competitive-teambuilder](https://github.com/alesop95/pok--competitive-teambuilder)
- **Languages**: TypeScript, PowerShell, Shell, Python
- **Start date**: 2026-06
- **Last updated**: 2026-07-06
- **Local folder**: `pokè-competitive-teambuilder`

A local Node.js and TypeScript tool that generates competitive Pokémon team proposals for the Pokémon Champions format, given a season's available roster. It reasons about team composition through deterministic tagging and scoring rather than battle simulation: roles are inferred from stats, abilities and movepools, candidate Pokémon are scored for synergy and type coverage against the current metadata, and the output includes a rationale, expected weaknesses and likely counters for each proposed team. Game data, the type chart and damage calculations come from the open-source Pokémon Showdown ecosystem (`@pkmn/dex`, `@smogon/calc`), and format-specific rules are derived from Showdown's community-maintained Champions mod.

The design keeps game logic and season data separate, so a new season can be supported by updating JSON/YAML data files without touching the engine code. A Fastify backend serves both a CLI report-generation mode and a small web UI; an optional second tier can enhance the rationale text via the Claude API when a key is configured, falling back to the deterministic offline text otherwise. Per its own roadmap the project is still early: the scaffold, roster tooling and core engine are in place, while the web UI and refined damage-calc scoring are explicitly marked as unfinished.
