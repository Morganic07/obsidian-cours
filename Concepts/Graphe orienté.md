---
type: concept
aliases: [graphes orientés, oriented graph, directed graph, graphe dirigé, parcours en profondeur, parcours en largeur, DFS, BFS, composante fortement connexe, strongly connected component, algorithme de Tarjan, degré entrant, degré sortant]
matieres: [graph theory]
sources: ["[[chp4 - oriented graphs]]"]
maj: 2026-11-05
---

Un graphe orienté $G = (V, A)$ a des arcs $A \subseteq V \times V$. Un **chemin** suit les arcs dans leur sens (élémentaire : sans répéter de sommet, simple : sans répéter d'arc) ; un **circuit** est un chemin fermé.

**Degrés** : $d^-(v)$ arcs entrants, $d^+(v)$ arcs sortants, avec $\sum d^+ = \sum d^- = |A|$.

**Parcours** : en profondeur (DFS, récursif) et en largeur (BFS, avec une file), tous deux en $O(|V| + |E|)$ avec des listes d'adjacence.

**Composante fortement connexe** : sous-graphe maximal où tout sommet atteint tout autre. Celle de $v$ est $\{v\} \cup (A(v) \cap D(v))$ avec $A(v)$ les ancêtres et $D(v)$ les descendants. Tarjan la calcule en $O(V + E)$.

Liens : [[Graphe non orienté]], [[Complexité algorithmique]]

Résumé : [[chp4 - oriented graphs (résumé)]]
