---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - bellman ford.pdf|chp4 - bellman ford.pdf]]"]
maj: 2026-11-12
complet: true
enrichi: 2026-11-12
---

Résumé de [[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - bellman ford.pdf|chp4 - bellman ford.pdf]], dans [[Cours/Informatique/Graph theory/_index|Graph theory]]. Diaporama de 32 diapositives d'une autre université (Aix-Marseille Université, 2023-2024), rangé par l'utilisatrice comme supplément du chapitre [[4 - oriented graphs]]. Voir [[Algorithme de Bellman-Ford]] et, pour l'autre algorithme de plus court chemin, [[4 - dijkstra]].

## Idée générale

Calculer les [[Plus court chemin|plus courts chemins]] issus d'un [[Sommet et arête|sommet]] dans un [[Graphe pondéré|graphe pondéré]] dont les poids peuvent être négatifs, par [[Programmation dynamique|programmation dynamique]] sur le nombre d'arcs ; simplifier l'algorithme en un [[Tableau (programmation)|tableau]] à une dimension, reconstruire les chemins, puis l'adapter au [[Routage IP|routage]] dans les réseaux.

## Plus courts chemins dans un graphe

Soit $G = (S, A, w)$ un [[Graphe pondéré|graphe pondéré]] [[Graphe orienté|orienté]] : $S$ est l'ensemble des [[Sommet et arête|sommets]], $A$ celui des arcs, et $w(u, v)$ le poids de l'arc $(u, v)$. On note $n = |S|$ et $m = |A|$.

- **Longueur d'un chemin** : la longueur du [[Chemin (graphe)|chemin]] $(u_1, \ldots, u_k)$ est la somme des poids de ses arcs,
$$\sum_{i=1}^{k-1} w(u_i, u_{i+1}).$$
- **Notation** : $\delta(u, v)$ est la longueur d'un [[Plus court chemin|plus court chemin]] de $u$ à $v$.

Ici la « longueur » est un poids total, et non le nombre d'arcs comme dans [[4 - oriented graphs]]. Par convention, $\delta(u, v) = +\infty$ si $v$ n'est pas accessible depuis $u$, et $\delta(u, u) = 0$. [[Complément hors du cours|ⓘ]]

Les poids représentent une distance, un temps, un coût ou une [[Latence (réseau)|latence]] ; on les lit dans la [[Matrice d'adjacence|matrice d'adjacence]] pondérée ou les [[Liste d'adjacence|listes d'adjacence]] du graphe. [[Complément hors du cours|ⓘ]]

## Quel algorithme selon les poids

| Situation | Algorithme |
|---|---|
| Arcs de poids positifs | [[Algorithme de Dijkstra\|algorithme de Dijkstra]] (source unique) |
| Circuits de longueur négative | pas de [[Plus court chemin\|plus court chemin]] vers les [[Sommet et arête\|sommets]] accessibles depuis un tel circuit, lui-même accessible depuis la source [[Erreurs du cours#^e-4-bellman-ford\|✎]] |
| Arcs de poids quelconques | [[Algorithme de Bellman-Ford\|algorithme de Bellman-Ford]] (source unique) ; [[Algorithme de Floyd-Warshall\|algorithme de Floyd-Warshall]] (tous les plus courts chemins, entre tous les couples de sommets) |

Bellman-Ford et Floyd-Warshall utilisent le principe de la [[Programmation dynamique|programmation dynamique]].

Pourquoi un [[Circuit absorbant|circuit de longueur négative]] (dit **circuit absorbant**) pose problème : chaque tour du [[Circuit (graphe)|circuit]] diminue la longueur du chemin, qu'on peut donc rendre aussi petite qu'on veut, et l'on pose $\delta(s, v) = -\infty$. Les sommets que le circuit n'atteint pas gardent un plus court chemin bien défini. Pour Dijkstra, « positifs » s'entend au sens large : les poids nuls sont admis. [[Complément hors du cours|ⓘ]]

Un [[Graphe non orienté|graphe non orienté]] se traite en remplaçant chaque arête $\{u, v\}$ par les deux arcs $(u, v)$ et $(v, u)$ ; une seule arête de poids négatif y forme alors un circuit absorbant $u \to v \to u$, si bien que Bellman-Ford ne sert, dans ce cas, qu'avec des poids positifs ou nuls. [[Complément hors du cours|ⓘ]]

Un problème voisin est, lui, difficile : trouver un plus long [[Chemin (graphe)|chemin élémentaire]] ([[Problème du plus long chemin]]) est NP-difficile (voir [[Classes P et NP]]), alors que les plus courts chemins se calculent en temps polynomial. [[Complément hors du cours|ⓘ]]

## Plus courts chemins élémentaires

**Propriété.** Si le graphe $G$ ne contient pas de [[Circuit absorbant|circuit de longueur négative]], alors il existe un [[Plus court chemin|plus court chemin]] **élémentaire** entre $s$ et $t$ (dès que $t$ est accessible depuis $s$).

- **[[Chemin (graphe)|Chemin élémentaire]]** : chaque [[Sommet et arête|sommet]] y apparaît au plus une fois (pas de [[Cycle (graphe)|cycle]] dans le chemin).
- Un chemin élémentaire a au plus $n$ sommets, donc **au plus $n - 1$ arcs**.

![[4 - bellman ford - p5.jpg]]
*Figure : un plus court chemin élémentaire de s à t passe par au plus n − 1 arcs.*

*Preuve* : si un plus court chemin passe deux fois par un même sommet, il contient un circuit, de longueur positive ou nulle par hypothèse ; le retirer donne un chemin de longueur inférieure ou égale. En répétant, on obtient un plus court chemin élémentaire. [[Complément hors du cours|ⓘ]]

## Algorithme de Bellman-Ford

Voir [[Algorithme de Bellman-Ford]].

- **Entrée** : un [[Graphe pondéré|graphe]] $G = (S, A, w)$ et un [[Sommet et arête|sommet]] source $s$.
- **Sortie** : les longueurs des [[Plus court chemin|plus courts chemins]] issus de $s$ (constitués d'au plus $n - 1$ arcs).

### Sous-problèmes

$OPT(i, v)$ : longueur minimale d'un chemin de $s$ à $v$ constitué d'**au plus $i$ arcs**.

**Objectif final** : $OPT(n - 1, v)$, longueur des plus courts chemins issus de $s$ d'au plus $n - 1$ arcs, qui vaut $\delta(s, v)$ (noté $\delta(v)$) d'après la propriété précédente, en l'absence de [[Circuit absorbant|circuit absorbant]].

**Principe** : initialiser $OPT(0, v)$ pour tout $v$, puis calculer $OPT(1, v)$ pour tout $v$, …, jusqu'à $OPT(n - 1, v)$ pour tout $v$.

Énumérer tous les chemins de $s$ à $v$ par [[Recherche exhaustive|recherche exhaustive]] coûterait un temps exponentiel ; la [[Programmation dynamique|programmation dynamique]] ramène le calcul à $n \times (n-1)$ sous-problèmes. Contrairement à [[Algorithme de Dijkstra|Dijkstra]], [[Algorithme glouton|algorithme glouton]] qui fixe définitivement une distance à chaque étape, Bellman-Ford peut améliorer une distance jusqu'à la dernière étape, ce qui lui permet d'accepter des poids négatifs. [[Complément hors du cours|ⓘ]]

### Récurrence

Soit $P$ un chemin optimal pour le sous-problème $OPT(i, v)$ :
- si $P$ contient au plus $i - 1$ arcs, alors $OPT(i, v) = OPT(i - 1, v)$ ;
- si $P$ contient exactement $i$ arcs, alors il existe un arc $(u, v) \in A$ tel que $OPT(i, v) = OPT(i - 1, u) + w(u, v)$.

![[4 - bellman ford - p9.jpg]]
*Figure : le chemin optimal P de s à v en au plus i arcs se décompose en un chemin optimal de s à u en au plus i − 1 arcs, suivi de l'arc (u, v).*

C'est le [[Principe d'optimalité de Bellman|principe d'optimalité]] : un sous-chemin d'un plus court chemin est lui-même un plus court chemin. Il justifie la décomposition en sous-problèmes, propre à la programmation dynamique. [[Complément hors du cours|ⓘ]]

**Définition récursive** (une [[Récurrence|récurrence]] sur $i$) :
$$OPT(0, s) = 0, \qquad OPT(0, v) = +\infty \text{ si } v \neq s,$$
$$OPT(i, v) = \min\Big\{\, OPT(i-1, v),\ \min_{u \in Adj^{-1}(v)} \big(OPT(i-1, u) + w(u, v)\big) \Big\} \quad \text{si } i \neq 0,$$
avec la notation $Adj^{-1}(v) = \{u \in S \mid (u, v) \in A\}$, l'ensemble des **prédécesseurs** de $v$.

Une programmation [[Récursivité|récursive]] directe de cette formule recalculerait sans cesse les mêmes $OPT(i-1, u)$ ; on remplit plutôt un [[Tableau (programmation)|tableau]] ligne par ligne, chaque valeur n'étant calculée qu'une fois. [[Complément hors du cours|ⓘ]]

### Version 1 : tableau à deux dimensions

```text
algorithme BELLMAN-FORD(G, s)
in : G = (S, A, w) un graphe pondéré, s un sommet de S
1  pour v ∈ S faire d[0, v] := ∞
2  d[0, s] := 0
3  pour i := 1, ..., n − 1 faire
4      pour v ∈ S faire
5          d[i, v] := min( d[i − 1, v],
6                          min_{u ∈ Adj⁻¹(v)} (d[i − 1, u] + w(u, v)) )
7      fin faire
8  fin faire
9  renvoyer d
fin fonction
```

À l'étape $i$, on considère chaque arc de $G$ une fois. **Complexité** : $O(m \times n)$, avec $n = |S|$ et $m = |A|$ (voir [[Complexité algorithmique]]).

Plus exactement, une étape parcourt les $n$ sommets et, pour chacun, ses prédécesseurs : la somme des [[Degré d'un sommet|degrés entrants]] vaut $m$, d'où $O(n + m)$ par étape et $O(n(n + m))$ au total, soit $O(mn)$ dès que $m \ge n - 1$ (cas d'un graphe où tous les sommets sont accessibles depuis $s$). Il faut des [[Liste d'adjacence|listes d'adjacence]] des prédécesseurs pour énumérer $Adj^{-1}(v)$ sans parcourir tout le graphe. [[Complément hors du cours|ⓘ]]

### Version 2 : parcours des arcs

```text
algorithme BELLMAN-FORD(G, s)
in : G = (S, A, w) un graphe pondéré, s un sommet de S
    pour v ∈ S faire d[0, v] := ∞
    d[0, s] := 0
    pour i := 1, ..., n − 1 faire
        pour v ∈ S faire d[i, v] := d[i − 1, v]
        pour (u, v) ∈ A faire
            si d[i, v] > d[i − 1, u] + w(u, v) alors
                d[i, v] := d[i − 1, u] + w(u, v)
        fin faire
    fin faire
    renvoyer d
fin fonction
```

Peu importe l'ordre dans lequel on considère les arcs.

Le test `si d[i, v] > … alors d[i, v] := …` est un **[[Relâchement d'un arc|relâchement]]** de l'arc $(u, v)$ : on regarde si passer par $u$ améliore la meilleure longueur connue pour $v$. Bellman-Ford n'est qu'une suite de relâchements de tous les arcs, répétée $n - 1$ fois. [[Complément hors du cours|ⓘ]]

## Exemple

![[4 - bellman ford - p18.jpg]]
*Figure : (a) graphe orienté à 6 sommets de source s ; (b) tableau des $d[i, v]$ pour i = 0 à 5.*

Arcs du graphe (a) : $s \to a$ (−3), $s \to c$ (3), $s \to d$ (4), $s \to e$ (2), $a \to d$ (9), $d \to b$ (−1), $b \to a$ (−4), $b \to c$ (8), $c \to e$ (−3), $e \to b$ (−2). Avec $n = 6$ sommets, il faut $n - 1 = 5$ étapes.

| $v$ | $i = 0$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| $s$ | 0 | 0 | 0 | 0 | 0 | 0 |
| $a$ | ∞ | −3 | −3 | −4 | −6 | −6 |
| $b$ | ∞ | ∞ | 0 | −2 | −2 | −2 |
| $c$ | ∞ | 3 | 3 | 3 | 3 | 3 |
| $d$ | ∞ | 4 | 4 | 4 | 4 | 3 |
| $e$ | ∞ | 2 | 0 | 0 | 0 | 0 |

Valeurs recalculées : elles sont exactes. Lecture de quelques cases [[Complément hors du cours|ⓘ]] :
- colonne 1 du [[Tableau (programmation)|tableau]] : seuls les successeurs directs du [[Sommet et arête|sommet]] $s$ sont atteints, avec le poids de l'arc ;
- $e$ à l'étape 2 : $s \to c \to e$ vaut $3 - 3 = 0 < 2$ ;
- $b$ à l'étape 2 : $s \to e \to b$ vaut $2 - 2 = 0$ ; à l'étape 3, $s \to c \to e \to b$ vaut $-2$ ;
- $a$ : $-3$ par l'arc direct, puis $-4$ ($s \to e \to b \to a$, 3 arcs), puis $-6$ ($s \to c \to e \to b \to a$, 4 arcs) ;
- $d$ ne change qu'à l'étape 5 : $s \to c \to e \to b \to a \to d$ vaut $-6 + 9 = 3 < 4$, chemin de 5 arcs, le maximum $n - 1$.

Une sixième étape ne changerait rien : le [[Graphe orienté|graphe orienté]] ne contient pas de [[Circuit absorbant|circuit absorbant]] (les [[Circuit (graphe)|circuits]] $a \to d \to b \to a$ et $b \to c \to e \to b$ ont pour longueurs 4 et 3). [[Complément hors du cours|ⓘ]]

## Simplification : tableau à une dimension

On remplace le tableau $d[i, v]$ par un [[Tableau (programmation)|tableau]] à une dimension $D[\,]$ : $D[v]$ est la longueur d'**un** chemin entre $s$ et $v$.

- **Initialement** : $D[v] = +\infty$ pour tout $v \neq s$, et $D[s] = 0$.
- **Mise à jour** : $D[v] = \min\big(D[v],\ \min_{u \in Adj^{-1}(v)} (D[u] + w(u, v))\big)$.

**Justification** : après $i$ mises à jour, $D[v] \le d[i, v]$ ; $D[v]$ est au plus la longueur d'un [[Plus court chemin|plus court chemin]] entre $s$ et $v$ contenant au plus $i$ arcs.

On a aussi toujours $D[v] \ge \delta(s, v)$, puisque $D[v]$ est la longueur d'un chemin réel (ou $+\infty$). Les deux inégalités forment un [[Invariant de boucle|invariant de boucle]] ; après $n - 1$ étapes, sans [[Circuit absorbant|circuit absorbant]], elles donnent $D[v] = \delta(s, v)$, ce qui prouve la [[Correction d'un algorithme|correction]] de l'algorithme. Mettre à jour $D$ « en place » ne fait qu'accélérer la progression : une valeur améliorée sert dès l'étape en cours. [[Complément hors du cours|ⓘ]]

```text
algorithme BELLMAN-FORD(G, s)
in : G = (S, A, w) un graphe pondéré, s un sommet de S
    pour v ∈ S faire D[v] := ∞
    D[s] := 0
    pour i := 1, ..., n − 1 faire
        pour v ∈ S faire
            D[v] := MIN( D[v], MIN_{u ∈ Adj⁻¹(v)} (D[u] + w(u, v)) )
        fin faire
    fin faire
    renvoyer D
fin fonction
```

**Espace** : $O(n)$, au lieu de $O(n^2)$ pour le tableau $d[i, v]$.

## Reconstruction des plus courts chemins

Si $D[v]$ est modifiée à l'étape $i$ par $D[v] := D[u] + w(u, v)$, on mémorise $u$, dernier [[Sommet et arête|sommet]] intermédiaire : $pred[v] := u$ (un second [[Tableau (programmation)|tableau]]).

Quand l'algorithme est terminé :
- le graphe constitué des arcs $(pred[v], v)$ est un [[Arbre (théorie des graphes)|arbre]] ;
- dans ce graphe, le chemin entre $s$ et $v$ est un [[Plus court chemin|plus court chemin]] dans $G$.

Cet arbre est l'[[Arbre des plus courts chemins|arbre des plus courts chemins]] : une [[Arborescence (graphe)|arborescence]] de racine $s$, qui couvre les sommets accessibles depuis $s$. On lit un chemin à l'envers, en remontant les $pred$ de $v$ jusqu'à $s$. [[Complément hors du cours|ⓘ]]

![[4 - bellman ford - p25.jpg]]
*Figure : arcs (pred[v], v) en bleu, et tableau final des distances et des prédécesseurs.*

| | $s$ | $a$ | $b$ | $c$ | $d$ | $e$ |
|---|---|---|---|---|---|---|
| $D$ | 0 | −6 | −2 | 3 | 3 | 0 |
| $pred$ | − | $b$ | $e$ | $s$ | $a$ | $c$ |

Par exemple, le plus court chemin de $s$ à $d$ se lit en remontant : $d \leftarrow a \leftarrow b \leftarrow e \leftarrow c \leftarrow s$, soit $s \to c \to e \to b \to a \to d$, de longueur $3 - 3 - 2 - 4 + 9 = 3$. Valeurs recalculées : exactes. [[Complément hors du cours|ⓘ]]

### Version complète, avec prédécesseurs

```text
algorithme BELLMAN-FORD(G, s)
in : G = (S, A, w) un graphe pondéré, s un sommet de S
    pour v ∈ S faire
        D[v] := ∞
        pred[v] := NONE
    fin faire
    D[s] := 0
    pour i := 1, ..., n − 1 faire
        pour (u, v) ∈ A faire
            si D[v] > D[u] + w(u, v) alors
                D[v] := D[u] + w(u, v)
                pred[v] := u
            fin si
        fin faire
    fin faire
    renvoyer (D, pred)
fin algo
```

**Détecter un circuit absorbant.** Après les $n - 1$ étapes, on fait une $n$-ième passe sur les arcs : si un arc $(u, v)$ vérifie encore $D[v] > D[u] + w(u, v)$, le graphe contient un [[Circuit absorbant|circuit absorbant]] accessible depuis $s$, et les distances obtenues ne sont pas des plus courts chemins. En remontant $n$ fois les $pred$ depuis $v$, on tombe sur un sommet du circuit. Sans circuit absorbant, aucune distance ne peut plus baisser. [[Complément hors du cours|ⓘ]]

**Arrêt anticipé.** Si une étape entière ne modifie aucune distance, les suivantes ne changeront rien non plus : on peut s'arrêter (c'est l'idée reprise plus bas pour le [[Routage IP|routage]]). Dans le meilleur cas, l'algorithme termine ainsi après deux passes. [[Complément hors du cours|ⓘ]]

**Repères.** L'[[Algorithme de Bellman-Ford|algorithme]] porte les noms de Richard Bellman (article de 1958) et de Lester Ford Jr. (1956) ; Edward F. Moore l'a aussi publié en 1959, d'où le nom de « Bellman-Ford-Moore ». Sur un [[Graphe orienté|graphe orienté]] sans circuit (DAG), on fait mieux : en [[Relâchement d'un arc|relâchant]] les arcs dans l'ordre d'un [[Tri topologique|tri topologique]], une seule passe suffit, en $O(n + m)$. [[Complément hors du cours|ⓘ]]

**Tous les couples de sommets.** L'[[Algorithme de Floyd-Warshall|algorithme de Floyd-Warshall]] calcule $\delta(u, v)$ pour tous les couples en $O(n^3)$, par [[Programmation dynamique|programmation dynamique]] sur les sommets intermédiaires autorisés. L'[[Algorithme de Johnson|algorithme de Johnson]] fait mieux sur les graphes peu denses : un Bellman-Ford sert à repondérer les arcs pour les rendre positifs, puis on lance un [[Algorithme de Dijkstra|Dijkstra]] depuis chaque sommet. [[Complément hors du cours|ⓘ]]

## Routage dans les réseaux de communication

Une application importante des algorithmes de [[Plus court chemin|plus courts chemins]] : déterminer le meilleur chemin pour router les messages dans un [[Réseau|réseau]].

| Graphe | Réseau de communications |
|---|---|
| [[Sommet et arête\|Sommets]] | [[Routeur\|Routeurs]] |
| Arcs | Lignes de communications |
| Longueurs | Délais ([[Latence (réseau)\|latence]]) |

- **[[Algorithme de Dijkstra]]** : fonctionnement **global**, choix du sommet le plus proche parmi tous les sommets.
- **[[Algorithme de Bellman-Ford]]** : fonctionnement **local**, chaque nœud a juste besoin de connaître les marques (distances) de ses voisins.

Ces deux fonctionnements correspondent aux deux familles de protocoles de [[Routage dynamique|routage dynamique]] [[Complément hors du cours|ⓘ]] :
- [[Routage à état de liens|routage à état de liens]] ([[OSPF]], IS-IS) : chaque [[Routeur|routeur]] reçoit la carte complète de sa zone et y lance Dijkstra en se prenant pour source ;
- [[Routage à vecteur de distances|routage à vecteur de distances]] (RIP) : chaque routeur n'échange que ses distances avec ses voisins, ce qui revient à exécuter Bellman-Ford de façon répartie (voir [[Informatique distribuée]]). RIP compte la distance en nombre de sauts, chaque lien valant 1.

Dans les messages échangés entre [[Nœud (réseau)|nœuds]], les données voyagent par [[Commutation de paquets|commutation de paquets]] ; le calcul des plus courts chemins sert à remplir la [[Routage statique|table de routage]] de chaque routeur, qui indique le prochain saut vers chaque destination. [[Complément hors du cours|ⓘ]]

## Amélioration pour le routage

Pour le [[Routage dynamique|routage]], l'[[Algorithme de Bellman-Ford|algorithme de Bellman-Ford]] se perfectionne ainsi.

**Calcul de $D[v]$ à l'étape $i$** : il se fait à partir des distances $D[u]$ des voisins. *Si aucune distance n'a changé, le calcul est inutile.*

D'où une nouvelle approche :
- chaque [[Sommet et arête|sommet]] dont la distance change **informe ses voisins** ;
- si aucune distance n'est modifiée, l'algorithme **s'arrête**.

### Version R1

[[Pseudo-code]], avec l'initialisation et la mise à jour de `pred`, que la fonction renvoie : [[Erreurs du cours#^e-4-bellman-ford|✎]]

```text
algorithme BELLMAN-FORD-R1(G, s)                 G = (S, A, w)
    pour chaque v ∈ S faire
        D[v] := ∞
        pred[v] := NONE
    D[s] := 0
    pour i := 1, ..., n − 1 faire
        pour chaque u ∈ S tel que D[u] a changé à l'étape i − 1 faire
            pour chaque (u, v) ∈ A faire
                si D[v] > D[u] + w(u, v) alors
                    D[v] := D[u] + w(u, v)
                    pred[v] := u
        si D n'a pas été modifié à l'étape i alors
            break
    fin faire
    renvoyer (D, pred)
fin algo
```

À l'étape 1, le seul sommet « qui a changé » est $s$, posé à 0 lors de l'[[Initialisation (programmation)|initialisation]]. L'instruction `break` (voir [[Instructions break et continue]]) réalise l'arrêt anticipé : la [[Boucle (programmation)|boucle]] s'interrompt dès qu'une étape ne modifie rien. [[Complément hors du cours|ⓘ]]

### Version asynchrone

**[[Notification|Notifications]]** :
- avertir les nœuds voisins d'un changement ;
- les notifications ne sont pas synchronisées ;
- d'où une version [[Communication asynchrone|asynchrone]] de l'algorithme : nœuds **actifs** / **inactifs**.

```text
algorithme BELLMAN-FORD-Asynchrone(G, s)          G = (S, A, w)
    pour chaque v ∈ S faire
        D[v] := ∞, pred[v] := NONE
    D[s] := 0
    F := {s}                          F : ensemble des nœuds actifs
    tant que F ≠ ∅ faire
        choisir et enlever un sommet u de F
        pour chaque arc (u, v) faire
            si D[v] > D[u] + w(u, v) alors
                D[v] := D[u] + w(u, v)
                pred[v] := u
                F := F ∪ {v}          v devient actif
            fin si
        fin pour
    fin tant que
    renvoyer (D, pred)
fin algo
```

$F$ est un [[Ensemble (mathématiques)|ensemble]] : un sommet déjà actif n'y figure qu'une fois. Gérée comme une file FIFO (voir [[Pile et file]]), cette version est l'algorithme connu sous le nom de [[Algorithme SPFA|SPFA]] (*Shortest Path Faster Algorithm*) ; sa [[Complexité algorithmique|complexité]] dans le pire cas reste $O(mn)$, mais elle est souvent bien plus rapide en pratique. Sur l'exemple ci-dessus, avec une file, elle obtient les mêmes $D$ et $pred$ en 11 extractions de sommets. [[Complément hors du cours|ⓘ]]

Attention à la [[Terminaison d'un algorithme|terminaison]] : s'il existe un [[Circuit absorbant|circuit absorbant]] accessible depuis $s$, ses sommets redeviennent actifs indéfiniment et la boucle `tant que` ne s'arrête jamais. On borne alors le nombre de fois où un sommet entre dans $F$ ($n$ fois au plus sans circuit absorbant). [[Complément hors du cours|ⓘ]]

**Dans les vrais réseaux : le comptage à l'infini.** Dans un protocole à [[Routage à vecteur de distances|vecteur de distances]], quand un lien tombe, les [[Routeur|routeurs]] peuvent se renvoyer des distances périmées qui augmentent d'un cran à chaque échange : c'est le [[Comptage à l'infini|comptage à l'infini]], qui crée des [[Boucle de routage|boucles de routage]] et ralentit la [[Convergence d'un protocole de routage|convergence]]. RIP le limite en fixant l'infini à 16 sauts et par l'*horizon partagé* (*split horizon*) : ne pas réannoncer une route au voisin dont on la tient. [[Complément hors du cours|ⓘ]]

## Voir aussi

- [[4 - dijkstra]] : l'autre algorithme de plus court chemin, pour les poids positifs.
- [[4 - oriented graphs]] : chemins, circuits, [[Parcours en largeur|parcours en largeur]] (plus courts chemins en nombre d'arcs).
- Concepts : [[Algorithme de Bellman-Ford]], [[Plus court chemin]], [[Programmation dynamique]], [[Relâchement d'un arc]], [[Circuit absorbant]], [[Arbre des plus courts chemins]], [[Algorithme de Floyd-Warshall]], [[Routage à vecteur de distances]].
