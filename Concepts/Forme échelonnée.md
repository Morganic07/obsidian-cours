---
type: concept
aliases: [echelon form, formes échelonnées, totalement échelonnée]
sources: ["[[Chp 0a - Linear combination]]", "[[Chp 0e - Eigenvalues and eigenvectors]]"]
maj: 2026-11-05
---

Matrice dont les lignes de zéros sont en bas, et où chaque ligne non nulle a plus de zéros à gauche que la précédente. Elle est **réduite** (totalement échelonnée) si, en plus, le premier coefficient non nul de chaque ligne vaut 1 et si sa colonne ne contient rien d'autre au-dessus de lui. Chaque matrice est équivalente par lignes à une seule matrice réduite.

- **Opérations élémentaires** : remplacer une ligne par sa somme avec un multiple d'une autre, échanger deux lignes, multiplier une ligne par une constante non nulle. Elles sont réversibles et conservent les solutions.
- **Pivot** : premier terme non nul d'une ligne. Une colonne pivot en contient un. Une colonne sans pivot correspond à une variable libre.

> [!warning] Attention
> La forme échelonnée ne donne en général pas les [[Valeur propre|valeurs propres]]. Une note de [[Chp 0e - Eigenvalues and eigenvectors]] affirme le contraire, mais l'avertissement du même chapitre l'exclut.

Liens : [[Système linéaire]], [[Rang d'une matrice]], [[Matrice inversible]]

Résumé : [[Chp 0a - Linear combination (résumé)]]
