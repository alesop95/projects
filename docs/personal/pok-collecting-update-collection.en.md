# pok-collecting_update_collection

Just a personal project to update my collection

- **Repository**: [alesop95/pok-collecting_update_collection](https://github.com/alesop95/pok-collecting_update_collection)
- **Languages**: Python, PowerShell, Shell, JavaScript
- **Start date**: 2026-05
- **Last updated**: 2026-07-06
- **Local folder**: `pok-collecting_update_collection`

A price-tracking companion for a personal Pokémon TCG collection kept in an Excel workbook. Rather than replacing the spreadsheet, the script treats it as the source of truth: it reads which cards are owned directly from the workbook via COM automation (xlwings), fetches current market prices from the CardTrader v2 REST API, and writes a lookup cache plus ready-to-paste formulas back so Excel can display up-to-date prices through XLOOKUP-style lookups. A SQLite database keeps an append-only price history so trends aren't lost between runs.

It was built after Cardmarket closed its public pricing API in 2024, forcing a switch to CardTrader as the only remaining data source. A discovery script fuzzy-matches the workbook's sheet names against the API's expansion catalogue to bootstrap the sheet-to-expansion mapping, since Excel sheet names don't line up cleanly with API identifiers. The generated lookup formulas are emitted in Italian Excel syntax (semicolon-separated, localized function names), a detail that reflects the single-user, single-locale nature of the tool rather than any attempt at portability.
