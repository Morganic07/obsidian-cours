---
type: concept
tags: [year4]
aliases: [bool, boolean, type booléen, booléens, true et false]
sources: ["[[Raw/Year 4/C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[4 - Cours complet]]) : type des variables logiques, qui valent `true` (vrai) ou `false` (faux) : `bool ouvert = true;`. C'est l'un des cinq types usuels du C++.

Complément, hors du cours : une comparaison (`a == b`) ou une combinaison par [[Opérateur logique|opérateurs logiques]] donne un `bool`. Converti en entier, `true` vaut 1 et `false` 0 ; inversement, tout nombre non nul est vrai. `cout` affiche `1` ou `0`, sauf avec `std::boolalpha`. En C, le type existe depuis C99 (`_Bool`, `bool` par `<stdbool.h>`) et `bool` est un mot-clé depuis C23 (voir [[Norme du C]]).

## Dans le cours

[[4 - Cours complet]] le range parmi les cinq types usuels, en le comparant au C (dont la fiche précise qu'il a `bool` depuis C99). Les fonctions booléennes se nomment avec un adjectif d'état (`estVide()`).

Voir aussi : [[Type primitif]].

Résumés : [[4 - Cours complet]]
