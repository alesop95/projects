# harmony-book

The technical under the hood of my book writing

- **Repository**: [alesop95/harmony-book](https://github.com/alesop95/harmony-book)
- **Technologies**: LuaLaTeX (memoir), LilyPond, biblatex e biber, TinyTeX, Python
- **Period**: 06/2026 - ongoing

Publishing toolchain for a book on harmony: the repository versions the typographic method and the build, while the text of the book stays out of git. Typesetting uses LuaLaTeX with the memoir class, LilyPond embedded through lilypond-book for the musical examples, biblatex and biber for the bibliography, imakeidx and glossaries for index and glossary. The TeX environment is a local TinyTeX installation described by a package manifest, reproducible on Windows and Linux.

The manuscript (chapters, examples, bibliography) sits in a folder excluded from git because it is meant for sale; a sample document shows that the chain works. The repository also contains Python tools for the music theory used in the book, such as computing the tritone content of scales and deriving secondary dominants, and a knowledge base on the sources consulted.
