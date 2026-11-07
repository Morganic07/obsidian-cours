---
type: concept
tags:
  - year3
aliases:
  - ecdf
  - empirical cumulative distribution function
  - empirical cumulative distribution
matieres:
  - Data analysis (Thanos)
sources:
  - "[[14 - functions in RStudio|Summary functions in RStudio]]"
maj: 2026-11-07
---

**Définition (complément, hors du cours)** : pour un échantillon $x_1,\dots,x_n$, la fonction de répartition empirique est $F_n(x)=\frac{1}{n}\,\mathrm{card}\{i : x_i\leq x\}$, la proportion des observations inférieures ou égales à $x$. C'est une fonction en escalier, croissante, qui va de $0$ à $1$ et saute de $\frac{1}{n}$ à chaque observation (d'un multiple de $\frac{1}{n}$ en cas d'ex aequo). Elle estime la [[Fonction de répartition]] de la loi dont l'échantillon est issu, et sert de base au [[Test de Kolmogorov-Smirnov]].

## Dans le cours

Nommée dans [[14 - functions in RStudio|Summary functions in RStudio]] sans définition : en R, `ecdf(x)` renvoie la fonction de répartition empirique de `x`, que trace `plot(ecdf(x))`.

Notion parente : [[Fonction de répartition]]. Voir aussi : [[Langage R]].

Résumés : [[14 - functions in RStudio]]
