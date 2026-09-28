# discoteca-api

- **Repository**: [alesop95/discoteca-api](https://github.com/alesop95/discoteca-api)
- **Technologies**: TypeScript, Express 5, Prisma, SQLite, Zod, Nodemailer, React
- **Period**: 05/2025 - 06/2025, completed

Proof of concept of a QR-code guest list for a nightclub. A single POST endpoint receives name and email, validated with Zod, creates or reuses the user in a SQLite database through Prisma, generates a QR code with the guest's data and emails it with Nodemailer, to be shown at the door. A Vite and React frontend holds only the registration form.

The data model is a single users table, with no events, separate lists or capacity tracking, and there are no automated tests.
