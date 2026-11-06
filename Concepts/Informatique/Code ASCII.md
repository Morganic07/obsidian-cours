---
type: concept
tags: [year2, year4]
aliases: [ASCII, American Standard Code for Information Interchange, Table ASCII]
matieres: [Operating System, C++]
sources: ["[[OS - chp 1]]", "[[Commandes Shell + explications]]", "[[Chp1 - basiques]]"]
maj: 2026-11-06
---

Correspondance entre nombres et caractères (American Standard Code for Information Interchange).

**En Operating System** : chaque touche du clavier a un code ASCII ; le processeur local du clavier convertit la touche en ASCII puis en binaire utilisable par le CPU. En Bash, `<` et `>` comparent des chaînes dans l'ordre alphabétique ASCII.

**En C** : le `char` est le support du code ASCII. L'ordinateur ne stocke que des nombres : `'A'` vaut 65 (01000001), `'B'` 66. Avec `%c`, `printf` affiche le symbole correspondant de la table.

Notion parente : [[Type primitif]]. Voir aussi : [[Contrôleur de périphérique]], [[Opérateur de comparaison]], [[Fonctions printf et scanf]].

Résumés : [[OS - chp 1 (résumé)]], [[Commandes Shell + explications (résumé)]], [[Chp1 - basiques (résumé)]]
