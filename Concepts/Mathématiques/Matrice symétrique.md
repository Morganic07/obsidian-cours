---
type: concept
tags: [year2, year3]
aliases: [symmetric matrix, symmetric matrices, matrices symétriques, diagonalization of symmetric matrices]
sources: ["[[Chp2 - Symmetric matrices and quadratic forms (résumé)|Chp2 - Symmetric matrices and quadratic forms]]", "[[Séance 13 - Principal Components Analysis (résumé)|Cours 13 - Principal Components Analysis]]"]
maj: 2026-11-06
---

Matrice telle que $A^T = A$, donc nécessairement carrée. Sa diagonale est libre, et ses autres coefficients vont par paires de part et d'autre.

$A$ est orthogonalement diagonalisable si et seulement si elle est symétrique. Des vecteurs propres d'espaces propres différents sont orthogonaux.

**Théorème spectral** : une matrice symétrique $n \times n$ a $n$ valeurs propres réelles (avec multiplicités), chaque espace propre a pour dimension la multiplicité de sa valeur propre, les espaces propres sont orthogonaux entre eux, et $A$ est orthogonalement diagonalisable. Le spectre de $A$ est l'ensemble de ses valeurs propres.

**Décomposition spectrale** : $A = \lambda_1\mathbf{u}_1\mathbf{u}_1^T + \dots + \lambda_n\mathbf{u}_n\mathbf{u}_n^T$, obtenue en développant $PDP^T$ colonnes-lignes. Chaque $\mathbf{u}_j\mathbf{u}_j^T$ est une matrice de [[Projection orthogonale|projection]] sur la droite engendrée par $\mathbf{u}_j$.

En Data analysis, la [[Matrice de covariance]] est symétrique, donc ses vecteurs propres sont orthogonaux ([[Séance 13 - Principal Components Analysis (résumé)]]).

Voir aussi : [[Théorème spectral]], [[Transposée]], [[Diagonalisation]], [[Espace propre]], [[Forme quadratique]], [[Matrice orthogonale]], [[Décomposition en valeurs singulières]], [[Matrice de covariance]].

Résumés : [[Chp2 - Symmetric matrices and quadratic forms (résumé)]], [[Séance 13 - Principal Components Analysis (résumé)]]
