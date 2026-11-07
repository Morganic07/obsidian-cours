---
type: concept
tags: [year1, year4]
aliases: [algorithmes gloutons, algo glouton, algos gloutons, greedy algorithm]
matieres: [Algo Maths, graph theory]
sources: ["[[explications DM d'algo (résumé)|explications DM d'algo]]", "[[chp 2 - tree (résumé)|Chp2 - tree]]"]
maj: 2026-11-06
---

Un algorithme glouton prend à chaque étape la meilleure décision locale, sans revenir dessus, jusqu'à avoir construit une solution complète. Il n'est optimal que si une solution optimale contient des solutions optimales des sous-problèmes (propriété que le cours invoque sans la démontrer).

Exemples du cours :
- [[Problème du sac à dos]] : trois variantes, qui ne diffèrent que par la clé de tri (valeur décroissante, poids croissant, densité décroissante). Aucune n'est optimale.
- [[Arbre couvrant minimal]] : l'[[Algorithme de Kruskal]] est présenté comme la solution gloutonne, l'énumération des arbres étant exponentielle, et donne, lui, un arbre de poids minimal.

## À vérifier

Le bloc encadré de `glouton_valeur` trie sans `reverse=True` (ordre croissant), contrairement au texte. La note de l'étudiant dit tenir son code de ChatGPT et met en garde : fiabilité faible.

Résumés : [[explications DM d'algo (résumé)]], [[chp 2 - tree (résumé)]]
