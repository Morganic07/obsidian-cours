---
type: concept
tags: [year2]
aliases: [Linux partitions, root partition, home partition, "partition /home", "partition /usr", "partition /var"]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp 4.pdf|OS - chp 4.pdf]]", "[[OS - chp 3 (résumé)|OS - chp 3]]"]
maj: 2026-11-06
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

## À vérifier

- La description de `/usr` « pour logiciels tiers » est contestée par le résumé.

Résumés : [[OS - chp 4 (résumé)]], [[OS - chp 3 (résumé)]]
