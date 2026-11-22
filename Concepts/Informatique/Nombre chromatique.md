---
type: concept
tags: [year4]
aliases: [chromatic number, χ(G)]
sources: ["[[Raw/Year 4/graph theory/chp5 - colorier graph.pdf|chp5 - colorier graph.pdf]]"]
maj: 2026-11-19
---

**Définition** (d'après [[5 - colorier graph]]) : le nombre chromatique $\chi(G)$ d'un graphe $G$ est le nombre minimum de couleurs d'une [[Coloration de graphe|coloration propre]] de $G$ :
$$\chi(G) = \min\{\text{card}(c(V)) \mid c \text{ coloration propre de } G\}$$

Propriétés données par le cours, pour un [[Graphe non orienté|graphe non orienté]] $G = (V, E)$ :
- **majorant** : $\chi(G) \leq \Delta + 1$, où $\Delta$ est le [[Degré d'un sommet|degré]] maximum ;
- **graphe complet** : $\chi(K_n) = n$ (voir [[Graphe complet]]) ;
- **croissance** : pour un [[Sous-graphe|sous-graphe]] $G'$ de $G$, $\chi(G') \leq \chi(G)$ ;
- **minorant** : si $G$ contient un sous-graphe complet à $p$ sommets ([[Clique (graphe)|clique]]), $\chi(G) \geq p$.

Compléments : en notant $\omega(G)$ la taille de la plus grande clique, $\omega(G) \leq \chi(G) \leq \Delta + 1$. Le [[Théorème de Brooks|théorème de Brooks]] (1941) abaisse le majorant à $\Delta$ pour tout [[Graphe connexe|graphe connexe]] qui n'est ni complet ni un cycle impair. $\chi(G) \leq 2$ si et seulement si $G$ est [[Graphe biparti|biparti]] ; $\chi(G) \leq 4$ pour tout [[Graphe planaire|graphe planaire]] ([[Théorème des quatre couleurs]]). Calculer $\chi(G)$ est NP-difficile (voir [[Classes P et NP]]). [[Complément hors du cours|ⓘ]]

## Dans le cours

Défini au chapitre 5 de Graph theory, avec la coloration optimale ; l'exercice 1 montre que l'[[Algorithme de Welsh-Powell|algorithme de Welsh-Powell]] peut utiliser plus de $\chi(G)$ couleurs.

Résumés : [[5 - colorier graph]]
