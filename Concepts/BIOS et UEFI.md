---
type: concept
aliases: [BIOS, UEFI, MBR, master boot record, POST, power-on self-test, bootstrap program, firmware]
matieres: [Operating System]
sources: ["[[OS - chp 1]]", "[[OS - chp 2]]"]
maj: 2026-11-05
---

Le *firmware* (BIOS ou UEFI) est le premier programme lancé au démarrage. Il est stocké en mémoire morte sur la carte mère. Étapes du BIOS : **POST** (test de l'alimentation, de la RAM et du matériel), puis localisation du système sur le disque et chargement en RAM.

**MBR** (*master boot record*) : situé sur le disque, il indique sur quelle partition se trouve le système et gère les partitions. Image du cours : le MBR est la table des matières, les partitions sont les chapitres, le système est le texte. S'il est corrompu, l'ordinateur ne trouve plus le système. Il n'y en a qu'un même avec plusieurs systèmes installés, indépendant de ceux-ci.

**UEFI** : successeur plus récent du BIOS.

| | BIOS | UEFI |
|---|---|---|
| Taille maximale du disque | 2,2 To | 9,4 Zo |
| Démarrage | lent | rapide |
| Options de démarrage sécurisé | limitées | étendues |
| Réseau, administration à distance | non | oui |
| Interface graphique | non | oui |

Liens : [[Système de fichiers]], [[Interruption]]

Résumé : [[OS - chp 2 (résumé)]], [[OS - chp 1 (résumé)]]
