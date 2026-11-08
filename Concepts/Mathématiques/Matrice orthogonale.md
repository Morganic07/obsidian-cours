---
type: concept
tags: [year2, year3]
aliases: [orthogonal matrix, orthogonal matrices, matrices orthogonales]
sources: ["[[1 - Orthogonality|chp 1 - Orthogonality]]", "[[13 - Principal Components Analysis|Cours 13 - Principal Components Analysis]]"]
maj: 2026-11-08
---

Matrice **carrée** à colonnes ortho**normales**, malgré son nom. Ses lignes sont aussi orthonormales. Elle est inversible, et $U^{-1} = U^T$.

**En ACP** : on cherche une matrice orthogonale $P$ telle que $X = PY$, d'où $Y_k = P^{-1}X_k = P^TX_k$ ([[Analyse en composantes principales]], [[13 - Principal Components Analysis]]).

## Compléments (hors du cours)

**Pourquoi $U^TU = I$** : le coefficient $(i,j)$ de $U^TU$ vaut $\mathbf{u}_i \cdot \mathbf{u}_j$, soit 1 si $i = j$ et 0 sinon, puisque les colonnes sont orthonormales. Pour une matrice $U$ de taille $m \times n$ à colonnes orthonormales avec $m > n$ (donc non carrée, pas une matrice orthogonale), on a encore $U^TU = I_n$, mais $UU^T$ n'est pas l'identité : c'est la matrice de la [[Projection orthogonale|projection orthogonale]] sur Col $U$.

**Déterminant** : $\det U = \pm 1$, car $\det(U^T)\det(U) = \det(U^TU) = \det(I) = 1$ et $\det(U^T) = \det(U)$ ([[Déterminant]]).

**Isométrie** : $\|U\mathbf{x}\| = \|\mathbf{x}\|$ et $(U\mathbf{x})\cdot(U\mathbf{y}) = \mathbf{x}\cdot\mathbf{y}$ ; elle conserve donc longueurs et angles. Si $\det U = 1$, c'est une rotation ; si $\det U = -1$, c'est une rotation composée avec une réflexion.

**Exemples dans $\mathbb{R}^2$** :
$$\begin{bmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{bmatrix} \ (\text{rotation d'angle } \theta, \det = 1), \qquad \begin{bmatrix}1 & 0 \\ 0 & -1\end{bmatrix} \ (\text{symétrie par rapport à l'axe des abscisses}, \det = -1).$$
Les matrices de permutation (identité aux lignes permutées) sont aussi orthogonales.

Notion parente : [[Famille orthogonale]].

Liens : [[Déterminant]], [[Projection orthogonale]], [[Transposée]], [[Matrice inversible]], [[Matrice symétrique]]

Résumés : [[1 - Orthogonality]], [[13 - Principal Components Analysis]]
