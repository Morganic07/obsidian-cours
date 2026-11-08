---
type: concept
tags: [year2]
aliases: [pseudoinverse, pseudo-inverse de Moore-Penrose, Moore-Penrose inverse, Moore-Penrose pseudoinverse, inverse généralisé]
sources: ["[[Raw/Year 2/Bilinear Algebra/Chp2 - Symmetric matrices and quadratic forms.docx|Chp2 - Symmetric matrices and quadratic forms]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : soit $A$ une matrice $m \times n$ de rang $r$, de [[Décomposition en valeurs singulières|SVD réduite]] $A = U_r D V_r^T$, où $U_r$ ($m \times r$) et $V_r$ ($n \times r$) regroupent les $r$ premiers vecteurs singuliers et $D = \text{diag}(\sigma_1, \dots, \sigma_r)$ les valeurs singulières non nulles. La **pseudo-inverse de Moore-Penrose** de $A$ est la matrice $n \times m$
$$A^+ = V_r D^{-1} U_r^T = \sum_{i=1}^{r} \frac{1}{\sigma_i}\,\mathbf{v}_i\mathbf{u}_i^T.$$
Elle existe pour toute matrice, carrée ou non, et elle est unique : c'est la seule matrice $X$ qui vérifie les quatre conditions de Penrose $AXA = A$, $XAX = X$, $(AX)^T = AX$, $(XA)^T = XA$.

**Propriétés** :

- si $A$ est [[Matrice inversible|inversible]], $A^+ = A^{-1}$ ;
- $AA^+ = U_rU_r^T$ est la [[Projection orthogonale|projection orthogonale]] sur Col $A$, et $A^+A = V_rV_r^T$ la projection orthogonale sur Row $A$ ([[Sous-espaces fondamentaux]]) ;
- si les colonnes de $A$ sont indépendantes ($r = n$), $A^+ = (A^TA)^{-1}A^T$ ; si ses lignes sont indépendantes ($r = m$), $A^+ = A^T(AA^T)^{-1}$ ;
- $(A^+)^+ = A$ et $(A^T)^+ = (A^+)^T$.

**Moindres carrés** : $\hat{\mathbf{x}} = A^+\mathbf{b}$ est une solution de [[Moindres carrés|moindres carrés]] de $A\mathbf{x} = \mathbf{b}$ : $A\hat{\mathbf{x}} = AA^+\mathbf{b}$ est le projeté orthogonal de $\mathbf{b}$ sur Col $A$, donc $\hat{\mathbf{x}}$ minimise $\|A\mathbf{x} - \mathbf{b}\|$. Parmi toutes les solutions de moindres carrés, c'est celle de plus petite norme, car elle est dans Row $A$. Quand les colonnes sont indépendantes, on retrouve la formule $(A^TA)^{-1}A^T\mathbf{b}$ des équations normales.

## Dans le cours

Le cours ne la nomme pas. Elle apparaît dans les compléments de [[2 - Symmetric matrices and quadratic forms]], comme application de la SVD.

Voir aussi : [[Décomposition en valeurs singulières]], [[Moindres carrés]], [[Matrice inversible]], [[Projection orthogonale]], [[Sous-espaces fondamentaux]], [[Rang d'une matrice]].

Résumés : [[2 - Symmetric matrices and quadratic forms]]
