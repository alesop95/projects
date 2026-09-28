Prova di concetto di una lista ospiti con codice QR per una discoteca. Un unico endpoint POST riceve nome ed email, validati con Zod, crea o riusa l'utente in un database SQLite tramite Prisma, genera un codice QR con i dati dell'ospite e lo invia per email con Nodemailer, da mostrare all'ingresso. Un frontend Vite e React contiene il solo modulo di registrazione.

Il modello dati è una sola tabella di utenti, senza eventi, liste distinte o gestione della capienza, e non ci sono test automatici.
