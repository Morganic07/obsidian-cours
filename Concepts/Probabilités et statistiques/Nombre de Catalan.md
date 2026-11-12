---
type: concept
tags: [year4]
aliases: [nombres de Catalan, Catalan number, Catalan numbers]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/Chp2 - tree revisions années précédentes.pdf|Chp2 - tree revisions années précédentes.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : les **nombres de Catalan** forment la suite d'entiers
$$C_n = \frac{1}{n+1}\binom{2n}{n} = \frac{(2n)!}{(n+1)!\,n!},$$
soit 1, 1, 2, 5, 14, 42, 132, 429… pour $n = 0, 1, 2, \dots$ (voir [[Coefficient binomial]]). Ils vérifient la relation de récurrence $C_0 = 1$ et $C_{n+1} = \sum_{i=0}^{n} C_i\,C_{n-i}$. Ils comptent de nombreux objets de [[Dénombrement|dénombrement]] : les formes d'[[Arbre binaire|arbres binaires]] à $n$ nœuds, les mots bien parenthésés à $n$ paires de parenthèses, les façons de parenthéser un produit de $n + 1$ facteurs, les triangulations d'un polygone convexe à $n + 2$ côtés, les arbres ordonnés à $n + 1$ nœuds. Ils croissent comme $C_n \sim \frac{4^n}{n^{3/2}\sqrt{\pi}}$ (par la [[Formule de Stirling|formule de Stirling]]).

**Pourquoi les arbres binaires.** Un arbre binaire à $n + 1$ nœuds, c'est une racine, un sous-arbre gauche à $i$ nœuds et un sous-arbre droit à $n - i$ nœuds, pour $i$ de $0$ à $n$ : on retrouve la récurrence. Exemple : $C_3 = 5$ arbres binaires à 3 nœuds (le peigne gauche, le peigne droit, les deux zigzags, l'arbre complet).

## Dans le cours

[[2 - tree revisions années précédentes]] ne compte pas les arbres ; ses compléments donnent le nombre de formes d'arbres binaires à $n$ nœuds.

Voir aussi : [[Coefficient binomial]], [[Dénombrement]], [[Récurrence]], [[Arbre binaire]].

Résumés : [[2 - tree revisions années précédentes]]
