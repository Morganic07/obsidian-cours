---
type: concept
tags: [year2]
aliases: [virtual machine, virtual machines, VMM, virtual machine manager, hyperviseur, VirtualBox, KVM, bare metal, hosted hypervisor, Kernel Virtual Machine, Kernel-based Virtual Machine, hyperviseur de type 1, hyperviseur de type 2, VT-x, AMD-V]
matieres: [Operating System]
sources: ["[[1 - OS|OS - chp 1]]", "[[3 - OS|OS - chp 3]]", "[[Raw/Year 2/Operating System/Cours OS/OS - chp 1.docx|OS - chp 1]]", "[[Raw/Year 2/Operating System/Cours OS/OS - chp 3.docx|OS - chp 3]]"]
maj: 2026-11-08
---

**Définition** (d'après [[1 - OS]]) : un gestionnaire de machines virtuelles (VMM) permet de créer plusieurs PC virtuels sur un même matériel. Chaque machine virtuelle a son propre [[Noyau]] et ses propres processus. Deux types :
- **bare metal** : le VMM s'installe directement sur le matériel, sans système hôte ;
- **hosted** : le VMM s'installe sur une machine qui a déjà un système (exemple : VirtualBox).

Le *cloud computing* (stockage, calcul, applications fournis par le réseau ; exemples : Shadow, Amazon EC2) est présenté comme une extension logique de la virtualisation ([[Cloud computing]]).

**Installer un système en machine virtuelle** (chapitre 3) : choisir le logiciel selon l'hôte, VirtualBox sur Windows ou KVM (Kernel Virtual Machine) sur Ubuntu, créer la machine, obtenir l'[[Image ISO]] et installer. Contrairement à une installation sur PC, la clé USB amorçable n'est pas nécessaire.

## Complément (hors du cours)

**Types d'hyperviseurs.** Le VMM s'appelle aussi **hyperviseur**.

| | Type 1 (*bare metal*) | Type 2 (*hosted*) |
|---|---|---|
| Installation | directement sur le matériel | comme une application sur un OS hôte |
| Exemples | VMware ESXi, Microsoft Hyper-V, Xen, KVM | VirtualBox, VMware Workstation |
| Usage | serveurs, centres de données, cloud | poste personnel, tester un autre système |
| Atout | plus performant, sans OS intermédiaire | plus simple à installer |

**KVM.** Son nom officiel est *Kernel-based Virtual Machine*. C'est un module du noyau Linux qui transforme Linux lui-même en hyperviseur de type 1. Sous Ubuntu, il s'utilise avec QEMU (qui émule les périphériques de la machine virtuelle) et une interface comme virt-manager.

**Support du processeur.** Les processeurs actuels ont des instructions dédiées à la virtualisation, Intel VT-x et AMD-V, qu'il faut souvent activer dans le micrologiciel ([[BIOS et UEFI]]) pour que l'hyperviseur fonctionne bien.

**Disque virtuel.** Le disque d'une machine virtuelle est un simple fichier sur le disque de l'hôte : `.vdi` pour VirtualBox, `.qcow2` pour KVM/QEMU (aussi `.vmdk` pour VMware). On peut le copier, le sauvegarder ou en prendre des instantanés (*snapshots*).

**Différence avec un conteneur.** Un [[Conteneur (informatique)|conteneur]] (Docker, par exemple) isole une application et ses dépendances mais **partage le noyau** de l'hôte, au lieu d'embarquer un OS complet : il démarre en quelques secondes et prend peu de place, mais ne peut faire tourner qu'un système compatible avec le noyau de l'hôte.

## Dans le cours

Le cours présente les deux types de VMM (chapitre 1) et l'installation dans VirtualBox ou KVM (chapitre 3) ; les noms de type 1 et 2, VT-x, AMD-V et les conteneurs sont des compléments de [[1 - OS]] et [[3 - OS]].

Notion parente : [[Environnement informatique]]. Voir aussi : [[Système d'exploitation]], [[Distribution Linux]], [[Noyau]], [[Cloud computing]], [[Clé USB amorçable]].

Résumés : [[1 - OS]], [[3 - OS]]
