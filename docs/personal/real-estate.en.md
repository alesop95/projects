# real-estate

- **Repository**: [alesop95/real-estate](https://github.com/alesop95/real-estate)
- **Technologies**: Python, TypeScript, React, Excel
- **Period**: 08/2026 - ongoing

A local tool for evaluating the purchase of a residential property in Italy for its three possible uses: own home, rental income and investment. It produces a 21-sheet Excel workbook with live formulas, a register of the properties under evaluation, a one-page sheet for negotiations and a 32-page mathematical treatment in LaTeX that derives every formula of the model. Every tax parameter carries its source and verification date, and the model's limits are stated in the cell that produces them.

The engine is a Python 3.13 library with openpyxl as its only mandatory dependency, driven by a single command line. It computes transfer taxes in the four cases, French amortization with voluntary prepayments and a stepped rate path, nominal and real net yield, the maximum sustainable price in closed form, and a risk simulation over a thousand draws with a declared seed, written as fixed values in the workbook so the result stays reproducible. OMI property valuations, ECB rates and ISTAT inflation come in through dedicated modules, and an optional local model via Ollama structures the text of a listing. Verification opens the workbook in Excel via COM and looks for cells in error, and 107 automated tests cover the engine, the workbook structure and the risk simulation.

The local tool works. Since September 2026 an authenticated web application on Cloudflare has been under development on a separate branch, with a TypeScript engine checked against 211 vectors produced by the Python engine, a Worker with authorized routes and a React interface; by mid-September two of the six planned areas plus administration were ready, and the application is not online yet. The property register and negotiation documents are not version-controlled.
