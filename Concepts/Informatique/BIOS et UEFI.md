---
type: concept
tags: [year2]
aliases: [BIOS, UEFI, Basic Input Output System, Unified Extensible Firmware Interface, POST, power-on self-test, bootstrap program, firmware]
matieres: [Operating System]
sources: ["[[1 - OS|OS - chp 1]]", "[[2 - OS|OS - chp 2]]"]
maj: 2026-11-07
---

Le programme d'amorçage (*bootstrap program*, *firmware* : BIOS ou UEFI) est le premier programme lancé au démarrage. Le BIOS est stocké en [[Mémoire morte|mémoire morte]] (ROM) sur une puce de la carte mère. Étapes du BIOS : **POST** (test de l'alimentation, de la RAM et du matériel), puis localisation du système sur le disque et chargement en RAM.

Le système est trouvé grâce au [[MBR]] (*master boot record*), situé sur le disque, qui indique sur quelle partition il se trouve.

**UEFI** : successeur plus récent du BIOS, avec une interface graphique, un démarrage plus rapide et plus sûr ([[Démarrage sécurisé]]), des disques plus grands, le réseau et l'administration à distance. Voir aussi [[Partition système EFI]].

| | BIOS | UEFI |
|---|---|---|
| Taille maximale du disque | 2,2 To | 9,4 Zo |
| Démarrage | lent | rapide |
| Options de démarrage sécurisé | limitées | étendues |
| Réseau, administration à distance | non | oui |
| Interface graphique | non | oui |

Liens : [[MBR]], [[Mémoire morte]], [[Démarrage sécurisé]], [[Partition système EFI]], [[Système de fichiers]], [[Interruption]]

Résumé : [[2 - OS]], [[1 - OS]]
