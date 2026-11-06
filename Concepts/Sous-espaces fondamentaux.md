---
type: concept
aliases: [four fundamental subspaces, fundamental subspaces, row space, left null space, left nullspace, quatre sous-espaces fondamentaux, Row A]
sources: ["[[Chp 0d - Vector Space]]", "[[chp 1 - Orthogonality]]", "[[Chp2 - Symmetric matrices and quadratic forms]]"]
maj: 2026-11-06
---

Une matrice $A$ de taille $m \times n$ et de rang $r$ définit quatre sous-espaces :

| Sous-espace | Dans | Dimension | Base issue de la SVD |
|---|---|---|---|
| Row space : Row $A$ = Col $A^T$ | $\mathbb{R}^n$ | $r$ | $\mathbf{v}_1, \dots, \mathbf{v}_r$ |
| Null space : Nul $A$ | $\mathbb{R}^n$ | $n - r$ | $\mathbf{v}_{r+1}, \dots, \mathbf{v}_n$ |
| Column space : Col $A$ | $\mathbb{R}^m$ | $r$ | $\mathbf{u}_1, \dots, \mathbf{u}_r$ |
| Left null space : Nul $A^T$ | $\mathbb{R}^m$ | $m - r$ | $\mathbf{u}_{r+1}, \dots, \mathbf{u}_m$ |

Autres notations du cours : $C(A)$, $N(A)$, $C(A^T)$, $N(A^T)$.

Ils sont orthogonaux deux à deux dans chaque espace : $(\text{Row } A)^\perp = \text{Nul } A$ et $(\text{Col } A)^\perp = \text{Nul } A^T$.

Notion parente : [[Sous-espace vectoriel]]. Liens : [[Espace des colonnes]], [[Espace nul]], [[Rang d'une matrice]], [[Complément orthogonal]], [[Décomposition en valeurs singulières]]

Résumés : [[Chp 0d - Vector Space (résumé)]], [[chp 1 - Orthogonality (résumé)]], [[Chp2 - Symmetric matrices and quadratic forms (résumé)]]
