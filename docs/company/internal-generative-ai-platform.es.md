# Plataforma interna de inteligencia artificial generativa

!!! tip "Proyecto insignia, en evolución continua"
    El más significativo entre los proyectos internos descritos en esta sección, en desarrollo
    activo: aborda IA generativa, infraestructura de GPU dedicada, orquestación de agentes e
    integración con el sistema de identidad corporativa. Esta página se ampliará más adelante cuando
    el trabajo se estabilice.

**Sector**: empresa de servicios lingüísticos y traducción profesional

**Periodo**: por confirmar - en curso

**Rol**: IT Manager, desarrollador full-stack, I+D

**Tecnologías**: Ollama (LLM autoalojado en GPU dedicada), RAG (retrieval-augmented generation),
Qdrant (base de datos vectorial), n8n (orquestación de workflows de IA agéntica), autenticación SSO
corporativa, proxy inverso en LAN protegida, Model Context Protocol (MCP), frontend propietario

## Contexto

La empresa quería un asistente conversacional interno basado en inteligencia artificial generativa,
con acceso al contexto documental corporativo, sin depender de servicios cloud de terceros para cada
interacción y con pleno control sobre los datos y la infraestructura. También era necesaria una forma
de extender las capacidades del asistente con herramientas personalizadas, sin limitarse a una simple
interfaz de chat.

## Qué se hizo

Plataforma interna de IA generativa construida alrededor de Ollama como motor de inferencia
autoalojado en hardware dedicado con GPU, con pruebas de referencia (benchmarks) e I+D para validar
las decisiones de modelo y hardware. Un sistema RAG con Qdrant como base de datos vectorial
proporciona el contexto documental corporativo al modelo. Los agentes de IA orquestan flujos de
trabajo personalizados mediante n8n, con la posibilidad de componer distintos workflows según el
perfil de quien accede. El acceso se realiza a través del mismo sistema de identidad corporativa
(SSO) usado para los demás servicios, de modo que el asistente reconozca al usuario y aplique el
contexto adecuado. El frontend se ha escrito desde cero con la identidad visual corporativa, y
también actúa como cliente MCP (Model Context Protocol) en la red interna hacia servidores MCP
personalizados, tanto centralizados como distribuidos en endpoints individuales. La infraestructura
se expone en la red interna mediante un proxy inverso protegido, con entornos de prueba y producción
separados.

## Resultado

Un asistente de IA interno personalizado según el contexto corporativo, con los datos y la inferencia
bajo control directo de la empresa en lugar de confiarlos por completo a servicios cloud de terceros,
y una arquitectura extensible que permite añadir nuevas herramientas y flujos sin tener que reescribir
el frontend.
