---
type: concept
tags: [year2]
aliases: [QR factorization, QR decomposition, The QR Factorization]
sources: ["[[chp 1 - Orthogonality (résumé)|chp 1 - Orthogonality]]"]
maj: 2026-11-06
---

Une matrice $A$ de taille $m \times n$ à colonnes linéairement indépendantes s'écrit $A = QR$. Les colonnes de $Q$ ($m \times n$) forment une base orthonormale de Col $A$, et $R$ ($n \times n$) est [[Matrice triangulaire|triangulaire]] supérieure, inversible, à diagonale positive. Appliquer Gram-Schmidt avec normalisation aux colonnes de $A$ revient à la factoriser ainsi.

La figure du cours donne les coefficients de $R$ pour trois colonnes : ligne $i$, colonne $j$, on trouve $\mathbf{e}_i^T \cdot \mathbf{a}_j$ pour $i \le j$ et 0 sinon, où les $\mathbf{e}_i$ sont les colonnes de $Q$ et les $\mathbf{a}_j$ celles de $A$. Sa légende dit « upper diagonal matrix », alors que le théorème parle d'« upper triangular ».

Notion parente : [[Procédé de Gram-Schmidt]]. Voir aussi : [[Matrice triangulaire]], [[Orthogonalité]], [[Famille orthogonale]], [[Espace des colonnes]]

Résumé : [[chp 1 - Orthogonality (résumé)]]
