---
type: concept
tags: [year2]
aliases: [QR factorization, QR decomposition, The QR Factorization]
sources: ["[[1 - Orthogonality|chp 1 - Orthogonality]]"]
maj: 2026-11-08
---

Une matrice $A$ de taille $m \times n$ à colonnes linéairement indépendantes s'écrit $A = QR$. Les colonnes de $Q$ ($m \times n$) forment une base orthonormale de Col $A$, et $R$ ($n \times n$) est [[Matrice triangulaire|triangulaire]] supérieure, inversible, à diagonale positive. Appliquer Gram-Schmidt avec normalisation aux colonnes de $A$ revient à la factoriser ainsi.

La figure du cours donne les coefficients de $R$ pour trois colonnes : ligne $i$, colonne $j$, on trouve $\mathbf{e}_i^T \cdot \mathbf{a}_j$ pour $i \le j$ et 0 sinon, où les $\mathbf{e}_i$ sont les colonnes de $Q$ et les $\mathbf{a}_j$ celles de $A$. Sa légende dit « upper diagonal matrix », alors que le théorème parle d'« upper triangular ».

## Compléments (hors du cours)

**Calcul de $R$** : puisque $Q^TQ = I$, on a $R = Q^TA$ ; le coefficient $(i,j)$ vaut $\mathbf{e}_i^T\mathbf{a}_j$, ce que donne la figure du cours. Les zéros sous la diagonale viennent de ce que $\mathbf{a}_j \in \text{Span}\{\mathbf{e}_1, \dots, \mathbf{e}_j\}$ (propriété de [[Procédé de Gram-Schmidt|Gram-Schmidt]]), sous-espace orthogonal à $\mathbf{e}_i$ pour $i > j$.

**Exemple** : $A = \begin{bmatrix}3&1\\6&2\\0&2\end{bmatrix}$. Gram-Schmidt donne les colonnes de $Q$ : $\mathbf{e}_1 = \left(\tfrac{1}{\sqrt5}, \tfrac{2}{\sqrt5}, 0\right)$ et $\mathbf{e}_2 = (0,0,1)$. Puis
$$R = Q^TA = \begin{bmatrix}3\sqrt5 & \sqrt5 \\ 0 & 2\end{bmatrix}.$$

**Usage pour les [[Moindres carrés|moindres carrés]]** : avec $A = QR$, $A^TA = R^TQ^TQR = R^TR$, et les équations normales $A^TA\hat{\mathbf{x}} = A^T\mathbf{b}$ se ramènent à
$$R\hat{\mathbf{x}} = Q^T\mathbf{b},$$
système triangulaire résolu par remontée. C'est plus stable que de résoudre directement les équations normales, qui élèvent le [[Conditionnement d'une matrice|conditionnement]] au carré ($\kappa(A^TA) = \kappa(A)^2$).

**En pratique**, les logiciels calculent la factorisation QR par réflexions de Householder ou par Gram-Schmidt modifié, plus robustes aux arrondis que le Gram-Schmidt classique.

Notion parente : [[Procédé de Gram-Schmidt]]. Voir aussi : [[Moindres carrés]], [[Conditionnement d'une matrice]], [[Matrice triangulaire]], [[Orthogonalité]], [[Famille orthogonale]], [[Espace des colonnes]]

Résumé : [[1 - Orthogonality]]
