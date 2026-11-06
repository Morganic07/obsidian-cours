---
type: matiere
sources: ["[[Chp 0a - Linear combination]]", "[[Chp 0b - Matrix algebra]]", "[[Chp 0c - Determinants]]", "[[Chp 0d - Vector Space]]", "[[Chp 0e - Eigenvalues and eigenvectors]]", "[[chp 1 - Orthogonality]]", "[[Chp2 - Symmetric matrices and quadratic forms]]", "[[Invertible matrix theorem]]"]
maj: 2026-11-06
---

Algèbre linéaire de 2e année : systèmes, matrices, espaces vectoriels, valeurs propres, orthogonalité, formes quadratiques et SVD. Les 8 notes sont intégrées.

## Parcours

Les chapitres 0a à 0e posent les bases et chacun réutilise le précédent. Le chapitre 1 ajoute la géométrie (longueurs, angles droits, projections). Le chapitre 2 réunit valeurs propres et orthogonalité.

| Note | Sujet | Résumé |
|---|---|---|
| [[Chp 0a - Linear combination]] | Systèmes, combinaisons, indépendance, transformations | [[Chp 0a - Linear combination (résumé)\|Résumé]] |
| [[Chp 0b - Matrix algebra]] | Produit, transposée, inverse | [[Chp 0b - Matrix algebra (résumé)\|Résumé]] |
| [[Chp 0c - Determinants]] | Déterminant, Cramer, formule de l'inverse | [[Chp 0c - Determinants (résumé)\|Résumé]] |
| [[Chp 0d - Vector Space]] | Sous-espaces, base, dimension, rang | [[Chp 0d - Vector Space (résumé)\|Résumé]] |
| [[Chp 0e - Eigenvalues and eigenvectors]] | Valeurs propres, diagonalisation | [[Chp 0e - Eigenvalues and eigenvectors (résumé)\|Résumé]] |
| [[chp 1 - Orthogonality]] | Projection, Gram-Schmidt, QR, moindres carrés | [[chp 1 - Orthogonality (résumé)\|Résumé]] |
| [[Chp2 - Symmetric matrices and quadratic forms]] | Théorème spectral, formes quadratiques, SVD | [[Chp2 - Symmetric matrices and quadratic forms (résumé)\|Résumé]] |
| [[Invertible matrix theorem]] | Les 20 énoncés équivalents | [[Invertible matrix theorem (résumé)\|Résumé]] |

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

- [[Chp2 - Symmetric matrices and quadratic forms (résumé)]] : « negative definite » est défini avec $Q(\mathbf{x}) > 0$.
- [[Chp 0e - Eigenvalues and eigenvectors (résumé)]] : une forme échelonnée ne donne pas les valeurs propres, contrairement à ta note.
- [[chp 1 - Orthogonality (résumé)]] : le projeté de $\mathbf{b}$ sur Col $A$ est $A\hat{\mathbf{x}}$, pas $\hat{\mathbf{x}}$.

## Liens avec les autres matières

Repérés dans les cours, à approfondir quand ces matières seront intégrées :

- **Year 3, Data analysis** : [[Cours 10 - linear regression]] et [[Cours 11 - Multiple Linear Regression and F-statistic]] reprennent la [[Régression linéaire]] et les [[Moindres carrés]]. Une figure de [[Cours 13 - Principal Components Analysis]] projette orthogonalement un point sur une composante.
- **Year 2, [[Year 2 - Analyse dans Rn]]** : [[Chp 2 - éléments de topologie dans Rn]] définit la [[Norme]] en général, alors que ce cours utilise celle qui vient du produit scalaire. La [[Matrice jacobienne]] y représente une [[Transformation linéaire]], et le [[Gradient]] s'y lit par un [[Produit scalaire]].
- **Year 1, [[Year 1 - Algèbre Linéaire]]** : mêmes notions en français, centrées sur les applications linéaires. La plupart des concepts sont communs aux deux matières.
- **Year 3, [[Year 3 - Data analysis (Thanos)]]** : l'ACP s'appuie sur la [[Décomposition en valeurs singulières]], la [[Matrice symétrique]], la [[Matrice orthogonale]] et le [[Théorème de Pythagore]] (aussi en [[Year 3 - Statistics]]).
- **Year 4, [[Year 4 - data mining]]** : des fonctions de [[Distance]] y sont proposées pour calculer l'inertie en clustering.
