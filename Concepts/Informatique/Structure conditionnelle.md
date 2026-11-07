---
type: concept
tags:
  - year1
  - year2
  - year3
  - year4
aliases:
  - structures conditionnelles
  - instruction conditionnelle
  - selon le cas
  - Structure conditionnelle en Bash
  - if statement
  - if elif else
  - if else statement
  - instruction if Bash
  - instruction if
  - instruction switch
  - if else
  - else if
  - structures de contrôle
  - switch case
matieres:
  - Algo Maths
  - Operating System
  - Java
  - C++
sources:
  - "[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"
  - "[[8 - OS commandes sh|Commandes Shell + explications]]"
  - "[[Raw/Year 2/Operating System/DM/DMs/DM Shell Scripting.docx|DM Shell Scripting]]"
  - "[[1 - Intro Java|Chp1 - Intro Java]]"
  - "[[2 - structures code|chp2 - structures code]]"
maj: 2026-11-07
---

Instruction qui exécute un bloc ou un autre selon la valeur d'une condition. Ce n'est pas une boucle.

**Pseudo-code et Python** (Algo Maths) : [[Opérateur de comparaison|opérateurs de comparaison]], `SI ... ALORS ... SINON ... FINSI`, et `SELON variable CAS ... DEFAUT ... FINSELON`, qui exécute telle suite d'instructions selon la valeur. Python : `if / elif / else`. Exercices : température de l'eau, année bissextile.

**Bash** (Operating System) : `if [ condition ] then ... elif [ condition ] then ... else ... fi`. Espaces obligatoires autour de `[` et `]`. `[ ]` sert aux comparaisons de chaînes, de fichiers et aux conditions simples ; `(( ))` aux expressions arithmétiques.

**Java** : `if` / `else`, et `switch` sur `char`, `byte`, `short`, `int`, avec `default` optionnel ; le cours dit les `break` optionnels.

**C++** : `if (condition1) {...} else if (condition2) {...} else {...}`. Le `switch (variable) { case valeur1 : ... break; ... default : ... }` évite les `if` imbriqués : une fois un `case` atteint, les instructions des `case` suivants s'exécutent aussi jusqu'au `break`, qu'il ne faut donc pas oublier. Les accolades sont facultatives pour une seule instruction.

Notion parente : [[Pseudo-code]]. Voir aussi : [[Boucle (programmation)]], [[Évaluation en court-circuit]], [[Opérateur logique]], [[Arithmétique en Bash]], [[Opérateur conditionnel]], [[Instruction vide]].

## Erreurs du cours

- [[1 - Intro Java|Chp1 - Intro Java]] écrit « ELSE IF N'EXISTE PAS EN JAVA » ; il faut « `else if` existe en Java », comme en C++ : `if (...) {...} else if (...) {...} else {...}`.

Résumés : [[0 - diapo prof]], [[8 - OS commandes sh]], [[1 - Intro Java]], [[2 - structures code]], [[1 - basiques]]
