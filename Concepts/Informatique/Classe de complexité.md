---
type: concept
tags:
  - year2
  - year4
aliases:
  - classes de complexité
  - complexité logarithmique
  - complexité linéaire
  - complexité quadratique
  - complexité polynomiale
  - complexité exponentielle
  - complexité constante
  - Ordre de grandeur de complexité
  - complexité quasi-linéaire
  - complexité cubique
  - complexité factorielle
sources:
  - "[[1 - récursivité et complexité|Chp1 - récursivité et complexité]]"
  - "[[3 - complexité|chp3 - complexité]]"
maj: 2026-11-08
---

Classement d'un algorithme selon l'ordre de grandeur de son coût $C(n)$.

**[[1 - récursivité et complexité|Chp1 - récursivité et complexité]]** : constante, logarithmique ($O(\ln n)$), linéaire, quadratique ($O(n^2)$), polynomiale de degré $p$ ($O(n^p)$), exponentielle s'il existe $a$ tel que $C(n)=O(a^n)$. Un graphique compare $a^n$, $n^3$, $n^2$, $n\log n$, $n$ et $\log n$.

**[[3 - complexité|chp3 - complexité]]** : constante, logarithmique, linéaire, quasi-linéaire, quadratique, cubique, exponentielle, factorielle. Exemples : `somme_1` (boucle `for i in range(n)`, qui calcule $0 + 1 + \dots + (n-1) = n(n-1)/2$) en $O(n)$, `somme_2` (formule $n(n+1)/2$) en $O(1)$ ; boucles `while` en $O(\min(m,n))$, $O(\max(m,n))$, $O(m+n)$ (linéaires) et $O(m \cdot n)$, qui n'est pas linéaire (quadratique si $m = n$). [[Erreurs du cours#^e-classe-de-complexite|✎]]

Notion parente : [[Complexité algorithmique]]. Voir aussi : [[Comparaison asymptotique]].

Résumés : [[1 - récursivité et complexité]], [[3 - complexité]]
