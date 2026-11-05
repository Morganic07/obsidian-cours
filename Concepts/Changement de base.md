---
type: concept
aliases: [matrice de passage, matrices de passage, changements de base, change of basis]
sources: ["[[Cours/Year 1/Algèbre Linéaire/Cours/chp5|chp5 (Algèbre)]]", "[[Chp2 - Symmetric matrices and quadratic forms]]"]
maj: 2026-11-05
---

La matrice de passage $P$ de la base $B$ à la base $B'$ a pour colonnes les coefficients des vecteurs de $B'$ exprimés dans $B$.

- **Composition** : $P_{B \to B'} \cdot P_{B' \to B''} = P_{B \to B''}$, et $P^{-1} = P_{B' \to B}$.
- **Application linéaire** : si $A$ est sa matrice dans $B$ et $A'$ sa matrice dans $B'$, alors $A' = P^{-1}AP$.
- **Coordonnées d'un vecteur** : $X' = P^{-1}X$. Le cours écrit $X^{-1}$, et l'hypothèse de ce théorème manque (voir le résumé).

C'est la même idée que le changement de variable $\mathbf{x} = P\mathbf{y}$ des [[Forme quadratique|formes quadratiques]] et que la [[Diagonalisation]] $A = PDP^{-1}$.

Liens : [[Base (algèbre linéaire)]], [[Transformation linéaire]], [[Matrice inversible]], [[Diagonalisation]]

Résumé : [[Sources/Year 1/Algèbre Linéaire/chp5 (résumé)|chp5 (résumé)]]
