---
type: concept
tags:
  - year2
  - year4
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
  - stack (structure de données)
  - queue (structure de données)
  - collections.deque
matieres:
  - Algo
sources:
  - "[[2 - piles listes file|chp2 - piles listes file]]"
  - "[[1 - récursivité et complexité|Chp1 - récursivité et complexité]]"
maj: 2026-11-12
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

**En Python (complément, hors du cours)** : sur une liste, `append` et `pop()` coûtent $O(1)$ (amorti), ce qui en fait une bonne pile ; dépiler une pile vide lève `IndexError`, d'où le test `estVide()` avant `depiler()`. Une liste fait en revanche une mauvaise file : `pop(0)` décale tous les éléments restants et coûte $O(n)$. On utilise `collections.deque`, où `append` enfile et `popleft` défile, tous deux en $O(1)$.

```python
from collections import deque
f = deque()
f.append("a"); f.append("b")   # enfiler
f.popleft()                    # défiler : "a"
```

**Usages (complément, hors du cours)** :
- piles : [[Pile d'exécution]] des appels de fonctions, « annuler » d'un éditeur, bouton précédent du navigateur, contrôle du bon parenthésage (empiler chaque ouvrante, dépiler à chaque fermante), évaluation en notation polonaise inverse (`3 4 + 2 *` : empiler les nombres, dépiler deux opérandes à chaque opérateur), [[Parcours en profondeur]] écrit sans récursivité ;
- files : file d'impression, [[Tampon (buffer)|tampon]] entre un producteur et un consommateur, file des processus prêts de l'[[Ordonnancement des processus|ordonnancement]], [[Parcours en largeur]].

Liens : [[Liste chaînée]], [[Récursivité]], [[Parcours en profondeur]], [[Parcours en largeur]], [[Ordonnancement des processus]], [[Tampon (buffer)]]

En graph theory, [[2 - tree revisions années précédentes]] réalise le [[Parcours en largeur|parcours en largeur]] d'un arbre avec une file (racine d'abord, puis les fils de chaque nœud retiré en tête) ; ses compléments écrivent le [[Parcours préfixe|parcours préfixe]] sans récursivité avec une pile, et distinguent la file ordinaire de la [[File de priorité|file de priorité]].

Résumés : [[2 - piles listes file]], [[1 - récursivité et complexité]], [[2 - tree revisions années précédentes]]
