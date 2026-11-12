---
type: concept
tags: [year4]
aliases: [function call, appel d'une fonction, appels de fonction]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[4 - Cours complet]]) : demande faite à une [[Fonction et procédure|fonction]] d'exécuter son traitement avec des [[Argument et paramètre|arguments]] donnés : `pow(i, 2)` appelle `pow` avec `i` et `2` et retourne `i²`. L'appel doit correspondre à la déclaration, que le compilateur vérifie : on n'est pas obligé d'utiliser le résultat, mais il faut donner exactement les arguments exigés, avec les parenthèses.

Complément, hors du cours : à l'appel, un cadre est empilé sur la [[Pile d'exécution|pile d'exécution]] (paramètres, variables locales, adresse de retour) ; au `return`, il est dépilé et l'exécution reprend après l'appel.

## Dans le cours

[[4 - Cours complet]] liste les appels invalides de `carre` : `carre()`, `carre`, `carre(1, 2)`, `carre("deux")`, et le seul correct, `carre(2)`.

Résumés : [[4 - Cours complet]]
