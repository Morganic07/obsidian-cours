---
type: concept
tags: [year4]
aliases: [pont d'un graphe]
matieres: [graph theory]
sources: ["[[2 - tree|Chp2 - tree]]"]
maj: 2026-11-08
---

Un pont est une arête $e$ telle que $G - e$ a une composante connexe de plus que $G$.

Le cours s'en sert pour montrer qu'un graphe connexe fini a un arbre couvrant : on retire une arête qui n'est pas un pont tant qu'il en reste ; le procédé termine car $E$ est fini. Le graphe obtenu est bien un arbre couvrant : il garde tous les sommets, reste connexe car on ne retire jamais un pont, et n'a plus de cycle car une arête d'un cycle n'est jamais un pont (complément, hors du cours).

**Caractérisation (complément, hors du cours)** : une arête est un pont si et seulement si elle n'appartient à aucun [[Cycle (graphe)|cycle]]. Si $e = uv$ est sur un cycle, le reste du cycle relie encore $u$ à $v$ après la suppression de $e$, donc la connexité est conservée ; réciproquement, si $G - e$ relie encore $u$ à $v$ par une [[Chaîne (graphe)|chaîne]], cette chaîne complétée par $e$ forme un cycle contenant $e$.

Conséquences :
- dans un [[Arbre (théorie des graphes)|arbre]], qui n'a aucun cycle, toute arête est un pont ;
- un graphe connexe dont toutes les arêtes sont des ponts n'a aucun cycle, c'est donc un arbre.

Les ponts sont les points fragiles d'un réseau : couper un pont isole une partie du graphe du reste.

Notion parente : [[Graphe connexe]]. Voir aussi : [[Arbre couvrant minimal]].

Résumés : [[2 - tree]]
