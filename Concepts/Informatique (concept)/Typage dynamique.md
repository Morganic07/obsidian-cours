---
type: concept
tags: [year1]
aliases: [typé dynamiquement, dynamically typed]
sources: ["[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"]
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : un langage est typé dynamiquement quand le type est porté par les valeurs et vérifié pendant l'exécution, et non attaché aux [[Variable (programmation)|variables]] et vérifié à la compilation. On ne déclare pas le type d'une variable, et une même variable peut désigner successivement un entier puis une chaîne ; une opération incompatible (comme `"a" + 1` en Python) ne provoque une erreur qu'au moment où elle est exécutée. Il s'oppose au [[Typage statique]] du C, du C++ ou de Java.

## Dans le cours

Nommé dans AlgoID1 sans définition, comme caractéristique de Python (« Dynamically typed ») ; le cours montre `type(x)` et `isinstance(x, float)`.

Notion parente : [[Langage Python]]. Voir aussi : [[Type primitif]], [[Transtypage]].

Résumés : [[0 - diapo prof (résumé)]]
