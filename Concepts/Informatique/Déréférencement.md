---
type: concept
tags: [year4]
aliases: [indirection, dereference, opérateur d'indirection, opérateur étoile]
sources: ["[[Raw/Year 4/C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[4 - Cours complet]]) : l'étoile `*` placée devant un [[Pointeur et adresse mémoire|pointeur]] accède à la variable dont il contient l'adresse : après `ptrInt = &i;`, `*ptrInt = 3;` met 3 dans `i` (« on pointe sur le contenu de `i` »). C'est l'indirection.

Complément, hors du cours : `*` a donc deux rôles, déclarer un pointeur (`int *p;`) et le déréférencer (`*p`). Déréférencer un pointeur nul ou non initialisé est un [[Comportement indéfini|comportement indéfini]], souvent une [[Erreur de segmentation|erreur de segmentation]]. Pour un pointeur sur structure, `p->champ` abrège `(*p).champ` (voir [[Opérateur flèche]]).

## Dans le cours

[[4 - Cours complet]] l'illustre par un schéma mémoire (adresses `0xbfbec7a8`…) et s'en sert dans l'exercice 5 (`echange2ParAdresse`). L'opération inverse est l'[[Opérateur d'adresse|opérateur `&`]].

Résumés : [[4 - Cours complet]]
