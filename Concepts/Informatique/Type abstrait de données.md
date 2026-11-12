---
type: concept
tags: [year4]
aliases: [types abstraits de données, type abstrait, TAD, abstract data type, ADT]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/Chp2 - tree revisions années précédentes.pdf|Chp2 - tree revisions années précédentes.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : un **type abstrait de données** (TAD) décrit un type par les opérations qu'on peut lui appliquer et par leur comportement (signatures, [[Précondition et postcondition|préconditions et postconditions]]), sans dire comment les données sont rangées en mémoire. Pile, file, liste, arbre, [[File de priorité|file de priorité]] ou [[Tableau associatif|tableau associatif]] sont des types abstraits ; une [[Structure de données|structure de données]] concrète (tableau, [[Liste chaînée|liste chaînée]], [[Tas binaire|tas]]…) en est une **implémentation**. Un programme qui n'utilise que les opérations du type abstrait ne dépend pas de l'implémentation, qu'on peut changer sans le réécrire : c'est le principe de l'[[Encapsulation (programmation)|encapsulation]], que les classes de la [[Programmation orientée objet|programmation orientée objet]] mettent en œuvre.

Exemple : la file (enfiler, défiler, estVide) peut être réalisée par un tableau circulaire ou par une liste chaînée ; un parcours en largeur qui n'appelle que ces opérations marche avec les deux.

## Dans le cours

[[2 - tree revisions années précédentes]] définit le type `Arbre d'Élément` (arbre k-aire) par huit opérations (`creerArbre`, `modifierRacine`, `ajouterFeuille`, `supprimerFeuille`, `estFeuille`, `racine`, `degre`, `recEnfant`), puis le type `ArbreBinaire d'Élément` (fils gauche et droit), sans jamais dire comment un arbre est représenté.

Voir aussi : [[Pile et file]], [[Arbre binaire]], [[Arbre (théorie des graphes)]], [[Fonction et procédure]].

Résumés : [[2 - tree revisions années précédentes]]
