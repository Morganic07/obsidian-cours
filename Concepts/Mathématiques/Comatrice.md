---
type: concept
tags:
  - year2
aliases:
  - cofactor
  - cofactors
  - cofacteur
  - cofacteurs
  - matrice des cofacteurs
  - adjugate
  - adjugate matrix
  - adj A
  - développement par cofacteurs
  - cofactor expansion
matieres:
  - Bilinear Algebra
sources:
  - "[[0 - Determinants|Chp 0c - Determinants]]"
maj: 2026-11-08
---

Le [[Déterminant]] se développe selon la première ligne avec les cofacteurs $(-1)^{1+j}\det A_{1j}$. La matrice adjointe (adjugate) $\text{adj}\,A$ est la [[Transposée|transposée]] de la matrice des cofacteurs : $C_{12}$ va en position $(2,1)$. Elle donne la formule de l'inverse d'une [[Matrice inversible|matrice inversible]] :

$$A^{-1}=\frac{1}{\det A}\,\text{adj}\,A.$$

Le cours en conclut la relation $(\det A)\,I = (\text{adj}\,A)A$ (le membre de droite est une matrice, d'où l'identité $I$ à gauche). [[Erreurs du cours#^e-comatrice|✎]]

Notion parente : [[Déterminant]].

Résumés : [[0 - Determinants]]
