# feature-based_characterization_loudspeakers

Master Degree project

- **Repository**: [alesop95/feature-based_characterization_loudspeakers](https://github.com/alesop95/feature-based_characterization_loudspeakers)
- **Linguaggi**: MATLAB, HTML, Python
- **Data di inizio**: 2026-03
- **Ultimo aggiornamento**: 2026-06-23
- **Cartella locale**: `feature-based_characterization_loudspeakers`

Questo repository contiene l'intero lavoro sperimentale alla base di una tesi magistrale in Sound and Music Engineering, volta a predire come vengono percepiti gli altoparlanti a partire solo da misurazioni oggettive. Quindici ascoltatori hanno valutato quattro woofer e quattro tweeter su volume percepito, bilanciamento timbrico e preferenza, in una sala d'ascolto controllata, con la riproduzione sincronizzata tramite commutazione pilotata via OSC in Reaper per confronti sample-accurate. In parallelo, una pipeline oggettiva di estrazione di feature calcola tredici descrittori spettrali, tra cui centroide, rolloff, kurtosis, entropia e una metrica personalizzata di deviazione assoluta media, a partire dalla risposta in frequenza anecoica on-axis e dalle misurazioni di distorsione di ciascun driver.

Le due fonti di dati sono collegate con una pipeline di regressione: le valutazioni multi-soggetto vengono prima aggregate con uno schema di pesatura per correlazione basato su STATIS che riduce il peso dei valutatori incoerenti, poi vengono addestrati e confrontati per attributo tre modelli, regressione lineare ordinaria e stepwise più support vector regression polinomiale, tramite selezione di feature ReliefF e valutazione con RMSE e R². ANOVA a una via e a due vie, eseguita sia in MATLAB sia in Python, verifica se le differenze percettive tra gli altoparlanti sono statisticamente significative. L'intero studio, GUI, gestione delle misurazioni e statistica, è implementato direttamente in MATLAB, con un'interfaccia personalizzata basata su GUIDE costruita per condurre il test d'ascolto stesso.
