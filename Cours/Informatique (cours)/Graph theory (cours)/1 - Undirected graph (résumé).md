---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/graph theory/Chp 1 - Undirected graph.docx|Chp 1 - Undirected graph]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 4/graph theory/Chp 1 - Undirected graph.docx|Chp 1 - Undirected graph]], dans [[Graph theory (index)]]. Cours en anglais. En cas d'écart, le cours et ses images font foi. L'image des chaînes (image 17) a été ouverte ; les autres sont lues par leur transcription. Voir [[Graphe non orienté]].

## Idée générale

Définitions de base des graphes non orientés (multigraphes avec boucles), puis graphes particuliers : planaire, complet, connexe, biparti, régulier, pondéré.

## Définitions de base

### Graphe non orienté

Un **graphe non orienté** (*undirected graph*) est un triplet $G = (V, E, \gamma)$ où :
- $V$ est un ensemble **fini non vide** : ses éléments sont les **sommets** (*vertices*) de $G$ (voir [[Sommet et arête]]) ;
- $E$ est un ensemble **fini, éventuellement vide** : ses éléments sont les **arêtes** (*edges*) ;
- $\gamma$ est une fonction de $E$ dans $V^2$ (voir Points à vérifier, 2).

Pour tout $e \in E$, les composantes de $\gamma(e)$ sont les **extrémités** (*endpoints*) de $e$.

### Vocabulaire

- **Sommets adjacents** (*neighbors*, *adjacent*) : $v_1, v_2 \in V$ sont voisins si et seulement s'il existe une arête $e \in E$ d'extrémités $v_1$ et $v_2$.
- **Sommet isolé** (*isolated*) : sommet adjacent à aucun autre.
- **Boucle** (*loop*) : arête dont les deux extrémités sont égales : $e$ est une boucle $\iff \exists v \in V,\ \gamma(e) = (v, v)$.
- **Arêtes multiples** ou **parallèles** (*multiple*, *parallel edges*) : deux arêtes qui ont les mêmes extrémités.

### Graphe simple et graphe sous-jacent

- **[[Graphe simple]]** : $G$ est simple si et seulement s'il n'a **ni boucle ni arête parallèle**.
- **[[Graphe sous-jacent]]** (*underlying graph*) de $G$ : le graphe simple non orienté $\tilde G = (V, E')$ avec $E' \subseteq V \times V$ et la condition « $\forall (v, v') \in E' \Leftrightarrow v \ne v'$ » (formulation du cours, voir Points à vérifier, 4) : on supprime les boucles et on fusionne les arêtes multiples.

![[Chp 1 - Undirected graph - image5.png]]
*Figure : à gauche, multigraphe sur $v_1, \dots, v_4$ ($e_1 = v_1v_2$ ; $e_2, e_3$ parallèles entre $v_2$ et $v_3$ ; $e_4 = v_2v_4$ ; $e_5 = v_3v_4$ ; boucle $e_6$ sur $v_4$). À droite, son graphe sous-jacent simple : $v_1v_2$, $v_2v_3$, $v_3v_4$, $v_2v_4$.*

## Matrice d'adjacence

Soit $G = (V, E, \gamma)$, $V = \{v_i\}_{1 \le i \le n}$, $n = \text{card}(V)$. La **[[Matrice d'adjacence|matrice d'adjacence]]** de $G$ est la matrice carrée $M$ d'ordre $n$ telle que $M_{i,j}$ est **le nombre d'arêtes** entre $v_i$ et $v_j$.

![[Chp 1 - Undirected graph - image4.png]]
*Figure : le graphe d'exemple ($e_1$ à $e_6$, mêmes arêtes que ci-dessus) et sa matrice d'adjacence.*

$$M = \begin{bmatrix} 0 & 1 & 0 & 0 \\ 1 & 0 & 2 & 1 \\ 0 & 2 & 0 & 1 \\ 0 & 1 & 1 & 1 \end{bmatrix}$$

Lecture : les deux arêtes parallèles $v_2v_3$ donnent $M_{2,3} = M_{3,2} = 2$ ; la boucle sur $v_4$ donne $M_{4,4} = 1$.

Pour un graphe non orienté, la matrice est **symétrique**.

## Isomorphisme de graphes

Soient $G_1 = (V_1, E_1, \gamma_1)$ et $G_2 = (V_2, E_2, \gamma_2)$. Un **isomorphisme** de $G_1$ vers $G_2$ est un couple $(\varphi, \psi)$ tel que :
- $\varphi$ est une [[Bijection|bijection]] de $V_1$ sur $V_2$ ;
- $\psi$ est une bijection de $E_1$ sur $E_2$ ;
- pour tout $e \in E_1$, si $v, v'$ sont les extrémités de $e$, alors $\varphi(v)$ et $\varphi(v')$ sont les extrémités de $\psi(e)$.

$G_1$ et $G_2$ sont **isomorphes** si et seulement s'il existe un isomorphisme de $G_1$ vers $G_2$. Voir [[Isomorphisme de graphes]].

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

$C_1$ est une chaîne de longueur 4. $C_2$ n'en est pas une : $e_1$ relie $v_1$ et $v_2$, pas $v_4$ et $v_1$ (voir Points à vérifier, 3).

### Chaîne simple, chaîne élémentaire, cycle

- **Chaîne simple** : les arêtes de $C$ sont deux à deux distinctes :
$$\forall (i, j) \in \{1, \ldots, p\}^2,\ (i \ne j) \implies e_i \ne e_j.$$
- **Chaîne élémentaire** : les sommets de $C$ sont deux à deux distincts :
$$\forall (i, j) \in \{0, \ldots, p\}^2,\ (i \ne j) \implies v_i \ne v_j.$$
- **Cycle** : chaîne **simple** $C$ telle que $\ell(C) > 0$ et $v_p = v_0$ (voir [[Cycle (graphe)]]).

À retenir (surligné dans la note) : **chaîne élémentaire $\Rightarrow$ chaîne simple**.

## Graphes particuliers

### Graphe planaire

Un graphe non orienté est **[[Graphe planaire|planaire]]** si ses arêtes ne se chevauchent pas dans **au moins une** représentation graphique.

**Proposition.** Soient $G_1$ et $G_2$ deux graphes non orientés, $G_1$ planaire.
1. Tout [[Sous-graphe|sous-graphe]] de $G_1$ est planaire.
2. Si $G_1$ et $G_2$ sont isomorphes, alors $G_2$ est planaire.

### Graphe complet

Un graphe non orienté est **[[Graphe complet|complet]]** si et seulement s'il est **simple** et que **toute paire de sommets est adjacente**.

**Proposition (nombre d'arêtes d'un graphe complet).** Si $G$ est complet et $n = \text{card}(V)$ :
$$\text{card}(E) = \binom{n}{2} = \frac{n(n-1)}{2}.$$

**Corollaire.** Si $G$ est simple et $n = \text{card}(V)$ :
$$\text{card}(E) \le \frac{n(n-1)}{2}.$$

Note de l'étudiante : dans un graphe **simple complet**, le [[Degré d'un sommet|degré]] de chaque sommet vaut $\text{card}(V) - 1$.

### Graphe connexe

- $G$ est **[[Graphe connexe|connexe]]** si et seulement si pour toute paire $(v, v') \in V \times V$, il existe un chemin (*path*, lire « chaîne ») d'extrémités $v$ et $v'$.
- **Composante connexe** : sous-graphe connexe **maximal** pour l'inclusion des sommets et des arêtes.

**Propositions.**
1. Un graphe est connexe si et seulement s'il a **une seule composante connexe** ; celle-ci est alors le graphe lui-même.
2. Les composantes connexes d'un graphe sont **disjointes** : elles ne partagent ni sommet ni arête.

### Graphe biparti

- $G$ est **[[Graphe biparti|biparti]]** si et seulement s'il existe une [[Partition d'un ensemble|partition]] $(V_1, V_2)$ de $V$, avec $V_1$ et $V_2$ non vides, telle que
$$\forall e \in E,\ e \text{ a une extrémité dans } V_1 \text{ et l'autre dans } V_2.$$
On note alors $G = (V_1, V_2, E, \gamma)$.
- **Biparti complet** : $G$ biparti est complet si et seulement s'il est simple et que **tout sommet de $V_1$ est adjacent à tout sommet de $V_2$**.
- **Caractérisation** : $G$ est biparti **si et seulement si tout cycle de $G$ est de longueur paire**.

Note de l'étudiante : « attention, les sous-partitions $V_1$ et $V_2$ doivent avoir minimum 2 nœuds » (voir Points à vérifier, 1).

![[Chp 1 - Undirected graph - image3.png]]
*Figure : $G = (\{v_1, v_3, v_4\}, \{v_2, v_5\}, E, \gamma)$ est biparti (arêtes $v_1v_2$, $v_3v_2$, $v_4v_2$, $v_4v_5$) ; puis les bipartis complets $K_{2,2}$, $K_{2,3}$ et $K_{3,3}$.*

### Graphe régulier

- Soit $k \in \mathbb{N}$. $G$ est **$k$-régulier** si et seulement si tout sommet est de degré $k$ : $\forall v \in V,\ d(v) = k$.
- $G$ est **régulier** s'il existe $k$ tel que $G$ soit $k$-régulier. Voir [[Graphe régulier]].

**Proposition.** Si $G$ est $k$-régulier, alors
$$k \cdot \text{card}(V) = 2 \cdot \text{card}(E).$$

### Graphe pondéré

Un **[[Graphe pondéré|graphe pondéré]]** non orienté est un quadruplet $G = (V, E, \gamma, w)$ où $(V, E, \gamma)$ est un graphe non orienté et $w : E \to \mathbb{R}$ est la **pondération** (*weighting*) de $G$.

**Matrice d'adjacence** d'un graphe simple pondéré, d'ordre $n = \text{card}(V)$ :
$$M_{i,j} = \begin{cases} 0 & \text{si } i = j \\ w(v_i v_j) & \text{si } v_i v_j \in E \\ +\infty & \text{si } v_i v_j \notin E \end{cases}$$

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Note sur les sous-ensembles du biparti** : « les sous-partitions $V_1$ et $V_2$ doivent avoir minimum 2 noeuds ». La définition du cours demande seulement $V_1$ et $V_2$ non vides, et l'exemple $G = (\{v_1, v_3, v_4\}, \{v_2, v_5\}, \ldots)$ est compatible avec les deux. La note de l'étudiant contredit la définition : un seul sommet de chaque côté suffit (par exemple une étoile).
2. **$\gamma : E \to V^2$** : un couple ordonné pour un graphe non orienté (alerte de la transcription). Il faudrait des paires non ordonnées (complément).
3. **Chaîne $C_2$** : $e_1$ relie $v_1$ et $v_2$, pas $v_4$ et $v_1$, donc $C_2 = (v_2, e_2, v_3, e_3, v_2, e_4, v_4, e_1, v_1)$ n'est pas une chaîne. Image ouverte : $C_1$ est bien en vert et $C_2$ en rouge, ce qui suggère un contre-exemple voulu ; le cours ne le dit pas explicitement.
4. **Graphe sous-jacent** : la condition « $\forall (v, v') \in E' \Leftrightarrow v \ne v'$ » est mal formulée (alerte de la transcription). L'idée est : $E'$ contient une arête entre deux sommets distincts adjacents dans $G$ (complément).
5. **Degré non défini** : $d(v)$ sert pour les graphes réguliers, mais le chapitre ne le définit pas. La formule $k\,\text{card}(V) = 2\,\text{card}(E)$ suppose qu'une boucle compte deux fois (complément).
6. **« Path » à la place de « chain »** : la connexité est définie par un « path », alors que le chapitre définit des chaînes. Il faut lire chaîne (complément).
7. **Boucle dans la matrice d'adjacence** : l'exemple compte la boucle $e_6$ pour 1 sur la diagonale ($M_{4,4} = 1$), conformément à la définition « nombre d'arêtes » ; d'autres conventions la comptent 2, ce qui s'accorde avec le degré (complément).
