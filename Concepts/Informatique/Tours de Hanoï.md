---
type: concept
tags:
  - year1
  - year4
aliases:
  - Hanoï
  - tours de Hanoi
  - Tower of Hanoi
matieres:
  - Algo Maths
  - graph theory
sources:
  - "[[0 - Algo Maths|Cours 1 (Algo Maths)]]"
  - "[[3 - complexité|chp3 - complexité]]"
  - "[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"
maj: 2026-11-07
---

Problème : déplacer $n$ disques d'un pilier à un autre, avec un nombre minimal de coups. Algorithme **récursif** : déplacer les $n - 1$ disques du dessus sur le pilier intermédiaire, déplacer le grand disque, replacer les $n - 1$ disques dessus.

Nombre de coups : $f(0) = 0$, $f(n+1) = 2f(n) + 1$, donc $f(n) = 2^n - 1$, démontré par [[Récurrence]] dans [[0 - Algo Maths|Cours 1 (Algo Maths)]]. Le pseudo-code de 1re année s'écrit `Déplacer(n, de, à, par)`. Le cours de graphes retrouve $T(n) = 2T(n-1) + 1$, $T(1) = 1$, d'où $T(n) = \sum_{k=0}^{n-1} 2^k = 2^n - 1$ et $\Theta(2^n)$ : voir [[Complexité algorithmique]] et [[Calcul de complexité et théorème de résolution]].

Notion parente : [[Récursivité]].

## Erreurs du cours

- [[3 - complexité|chp3 - complexité]] écrit « Si $n > 0$ […] $T(n) = 2T(n-1) + 1$ » ; il faut « si $n > 1$ », puisque le cas de base est $T(1) = 1$. La résolution se poursuit sur l'image suivante jusqu'à $T(n) = \sum_{0}^{n-1} 2^k = \Theta(2^n)$.

Résumés : [[0 - Algo Maths|Cours 1 (Algo Maths)]], [[3 - complexité]], [[0 - diapo prof]]
