---
type: concept
tags: [year4]
aliases: [précondition, postcondition, préconditions, postconditions, precondition, postcondition (programmation), précond, postcond]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/Chp2 - tree revisions années précédentes.pdf|Chp2 - tree revisions années précédentes.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : la **précondition** d'une opération (fonction ou procédure) est la condition que les données doivent remplir **avant** l'appel ; la **postcondition** est ce que l'opération garantit **après** l'appel, si la précondition était vraie. Ensemble, elles forment la spécification (le « contrat ») de l'opération : elles disent ce qu'elle fait sans dire comment. Si l'appelant viole la précondition, l'opération ne promet rien : c'est à lui de la vérifier. Cette idée, formalisée par la logique de Hoare (triplet $\{P\}\ S\ \{Q\}$), sert à prouver la [[Correction d'un algorithme|correction d'un algorithme]] et fonde la « programmation par contrat ».

Exemple : pour `recEnfant(a, pos)`, la précondition « `a` initialisé et $1 \le pos \le$ `degre(a)` » interdit de demander un fils qui n'existe pas ; la postcondition « renvoie le fils de `a` à la position `pos` » décrit le résultat.

En C, on vérifie une précondition pendant le développement avec la macro `assert` (`<assert.h>`), qui arrête le programme si la condition est fausse ; en Java, une précondition non respectée lève souvent une exception (`IllegalArgumentException`).

## Dans le cours

[[2 - tree revisions années précédentes]] décrit chaque opération du [[Type abstrait de données|type abstrait]] arbre (k-aire, puis binaire) par sa signature, sa précondition (« Précond : a initialisé… ») et sa postcondition (« Postcond : renvoie… »).

Voir aussi : [[Fonction et procédure]], [[Type abstrait de données]], [[Invariant de boucle]], [[Invariant de classe]], [[Correction d'un algorithme]].

Résumés : [[2 - tree revisions années précédentes]]
