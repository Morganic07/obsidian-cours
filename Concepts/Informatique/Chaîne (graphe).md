---
type: concept
tags:
  - year4
aliases:
  - chaîne élémentaire
  - chaîne simple
  - simple chain
  - longueur d'une chaîne
sources:
  - "[[1 - Undirected graph|Chp 1 - Undirected graph]]"
  - "[[0 - Graph - Python|Graph - Python]]"
maj: 2026-11-07
---

Dans un graphe non orienté, une chaîne est une suite $(v_0, e_1, v_1, \ldots, e_p, v_p)$ alternant sommets et arêtes ; $p$ est sa longueur.

Exemple du cours : $C_1 = (v_2, e_2, v_3, e_3, v_2, e_4, v_4, e_6, v_4)$, écrite en vert, est une chaîne ; $C_2 = (v_2, e_2, v_3, e_3, v_2, e_4, v_4, e_1, v_1)$, écrite en rouge, n'en est pas une, car $e_1$ relie $v_1$ et $v_2$, pas $v_4$ et $v_1$.

- **Chaîne simple** : ses arêtes sont distinctes.
- **Chaîne élémentaire** : ses sommets sont distincts. Une chaîne élémentaire est simple.

Le TP Python écrit les fonctions `isChain`, `estChaineElementaire` et `isSimpleChain`.

Notion parente : [[Graphe non orienté]]. Voir aussi : [[Cycle (graphe)]], [[Graphe connexe]].

Résumés : [[1 - Undirected graph]], [[0 - Graph - Python]]
