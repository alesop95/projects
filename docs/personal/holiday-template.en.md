# holiday-template

A free-customized interactive holiday tracker

- **Repository**: [alesop95/holiday-template](https://github.com/alesop95/holiday-template)
- **Technologies**: JavaScript (moduli ES), Firebase Firestore e Hosting, Leaflet, Python, FastAPI
- **Period**: 06/2026 - ongoing

Template for building progressive web apps for trip planning shared between two people. A single HTML and JavaScript shell, split into ES modules, handles rendering, state and synchronization with Firebase and is never edited; each trip has its own folder under `trips/` with a single configuration file for itinerary, restaurants, map markers and checklist. All trips share one Firebase project and are separated in Firestore by an identifier, so the checklist syncs in real time between the two devices without a backend per trip. Every tab can be printed to PDF.

Next to the planner there are four FastAPI services, local only for now: flight search (scraping Google Flights), accommodation search, points of interest from OpenStreetMap and a service that combines them into a single response, called by the shell from a planning tab. Two flight data sources, Amadeus and Kiwi Tequila, were integrated and then removed when they closed self-service access. Work is in progress: the services have not been deployed yet.
