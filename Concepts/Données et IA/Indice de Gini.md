---
type: concept
tags: [year4]
aliases: [Gini index, critère de Gini]
sources: ["[[raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof]]"]
maj: 2026-11-06
---

Critère d'impureté d'un nœud utilisé par CART :

$$IG(N_o) = 1 - \sum_{i=1}^{N_C} p_i^2$$

où $p_i$ est la fréquence de la classe $i$ dans le nœud. Plus il est petit, plus le nœud est pur. On cherche la variable qui maximise

$$IG(\text{avant}) - [W_1\, IG(\text{fils}_1) + W_2\, IG(\text{fils}_2)]$$

Pour deux classes, la courbe est une parabole de maximum 0,5.

Notion parente : [[Algorithme CART]]. Voir aussi : [[Entropie (théorie de l'information)]], [[Arbre de décision]].

## À vérifier

- Le calcul du fils « false » écrit $(2/8)^2 + (6/8)^2$ dans l'ordre inverse de l'arbre, sans incidence sur le résultat (relevé du résumé).

Résumés : [[Chp1 - intro to data mining (résumé)]], [[cours data mining du prof (résumé)]]
