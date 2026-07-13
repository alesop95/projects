# rodrainaudio-reverse-eng

A non-complete reverse-engineering of a customized DAC, 4fun

- **Repository**: [alesop95/rodrainaudio-reverse-eng](https://github.com/alesop95/rodrainaudio-reverse-eng)
- **Languages**: TeX, PowerShell, Shell, Python
- **Start date**: 2026-06
- **Last updated**: 2026-07-06
- **Local folder**: `rodrainaudio-reverse-eng`

A hardware reverse-engineering writeup, not a software project: it is a LaTeX technical report analyzing a cheap rebranded "Rod Rain audio" headphone amplifier with an embedded USB DAC module. The chassis follows the general topology of the Beyerdynamic A1 headphone amp, while the DAC path combines a SaviTech SA9023 USB-to-I2S receiver with an ESS ES9023 DAC chip, reconstructed from datasheets, visual inspection of the board, and behavior observed under Windows 11.

What stands out is the methodological discipline: the document explicitly separates what has been observed or is documented from what remains an untested hypothesis, and an entire section is dedicated to correcting four assumptions from an earlier draft that turned out to be wrong, such as initially treating the ES9023 as a USB device instead of an I2S-input DAC fed by a separate USB receiver, and misjudging the amplifier's output impedance and gain. It closes with concrete measurement procedures to resolve the remaining open questions and a parametric SPICE model, treating the analysis as a living document rather than a finished conclusion.
