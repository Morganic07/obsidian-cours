---
type: concept
tags:
  - year2
aliases:
  - file path
  - chemin d'accès
  - répertoire courant
  - répertoire parent
  - current directory
  - parent directory
  - chemin absolu
  - chemin relatif
  - absolute path
  - relative path
sources:
  - "[[Raw/Year 2/Operating System/DM/TP2/Copy of TP2-Commands.pdf|Copy of TP2-Commands.pdf]]"
  - "[[2 - TP2|Cours TP2]]"
  - "[[1 - TP1|cours TP1]]"
  - "[[Raw/Year 2/Operating System/Cours OS/Cours TP4.docx|Cours TP4]]"
maj: 2026-11-08
---

Dans un chemin, `/` sépare les répertoires (`cd /home/user`), `~` représente le [[Répertoire personnel]], `.` le répertoire courant (`./script.sh`) et `..` le répertoire parent (`cd ..`).

## Chemin absolu et chemin relatif (complément, hors du cours)

- Un **chemin absolu** commence par `/` (le [[Répertoire racine]]) et désigne le même fichier depuis n'importe quel répertoire : `/home/user/data/time.txt`.
- Un **chemin relatif** ne commence pas par `/` : il est résolu à partir du répertoire de travail du processus (celui qu'affiche [[Commande pwd|pwd]]) : `time.txt`, `data/time.txt`, `../backup`.

Un même chemin relatif désigne donc des fichiers différents selon le répertoire d'où l'on lance le programme. Dans le TP4, le parent écrit dans `"time.txt"` (relatif) alors que le fils copie un chemin absolu : les deux ne désignent le même fichier que si le programme est lancé depuis le bon dossier. Les [[Tâche planifiée cron|tâches cron]], qui ne s'exécutent pas depuis un répertoire choisi par l'utilisateur, doivent utiliser des chemins absolus.

Notion parente : [[Méta-caractère]]. Voir aussi : [[Commande cd]], [[Commande pwd]], [[Répertoire personnel]], [[Répertoire racine]], [[Arborescence des répertoires Linux]].

Résumés : [[2 - TP2]], [[4 - TP4]], [[4 - OS]]
