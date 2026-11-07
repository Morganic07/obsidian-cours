---
type: concept
tags: [year2, year3]
aliases: [covariance, correlation coefficient, coefficient de corrélation, variables non corrélées, uncorrelated, combinaison linéaire de variables aléatoires, linear combination of rvs, Covariance shortcut formula, distributive property of covariance, correlation versus causation, corrélation de Pearson, coefficient de corrélation de Pearson, Pearson correlation, "coefficient d'échantillon r"]
matieres: [Probability, Statistics, Data analysis (Thanos)]
sources: ["[[6 - Joint probability distributions|Chp 6 - Joint probability distributions]]", "[[3 - More on probability|Chp3 - More on probability]]", "[[9 - Covariance and Correlation|Cours 9 - Covariance and Correlation]]"]
maj: 2026-11-07
---

$\mathrm{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)] = E(XY) - \mu_X\mu_Y$ (formule raccourcie) ; symétrique, avec $\mathrm{Cov}(X, X) = \mathrm{Var}(X)$. Distributivité : $\mathrm{Cov}(aX + bY + c, Z) = a\,\mathrm{Cov}(X, Z) + b\,\mathrm{Cov}(Y, Z)$. La covariance dépend des unités ; elle s'estime sur un échantillon par $\sum (x_i - \bar X)(y_i - \bar Y)/(n-1)$.

**Corrélation de Pearson** : $\rho = \mathrm{Cov}(X, Y)/(\sigma_X\sigma_Y)$, sans unité, entre $-1$ et $1$. Si $X$ et $Y$ sont [[Indépendance de variables aléatoires|indépendantes]], $\rho = 0$, mais $\rho = 0$ n'entraîne pas l'indépendance. $\rho = \pm 1$ si et seulement si $Y = aX + b$, $a \ne 0$. Non corrélées signifie $E[XY] = \mu_X\mu_Y$. Corrélation n'est pas causalité : voir [[Corrélation et causalité]]. Coefficient d'échantillon : $r = SS_{xy}/\sqrt{SS_{xx}SS_{yy}}$.

En Data analysis, le cours rapproche Pearson du [[Coefficient de corrélation de Spearman]], du [[Tau de Kendall]] et du [[Coefficient de détermination]] ; la version multivariée est la [[Matrice de covariance]].

**Combinaison linéaire** $a_1X_1 + \dots + a_nX_n + b$ : $E = \sum a_i\mu_i + b$ sans condition ; $\mathrm{Var} = \sum_i\sum_j a_ia_j\mathrm{Cov}(X_i, X_j)$, qui devient $\sum a_i^2\sigma_i^2$ si les $X_i$ sont indépendantes. Pour une moyenne empirique, voir [[Théorème central limite]].

Notion parente : [[Loi conjointe]]. Voir aussi : [[Espérance et variance]], [[Corrélation et causalité]], [[Indépendance de variables aléatoires]], [[Matrice de covariance]], [[Coefficient de corrélation de Spearman]], [[Tau de Kendall]], [[Coefficient de détermination]]

## Erreurs du cours

- [[6 - Joint probability distributions|Chp 6 - Joint probability distributions]] (image vérifiée) écrit « constants $a_1, a_2, \dots, a_n, b = 0$ » dans la définition de la combinaison linéaire $a_1X_1 + \dots + a_nX_n + b$ ; il faut « constants $a_1, \dots, a_n, b$ » : $b$ est quelconque, et ne vaut 0 que pour la moyenne empirique, comme le dit la suite.
- [[9 - Covariance and Correlation|Cours 9 - Covariance and Correlation]] (image vérifiée) écrit que la corrélation est « comprise strictement entre −1 et 1 » ; il faut « comprise entre −1 et 1 (bornes incluses) » : le même passage décrit $1$ et $-1$ comme des relations parfaites.

Résumés : [[6 - Joint probability distributions]], [[3 - More on probability]], [[9 - Covariance and Correlation]], [[0 - proba&stats utilitaire]]
