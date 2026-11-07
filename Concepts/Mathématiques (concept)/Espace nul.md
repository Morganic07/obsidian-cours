---
type: concept
tags:
  - year1
  - year2
aliases:
  - null space
  - nullspace
  - null spaces
  - Nul A
  - kernel
  - noyau
  - Ker
  - noyau d'une application linéaire
  - N(A)
matieres:
  - Bilinear Algebra
  - Algèbre Linéaire
sources:
  - "[[0 - Vector Space (résumé)|Chp 0d - Vector Space]]"
  - "[[Cours/Mathématiques (cours)/Algèbre linéaire (cours)/2 - Algèbre linéaire (résumé)|chp2 (Algèbre)]]"
  - "[[7 - Algèbre linéaire (résumé)|chp7 (Algèbre)]]"
maj: 2026-11-06
---

Nul $A$, aussi appelé noyau, est l'ensemble des solutions de $A\mathbf{x} = \mathbf{0}$ : tous les vecteurs envoyés sur le vecteur nul. C'est un sous-espace de $\mathbb{R}^n$. Pour une transformation $T$ quelconque, $\ker(T) = \{\mathbf{v} \mid T\mathbf{v} = \mathbf{0}\}$.

- Quand Nul $A$ contient des vecteurs non nuls, sa famille génératrice compte autant de vecteurs que l'équation ([[Système linéaire homogène|système homogène]]) a de [[Variable libre|variables libres]].
- Nul $A = \{\mathbf{0}\}$ si et seulement si $A\mathbf{x} = \mathbf{0}$ n'a que la solution triviale, c'est-à-dire si la transformation est injective.

Il est défini implicitement, par une condition : trouver ses vecteurs demande de réduire $[A \ \mathbf{0}]$. En revanche, tester un $\mathbf{v}$ donné est immédiat, il suffit de calculer $A\mathbf{v}$. C'est l'inverse pour l'[[Espace des colonnes]] ; le cours compare les deux en 8 points.

**En Algèbre linéaire de première année** : le noyau de $f \in L(E, F)$ est $\mathrm{Ker} f = \{x \in E \mid f(x) = 0\}$, un sous-espace vectoriel de $E$ qui contient toujours 0. $f$ est injective si et seulement si $\mathrm{Ker} f = \{0\}$ ([[Injectivité et surjectivité]]). Une [[Valeur propre|valeur propre]] peut être nulle si $\mathrm{Ker} f \neq \{0\}$ (chp7).

Notion parente : [[Sous-espaces fondamentaux]] (Bilinear Algebra), [[Transformation linéaire]] (Algèbre linéaire). Voir aussi : [[Système linéaire homogène]], [[Variable libre]], [[Théorème du rang]], [[Valeur propre]], [[Espace des colonnes]], [[Rang d'une matrice]], [[Transformation linéaire]], [[Sous-espaces fondamentaux]], [[Espace propre]], [[Injectivité et surjectivité]]

Résumés : [[0 - Vector Space (résumé)]], [[Cours/Mathématiques (cours)/Algèbre linéaire (cours)/2 - Algèbre linéaire (résumé)|chp2 (résumé)]], [[7 - Algèbre linéaire (résumé)]]
