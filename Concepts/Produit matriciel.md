---
type: concept
aliases: [matrix product, matrix multiplication, produits matriciels, multiplication matricielle]
sources: ["[[Chp 0a - Linear combination]]", "[[Chp 0b - Matrix algebra]]", "[[Cours/Year 1/Algèbre Linéaire/Cours/chp4|chp4 (Algèbre)]]"]
maj: 2026-11-05
---

Si $A$ est de taille $m \times n$ et $B$ de taille $n \times p$, alors $AB$ est la matrice $m \times p$ de colonnes $A\mathbf{b}_1, \dots, A\mathbf{b}_p$. Coefficient par coefficient, c'est la somme sur $k$ des $a_{ik}b_{kj}$. $A\mathbf{x}$ est la combinaison des colonnes de $A$, de poids les coefficients de $\mathbf{x}$.

Propriétés : $A(BC) = (AB)C$, $A(B + C) = AB + AC$, $(B + C)A = BA + CA$, $r(AB) = (rA)B = A(rB)$, et $I_mA = A = AI_n$.

En général :

- $AB \neq BA$ ;
- $AB = AC$ n'implique pas $B = C$ ;
- $AB = 0$ n'implique pas $A = 0$ ou $B = 0$.

Il représente la composée d'applications : $M_{g \circ f} = M_g \times M_f$. Le développement colonnes-lignes donne aussi $AB = \text{col}_1(A)\,\text{row}_1(B) + \dots + \text{col}_n(A)\,\text{row}_n(B)$.

Liens : [[Combinaison linéaire]], [[Transposée]], [[Matrice inversible]], [[Déterminant]], [[Transformation linéaire]]

Résumés : [[Chp 0b - Matrix algebra (résumé)]], [[Sources/Year 1/Algèbre Linéaire/chp4 (résumé)|chp4 (résumé)]]
