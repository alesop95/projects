# sony-xperia-1-III-customization

_No description on GitHub._

- **Repository**: [alesop95/sony-xperia-1-III-customization](https://github.com/alesop95/sony-xperia-1-III-customization)
- **Main language**: Python
- **Last updated**: 2026-07-06
- **Local folder**: `sony-xperia-1-III-customization`

A documentation and tooling project around customizing a Sony Xperia 1 III (codename pdx215) running LineageOS 22.2, organized as a set of runbooks covering software setup, audio, photo/video and gaming, alongside a small collection of standalone scripts. The tooling includes PowerShell and shell scripts to preflight-check the phone and batch-install APKs over ADB, a Magisk module skeleton, and a set of Python audio-analysis scripts (spectral auditing, benchmark calculation and track benchmarking against reference masters) built to evaluate the quality of high-resolution music files against source masters for the device's audio path.

A separate script converts a large source .docx (kept local, outside version control) into the Markdown documentation tracked in the repo, which explains why the docs are structured as generated runbooks rather than hand-authored pages. This is a personal device-configuration project rather than a reusable library: the value is in the accumulated notes, checklists and small verification scripts rather than in a packaged deliverable.
