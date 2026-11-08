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
  - "[[Raw/Year 4/C++/Chp3 - pointeurs , tableaux, listes chainées, structures.docx|Chp3 - pointeurs , tableaux, listes chainées, structures]]"
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : l'allocation dynamique réserve de la mémoire pendant l'exécution, sur le tas, pour une taille connue seulement à ce moment-là, et pour une durée choisie par le programme : le bloc existe jusqu'à sa libération explicite.

`malloc` (*memory allocation*) réserve des octets sur le tas (*heap*) : `malloc(sizeof(unsigned char) * 10)` réserve 10 octets, et le pointeur renvoyé contient l'adresse, pas les octets.

Règle du cours : après chaque `malloc`, toujours un `free`, qui libère le bloc pour qu'il soit réutilisé, sans en effacer le contenu. [[Erreurs du cours#^e-allocation-dynamique|✎]] Après `free`, les pointeurs gardent leur adresse. Précautions : initialiser les pointeurs et tester `NULL` ([[Pointeur NULL]]).

**Compléments, hors du cours** :

- **Pile et tas** : les variables locales sont sur la [[Pile d'exécution|pile]] et disparaissent automatiquement à la fin de leur bloc ; un bloc obtenu par `malloc` est sur le tas et existe jusqu'au `free`, quelle que soit la fonction en cours (voir [[Espace mémoire d'un processus]]). C'est ce qui permet à une fonction de créer une donnée qui lui survit, comme un chaînon de [[Liste chaînée]].
- **Échec** : `malloc` renvoie `NULL` quand l'allocation échoue ; il faut tester le résultat avant de s'en servir.
- **Type de retour** : `malloc` renvoie un `void *`, converti implicitement vers le bon type de pointeur en C ; en C++, il faut un transtypage explicite, et l'on préfère `new` et `delete` (`new T[n]` pour un tableau, libéré par `delete[]`), qui appellent aussi constructeurs et destructeurs.
- **Après `free`** : le pointeur garde l'adresse d'un bloc qui n'est plus à lui ; c'est un [[Pointeur pendant]], à remettre à `NULL`.
- **Oubli de `free`** : le bloc reste réservé et inaccessible, c'est une [[Fuite mémoire]].

Notion parente : [[Pointeur et adresse mémoire]]. Voir aussi : [[Pile d'exécution]], [[Pointeur NULL]], [[Liste chaînée]], [[Espace mémoire d'un processus]], [[Pointeur pendant]], [[Fuite mémoire]].

Résumés : [[3 - pointeurs , tableaux, listes chainées, structures]]
