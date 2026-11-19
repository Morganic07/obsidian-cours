---
type: concept
tags: [year4]
aliases: [itemsets fréquents, frequent itemset, frequent itemsets, ensemble d'items fréquent, motif fréquent, frequent pattern, itemset, k-itemset]
matieres: [data mining]
sources: ["[[Raw/Year 4/data mining/chp 2 - association rules.pdf|chp 2 - association rules.pdf]]"]
maj: 2026-11-18
---

**Définition** (d'après [[2 - association rules]]) : un **item** est un atome du domaine (un produit, par exemple) ; un **ensemble d'items** (*itemset*) est une suite d'items rangés dans un ordre prédéfini. Un itemset est **fréquent** quand son [[Support (règle d'association)|support]], la proportion des [[Transaction (fouille de données)|transactions]] qui le contiennent, est supérieur ou égal au seuil `minSupp`. Les itemsets fréquents sont les motifs fréquents de la base.

Notations du cours : $L_k$ est l'ensemble des itemsets fréquents de longueur $k$, $C_k$ celui des candidats de longueur $k$, avec $L_k \subseteq C_k$.

**Exemple du cours** : sur les transactions {1, 3, 4}, {2, 3, 5}, {1, 2, 3, 5}, {2, 5} avec `minSupp` $= 2/4$, $L_1 = \{1, 2, 3, 5\}$, $L_2 = \{13, 23, 25, 35\}$, $L_3 = \{235\}$.

## Compléments (complément, hors du cours)

- Un itemset de $k$ items s'appelle un $k$-itemset. Avec $n$ items, il y a $2^n - 1$ itemsets non vides ([[Opérations sur les ensembles|ensemble des parties]]), d'où la nécessité d'élaguer ([[Explosion combinatoire]]).
- Tout sous-ensemble d'un itemset fréquent est fréquent ([[Propriété de fermeture descendante]]) ; on résume souvent la famille des itemsets fréquents par ses éléments **maximaux** (aucun sur-ensemble fréquent) ou **fermés** (aucun sur-ensemble de même support).

Notion parente : [[Règle d'association]]. Voir aussi : [[Algorithme Apriori]], [[Algorithme FP-Growth]].

Résumés : [[2 - association rules]]
