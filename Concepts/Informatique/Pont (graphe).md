---
type: concept
tags: [year4]
aliases: [pont d'un graphe]
matieres: [graph theory]
sources: ["[[2 - tree|Chp2 - tree]]"]
maj: 2026-11-07
---

Un pont est une arête $e$ telle que $G - e$ a une composante connexe de plus que $G$.

Le cours s'en sert pour montrer qu'un graphe connexe fini a un arbre couvrant : on retire une arête qui n'est pas un pont tant qu'il en reste ; le procédé termine car $E$ est fini.

Notion parente : [[Graphe connexe]]. Voir aussi : [[Arbre couvrant minimal]].

## Erreurs du cours

- [[2 - tree|Chp2 - tree]] démontre la proposition 6 (« Every finite connected graph has at least one spanning tree ») en s'arrêtant à la terminaison du procédé (vérifié sur l'image) ; il faut ajouter pourquoi le graphe obtenu est un arbre couvrant : il garde tous les sommets, reste connexe car on ne retire jamais un pont, et n'a plus de cycle car une arête d'un cycle n'est jamais un pont (complément, hors du cours).

Résumés : [[2 - tree]]
