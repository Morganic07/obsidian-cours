---
type: concept
tags: [year2]
aliases: [Linux partitions, root partition, home partition, "partition /home", "partition /usr", "partition /var"]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4.pdf]]", "[[3 - OS|OS - chp 3]]"]
maj: 2026-11-07
---

Partitions d'un système Linux selon le cours :

- **racine `/`** : noyau, programmes de base, configuration, bibliothèques ; créée en premier, montée en lecture-écriture ([[Répertoire racine]]) ;
- **`/home`** : données des utilisateurs, séparée pour que les mises à jour n'y touchent pas et pour la sécurité ([[Répertoire personnel]]) ;
- **`/usr`** : logiciels tiers ;
- **`/var`** : données qui changent souvent ;
- **`/boot`** et partition amorçable ([[Partition de démarrage]]) ;
- **swap** ([[Espace d'échange (swap)]]).

Les partitions séparent système et données, améliorent la sécurité et simplifient les mises à jour.

Notion parente : [[Système de fichiers]]. Voir aussi : [[Partition (disque)]].

Résumés : [[4 - OS]], [[3 - OS]]
