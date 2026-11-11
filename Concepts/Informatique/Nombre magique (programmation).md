---
type: concept
tags: [year4]
aliases: [constante magique, magic number, constantes magiques]
sources: ["[[Raw/Year 4/C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[4 - Cours complet]]) : [[Valeur littérale|valeur littérale]] écrite directement dans le code, hors d'une définition `const` ; le polycopié dit par dérision « constante magique ». Elle rend le code obscur (que signifie `2.54`, `100` ?) et oblige, si elle change, à la modifier partout.

Complément, hors du cours : on la remplace par une [[Constante (programmation)|constante]] nommée (`const double CM_PAR_POUCE = 2.54;`). Les valeurs évidentes (0, 1) sont tolérées. Le terme désigne aussi, en un autre sens, les octets d'en-tête qui identifient un format de fichier.

## Dans le cours

[[4 - Cours complet]] en fait une [[Règle de codage|règle de codage]] : éviter les littéraux dans le code et utiliser des constantes aux noms significatifs ; l'exercice 4 remplace ainsi `100` par `MAXIMUM`.

Résumés : [[4 - Cours complet]]
