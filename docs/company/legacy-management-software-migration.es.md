# Migración de un software de gestión legacy a un sistema operativo con soporte

**Sector**: empresa de servicios lingüísticos y traducción profesional

**Periodo**: por confirmar (duración: algunos meses)

**Rol**: IT Manager, administrador de sistemas

**Tecnologías**: Ubuntu 10 → Ubuntu 24.04 LTS, parches de aplicaciones, gestión de usuarios en red LAN

## Contexto

Un software de gestión legacy de la empresa, que databa de mediados de la década de 2000, seguía
ejecutándose en una distribución Linux sin soporte ni actualizaciones de seguridad desde hacía
tiempo, con un riesgo creciente de incompatibilidades y vulnerabilidades sin resolver.

## Qué se hizo

Migración, con una duración de algunos meses, del software de gestión legacy de Ubuntu 10 a Ubuntu
24.04 LTS, con la restauración 1:1 de todos los parches de aplicaciones necesarios para mantener la
compatibilidad con los usuarios específicos de la red LAN que dependen del software, documentada en
detalle para referencia futura.

## Resultado

Un software de gestión crítico para la actividad de la empresa llevado a un sistema operativo con
soporte y con posibilidad de aplicar parches, eliminando el riesgo acumulado de funcionar en una
distribución fuera de soporte (end-of-life), sin pérdida de funcionalidad para los usuarios finales.
