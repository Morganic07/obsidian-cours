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
  - "[[chp 1 - récursivité et complexité (résumé)|Chp1 - récursivité et complexité]]"
  - "[[chp 3 - complexité (résumé)|chp3 - complexité]]"
maj: 2026-11-06
---

Classement d'un algorithme selon l'ordre de grandeur de son coût $C(n)$.

**[[chp 1 - récursivité et complexité (résumé)|Chp1 - récursivité et complexité]]** : constante, logarithmique ($O(\ln n)$), linéaire, quadratique ($O(n^2)$), polynomiale de degré $p$ ($O(n^p)$), exponentielle s'il existe $a$ tel que $C(n)=O(a^n)$. Un graphique compare $a^n$, $n^3$, $n^2$, $n\log n$, $n$ et $\log n$.

**[[chp 3 - complexité (résumé)|chp3 - complexité]]** : constante, logarithmique, linéaire, quasi-linéaire, quadratique, cubique, exponentielle, factorielle. Exemples : `somme_1` (boucle) en $O(n)$, `somme_2` (formule) en $O(1)$ ; boucles `while` en $O(\min(m,n))$, $O(\max(m,n))$, $O(m+n)$, $O(m \cdot n)$.

Notion parente : [[Complexité algorithmique]]. Voir aussi : [[Comparaison asymptotique]].

## À vérifier

- En informatique théorique, « classe de complexité » désigne autre chose (P, NP) : le titre suit l'usage du cours.
- Dans [[chp 3 - complexité (résumé)|chp3 - complexité]], l'algorithme D en $O(m \cdot n)$ est noté « linéaire » (il est quadratique si $m = n$) : à corriger avant un examen.
- `somme_1` et `somme_2` ne calculent pas la même somme (relevé du résumé).

Résumés : [[chp 1 - récursivité et complexité (résumé)]], [[chp 3 - complexité (résumé)]]
