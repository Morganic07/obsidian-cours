---
type: concept
aliases: [matrix product, matrix multiplication, produits matriciels, multiplication matricielle]
sources: ["[[Chp 0a - Linear combination]]", "[[Chp 0b - Matrix algebra]]"]
maj: 2026-11-05
---

Si $A$ est de taille $m \times n$ et $B$ de taille $n \times p$, alors $AB$ est la matrice $m \times p$ de colonnes $A\mathbf{b}_1, \dots, A\mathbf{b}_p$. $A\mathbf{x}$ est la combinaison des colonnes de $A$, de poids les coefficients de $\mathbf{x}$.

Propriétés : $A(BC) = (AB)C$, $A(B + C) = AB + AC$, $(B + C)A = BA + CA$, $r(AB) = (rA)B = A(rB)$, et $I_mA = A = AI_n$.

En général :

- $AB \neq BA$ ;
- $AB = AC$ n'implique pas $B = C$ ;
- $AB = 0$ n'implique pas $A = 0$ ou $B = 0$.

Liens : [[Combinaison linéaire]], [[Transposée]], [[Matrice inversible]], [[Déterminant]]

Résumé : [[Chp 0b - Matrix algebra (résumé)]]
