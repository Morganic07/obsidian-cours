---
type: concept
tags: [year2]
aliases: [tree of processes, process tree]
sources: ["[[OS - chp7]]", "[[Copy of 08 Processes-TP]]"]
maj: 2026-11-06
---

Les processus parents créent des enfants, qui en créent d'autres à leur tour. Exemple du cours : A crée B et C ; B crée D, E et F ; C crée G ; D crée H ; H crée I.

Lab 5 : arbre A, B, C, D, E, F, K, L (puis M), construit par des `fork()` imbriqués ; chaque processus finit par `exit(0)` et le parent attend avec `waitpid`.

Notion parente : [[Création et terminaison de processus]]. Voir aussi : [[Appel fork()]].

## À vérifier

Lab 5 : `exit(0)` de F mal placé selon la transcription (image non rouverte).

Résumés : [[OS - chp7 (résumé)]], [[Copy of 08 Processes-TP (résumé)]]
