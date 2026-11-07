---
type: concept
tags: [year1, year2]
aliases: [opérations élémentaires, row operations, elementary row operations, row equivalent, lignes équivalentes, row reduction]
matieres: [Algèbre Linéaire, Bilinear Algebra]
sources: ["[[chp3 (résumé)|chp3]]", "[[Chp 0a - Linear combination (résumé)|Chp 0a - Linear combination]]", "[[Chp 0c - Determinants (résumé)|Chp 0c - Determinants]]"]
maj: 2026-11-06
---

Opérations autorisées sur les lignes d'un système (ou de sa matrice) pour le résoudre par pivot de Gauss.

**Algèbre Linéaire** : échanger deux lignes $L_i \leftrightarrow L_j$ ; multiplier une ligne par un scalaire non nul, $L_i \leftarrow \lambda L_i$ avec $\lambda \neq 0$ ; ajouter à une ligne une combinaison linéaire des autres, $L_i \leftarrow \alpha L_i + \beta L_j$. Le cours précise : « Utiliser que ça sinon on perd de l'information. »

**Bilinear Algebra** : échanger deux équations, multiplier une équation par une constante non nulle, remplacer une équation par sa somme avec un multiple d'une autre. Ces opérations sont réversibles. Deux matrices sont **équivalentes par lignes** (row equivalent) si l'on passe de l'une à l'autre par ces opérations ; les systèmes correspondants ont alors le même ensemble de solutions.

**Effet sur le [[Déterminant]]** : ajouter un multiple d'une ligne à une autre le laisse inchangé, échanger deux lignes change son signe, multiplier une ligne par $k$ le multiplie par $k$.

Notion parente : [[Forme échelonnée]]. Voir aussi : [[Système linéaire]], [[Matrice augmentée]], [[Matrice inversible]].

## À vérifier

- Pour $L_i \leftarrow \alpha L_i + \beta L_j$, il faut $\alpha \neq 0$, ce que [[chp3 (résumé)|chp3]] ne précise pas.
- La réduction par lignes ne donne pas les valeurs propres : c'est l'avertissement de Chp 0e, contredit par une note personnelle du même chapitre (voir [[Chp 0e - Eigenvalues and eigenvectors (résumé)]]).

Résumés : [[chp3 (résumé)]], [[Chp 0a - Linear combination (résumé)]], [[Chp 0b - Matrix algebra (résumé)]], [[Chp 0c - Determinants (résumé)]]
