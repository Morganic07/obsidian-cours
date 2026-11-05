---
type: concept
aliases: [singular value decomposition, SVD, singular values, singular value, valeurs singulières]
sources: ["[[Chp2 - Symmetric matrices and quadratic forms]]"]
maj: 2026-11-05
---

Toute matrice $A$ de taille $m \times n$ et de rang $r$ s'écrit $A = U\Sigma V^T$, contrairement à $PDP^{-1}$ qui n'existe pas toujours. $U$ ($m \times m$) et $V$ ($n \times n$) sont orthogonales, et $\Sigma$ ($m \times n$) porte sur sa diagonale $\sigma_1 \ge \dots \ge \sigma_r > 0$.

- **Valeurs singulières** : $\sigma_i = \sqrt{\lambda_i}$, où les $\lambda_i \ge 0$ sont les valeurs propres de $A^TA$. Ce sont aussi les longueurs des $A\mathbf{v}_i$.
- **Colonnes** : celles de $V$ (right singular vectors) sont les vecteurs propres de $A^TA$, celles de $U$ (left singular vectors) ceux de $AA^T$.
- **Relations** : $A\mathbf{v}_i = \sigma_i\mathbf{u}_i$ et $A^T\mathbf{u}_i = \sigma_i\mathbf{v}_i$.
- **Rang** : $\text{rank } A = r$, le nombre de valeurs singulières non nulles, et $\{A\mathbf{v}_1, \dots, A\mathbf{v}_r\}$ est une base orthogonale de Col $A$.
- **Unicité** : $U$ et $V$ ne sont pas uniques, mais les valeurs singulières le sont.
- **Application** : pour $A$ inversible, $\sigma_1/\sigma_n$ est le conditionnement. Les instabilités numériques se repèrent dans $\Sigma$, car $U$ et $V$ ne changent ni les longueurs ni les angles.

Liens : [[Valeur propre]], [[Matrice orthogonale]], [[Rang d'une matrice]], [[Sous-espaces fondamentaux]], [[Matrice symétrique]]

Résumé : [[Chp2 - Symmetric matrices and quadratic forms (résumé)]]
