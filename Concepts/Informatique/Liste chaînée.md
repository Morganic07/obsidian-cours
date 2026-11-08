---
type: concept
tags:
  - year2
  - year4
aliases:
  - liste chaînée
  - listes chaînées
  - liste chainée
  - listes chainées
  - liste chaînée simple
  - chaînon
  - chaînons
  - liste (structure de données)
  - ajouteEnTete
  - supprEnTete
  - linked list
  - liste doublement chaînée
  - doubly linked list
  - liste circulaire
matieres:
  - Algo
  - C++
sources:
  - "[[2 - piles listes file|chp2 - piles listes file]]"
  - "[[3 - pointeurs , tableaux, listes chainées, structures|Chp3 - pointeurs , tableaux, listes chainées, structures]]"
maj: 2026-11-08
---

En algo, une **liste** regroupe des éléments de même nature, chacun avec un rang, qu'on peut ajouter ou supprimer n'importe où.

Une liste chaînée est une structure dynamique faite de cellules (ou chaînons, ou nœuds). Chacune est rangée à une certaine adresse, contient une valeur et un pointeur, souvent nommé `suivant`, vers la cellule suivante. À la différence d'un tableau, les cellules ne sont pas contiguës en mémoire.

- Le pointeur de la dernière cellule vaut `NULL` ([[Pointeur NULL]]).
- Une liste est définie par l'adresse de son premier élément. Une liste vide est un pointeur `NULL`.

**Opérations du cours d'algo** : `vide()`, `estVide(L)`, `ajouteEnTete(x,L)`, `supprEnTete(L)`, `compte(L)`, `cons(x,L)`. La tête est le dernier élément ajouté, la queue est le reste.

**En C** : le chaînon est une `struct` avec un champ `valeur` et un champ `struct Chainon *suivant`. Pour ajouter en tête, la fonction reçoit l'adresse du pointeur de tête (`Chainon **`), car elle doit le modifier. Pour seulement parcourir, un `Chainon *` suffit. L'exemple du cours définit `typedef struct Chainon`, `ajouter_au_debut(Chainon **premier_ptr, int)` et `afficher_liste(Chainon *premier)`. Voir [[Pointeur et adresse mémoire]], [[Structure (struct)]], [[Opérateur flèche]] et [[Allocation dynamique]].

**Définition récursive (complément, hors du cours)** : une liste est soit vide, soit `cons(x, L)`, un élément suivi d'une liste. Les fonctions s'écrivent alors par [[Récursivité|récursivité]] sur cette forme : `compte(L)` vaut 0 si `estVide(L)`, et `1 + compte(queue(L))` sinon.

**En Python (complément, hors du cours)** : un chaînon est un objet à deux attributs, `elm` et `suivant` (`None` en fin de liste) ; la liste est la référence vers le premier chaînon.

```python
class Chainon:
    def __init__(self, elm, suivant=None):
        self.elm = elm
        self.suivant = suivant

L = Chainon(1, Chainon(2, Chainon(3)))   # 1 -> 2 -> 3
```

**Coûts comparés à un tableau (complément, hors du cours)** ([[Complexité algorithmique]]) :

| Opération | Tableau | Liste chaînée |
|---|---|---|
| Accès au $k$-ième élément | $O(1)$ | $O(k)$, il faut suivre $k$ pointeurs |
| Ajout ou suppression en tête | $O(n)$, décalage des éléments | $O(1)$ |
| Insertion ou suppression après un chaînon repéré | $O(n)$ | $O(1)$ |
| Taille | fixée à l'avance (tableau statique) | variable à l'exécution |
| Mémoire | contiguë, bon usage du cache | un pointeur de plus par cellule, cellules dispersées (moins bon usage du cache) |

**Variantes (complément, hors du cours)** :
- **liste doublement chaînée** : chaque cellule a aussi un pointeur `precedent` ; parcours dans les deux sens et suppression d'une cellule repérée en $O(1)$, au prix d'un pointeur de plus ;
- **liste circulaire** : la dernière cellule pointe vers la première au lieu de `NULL` ; utile pour un parcours en tourniquet (ordonnancement *round robin*).

**Libération en C (complément, hors du cours)** : parcourir la liste en sauvegardant `courant->suivant` avant chaque `free(courant)`, puisque la cellule libérée ne doit plus être lue, puis remettre la tête à `NULL` pour ne pas garder de pointeur pendant.

```c
Chainon *courant = *premier_ptr;
while (courant != NULL) {
    Chainon *suivant = courant->suivant;
    free(courant);
    courant = suivant;
}
*premier_ptr = NULL;
```

Liens : [[Pile et file]], [[Pointeur et adresse mémoire]], [[Structure (struct)]], [[Complexité algorithmique]], [[Récursivité]]

Résumés : [[2 - piles listes file]], [[3 - pointeurs , tableaux, listes chainées, structures]]
