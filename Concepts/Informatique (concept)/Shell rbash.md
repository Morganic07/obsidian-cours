---
type: concept
tags: [year2]
aliases: [rbash, restricted bash]
matieres: [Operating System]
sources: ["[[OS - chp 5 (résumé)|OS - chp 5]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : rbash (*restricted bash*) est Bash lancé en mode restreint (équivalent de `bash -r`), destiné à limiter ce qu'un utilisateur peut faire. Il interdit notamment de changer de répertoire avec `cd`, de modifier les variables `PATH` et `SHELL`, de lancer une commande dont le nom contient `/` et de rediriger la sortie vers un fichier. Ce n'est pas une protection complète : un programme autorisé qui ouvre lui-même un shell permet d'en sortir.

## Dans le cours

Nommé sans définition : rbash est cité parmi les shells, et `/bin/rbash` figure dans `/etc/shells`.

Notion parente : [[Shell et Bash]].

## À vérifier

- Le développé « restricted bash » n'est pas dans le cours.

Résumés : [[OS - chp 5 (résumé)]], [[DM Shell Scripting (résumé)]]
