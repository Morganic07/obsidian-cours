---
type: concept
tags: [year1, year4]
aliases: [algorithmes gloutons, algo glouton, algos gloutons, greedy algorithm]
matieres: [Algo Maths, graph theory]
sources: ["[[Raw/Year 1/Algo Maths/explications DM d'algo .docx|explications DM d'algo]]", "[[2 - tree|Chp2 - tree]]"]
maj: 2026-11-07
---

Un algorithme glouton prend à chaque étape la meilleure décision locale, sans revenir dessus, jusqu'à avoir construit une solution complète. Il n'est optimal que si une solution optimale contient des solutions optimales des sous-problèmes (propriété que le cours invoque sans la démontrer).

Exemples du cours :
- [[Problème du sac à dos]] : trois variantes, qui ne diffèrent que par la clé de tri (valeur décroissante, poids croissant, densité décroissante). Aucune n'est optimale.
- [[Arbre couvrant minimal]] : l'[[Algorithme de Kruskal]] est présenté comme la solution gloutonne, l'énumération des arbres étant exponentielle, et donne, lui, un arbre de poids minimal.

## Erreurs du cours

- [[Raw/Year 1/Algo Maths/explications DM d'algo .docx|explications DM d'algo]] écrit, dans le bloc encadré de `glouton_valeur`, « objets = sorted(objets, key=lambda x: x.v) » ; il faut « objets = sorted(objets, key=lambda x: x.v, reverse = True) » (valeur décroissante), comme dans la version commentée juste en dessous.

Résumés : [[2 - tree]]
