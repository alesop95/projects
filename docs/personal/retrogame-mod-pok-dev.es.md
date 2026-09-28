# retrogame-mod-pok-dev

- **Repositorio**: [alesop95/retrogame-mod-pok-dev](https://github.com/alesop95/retrogame-mod-pok-dev)
- **Tecnologías**: Python, formati di salvataggio delle generazioni 1-3
- **Periodo**: 08/2026 - en curso

Investigación técnica, código y procedimientos para leer, verificar y transformar datos de Pokémon entre consolas y generaciones distintas, con el objetivo de completar una colección en Pokémon Home a partir de cartuchos y consolas propios. El repositorio se divide en diez subproyectos que avanzan en paralelo, desde el modding de Nintendo 3DS y el volcado de los cartuchos hasta la sustitución de la batería, y desde el intercambio inalámbrico local con Nintendo Switch hasta la recreación de las distribuciones y los eventos históricos.

La parte técnica central es una referencia byte a byte de los formatos de las tres primeras generaciones, con las estructuras de caja y equipo, las codificaciones de los nombres, las sumas de comprobación, el cifrado y el protocolo del cable Link, junto con la librería Python pokebridge, que lee y escribe estructuras y partidas guardadas de esas generaciones y tiene pruebas de simetría byte a byte y un módulo que sintetiza el paso de los datos de la tercera a la cuarta generación. El caso de una partida de Pokémon Esmeralda documenta la corrección de un inventario corrupto, con la recomposición de las ranuras, el recálculo de las sumas de comprobación de sección y la verificación de la escritura por relectura. Los catálogos y las tablas se generan con herramientas reproducibles, y los lotes más recientes se generan y controlan con la librería PKHeX.Core.

Un registro único de fuentes indica para cada una qué documenta y con qué fiabilidad, y distingue las fuentes leídas de las solo catalogadas. El proyecto está activo: a mediados de septiembre de 2026 la lista de control hacia Home contaba 685 entradas de las 1025 de la Pokédex nacional. Las partidas guardadas y los volcados personales quedan fuera de git.
