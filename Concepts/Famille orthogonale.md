---
type: concept
aliases: [orthogonal set, orthogonal sets, orthogonal basis, base orthogonale, orthonormal set, orthonormal sets, orthonormal basis, orthonormal columns, base orthonormale, famille orthonormale]
sources: ["[[chp 1 - Orthogonality]]"]
maj: 2026-11-05
---

Vecteurs deux à deux orthogonaux. Sans vecteur nul, ils sont linéairement indépendants et forment une base du sous-espace qu'ils engendrent.

Dans une base orthogonale $\{\mathbf{u}_1, \dots, \mathbf{u}_p\}$, les coefficients de $\mathbf{y} = c_1\mathbf{u}_1 + \dots + c_p\mathbf{u}_p$ se calculent directement : $c_j = \frac{\mathbf{y} \cdot \mathbf{u}_j}{\mathbf{u}_j \cdot \mathbf{u}_j}$.

La famille est **orthonormale** si, en plus, chaque vecteur est de norme 1. Une matrice $U$ de taille $m \times n$ a des colonnes orthonormales si et seulement si $U^TU = I$. Dans ce cas, $\|U\mathbf{x}\| = \|\mathbf{x}\|$ et $(U\mathbf{x}) \cdot (U\mathbf{y}) = \mathbf{x} \cdot \mathbf{y}$ : $U$ préserve les longueurs et l'orthogonalité.

Liens : [[Orthogonalité]], [[Indépendance linéaire]], [[Base (algèbre linéaire)]], [[Norme]], [[Matrice orthogonale]], [[Procédé de Gram-Schmidt]]

Résumé : [[chp 1 - Orthogonality (résumé)]]
