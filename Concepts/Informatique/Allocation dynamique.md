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
  - "[[3 - pointeurs , tableaux, listes chainées, structures|Chp3 - pointeurs , tableaux, listes chainées, structures]]"
maj: 2026-11-07
---

`malloc` (*memory allocation*) réserve des octets sur le tas (*heap*) : `malloc(sizeof(unsigned char) * 10)` réserve 10 octets, et le pointeur renvoyé contient l'adresse, pas les octets.

Règle du cours : après chaque `malloc`, toujours un `free`. Après `free`, les pointeurs gardent leur adresse. Précautions : initialiser les pointeurs et tester `NULL` ([[Pointeur NULL]]).

Notion parente : [[Pointeur et adresse mémoire]]. Voir aussi : [[Pile d'exécution]], [[Pointeur NULL]], [[Liste chaînée]].

## Erreurs du cours

- [[Raw/Year 4/C++/Chp3 - pointeurs , tableaux, listes chainées, structures.docx|Chp3 - pointeurs , tableaux, listes chainées, structures]] écrit que `free()` va « vider le contenu de la mémoire à cette adresse » ; il faut « libérer le bloc » : `free` rend la mémoire au système sans l'effacer (complément, hors du cours).
- Même document : le programme déclare `unsigned char *buffer;` puis utilise `bufferinheap`, jamais déclaré, et appelle `free(buffer)` sur le pointeur non initialisé ; il faut déclarer `unsigned char *bufferinheap;` et appeler `free(bufferinheap)`. Tel quel, le programme ne compile pas.

Résumés : [[3 - pointeurs , tableaux, listes chainées, structures]]
