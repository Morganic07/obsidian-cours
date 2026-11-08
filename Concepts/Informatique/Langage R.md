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
maj: 2026-11-08
---

Langage où tout passe par des fonctions et où tout est un objet. Les arguments nommés sont stricts, et l'aide s'obtient par `help()` ou `?` ([[1 - Data analysis|Cours 1 (Data analysis)]]).

**Structures** : vecteur (linéaire, éléments de même type), matrice (rectangulaire, même type, rangée par colonnes), liste (types mélangés) et [[Data frame]].

**Fonctions vues dans les cours** : `c()`, `seq`, `mean`, `summary`, `table`, `plot`, `t()` (Cours 1) ; `sd`, `var`, `quantile`, `hist`, `boxplot`, `qqnorm`, `cbind`, `rbind` ([[14 - functions in RStudio|Summary functions in RStudio]]) ; `cov`, `eigen`, `prcomp` pour l'[[Analyse en composantes principales]] ([[13 - PCA in R|Cours 13 - PCA in R]]).

**Sous-ensembles d'un data frame** : `myframe[1:5, ]` donne les 5 premières lignes (sans la virgule, `myframe[1:5]` sélectionne les 5 premières colonnes) ; `myframe[myframe[,1] < 5, ]` garde les lignes dont la première colonne est inférieure à 5. [[Erreurs du cours#^e-langage-r|✎]]

Voir aussi : [[Data frame]], [[Facteur (variable catégorielle)]], [[Formule de modèle en R]], [[Bibliothèque ggplot2]], [[Analyse en composantes principales]].

Résumés : [[1 - Data analysis|Cours 1 (Data analysis (Thanos), résumé)]], [[14 - functions in RStudio]], [[13 - PCA in R]], [[3 - Paradoxe de Simpson]]
