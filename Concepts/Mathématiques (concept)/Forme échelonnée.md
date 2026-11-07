---
type: concept
tags:
  - year1
  - year2
aliases:
  - echelon form
  - formes échelonnées
  - totalement échelonnée
  - pivot de Gauss
  - méthode du pivot de Gauss
  - système en cascade
  - reduced echelon form
  - forme échelonnée réduite
  - colonne pivot
  - pivot column
  - pivot position
  - position pivot
sources:
  - "[[0 - Linear combination (résumé)|Chp 0a - Linear combination]]"
  - "[[0 - Eigenvalues and eigenvectors (résumé)|Chp 0e - Eigenvalues and eigenvectors]]"
  - "[[3 - Algèbre linéaire (résumé)|chp3 (Algèbre)]]"
  - "[[Raw/Year 1/Contrôles.pdf|Contrôles.pdf]]"
maj: 2026-11-06
---

Matrice dont les lignes de zéros sont en bas, et où chaque ligne non nulle a plus de zéros à gauche que la précédente. Elle est **réduite** (totalement échelonnée) si, en plus, le premier coefficient non nul de chaque ligne vaut 1 et si sa colonne ne contient rien d'autre au-dessus de lui. Chaque matrice est équivalente par lignes à une seule matrice réduite.

- **[[Opérations élémentaires sur les lignes|Opérations élémentaires]]** : remplacer une ligne par sa somme avec un multiple d'une autre, échanger deux lignes, multiplier une ligne par une constante non nulle. Elles sont réversibles et conservent les solutions.
- **Pivot** : premier terme non nul d'une ligne. Une colonne pivot en contient un. On réduit la [[Matrice augmentée|matrice augmentée]] et on entoure les positions pivots ; une colonne de la matrice des coefficients sans pivot correspond à une [[Variable libre|variable libre]]. $A\mathbf{x} = \mathbf{b}$ a une solution pour tout $\mathbf{b}$ si et seulement si $A$ a un pivot par ligne.
- **Pivot de Gauss** : la méthode qui amène un système à cette forme. On choisit une ligne pivot qu'on ne touche plus, on élimine les inconnues une par une par [[Combinaison linéaire|combinaisons linéaires]] pour obtenir un système en cascade, puis on remonte la cascade pour trouver leurs valeurs. Le cours de 1re année ne parle pas de forme échelonnée, seulement de pivot de Gauss ; la méthode et les opérations élémentaires sont demandées à l'évaluation 1 ([[Raw/Year 1/Contrôles.pdf|Contrôles]]).

> [!warning] Attention
> La forme échelonnée ne donne en général pas les [[Valeur propre|valeurs propres]]. Une note de [[0 - Eigenvalues and eigenvectors (résumé)|Chp 0e - Eigenvalues and eigenvectors]] affirme le contraire, mais l'avertissement du même chapitre l'exclut.

Notion parente : [[Système linéaire]].

Liens : [[Rang d'une matrice]], [[Matrice inversible]]

## À vérifier

- Le résumé de [[0 - Linear combination (résumé)]] (point 3) dit qu'« une colonne pivot est linéairement indépendante », formulation imprécise.

Résumés : [[0 - Linear combination (résumé)]], [[3 - Algèbre linéaire (résumé)|chp3 (résumé)]]
