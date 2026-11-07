---
type: concept
tags:
  - year1
  - year2
aliases:
  - factorielles
  - factorial
matieres:
  - Analyse Maths
  - Algo Maths
  - Operating System
  - Algo
  - Probability
sources:
  - "[[Raw/Year 1/Analyse Maths/Cours/Chap0-Rappels-etc.pdf|Chap0-Rappels-etc.pdf]]"
  - "[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"
  - "[[Raw/Year 1/Algo Maths/explications DM d'algo .docx|explications DM d'algo]]"
  - "[[Raw/Year 2/Operating System/DM/DMs/Copy of 08 Processes-TP.docx|Copy of 08 Processes-TP]]"
  - "[[1 - récursivité et complexité (résumé)|Chp1 - récursivité et complexité]]"
  - "[[3 - Combinatorics (résumé)|Chp 3 - Combinatorics]]"
maj: 2026-11-06
---

$n! = n \times (n-1)!$ avec $0! = 1$.

**Analyse Maths** : introduite au chapitre 0 avec le coefficient binomial ; en TD, $\prod k^2 = (n!)^2$.

**Algorithmique** (Algo Maths, Algo) : exemple type de fonction récursive, en version non terminale, terminale (`factRT(n, acc)`) et itérative, de complexité $O(n)$. Le DM du sac à dos rappelle que $n!$ compte des permutations, pas des configurations d'inclusion.

**Probability** : $n!$ compte les permutations de $n$ objets distincts.

**Operating System** : au lab 7, le processus fils calcule une factorielle, puis le parent affiche les nombres premiers jusqu'à une borne (simple exemple, sans définition).

Voir aussi : [[Dénombrement]], [[Récursivité]], [[Récursivité terminale]], [[Création et terminaison de processus]], [[Permutation (dénombrement)]].

## À vérifier

- AlgoID1 : le cas d'arrêt de la factorielle récursive est $n = 1$, donc `fact(0)` ne se termine pas (le cours suppose $n \ge 1$).

Résumés : [[0 - Rappels-etc (résumé)]], [[0 - diapo prof (résumé)]], [[1 - récursivité et complexité (résumé)]], [[3 - Combinatorics (résumé)]]
