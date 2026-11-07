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
maj: 2026-11-07
---

**En Bash** (Operating System) :

- entiers dans `[ ]` : `-eq`, `-ne`, `-gt`, `-ge`, `-lt`, `-le` ; dans `(( ))` : `<`, `<=`, `>`, `>=` ([[Arithmétique en Bash]]) ;
- chaînes : `=` ou `==`, `!=`, `<` et `>` (ordre [[Code ASCII|ASCII]], dans `[[ ]]`), `-z` (chaîne vide).

Ne pas confondre : `=`/`!=` pour les chaînes, `-eq`/`-ne` pour les nombres.

**En C** : `==`, `!=`, `>`, `>=`, `<`, `<=`, `&&` (ET logique), `||` (OU logique), `!` (NOT logique), `^` (donné par le cours comme XOR logique). Une condition vraie vaut 1 et fausse 0 : `a == b == c` est lu `(a == b) == c`, donc avec `a = b = c = 5` on teste `1 == 5`, faux. Le cours propose `if (a == b && b == c)`. Piège associé : `if (a = 3)` affecte au lieu de comparer.

Notion parente : [[Structure conditionnelle]]. Voir aussi : [[Évaluation en court-circuit]], [[Opérateur logique]].

## Erreurs du cours

- [[1 - basiques|Chp1 - basiques]] écrit que `if (a=3)` « test si a peut prendre la valeur 3, retour 1 si oui et 0 si non » ; il faut : `a = 3` affecte 3 à `a` et vaut 3, donc la condition est toujours vraie (d'où l'affichage de « bonjour »).
- Le même chapitre propose `if ( ((a==b) == 1) == (b==c) )` comme équivalent de `a == b && b == c` ; il faut `if (a == b && b == c)` seul : la première forme est aussi vraie quand $a \ne b$ et $b \ne c$ (elle teste alors `0 == 0`).
- [[2 - structures code|chp2 - structures code]] donne `^` comme « XOR logique » ; il faut « OU exclusif bit à bit » : le C n'a pas d'opérateur XOR logique (on écrit par exemple `(a != 0) != (b != 0)`).

Résumés : [[8 - OS commandes sh]], [[1 - basiques]], [[2 - structures code]]
