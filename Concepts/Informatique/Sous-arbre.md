---
type: concept
tags: [year4]
aliases: [sous-arbres, subtree, sous-arbre enraciné]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/Chp2 - tree revisions années précédentes.pdf|Chp2 - tree revisions années précédentes.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : dans un [[Arborescence (graphe)|arbre enraciné]], le **sous-arbre** enraciné en un nœud $u$ est l'arbre formé de $u$ et de tous ses descendants, avec les arcs qui les relient ; $u$ en est la racine. Les sous-arbres des fils de la racine sont les sous-arbres de l'arbre : c'est sur eux que porte la définition [[Récursivité|récursive]] d'un arbre (une racine reliée à des sous-arbres disjoints) et que s'appellent les algorithmes récursifs (parcours, calcul de la [[Hauteur d'un arbre|hauteur]] ou de la taille, recherche dans un ABR). Dans un [[Arbre binaire|arbre binaire]], on distingue le sous-arbre gauche et le sous-arbre droit.

## Dans le cours

[[2 - tree revisions années précédentes]] s'en sert pour définir l'ancêtre et le descendant (« $w$ est dans l'arbre enraciné à $u$ »), les parcours (« parcours préfixe des sous-arbres de gauche à droite ») et l'[[Arbre binaire de recherche|arbre binaire de recherche]] (« tout sous-arbre de $a$ est un ABR »).

Voir aussi : [[Vocabulaire des arbres]], [[Arbre (théorie des graphes)]], [[Sous-graphe]].

Résumés : [[2 - tree revisions années précédentes]]
