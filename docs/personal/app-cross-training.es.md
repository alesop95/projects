# app-cross-training

_Sin descripción en GitHub._

- **Repositorio**: [alesop95/app-cross-training](https://github.com/alesop95/app-cross-training)
- **Lenguajes**: -
- **Fecha de inicio**: 2026-06
- **Última actualización**: 2026-06-23
- **Carpeta local**: `app-cross-training`

X CROSS Training es, en esta etapa, un paquete de especificaciones y datasets para una app móvil Flutter pensada para programar entrenamientos de cross-training/funcional, todavía no una aplicación implementada: el repositorio declara explícitamente que no existe código de aplicación, solo documentos y datos JSON extraídos de una presentación PowerPoint de origen y de un libro de Excel.

El artefacto técnico más concreto es el diseño del algoritmo central de generación de combinaciones: los entrenamientos se construyen combinando ejercicios de tres familias (halterofilia, gimnasia, locomoción) en combinaciones sin repetición de uno, dos o tres elementos a lo largo de un ciclo de entrenamiento. El diseño deriva directamente de un prototipo funcional en Excel que usaba RANDBETWEEN sobre un rango decreciente para extraer combinaciones sin reemplazo, documentado aquí como una variante del algoritmo de Fisher-Yates y traducido a una especificación de clase Dart (GeneratoreCombinazioni) con filtros por equipamiento disponible, nivel del atleta y grupos de ejercicios habilitados. El resto del repositorio define los modelos de datos, los modos de entrenamiento (EMOM, Tabata, AMRAP, For Time) y una hoja de ruta para el MVP. Se presenta como una planificación previa minuciosa, entregada para su desarrollo, más que como un producto funcional.
