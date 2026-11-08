---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/graph theory/chp4 - oriented graphs.docx|chp4 - oriented graphs]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 4/graph theory/chp4 - oriented graphs.docx|chp4 - oriented graphs]], dans [[Cours/Informatique/Graph theory/_index|Graph theory]]. Cours en anglais. Images non ouvertes : lues par leur transcription. Voir [[Graphe orienté]].

## Idée générale

Graphes orientés : chemins, degrés entrants et sortants, parcours en profondeur et en largeur, composantes fortement connexes.

## Définition

Un **graphe orienté** (*oriented graph*) est, selon le cours, un graphe dirigé obtenu en donnant une direction à chaque arête d'un [[Graphe non orienté|graphe non orienté]]. Formellement, c'est un couple $G = (V, A)$ où :
- $V$ est un ensemble de **sommets** (*vertices*, voir [[Sommet et arête]]) ;
- $A \subseteq V \times V$ est un ensemble d'**arcs** orientés.

Vocabulaire d'un arc $(u, v)$, noté aussi $u \to v$ : $u$ est son **origine** (ou queue), $v$ son **extrémité** (ou tête) ; $v$ est un **successeur** de $u$ et $u$ un **prédécesseur** de $v$. Les « fils » (*children*) des pseudo-codes ci-dessous sont les successeurs. Comme $(u, v) \ne (v, u)$, l'ordre compte : $u \to v$ n'implique pas $v \to u$. [[Complément hors du cours|ⓘ]]

En anglais, *oriented graph* désigne au sens strict un graphe orienté sans paire d'arcs opposés ($u \to v$ et $v \to u$), ce qui correspond à la définition du cours (on oriente chaque arête dans **un** sens) ; le terme général est *directed graph* ou *digraph*, qui autorise les deux sens. Les exemples du cours (arcs $0 \to 4$ et $4 \to 0$) relèvent du sens général. [[Complément hors du cours|ⓘ]]

**Représentation en machine.** Un graphe orienté se stocke par sa [[Matrice d'adjacence|matrice d'adjacence]] $M$, avec $M_{i,j} = 1$ s'il existe un arc $v_i \to v_j$ et 0 sinon (elle n'est plus symétrique), ou par ses [[Liste d'adjacence|listes d'adjacence]], qui donnent pour chaque sommet la liste de ses successeurs (en Python, un dictionnaire `{0: [2, 5, 4], 1: [0], …}`). La matrice occupe $O(|V|^2)$ en mémoire et teste un arc en $O(1)$ ; les listes occupent $O(|V| + |A|)$ et sont préférées pour les graphes peu denses. [[Complément hors du cours|ⓘ]]

## Chemin et circuit

- **Chemin** (*path*) : suite de sommets $v_1, v_2, \ldots, v_k$ telle que pour tout $i$, $1 \le i < k$, il existe un arc de $v_i$ vers $v_{i+1}$. [[Erreurs du cours#^e-4-oriented-graphs|✎]] Voir [[Chemin (graphe)]].
  - Chemin **élémentaire** : ne répète pas de sommet.
  - Chemin **simple** : ne répète pas d'arc.
- **Circuit** : chemin **fermé**, qui commence et finit au même sommet. Voir [[Circuit (graphe)]].

Dans un graphe orienté, l'arc entre $v_i$ et $v_{i+1}$ doit aller **de $v_i$ vers $v_{i+1}$** : un chemin suit le sens des arcs. La **longueur** d'un chemin est son nombre d'arcs, $k - 1$ pour $v_1, \ldots, v_k$. Un sommet $v'$ est **accessible** depuis $v$ s'il existe un chemin de $v$ à $v'$ : c'est la relation qui sert plus bas aux descendants, aux ancêtres et aux composantes fortement connexes. [[Complément hors du cours|ⓘ]]

## Degrés d'un sommet

Soit $G = (V, A)$ un graphe orienté. Pour tout $v \in V$ (voir [[Degré d'un sommet]]) :
- **degré sortant** (*out-degree*) $d^+(v)$ : nombre d'arcs qui **partent** de $v$ ;
- **degré entrant** (*in-degree*) $d^-(v)$ : nombre d'arcs qui **arrivent** en $v$.

**Propriété :**
$$\sum_{v \in V} d^+(v) = \sum_{v \in V} d^-(v) = |A|$$
où $|A|$ est le nombre total d'arcs. *Interprétation* : chaque arc compte une fois dans le degré sortant de son origine et une fois dans le degré entrant de sa cible.

### Exemple

![[chp4 - oriented graphs - image2.png]]
*Figure : graphe orienté à 4 nœuds, arcs A→B, A→C, B→D, B→C (arc courbe) et C→D, avec son tableau de degrés.*

| Nœud | $d^-$ | $d^+$ |
|---|---|---|
| A | 0 | 2 |
| B | 1 | 2 |
| C | 2 | 1 |
| D | 2 | 0 |

Vérification : $\sum d^- = \sum d^+ = 5 = |A|$.

Un sommet de degré entrant nul est une **source** (ici A), un sommet de degré sortant nul un **puits** (ici D). Avec la matrice d'adjacence, $d^+(v_i)$ est la somme de la ligne $i$ et $d^-(v_i)$ la somme de la colonne $i$. [[Complément hors du cours|ⓘ]]

## Parcours en profondeur (DFS, *depth first search*)

Voir [[Parcours en profondeur]].

**Pseudo-code** `DFS(graph, v)` :
1. marquer $v$ comme visité ;
2. `print(v)` ;
3. pour chaque fils (*child*) de $v$ : s'il n'a pas été visité, appeler `DFS(graph, child)`.

![[chp4 - oriented graphs - image9.png]]
*Figure : graphe orienté à 7 sommets (0 à 6), arcs 1→0, 0→2, 0→5, 0→4, 4→0, 2→1, 2→5, 3→1, 3→6, 6→3, 4→5 et 6→5.*

Sur ce graphe, un DFS partant de 0 **peut** visiter les sommets dans l'ordre **0, 2, 1, 5, 4** (3 et 6 ne sont pas atteignables depuis 0).

Déroulé de cet ordre, en prenant les fils de 0 dans l'ordre 2, 5, 4 : on visite 0, puis son fils 2 ; depuis 2, on visite 1, dont le seul fils (0) est déjà visité ; on revient à 2 et on visite 5, qui n'a pas de successeur ; on revient à 0, dont le fils 5 est déjà visité, et on visite 4, dont les fils 0 et 5 sont déjà visités. Le parcours va **le plus loin possible** avant de revenir en arrière (*backtracking*). [[Complément hors du cours|ⓘ]]

**Complexité** : $O(|V| + |E|)$, car chaque sommet est visité une seule fois et chaque arête explorée une seule fois ($V$ = sommets, $E$ = arêtes).

Cette borne suppose des [[Liste d'adjacence|listes d'adjacence]] : avec une matrice d'adjacence, chercher les fils d'un sommet oblige à lire toute sa ligne, et le parcours coûte $O(|V|^2)$. Le même raisonnement vaut pour le BFS. [[Complément hors du cours|ⓘ]]

La version récursive s'appuie sur la [[Pile d'exécution|pile d'exécution]] ; on peut l'écrire de façon itérative avec une [[Pile et file|pile]] explicite, la file du BFS remplacée par une pile. Le DFS sert de base à de nombreux algorithmes : détection de circuit (le parcours rencontre un arc vers un sommet dont l'exploration n'est pas terminée), [[Tri topologique|tri topologique]], calcul des composantes fortement connexes (Tarjan, ci-dessous). [[Complément hors du cours|ⓘ]]

## Parcours en largeur (BFS, *breadth first search*)

Voir [[Parcours en largeur]] et [[Pile et file]].

**Pseudo-code** `BFS(graph, start_node)` :
1. créer une **file** (*queue*) et y enfiler `start_node` ;
2. marquer `start_node` comme visité ;
3. tant que la file n'est pas vide :
   - défiler un nœud $v$ ;
   - `print(v)` ;
   - pour chaque fils de $v$ : s'il n'a pas été visité, le marquer comme visité et l'enfiler.

Le sommet est **marqué à l'entrée dans la file** et **affiché à la sortie**.

**Complexité** : $O(|V| + |E|)$, pour les mêmes raisons que le DFS.

Sur le graphe à 7 sommets, en prenant les fils dans l'ordre 2, 5, 4, un BFS depuis 0 donne 0, 2, 5, 4, 1. [[Complément hors du cours|ⓘ]]

Le BFS visite les sommets **par distance croissante** au départ : d'abord ceux à un arc (2, 5, 4), puis ceux à deux arcs (1). Il donne donc les **plus courts chemins en nombre d'arcs** depuis `start_node`, ce que le DFS ne garantit pas ; pour des arcs pondérés, il faut un autre algorithme (Dijkstra, pour des poids positifs). [[Complément hors du cours|ⓘ]]

## Composantes fortement connexes (SCC)

**Définition.** Une **[[Composante fortement connexe|composante fortement connexe]]** (*strongly connected component*, SCC) d'un graphe orienté $G = (V, E)$ est un [[Sous-graphe|sous-graphe]] **maximal** $G' = (V', E')$ tel que :
- pour toute paire de sommets $u, v \in V'$, il existe un chemin orienté de $u$ vers $v$ **et** un de $v$ vers $u$ ;
- $G'$ est maximal : on ne peut ajouter aucun sommet à $V'$ sans perdre la forte connexité.

![[chp4 - oriented graphs - image7.png]]
*Figure : graphe orienté à 8 sommets (A à H), arcs A→B, A→E, B→C, B→E, C→F, C→G, D→G, D→H, E→F, F→B, G→F et H→G ; zones violettes pour les SCC : $\{B, C, E, F, G\}$, et trois composantes à un sommet $\{A\}$, $\{D\}$, $\{H\}$.*

Pourquoi $\{B, C, E, F, G\}$ : les circuits $B \to C \to F \to B$, $B \to E \to F \to B$ et $C \to G \to F \to B \to C$ relient ces cinq sommets dans les deux sens. A n'a aucun arc entrant, D non plus, et H n'est atteint que depuis D : aucun des trois n'est sur un circuit, chacun forme seul sa composante. [[Complément hors du cours|ⓘ]]

La relation « $u$ et $v$ sont mutuellement accessibles » est une [[Relation d'équivalence|relation d'équivalence]] sur $V$ ; ses classes sont les SCC, qui forment donc une **partition** des sommets : chaque sommet appartient à une et une seule SCC. Le graphe est **fortement connexe** s'il n'a qu'une seule SCC. [[Complément hors du cours|ⓘ]]

En contractant chaque SCC en un seul sommet, on obtient le **graphe réduit** (ou condensation), qui est toujours **sans circuit** : un circuit entre deux SCC les fusionnerait en une seule. Sur l'exemple : $\{A\} \to \{B, C, E, F, G\}$, $\{D\} \to \{B, C, E, F, G\}$, $\{D\} \to \{H\}$ et $\{H\} \to \{B, C, E, F, G\}$. [[Complément hors du cours|ⓘ]]

Un graphe orienté sans circuit (*DAG*, *directed acyclic graph*) admet un **[[Tri topologique|tri topologique]]** : un ordre des sommets où tout arc va d'un sommet à un sommet placé après lui. On l'obtient en $O(|V| + |E|)$, soit en retirant une à une les sources (algorithme de Kahn), soit en rangeant les sommets par date de fin décroissante d'un DFS. Il sert à ordonner des tâches qui dépendent les unes des autres (prérequis de cours, compilation de modules, installation de paquets). Sur le graphe réduit ci-dessus : $\{A\}, \{D\}, \{H\}, \{B, C, E, F, G\}$. [[Complément hors du cours|ⓘ]]

### Algorithme 1 : descendants et ancêtres

Soit $G = (V, E)$ orienté. Pour chaque sommet $v$ :
- **descendants** de $v$ : $D(v) = \{ v' \in V \mid v\ \sigma\ v' \}$, où $\sigma$ est un chemin qui permet d'atteindre $v'$ depuis $v$ ;
- **ancêtres** de $v$ : $A(v) = \{ v' \in V \mid v'\ \sigma\ v \}$.

**Principe** : depuis un sommet $v$, on calcule la SCC qui le contient :
1. calculer $D(v)$ (par exemple par un parcours depuis $v$) ;
2. calculer $A(v)$ ;
3. la SCC contenant $v$ est
$$\{v\} \cup (A(v) \cap D(v)).$$

Pour calculer $A(v)$, on fait un parcours depuis $v$ dans le **graphe transposé** $G^T$ (tous les arcs inversés) : les sommets atteints sont ceux qui atteignent $v$ dans $G$. Chaque SCC coûte ainsi deux parcours, $O(|V| + |E|)$ ; en recommençant depuis un sommet pas encore classé jusqu'à épuisement, on obtient toutes les SCC en $O(|V| \cdot (|V| + |E|))$ au pire. [[Complément hors du cours|ⓘ]]

Exemple sur le graphe à 8 sommets avec $v = B$ : $D(B) = \{B, C, E, F, G\}$ (les arcs sortant de ces sommets ne mènent qu'entre eux) et $A(B) = \{A, B, C, D, E, F, G, H\}$, d'où la SCC $\{B\} \cup (A(B) \cap D(B)) = \{B, C, E, F, G\}$. [[Complément hors du cours|ⓘ]]

### Algorithme de Tarjan

L'[[Algorithme de Tarjan|algorithme de Tarjan]] s'exécute en temps $O(V + E)$ ($V$ sommets, $E$ arêtes) ; sa complexité en espace est $O(V)$, à cause de la pile et des tableaux qui stockent les indices et les *lowlinks*. Le cours n'en décrit pas le fonctionnement.

Principe, publié par Robert Tarjan en 1972 : un seul DFS, au cours duquel : [[Complément hors du cours|ⓘ]]
1. chaque sommet reçoit, à sa découverte, un **indice** (son numéro d'ordre de visite) et est empilé sur une pile ; [[Complément hors du cours|ⓘ]]
2. son ***lowlink*** est le plus petit indice d'un sommet encore sur la pile qu'on peut atteindre depuis lui en descendant dans le parcours puis en suivant au plus un arc « retour » ; on l'initialise à son indice et on le met à jour au retour de chaque fils (minimum avec le *lowlink* du fils) ou en rencontrant un arc vers un sommet déjà sur la pile (minimum avec l'indice de ce sommet) ; [[Complément hors du cours|ⓘ]]
3. quand l'exploration de $v$ est finie et que $\text{lowlink}(v) = \text{indice}(v)$, $v$ est la **racine** d'une SCC : on dépile jusqu'à $v$ inclus, et les sommets dépilés forment cette SCC. [[Complément hors du cours|ⓘ]]

Chaque sommet est empilé et dépilé une fois, chaque arc examiné une fois : d'où le $O(V + E)$. [[Complément hors du cours|ⓘ]]

Autre méthode classique, l'**algorithme de Kosaraju**, également en $O(V + E)$ : un premier DFS sur $G$ note l'ordre de fin des sommets ; un second DFS sur le graphe transposé $G^T$, lancé depuis les sommets par date de fin décroissante, découvre exactement une SCC à chaque nouveau départ. Il prolonge l'idée de l'algorithme 1 (parcours de $G$ et de $G^T$) sans le refaire pour chaque sommet. [[Complément hors du cours|ⓘ]]
