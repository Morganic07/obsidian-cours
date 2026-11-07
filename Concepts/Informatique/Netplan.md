---
type: concept
tags:
  - year2
aliases:
  - /etc/netplan
  - /etc/network/interfaces
  - static IP configuration
  - adresse IP statique
matieres:
  - Operating System
sources:
  - "[[3 - TP3|Cours TP3]]"
  - "[[Raw/Year 2/Operating System/DM/TP3/TP3-Commands  (2).pdf|TP3-Commands  (2).pdf]]"
maj: 2026-11-07
---

Outil de configuration réseau par défaut d'Ubuntu depuis la 18.04 : la configuration est écrite dans des fichiers [[YAML]] de `/etc/netplan` (par exemple `01-netcfg.yaml`), avec des exemples d'adresse statique et de [[DHCP]]. À défaut de Netplan, chercher `/etc/network/interfaces` (rendu du TP3 : `iface eth0 inet dhcp`).

Exemples du sujet (figures 3.1 et 3.2 de [[Raw/Year 2/Operating System/DM/TP3/TP3-Commands  (2).pdf|TP3-Commands  (2).pdf]], page 5) :

```yaml
# Figure 3.1 : adresse statique
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      dhcp4: no
      addresses:
        - 192.168.1.100/24
      gateway4: 192.168.1.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 8.8.4.4
```

```yaml
# Figure 3.2 : adresse obtenue par DHCP
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      dhcp4: yes
```

Le sujet légende aussi la figure 3.2 « Example Static IP Configuration », alors qu'elle montre la configuration dynamique.

Notion parente : [[Interface réseau]].

Résumés : [[3 - TP3]]
