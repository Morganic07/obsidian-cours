---
type: concept
tags:
  - year2
  - year4
aliases:
  - Opérateurs de comparaison en Bash
  - integer comparison operators
  - string comparison operators
  - opérateurs de comparaison
  - XOR logique
  - triple égalité
matieres:
  - Operating System
  - C++
sources:
  - "[[8 - OS commandes sh (résumé)|Commandes Shell + explications]]"
  - "[[Raw/Year 2/Operating System/DM/DMs/DM Shell Scripting.docx|DM Shell Scripting]]"
  - "[[1 - basiques (résumé)|Chp1 - basiques]]"
  - "[[2 - structures code (résumé)|chp2 - structures code]]"
maj: 2026-11-06
---

**En Bash** (Operating System) :

- entiers dans `[ ]` : `-eq`, `-ne`, `-gt`, `-ge`, `-lt`, `-le` ; dans `(( ))` : `<`, `<=`, `>`, `>=` ([[Arithmétique en Bash]]) ;
- chaînes : `=` ou `==`, `!=`, `<` et `>` (ordre [[Code ASCII|ASCII]], dans `[[ ]]`), `-z` (chaîne vide).

Ne pas confondre : `=`/`!=` pour les chaînes, `-eq`/`-ne` pour les nombres.

**En C** : `==`, `!=`, `>`, `>=`, `<`, `<=`, `&&` (ET logique), `||` (OU logique), `!` (NOT logique), `^` (donné par le cours comme XOR logique). Une condition vraie vaut 1 et fausse 0 : `a == b == c` est lu `(a == b) == c`, donc avec `a = b = c = 5` on teste `1 == 5`, faux. Le cours propose `if (a == b && b == c)`. Piège associé : `if (a = 3)` affecte au lieu de comparer.

Notion parente : [[Structure conditionnelle]]. Voir aussi : [[Évaluation en court-circuit]], [[Opérateur logique]].

## À vérifier

À corriger avant un examen (compléments du résumé) :

- `if (a=3)` ne teste pas si « a peut prendre la valeur 3 » : il affecte 3 et vaut 3, donc vrai ;
- `if (((a==b) == 1) == (b==c))` n'équivaut pas à `a == b && b == c` ;
- `^` est un OU exclusif bit à bit : il n'y a pas de XOR logique en C.

Résumés : [[8 - OS commandes sh (résumé)]], [[1 - basiques (résumé)]], [[2 - structures code (résumé)]]
