---
type: concept
tags: [year2, year4]
aliases: [degree of a vertex, sommet pendant]
matieres: [Algo, graph theory]
sources: ["[[Raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres.pdf]]", "[[1 - Undirected graph|Chp 1 - Undirected graph]]", "[[4 - oriented graphs|chp4 - oriented graphs]]"]
maj: 2026-11-08
---

Nombre d'arêtes incidentes à un sommet. Le chapitre 1 l'utilise pour les graphes $k$-réguliers ([[Graphe régulier]]) et complets ([[Graphe complet]], chaque sommet de degré $n - 1$) ; le TP Python le calcule avec une fonction `degre`. Le chapitre 1 emploie $d(v)$ sans le définir, et énonce : si $G$ est $k$-régulier, alors $k \cdot \text{card}(V) = 2 \cdot \text{card}(E)$. Cette relation suppose qu'une boucle compte deux fois dans le degré de son sommet (convention usuelle, complément, hors du cours).

**Graphe orienté** (chapitre 4) : degré entrant $d^-(v)$ (nombre d'arcs entrants) et degré sortant $d^+(v)$ (nombre d'arcs sortants), avec $\sum_v d^+(v) = \sum_v d^-(v) = |A|$, chaque arc comptant une fois dans chaque somme.

**Algo** ([[3 - Arbres]]) : un sommet de degré 0 est un sommet isolé ; dans un graphe orienté, le degré d'un sommet est la somme de son degré entrant et de son degré sortant.

**Lemme des poignées de main (complément, hors du cours)** : chaque arête apporte 2 à la somme des degrés (1 à chacune de ses extrémités, ou 2 au même sommet pour une boucle), donc $\sum_{v} d(v) = 2\,\text{card}(E)$. Conséquence : le nombre de sommets de degré impair est toujours pair. La relation des graphes $k$-réguliers en est le cas particulier où tous les degrés valent $k$. Voir [[Lemme des poignées de main]].

**Compléments (hors du cours)** :
- un sommet de degré 1 est un sommet pendant (une feuille dans un [[Arbre (théorie des graphes)|arbre]]) ;
- dans la [[Matrice d'adjacence]] d'un graphe simple, le degré de $v_i$ est la somme de la ligne $i$. Avec des boucles, la matrice du cours compte une boucle 1 sur la diagonale alors qu'elle compte 2 dans le degré : il faut alors ajouter le terme diagonal une seconde fois ;
- ne pas confondre avec le « degré d'un nœud » des arbres enracinés ([[Vocabulaire des arbres]]), qui est son nombre de fils : un nœud autre que la racine a une arête incidente de plus, celle qui le relie à son père.

Notion parente : [[Graphe non orienté]]. Voir aussi : [[Graphe régulier]], [[Graphe complet]], [[Graphe orienté]], [[Lemme des poignées de main]], [[Matrice d'adjacence]], [[Vocabulaire des arbres]].

Résumés : [[3 - Arbres]], [[1 - Undirected graph]], [[4 - oriented graphs]], [[0 - Graph - Python]]
