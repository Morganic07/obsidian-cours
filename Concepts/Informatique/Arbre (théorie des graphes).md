---
type: concept
tags: [year2, year4]
aliases: [arbre (graphe), propriétés des arbres, acyclic connected graph]
matieres: [Algo, graph theory]
sources: ["[[Raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres.pdf]]", "[[2 - tree|Chp2 - tree]]"]
maj: 2026-11-08
---

Graphe non orienté connexe et sans cycle.

**graph theory** : un arbre est simple, et toute chaîne élémentaire est un arbre. Exemples : chaîne, étoile, deux nœuds internes reliés.

**Algo** : pour un graphe non orienté $G=(S,A)$, les énoncés suivants sont équivalents :

- $G$ est un arbre ;
- deux sommets quelconques sont reliés par un unique chemin élémentaire ;
- $G$ est acyclique et $|A|=|S|-1$ ;
- $G$ est acyclique, mais l'ajout d'une arête quelconque crée un cycle.

**Autres caractérisations (complément, hors du cours)** : sont aussi équivalents à « $G$ est un arbre » :

- $G$ est connexe et $|A| = |S| - 1$ ;
- $G$ est connexe et chacune de ses arêtes est un [[Pont (graphe)|pont]] (la retirer déconnecte le graphe).

Un arbre est donc à la fois un graphe connexe minimal (on ne peut retirer aucune arête sans le déconnecter) et un graphe acyclique maximal (on ne peut ajouter aucune arête sans créer de cycle). Tout graphe connexe contient un arbre couvrant, obtenu en retirant des arêtes de cycles tant qu'il en reste ([[Arbre couvrant minimal]]). Un graphe acyclique non connexe est une [[Forêt (graphe)|forêt]], dont chaque composante connexe est un arbre.

**Feuilles (complément, hors du cours)** : tout arbre à au moins 2 sommets a au moins deux feuilles (sommets de degré 1, voir [[Degré d'un sommet]]) : les deux extrémités d'une plus longue [[Chaîne (graphe)|chaîne élémentaire]] conviennent, car une arête de plus en partant d'une extrémité prolongerait la chaîne ou fermerait un cycle. Retirer une feuille et son arête laisse un arbre à $n - 1$ sommets, ce qui fonde les démonstrations par récurrence sur les arbres (par exemple $|A| = |S| - 1$).

**Pourquoi un arbre est simple (complément, hors du cours)** : une boucle est un cycle de longueur 1 et deux arêtes parallèles forment un cycle de longueur 2 ; un graphe acyclique n'a donc ni l'une ni l'autre, et il est [[Graphe simple|simple]].

Comme structure de données, l'arbre est non linéaire, naturellement récursif et hiérarchique (systèmes de fichiers, XML, sites web).

Notion parente : [[Graphe non orienté]]. Voir aussi : [[Cycle (graphe)]], [[Arborescence (graphe)]], [[Arbre binaire]], [[Arbre couvrant minimal]], [[Forêt (graphe)]], [[Vocabulaire des arbres]], [[Pont (graphe)]], [[Degré d'un sommet]], [[Graphe simple]].

Résumés : [[3 - Arbres]], [[2 - tree]]
