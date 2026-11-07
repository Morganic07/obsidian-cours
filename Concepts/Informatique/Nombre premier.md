---
type: concept
tags:
  - year1
  - year2
aliases:
  - nombres premiers
  - prime number
  - prime numbers
  - test de primalité
sources:
  - "[[0 - Algo Maths|Cours 1 (Algo Maths)]]"
  - "[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"
  - "[[Raw/Year 2/Operating System/DM/DMs/DM Shell Scripting.docx|DM Shell Scripting]]"
  - "[[Raw/Year 2/Operating System/DM/DMs/Copy of 08 Processes-TP.docx|Copy of 08 Processes-TP]]"
maj: 2026-11-07
---

**Algo Maths** : interprétation géométrique avec des billes. Si l'on peut ranger $X$ billes en rectangle, $X$ n'est pas premier ; si la seule disposition est une ligne, il l'est (15 billes : $3 \times 5$ ; 7 billes : une ligne). Exercice Python d'AlgoID1 : compter les nombres premiers inférieurs ou égaux à $n$.

**Operating System** : propriété citée au DM, tout nombre non premier $n > 2$ admet un diviseur premier $p \le \sqrt{n}$ ; donc si $n$ n'a aucun diviseur entre 2 et $\sqrt{n}$, il est premier. D'où le test `for ((i=2; i*i<=n; i++))` pour afficher les 500 premiers nombres premiers, et le test `i*i <= num` du lab 7.

Voir aussi : [[Arithmétique en Bash]], [[Boucle (programmation)]].

## Erreurs du cours

- La version Python de [[Raw/Year 2/Operating System/DM/DMs/DM Shell Scripting.docx|DM Shell Scripting]] écrit `for i in range(2, int(NombreActuel**0.5)):` ; il faut `range(2, int(NombreActuel**0.5) + 1)`. La borne supérieure de `range` est exclue : pour 4, la boucle est vide (`range(2, 2)`) et pour 9 elle ne teste que 2 (`range(2, 3)`), si bien que 4 et 9 seraient jugés premiers. La version Bash du même DM (`i*i<=NombreActuel`) est juste.

Résumés : [[0 - Algo Maths|Cours 1 (Algo Maths)]], [[0 - diapo prof]]
