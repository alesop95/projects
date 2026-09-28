# Plataforma interna de inteligencia artificial generativa

**Sector**: empresa de servicios lingüísticos y traducción profesional

**Periodo**: 03/2025 - en curso

**Rol**: IT Manager, desarrollador full-stack, I+D

**Tecnologías**: Ollama con modelos de código abierto en GPU dedicada, RAG con Qdrant y embeddings bge-m3, n8n para la orquestación de los workflows, backend Node.js, frontend React, Nginx como proxy inverso, Docker Compose, autenticación con la identidad corporativa (SSO), Model Context Protocol (MCP) en el entorno de pruebas

## Contexto

La empresa quería un asistente interno que respondiera sobre la documentación corporativa sin enviar los documentos a servicios externos de inteligencia artificial, sobre hardware ya disponible. La pregunta técnica era si una sola GPU en una máquina reutilizada bastaba para servir una aplicación empresarial con tiempos de respuesta aceptables.

## Qué se hizo

La primera versión, iniciada en 2025, usaba n8n, una base de datos vectorial local y un modelo ejecutado en CPU, con latencias altas en los modelos más grandes. En 2026 la aplicación se reescribió con un backend Node.js, un frontend React y Qdrant como base de datos vectorial, en contenedores detrás de un proxy inverso, con la inferencia a cargo de Ollama en un host de la red interna con GPU dedicada. El flujo en producción es un chat RAG: la pregunta se convierte en embedding, Qdrant devuelve los pasajes pertinentes y un agente de n8n genera la respuesta con ese contexto; un segundo flujo indexa los PDF que suben los administradores. El acceso pasa por la identidad corporativa.

En un entorno de pruebas separado, hoy fuera de servicio, existe un servidor MCP que expone herramientas filtradas por departamento, pensado para un primer caso de uso en la redacción de borradores de correos comerciales; no forma parte del stack de producción. En paralelo se realizó un benchmark entre CPU y GPU y entre modelos de distinto tamaño, sobre el que se está preparando un whitepaper.

## Resultado

El chat sobre documentos corporativos está en producción, con la inferencia y el archivo documental en la red interna; la autenticación, en cambio, pasa por un servicio de identidad externo. La ampliación con herramientas mediante MCP sigue en fase de pruebas, y los resultados del benchmark se publicarán con el whitepaper.
