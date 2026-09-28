# real-estate

- **Repositorio**: [alesop95/real-estate](https://github.com/alesop95/real-estate)
- **Tecnologías**: Python, TypeScript, React, Excel
- **Periodo**: 08/2026 - en curso

Herramienta local para evaluar la compra de una vivienda en Italia en sus tres destinos posibles: vivienda propia, alquiler e inversión. Produce un libro de Excel de veintiuna hojas con fórmulas vivas, un registro de los inmuebles en evaluación, una ficha de una página para la negociación y un tratado matemático en LaTeX de treinta y dos páginas que deriva cada fórmula del modelo. Cada parámetro fiscal lleva la fuente y la fecha de verificación, y los límites del modelo se declaran en la celda que los produce.

El motor es una librería Python 3.13 con openpyxl como única dependencia obligatoria, usada desde una sola línea de comandos. Calcula los impuestos de transmisión en los cuatro casos, la amortización francesa con amortizaciones anticipadas y una trayectoria del tipo de interés por tramos, la rentabilidad neta nominal y real, el precio máximo sostenible en forma cerrada y una simulación del riesgo sobre mil extracciones con semilla declarada, escritas como valores fijos en el libro para que el resultado sea reproducible. Las cotizaciones OMI, los tipos del BCE y la inflación del ISTAT entran por módulos dedicados, y un modelo local mediante Ollama, opcional, estructura el texto de un anuncio. La verificación abre el libro con Excel mediante COM y busca las celdas con error, y 107 pruebas automáticas cubren el motor, la estructura del libro y la simulación del riesgo.

La herramienta local funciona. Desde septiembre de 2026 se desarrolla, en una rama separada, una aplicación web autenticada sobre Cloudflare, con un motor TypeScript contrastado con 211 vectores producidos por el motor Python, un Worker con rutas autorizadas y una interfaz React; a mediados de septiembre estaban listas dos de las seis áreas previstas más la administración, y la aplicación todavía no está en línea. El registro de inmuebles y los documentos de negociación no están versionados.
