---
type: concept
tags: [year4]
aliases: [printf, scanf, séquences de contrôle, spécificateur de format, modificateurs de format]
matieres: [C++]
sources: ["[[Chp1 - basiques]]", "[[Chp3 - pointeurs , tableaux, listes chainées, structures]]"]
maj: 2026-11-06
---

`printf` affiche, `scanf` lit : `scanf("%d", &i)` range l'entier lu à l'adresse de `i`.

Les **séquences de contrôle** commencent par `%` :

| Séquence | Interprétation |
|---|---|
| `%d`, `%i` | entier signé décimal |
| `%u` | entier non signé |
| `%o` | octal |
| `%x`, `%X` | hexadécimal |
| `%f` | réel |
| `%c` | caractère |
| `%s` | chaîne |
| `%p` | adresse (chapitre 3) |

Des **modificateurs** règlent la largeur (`%3d`, `%03d`). Le spécificateur choisit comment interpréter les bits : `char lettre = 66` s'affiche 66 avec `%d` et B avec `%c`.

Notion parente : [[Langage C]]. Voir aussi : [[Type primitif]], [[Pointeur et adresse mémoire]].

## À vérifier

- Chapitre 3 : « soit on fait %d, soit %p » pour afficher une adresse ; seul `%p` est correct (complément du résumé).

Résumés : [[Chp1 - basiques (résumé)]], [[Chp3 - pointeurs , tableaux, listes chainées, structures (résumé)]]
