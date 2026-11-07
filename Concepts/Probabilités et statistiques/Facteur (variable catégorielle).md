---
type: concept
tags:
  - year3
aliases:
  - niveaux d'un facteur
  - fonction factor
  - facteurs et régresseurs
matieres:
  - Data analysis (Thanos)
sources:
  - "[[1 - Data analysis|Cours 1]]"
  - "[[14 - functions in RStudio|Summary functions in RStudio]]"
maj: 2026-11-06
---

Un facteur est une variable catégorielle, alors qu'un régresseur est continu. En R, il faut déclarer les facteurs (`factor(pain, levels=0:3)`, `levels()`) : R crée alors les [[Variable indicatrice|variables indicatrices]]. Le code interne d'un facteur commence toujours à 1 ([[1 - Data analysis|Cours 1 (Data analysis)]], [[14 - functions in RStudio|Summary functions in RStudio]]).

En [[ANOVA]], les facteurs sont les variables qualitatives, et leurs modalités sont les niveaux ([[12 - ANOVA and F-statistic]]).

Notion parente : [[Langage R]]. Voir aussi : [[Variable indicatrice]], [[ANOVA]], [[Type de variable statistique]].

Résumés : [[1 - Data analysis|Cours 1 (Data analysis (Thanos), résumé)]], [[14 - functions in RStudio]], [[12 - ANOVA and F-statistic]]
