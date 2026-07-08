# crosswords

A personal repo to develop new crossword games (italian language)

- **Repositorio**: [alesop95/crosswords](https://github.com/alesop95/crosswords)
- **Lenguaje principal**: TypeScript
- **Última actualización**: 2026-07-06
- **Carpeta local**: `crosswords`

Una app web local-first, sin backend, para construir cuadrículas de crucigramas al estilo tradicional italiano (parole crociate), escrita en TypeScript con Vite. Más allá del previsible editor de cuadrícula con casillas negras libres y simetría opcional, y de un editor de pistas con exportación a ipuz y soporte de impresión, la ingeniería interesante está en el rellenado automático: la base de código implementa un solver de satisfacción de restricciones con propagación de arc-consistency, ejecutado fuera del hilo principal en un web worker, en lugar de un simple comparador de palabras por fuerza bruta, de modo que la interfaz permanece receptiva incluso al rellenar cuadrículas grandes. El diccionario de candidatos se genera a partir del léxico italiano Morph-it! y se anota con puntuaciones de frecuencia, lo que permite al solver preferir palabras comunes durante el autorrelleno.

El proyecto también documenta, en un archivo de documentación dedicado, el marco legal y fiscal italiano para vender crucigramas a revistas impresas, lo que sugiere que se está construyendo pensando en un uso comercial concreto, aunque modesto, más que como un simple ejercicio. Está marcado explícitamente como en desarrollo, con pruebas unitarias y de rendimiento ya implementadas alrededor del solver.
