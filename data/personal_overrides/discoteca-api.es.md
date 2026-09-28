Prueba de concepto de una lista de invitados con código QR para una discoteca. Un único endpoint POST recibe nombre y email, validados con Zod, crea o reutiliza el usuario en una base de datos SQLite mediante Prisma, genera un código QR con los datos del invitado y lo envía por email con Nodemailer, para mostrarlo en la entrada. Un frontend Vite y React contiene solo el formulario de registro.

El modelo de datos es una sola tabla de usuarios, sin eventos, listas separadas ni control de aforo, y no hay tests automáticos.
