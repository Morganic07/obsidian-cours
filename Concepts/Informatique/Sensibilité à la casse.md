---
type: concept
tags: [year4]
aliases: [case sensitivity, sensible à la casse, case sensitive, casse]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : propriété d'un langage, d'un système ou d'une comparaison qui distingue majuscules et minuscules. Le C, le C++ et Java sont sensibles à la casse (`valeur`, `Valeur` et `VALEUR` sont trois noms différents), tout comme les systèmes de fichiers Linux ; ceux de Windows ne le sont pas. Une comparaison de chaînes avec `==` est sensible à la casse : « toto » et « Toto » diffèrent, et `<` range les majuscules avant les minuscules (ordre des codes [[Code ASCII|ASCII]]).

## Dans le cours

[[4 - Cours complet]] le montre par l'exécution « toto est après Toto » et déconseille de distinguer deux identificateurs par la seule casse.

Résumés : [[4 - Cours complet]]
