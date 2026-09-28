# feature-based_characterization_loudspeakers

Master Degree project

- **Repository**: [alesop95/feature-based_characterization_loudspeakers](https://github.com/alesop95/feature-based_characterization_loudspeakers)
- **Tecnologie**: MATLAB (GUIDE, Statistics and Machine Learning Toolbox), Reaper con OSC, Python (SciPy)
- **Periodo**: 01/2020 - 02/2020, concluso

Lavoro sperimentale di una tesi magistrale che cerca di predire la percezione di un altoparlante a partire dalle sole misure oggettive. Quindici ascoltatori hanno valutato quattro woofer e quattro tweeter su volume percepito, bilanciamento timbrico e preferenza in una sala d'ascolto controllata, con la commutazione fra i diffusori pilotata in Reaper via OSC e un'interfaccia di test scritta in MATLAB. In parallelo, tredici descrittori spettrali (fra cui centroide, rolloff, kurtosis ed entropia) sono estratti dalla risposta in frequenza anecoica e dalle misure di distorsione di ciascun driver.

Le valutazioni sono aggregate con una pesatura per correlazione basata su STATIS, che riduce il peso dei valutatori incoerenti. Per ogni attributo si confrontano regressione lineare, regressione stepwise e support vector regression polinomiale, con selezione delle feature ReliefF e valutazione su RMSE e R². ANOVA a una e due vie, in MATLAB e in Python, verifica se le differenze percepite sono significative. La parte principale del lavoro, cioè interfaccia di test, gestione delle misure e statistica, è in MATLAB.
