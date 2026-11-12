---
type: concept
tags: [year1, year4]
aliases: [division entière, quotient et reste, DIV et MOD]
matieres: [Algo Maths]
sources: ["[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"]
maj: 2026-11-12
---

Opérateurs `DIV` et `MOD` sur les `ENTIER` du pseudo-code (en Python : `//` et `%`).

Exemples d'AlgoID1 : décomposition d'une somme en billets et pièces, conversion de secondes en heures, minutes et secondes, procédure `divisionEntiere(E a, b, S q, r)` par soustractions successives. Le TD3 calcule le quotient et le reste par récursivité.

Voir aussi : [[Récursivité]], [[Polynôme]] (division euclidienne de polynômes en Outil Maths).

## Dans le cours

**C++** ([[4 - Cours complet]]) : la division de deux entiers est une division euclidienne, « une division ENTIÈRE » (`10 / 3` vaut 3, `10 % 3` vaut 1) ; pour une division réelle, il faut qu'un des opérandes soit réel (`valeur / 3.0`). C'est le piège du calcul de moyenne de l'exercice 3.

- [[tp2]] : `(note1 + note2) / 2` entre `int` donne une moyenne tronquée (`27 / 2` vaut 13) ; écrire `/ 2.0` pour une division réelle (2.3).
- [[tp3]] : parité testée par le reste `%` (3.7), puis par `nombre/2*2 == nombre` (3.9), qui repose sur la troncature du quotient.
- [[tp5]] : `nombre % i == 0` détecte les diviseurs dans les tests de [[Nombre premier|nombre premier]] et de [[Nombre parfait|nombre parfait]].
- [[tp6]] : `4/3` vaut 1 dans le volume de la sphère ; il faut `4.0/3.0`.
- [[tp7]] : `compteur/5` tronquait la moyenne d'un tableau (7.3), corrigé en `compteur/5.0f` ; en C, `-3 % 2` vaut `-1` (quotient tronqué vers zéro depuis C99), d'où le test d'imparité `% 2 != 0`.

Résumés : [[0 - diapo prof]], [[4 - Cours complet]]
