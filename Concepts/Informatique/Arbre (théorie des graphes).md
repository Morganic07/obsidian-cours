---
type: concept
tags: [year2, year4]
aliases: [arbre (graphe), propriétés des arbres, acyclic connected graph]
matieres: [Algo, graph theory]
sources: [".raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf", "[[Chp2 - tree]]"]
maj: 2026-11-06
---

Graphe non orienté connexe et sans cycle.

**graph theory** : un arbre est simple, et toute chaîne élémentaire est un arbre. Exemples : chaîne, étoile, deux nœuds internes reliés.

**Algo** : pour un graphe non orienté $G=(S,A)$, les énoncés suivants sont équivalents :

- $G$ est un arbre ;
- deux sommets quelconques sont reliés par un unique chemin élémentaire ;
- $G$ est acyclique et $|A|=|S|-1$ ;
- $G$ est acyclique, mais l'ajout d'une arête quelconque crée un cycle.

Comme structure de données, l'arbre est non linéaire, naturellement récursif et hiérarchique (systèmes de fichiers, XML, sites web).

Notion parente : [[Graphe non orienté]]. Voir aussi : [[Cycle (graphe)]], [[Arborescence (graphe)]], [[Arbre binaire]], [[Arbre couvrant minimal]], [[Forêt (graphe)]], [[Vocabulaire des arbres]].

Résumés : [[Chapitre3-Arbres (résumé)]], [[Chp2 - tree (résumé)]]
