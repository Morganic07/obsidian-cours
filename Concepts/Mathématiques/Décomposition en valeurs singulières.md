---
type: concept
tags: [year2, year3]
aliases: [singular value decomposition, SVD, singular values, singular value, valeurs singulières, The Singular Value Decomposition, SVD Summary, SVD réduite, reduced SVD, approximation de rang faible, low-rank approximation, théorème d'Eckart-Young]
sources: ["[[2 - Symmetric matrices and quadratic forms|Chp2 - Symmetric matrices and quadratic forms]]", "[[13 - Principal Components Analysis|Cours 13 - Principal Components Analysis]]"]
maj: 2026-11-08
---

Toute matrice $A$ de taille $m \times n$ et de rang $r$ s'écrit $A = U\Sigma V^T$, contrairement à $PDP^{-1}$ qui n'existe pas toujours. $U$ ($m \times m$) et $V$ ($n \times n$) sont orthogonales, et $\Sigma$ ($m \times n$) porte sur sa diagonale $\sigma_1 \ge \dots \ge \sigma_r > 0$. [[Erreurs du cours#^e-decomposition-en-valeurs-singulieres|✎]]

- **Valeurs singulières** : $\sigma_i = \sqrt{\lambda_i}$, où les $\lambda_i \ge 0$ sont les valeurs propres de $A^TA$. Ce sont aussi les longueurs des $A\mathbf{v}_i$.
- **Colonnes** : celles de $V$ (right singular vectors) sont les vecteurs propres de $A^TA$, celles de $U$ (left singular vectors) ceux de $AA^T$.
- **Relations** : $A\mathbf{v}_i = \sigma_i\mathbf{u}_i$ et $A^T\mathbf{u}_i = \sigma_i\mathbf{v}_i$.
- **Rang** : $\text{rank } A = r$, le nombre de valeurs singulières non nulles, et $\{A\mathbf{v}_1, \dots, A\mathbf{v}_r\}$ est une base orthogonale de Col $A$.
- **Unicité** : $U$ et $V$ ne sont pas uniques, mais les valeurs singulières le sont.
- **Application** : pour $A$ inversible, $\sigma_1/\sigma_n$ est le conditionnement ([[Conditionnement d'une matrice]]). Les instabilités numériques se repèrent dans $\Sigma$, car $U$ et $V$ ne changent ni les longueurs ni les angles.
- **Sous-espaces** : la SVD fournit des bases des quatre [[Sous-espaces fondamentaux]].

**Construction (complément, hors du cours)** :

1. diagonaliser orthogonalement $A^TA$ (symétrique, valeurs propres $\lambda_1 \ge \dots \ge \lambda_n \ge 0$) : ses vecteurs propres orthonormés $\mathbf{v}_1, \dots, \mathbf{v}_n$ forment $V$ ;
2. poser $\sigma_i = \sqrt{\lambda_i}$ ;
3. pour $i \le r$, poser $\mathbf{u}_i = \dfrac{A\mathbf{v}_i}{\sigma_i}$ (ces vecteurs sont automatiquement orthonormés) ;
4. si $r < m$, compléter $\{\mathbf{u}_1, \dots, \mathbf{u}_r\}$ en une base orthonormée de $\mathbb{R}^m$ par une base orthonormée de Nul $A^T$ (par exemple avec [[Procédé de Gram-Schmidt]]).

**SVD réduite (complément, hors du cours)** : en ne gardant que les $r$ premières colonnes, $A = U_r D V_r^T = \sum_{i=1}^{r} \sigma_i\,\mathbf{u}_i\mathbf{v}_i^T$, avec $D = \text{diag}(\sigma_1, \dots, \sigma_r)$ inversible. Elle sert à définir la [[Pseudo-inverse]] $A^+ = V_r D^{-1} U_r^T$.

**Approximation de rang faible (complément, hors du cours)** : $A_k = \sum_{i=1}^{k} \sigma_i\,\mathbf{u}_i\mathbf{v}_i^T$ ($k < r$) est la meilleure approximation de $A$ par une matrice de rang $k$ (théorème d'Eckart-Young, 1936), avec l'erreur $\|A - A_k\|_2 = \sigma_{k+1}$ ; en particulier $\|A\|_2 = \sigma_1$. Usages : compression d'images (on ne stocke que $k$ triplets $(\sigma_i, \mathbf{u}_i, \mathbf{v}_i)$), réduction de dimension en [[Analyse en composantes principales|ACP]].

**Cas symétrique (complément, hors du cours)** : pour $A$ [[Matrice symétrique|symétrique]], les valeurs singulières sont les $|\lambda_i|$ ; pour $A$ symétrique [[Forme quadratique définie positive|définie positive]], la SVD coïncide avec la diagonalisation orthogonale $A = PDP^T$.

**En ACP** ([[13 - Principal Components Analysis|Cours 13 - Principal Components Analysis]]) : on écrit $A = U\Sigma V^T = \sigma_1\mathbf{u}_1\mathbf{v}_1^T + \dots + \sigma_r\mathbf{u}_r\mathbf{v}_r^T$, et $V$ est la matrice des loadings ([[Loadings et scores (ACP)]]).

Notion parente : [[Matrice symétrique]].

Liens : [[Valeur propre]], [[Matrice orthogonale]], [[Rang d'une matrice]], [[Pseudo-inverse]], [[Procédé de Gram-Schmidt]], [[Analyse en composantes principales]] (application en statistique)

Résumés : [[2 - Symmetric matrices and quadratic forms]], [[13 - Principal Components Analysis]]
