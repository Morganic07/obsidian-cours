---
type: concept
tags:
  - year4
aliases:
  - variable non définie
sources:
  - "[[1 - basiques|Chp1 - basiques]]"
  - "[[Raw/Year 4/C++/chp4 C++.pdf|chp4 C++.pdf]]"
maj: 2026-11-08
---

En C, `int y; printf("y = %d", y);` affiche selon le cours une « valeur aléatoire ». De même, les éléments d'un tableau ne sont pas initialisés à zéro.

**En C++** ([[4 - C++]]) : sans constructeur, les attributs `x` et `y` d'un objet ne sont pas initialisés et contiennent « une valeur indéterminée (n'importe quoi) ». Le [[Constructeur (programmation)|constructeur par défaut]] sert à créer chaque objet dans un état connu. Piège relevé dans [[4 - Prise de note]] : `int x = 0;` écrit dans le constructeur déclare une variable locale, et l'attribut reste non initialisé.

Notion parente : [[Langage C]]. Voir aussi : [[Tableau (programmation)]].

Résumés : [[1 - basiques]], [[2 - structures code]], [[4 - C++]], [[4 - Prise de note]]
