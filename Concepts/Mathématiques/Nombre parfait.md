---
type: concept
tags: [year1, year4]
aliases: [nombres parfaits]
sources: ["[[Raw/Year 1/Contrôles.pdf|Contrôles.pdf]]"]
maj: 2026-11-12
---

Définition de l'examen d'informatique du 14 novembre 2022 (partie 2, pages 31-32 de `Contrôles.pdf`) : « Un nombre est dit parfait s'il est égal à la moitié de la somme de ses diviseurs. »

Exemple de l'énoncé : $6 = \frac{1 + 2 + 3 + 6}{2}$.

Cela revient à dire que le nombre est égal à la somme de ses diviseurs autres que lui-même ($6 = 1 + 2 + 3$).

L'exercice fait d'abord écrire une fonction `divise(a, b)`, puis la fonction `parfait(n : entier) : booléen`.

## Dans le cours

- [[tp5]] : en C, le programme 5.5 teste si un entier est parfait en accumulant la somme de ses diviseurs propres (test corrigé : l'ancienne version incluait le nombre lui-même), et le programme 5.7 liste les nombres parfaits jusqu'à 10 000 : 6, 28, 496, 8128.

Voir aussi : [[Fonction et procédure]], [[Nombre d'Armstrong]].

Résumés (rapprochement, complément hors du cours) : [[0 - diapo prof]]
