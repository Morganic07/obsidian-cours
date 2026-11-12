---
type: concept
tags: [year1, year4]
aliases: [présentation modulaire, approche modulaire, modularité, décomposition en sous-problèmes]
matieres: [Algo Maths, C／C++]
sources: ["[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"]
maj: 2026-11-11
---

Pour résoudre un problème complexe, on le décompose en sous-problèmes ; AlgoID1 cite Descartes (*Discours de la méthode*).

La présentation modulaire demande des modules courts et testables, le moins possible de variables globales, et un découpage qui rend l'algorithme léger et lisible. Elle aide à chercher les erreurs et à vérifier la correction.

## En C++

[[5 - Compilation séparée]] découpe un programme en fichiers : pour chaque classe, un [[Fichier d'en-tête|fichier d'en-tête]] `.h` qui la déclare (l'interface) et un [[Fichier source|fichier source]] `.cpp` qui définit ses méthodes (l'implémentation), plus `main.cpp`. Chaque `.cpp` est compilé séparément ([[Compilation séparée]]), et un [[Make (logiciel)|Makefile]] automatise la construction.

Le découpage en modules réduit le couplage : un module ne dépend que de l'interface des autres, pas de leur code, si bien qu'on peut modifier une implémentation sans toucher aux fichiers qui l'utilisent (voir [[Interface et implémentation]]). [[Complément hors du cours|ⓘ]]

Notion parente : [[Algorithme]]. Voir aussi : [[Fonction et procédure]], [[Portée d'une variable]].

[[4 - Cours complet]] (troisième partie, « Programmation modulaire ») décrit un programme comme un ensemble de parties qui coopèrent et échangent des données ; l'exercice 4 déplace `somme1aN()` dans `somme.cpp`, déclarée dans `somme.h`, incluse dans le fichier de `main()`.

Résumés : [[0 - diapo prof]], [[5 - Compilation séparée]], [[4 - Cours complet]]
