---
type: concept
tags: [year1, year2, year3]
aliases: [trace of a matrix, trace d'un endomorphisme]
matieres: [Algèbre Linéaire, Bilinear Algebra, Data analysis (Thanos)]
sources: ["[[13 - Principal Components Analysis|Cours 13 - Principal Components Analysis]]", "[[Raw/Year 1/Algèbre Linéaire/Cours /chp7.docx|chp7 (Algèbre)]]", "[[Raw/Year 2/Bilinear Algebra/Chp 0e - Eigenvalues and eigenvectors.docx|Chp 0e - Eigenvalues and eigenvectors]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : la trace d'une matrice carrée $A = (a_{ij})$ de taille $n$ est la somme de ses coefficients diagonaux,
$$\text{tr}(A) = \sum_{i=1}^{n} a_{ii} = a_{11} + \dots + a_{nn}.$$

Somme des coefficients diagonaux d'une matrice carrée. Pour la [[Matrice de covariance]], c'est la variance totale des données : 50 dans l'exemple du cours ([[13 - Principal Components Analysis|Cours 13 - Principal Components Analysis]]).

## Propriétés (complément, hors du cours)

- **Linéarité** : $\text{tr}(A + B) = \text{tr}(A) + \text{tr}(B)$ et $\text{tr}(\alpha A) = \alpha\,\text{tr}(A)$ ; de plus $\text{tr}(A^T) = \text{tr}(A)$.
- **Produit** : $\text{tr}(AB) = \text{tr}(BA)$ (même si $AB \neq BA$), car les deux valent $\sum_{i,j} a_{ij}b_{ji}$. Attention, en général $\text{tr}(AB) \neq \text{tr}(A)\,\text{tr}(B)$.
- **Invariance par similitude** : si $A' = P^{-1}AP$ ([[Changement de base]]), $\text{tr}(A') = \text{tr}\big((AP)P^{-1}\big) = \text{tr}(A)$. Deux [[Matrices semblables|matrices semblables]] ont donc la même trace, et la trace d'un endomorphisme ne dépend pas de la base choisie.
- **Lien avec les valeurs propres** : en comptant les [[Valeur propre|valeurs propres]] complexes avec leur [[Multiplicité d'une valeur propre|multiplicité]], leur somme vaut $\text{tr}(A)$ (et leur produit vaut $\det A$, voir [[Déterminant]]). Pour une matrice diagonalisable $A = PDP^{-1}$, c'est immédiat : $\text{tr}(A) = \text{tr}(D)$.
- **Taille 2** : le polynôme caractéristique s'écrit $\chi_A(\lambda) = \lambda^2 - \text{tr}(A)\,\lambda + \det A$ ([[Équation caractéristique]]), d'où la relation $A^2 - \text{tr}(A)\,A + \det(A)\,I_2 = 0$ ([[Théorème de Cayley-Hamilton]]).

**Exemple** : $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ a pour valeurs propres $1$ et $3$ ([[7 - Algèbre linéaire]]) : $\text{tr}(A) = 4 = 1 + 3$ et $\det A = 3 = 1 \times 3$.

## Dans le cours

- En Data analysis (year 3), la trace de la matrice de covariance donne la variance totale ([[13 - Principal Components Analysis]]).
- Le chapitre 7 d'algèbre linéaire (year 1) relie trace, déterminant et valeurs propres dans ses compléments ([[7 - Algèbre linéaire]]).
- Le cours de Bilinear Algebra (year 2) n'en parle pas ; la fiche [[0 - Eigenvalues and eigenvectors]] s'en sert dans ses compléments sur le polynôme caractéristique.

Voir aussi : [[Matrice de covariance]], [[Valeur propre]], [[Équation caractéristique]], [[Matrices semblables]], [[Changement de base]], [[Déterminant]], [[Théorème de Cayley-Hamilton]], [[Diagonalisation]].

Résumés : [[13 - Principal Components Analysis]], [[7 - Algèbre linéaire]], [[0 - Eigenvalues and eigenvectors]]
