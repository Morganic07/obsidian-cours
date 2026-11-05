---
type: concept
aliases: [symmetric matrix, symmetric matrices, matrices symétriques]
sources: ["[[Chp2 - Symmetric matrices and quadratic forms]]"]
maj: 2026-11-05
---

Matrice telle que $A^T = A$, donc nécessairement carrée. Sa diagonale est libre, et ses autres coefficients vont par paires de part et d'autre.

$A$ est orthogonalement diagonalisable si et seulement si elle est symétrique. Des vecteurs propres d'espaces propres différents sont orthogonaux.

**Théorème spectral** : une matrice symétrique $n \times n$ a $n$ valeurs propres réelles (avec multiplicités), chaque espace propre a pour dimension la multiplicité de sa valeur propre, les espaces propres sont orthogonaux entre eux, et $A$ est orthogonalement diagonalisable. Le spectre de $A$ est l'ensemble de ses valeurs propres.

**Décomposition spectrale** : $A = \lambda_1\mathbf{u}_1\mathbf{u}_1^T + \dots + \lambda_n\mathbf{u}_n\mathbf{u}_n^T$ (formule complétée, le cours n'en commente que les termes). Chaque $\mathbf{u}_j\mathbf{u}_j^T$ est une matrice de [[Projection orthogonale|projection]] sur la droite engendrée par $\mathbf{u}_j$.

Liens : [[Transposée]], [[Diagonalisation]], [[Espace propre]], [[Forme quadratique]], [[Matrice orthogonale]], [[Décomposition en valeurs singulières]]

Résumé : [[Chp2 - Symmetric matrices and quadratic forms (résumé)]]
