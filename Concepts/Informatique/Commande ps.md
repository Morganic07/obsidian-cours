---
type: concept
tags: [year2]
aliases: [ps, ps aux, ps -ef, process status]
matieres: [Operating System]
sources: ["[[Raw/Year 2/Operating System/Cours OS/OS - chp7.docx|OS - chp7]]", "[[Raw/Year 2/Operating System/Cours OS/Commandes Shell + explications.docx|Commandes Shell + explications]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : `ps` (*process status*) affiche les [[Processus|processus]] en cours d'exécution. Sans option, il ne montre que ceux du terminal courant ; les deux formes usuelles listent tout le système :

- `ps aux` : tous les processus, avec l'utilisateur, le PID, `%CPU`, `%MEM`, l'état (`STAT`) et la commande ;
- `ps -ef` : tous les processus, avec en plus le `PPID`, PID du processus parent ([[Identifiant de processus]]).

Commandes voisines : `top` (ou `htop`) affiche la même information en continu, triée par consommation ; `pstree -p` affiche l'arbre des processus avec leurs PID.

**Colonne `STAT`** ([[États d'un processus]]) :

| Lettre | État |
|---|---|
| `R` | en exécution ou prêt (*running* / *runnable*) |
| `S` | endormi, attend un événement |
| `D` | attente non interruptible, souvent une E/S disque |
| `T` | stoppé, par exemple par Ctrl+Z |
| `Z` | zombie, affiché `<defunct>` ([[Processus zombie et orphelin]]) |

À distinguer de [[Commande jobs|jobs]], qui ne montre que les tâches lancées depuis le shell courant. Le PID lu dans `ps` sert ensuite à [[Commande kill|kill]].

## Dans le cours

Le cours ne présente pas la commande. Elle apparaît dans les compléments de [[7 - OS]] (liste des processus, lettres de `STAT`, `ps -ef` pour le PPID) et de [[8 - OS commandes sh]] (pour voir les processus que `jobs` ne montre pas).

Voir aussi : [[Processus]], [[États d'un processus]], [[Identifiant de processus]], [[Commande jobs]], [[Commande kill]], [[Processus zombie et orphelin]].

Résumés : [[7 - OS]], [[8 - OS commandes sh]]
