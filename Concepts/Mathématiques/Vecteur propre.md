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
  - "[[Chp 0e - Eigenvalues and eigenvectors]]"
  - "[[chp7|chp7 (Algèbre)]]"
  - "[[Cours 13 - Principal Components Analysis]]"
maj: 2026-11-06
---

Vecteur **non nul** $\mathbf{x}$ tel que $A\mathbf{x} = \lambda\mathbf{x}$ pour un scalaire $\lambda$. On le trouve en résolvant $(A - \lambda I)\mathbf{x} = \mathbf{0}$, ici par réduction par lignes.

- Des vecteurs propres associés à des valeurs propres distinctes sont linéairement indépendants.
- $A^n\mathbf{x} = \lambda^n\mathbf{x}$, par récurrence.
- Une combinaison non nulle de vecteurs propres d'une **même** valeur propre reste un vecteur propre de celle-ci. [[Chp 0e - Eigenvalues and eigenvectors]] l'énonce sans ces deux précisions.

> [!warning] Écart dans le cours
> [[chp7 (résumé)|chp7]] définit les éléments propres d'une matrice avec un vecteur « nul ». Il faut lire « non nul », comme le dit le même chapitre plus haut.

En 1re année, la définition porte sur une application linéaire : $v$ est vecteur propre de $f$ associé à $\lambda$ si $f(v) = \lambda v$ et $v \neq 0$.

**En ACP** (Data analysis) : un vecteur propre de la matrice de covariance est une direction de composante principale (vecteur directeur de PC1, ou vecteur singulier). Voir [[Analyse en composantes principales]].

## À vérifier

- [[Chp 0e - Eigenvalues and eigenvectors]] écrit « Any linear combination of basic eigenvectors is an eigenvector » : ce n'est vrai que pour une même valeur propre et une combinaison non nulle.

Notion parente : [[Valeur propre]]. Liens : [[Espace propre]], [[Diagonalisation]], [[Indépendance linéaire]], [[Analyse en composantes principales]]

Résumés : [[Chp 0e - Eigenvalues and eigenvectors (résumé)]], [[chp7 (résumé)|chp7 (résumé)]], [[Séance 13 - Principal Components Analysis (résumé)]], [[Séance 13 - PCA in R (résumé)]]
