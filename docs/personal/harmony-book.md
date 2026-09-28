# harmony-book

The technical under the hood of my book writing

- **Repository**: [alesop95/harmony-book](https://github.com/alesop95/harmony-book)
- **Tecnologie**: LuaLaTeX (memoir), LilyPond, biblatex e biber, TinyTeX, Python
- **Periodo**: 06/2026 - in corso

Toolchain di pubblicazione di un libro di armonia: il repository versiona il metodo tipografico e la build, mentre il testo del libro resta fuori da git. La composizione usa LuaLaTeX con la classe memoir, LilyPond incorporato con lilypond-book per gli esempi musicali, biblatex e biber per la bibliografia, imakeidx e glossaries per indice e glossario. L'ambiente TeX è un'installazione TinyTeX locale descritta da un manifesto di pacchetti, riproducibile su Windows e Linux.

Il manoscritto (capitoli, esempi, bibliografia) sta in una cartella esclusa da git perché destinato alla vendita; un documento di esempio dimostra che la catena funziona. Il repository contiene anche strumenti Python per la teoria musicale usata nel libro, come il calcolo del contenuto di tritoni delle scale e la derivazione delle dominanti secondarie, e una base di conoscenza sulle fonti consultate.
