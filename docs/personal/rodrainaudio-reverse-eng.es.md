# rodrainaudio-reverse-eng

A non-complete reverse-engineering of a customized DAC, 4fun

- **Repositorio**: [alesop95/rodrainaudio-reverse-eng](https://github.com/alesop95/rodrainaudio-reverse-eng)
- **Tecnologías**: LaTeX, analisi hardware di un DAC ES9023
- **Periodo**: 12/2025 - 06/2026, en pausa

Un informe técnico en LaTeX de ingeniería inversa de hardware sobre un amplificador de auriculares económico de marca "Rod Rain audio", un rebrand con un módulo DAC USB integrado. El chasis sigue la topología general del amplificador de auriculares Beyerdynamic A1, mientras que la ruta del DAC combina un receptor USB-I2S SaviTech SA9023 con un chip DAC ESS ES9023, reconstruida a partir de hojas de datos, la inspección visual de la placa y el comportamiento observado bajo Windows 11.

El documento separa lo observado o documentado de lo que sigue siendo hipótesis, y una sección corrige cuatro suposiciones erróneas de un borrador anterior, entre ellas haber tratado el ES9023 como un dispositivo USB en lugar de un DAC de entrada I2S alimentado por un receptor USB separado, y una estimación equivocada de la impedancia de salida y la ganancia del amplificador. Termina con procedimientos de medición para las preguntas aún abiertas y un modelo SPICE paramétrico.
