---
type: concept
tags: [year4]
aliases: [FP-Growth, FP-tree, frequent pattern growth]
sources: ["[[Raw/Year 4/data mining/chp 2 - association rules.pdf|chp 2 - association rules.pdf]]"]
maj: 2026-11-18
---

**Définition (complément, hors du cours)** : algorithme d'extraction des [[Itemset fréquent|itemsets fréquents]] proposé par Jiawei Han, Jian Pei et Yiwen Yin (SIGMOD, 2000). Il lit la base deux fois : une fois pour compter les items, une fois pour la compresser dans un **FP-tree**, [[Arbre (théorie des graphes)|arbre]] de préfixes où les transactions qui commencent par les mêmes items fréquents partagent un chemin. Il extrait ensuite les itemsets fréquents récursivement, par des bases conditionnelles, sans générer de candidats. Il trouve les mêmes itemsets que l'[[Algorithme Apriori]], en général beaucoup plus vite quand les itemsets fréquents sont nombreux ou longs.

## Dans le cours

Absent du cours de data mining, qui ne présente qu'Apriori ; il est cité en complément de [[2 - association rules]] parmi les alternatives à Apriori.

Notion parente : [[Règle d'association]]. Voir aussi : [[Explosion combinatoire]].

Résumés : [[2 - association rules]]
