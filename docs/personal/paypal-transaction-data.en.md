# paypal-transaction-data

- **Repository**: [alesop95/paypal-transaction-data](https://github.com/alesop95/paypal-transaction-data)
- **Technologies**: Python, API REST di PayPal, Google Sheets, Excel
- **Period**: 06/2026, paused

A Python command-line tool that downloads transaction history from the PayPal REST API and syncs it to a Google Sheet, or alternatively to an Excel file, to keep an accounting ledger without copying statements by hand. It extracts the fields needed for reconciliation, namely transaction and reference identifiers, gross and net amounts, fees, currency, status and payer, and skips records already synced.

It works in sandbox and live mode, as a single sync, over a date range or as a periodic job, with a subcommand that checks the API connection. The repository contains only code and instructions, no transaction data.
