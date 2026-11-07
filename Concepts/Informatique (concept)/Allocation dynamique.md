---
type: concept
tags:
  - year4
aliases:
  - heap
  - memory allocation
  - free()
  - malloc
matieres:
  - C++
sources:
  - "[[chp 3 - pointeurs , tableaux, listes chainées, structures (résumé)|Chp3 - pointeurs , tableaux, listes chainées, structures]]"
maj: 2026-11-06
---

`malloc` (*memory allocation*) réserve des octets sur le tas (*heap*) : `malloc(sizeof(unsigned char) * 10)` réserve 10 octets, et le pointeur renvoyé contient l'adresse, pas les octets.

Règle du cours : après chaque `malloc`, toujours un `free`. Après `free`, les pointeurs gardent leur adresse. Précautions : initialiser les pointeurs et tester `NULL` ([[Pointeur NULL]]).

Notion parente : [[Pointeur et adresse mémoire]]. Voir aussi : [[Pile d'exécution]], [[Pointeur NULL]], [[Liste chaînée]].

## À vérifier

- Le cours dit que `free` « vide le contenu de la mémoire » ; en réalité `free` libère le bloc sans l'effacer (complément du résumé).
- Le programme complet du cours ne compile pas (`bufferinheap` non déclaré).

Résumés : [[chp 3 - pointeurs , tableaux, listes chainées, structures (résumé)]]
