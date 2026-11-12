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
  - boucle for-each
  - for-each
  - boucle étiquetée
matieres:
  - Algo Maths
  - Operating System
  - Java
  - C／C++
sources:
  - "[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"
  - "[[0 - Python|Python (Algo Maths)]]"
  - "[[8 - OS commandes sh|Commandes Shell + explications]]"
  - "[[Raw/Year 2/Operating System/DM/DMs/DM Shell Scripting.docx|DM Shell Scripting]]"
  - "[[3 - TP3|Cours TP3]]"
  - "[[1 - Intro Java|Chp1 - Intro Java]]"
  - "[[2 - structures code|chp2 - structures code]]"
  - "[[Raw/Year 3/Java/Chp1 : Intro Java.docx|Chp1 - Intro Java]]"
maj: 2026-11-12
---

Structure qui répète un bloc d'instructions tant qu'une condition le demande.

**Pseudo-code et Python** (Algo Maths) : `TANTQUE` teste avant, `REPETER ... JUSQUACEQUE` teste après, `POUR i DE ... A ...` utilise un compteur qu'il ne faut pas modifier (`i ← i+1` à chaque tour). Python : `while`, `for ... in`, `break`, `continue`. L'examen de novembre 2022 fait chercher les erreurs d'une boucle `POUR` qui modifie son compteur.

**Bash** (Operating System) : `while [ condition ] do ... done` et `for (( initialisation; condition; compteur )) do ... done`. Exemple : afficher 1 à 10 avec `while [ $n -le 10 ]` ou `(( $n <= 10 ))` et `n=$(( n+1 ))` ou `(( n++ ))`. Les scripts de sauvegarde utilisent une boucle infinie `while true`.

**Java** : `while`, `do-while` (au moins une exécution), `for` (initialisation, condition, itération ; quand le nombre d'itérations est connu). `break` sort de la boucle, `continue` saute la fin de l'itération.

Complément (hors du cours) : `for (init; cond; iter) corps` équivaut à `init; while (cond) { corps; iter; }` (à `continue` près, qui dans un `for` exécute encore `iter`) ; une variable déclarée dans l'en-tête n'existe que dans la boucle. La boucle **for-each** (depuis Java 5) parcourt un tableau ou une collection : `for (int v : tableau) { ... }`, où `v` reçoit une copie de chaque élément (la modifier ne change pas le tableau). Dans des boucles imbriquées, `break` et `continue` n'agissent que sur la boucle la plus intérieure ; `break etiquette;` sort d'une boucle extérieure étiquetée :

```java
externe:
for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
        if (t[i][j] == cible) break externe;   // quitte les deux boucles
    }
}
```

**C++** : `for (initialisation ; condition ; incrémentation)` ; l'initialisation a lieu une fois avant la boucle, la condition avant chaque tour, l'incrémentation après chaque tour. Avec `i = 0`, `i < 10`, `i = i + 1` : 10 tours, `i` de 0 à 9, puis 10 en sortie. `do { ... } while (condition);` exécute le bloc au moins une fois (le `;` final est obligatoire) ; `while (condition) { ... }` peut ne jamais l'exécuter.

Notion parente : [[Pseudo-code]]. Voir aussi : [[Fonction range (Python)]], [[Structure conditionnelle]], [[Commande sleep]], [[Sauvegarde de fichier]], [[Portée d'une variable]], [[Tableau (programmation)]], [[Instruction vide]].

## Dans le cours

**C++** ([[4 - Cours complet]]) : `while` (et `do … while`) et `for`, illustrés par la table des carrés de l'[[EDSAC]]. Dangers : variable de contrôle non initialisée, oubli de l'incrémentation (boucle infinie ; le polycopié déconseille `while(1)`). `for` regroupe initialisation, condition et incrémentation sur une ligne ; il existe toujours un `while` équivalent, et on n'utilise `while` que lorsque cette forme ne s'applique pas.

- [[tp2]] : le dernier programme (2.10) affiche les termes d'une suite arithmétique et leur somme avec une boucle `for(int n=1; n<=nmax; n++)`.
- [[tp3]] : en complément, le minimum provisoire de trois nombres se généralise à un tableau avec une boucle.
- [[tp4]] : TP sur la boucle `for` : compteurs, sortie anticipée avec `break`, accumulateurs, [[Boucle imbriquée|boucles imbriquées]] pour dessiner des motifs.
- [[tp5]] : boucles `while` et `do … while` sur des problèmes d'arithmétique ; oublier `i = i+1` donne une boucle infinie ; boucles imbriquées pour lister nombres premiers et nombres parfaits.
- [[tp7]] : remplissage et parcours d'un tableau avec une boucle `for`.
- [[td listes chaînées]] : parcours d'une liste chaînée par une boucle `while (actuel != NULL)`.
- [[formation C++]] : le programme 3-boucles montre `for`, `while` et `do … while` en C++ ; `do … while` s'exécute au moins une fois.

Résumés : [[0 - diapo prof]], [[8 - OS commandes sh]], [[3 - TP3]], [[1 - Intro Java]], [[2 - structures code]], [[1 - basiques]], [[4 - Cours complet]]
