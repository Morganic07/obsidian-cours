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
maj: 2026-11-07
---

Vecteur **non nul** $\mathbf{x}$ tel que $A\mathbf{x} = \lambda\mathbf{x}$ pour un scalaire $\lambda$. On le trouve en résolvant $(A - \lambda I)\mathbf{x} = \mathbf{0}$, ici par réduction par lignes.

- Des vecteurs propres associés à des valeurs propres distinctes sont linéairement indépendants.
- $A^n\mathbf{x} = \lambda^n\mathbf{x}$, par récurrence.
- Une combinaison non nulle de vecteurs propres d'une **même** valeur propre reste un vecteur propre de celle-ci. [[0 - Eigenvalues and eigenvectors|Chp 0e - Eigenvalues and eigenvectors]] l'énonce sans ces deux précisions.

> [!warning] Écart dans le cours
> [[7 - Algèbre linéaire|chp7]] définit les éléments propres d'une matrice avec un vecteur « nul ». Il faut lire « non nul », comme le dit le même chapitre plus haut.

En 1re année, la définition porte sur une application linéaire : $v$ est vecteur propre de $f$ associé à $\lambda$ si $f(v) = \lambda v$ et $v \neq 0$.

**En ACP** (Data analysis) : un vecteur propre de la matrice de covariance est une direction de composante principale (vecteur directeur de PC1, ou vecteur singulier). Voir [[Analyse en composantes principales]].

Notion parente : [[Valeur propre]]. Liens : [[Espace propre]], [[Diagonalisation]], [[Indépendance linéaire]], [[Analyse en composantes principales]]

## Erreurs du cours

- [[0 - Eigenvalues and eigenvectors|Chp 0e - Eigenvalues and eigenvectors]] écrit « every linear combination of basic eigenvectors is an eigenvector » ; il faut « every **non-zero** linear combination of basic eigenvectors **for the same eigenvalue** » : la combinaison nulle n'est pas un vecteur propre, et deux vecteurs propres de valeurs propres distinctes ne se combinent pas en vecteur propre.

Résumés : [[0 - Eigenvalues and eigenvectors]], [[7 - Algèbre linéaire|chp7]], [[13 - Principal Components Analysis]], [[13 - PCA in R]]
