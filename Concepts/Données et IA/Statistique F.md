---
type: concept
tags: [year3]
aliases: [F-statistic, F statistic, F-test, F-value, F-distribution, F distribution, loi de Fisher-Snedecor, test F, loi de Snedecor, Snedecor-Fisher]
matieres: [Data analysis (Thanos)]
sources: ["[[Cours 11 - Multiple Linear Regression and F-statistic]]", "[[Cours 12 - ANOVA and F-statistic]]"]
maj: 2026-11-06
---

Rapport de deux [[Carré moyen|carrés moyens]] (variances), $MS_{model}/MS_{error}$ : variation expliquée sur variation non expliquée, ou variance inter-groupes sur variance intra-groupe. Elle suit une loi $F$ de Snedecor-Fisher à deux degrés de liberté, $v_1$ au numérateur et $v_2$ au dénominateur, qui décrit un rapport de deux variables du χ² divisées par leurs degrés de liberté. Pour deux échantillons normaux, c'est la loi de $\dfrac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2}$ ([[Cours 11 - Multiple Linear Regression and F-statistic]]). La statistique est positive, la zone de rejet est à droite.

**En ANOVA** : $F = \dfrac{SST_G/(k-1)}{SST_E/(N-k)}$. Voir [[ANOVA]].

**En régression** : $F = \dfrac{(TSS - RSS)/(p-1)}{RSS/(n-p)}$ avec $p$ paramètres constante comprise. Il teste $H_0 : \beta_1 = \dots = \beta_k = 0$, c'est-à-dire que le modèle ne fait pas mieux qu'un modèle réduit à l'ordonnée à l'origine. Les prédicteurs se jugent ensuite un à un par des tests $t$. Lien avec $R^2$ ([[Coefficient de détermination]]) : $R^2 = 1 - \left(1 + F\dfrac{p-1}{n-p}\right)^{-1}$.

**Différence avec le test $t$** : le test $t$ juge une variable, le test F un groupe de variables ensemble.

**Décision** ([[Test d'hypothèse]]) : rejeter $H_0$ si la p-value est inférieure à $\alpha$, ou si $F$ dépasse la valeur critique de la table.

Voir aussi : [[ANOVA]], [[Régression linéaire]], [[Carré moyen]], [[Coefficient de détermination]], [[Test d'hypothèse]]

## À vérifier

- La première diapositive de [[Cours 11 - Multiple Linear Regression and F-statistic]] écrit $F$ = variance non expliquée / variance expliquée, à l'envers (à corriger avant un examen).
- La règle de rejet est énoncée à l'envers dans [[Cours 12 - ANOVA and F-statistic]] (« on ne rejette pas $H_0$ si la valeur critique est plus petite que $F$ »).
- [[Cours 12 - ANOVA and F-statistic]] écrit « F = 22,59, p > 0,05 » : c'est faux, $F$ dépasse la valeur critique 3,89, donc $p < 0{,}05$.

Résumés : [[Cours 11 - Multiple Linear Regression and F-statistic (résumé)]], [[Cours 12 - ANOVA and F-statistic (résumé)]], [[Cours 5 - Hypothesis Testing (résumé)]], [[Cours 6 - T-Test (résumé)]], [[Cours 7 - Z-Test (résumé)]]
