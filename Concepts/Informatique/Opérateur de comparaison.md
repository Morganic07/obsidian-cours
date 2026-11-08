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
  - "[[8 - OS commandes sh|Commandes Shell + explications]]"
  - "[[Raw/Year 2/Operating System/DM/DMs/DM Shell Scripting.docx|DM Shell Scripting]]"
  - "[[1 - basiques|Chp1 - basiques]]"
  - "[[2 - structures code|chp2 - structures code]]"
maj: 2026-11-08
---

**En Bash** (Operating System) :

- entiers dans `[ ]` : `-eq`, `-ne`, `-gt`, `-ge`, `-lt`, `-le` ; dans `(( ))` : `<`, `<=`, `>`, `>=` ([[Arithmétique en Bash]]) ;
- chaînes : `=` ou `==`, `!=`, `<` et `>` (ordre [[Code ASCII|ASCII]], dans `[[ ]]`), `-z` (chaîne vide).

Ne pas confondre : `=`/`!=` pour les chaînes, `-eq`/`-ne` pour les nombres.

**En C** : `==`, `!=`, `>`, `>=`, `<`, `<=`, `&&` (ET logique), `||` (OU logique), `!` (NOT logique), `^` (OU exclusif bit à bit ; le C n'a pas de XOR logique, on écrit par exemple `(a != 0) != (b != 0)`). [[Erreurs du cours#^e-operateur-de-comparaison|✎]] Une condition vraie vaut 1 et fausse 0 : `a == b == c` est lu `(a == b) == c`, donc avec `a = b = c = 5` on teste `1 == 5`, faux. Le cours propose `if (a == b && b == c)` ; la forme `if ( ((a==b) == 1) == (b==c) )` ne lui est pas équivalente, car elle est aussi vraie quand $a \ne b$ et $b \ne c$ (elle teste alors `0 == 0`). [[Erreurs du cours#^e-operateur-de-comparaison|✎]] Piège associé : `if (a = 3)` ne teste rien, il affecte 3 à `a` et vaut 3, donc la condition est toujours vraie. [[Erreurs du cours#^e-operateur-de-comparaison|✎]]

Notion parente : [[Structure conditionnelle]]. Voir aussi : [[Évaluation en court-circuit]], [[Opérateur logique]].

Résumés : [[8 - OS commandes sh]], [[1 - basiques]], [[2 - structures code]]
