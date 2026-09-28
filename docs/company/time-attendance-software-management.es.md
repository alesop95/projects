# Migración del software de control de presencia

**Sector**: empresa de servicios lingüísticos y traducción profesional

**Periodo**: 02/2025, concluido

**Rol**: IT Manager, administrador de sistemas

**Tecnologías**: Windows Server 2012 → Windows Server 2022, VMware vSphere → Proxmox VE, IIS, MariaDB, lectores biométricos de red, diagnóstico de red entre VLAN

## Contexto

El sistema de control de presencia y de accesos, dos lectores biométricos con su software de gestión en una máquina virtual Windows Server 2012, tenía que salir del antiguo host de virtualización, que se estaba sustituyendo por un nuevo servidor con Proxmox. Ese mismo mes el lector de entrada dejó de sincronizar los fichajes, mientras que el de salida, conectado al primero por una línea serie RS-485 en configuración maestro y esclavo, seguía funcionando.

## Qué se hizo

El trabajo, desde el software y su configuración hasta la red y la migración de la máquina virtual y de los servicios, lo realizó el IT Manager; quedan fuera la actualización del firmware del nuevo lector, gestionada aparte, y el montaje en la pared, que hizo el electricista. El diagnóstico del lector descartó cables y switches y mostró un síntoma de segmentación: las respuestas llegaban desde la puerta de enlace de otra VLAN y no desde el dispositivo, porque el puesto de pruebas estaba en una red distinta de la del lector, sin enrutamiento entre ambas. Un restablecimiento de la configuración de red lo devolvió al funcionamiento durante un día; después la avería volvió de una forma que no se podía resolver por software y el lector se sustituyó por un equipo nuevo. Al trasladar directamente la máquina virtual al nuevo hipervisor, esta quedaba atrapada en un ciclo de reinicios, así que los servicios, es decir, la aplicación web en IIS y las bases de datos en MariaDB, se migraron a una nueva máquina Windows Server 2022 en lugar de recuperar la antigua.

## Resultado

El control de presencia y de accesos funciona en Windows Server 2022 sobre la nueva infraestructura virtualizada, y el antiguo host se ha retirado del inventario. La migración se completó antes de que terminara febrero de 2025.
