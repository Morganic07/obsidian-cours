---
type: concept
tags: [year4]
aliases: [complete graph]
sources: ["[[1 - Undirected graph|Chp 1 - Undirected graph]]"]
maj: 2026-11-06
---

[[Graphe simple]] où toute paire de sommets est adjacente : $\text{card}(E) = \binom{n}{2}$. Un graphe simple a au plus $\frac{n(n-1)}{2}$ arêtes.

Dans un graphe simple complet, chaque sommet est de [[Degré d'un sommet|degré]] $n - 1$ : la remarque vient de la note de l'étudiante, et le TP la reprend dans les fonctions `isGraphFull` et `infoGraphFull`.

**Coloration** : au chapitre 5 ([[5 - colorier graph]]), le cours établit $\chi(K_n) = n$ (voir [[Nombre chromatique]]) : tous les sommets étant adjacents, ils ont tous des couleurs différentes. Un graphe qui contient un sous-graphe complet à $p$ sommets ([[Clique (graphe)|clique]]) a donc $\chi(G) \geq p$.

Notion parente : [[Graphe simple]]. Voir aussi : [[Degré d'un sommet]].

Résumés : [[1 - Undirected graph]], [[0 - Graph - Python]], [[5 - colorier graph]]
