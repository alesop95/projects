# Migración de un software de gestión heredado a un sistema operativo con soporte

**Sector**: empresa de servicios lingüísticos y traducción profesional

**Periodo**: 02/2026 - en curso

**Rol**: IT Manager, administrador de sistemas

**Tecnologías**: Ubuntu 10.04 LTS → Ubuntu 24.04 LTS, Docker, contenedores separados para producción y pruebas, base de datos relacional, Proxmox VE

## Contexto

El software de gestión que la empresa usó para el trabajo diario hasta 2021, una aplicación web de mediados de los años 2000, hoy sirve como archivo: se consulta internamente para los datos históricos. Funcionaba en un servidor Ubuntu 10.04 LTS, una distribución sin soporte desde hace muchos años, dentro de la infraestructura virtualizada de la empresa.

## Qué se hizo

El software se reconstruyó en una nueva máquina virtual Ubuntu 24.04 LTS en la infraestructura Proxmox, con la aplicación y su base de datos en contenedores. En la misma máquina funcionan dos instancias independientes, una de producción y otra de pruebas, cada una con su propia base de datos, para que los cambios se prueben antes de tocar el archivo que consultan los usuarios. La migración la dirigió el IT Manager, con la contribución del equipo.

## Resultado

Los datos históricos se pueden consultar desde una instancia que funciona sobre un sistema operativo con soporte, con un entorno de pruebas separado del de producción. El trabajo sigue en curso: el servidor antiguo sigue encendido y su desmantelamiento está pendiente.
