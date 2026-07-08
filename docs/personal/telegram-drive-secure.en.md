# telegram-drive-secure

A customization from the https://github.com/caamer20/Telegram-Drive repo without forking it.

- **Repository**: [alesop95/telegram-drive-secure](https://github.com/alesop95/telegram-drive-secure)
- **Main language**: TypeScript
- **Last updated**: 2026-07-02
- **Local folder**: `telegram-drive-secure-fork`

This is a customization of the open-source desktop app caamer20/Telegram-Drive rather than an independently written project or a formal GitHub fork: the upstream code (Tauri, Rust, React, using Telegram's own servers as a file backend, with channels standing in for folders) was imported at a pinned upstream commit without preserving its original commit history, a decision recorded explicitly in the project's own notes. The stated goal is to add client-side end-to-end encryption of files before upload and general attack-surface hardening on top of the imported app, but as of the latest commits only two changes have actually landed: the clean import itself, and a pass that strips references to the original author from the app identifier and product name plus a review of the inherited CI workflow. The encryption module and the broader hardening work are still planned, not implemented.

Worth noting for anyone reading the code: the upstream README claims an MIT license, but no `LICENSE` file was present in the imported source tree, a discrepancy the project's own documentation flags as unresolved rather than glossing over. The value of this project right now is mostly in the planning documents, threat model, and phased roadmap it carries forward from the fork decision, not in delivered security features.
