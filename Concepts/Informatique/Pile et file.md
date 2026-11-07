---
type: concept
tags:
  - year2
aliases:
  - LIFO
  - FIFO
  - last in first out
  - first in first out
  - empiler
  - dépiler
  - enfiler
  - défiler
  - push et pop
  - sommet de pile
  - lireSommet
matieres:
  - Algo
sources:
  - "[[2 - piles listes file|chp2 - piles listes file]]"
  - "[[1 - récursivité et complexité|Chp1 - récursivité et complexité]]"
maj: 2026-11-07
---

| | Pile | File |
|---|---|---|
| Ordre | LIFO : le dernier inséré sort le premier | FIFO : le premier inséré sort le premier |
| Opérations | empiler (push), dépiler (pop) | enfiler (enqueue), défiler (dequeue) |
| Pointeurs | un seul, `top`, sur le haut | deux : avant (tête) et arrière (fin) |
| Représentation | verticale | horizontale |

**Méthodes d'une pile** : `estVide()`, `empiler(élément)`, `depiler()`, `lireSommet()` (lit le sommet de pile, le dernier élément empilé, pointé par `top`), `taille()`. En Python, une liste suffit : `append` empile, `pop` dépile.

**Méthodes d'une file** : `enfiler`, `defiler`, `estVide`, et une méthode pour le nombre d'éléments.

Le cours place les deux à côté de la [[Liste chaînée]]. La pile d'exécution, qui stocke paramètres, variables locales et adresses de retour des fonctions en cours, est une pile : voir [[Pile d'exécution]] et [[Récursivité]].

Liens : [[Liste chaînée]], [[Récursivité]]

Résumés : [[2 - piles listes file]], [[1 - récursivité et complexité]]
