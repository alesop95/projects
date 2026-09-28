# Time and attendance software migration

**Sector**: language services and professional translation company

**Period**: 02/2025, completed

**Role**: IT Manager, systems administrator

**Technologies**: Windows Server 2012 → Windows Server 2022, VMware vSphere → Proxmox VE, IIS, MariaDB, networked biometric readers, network diagnosis across VLANs

## Context

The time and attendance and access control system, two biometric readers with their management software on a Windows Server 2012 virtual machine, had to leave the old virtualization host, which was being replaced by a new server running Proxmox. In the same month the entrance reader stopped synchronizing clock-ins, while the exit reader, connected to the first one over an RS-485 serial line in a master and slave configuration, kept working.

## What was done

The work, from the software and its configuration to the network and the migration of the virtual machine and its services, was carried out by the IT Manager; the only exceptions are the firmware update of the new reader, handled separately, and the wall mounting, done by the electrician. The diagnosis of the reader ruled out cables and switches and showed a segmentation symptom: replies came from the gateway of another VLAN rather than from the device, because the test workstation sat on a different network from the reader, with no routing between the two. Resetting the network settings brought it back for a day; the fault then returned in a form that could not be fixed in software, and the reader was replaced with a new unit. Moving the virtual machine directly onto the new hypervisor left it stuck in a reboot loop, so the services, that is the web application on IIS and the databases on MariaDB, were migrated to a new Windows Server 2022 machine instead of recovering the old one.

## Result

Time and attendance and access control run on Windows Server 2022 on the new virtualized infrastructure, and the old host has been removed from the inventory. The migration was completed by the end of February 2025.
