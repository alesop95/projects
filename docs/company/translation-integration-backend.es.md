# Backend de integración para un servicio de traducción

**Sector**: empresa de servicios lingüísticos y traducción profesional

**Periodo**: 03/2025 - en curso

**Rol**: IT Manager, desarrollador backend

**Tecnologías**: Python, FastAPI, integración con un sistema de gestión de proyectos de
traducción de terceros, un motor de traducción automática basado en inteligencia artificial, un
servicio de traducción automática público como respaldo

## Contexto

El servicio de traducción dirigido a los clientes se apoya en un sistema de gestión de proyectos
de terceros para la asignación del trabajo y en un motor de traducción automática para el primer
borrador. Los dos sistemas no se comunican de forma nativa en el flujo requerido por la empresa:
hacía falta una capa de integración que orquestara las llamadas entre ambos, con una cobertura de
continuidad para cuando el motor principal no está disponible o no cubre una combinación de
idiomas.

## Qué se hizo

Backend REST en Python/FastAPI que actúa de puente entre el sistema de gestión de proyectos y el
motor de traducción, con un servicio de traducción automática público usado como respaldo cuando
el motor principal no responde o no cubre el idioma solicitado. El flujo está organizado en tres
fases (recuperación del proyecto, envío al motor de traducción, recopilación y normalización del
resultado), con gestión de errores y reintentos en la capa de integración. Documentación técnica
estructurada para poder retomar el trabajo entre sesiones no consecutivas.

## Resultado

Automatiza un paso que antes requería intervención manual para encaminar cada proyecto entre los
dos sistemas, reduciendo el tiempo de espera entre la apertura de un proyecto de traducción y la
disponibilidad del primer borrador automático.
