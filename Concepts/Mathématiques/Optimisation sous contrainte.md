---
type: concept
tags: [year2]
aliases: [Constrained Optimization, quotient de Rayleigh, Rayleigh quotient]
matieres: [Bilinear Algebra]
sources: ["[[2 - Symmetric matrices and quadratic forms|Chp2 - Symmetric matrices and quadratic forms]]"]
maj: 2026-11-08
---

En Bilinear Algebra, il s'agit d'optimiser une forme quadratique sur la sphère unité. Sous la contrainte $\|\mathbf{x}\|=1$ :

- le maximum de $\mathbf{x}^TA\mathbf{x}$ est la plus grande valeur propre $\lambda_1$, atteint en un vecteur propre unitaire associé ;
- le minimum est la plus petite valeur propre.

Avec en plus $\mathbf{x}^T\mathbf{u}_1=\dots=\mathbf{x}^T\mathbf{u}_{k-1}=0$, le maximum est $\lambda_k$.

## Compléments (hors du cours)

**Preuve dans les axes principaux** : on diagonalise $A = PDP^T$ avec $P$ orthogonale ([[Théorème spectral]]) et $\lambda_1 \ge \dots \ge \lambda_n$. Avec $\mathbf{x} = P\mathbf{y}$, on a $\|\mathbf{y}\| = \|\mathbf{x}\| = 1$ ([[Matrice orthogonale]]) et
$$Q(\mathbf{x}) = \sum_{i=1}^n \lambda_i y_i^2 \le \lambda_1 \sum_{i=1}^n y_i^2 = \lambda_1,$$
avec égalité pour $\mathbf{y} = \mathbf{e}_1$, c'est-à-dire $\mathbf{x} = \mathbf{u}_1$. De même $Q(\mathbf{x}) \ge \lambda_n$, avec égalité en $\mathbf{u}_n$. Imposer $\mathbf{x} \perp \mathbf{u}_1, \dots, \mathbf{u}_{k-1}$ revient à $y_1 = \dots = y_{k-1} = 0$, d'où le maximum $\lambda_k$.

**Quotient de Rayleigh** : pour $\mathbf{x} \ne \mathbf{0}$, $R(\mathbf{x}) = \dfrac{\mathbf{x}^TA\mathbf{x}}{\mathbf{x}^T\mathbf{x}}$. Il ne dépend que de la direction de $\mathbf{x}$ ($R(c\mathbf{x}) = R(\mathbf{x})$ pour $c \ne 0$), donc l'optimiser sans contrainte revient à optimiser $Q$ sur la sphère unité : $\lambda_n \le R(\mathbf{x}) \le \lambda_1$.

**Application à l'ACP** : la direction qui maximise la variance projetée des données centrées est le vecteur propre unitaire de la plus grande valeur propre de la [[Matrice de covariance|matrice de covariance]] $S$, car cette variance vaut $\mathbf{u}^TS\mathbf{u}$. La $k$-ième composante principale est le vecteur propre de la $k$-ième plus grande valeur propre (contrainte d'orthogonalité aux précédentes), et cette valeur propre est la variance expliquée par la composante ([[Analyse en composantes principales]]).

**Exemple** : $Q(\mathbf{x}) = 5x_1^2 - 4x_1x_2 + 5x_2^2$ a pour matrice $\begin{pmatrix} 5 & -2 \\ -2 & 5 \end{pmatrix}$, de valeurs propres $7$ (vecteur propre $\frac{1}{\sqrt2}(1, -1)$) et $3$ (vecteur propre $\frac{1}{\sqrt2}(1, 1)$). Sur le cercle unité, le maximum de $Q$ est $7$ et son minimum $3$.

Notion parente : [[Forme quadratique]]. Voir aussi : [[Valeur propre]], [[Théorème spectral]], [[Matrice orthogonale]], [[Matrice de covariance]], [[Analyse en composantes principales]].

Résumés : [[2 - Symmetric matrices and quadratic forms]]
