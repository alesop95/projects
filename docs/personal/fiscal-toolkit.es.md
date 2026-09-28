# fiscal-toolkit

- **Repositorio**: [alesop95/fiscal-toolkit](https://github.com/alesop95/fiscal-toolkit)
- **Tecnologías**: Node.js, TypeScript, SQLite (node:sqlite), Vitest
- **Periodo**: 07/2026 - en curso

Herramienta personal para entender la fiscalidad de un trabajador por cuenta ajena en Italia: del bruto anual (RAL) al neto, con el peso del IRPEF, las deducciones, la cuña fiscal, las cotizaciones al INPS y los recargos regionales y municipales. El cálculo es determinista y explicable: cada partida del resultado lleva el parámetro usado y la norma de la que procede. Los parámetros están en archivos versionados por año fiscal, actualizados a mano con cada Ley de Presupuestos, y se verifican contra el texto legal indexado por el proyecto legal-consultant.

Estado: el motor de cálculo para 2025 y 2026 está completo y cubierto por tests, con una CLI y una primera interfaz local que muestran la composición del salario y la comparación entre años. La comparación entre trabajo por cuenta ajena y autónomo (partita IVA) está prevista pero todavía no implementada. La fase siguiente, la lectura de documentos fiscales reales (Certificazione Unica, nóminas), no ha empezado. No es asesoramiento fiscal.
