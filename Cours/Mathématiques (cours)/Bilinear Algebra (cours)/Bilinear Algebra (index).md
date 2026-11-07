---
type: matiere
tags:
  - year2
sources:
  - "[[0 - Linear combination (résumé)|Chp 0a - Linear combination]]"
  - "[[0 - Matrix algebra (résumé)|Chp 0b - Matrix algebra]]"
  - "[[0 - Determinants (résumé)|Chp 0c - Determinants]]"
  - "[[0 - Vector Space (résumé)|Chp 0d - Vector Space]]"
  - "[[0 - Eigenvalues and eigenvectors (résumé)|Chp 0e - Eigenvalues and eigenvectors]]"
  - "[[1 - Orthogonality (résumé)|chp 1 - Orthogonality]]"
  - "[[2 - Symmetric matrices and quadratic forms (résumé)|Chp2 - Symmetric matrices and quadratic forms]]"
  - "[[3 -Invertible matrix theorem (résumé)|Invertible matrix theorem]]"
maj: 2026-11-06
---

Algèbre linéaire de 2e année : systèmes, matrices, espaces vectoriels, valeurs propres, orthogonalité, formes quadratiques et SVD. Les 8 notes sont intégrées.

## Parcours

Les chapitres 0a à 0e posent les bases et chacun réutilise le précédent. Le chapitre 1 ajoute la géométrie (longueurs, angles droits, projections). Le chapitre 2 réunit valeurs propres et orthogonalité.

| Note | Sujet | Résumé |
|---|---|---|
| [[0 - Linear combination (résumé)\|Chp 0a - Linear combination]] | Systèmes, combinaisons, indépendance, transformations | [[0 - Linear combination (résumé)\|Résumé]] |
| [[0 - Matrix algebra (résumé)\|Chp 0b - Matrix algebra]] | Produit, transposée, inverse | [[0 - Matrix algebra (résumé)\|Résumé]] |
| [[0 - Determinants (résumé)\|Chp 0c - Determinants]] | Déterminant, Cramer, formule de l'inverse | [[0 - Determinants (résumé)\|Résumé]] |
| [[0 - Vector Space (résumé)\|Chp 0d - Vector Space]] | Sous-espaces, base, dimension, rang | [[0 - Vector Space (résumé)\|Résumé]] |
| [[0 - Eigenvalues and eigenvectors (résumé)\|Chp 0e - Eigenvalues and eigenvectors]] | Valeurs propres, diagonalisation | [[0 - Eigenvalues and eigenvectors (résumé)\|Résumé]] |
| [[1 - Orthogonality (résumé)\|chp 1 - Orthogonality]] | Projection, Gram-Schmidt, QR, moindres carrés | [[1 - Orthogonality (résumé)\|Résumé]] |
| [[2 - Symmetric matrices and quadratic forms (résumé)\|Chp2 - Symmetric matrices and quadratic forms]] | Théorème spectral, formes quadratiques, SVD | [[2 - Symmetric matrices and quadratic forms (résumé)\|Résumé]] |
| [[3 -Invertible matrix theorem (résumé)\|Invertible matrix theorem]] | Les 20 énoncés équivalents | [[3 -Invertible matrix theorem (résumé)\|Résumé]] |

## Concepts

- **Systèmes et vecteurs (0a)** : [[Système linéaire]], [[Système linéaire homogène]], [[Matrice augmentée]], [[Opérations élémentaires sur les lignes]], [[Forme échelonnée]], [[Variable libre]], [[Combinaison linéaire]], [[Espace engendré]], [[Indépendance linéaire]]
- **Transformations (0a)** : [[Transformation linéaire]], [[Transformations géométriques du plan]], [[Injectivité et surjectivité]]
- **Matrices (0b)** : [[Produit matriciel]], [[Matrice diagonale]], [[Transposée]], [[Matrice inversible]], [[Théorème de la matrice inversible]]
- **Déterminants (0c)** : [[Déterminant]], [[Matrice triangulaire]], [[Comatrice]], [[Règle de Cramer]]
- **Espaces (0d)** : [[Espace vectoriel]], [[Sous-espace vectoriel]], [[Sous-espaces fondamentaux]], [[Espace des colonnes]], [[Espace nul]], [[Base (algèbre linéaire)]], [[Dimension (algèbre linéaire)]], [[Rang d'une matrice]]
- **Valeurs propres (0e)** : [[Valeur propre]], [[Vecteur propre]], [[Équation caractéristique]], [[Multiplicité d'une valeur propre]], [[Espace propre]], [[Diagonalisation]], [[Récurrence]]
- **Orthogonalité (chapitre 1)** : [[Produit scalaire]], [[Norme]], [[Vecteur unitaire]], [[Distance]], [[Orthogonalité]], [[Théorème de Pythagore]], [[Complément orthogonal]], [[Famille orthogonale]], [[Matrice orthogonale]], [[Projection orthogonale]], [[Procédé de Gram-Schmidt]], [[Factorisation QR]], [[Moindres carrés]], [[Régression linéaire]]
- **Matrices symétriques (chapitre 2)** : [[Matrice symétrique]], [[Théorème spectral]], [[Décomposition spectrale]], [[Développement colonnes-lignes]], [[Corps (algèbre)]]
- **Formes (chapitre 2)** : [[Forme linéaire]], [[Forme bilinéaire]], [[Forme quadratique]], [[Forme quadratique définie positive]], [[Théorème des axes principaux]], [[Optimisation sous contrainte]]
- **SVD (chapitre 2)** : [[Décomposition en valeurs singulières]], [[Conditionnement d'une matrice]]

## À revoir en priorité avant un examen

Trois passages de tes notes semblent faux et touchent à des points de cours importants. Le détail est dans les résumés.

- [[2 - Symmetric matrices and quadratic forms (résumé)]] : « negative definite » est défini avec $Q(\mathbf{x}) > 0$.
- [[0 - Eigenvalues and eigenvectors (résumé)]] : une forme échelonnée ne donne pas les valeurs propres, contrairement à ta note.
- [[1 - Orthogonality (résumé)]] : le projeté de $\mathbf{b}$ sur Col $A$ est $A\hat{\mathbf{x}}$, pas $\hat{\mathbf{x}}$.

## Liens avec les autres matières

Repérés dans les cours, à approfondir quand ces matières seront intégrées :

- **Year 3, Data analysis** : [[10 - linear regression (résumé)|Cours 10 - linear regression]] et [[11 - Multiple Linear Regression and F-statistic (résumé)|Cours 11 - Multiple Linear Regression and F-statistic]] reprennent la [[Régression linéaire]] et les [[Moindres carrés]]. Une figure de [[13 - Principal Components Analysis (résumé)|Cours 13 - Principal Components Analysis]] projette orthogonalement un point sur une composante.
- **Year 2, [[Analyse dans Rn (index)]]** : [[2 - éléments de topologie dans Rn (résumé)|Chp 2 - éléments de topologie dans Rn]] définit la [[Norme]] en général, alors que ce cours utilise celle qui vient du produit scalaire. La [[Matrice jacobienne]] y représente une [[Transformation linéaire]], et le [[Gradient]] s'y lit par un [[Produit scalaire]].
- **Year 1, [[Algèbre linéaire (index)]]** : mêmes notions en français, centrées sur les applications linéaires. La plupart des concepts sont communs aux deux matières.
- **Year 3, [[Data analysis (index)]]** : l'ACP s'appuie sur la [[Décomposition en valeurs singulières]], la [[Matrice symétrique]], la [[Matrice orthogonale]] et le [[Théorème de Pythagore]] (aussi en [[Statistics (index)]]).
- **Year 4, [[Data mining (index)]]** : des fonctions de [[Distance]] y sont proposées pour calculer l'inertie en clustering.
