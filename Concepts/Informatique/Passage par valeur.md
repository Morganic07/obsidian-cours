---
type: concept
tags: [year4]
aliases: [passage par copie, pass by value, paramètres par référence]
sources: ["[[chp2 - structures code]]", "[[Chp3 - pointeurs , tableaux, listes chainées, structures]]"]
maj: 2026-11-06
---

En C, les arguments d'une fonction sont passés par copie : une variable simple passée à une fonction n'est pas modifiée dans `main`. `echange(int a, int b)` n'échange donc pas `var1` et `var2`.

Pour modifier la variable, on passe son adresse : `echange(int *a, int *b)`, appelée avec `echange(&var1, &var2)`. C'est le passage par adresse, traité avec [[Pointeur et adresse mémoire]].

Notion parente : [[Fonction et procédure]]. Voir aussi : [[Pile d'exécution]], [[Tableau (programmation)]].

## À vérifier

- Le texte de la version par valeur écrit `echange(&var1, &var2)` au lieu de `echange(var1, var2)` (relevé du résumé).
- Le titre du cours parle de « paramètres par référence » alors qu'il s'agit de passage par adresse.

Résumés : [[chp2 - structures code (résumé)]], [[Chp3 - pointeurs , tableaux, listes chainées, structures (résumé)]]
