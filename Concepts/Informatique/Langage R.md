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
  - "[[1 - Data analysis|Cours 1]]"
  - "[[14 - functions in RStudio|Summary functions in RStudio]]"
  - "[[13 - PCA in R|Cours 13 - PCA in R]]"
maj: 2026-11-07
---

Langage où tout passe par des fonctions et où tout est un objet. Les arguments nommés sont stricts, et l'aide s'obtient par `help()` ou `?` ([[1 - Data analysis|Cours 1 (Data analysis)]]).

**Structures** : vecteur (linéaire, éléments de même type), matrice (rectangulaire, même type, rangée par colonnes), liste (types mélangés) et [[Data frame]].

**Fonctions vues dans les cours** : `c()`, `seq`, `mean`, `summary`, `table`, `plot`, `t()` (Cours 1) ; `sd`, `var`, `quantile`, `hist`, `boxplot`, `qqnorm`, `cbind`, `rbind` ([[14 - functions in RStudio|Summary functions in RStudio]]) ; `cov`, `eigen`, `prcomp` pour l'[[Analyse en composantes principales]] ([[13 - PCA in R|Cours 13 - PCA in R]]).

Voir aussi : [[Data frame]], [[Facteur (variable catégorielle)]], [[Formule de modèle en R]], [[Bibliothèque ggplot2]], [[Analyse en composantes principales]].

## Erreurs du cours

- [[1 - Data analysis|Cours 1 (Data analysis)]] écrit que « `myframe[1:5]` gives first 5 rows of data » ; il faut `myframe[1:5, ]` pour les 5 premières lignes, car `myframe[1:5]` sélectionne les 5 premières colonnes d'un data frame (vérifié sur l'image de la diapositive).
- La même diapositive écrit `myframe[myframe[,1], < 5,]` ; il faut `myframe[myframe[,1] < 5, ]` pour garder les lignes dont la première colonne est inférieure à 5.

Résumés : [[1 - Data analysis|Cours 1 (Data analysis (Thanos), résumé)]], [[14 - functions in RStudio]], [[13 - PCA in R]], [[3 - Paradoxe de Simpson]]
