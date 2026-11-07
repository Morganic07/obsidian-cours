---
type: concept
tags: [year2]
aliases: [Network File System]
matieres: [Operating System]
sources: ["[[2 - OS|OS - chp 2]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : NFS (Network File System) est un protocole de partage de fichiers en réseau, conçu à l'origine par Sun Microsystems, surtout utilisé entre systèmes Unix et Linux. Un serveur NFS exporte des répertoires, que les clients montent dans leur propre arborescence (voir [[Point de montage]]) et utilisent comme s'ils étaient locaux. C'est donc un système de fichiers distant, qui s'appuie côté serveur sur un système de fichiers local comme [[EXT4]] ; le cours le range pourtant avec les systèmes de fichiers locaux.

## Dans le cours

Nommé dans le chapitre 2 sans définition : le cours le classe parmi les systèmes de fichiers Linux, avec jusqu'à 8 exaoctets, sans chiffrement ni compression, compatible Linux et macOS.

Notion parente : [[Système de fichiers]]. Voir aussi : [[EXT4]].

Résumés : [[2 - OS]]
