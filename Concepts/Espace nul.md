---
type: concept
aliases: [null space, nullspace, null spaces, Nul A, kernel, noyau]
matieres: [Bilinear Algebra, Algèbre Linéaire]
sources: ["[[Chp 0d - Vector Space]]"]
maj: 2026-11-05
---

Nul $A$, aussi appelé noyau, est l'ensemble des solutions de $A\mathbf{x} = \mathbf{0}$ : tous les vecteurs envoyés sur le vecteur nul. C'est un sous-espace de $\mathbb{R}^n$. Pour une transformation $T$ quelconque, $\ker(T) = \{\mathbf{v} \mid T\mathbf{v} = \mathbf{0}\}$.

- Quand Nul $A$ contient des vecteurs non nuls, sa famille génératrice compte autant de vecteurs que l'équation a de variables libres.
- Nul $A = \{\mathbf{0}\}$ si et seulement si $A\mathbf{x} = \mathbf{0}$ n'a que la solution triviale, c'est-à-dire si la transformation est injective.

Il est défini implicitement, par une condition : trouver ses vecteurs demande de réduire $[A \ \mathbf{0}]$. En revanche, tester un $\mathbf{v}$ donné est immédiat, il suffit de calculer $A\mathbf{v}$. C'est l'inverse pour l'[[Espace des colonnes]].

Liens : [[Espace des colonnes]], [[Rang d'une matrice]], [[Transformation linéaire]], [[Sous-espaces fondamentaux]], [[Espace propre]], [[Injectivité et surjectivité]]

Résumé : [[Chp 0d - Vector Space (résumé)]]
