---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/graph theory/Chp 1 - Undirected graph.docx|Chp 1 - Undirected graph]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 4/graph theory/Chp 1 - Undirected graph.docx|Chp 1 - Undirected graph]], dans [[Cours/Informatique/Graph theory/_index|Graph theory]]. Cours en anglais. L'image des chaînes (image 17) a été ouverte ; les autres sont lues par leur transcription. Voir [[Graphe non orienté]].

## Idée générale

Définitions de base des graphes non orientés (multigraphes avec boucles), puis graphes particuliers : planaire, complet, connexe, biparti, régulier, pondéré.

La théorie des graphes naît en 1736 avec le problème des sept ponts de Königsberg, résolu par Euler : peut-on se promener en traversant chaque pont une fois et une seule ? En représentant les quartiers par des sommets et les ponts par des arêtes, Euler montre que c'est impossible, parce que trop de sommets ont un degré impair. On en tire la notion de [[Graphe eulérien|graphe eulérien]] : un graphe connexe possède un cycle passant une fois par chaque arête si et seulement si tous ses sommets sont de degré pair. [[Complément hors du cours|ⓘ]]

## Définitions de base

### Graphe non orienté

Un **graphe non orienté** (*undirected graph*) est un triplet $G = (V, E, \gamma)$ où :
- $V$ est un ensemble **fini non vide** : ses éléments sont les **sommets** (*vertices*) de $G$ (voir [[Sommet et arête]]) ;
- $E$ est un ensemble **fini, éventuellement vide** : ses éléments sont les **arêtes** (*edges*) ;
- $\gamma$ est une fonction qui associe à chaque arête une paire **non ordonnée** de sommets $\{v, v'\}$ (avec $v = v'$ pour une boucle). [[Erreurs du cours#^e-1-undirected-graph|✎]]

Pour tout $e \in E$, les éléments de $\gamma(e)$ sont les **extrémités** (*endpoints*) de $e$.

### Vocabulaire

- **Sommets adjacents** (*neighbors*, *adjacent*) : $v_1, v_2 \in V$ sont voisins si et seulement s'il existe une arête $e \in E$ d'extrémités $v_1$ et $v_2$.
- **Sommet isolé** (*isolated*) : sommet adjacent à aucun autre.
- **Boucle** (*loop*) : arête dont les deux extrémités sont égales : $e$ est une boucle $\iff \exists v \in V,\ \gamma(e) = (v, v)$.
- **Arêtes multiples** ou **parallèles** (*multiple*, *parallel edges*) : deux arêtes qui ont les mêmes extrémités.
- **[[Degré d'un sommet|Degré]]** $d(v)$ (*degree*), employé plus bas sans être défini : nombre d'arêtes dont $v$ est une extrémité, une boucle comptant **deux fois**. Un sommet isolé est de degré 0 ; un sommet de degré 1 est dit **pendant** (une feuille dans un arbre). [[Complément hors du cours|ⓘ]]
- **[[Lemme des poignées de main]]** : chaque arête apporte 2 à la somme des degrés (1 à chaque extrémité, ou 2 au même sommet pour une boucle), donc $\sum_{v \in V} d(v) = 2\,\text{card}(E)$. Conséquence : le nombre de sommets de degré impair est toujours **pair**. [[Complément hors du cours|ⓘ]]

### Graphe simple et graphe sous-jacent

- **[[Graphe simple]]** : $G$ est simple si et seulement s'il n'a **ni boucle ni arête parallèle**.
- **[[Graphe sous-jacent]]** (*underlying graph*) de $G$ : le graphe simple non orienté $\tilde G = (V, E')$ avec $E' \subseteq V \times V$ et la condition « $(v, v') \in E' \Leftrightarrow v \ne v'$ et $v, v'$ adjacents dans $G$ » : on supprime les boucles et on fusionne les arêtes multiples. [[Erreurs du cours#^e-1-undirected-graph|✎]]

![[Chp 1 - Undirected graph - image5.png]]
*Figure : à gauche, multigraphe sur $v_1, \dots, v_4$ ($e_1 = v_1v_2$ ; $e_2, e_3$ parallèles entre $v_2$ et $v_3$ ; $e_4 = v_2v_4$ ; $e_5 = v_3v_4$ ; boucle $e_6$ sur $v_4$). À droite, son graphe sous-jacent simple : $v_1v_2$, $v_2v_3$, $v_3v_4$, $v_2v_4$.*

## Matrice d'adjacence

Soit $G = (V, E, \gamma)$, $V = \{v_i\}_{1 \le i \le n}$, $n = \text{card}(V)$. La **[[Matrice d'adjacence|matrice d'adjacence]]** de $G$ est la matrice carrée $M$ d'ordre $n$ telle que $M_{i,j}$ est **le nombre d'arêtes** entre $v_i$ et $v_j$.

![[Chp 1 - Undirected graph - image4.png]]
*Figure : le graphe d'exemple ($e_1$ à $e_6$, mêmes arêtes que ci-dessus) et sa matrice d'adjacence.*

$$M = \begin{bmatrix} 0 & 1 & 0 & 0 \\ 1 & 0 & 2 & 1 \\ 0 & 2 & 0 & 1 \\ 0 & 1 & 1 & 1 \end{bmatrix}$$

Lecture : les deux arêtes parallèles $v_2v_3$ donnent $M_{2,3} = M_{3,2} = 2$ ; la boucle sur $v_4$ donne $M_{4,4} = 1$.

Pour un graphe non orienté, la matrice est **symétrique**.

Pour un graphe simple, la matrice ne contient que des 0 et des 1, avec des 0 sur la diagonale, et la somme de la ligne $i$ vaut le degré de $v_i$. Avec des boucles, attention : la boucle compte 1 dans la matrice du cours mais 2 dans le degré. [[Complément hors du cours|ⓘ]]

L'autre représentation courante est la **[[Liste d'adjacence|liste d'adjacence]]** : pour chaque sommet, la liste de ses voisins (c'est le dictionnaire du [[0 - Graph - Python|TP Python]]). La matrice occupe $n^2$ cases quel que soit le nombre d'arêtes $m$ et teste l'adjacence de deux sommets en temps constant ; la liste occupe une place proportionnelle à $n + m$, plus économe pour un graphe **creux** (peu d'arêtes), mais tester l'adjacence demande de parcourir une liste de voisins. [[Complément hors du cours|ⓘ]]

## Isomorphisme de graphes

Soient $G_1 = (V_1, E_1, \gamma_1)$ et $G_2 = (V_2, E_2, \gamma_2)$. Un **isomorphisme** de $G_1$ vers $G_2$ est un couple $(\varphi, \psi)$ tel que :
- $\varphi$ est une [[Bijection|bijection]] de $V_1$ sur $V_2$ ;
- $\psi$ est une bijection de $E_1$ sur $E_2$ ;
- pour tout $e \in E_1$, si $v, v'$ sont les extrémités de $e$, alors $\varphi(v)$ et $\varphi(v')$ sont les extrémités de $\psi(e)$.

$G_1$ et $G_2$ sont **isomorphes** si et seulement s'il existe un isomorphisme de $G_1$ vers $G_2$. Voir [[Isomorphisme de graphes]].

Deux graphes isomorphes sont « le même graphe dessiné ou nommé autrement » : ils ont le même nombre de sommets, le même nombre d'arêtes, la même liste de degrés, le même nombre de cycles de chaque longueur, etc. Ces **invariants** servent à prouver que deux graphes **ne sont pas** isomorphes (un invariant diffère) ; leur égalité ne suffit pas à prouver qu'ils le sont : il faut alors exhiber la bijection. [[Complément hors du cours|ⓘ]]

![[Chp 1 - Undirected graph - image7.png]]
*Figure : exemple de deux graphes isomorphes. À gauche, triangle $v_2v_3v_4$ avec $v_1$ pendant à $v_2$ ; à droite, le même graphe avec des symboles de cartes (trèfle relié au carreau ; carreau, pique, cœur en triangle).*

## Chaînes

### Chaîne

Une **chaîne** (*chain*) dans $G$ est une suite finie $C = (v_0, e_1, v_1, \ldots, e_i, v_i, \ldots, e_p, v_p)$ telle que :
- $\forall i \in \{0, \ldots, p\},\ v_i \in V$ ;
- $\forall i \in \{1, \ldots, p\},\ e_i \in E$ et ses extrémités sont $v_{i-1}$ et $v_i$.

L'entier $p$ est la **longueur** de $C$, notée $\ell(C)$ ; $v_0$ et $v_p$ sont les extrémités de $C$. Voir [[Chaîne (graphe)]].

![[Chp 1 - Undirected graph - image17.png]]
*Figure : le graphe d'exemple, avec $C_1 = (v_2, e_2, v_3, e_3, v_2, e_4, v_4, e_6, v_4)$ en vert et $C_2 = (v_2, e_2, v_3, e_3, v_2, e_4, v_4, e_1, v_1)$ en rouge.*

$C_1$ est une chaîne de longueur 4. $C_2$ n'en est pas une : $e_1$ relie $v_1$ et $v_2$, pas $v_4$ et $v_1$. Dans l'image, $C_1$ est écrite en vert et $C_2$ en rouge.

### Chaîne simple, chaîne élémentaire, cycle

- **Chaîne simple** : les arêtes de $C$ sont deux à deux distinctes :
$$\forall (i, j) \in \{1, \ldots, p\}^2,\ (i \ne j) \implies e_i \ne e_j.$$
- **Chaîne élémentaire** : les sommets de $C$ sont deux à deux distincts :
$$\forall (i, j) \in \{0, \ldots, p\}^2,\ (i \ne j) \implies v_i \ne v_j.$$
- **Cycle** : chaîne **simple** $C$ telle que $\ell(C) > 0$ et $v_p = v_0$ (voir [[Cycle (graphe)]]).

À retenir (surligné dans la note) : **chaîne élémentaire $\Rightarrow$ chaîne simple**.

Pourquoi : si une arête revenait deux fois ($e_i = e_j$ avec $i < j$), ses extrémités $\{v_{i-1}, v_i\}$ et $\{v_{j-1}, v_j\}$ seraient les mêmes, donc un sommet apparaîtrait à deux positions différentes, ce qu'interdit une chaîne élémentaire. La réciproque est fausse : dans un triangle $v_1v_2v_3$, la chaîne $(v_1, v_2, v_3, v_1)$ n'emprunte chaque arête qu'une fois (simple) mais repasse par $v_1$ (non élémentaire) ; c'est un cycle. [[Complément hors du cours|ⓘ]]

Propriété classique : s'il existe une chaîne de $v$ à $v'$, il en existe une **élémentaire** ; il suffit de couper les boucles de la chaîne, c'est-à-dire de supprimer le morceau entre deux passages par un même sommet, tant qu'il en reste. [[Complément hors du cours|ⓘ]]

## Graphes particuliers

### Graphe planaire

Un graphe non orienté est **[[Graphe planaire|planaire]]** si ses arêtes ne se chevauchent pas dans **au moins une** représentation graphique.

**Proposition.** Soient $G_1$ et $G_2$ deux graphes non orientés, $G_1$ planaire.
1. Tout [[Sous-graphe|sous-graphe]] de $G_1$ est planaire.
2. Si $G_1$ et $G_2$ sont isomorphes, alors $G_2$ est planaire.

Un dessin sans croisement d'un graphe planaire découpe le plan en **faces** (la face extérieure comprise). Pour un graphe planaire connexe à $n$ sommets, $m$ arêtes et $f$ faces, la **formule d'Euler** donne $n - m + f = 2$. On en déduit qu'un graphe simple planaire à $n \ge 3$ sommets a au plus $3n - 6$ arêtes. [[Complément hors du cours|ⓘ]]

Les deux graphes non planaires de référence sont $K_5$ (complet à 5 sommets : $10 > 3 \times 5 - 6 = 9$ arêtes) et $K_{3,3}$ (biparti complet, problème des trois maisons à relier à trois usines sans croisement). Le théorème de Kuratowski (1930) établit qu'un graphe est planaire si et seulement s'il ne contient pas de subdivision de l'un d'eux. [[Complément hors du cours|ⓘ]]

Culture générale : le **théorème des quatre couleurs** affirme que les sommets de tout graphe planaire peuvent être coloriés avec quatre couleurs sans que deux sommets voisins aient la même (colorier une carte où deux pays frontaliers diffèrent). Démontré en 1976 par Appel et Haken, c'est le premier grand théorème dont la preuve repose sur un calcul par ordinateur. [[Complément hors du cours|ⓘ]]

### Graphe complet

Un graphe non orienté est **[[Graphe complet|complet]]** si et seulement s'il est **simple** et que **toute paire de sommets est adjacente**.

**Proposition (nombre d'arêtes d'un graphe complet).** Si $G$ est complet et $n = \text{card}(V)$ :
$$\text{card}(E) = \binom{n}{2} = \frac{n(n-1)}{2}.$$

**Corollaire.** Si $G$ est simple et $n = \text{card}(V)$ :
$$\text{card}(E) \le \frac{n(n-1)}{2}.$$

Le graphe complet à $n$ sommets se note $K_n$. Justification : dans un graphe simple, une arête correspond à **une paire** de sommets distincts (pas de boucle) et chaque paire porte au plus une arête (pas d'arête parallèle). Il y a $\binom{n}{2}$ paires ; le graphe complet les prend toutes, un graphe simple quelconque une partie seulement, d'où le corollaire. [[Complément hors du cours|ⓘ]]

Note de l'étudiante : dans un graphe **simple complet**, le [[Degré d'un sommet|degré]] de chaque sommet vaut $\text{card}(V) - 1$.

### Graphe connexe

- $G$ est **[[Graphe connexe|connexe]]** si et seulement si pour toute paire $(v, v') \in V \times V$, il existe un chemin (*path*, lire « chaîne ») d'extrémités $v$ et $v'$.
- **Composante connexe** : sous-graphe connexe **maximal** pour l'inclusion des sommets et des arêtes.

**Propositions.**
1. Un graphe est connexe si et seulement s'il a **une seule composante connexe** ; celle-ci est alors le graphe lui-même.
2. Les composantes connexes d'un graphe sont **disjointes** : elles ne partagent ni sommet ni arête.

La relation « il existe une chaîne de $v$ à $v'$ » est une [[Relation d'équivalence|relation d'équivalence]] sur $V$ (réflexive avec la chaîne de longueur 0, symétrique en lisant la chaîne à l'envers, transitive en mettant deux chaînes bout à bout) ; les composantes connexes sont ses classes, ce qui explique qu'elles forment une partition de $V$. On les obtient en pratique par un [[Parcours en largeur|parcours en largeur]] ou en [[Parcours en profondeur|profondeur]] lancé depuis chaque sommet non encore visité. [[Complément hors du cours|ⓘ]]

Un graphe connexe à $n$ sommets a au moins $n - 1$ arêtes ; il en a exactement $n - 1$ si et seulement si c'est un arbre (voir [[2 - tree]]). [[Complément hors du cours|ⓘ]]

### Graphe biparti

- $G$ est **[[Graphe biparti|biparti]]** si et seulement s'il existe une [[Partition d'un ensemble|partition]] $(V_1, V_2)$ de $V$, avec $V_1$ et $V_2$ non vides, telle que
$$\forall e \in E,\ e \text{ a une extrémité dans } V_1 \text{ et l'autre dans } V_2.$$
On note alors $G = (V_1, V_2, E, \gamma)$.
- **Biparti complet** : $G$ biparti est complet si et seulement s'il est simple et que **tout sommet de $V_1$ est adjacent à tout sommet de $V_2$**.
- **Caractérisation** : $G$ est biparti **si et seulement si tout cycle de $G$ est de longueur paire**.
- Sens direct de la caractérisation : en suivant un cycle, on change de côté ($V_1$, $V_2$) à chaque arête ; pour revenir au sommet de départ, il faut un nombre pair de changements. Un triangle (cycle de longueur 3) n'est donc jamais biparti. En pratique, on teste la bipartition par une **2-coloration** en parcours en largeur, comme la fonction `isGraphBipartite` du [[0 - Graph - Python|TP Python]]. [[Complément hors du cours|ⓘ]]
- Le biparti complet avec $\text{card}(V_1) = p$ et $\text{card}(V_2) = q$ se note $K_{p,q}$ ; il a $p \times q$ arêtes. Les graphes bipartis modélisent les problèmes d'**affectation** (personnes et tâches, étudiants et stages), où l'on cherche un **couplage** : un ensemble d'arêtes sans extrémité commune. [[Complément hors du cours|ⓘ]]

Note de l'étudiante : attention, les sous-partitions $V_1$ et $V_2$ doivent être non vides ; un seul sommet de chaque côté suffit (une arête seule, $K_{1,1}$, est un graphe biparti). [[Erreurs du cours#^e-1-undirected-graph|✎]]

![[Chp 1 - Undirected graph - image3.png]]
*Figure : $G = (\{v_1, v_3, v_4\}, \{v_2, v_5\}, E, \gamma)$ est biparti (arêtes $v_1v_2$, $v_3v_2$, $v_4v_2$, $v_4v_5$) ; puis les bipartis complets $K_{2,2}$, $K_{2,3}$ et $K_{3,3}$.*

### Graphe régulier

- Soit $k \in \mathbb{N}$. $G$ est **$k$-régulier** si et seulement si tout sommet est de degré $k$ : $\forall v \in V,\ d(v) = k$.
- $G$ est **régulier** s'il existe $k$ tel que $G$ soit $k$-régulier. Voir [[Graphe régulier]].

**Proposition.** Si $G$ est $k$-régulier, alors
$$k \cdot \text{card}(V) = 2 \cdot \text{card}(E).$$

C'est le [[Lemme des poignées de main|lemme des poignées de main]] avec tous les degrés égaux à $k$ : $\sum_v d(v) = k \cdot \text{card}(V)$. Exemples : $K_n$ est $(n-1)$-régulier ; un cycle est 2-régulier ; le cube (8 sommets, 12 arêtes) est 3-régulier, et $3 \times 8 = 2 \times 12$. Conséquence : un graphe $k$-régulier avec $k$ impair a forcément un nombre pair de sommets. [[Complément hors du cours|ⓘ]]

### Graphe pondéré

Un **[[Graphe pondéré|graphe pondéré]]** non orienté est un quadruplet $G = (V, E, \gamma, w)$ où $(V, E, \gamma)$ est un graphe non orienté et $w : E \to \mathbb{R}$ est la **pondération** (*weighting*) de $G$.

**Matrice d'adjacence** d'un graphe simple pondéré, d'ordre $n = \text{card}(V)$ :
$$M_{i,j} = \begin{cases} 0 & \text{si } i = j \\ w(v_i v_j) & \text{si } v_i v_j \in E \\ +\infty & \text{si } v_i v_j \notin E \end{cases}$$

Ce choix vient des problèmes de distance : le poids est une longueur ou un coût ; aller de $v_i$ à lui-même ne coûte rien (0), et l'absence d'arête équivaut à un trajet direct impossible, de coût infini ($+\infty$). Un 0 ne pourrait pas marquer l'absence d'arête, puisqu'il se confondrait avec une arête de poids nul. C'est la matrice de départ des algorithmes de plus court chemin, comme celui de Floyd-Warshall. [[Complément hors du cours|ⓘ]]