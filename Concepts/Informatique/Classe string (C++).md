---
type: concept
tags: [year4]
aliases: [std::string, string C++, "<string>"]
sources: ["[[Raw/Year 4/C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[4 - Cours complet]]) : type des [[Chaîne de caractères|chaînes de caractères]] en C++ (`string prenom = "Robert";`). Il définit ses propres opérations : `+` concatène (`nom + " Junior"`), `==`, `<`, `>` comparent selon l'ordre lexicographique ; `-` n'est pas défini et provoque une erreur de compilation. `cin >> s` lit un mot, jusqu'au premier [[Espace blanc|espace blanc]].

Complément, hors du cours : `std::string` est une classe de la [[Bibliothèque standard du C++|bibliothèque standard]], déclarée dans `<string>`, qui gère seule sa mémoire (pas de taille fixe ni de `'\0'` à gérer comme en C). Méthodes utiles : `size()`, `substr(pos, n)`, `find(…)`, `s[i]`. Ses opérateurs sont des [[Surcharge d'opérateurs|surcharges d'opérateurs]]. Une ligne entière se lit avec [[Fonction getline|`getline`]].

## Dans le cours

[[4 - Cours complet]] l'utilise dès la deuxième partie (saisie du nom, comparaison de chaînes, détecteur de mots répétés) et note qu'il n'existe pas en C.

Résumés : [[4 - Cours complet]]
