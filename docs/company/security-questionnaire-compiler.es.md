# Cumplimentación asistida de cuestionarios de seguridad y privacidad

**Sector**: empresa de servicios lingüísticos y traducción profesional

**Periodo**: 08/2026 - en curso

**Rol**: IT Manager, desarrollador

**Tecnologías**: Python, openpyxl, python-docx, pypdf, pytest

## Contexto

En la cualificación de proveedores los clientes envían cuestionarios de seguridad y privacidad y documentos contractuales que hay que cumplimentar: cuestionarios en Excel, listas de verificación en Word sobre el tratamiento de datos por cuenta del cliente, nombramientos, formularios de notificación de brechas de datos. Las preguntas se repiten de un cliente a otro con redacciones distintas, y cada respuesta debe ser coherente con las ya dadas y con la postura de seguridad real de la empresa.

## Qué se hizo

Una pipeline en Python que reconoce por sí sola la estructura del documento recibido, Excel o Word, busca las respuestas en una base de conocimiento de pares pregunta-respuesta y produce un borrador cumplimentado que conserva el formato, los estilos y las celdas del archivo original; las respuestas validadas vuelven después a la base de conocimiento. El motor de correspondencia entre preguntas está escrito en Python puro, y las dependencias se limitan a las bibliotecas para leer y escribir formatos de oficina. Código y datos están separados por diseño: el repositorio contiene solo la maquinaria, mientras que la base de conocimiento y los documentos de los clientes están fuera, bajo una raíz declarada en la configuración local, y un control automático verifica que ningún contenido de un cliente entre en los archivos versionados. Las pruebas se ejecutan sobre documentos inventados.

## Resultado

La cumplimentación de un cuestionario parte de un borrador coherente con las respuestas ya dadas en lugar de una hoja en blanco. La rama Excel está en uso; la rama Word ha superado pruebas con documentos reales en algunas partes, y la prueba completa con un documento real está pendiente.
