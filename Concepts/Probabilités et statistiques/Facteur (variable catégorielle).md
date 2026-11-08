---
type: concept
tags:
  - year3
aliases:
  - niveaux d'un facteur
  - fonction factor
  - facteurs et régresseurs
  - facteur ordonné
  - ordered factor
matieres:
  - Data analysis (Thanos)
sources:
  - "[[1 - Data analysis|Cours 1]]"
  - "[[14 - functions in RStudio|Summary functions in RStudio]]"
  - "[[Raw/Year 3/Data analysis (Thanos)/Summary functions in RStudio :.docx|Summary functions in RStudio]]"
maj: 2026-11-08
---

Un facteur est une variable catégorielle, alors qu'un régresseur est continu. En R, il faut déclarer les facteurs (`factor(pain, levels=0:3)`, `levels()`) : R crée alors les [[Variable indicatrice|variables indicatrices]]. Le code interne d'un facteur commence toujours à 1 ([[1 - Data analysis|Cours 1 (Data analysis)]], [[14 - functions in RStudio|Summary functions in RStudio]]).

En [[ANOVA]], les facteurs sont les variables qualitatives, et leurs modalités sont les niveaux ([[12 - ANOVA and F-statistic]]).

**Complément (hors du cours)** :

- **Piège de `as.numeric`** : sur un facteur dont les niveaux sont des nombres, `as.numeric(f)` renvoie les codes internes (1, 2, 3…), pas les valeurs. Pour retrouver les valeurs : `as.numeric(as.character(f))`. Exemple : `f <- factor(c(10, 20, 10))` ; `as.numeric(f)` donne `1 2 1`, `as.numeric(as.character(f))` donne `10 20 10`.
- **Effectifs** : `table(f)` compte les observations par niveau, dans l'ordre des niveaux, y compris un niveau déclaré mais absent des données (effectif 0).
- **Facteur ordonné** : pour une variable ordinale ([[Type de variable statistique]]), `factor(x, levels = c("faible", "moyen", "fort"), ordered = TRUE)` ou `ordered(x, levels = …)`. Il accepte les comparaisons (`f < "fort"`) et une médiane avec `quantile(f, 0.5, type = 1)`, qui renvoie un niveau. Un facteur non ordonné n'a ni ordre ni médiane.

Notion parente : [[Langage R]]. Voir aussi : [[Variable indicatrice]], [[ANOVA]], [[Type de variable statistique]].

Résumés : [[1 - Data analysis|Cours 1 (Data analysis (Thanos), résumé)]], [[14 - functions in RStudio]], [[12 - ANOVA and F-statistic]]
