---
type: concept
aliases: [algorithmes gloutons, algo glouton, algos gloutons, greedy algorithm]
matieres: [Algo Maths, graph theory]
sources: ["[[explications DM d'algo]]", "[[Chp2 - tree]]"]
maj: 2026-11-05
---

Un algorithme glouton prend à chaque étape la meilleure décision locale, sans revenir dessus, jusqu'à avoir construit une solution complète. Il n'est optimal que si une solution optimale contient des solutions optimales des sous-problèmes (propriété que le cours invoque sans la démontrer).

Exemples du cours :
- [[Problème du sac à dos]] : trois variantes, qui ne diffèrent que par la clé de tri (valeur décroissante, poids croissant, densité décroissante). Aucune n'est optimale.
- [[Arbre couvrant minimal]] : l'algorithme de Kruskal est glouton et, lui, donne un arbre de poids minimal.

Résumés : [[explications DM d'algo (résumé)]], [[Chp2 - tree (résumé)]]
