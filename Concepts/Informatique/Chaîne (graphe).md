---
type: concept
tags: [year4]
aliases: [chaîne élémentaire, chaîne simple, simple chain, longueur d'une chaîne]
sources: ["[[Chp 1 - Undirected graph (résumé)|Chp 1 - Undirected graph]]", "[[Graph - Python (résumé)|Graph - Python]]"]
maj: 2026-11-06
---

Dans un graphe non orienté, une chaîne est une suite $(v_0, e_1, v_1, \ldots, e_p, v_p)$ alternant sommets et arêtes ; $p$ est sa longueur.

- **Chaîne simple** : ses arêtes sont distinctes.
- **Chaîne élémentaire** : ses sommets sont distincts. Une chaîne élémentaire est simple.

Le TP Python écrit les fonctions `isChain`, `estChaineElementaire` et `isSimpleChain`.

Notion parente : [[Graphe non orienté]]. Voir aussi : [[Cycle (graphe)]], [[Graphe connexe]].

## À vérifier

La chaîne $C_2$ de l'exemple du cours n'en est pas une ($e_1$ relie $v_1$ et $v_2$) : probablement un contre-exemple (en rouge), image non ouverte.

Résumés : [[Chp 1 - Undirected graph (résumé)]], [[Graph - Python (résumé)]]
