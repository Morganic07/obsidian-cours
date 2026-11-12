---
type: concept
tags: [year4]
aliases: [tests unitaires, unit test, unit testing]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : test automatisé d'une petite unité de code, en général une fonction, isolée du reste : on lui fournit des entrées choisies et on compare le résultat obtenu au résultat attendu. Rejoués à chaque modification, les tests détectent les régressions. En C++, on utilise `assert` (en-tête `<cassert>`) ou des cadriciels comme GoogleTest ou Catch2 : `assert(carre(3) == 9);`. Une fonction sans saisie ni affichage, qui reçoit ses entrées en paramètres et rend un résultat, est bien plus facile à tester.

## Dans le cours

[[4 - Cours complet]] compte parmi les raisons de définir une fonction le fait qu'elle « facilite les tests (on simule des entrées et on compare le résultat obtenu à celui attendu) ».

Résumés : [[4 - Cours complet]]
