---
type: concept
tags: [year2]
aliases: [quadratic form, quadratic forms, formes quadratiques, change of variable in a quadratic form, Classifying quadratic forms, signature d'une forme quadratique, loi d'inertie de Sylvester, Sylvester's law of inertia, identité de polarisation, polarization identity]
sources: ["[[2 - Symmetric matrices and quadratic forms|Chp2 - Symmetric matrices and quadratic forms]]"]
maj: 2026-11-08
---

Fonction $Q(\mathbf{x}) = \mathbf{x}^TA\mathbf{x}$ avec $A$ symétrique, la matrice de la forme. Exemple le plus simple : $\mathbf{x}^TI\mathbf{x} = \|\mathbf{x}\|^2$. Dans le plan, $ax^2 + bxy + cy^2$ s'écrit avec la matrice symétrique associée.

- **Changement de variable** : avec $\mathbf{x} = P\mathbf{y}$, la matrice devient $P^TAP$. Si $P$ est orthogonale et diagonalise $A$, on obtient $\mathbf{y}^TD\mathbf{y}$, sans terme croisé.
- **Axes principaux** : les colonnes de $P$. Ils donnent un repère où la courbe $\mathbf{x}^TA\mathbf{x} = c$ (ellipse, hyperbole, etc.) est en position standard.
- **Classement selon les valeurs propres de $A$** : définie positive si toutes sont positives, définie négative ($Q(\mathbf{x}) < 0$ pour tout $\mathbf{x} \neq \mathbf{0}$) si toutes sont négatives, indéfinie s'il y a les deux signes. [[Erreurs du cours#^e-forme-quadratique|✎]]
- **Coupes horizontales** des graphes $z = Q(\mathbf{x})$ dans le plan : ellipse pour $3x_1^2 + 7x_2^2$ et $-3x_1^2 - 7x_2^2$, deux droites parallèles pour $3x_1^2$ ($x_1 = \pm\sqrt{c/3}$ ; c'est la coupe verticale à $x_2$ fixé qui est une parabole), hyperbole pour $3x_1^2 - 7x_2^2$. [[Erreurs du cours#^e-forme-quadratique|✎]]
- **Optimisation sous $\|\mathbf{x}\| = 1$** : le maximum de $\mathbf{x}^TA\mathbf{x}$ est la plus grande valeur propre, atteinte en un vecteur propre unitaire $\mathbf{u}_1$, et le minimum la plus petite. Si l'on impose en plus $\mathbf{x}^T\mathbf{u}_1 = \dots = \mathbf{x}^T\mathbf{u}_{k-1} = 0$, le maximum est $\lambda_k$, atteint en $\mathbf{u}_k$.

## Compléments (hors du cours)

- **Lire la matrice** : le coefficient diagonal $a_{ii}$ est le coefficient de $x_i^2$, et pour $i \ne j$, $a_{ij} = a_{ji}$ vaut la **moitié** du coefficient de $x_ix_j$. Ainsi $ax^2 + bxy + cy^2$ a pour matrice $\begin{pmatrix} a & b/2 \\ b/2 & c \end{pmatrix}$, et $5x_1^2 - 4x_1x_2 + 5x_2^2$ a pour matrice $\begin{pmatrix} 5 & -2 \\ -2 & 5 \end{pmatrix}$.
- **Pourquoi symétrique** : pour toute matrice carrée $M$, $\mathbf{x}^TM\mathbf{x}$ est un scalaire, égal à sa transposée $\mathbf{x}^TM^T\mathbf{x}$, donc $\mathbf{x}^TM\mathbf{x} = \mathbf{x}^T\left(\frac{M + M^T}{2}\right)\mathbf{x}$. On peut toujours remplacer $M$ par sa partie symétrique, et la matrice symétrique d'une forme quadratique est unique.
- **Identité de polarisation** : la [[Forme bilinéaire|forme bilinéaire]] symétrique associée à $Q$ est $f(\mathbf{x}, \mathbf{y}) = \mathbf{x}^TA\mathbf{y} = \frac12\left[Q(\mathbf{x} + \mathbf{y}) - Q(\mathbf{x}) - Q(\mathbf{y})\right]$, et $Q(\mathbf{x}) = f(\mathbf{x}, \mathbf{x})$ : forme quadratique et forme bilinéaire symétrique se déterminent mutuellement.
- **Signature et loi d'inertie de Sylvester** : par tout changement de variable inversible qui ramène $Q$ à une somme de carrés $\sum_i d_i y_i^2$ (diagonalisation orthogonale, ou méthode de Gauss par complétion des carrés), le nombre $p$ de coefficients $d_i > 0$ et le nombre $q$ de coefficients $d_i < 0$ ne dépendent pas de la réduction choisie. Le couple $(p, q)$ est la **signature** de $Q$ ; $p$ et $q$ sont les nombres de valeurs propres positives et négatives de $A$, et $p + q$ est le [[Rang d'une matrice|rang]] de $A$. Ainsi $Q$ est définie positive ssi sa signature est $(n, 0)$.
Notion parente : [[Forme bilinéaire]]. Voir aussi : [[Matrice symétrique]], [[Valeur propre]], [[Diagonalisation]], [[Norme]], [[Théorème des axes principaux]], [[Forme quadratique définie positive]], [[Optimisation sous contrainte]], [[Rang d'une matrice]].
Résumé : [[2 - Symmetric matrices and quadratic forms]]
