# template-claude-developing

A customized Claude code setup for starting a project from scratch (or.... boosting it!)

- **Repository**: [alesop95/template-claude-developing](https://github.com/alesop95/template-claude-developing)
- **Technologies**: Claude Code, Markdown, Python, PowerShell
- **Period**: 06/2026 - ongoing

A portable system of context, documentation and version control for projects developed with Claude Code and Codex. It installs into a project's `.claude` folder and keeps the project's state recoverable from the repository at any time: the chat session is lost when it closes, while project memory, technical sheets and the decision log live on disk and are read again at every new session. Two fixed prompts instantiate it on a new project or apply it retroactively to an existing one, rebuilding the memory from the commit history without rewriting it.

Each technical sheet carries a metadata block that anchors it to a commit and to the code paths it describes, and the `sync-context` skill compares those paths with the current state and proposes targeted updates instead of regenerating the documents. Around this core sit modular rules on style, git identity, permissions, context usage and the reliability of tests, Python tools for the Markdown convention and Italian typography, and a catalogue of optional packages split into ten sectors, which a skill proposes according to the sectors recognized in the project. Commit and push always stay manual.

The template has been under continuous development since June 2026 and is used by about thirty personal repositories, including most of the projects described on this site; fixes that arise in one project are generalized in the template and then propagated to the others.
