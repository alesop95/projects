# crosswords

A personal repo to develop new crossword games (italian language)

- **Repositorio**: [alesop95/crosswords](https://github.com/alesop95/crosswords)
- **Tecnologías**: TypeScript, Vite, Web Worker
- **Periodo**: 07/2026, finalizado

Constructor de crucigramas al estilo italiano que funciona en el navegador, sin servidor: todo el trabajo se queda en la máquina del usuario. Se dibuja el esquema (casillas negras libres, simetría opcional, de 5x5 a 25x25), se rellena la cuadrícula de forma automática o palabra por palabra, se escriben las definiciones, se guarda en formato ipuz y se imprimen esquema y solución en A4. La app está en línea en [alesop95.github.io/crosswords](https://alesop95.github.io/crosswords/) y se vuelve a publicar con GitHub Actions en cada push.

El rellenado automático es un resolvedor de restricciones (backtracking con heurística MRV, forward checking y consistencia de arcos) ejecutado en un Web Worker, de modo que la interfaz sigue respondiendo y el rellenado se puede interrumpir. El diccionario, unas 350.000 entradas, se genera a partir de Morph-it! y se pondera con las frecuencias de itWaC, así el resolvedor prefiere las palabras comunes. El repositorio documenta también el marco legal y fiscal italiano para vender crucigramas a revistas. La versión 1 está cerrada.
