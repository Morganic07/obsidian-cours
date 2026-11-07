---
type: concept
tags:
  - year1
  - year2
aliases:
  - matrice de passage
  - matrices de passage
  - changements de base
  - change of basis
sources:
  - "[[5 - Algèbre linéaire (résumé)|chp5 (Algèbre)]]"
  - "[[2 - Symmetric matrices and quadratic forms (résumé)|Chp2 - Symmetric matrices and quadratic forms]]"
  - "[[Raw/Year 1/Contrôles.pdf|Contrôles.pdf]]"
maj: 2026-11-06
---

La matrice de passage $P$ de la base $B$ à la base $B'$ a pour colonnes les coefficients des vecteurs de $B'$ exprimés dans $B$.

- **Composition** : $P_{B \to B'} \cdot P_{B' \to B''} = P_{B \to B''}$, et $P^{-1} = P_{B' \to B}$.
- **Application linéaire** : si $A$ est sa matrice dans $B$ et $A'$ sa matrice dans $B'$, alors $A' = P^{-1}AP$.
- **Coordonnées d'un vecteur** : $X' = P^{-1}X$. Le cours écrit $X^{-1}$, et l'hypothèse de ce théorème manque (voir le résumé).

Le cours résume la règle des colonnes par « nouveaux en fonction des anciens ».

C'est la même idée que le changement de variable $\mathbf{x} = P\mathbf{y}$ des [[Forme quadratique|formes quadratiques]] et que la [[Diagonalisation]] $A = PDP^{-1}$.

L'évaluation 3 de première année porte sur les [[Coordonnées dans une base|coordonnées dans une base]] de $\mathbb{R}^3$ et la [[Matrice d'une application linéaire|matrice d'une application]] dans cette base.

Notion parente : [[Base (algèbre linéaire)]]. Voir aussi : [[Matrice d'une application linéaire]], [[Coordonnées dans une base]], [[Transformation linéaire]], [[Matrice inversible]], [[Diagonalisation]]

## À vérifier

- chp5 : « $X^{-1} = P^{-1} \cdot X$ » (à lire $X' = P^{-1}X$), une ligne « Si X = X = » vide, et « matrice de F / de E » pour « matrice de $f$ ».

Résumés : [[5 - Algèbre linéaire (résumé)|chp5 (résumé)]]
