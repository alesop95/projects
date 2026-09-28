# pok-collecting_update_collection

Just a personal project to update my collection

- **Repositorio**: [alesop95/pok-collecting_update_collection](https://github.com/alesop95/pok-collecting_update_collection)
- **Tecnologías**: Python, xlwings, openpyxl, SQLite, API REST di CardTrader
- **Periodo**: 05/2026 - 06/2026, en pausa

Un complemento de seguimiento de precios para una colección personal de cartas Pokémon TCG guardada en un libro de Excel. El script trata la hoja de cálculo como fuente de verdad: lee las cartas que se poseen directamente del libro mediante automatización COM (xlwings), obtiene los precios de mercado actuales desde la API REST de CardTrader v2 y escribe una caché de búsqueda con fórmulas listas para pegar, de modo que Excel muestre precios actualizados mediante búsquedas al estilo XLOOKUP. Una base de datos SQLite guarda un historial de precios de solo adición, para que las tendencias no se pierdan entre una ejecución y otra.

Nació tras el cierre de la API pública de precios de Cardmarket, hacia 2024 según la documentación del proyecto, que dejó CardTrader como fuente de datos. Un script de descubrimiento asocia por fuzzy matching los nombres de las hojas del libro con el catálogo de expansiones de la API, porque los nombres de las hojas no coinciden con los identificadores de la API. Las fórmulas de búsqueda se generan en sintaxis de Excel en italiano, con el punto y coma como separador y los nombres de función localizados.
