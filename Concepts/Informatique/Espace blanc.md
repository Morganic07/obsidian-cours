---
type: concept
tags: [year4]
aliases: [whitespace, blanc, caractère d'espacement, espaces blancs]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[4 - Cours complet]]) : caractère d'espacement (*whitespace*) : l'espace, la tabulation ou le retour à la ligne. Par convention, la lecture d'une chaîne par `cin >>` se termine sur un espace blanc, et les espaces qui précèdent sont ignorés.

Complément, hors du cours : en C++, `std::isspace` (en-tête `<cctype>`) reconnaît aussi le retour chariot `\r`, la tabulation verticale et le saut de page. Dans le code source, les espaces blancs ne servent qu'à séparer les mots : le compilateur ignore leur nombre, d'où la liberté d'indentation.

## Dans le cours

[[4 - Cours complet]] explique ainsi que `cin >> nom` ne lit qu'un mot, et s'en sert pour le détecteur de mots répétés : `motPrecedent` est initialisé à `" "`, valeur que `cin` ne peut jamais lire.

Résumés : [[4 - Cours complet]]
