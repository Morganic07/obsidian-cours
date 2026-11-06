---
type: concept
aliases: [liste chaînée, listes chaînées, liste chainée, listes chainées, liste chaînée simple, chaînon, chaînons, liste (structure de données), ajouteEnTete, supprEnTete]
matieres: [Algo, C++]
sources: ["[[chp2 - piles listes file]]", "[[Chp3 - pointeurs , tableaux, listes chainées, structures]]"]
maj: 2026-11-06
---

En algo, une **liste** regroupe des éléments de même nature, chacun avec un rang, qu'on peut ajouter ou supprimer n'importe où.

Une liste chaînée est une structure dynamique faite de cellules (ou chaînons, ou nœuds). Chacune est rangée à une certaine adresse, contient une valeur et un pointeur, souvent nommé `suivant`, vers la cellule suivante. À la différence d'un tableau, les cellules ne sont pas contiguës en mémoire.

- Le pointeur de la dernière cellule vaut `NULL` ([[Pointeur NULL]]).
- Une liste est définie par l'adresse de son premier élément. Une liste vide est un pointeur `NULL`.

**Opérations du cours d'algo** : `vide()`, `estVide(L)`, `ajouteEnTete(x,L)`, `supprEnTete(L)`, `compte(L)`, `cons(x,L)`. La tête est le dernier élément ajouté, la queue est le reste.

**En C** : le chaînon est une `struct` avec un champ `valeur` et un champ `struct Chainon *suivant`. Pour ajouter en tête, la fonction reçoit l'adresse du pointeur de tête (`Chainon **`), car elle doit le modifier. Pour seulement parcourir, un `Chainon *` suffit. L'exemple du cours définit `typedef struct Chainon`, `ajouter_au_debut(Chainon **premier_ptr, int)` et `afficher_liste(Chainon *premier)`. Voir [[Pointeur et adresse mémoire]], [[Structure (struct)]], [[Opérateur flèche]] et [[Allocation dynamique]].

Liens : [[Pile et file]], [[Pointeur et adresse mémoire]], [[Structure (struct)]]

## À vérifier

- [[Chp3 - pointeurs , tableaux, listes chainées, structures]] : une annotation `[cite: 1]` est restée dans un commentaire du code (relevé du résumé).

Résumés : [[chp2 - piles listes file (résumé)]], [[Chp3 - pointeurs , tableaux, listes chainées, structures (résumé)]]
