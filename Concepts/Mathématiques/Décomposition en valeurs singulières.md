---
type: concept
tags: [year2, year3]
aliases: [singular value decomposition, SVD, singular values, singular value, valeurs singulières, The Singular Value Decomposition, SVD Summary]
sources: ["[[Chp2 - Symmetric matrices and quadratic forms]]", "[[Cours 13 - Principal Components Analysis]]"]
maj: 2026-11-06
---

Toute matrice $A$ de taille $m \times n$ et de rang $r$ s'écrit $A = U\Sigma V^T$, contrairement à $PDP^{-1}$ qui n'existe pas toujours. $U$ ($m \times m$) et $V$ ($n \times n$) sont orthogonales, et $\Sigma$ ($m \times n$) porte sur sa diagonale $\sigma_1 \ge \dots \ge \sigma_r > 0$.

- **Valeurs singulières** : $\sigma_i = \sqrt{\lambda_i}$, où les $\lambda_i \ge 0$ sont les valeurs propres de $A^TA$. Ce sont aussi les longueurs des $A\mathbf{v}_i$.
- **Colonnes** : celles de $V$ (right singular vectors) sont les vecteurs propres de $A^TA$, celles de $U$ (left singular vectors) ceux de $AA^T$.
- **Relations** : $A\mathbf{v}_i = \sigma_i\mathbf{u}_i$ et $A^T\mathbf{u}_i = \sigma_i\mathbf{v}_i$.
- **Rang** : $\text{rank } A = r$, le nombre de valeurs singulières non nulles, et $\{A\mathbf{v}_1, \dots, A\mathbf{v}_r\}$ est une base orthogonale de Col $A$.
- **Unicité** : $U$ et $V$ ne sont pas uniques, mais les valeurs singulières le sont.
- **Application** : pour $A$ inversible, $\sigma_1/\sigma_n$ est le conditionnement ([[Conditionnement d'une matrice]]). Les instabilités numériques se repèrent dans $\Sigma$, car $U$ et $V$ ne changent ni les longueurs ni les angles.
- **Sous-espaces** : la SVD fournit des bases des quatre [[Sous-espaces fondamentaux]].

**En ACP** ([[Cours 13 - Principal Components Analysis]]) : on écrit $A = U\Sigma V^T = \sigma_1\mathbf{u}_1\mathbf{v}_1^T + \dots + \sigma_r\mathbf{u}_r\mathbf{v}_r^T$, et $V$ est la matrice des loadings ([[Loadings et scores (ACP)]]).

Notion parente : [[Matrice symétrique]].

Liens : [[Valeur propre]], [[Matrice orthogonale]], [[Rang d'une matrice]], [[Analyse en composantes principales]] (application en statistique)

## À vérifier

- [[Chp2 - Symmetric matrices and quadratic forms]] : coquille $V^r$ pour $V^T$, et une taille « $n \times m$ » contre $m \times n$ ailleurs.

Résumés : [[Chp2 - Symmetric matrices and quadratic forms (résumé)]], [[Cours 13 - Principal Components Analysis (résumé)]]
