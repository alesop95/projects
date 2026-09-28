# Software license migration and lifecycle management

**Sector**: language services and professional translation company

**Period**: 01/2025 - 03/2025

**Role**: IT Manager, migration lead and systems administrator

**Technologies**: Windows Server 2012 R2 → Windows Server 2022, Proxmox VE, concurrent-use network license managers, administrative installation from a network share

## Context

An optical character recognition (OCR) tool and a computer-assisted translation (CAT) tool use network licenses, handed out to the workstations by a license manager on a server. The OCR license manager ran on a Windows Server 2012 R2 virtual machine hosted on the old virtualization host, which at the beginning of 2025 was being replaced by a new server running Proxmox: the license manager therefore had to move to a new Windows Server 2022 without leaving the workstations without a license.

## What was done

The work was planned and led by the IT Manager, who decided the order of the steps, the checks and the choices on the license perimeter, with help from a colleague present only in the mornings; the vendor steps in only when the license supply changes. The OCR licenses are perpetual but have no maintenance contract, so the vendor's support was limited to activations and installation packages. The first package that could be downloaded directly installed a license manager of a later version, incompatible with the licenses owned, and was discarded in favour of the package for the correct version; the version of the OCR tool stayed the same. Offline activation did not succeed, and copying the license folders by hand from the old server proved useless, because the configuration does not live in files that can be copied: the new license manager was activated online. At that point the old and the new manager exposed the same serial number, and actual concurrency would have exceeded the number of licenses purchased; the decision was therefore to reinstall the workstations quickly and decommission the old manager. For the reinstallation an administrative installation point was set up on the new server and shared on the network, and a setup error caused by leftover data from the old installation was solved by removing its folders before running the setup again.

## Result

The OCR license manager runs on Windows Server 2022 on the new infrastructure, with the same version of the tool and the first reinstalled workstation correctly reading its license from the new server. The CAT tool licenses remain network licenses, served by a server and distributed across about eighteen workstations.
