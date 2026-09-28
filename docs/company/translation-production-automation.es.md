# Automatizaciones para la producción lingüística

**Sector**: empresa de servicios lingüísticos y traducción profesional

**Periodo**: 10/2024 - en curso

**Rol**: IT Manager, desarrollador de scripts

**Tecnologías**: PowerShell, AutoHotkey, Programador de tareas de Windows, Python, spaCy, NLTK, openpyxl

## Contexto

El trabajo de los project managers y de los traductores pasa por herramientas que no siempre ofrecen una interfaz programable, y por materiales que hay que preparar antes de la traducción: sitios web descargados, PDF, archivos XML, documentos Word y Excel. Parte de estas operaciones se repetía a mano en cada proyecto, y la copia de seguridad de las memorias de traducción dependía de una exportación manual.

## Qué se hizo

Dos grupos de herramientas. El primero, de 2024 y 2025, es una colección de scripts en Python para preparar el material que se va a traducir: extracción de texto de HTML, PDF, XML, Word y Excel, división de archivos Excel grandes, reducción por muestreo de una memoria de traducción, extracción de n-gramas con spaCy y NLTK para detectar la terminología recurrente, control de líneas demasiado largas, y flujos que extraen el texto de un esqueleto HTML y lo reinsertan después de la traducción. El segundo, de noviembre de 2025, es la copia de seguridad diaria de las memorias de traducción desde el servidor compartido de la herramienta CAT: un script de PowerShell crea la carpeta con fecha, prepara el archivo de configuración del trabajo, controla con AutoHotkey la herramienta de exportación del proveedor, que no tiene interfaz programable, aplica una política de conservación y se ejecuta como tarea programada.

## Resultado

Las memorias de traducción tienen una copia de seguridad diaria automática con conservación controlada, en funcionamiento desde noviembre de 2025. Los scripts de preparación del material se usaron en los proyectos de 2024 y 2025 y hoy ya no se desarrollan.
