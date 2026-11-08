---
type: concept
tags:
  - year2
  - year4
aliases:
  - ASCII
  - American Standard Code for Information Interchange
  - Table ASCII
matieres:
  - Operating System
  - C++
sources:
  - "[[1 - OS|OS - chp 1]]"
  - "[[8 - OS commandes sh|Commandes Shell + explications]]"
  - "[[1 - basiques|Chp1 - basiques]]"
maj: 2026-11-06
---

Correspondance entre nombres et caractères (American Standard Code for Information Interchange).

**En Operating System** : le processeur local du clavier envoie pour chaque touche un code de touche (*scan code*, ou code d'usage USB HID), que le pilote du système d'exploitation convertit en caractère, par exemple en code ASCII. [[Erreurs du cours#^e-code-ascii|✎]] En Bash, `<` et `>` comparent des chaînes dans l'ordre alphabétique ASCII.

**En C** : le `char` est le support du code ASCII. L'ordinateur ne stocke que des nombres : `'A'` vaut 65 (01000001), `'B'` 66. Avec `%c`, `printf` affiche le symbole correspondant de la table.

Notion parente : [[Type primitif]]. Voir aussi : [[Contrôleur de périphérique]], [[Opérateur de comparaison]], [[Fonctions printf et scanf]].

Résumés : [[1 - OS]], [[8 - OS commandes sh]], [[1 - basiques]]
