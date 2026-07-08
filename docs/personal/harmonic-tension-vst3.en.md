# harmonic-tension-vst3

_No description on GitHub._

- **Repository**: [alesop95/harmonic-tension-vst3](https://github.com/alesop95/harmonic-tension-vst3)
- **Main language**: C++
- **Last updated**: 2026-06-23
- **Local folder**: `harmonic-tension-vst3`

This is a VST3 audio plugin, built in C++ on the JUCE framework, that listens to incoming MIDI in real time and turns harmonic analysis into a live control signal for stage lighting rather than into sound. It implements Elaine Chew's Spiral Array model, a geometric representation of tonal harmony, computing metrics such as harmonic tension, cloud diameter, and tensile strain from the sequence of played notes and their timing, then estimating the current key by finding the closest point on the spiral to the notes' center of effect. The idea was demonstrated live, mapping the derived tension values to brightness and pattern changes on stage lights, at the Festivalle electronic music event in Valle dei Templi in August 2019.

The processor class itself is still named `ProgettoProvaAudioProcessor` ("test project" in Italian) in the source, a naming leftover from JUCE's project scaffolding that signals this stayed a working prototype rather than a polished, renamed release. The accompanying PDF in the repository documents the underlying geometric model and the intelligent-lighting use case in more depth than the code comments do.
