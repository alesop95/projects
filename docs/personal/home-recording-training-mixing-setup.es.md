# home-recording-training-mixing-setup

- **Repositorio**: [alesop95/home-recording-training-mixing-setup](https://github.com/alesop95/home-recording-training-mixing-setup)
- **Tecnologías**: Ubuntu Studio, kernel generico con preempt=full e threadirqs, PipeWire, Wine
- **Periodo**: 06/2026 - en curso

Repositorio de notas para un home studio de grabación y mezcla. El contenido técnico presente trata de la máquina de trabajo, un ordenador de sobremesa reconvertido con Ubuntu Studio 26.04: la instalación limpia, la configuración de baja latencia obtenida del kernel genérico con los parámetros de arranque `preempt=full` y `threadirqs`, la cadena de audio sobre PipeWire con el procedimiento para verificarla, la capa de compatibilidad Wine para los programas de Windows y el procedimiento de reinstalación y copia de seguridad con Veeam Agent for Linux. Este bloque es una copia sincronizada del proyecto hermano diy-2way-monitors-home, que usa la misma máquina.

La decisión propia del proyecto sigue abierta: la elección de una interfaz de audio con más entradas para la grabación multipista, con los criterios fijados antes de comparar modelos, empezando por el número de entradas simultáneas y la conformidad con la clase de audio USB, que en Linux evita controladores y software de configuración propietarios. Todavía no hay una cadena de señal para la grabación, proyectos de DAW, una lista de equipo ni notas de mezcla.
