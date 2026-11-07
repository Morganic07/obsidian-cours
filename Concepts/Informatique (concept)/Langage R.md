---
type: concept
tags:
  - year3
aliases:
  - RStudio
  - R language
matieres:
  - Data analysis (Thanos)
sources:
  - "[[1 - Data analysis (résumé)|Cours 1]]"
  - "[[14 - functions in RStudio (résumé)|Summary functions in RStudio]]"
  - "[[13 - PCA in R (résumé)|Cours 13 - PCA in R]]"
maj: 2026-11-06
---

Langage où tout passe par des fonctions et où tout est un objet. Les arguments nommés sont stricts, et l'aide s'obtient par `help()` ou `?` ([[1 - Data analysis (résumé)|Cours 1 (Data analysis)]]).

**Structures** : vecteur (linéaire, éléments de même type), matrice (rectangulaire, même type, rangée par colonnes), liste (types mélangés) et [[Data frame]].

**Fonctions vues dans les cours** : `c()`, `seq`, `mean`, `summary`, `table`, `plot`, `t()` (Cours 1) ; `sd`, `var`, `quantile`, `hist`, `boxplot`, `qqnorm`, `cbind`, `rbind` ([[14 - functions in RStudio (résumé)|Summary functions in RStudio]]) ; `cov`, `eigen`, `prcomp` pour l'[[Analyse en composantes principales]] ([[13 - PCA in R (résumé)|Cours 13 - PCA in R]]).

Voir aussi : [[Data frame]], [[Facteur (variable catégorielle)]], [[Formule de modèle en R]], [[Bibliothèque ggplot2]], [[Analyse en composantes principales]].

## À vérifier

- Cours 1 : `myframe[1:5]` sélectionne des colonnes, pas des lignes.

Résumés : [[1 - Data analysis (résumé)|Cours 1 (Data analysis (Thanos), résumé)]], [[14 - functions in RStudio (résumé)]], [[13 - PCA in R (résumé)]], [[3 - Paradoxe de Simpson (résumé)]]
