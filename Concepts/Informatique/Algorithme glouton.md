---
type: concept
tags: [year1, year4]
aliases: [algorithmes gloutons, algo glouton, algos gloutons, greedy algorithm]
matieres: [Algo Maths, graph theory]
sources: ["[[Raw/Year 1/Algo Maths/explications DM d'algo .docx|explications DM d'algo]]", "[[2 - tree|Chp2 - tree]]"]
maj: 2026-11-12
---

Un algorithme glouton prend à chaque étape la meilleure décision locale, sans revenir dessus, jusqu'à avoir construit une solution complète. Il n'est optimal que si une solution optimale contient des solutions optimales des sous-problèmes (propriété que le cours invoque sans la démontrer).

Exemples du cours :
- [[Problème du sac à dos]] : trois variantes, qui ne diffèrent que par la clé de tri (valeur décroissante, poids croissant, densité décroissante). Aucune n'est optimale. Pour la valeur décroissante, le tri s'écrit `objets = sorted(objets, key=lambda x: x.v, reverse=True)`. [[Erreurs du cours#^e-algorithme-glouton|✎]]
- [[Arbre couvrant minimal]] : l'[[Algorithme de Kruskal]] est présenté comme la solution gloutonne, l'énumération des arbres étant exponentielle, et donne, lui, un arbre de poids minimal.

En complément de [[4 - dijkstra]] et [[4 - bellman ford]] (Graph theory), l'[[Algorithme de Dijkstra|algorithme de Dijkstra]] est un autre algorithme glouton : il fixe à chaque étape la distance du sommet non traité le plus proche, sans y revenir, ce qui n'est juste qu'avec des poids positifs ou nuls ; l'[[Algorithme de Bellman-Ford|algorithme de Bellman-Ford]], par programmation dynamique, peut au contraire améliorer une distance jusqu'à la fin.

Résumés : [[2 - tree]], [[4 - dijkstra]], [[4 - bellman ford]]
