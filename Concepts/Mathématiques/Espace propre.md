---
type: concept
tags:
  - year1
  - year2
aliases:
  - eigenspace
  - eigenspaces
  - espaces propres
  - sous-espace propre
sources:
  - "[[0 - Eigenvalues and eigenvectors|Chp 0e - Eigenvalues and eigenvectors]]"
  - "[[2 - Symmetric matrices and quadratic forms|Chp2 - Symmetric matrices and quadratic forms]]"
  - "[[7 - Algèbre linéaire|chp7 (Algèbre)]]"
maj: 2026-11-06
---

L'espace propre de $A$ associé à $\lambda$ est l'ensemble des solutions de $(A - \lambda I)\mathbf{x} = \mathbf{0}$, soit Nul$(A - \lambda I)$. C'est un sous-espace de $\mathbb{R}^n$, formé du vecteur nul et de tous les vecteurs propres associés à $\lambda$.

- Sa dimension est inférieure ou égale à la [[Multiplicité d'une valeur propre|multiplicité]] de $\lambda$.
- $A$ est diagonalisable si et seulement si la somme des dimensions des espaces propres vaut $n$.
- Pour une matrice symétrique, chaque dimension égale la multiplicité, et les espaces propres sont orthogonaux entre eux.
- Pour un endomorphisme $f$ (chp7 d'Algèbre linéaire, « sous-espace propre »), on note $E_\lambda = \{x \in E \mid f(x) = \lambda x\} = \text{Ker}(f - \lambda \text{Id})$. $\lambda$ est valeur propre si et seulement si $E_\lambda \neq \{0\}$. Les espaces propres de valeurs propres distinctes sont en [[Somme directe]].

Notion parente : [[Valeur propre]]. Voir aussi : [[Vecteur propre]], [[Multiplicité d'une valeur propre]], [[Espace nul]], [[Diagonalisation]], [[Matrice symétrique]], [[Somme directe]]

Résumés : [[0 - Eigenvalues and eigenvectors]], [[2 - Symmetric matrices and quadratic forms]], [[7 - Algèbre linéaire|chp7]]
