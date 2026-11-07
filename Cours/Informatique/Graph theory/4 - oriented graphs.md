---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/graph theory/chp4 - oriented graphs.docx|chp4 - oriented graphs]]"]
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 4/graph theory/chp4 - oriented graphs.docx|chp4 - oriented graphs]], dans [[Cours/Informatique/Graph theory/_index|Graph theory]]. Cours en anglais. En cas d'écart, le cours et ses images font foi. Images non ouvertes : lues par leur transcription. Voir [[Graphe orienté]].

## Idée générale

Graphes orientés : chemins, degrés entrants et sortants, parcours en profondeur et en largeur, composantes fortement connexes.

## Définition

Un **graphe orienté** (*oriented graph*) est, selon le cours, un graphe dirigé obtenu en donnant une direction à chaque arête d'un [[Graphe non orienté|graphe non orienté]]. Formellement, c'est un couple $G = (V, A)$ où :
- $V$ est un ensemble de **sommets** (*vertices*, voir [[Sommet et arête]]) ;
- $A \subseteq V \times V$ est un ensemble d'**arcs** orientés.

## Chemin et circuit

- **Chemin** (*path*) : suite de sommets $v_1, v_2, \ldots, v_k$ telle que pour tout $i$, $1 \le i < k$, un arc relie $v_i$ et $v_{i+1}$. Voir [[Chemin (graphe)]].
  - Chemin **élémentaire** : ne répète pas de sommet.
  - Chemin **simple** : ne répète pas d'arc.
- **Circuit** : chemin **fermé**, qui commence et finit au même sommet. Voir [[Circuit (graphe)]].

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

## Parcours en profondeur (DFS, *depth first search*)

Voir [[Parcours en profondeur]].

**Pseudo-code** `DFS(graph, v)` :
1. marquer $v$ comme visité ;
2. `print(v)` ;
3. pour chaque fils (*child*) de $v$ : s'il n'a pas été visité, appeler `DFS(graph, child)`.

![[chp4 - oriented graphs - image9.png]]
*Figure : graphe orienté à 7 sommets (0 à 6), arcs 1→0, 0→2, 0→5, 0→4, 4→0, 2→1, 2→5, 3→1, 3→6, 6→3, 4→5 et 6→5.*

Sur ce graphe, un DFS partant de 0 **peut** visiter les sommets dans l'ordre **0, 2, 1, 5, 4** (3 et 6 ne sont pas atteignables depuis 0).

**Complexité** : $O(|V| + |E|)$, car chaque sommet est visité une seule fois et chaque arête explorée une seule fois ($V$ = sommets, $E$ = arêtes).

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

(Complément, non donné par le cours : sur le graphe à 7 sommets, en prenant les fils dans l'ordre 2, 5, 4, un BFS depuis 0 donne 0, 2, 5, 4, 1.)

## Composantes fortement connexes (SCC)

**Définition.** Une **[[Composante fortement connexe|composante fortement connexe]]** (*strongly connected component*, SCC) d'un graphe orienté $G = (V, E)$ est un [[Sous-graphe|sous-graphe]] **maximal** $G' = (V', E')$ tel que :
- pour toute paire de sommets $u, v \in V'$, il existe un chemin orienté de $u$ vers $v$ **et** un de $v$ vers $u$ ;
- $G'$ est maximal : on ne peut ajouter aucun sommet à $V'$ sans perdre la forte connexité.

![[chp4 - oriented graphs - image7.png]]
*Figure : graphe orienté à 8 sommets (A à H), arcs A→B, A→E, B→C, B→E, C→F, C→G, D→G, D→H, E→F, F→B, G→F et H→G ; zones violettes pour les SCC : $\{B, C, E, F, G\}$, et trois composantes à un sommet $\{A\}$, $\{D\}$, $\{H\}$.*

### Algorithme 1 : descendants et ancêtres

Soit $G = (V, E)$ orienté. Pour chaque sommet $v$ :
- **descendants** de $v$ : $D(v) = \{ v' \in V \mid v\ \sigma\ v' \}$, où $\sigma$ est un chemin qui permet d'atteindre $v'$ depuis $v$ ;
- **ancêtres** de $v$ : $A(v) = \{ v' \in V \mid v'\ \sigma\ v \}$.

**Principe** : depuis un sommet $v$, on calcule la SCC qui le contient :
1. calculer $D(v)$ (par exemple par un parcours depuis $v$) ;
2. calculer $A(v)$ ;
3. la SCC contenant $v$ est
$$\{v\} \cup (A(v) \cap D(v)).$$

### Algorithme de Tarjan

L'[[Algorithme de Tarjan|algorithme de Tarjan]] s'exécute en temps $O(V + E)$ ($V$ sommets, $E$ arêtes) ; sa complexité en espace est $O(V)$, à cause de la pile et des tableaux qui stockent les indices et les *lowlinks*. Le cours n'en décrit pas le fonctionnement.
