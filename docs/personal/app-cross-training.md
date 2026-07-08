# app-cross-training

_Nessuna descrizione su GitHub._

- **Repository**: [alesop95/app-cross-training](https://github.com/alesop95/app-cross-training)
- **Ultimo aggiornamento**: 2026-06-23
- **Cartella locale**: `app-cross-training`

X CROSS Training è, a questo stadio, un pacchetto di specifiche e dataset per un'app mobile Flutter destinata a programmare allenamenti di cross-training/functional, non ancora un'applicazione implementata: il repository dichiara esplicitamente che non esiste codice applicativo, ma solo documenti e dati JSON estratti da una presentazione PowerPoint di partenza e da un foglio di calcolo Excel.

L'artefatto tecnico più concreto è la progettazione dell'algoritmo centrale di generazione delle combinazioni: gli allenamenti si costruiscono combinando esercizi provenienti da tre famiglie (sollevamento pesi, ginnastica, locomozione) in combinazioni senza ripetizioni di uno, due o tre elementi lungo un ciclo di allenamento. La progettazione deriva direttamente da un prototipo Excel funzionante che usava RANDBETWEEN su un intervallo decrescente per estrarre combinazioni senza reinserimento, qui documentato come variante dell'algoritmo di Fisher-Yates e tradotto in una specifica di classe Dart (GeneratoreCombinazioni) con filtri per attrezzatura disponibile, livello dell'atleta e gruppi di esercizi abilitati. Il resto del repository definisce i modelli dati, le modalità di allenamento (EMOM, Tabata, AMRAP, For Time) e una roadmap per l'MVP. Si presenta come una pianificazione preliminare accurata, consegnata per lo sviluppo, più che come un prodotto funzionante.
