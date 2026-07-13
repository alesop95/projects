# feature-based_characterization_loudspeakers

Master Degree project

- **Repository**: [alesop95/feature-based_characterization_loudspeakers](https://github.com/alesop95/feature-based_characterization_loudspeakers)
- **Languages**: MATLAB, HTML, Python
- **Start date**: 2026-03
- **Last updated**: 2026-06-23
- **Local folder**: `feature-based_characterization_loudspeakers`

This repository holds the full experimental work behind a Master's thesis in Sound and Music Engineering, aimed at predicting how loudspeakers are perceived from objective measurements alone. Fifteen listeners rated four woofers and four tweeters on loudness, timbral balance, and preference in a controlled listening room, with playback synchronized through OSC-driven switching in Reaper for sample-accurate comparisons. In parallel, an objective feature extraction pipeline computes thirteen spectral descriptors, including centroid, rolloff, kurtosis, entropy, and a custom average absolute deviation metric, from anechoic on-axis frequency response and distortion measurements of each driver.

The two data sources are bridged with a regression pipeline: multi-subject ratings are first aggregated with a STATIS-based correlation weighting scheme that down-weights inconsistent raters, then ReliefF feature selection and three regression models, ordinary and stepwise linear regression plus polynomial support vector regression, are trained and compared per attribute using RMSE and R². One-way and two-way ANOVA, run in both MATLAB and Python, validate whether the perceptual differences across speakers are statistically significant. The entire study, GUI, measurement handling, and statistics, is implemented directly in MATLAB, with a custom GUIDE-based interface built for administering the listening test itself.
