---
type: concept
aliases: [linear system, linear systems, system of linear equation, system of linear equations, systems of linear equation, systems of linear equations, systèmes linéaires]
sources: ["[[Chp 0a - Linear combination]]", "[[Cours/Year 1/Algèbre Linéaire/Cours/chp3|chp3 (Algèbre)]]"]
maj: 2026-11-05
---

Ensemble d'équations $a_1x_1 + \dots + a_nx_n = b$. Deux systèmes sont équivalents s'ils ont les mêmes solutions. Un système est **compatible** (consistent) s'il a une ou une infinité de solutions, et **incompatible** (inconsistent) s'il n'en a aucune.

Trois écritures ont les mêmes solutions : $A\mathbf{x} = \mathbf{b}$, $x_1\mathbf{a}_1 + \dots + x_n\mathbf{a}_n = \mathbf{b}$ et la matrice augmentée $[\mathbf{a}_1 \cdots \mathbf{a}_n \mid \mathbf{b}]$.

- **Existence** : le système est compatible si et seulement si la dernière colonne de la matrice augmentée n'est pas une colonne pivot. Une équation $0 = \lambda$ avec $\lambda \neq 0$ le rend donc incompatible.
- **Unicité** : un système compatible a une seule solution s'il n'a pas de variable libre, et une infinité sinon.
- **Homogène** : $A\mathbf{x} = \mathbf{0}$ a toujours la solution triviale $\mathbf{x} = \mathbf{0}$. Ses solutions forment un sous-espace, avec des solutions non nulles s'il y a plus d'inconnues que d'équations.
- **Non homogène** : les solutions sont $\mathbf{p} + \mathbf{v}_h$, où $\mathbf{p}$ est une solution particulière et $\mathbf{v}_h$ une solution de l'équation homogène.

Liens : [[Forme échelonnée]], [[Combinaison linéaire]], [[Espace nul]], [[Matrice inversible]], [[Moindres carrés]]

Résumés : [[Chp 0a - Linear combination (résumé)]], [[Sources/Year 1/Algèbre Linéaire/chp3 (résumé)|chp3 (résumé)]]
