---
type: concept
tags: [year3]
aliases: [VLAN, VLANs, V-LAN, Inter VLAN Routing, InterVLANRouting, routage inter-VLAN, lien trunk, trunk link, access link, switchport mode access, switchport mode trunk, VLAN 1, VLAN par défaut, IVR]
matieres: [Computer Network]
sources: ["[[4 - VLAN ／ IVR Commands|Chp4 - VLAN ／ IVR Commands]]"]
maj: 2026-11-07
---

Un VLAN divise le domaine de diffusion (broadcast) d'un switch en plusieurs domaines. Par défaut, tous les ports d'un switch Cisco sont dans le VLAN 1, VLAN par défaut qu'on ne peut pas supprimer.

- **Lien access** : associé à un seul VLAN. **Lien trunk** : transporte plusieurs VLAN.
- **Créer** : `vlan 10` puis `name ADMIN`.
- **Ports** : `interface range fastEthernet 0/1-5`, `switchport mode access`, `switchport access vlan 10`.
- **Trunk entre switchs** : `switchport mode trunk`, `switchport trunk allowed vlan add 10`.
- **Routage inter-VLAN (IVR)** : un routeur relié au switch par un trunk. Une sous-interface par VLAN, par exemple `interface gigabitEthernet 0/1.10`, avec `encapsulation dot1q 10` et l'adresse IP, qui sert de passerelle par défaut. L'interface physique doit être activée par `no shutdown`.

> [!warning] Écart dans le cours
> Dans l'exemple du cours, les trois sous-interfaces portent `encapsulation dot1q 10`. Les sous-interfaces `.20` et `.30` devraient porter 20 et 30 (complément).

Liens : [[Domaine de diffusion]], [[Sous-interface]], [[Encapsulation 802.1Q]], [[Commutateur]], [[CLI Cisco IOS]], [[Adressage IPv4 et CIDR]]

Résumés : [[4 - VLAN ／ IVR Commands]], [[3 - Dynamic Routing]]
