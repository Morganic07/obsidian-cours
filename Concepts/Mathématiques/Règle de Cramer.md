---
type: concept
tags:
  - year2
aliases:
  - Cramer's rule
  - Cramer’s Rule
  - formules de Cramer
  - Cramer
matieres:
  - Bilinear Algebra
sources:
  - "[[0 - Determinants|Chp 0c - Determinants]]"
maj: 2026-11-07
---

Soit $A$ une matrice $n \times n$ inversible. Pour tout $\mathbf{b} \in \mathbb{R}^n$, l'unique solution du système $A\mathbf{x}=\mathbf{b}$ a pour coordonnées ($i = 1, \dots, n$) :
$$x_i=\frac{\det A_i(\mathbf{b})}{\det A},$$
où $A_i(\mathbf{b})$ est la matrice $A$ dont la colonne $i$ est remplacée par $\mathbf{b}$. Le cours la dit efficace en tailles 2 et 3.

Notion parente : [[Déterminant]]. Voir aussi : [[Système linéaire]].

Résumés : [[0 - Determinants]]
