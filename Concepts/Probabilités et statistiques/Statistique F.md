---
type: concept
tags: [year3]
aliases: [F-statistic, F statistic, F-test, F-value, F-distribution, F distribution, loi de Fisher-Snedecor, test F, loi de Snedecor, Snedecor-Fisher]
matieres: [Data analysis (Thanos)]
sources: ["[[11 - Multiple Linear Regression and F-statistic|Cours 11 - Multiple Linear Regression and F-statistic]]", "[[12 - ANOVA and F-statistic|Cours 12 - ANOVA and F-statistic]]"]
maj: 2026-11-07
---

Rapport de deux [[Carré moyen|carrés moyens]] (variances), $MS_{model}/MS_{error}$ : variation expliquée sur variation non expliquée, ou variance inter-groupes sur variance intra-groupe. Elle suit une loi $F$ de Snedecor-Fisher à deux degrés de liberté, $v_1$ au numérateur et $v_2$ au dénominateur, qui décrit un rapport de deux variables du χ² divisées par leurs degrés de liberté. Pour deux échantillons normaux, c'est la loi de $\dfrac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2}$ ([[11 - Multiple Linear Regression and F-statistic|Cours 11 - Multiple Linear Regression and F-statistic]]). La statistique est positive, la zone de rejet est à droite.

**En ANOVA** : $F = \dfrac{SST_G/(k-1)}{SST_E/(N-k)}$. Voir [[ANOVA]].

**En régression** : $F = \dfrac{(TSS - RSS)/(p-1)}{RSS/(n-p)}$ avec $p$ paramètres constante comprise. Il teste $H_0 : \beta_1 = \dots = \beta_k = 0$, c'est-à-dire que le modèle ne fait pas mieux qu'un modèle réduit à l'ordonnée à l'origine. Les prédicteurs se jugent ensuite un à un par des tests $t$. Lien avec $R^2$ ([[Coefficient de détermination]]) : $R^2 = 1 - \left(1 + F\dfrac{p-1}{n-p}\right)^{-1}$.

**Différence avec le test $t$** : le test $t$ juge une variable, le test F un groupe de variables ensemble.

**Décision** ([[Test d'hypothèse]]) : rejeter $H_0$ si la p-value est inférieure à $\alpha$, ou si $F$ dépasse la valeur critique de la table.

Voir aussi : [[ANOVA]], [[Régression linéaire]], [[Carré moyen]], [[Coefficient de détermination]], [[Test d'hypothèse]]

## Erreurs du cours

- [[11 - Multiple Linear Regression and F-statistic|Cours 11 - Multiple Linear Regression and F-statistic]] (première diapositive, vérifiée sur l'image) écrit « F = variance **not** explained by the model / variance explained by the model » ; il faut l'inverse, $F$ = variance expliquée / variance non expliquée, comme le donnent les diapositives suivantes ($MS_{model}/MS_{error}$).
- [[11 - Multiple Linear Regression and F-statistic|Cours 11 - Multiple Linear Regression and F-statistic]] et [[12 - ANOVA and F-statistic|Cours 12 - ANOVA and F-statistic]] (vérifié sur l'image) écrivent « You should not reject the null if your critical f value is smaller than your F-value, unless you also have a small p-value » ; il faut : on rejette $H_0$ quand $F$ dépasse la valeur critique, ce qui équivaut à une p-value inférieure à $\alpha$.
- [[12 - ANOVA and F-statistic|Cours 12 - ANOVA and F-statistic]] écrit « F = 22.59, p > 0.05 » (vérifié sur l'image) ; il faut $p < 0{,}05$, puisque $F$ dépasse la valeur critique 3,89. Les sommes de carrés de cet exemple sont elles-mêmes fausses (voir [[Somme des carrés (SST, SSR, SSE)]]).

Résumés : [[11 - Multiple Linear Regression and F-statistic]], [[12 - ANOVA and F-statistic]], [[5 - Hypothesis Testing]], [[6 - T-Test]], [[7 - Z-Test]]
