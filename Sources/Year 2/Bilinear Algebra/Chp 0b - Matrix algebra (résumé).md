---
type: source
sources: ["[[Chp 0b - Matrix algebra]]"]
maj: 2026-11-05
---

Résumé de [[Chp 0b - Matrix algebra]], dans [[Year 2 - Bilinear Algebra]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Le chapitre donne les règles de calcul sur les matrices, puis caractérise les matrices inversibles.

## Contenu, dans l'ordre du cours

- **Opérations** : l'addition et la multiplication par un scalaire suivent les règles habituelles. Le cours définit aussi les matrices diagonale et identité.
- **[[Produit matriciel]]** : $AB = [A\mathbf{b}_1 \cdots A\mathbf{b}_p]$. Il est associatif et distributif, mais en général $AB \neq BA$, et ni $AB = AC$ ni $AB = 0$ ne permettent de simplifier.
- **[[Transposée]]** : $(AB)^T = B^TA^T$ et $(ABC)^T = C^TB^TA^T$.
- **[[Matrice inversible]]** : l'inverse est unique. Pour une matrice $2 \times 2$, $A^{-1} = \frac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$. En général, on réduit $[A \ I]$ jusqu'à $[I \ A^{-1}]$. Si $A$ est inversible, $A\mathbf{x} = \mathbf{b}$ a l'unique solution $\mathbf{x} = A^{-1}\mathbf{b}$.
- **Théorème de la matrice inversible** : énoncés a à l, voir [[Invertible matrix theorem]].
- **Transformation inversible** : il existe $S$ telle que $S(T(\mathbf{x})) = \mathbf{x}$ et $T(S(\mathbf{x})) = \mathbf{x}$. Multiplier par $A^{-1}$ annule la multiplication par $A$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Exemple $e^x$ et $\ln(x)$** : il illustre bien une fonction réciproque, mais il suit une définition portant sur des transformations **linéaires** de $\mathbb{R}^n$. Or ces deux fonctions ne sont pas linéaires, et $\ln$ n'est pas définie sur tout $\mathbb{R}$ (complément). L'exemple est donc seulement une analogie.
