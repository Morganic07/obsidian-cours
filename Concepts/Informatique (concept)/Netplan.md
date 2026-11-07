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
  - "[[3 - TP3 (résumé)|Cours TP3]]"
  - "[[Raw/Year 2/Operating System/DM/TP3/TP3-Commands  (2).pdf|TP3-Commands  (2).pdf]]"
maj: 2026-11-06
---

Outil de configuration réseau par défaut d'Ubuntu depuis la 18.04 : la configuration est écrite dans des fichiers [[YAML]] de `/etc/netplan` (par exemple `01-netcfg.yaml`), avec des exemples d'adresse statique et de [[DHCP]]. À défaut de Netplan, chercher `/etc/network/interfaces` (rendu du TP3 : `iface eth0 inet dhcp`).

Notion parente : [[Interface réseau]].

## À vérifier

- Les figures d'exemple de configuration statique et DHCP du sujet sont des images non lues.

Résumés : [[3 - TP3 (résumé)]], [[TP3-Commands (2) (résumé)]], [[TP3 (résumé)]]
