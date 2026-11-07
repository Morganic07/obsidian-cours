---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres.pdf]]"]
maj: 2026-11-07
complet: true
---

Résumé du PDF Chapitre3-Arbres ([[Raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres.pdf]]) (29 diapositives, « Chapitre 3 : Graphes et arbres », groupe ID2), dans [[Cours/Informatique/Algo/_index|Algo]].

## Idée générale

Le chapitre rappelle le vocabulaire des graphes, puis définit l'arbre comme un graphe particulier et donne le vocabulaire des arbres.

## 1. Rappel sur les graphes

### Graphe orienté et non orienté

- Un **graphe orienté** $G$ est représenté par un couple $(S, A)$ où $S$ est un ensemble fini et $A$ une [[Relation binaire|relation binaire]] sur $S$. $S$ est l'ensemble des **sommets** de $G$, $A$ l'ensemble des **arcs**.
- Deux types de graphes :
  - [[Graphe orienté|graphe orienté]] : les relations sont orientées, on parle d'**arc** ; un arc est un couple de sommets **ordonnés** ;
  - [[Graphe non orienté|graphe non orienté]] : les relations ne sont pas orientées, on parle d'**arêtes** ; une arête est une paire de sommets **non ordonnés**.

![[Chapitre3-Arbres - p2.jpg]]
*Figure : exemple de graphe orienté.*

![[Chapitre3-Arbres - p3.jpg]]
*Figure : exemple de graphe non orienté.*

### Boucle

Une **boucle** est un arc qui relie un sommet à lui-même. Dans un graphe non orienté, les boucles sont interdites : chaque arête est constituée de deux sommets distincts.

![[Chapitre3-Arbres - p4.jpg]]
*Figure : graphe sur les sommets a à e avec une boucle $(a ; a)$ en rouge.*

### Degré d'un sommet

Voir [[Degré d'un sommet]].

- **Graphe non orienté** : le degré d'un sommet est le nombre d'arêtes qui lui sont incidentes. Un sommet de degré 0 est dit **isolé**.

![[Chapitre3-Arbres - p5.jpg]]
*Figure : graphe non orienté sur a à e ; le sommet e, surligné, est de degré 3.*

- **Graphe orienté** : nombre d'arcs arrivant à un sommet ou partant de lui.

![[Chapitre3-Arbres - p6.jpg]]
*Figure : graphe orienté sur a à e ; le sommet d, surligné, est de degré 2.*

- **Degré sortant** : nombre d'arcs qui partent du sommet.
- **Degré entrant** (« rentrant » sur la diapositive) : nombre d'arcs qui y arrivent.
- Le **degré** est la somme du degré entrant et du degré sortant.

### Chemin

**Définition.** Dans un graphe orienté $G = (S, A)$, un [[Chemin (graphe)|chemin]] de longueur $k$ d'un sommet $u$ à un sommet $v$ est une séquence $(u_0, u_1, \dots, u_k)$ de sommets telle que $u = u_0$, $v = u_k$ et $(u_{i-1}, u_i) \in A$ pour tout $i$. Un chemin est **élémentaire** si ses sommets sont tous distincts.

![[Chapitre3-Arbres - p9.jpg]]
*Figure : graphe orienté de l'exemple, sommets 1 à 6, avec une boucle sur 6.*

Exemple, sur ce graphe :

- un chemin élémentaire : $\langle 1, 4, 2, 5 \rangle$ ;
- un chemin non élémentaire : $\langle 3, 6, 6, 6 \rangle$.

**Sous-chemin.** Un sous-chemin $p_0$ d'un chemin $p = (u_0, u_1, \dots, u_k)$ est une sous-séquence contiguë de ses sommets : il existe $i$ et $j$, $0 \le i \le j \le k$, tels que $p_0 = (u_i, u_{i+1}, \dots, u_j)$.

### Circuit

**Définition.** Dans un graphe orienté $G = (S, A)$, un chemin $(u_0, u_1, \dots, u_k)$ forme un [[Circuit (graphe)|circuit]] si $u_0 = u_k$ et si le chemin contient au moins un arc. Ce circuit est élémentaire si les sommets $u_0, \dots, u_k$ sont distincts. Une boucle est un circuit de longueur 1.

![[Chapitre3-Arbres - p13.jpg]]
*Figure : même graphe 1 à 6, exemple de circuits.*

- Circuit élémentaire : $\langle 1, 2, 5, 4, 1 \rangle$ ;
- circuit non élémentaire : $\langle 1, 2, 5, 4, 2, 5, 4, 1 \rangle$.

### Cycle

**Définition.** Dans un graphe non orienté $G = (S, A)$, une [[Chaîne (graphe)|chaîne]] $(u_0, u_1, \dots, u_k)$ forme un [[Cycle (graphe)|cycle]] si $k \ge 2$ et si $u_0 = u_k$. Ce cycle est élémentaire si les sommets $u_0, \dots, u_k$ sont distincts. Un graphe sans cycle est dit **acyclique**.

![[Chapitre3-Arbres - p14.jpg]]
*Figure : graphe non orienté sur a à e ; a-b-e-a est un cycle de longueur 3.*

Exemple : a-b-e-a est un cycle qui part de a ; il est de longueur 3.

### Sous-graphe

**Définition.** $G_0 = (S_0, A_0)$ est un [[Sous-graphe|sous-graphe]] de $G = (S, A)$ si $S_0 \subset S$ et $A_0 \subset A$.

![[Chapitre3-Arbres - p15.jpg]]
*Figure : un graphe G sur a à e et un sous-graphe G' sur a, b, e, d.*

## 2. Les arbres

### Propriétés des arbres

Soit $G = (S, A)$ un graphe non orienté. Les affirmations suivantes sont **équivalentes** (voir [[Arbre (théorie des graphes)]]) :

1. $G$ est un arbre.
2. Deux sommets quelconques de $G$ sont reliés par un unique chemin élémentaire.
3. $G$ est acyclique et $|A| = |S| - 1$.
4. $G$ est acyclique, mais si une arête quelconque est ajoutée à $A$, le graphe résultant contient un cycle.

### Qu'est-ce qu'un arbre ?

- Une structure de données **non linéaire**, naturellement **récursive** (voir [[Récursivité]]).
- Une organisation **hiérarchique** entre les données stockées.
- Utilisée pour structurer des données : système de fichiers, base de données, sites web, fichiers XML.
- Un arbre est une structure de données (souvent dynamique) représentant un ensemble de valeurs organisées hiérarchiquement. Chaque valeur est stockée dans un **nœud** ; les nœuds sont connectés par des **arêtes** qui représentent la relation parent/fils.

**Exemple.** L'explorateur de fichiers de Windows propose une structure arborescente (voir [[Arborescence des répertoires Linux]] pour l'équivalent Linux). La racine d'une partition, notée `C:`, est la racine de l'arbre. Les répertoires comme `Programmes` ou `Windows` sont des nœuds ; chaque répertoire peut contenir des sous-répertoires, qui sont aussi des nœuds, et ainsi de suite. Les fichiers sont les feuilles.

![[Chapitre3-Arbres - p19.jpg]]
*Figure : arborescence de fichiers : `C:` à la racine, puis `Windows`, `Users`, `Programs`, et des sous-répertoires (`System32`, `Python 3.7`…).*

### Vocabulaire

Voir [[Vocabulaire des arbres]].

- **Racine** : le nœud qui n'a pas de prédécesseur (parent) et possède 0 ou plusieurs fils. La racine constitue la caractéristique d'un arbre.
- **Feuille** : un nœud qui n'a pas de successeur (fils). Aussi appelée **nœud externe**.
- **Nœud interne** : tout nœud qui admet au moins un fils.
- Un nœud peut avoir un nombre arbitraire d'enfants.
- **Arité d'un nœud** $n$ : nombre de fils de $n$.
- **Arité d'un arbre** $a$ : nombre maximal de fils d'un nœud de $a$.

![[Chapitre3-Arbres - p20.jpg]]
*Figure : arbre exemple de racine A ; racine, nœuds internes et feuilles (en rouge) étiquetés.*

L'arbre exemple : A a pour fils B, C, D ; B a pour fils E ; D a pour fils F, G, H, I ; G a pour fils J, K ; I a pour fils L.

![[Chapitre3-Arbres - p21.jpg]]
*Figure : le même arbre, support des définitions de sous-arbre, branche, descendants et ascendants.*

- **Sous-arbre** : une portion de l'arbre. Le nœud G avec ses deux fils J et K constitue un sous-arbre.
- **Branche** : une suite de nœuds connectés de père en fils, de la racine à une feuille : A-B-E ; A-C ; A-D-F ; A-D-G-J ; …
- **Descendants d'un nœud** : tous les nœuds du sous-arbre de racine ce nœud. Les descendants de D sont F, G, H, I, J, K et L.
- **Ascendants d'un nœud** : tous les nœuds sur la branche de la racine vers ce nœud. Les ascendants de J sont G, D et A.
- **Taille de l'arbre** : son nombre de nœuds. Taille de l'arbre exemple : 12 ; taille d'un arbre vide : 0.
- **Degré d'un nœud** : le nombre de ses fils. Degré de B : 1 ; degré de D : 4.
- **Degré d'un arbre** : le degré maximum de ses nœuds. Degré de l'arbre exemple : 4.
- **Niveau d'un nœud** : la distance qui le sépare de la racine. Niveau de la racine : 0 ; le niveau de chaque nœud est celui de son père plus 1 ; le niveau de G est 2.

![[Chapitre3-Arbres - p23.jpg]]
*Figure : niveaux de l'arbre exemple : A au niveau 0 ; B, C, D au niveau 1 ; E, F, G, H, I au niveau 2 ; J, K, L au niveau 3.*

### Définition récursive

**Cas général.** Si $n$ est un nœud et si $T_1, T_2, \dots, T_m$ sont des arbres, on construit un nouvel arbre en connectant $T_1, T_2, \dots, T_m$ comme fils de $n$. Chaque $T_i$ est défini récursivement de la même manière. $T_1, \dots, T_m$ sont alors des sous-arbres de $n$.

![[Chapitre3-Arbres - p24.jpg]]
*Figure : un arbre vu comme une racine reliée aux racines de ses sous-arbres $T_1$, $T_2$…, eux-mêmes composés de sous-arbres emboîtés.*

### Hauteur

Voir [[Hauteur d'un arbre]].

- **Hauteur d'un arbre** : la profondeur maximale de ses nœuds.
- Un arbre à un seul nœud est de hauteur 0.
- L'arbre vide est de hauteur $-1$.

### Familles d'arbres

- **[[Arbre m-aire|Arbre $m$-aire]]** : arbre d'ordre $m$ dont le degré maximum d'un nœud est égal à $m$.
- **[[B-arbre]]** : un B-arbre d'ordre $n$ est un arbre où :
  - la racine a au moins deux fils ;
  - chaque nœud autre que la racine a entre $n/2$ et $n$ fils ;
  - tous les nœuds feuilles sont au même niveau.
- **[[Arbre binaire]]** : arbre où le degré maximum d'un nœud est égal à 2.
- **[[Arbre binaire de recherche]]** : arbre binaire où la clé de chaque nœud est supérieure à celle de ses descendants gauches et inférieure à celle de ses descendants droits.

### Arbre enraciné (arborescence)

**Définition.** Un arbre enraciné, ou [[Arborescence (graphe)|arborescence]], est un arbre dans lequel l'un des sommets, la **racine**, se distingue des autres. Ce sommet impose un sens de parcours de l'arbre.

Autrement dit, une arborescence est un graphe orienté sans circuit admettant une racine $s_0 \in S$ telle que, pour tout autre sommet $s_i \in S$, il existe un chemin unique de $s_0$ vers $s_i$. Si l'arborescence comporte $n$ sommets, elle comporte exactement $n - 1$ arcs.

![[Chapitre3-Arbres - p28.jpg]]
*Figure : exemple d'arborescence de racine a.*

- **Ancêtre** : soit $x$ un nœud d'un arbre $A$ de racine $r$. Tout nœud $y$ sur l'unique chemin de $r$ à $x$ est un ancêtre de $x$.
- **Père et fils** : si $(y, x)$ est un arc, $y$ est le père de $x$ et $x$ est le fils de $y$. La racine est le seul nœud qui n'a pas de père.

## Liens

Suite du cours : [[4 - Arbres binaires]] sur les [[Arbre binaire|arbres binaires]], puis [[5 - ABR]] sur l'[[Arbre binaire de recherche]].
