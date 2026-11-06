---
type: concept
aliases: [graphes orientés, oriented graph, directed graph, graphe dirigé, degré entrant, degré sortant, arc, arcs, degré rentrant]
matieres: [graph theory, Algo]
sources: ["[[chp4 - oriented graphs]]", "[[raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres]]"]
maj: 2026-11-06
---

Un graphe orienté $G = (V, A)$ a des arcs $A \subseteq V \times V$. Un **chemin** suit les arcs dans leur sens (élémentaire : sans répéter de sommet, simple : sans répéter d'arc) ; un **circuit** est un chemin fermé.

En Algo (chapitre sur les arbres), le graphe orienté est un couple $(S, A)$ où $S$ est un ensemble fini de sommets et $A$ une relation binaire sur $S$ (les arcs). Une boucle relie un sommet à lui-même.

**Degrés** : $d^-(v)$ arcs entrants, $d^+(v)$ arcs sortants, avec $\sum d^+ = \sum d^- = |A|$. Le cours d'Algo dit « degré rentrant » pour le degré entrant, et appelle degré la somme des deux.

**Parcours** : [[Parcours en profondeur]] (DFS, récursif) et [[Parcours en largeur]] (BFS, avec une file), tous deux en $O(|V| + |E|)$ avec des listes d'adjacence.

**[[Composante fortement connexe]]** : sous-graphe maximal où tout sommet atteint tout autre. Celle de $v$ est $\{v\} \cup (A(v) \cap D(v))$ avec $A(v)$ les ancêtres et $D(v)$ les descendants. L'[[Algorithme de Tarjan]] la calcule en $O(V + E)$.

Voir aussi : [[Graphe non orienté]], [[Complexité algorithmique]], [[Chemin (graphe)]], [[Circuit (graphe)]], [[Degré d'un sommet]], [[Arborescence (graphe)]].

## À vérifier

- L'exemple de DFS du cours de graph theory contient $0 \to 4$ et $4 \to 0$ : graphe orienté au sens large, pas « oriented graph » au sens strict (relevé du résumé [[chp4 - oriented graphs (résumé)]]).

Résumés : [[chp4 - oriented graphs (résumé)]], [[Chapitre3-Arbres (résumé)]]
