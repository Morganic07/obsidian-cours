---
type: concept
tags: [year4]
aliases: [pointeurs pendants, dangling pointer, pointeur fou, double free]
sources: ["[[Raw/Year 4/C++/Chp3 - pointeurs , tableaux, listes chainées, structures.docx|Chp3 - pointeurs , tableaux, listes chainées, structures]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : un pointeur pendant (*dangling pointer*) contient l'adresse d'une zone mémoire qui n'est plus valide. Deux cas classiques :

- un bloc libéré par `free` (ou `delete` en C++) : le pointeur garde l'adresse, mais le bloc a été rendu à l'allocateur ;
- une variable locale d'une fonction déjà terminée : son cadre de [[Pile d'exécution|pile]] a été libéré et sera réutilisé par l'appel suivant.

Lire ou écrire à travers un pointeur pendant est un comportement indéfini : le bloc a pu être réattribué à une autre donnée, d'où des valeurs fausses, la corruption d'autres variables ou une [[Erreur de segmentation]]. Le bug est souvent intermittent, car le programme peut sembler fonctionner tant que la zone n'a pas été réutilisée.

Bonnes pratiques :

- remettre le pointeur à `NULL` juste après le `free` ([[Pointeur NULL]]) : un accès ultérieur échoue alors franchement au lieu de lire une zone réattribuée ;
- ne jamais libérer deux fois le même bloc (*double free*), qui corrompt les structures internes de l'allocateur ; `free(NULL)` est en revanche sans effet ;
- ne jamais renvoyer l'adresse d'une variable locale (`return &a;`) ;
- dans une boucle qui libère une [[Liste chaînée]], sauvegarder l'adresse du suivant avant le `free`.

## Dans le cours

Le cours ne nomme pas la notion. Dans [[3 - pointeurs , tableaux, listes chainées, structures]], la sortie du programme complet montre qu'après `free`, `bufferinheap` et `pb` contiennent encore l'adresse du bloc (lignes 8 et 9) ; la fiche l'explique dans ses compléments.

Voir aussi : [[Allocation dynamique]], [[Pointeur NULL]], [[Erreur de segmentation]], [[Fuite mémoire]], [[Pointeur et adresse mémoire]].

Résumés : [[3 - pointeurs , tableaux, listes chainées, structures]]
