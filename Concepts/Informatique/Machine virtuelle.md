---
type: concept
tags: [year2]
aliases: [virtual machine, virtual machines, VMM, virtual machine manager, hyperviseur, VirtualBox, KVM, bare metal, hosted hypervisor, Kernel Virtual Machine]
matieres: [Operating System]
sources: ["[[OS - chp 1]]", "[[OS - chp 3]]"]
maj: 2026-11-06
---

Un gestionnaire de machines virtuelles (VMM) permet de créer plusieurs PC virtuels sur un même matériel. Chaque machine virtuelle a son propre [[Noyau]] et ses propres processus. Deux types :
- **bare metal** : le VMM s'installe directement sur le matériel, sans système hôte ;
- **hosted** : le VMM s'installe sur une machine qui a déjà un système (exemple : VirtualBox).

Le *cloud computing* (stockage, calcul, applications fournis par le réseau ; exemples : Shadow, Amazon EC2) est présenté comme une extension logique de la virtualisation ([[Cloud computing]]).

**Installer un système en machine virtuelle** (chapitre 3) : choisir le logiciel selon l'hôte, VirtualBox sur Windows ou KVM (Kernel Virtual Machine) sur Ubuntu, créer la machine, obtenir l'[[Image ISO]] et installer. Contrairement à une installation sur PC, la clé USB amorçable n'est pas nécessaire.

Notion parente : [[Environnement informatique]]. Voir aussi : [[Système d'exploitation]], [[Distribution Linux]], [[Noyau]].

Résumés : [[OS - chp 1 (résumé)]], [[OS - chp 3 (résumé)]]
