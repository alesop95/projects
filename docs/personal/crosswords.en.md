# crosswords

A personal repo to develop new crossword games (italian language)

- **Repository**: [alesop95/crosswords](https://github.com/alesop95/crosswords)
- **Technologies**: TypeScript, Vite, Web Worker
- **Period**: 07/2026, completed

Italian-style crossword builder that runs in the browser with no server: all the work stays on the user's machine. You draw the grid (free black squares, optional symmetry, from 5x5 to 25x25), fill it automatically or word by word, write the clues, save in ipuz format and print grid and solution on A4. The app is online at [alesop95.github.io/crosswords](https://alesop95.github.io/crosswords/) and is republished by GitHub Actions on every push.

Autofill is a constraint solver (backtracking with the MRV heuristic, forward checking and arc consistency) running in a Web Worker, so the interface stays responsive and the fill can be interrupted. The dictionary, about 350,000 entries, is generated from Morph-it! and weighted with itWaC frequencies, so the solver prefers common words. The repository also documents the Italian legal and tax framework for selling crosswords to magazines. Version 1 is closed.
