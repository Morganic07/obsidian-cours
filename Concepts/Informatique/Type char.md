---
type: concept
tags: [year4]
aliases: [char, caractère (type), type caractère]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[4 - Cours complet]]) : type des caractères individuels (`char pointDecimal = '.';`), qui sert aussi pour des variables entières sur 8 bits (un [[Octet|octet]]). Un caractère s'écrit entre apostrophes `'a'`, une chaîne entre guillemets `"abc"`.

Complément, hors du cours : un `char` stocke en réalité le code numérique du caractère (65 pour `'A'` en [[Code ASCII|ASCII]]), ce qui explique qu'on puisse comparer des caractères ou les utiliser dans un `switch`. Les caractères spéciaux s'écrivent par [[Caractère d'échappement|échappement]] : `'\n'`, `'\t'`, `'\0'`. Un caractère accentué en UTF-8 occupe plusieurs `char` (voir [[Unicode]]).

## Dans le cours

[[4 - Cours complet]] l'utilise pour l'unité (`'c'` ou `'i'`) du programme de conversion cm/pouce, testée par un `switch`.

Voir aussi : [[Type primitif]].

Résumés : [[4 - Cours complet]]
