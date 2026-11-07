---
type: concept
tags:
  - year1
  - year2
  - year3
  - year4
aliases:
  - boucle TANTQUE
  - boucle POUR
  - boucle REPETER
  - boucle while
  - boucle for
  - Boucle en Bash
  - while loop
  - for loop
  - while true
  - boucle do-while
  - do-while
  - boucles for
  - boucles while
  - do while
  - do ... while
  - boucle infinie
matieres:
  - Algo Maths
  - Operating System
  - Java
  - C++
sources:
  - "[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"
  - "[[0 - Python|Python (Algo Maths)]]"
  - "[[8 - OS commandes sh|Commandes Shell + explications]]"
  - "[[Raw/Year 2/Operating System/DM/DMs/DM Shell Scripting.docx|DM Shell Scripting]]"
  - "[[3 - TP3|Cours TP3]]"
  - "[[1 - Intro Java|Chp1 - Intro Java]]"
  - "[[2 - structures code|chp2 - structures code]]"
maj: 2026-11-07
---

Structure qui répète un bloc d'instructions tant qu'une condition le demande.

**Pseudo-code et Python** (Algo Maths) : `TANTQUE` teste avant, `REPETER ... JUSQUACEQUE` teste après, `POUR i DE ... A ...` utilise un compteur qu'il ne faut pas modifier (`i ← i+1` à chaque tour). Python : `while`, `for ... in`, `break`, `continue`. L'examen de novembre 2022 fait chercher les erreurs d'une boucle `POUR` qui modifie son compteur.

**Bash** (Operating System) : `while [ condition ] do ... done` et `for (( initialisation; condition; compteur )) do ... done`. Exemple : afficher 1 à 10 avec `while [ $n -le 10 ]` ou `(( $n <= 10 ))` et `n=$(( n+1 ))` ou `(( n++ ))`. Les scripts de sauvegarde utilisent une boucle infinie `while true`.

**Java** : `while`, `do-while` (au moins une exécution), `for` (initialisation, condition, itération ; quand le nombre d'itérations est connu). `break` sort de la boucle, `continue` saute la fin de l'itération.

**C++** : `for (initialisation ; condition ; incrémentation)` ; l'initialisation a lieu une fois avant la boucle, la condition avant chaque tour, l'incrémentation après chaque tour. Avec `i = 0`, `i < 10`, `i = i + 1` : 10 tours, `i` de 0 à 9, puis 10 en sortie. `do { ... } while (condition);` exécute le bloc au moins une fois (le `;` final est obligatoire) ; `while (condition) { ... }` peut ne jamais l'exécuter.

Notion parente : [[Pseudo-code]]. Voir aussi : [[Fonction range (Python)]], [[Structure conditionnelle]], [[Commande sleep]], [[Sauvegarde de fichier]], [[Portée d'une variable]], [[Tableau (programmation)]], [[Instruction vide]].

Résumés : [[0 - diapo prof]], [[8 - OS commandes sh]], [[3 - TP3]], [[1 - Intro Java]], [[2 - structures code]], [[1 - basiques]]
