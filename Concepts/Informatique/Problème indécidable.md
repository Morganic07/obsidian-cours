---
type: concept
tags:
  - year1
aliases:
  - indécidable
  - indécidabilité
  - problème de l'arrêt
  - halting problem
  - undecidable problem
matieres:
  - Algo Maths
sources:
  - "[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"
  - "[[0 - diapo prof]]"
maj: 2026-11-08
---

**Définition** (d'après [[0 - diapo prof]]) : le cours donne le sens du mot sur l'exemple de la [[Terminaison d'un algorithme|terminaison]] : dire que la terminaison est un problème indécidable, c'est dire qu'« il n'existe pas d'algorithme qui a pour donnée un programme et obtient comme résultat *true* si et seulement si ce programme termine ».

## Dans le cours

AlgoID1 l'affirme à propos de la terminaison (« La terminaison est un problème indécidable ! »), puis explique ce que cela veut dire, par la phrase reprise en définition ci-dessus.

## Compléments (complément, hors du cours)

- **Définition générale** : un problème de décision (question à réponse oui/non sur une entrée) est indécidable s'il n'existe aucun algorithme qui, sur *toutes* les entrées, se termine et donne la bonne réponse.
- **Le problème de l'arrêt** est l'exemple fondateur : Alan Turing a démontré son indécidabilité en 1936.
- **Idée de la preuve**, par l'[[Raisonnement par l'absurde|absurde]] : supposons qu'un programme `arret(P, x)` rende *true* si `P` s'arrête sur l'entrée `x`, *false* sinon. On écrit `paradoxe(P)` : si `arret(P, P)` vaut *true*, boucler indéfiniment ; sinon, s'arrêter. Alors `paradoxe(paradoxe)` s'arrête si et seulement s'il ne s'arrête pas : contradiction, donc `arret` n'existe pas.
- **Conséquence pratique** : aucun outil ne peut détecter à coup sûr toutes les boucles infinies ; on prouve la terminaison programme par programme, par un variant (voir [[Invariant de boucle]]).

Notion parente : [[Terminaison d'un algorithme]].

Résumés : [[0 - diapo prof]]
