# app-cross-training

_No description on GitHub._

- **Repository**: [alesop95/app-cross-training](https://github.com/alesop95/app-cross-training)
- **Languages**: -
- **Start date**: 2026-06
- **Last updated**: 2026-06-23
- **Local folder**: `app-cross-training`

X CROSS Training is a Flutter mobile app for programming cross-training and functional-training workouts, built from a set of specs and datasets extracted from an existing PowerPoint deck and Excel workbook. The repository started as a specification-only package (documents, data model, JSON datasets) meant for handoff to a developer, and has since grown to include a real Flutter scaffold: design system, reusable components, and the app's main screens.

The product's core idea is building workouts by combining exercises from three families, weightlifting, gymnastics, and locomotion, into non-repeating one-, two-, or three-element combinations across a training cycle. The design is derived from a working Excel prototype that used RANDBETWEEN over a shrinking range to draw combinations without replacement, a Fisher-Yates variant. In the Flutter code this logic is implemented as a CombinationGenerator class, with filters for available equipment, athlete level, and enabled exercise groups, pure logic with no Flutter dependency and therefore testable in isolation (with its own test suite). The repository today holds more than planning alone: a Flutter scaffold with a themeable design system, the main screens matching the design mockup, a working Tabata timer, and the combination generator with its tests, though it has never been compiled or run on a real environment (Flutter isn't installed on the machine it was written on).
