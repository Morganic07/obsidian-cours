---
type: concept
tags: [year4]
aliases: [Gini index, critère de Gini]
sources: ["[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]"]
maj: 2026-11-07
---

Critère d'impureté d'un nœud utilisé par CART :

$$IG(N_o) = 1 - \sum_{i=1}^{N_C} p_i^2$$

où $p_i$ est la fréquence de la classe $i$ dans le nœud. Plus il est petit, plus le nœud est pur. On cherche la variable qui maximise

$$IG(\text{avant}) - [W_1\, IG(\text{fils}_1) + W_2\, IG(\text{fils}_2)]$$

Pour deux classes, la courbe est une parabole de maximum 0,5.

Notion parente : [[Algorithme CART]]. Voir aussi : [[Entropie (théorie de l'information)]], [[Arbre de décision]].

Résumés : [[1 - intro to data mining]], [[1 - pdf du prof]]
