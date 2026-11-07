---
type: concept
tags: [year1, year2, year3, year4]
aliases: [structures conditionnelles, instruction conditionnelle, selon le cas, Structure conditionnelle en Bash, if statement, if elif else, if else statement, instruction if Bash, instruction if, instruction switch, if else, else if, structures de contrôle, switch case]
matieres: [Algo Maths, Operating System, Java, C++]
sources: ["[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]", "[[Commandes Shell + explications (résumé)|Commandes Shell + explications]]", "[[DM Shell Scripting (résumé)|DM Shell Scripting]]", "[[Chp1 - Intro Java (résumé)|Chp1 - Intro Java]]", "[[chp2 - structures code (résumé)|chp2 - structures code]]"]
maj: 2026-11-06
---

Instruction qui exécute un bloc ou un autre selon la valeur d'une condition. Ce n'est pas une boucle.

**Pseudo-code et Python** (Algo Maths) : [[Opérateur de comparaison|opérateurs de comparaison]], `SI ... ALORS ... SINON ... FINSI`, et `SELON variable CAS ... DEFAUT ... FINSELON`, qui exécute telle suite d'instructions selon la valeur. Python : `if / elif / else`. Exercices : température de l'eau, année bissextile.

**Bash** (Operating System) : `if [ condition ] then ... elif [ condition ] then ... else ... fi`. Espaces obligatoires autour de `[` et `]`. `[ ]` sert aux comparaisons de chaînes, de fichiers et aux conditions simples ; `(( ))` aux expressions arithmétiques.

**Java** : `if` / `else`, et `switch` sur `char`, `byte`, `short`, `int`, avec `default` optionnel ; le cours dit les `break` optionnels.

**C++** : `if (condition1) {...} else if (condition2) {...} else {...}`. Le `switch (variable) { case valeur1 : ... break; ... default : ... }` évite les `if` imbriqués : une fois un `case` atteint, les instructions des `case` suivants s'exécutent aussi jusqu'au `break`, qu'il ne faut donc pas oublier. Les accolades sont facultatives pour une seule instruction.

Notion parente : [[Pseudo-code]]. Voir aussi : [[Boucle (programmation)]], [[Évaluation en court-circuit]], [[Opérateur logique]], [[Arithmétique en Bash]], [[Opérateur conditionnel]], [[Instruction vide]].

## À vérifier

- Le cours de Java affirme « ELSE IF N'EXISTE PAS EN JAVA », ce qui est faux (à corriger avant un examen). Sans `break`, l'exécution continue au cas suivant ; `switch` accepte aussi `String` et `enum`.

Résumés : [[AlgoID1 (résumé)]], [[Commandes Shell + explications (résumé)]], [[DM Shell Scripting (résumé)]], [[Chp1 - Intro Java (résumé)]], [[chp2 - structures code (résumé)]], [[Chp1 - basiques (résumé)]]
