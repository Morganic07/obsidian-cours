---
type: concept
tags: [year2]
aliases: [orthogonal set, orthogonal sets, orthogonal basis, base orthogonale, orthonormal set, orthonormal sets, orthonormal basis, orthonormal columns, base orthonormale, famille orthonormale, Orthonormal Decomposition Theorem]
sources: ["[[chp 1 - Orthogonality (résumé)|chp 1 - Orthogonality]]"]
maj: 2026-11-06
---

Vecteurs deux à deux orthogonaux. Sans vecteur nul, ils sont linéairement indépendants et forment une base du sous-espace qu'ils engendrent.

Dans une base orthogonale $\{\mathbf{u}_1, \dots, \mathbf{u}_p\}$, les coefficients de $\mathbf{y} = c_1\mathbf{u}_1 + \dots + c_p\mathbf{u}_p$ se calculent directement : $c_j = \frac{\mathbf{y} \cdot \mathbf{u}_j}{\mathbf{u}_j \cdot \mathbf{u}_j}$.

La famille est **orthonormale** si, en plus, chaque vecteur est de norme 1. Une matrice $U$ de taille $m \times n$ a des colonnes orthonormales si et seulement si $U^TU = I$. Dans ce cas, $\|U\mathbf{x}\| = \|\mathbf{x}\|$ et $(U\mathbf{x}) \cdot (U\mathbf{y}) = \mathbf{x} \cdot \mathbf{y}$ : $U$ préserve les longueurs et l'orthogonalité.

**Orthonormal Decomposition Theorem** : si $\{\mathbf{u}_1, \dots, \mathbf{u}_p\}$ est une base orthonormale d'un sous-espace $W$ de $\mathbb{R}^n$, alors $\text{proj}_W\mathbf{y} = (\mathbf{y} \cdot \mathbf{u}_1)\mathbf{u}_1 + \dots + (\mathbf{y} \cdot \mathbf{u}_p)\mathbf{u}_p$, soit $\text{proj}_W\mathbf{y} = UU^T\mathbf{y}$ avec $U = [\mathbf{u}_1 \cdots \mathbf{u}_p]$ ([[Projection orthogonale]]). La preuve est hors examen.

Notion parente : [[Orthogonalité]].

Liens : [[Indépendance linéaire]], [[Base (algèbre linéaire)]], [[Norme]], [[Matrice orthogonale]], [[Procédé de Gram-Schmidt]]

Résumé : [[chp 1 - Orthogonality (résumé)]]
