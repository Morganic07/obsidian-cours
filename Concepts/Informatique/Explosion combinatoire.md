---
type: concept
tags: [year4]
aliases: [combinatorial explosion]
sources: ["[[Raw/Year 4/data mining/chp 2 - association rules.pdf|chp 2 - association rules.pdf]]"]
maj: 2026-11-18
---

**Définition (complément, hors du cours)** : croissance très rapide (exponentielle ou factorielle) du nombre de cas à examiner quand la taille d'un problème augmente, qui rend la [[Recherche exhaustive|recherche exhaustive]] impraticable. Exemple : avec $n$ items, il existe $2^n - 1$ itemsets non vides, soit plus de $10^{30}$ pour 100 produits ; un voyageur de commerce sur $n$ villes a $(n-1)!/2$ tournées. On y répond par l'élagage (couper des branches dont on sait qu'elles ne contiennent pas de solution), par des [[Heuristique (algorithmique)|heuristiques]] ou par des algorithmes approchés.

## Dans le cours

Le chapitre sur les règles d'association ([[2 - association rules]]) ne nomme pas le problème, mais l'[[Algorithme Apriori]] y répond : la [[Propriété de fermeture descendante|propriété de fermeture descendante]] élague les sur-ensembles des itemsets non fréquents.

Voir aussi : [[Complexité algorithmique]], [[Problème du voyageur de commerce]], [[Coefficient binomial]].

Résumés : [[2 - association rules]]
