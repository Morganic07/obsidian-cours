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
  - "[[Séance 1 - Data analysis (Thanos) (résumé)|Cours 1]]"
  - "[[Summary functions in RStudio (résumé)|Summary functions in RStudio]]"
maj: 2026-11-06
---

Un facteur est une variable catégorielle, alors qu'un régresseur est continu. En R, il faut déclarer les facteurs (`factor(pain, levels=0:3)`, `levels()`) : R crée alors les [[Variable indicatrice|variables indicatrices]]. Le code interne d'un facteur commence toujours à 1 ([[Séance 1 - Data analysis (Thanos) (résumé)|Cours 1 (Data analysis)]], [[Summary functions in RStudio (résumé)|Summary functions in RStudio]]).

En [[ANOVA]], les facteurs sont les variables qualitatives, et leurs modalités sont les niveaux ([[Séance 12 - ANOVA and F-statistic (résumé)]]).

Notion parente : [[Langage R]]. Voir aussi : [[Variable indicatrice]], [[ANOVA]], [[Type de variable statistique]].

Résumés : [[Séance 1 - Data analysis (Thanos) (résumé)|Cours 1 (Data analysis (Thanos), résumé)]], [[Summary functions in RStudio (résumé)]], [[Séance 12 - ANOVA and F-statistic (résumé)]]
