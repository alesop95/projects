# crosswords

A personal repo to develop new crossword games (italian language)

- **Repository**: [alesop95/crosswords](https://github.com/alesop95/crosswords)
- **Linguaggi**: TypeScript, PowerShell, Shell, Python
- **Data di inizio**: 2026-07
- **Ultimo aggiornamento**: 2026-07-06
- **Cartella locale**: `crosswords`

Un'app web local-first, senza backend, per costruire griglie di parole crociate in stile tradizionale italiano, scritta in TypeScript con Vite. Oltre al prevedibile editor di griglia con caselle nere libere e simmetria opzionale, e a un editor di definizioni con esportazione ipuz e supporto alla stampa, l'ingegneria interessante sta nel riempimento automatico: la codebase implementa un solver a soddisfacimento di vincoli con propagazione ad arc-consistency, eseguito fuori dal thread principale in un web worker, invece di un semplice abbinatore di parole a forza bruta, così che l'interfaccia resti reattiva anche riempiendo griglie grandi. Il dizionario dei candidati è generato a partire dal lessico italiano Morph-it! e annotato con punteggi di frequenza, il che permette al solver di preferire le parole più comuni durante il riempimento automatico.

Il progetto documenta inoltre, in un file di documentazione dedicato, il quadro giuridico e fiscale italiano per la vendita di cruciverba alle riviste a stampa, il che suggerisce che venga costruito guardando a un uso commerciale concreto, per quanto modesto, più che come puro esercizio. È esplicitamente segnato come in corso di sviluppo, con test unitari e di performance già in atto attorno al solver.
