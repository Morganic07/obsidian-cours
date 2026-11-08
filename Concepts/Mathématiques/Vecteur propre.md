---
type: concept
tags:
  - year1
  - year2
  - year3
aliases:
  - eigenvector
  - eigenvectors
  - vecteurs propres
sources:
  - "[[0 - Eigenvalues and eigenvectors|Chp 0e - Eigenvalues and eigenvectors]]"
  - "[[7 - Algèbre linéaire|chp7 (Algèbre)]]"
  - "[[13 - Principal Components Analysis|Cours 13 - Principal Components Analysis]]"
maj: 2026-11-08
---

Vecteur **non nul** $\mathbf{x}$ tel que $A\mathbf{x} = \lambda\mathbf{x}$ pour un scalaire $\lambda$. On le trouve en résolvant $(A - \lambda I)\mathbf{x} = \mathbf{0}$, ici par réduction par lignes.

- Des vecteurs propres associés à des valeurs propres distinctes sont linéairement indépendants.
- $A^n\mathbf{x} = \lambda^n\mathbf{x}$, par récurrence.
- Une combinaison non nulle de vecteurs propres d'une **même** valeur propre reste un vecteur propre de celle-ci ([[0 - Eigenvalues and eigenvectors|Chp 0e - Eigenvalues and eigenvectors]]) ; deux vecteurs propres de valeurs propres distinctes, eux, ne se combinent pas en vecteur propre. [[Erreurs du cours#^e-vecteur-propre|✎]]

En 1re année, la définition porte sur une application linéaire : $v$ est vecteur propre de $f$ associé à $\lambda$ si $f(v) = \lambda v$ et $v \neq 0$ ; pour une matrice, de même, $AX = \lambda X$ avec $X$ **non nul** ([[7 - Algèbre linéaire|chp7]]). [[Erreurs du cours#^e-vecteur-propre|✎]]

**En ACP** (Data analysis) : un vecteur propre de la matrice de covariance est une direction de composante principale (vecteur directeur de PC1, ou vecteur singulier). Voir [[Analyse en composantes principales]].

Notion parente : [[Valeur propre]]. Liens : [[Espace propre]], [[Diagonalisation]], [[Indépendance linéaire]], [[Analyse en composantes principales]]


Résumés : [[0 - Eigenvalues and eigenvectors]], [[7 - Algèbre linéaire|chp7]], [[13 - Principal Components Analysis]], [[13 - PCA in R]]
