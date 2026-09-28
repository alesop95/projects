# diy-2way-monitors-home

- **Repositorio**: [alesop95/diy-2way-monitors-home](https://github.com/alesop95/diy-2way-monitors-home)
- **Tecnologías**: REW, Blender, GNU Octave (MATAA), VituixCAD, FreeCAD, Akabak 3 sotto Wine, Ubuntu Studio
- **Periodo**: 06/2026 - en curso

Diseño y construcción de un par de monitores de estudio de dos vías para un punto de escucha doméstico con techo inclinado, que no admite tratamiento acústico. El proyecto parte de la sala: se mide el punto de escucha, se valida un modelo geométrico de la sala contra la medición, se diseña el altavoz y solo al final se optimiza la posición con los dos modelos juntos. El objetivo es una respuesta dentro de más o menos 2 dB de 60 Hz a unos 20 kHz, en eje y hasta diez grados fuera de eje, medida en el punto de escucha real.

El flujo funciona sobre Ubuntu Studio: nativos REW, Blender, Octave con MATAA y FreeCAD; bajo Wine los programas de Windows sin alternativa, es decir Akabak 3 para la simulación electroacústica y de la sala, VACS, VituixCAD para crossover y directividad y EASE Focus.

Estado: el entorno de trabajo está preparado y documentado paso a paso, con los cuatro programas de Windows funcionando, la cadena de audio verificada y un registro de cada intervención con su resultado. La parte física no ha empezado: ninguna medición, ningún driver comprado, ningún cabinet. El paso en curso es el levantamiento geométrico de la sala.
