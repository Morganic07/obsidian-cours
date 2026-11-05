---
type: concept
aliases: [F-statistic, F statistic, F-test, F-value, F-distribution, F distribution, loi de Fisher-Snedecor, test F]
matieres: [Data analysis (Thanos)]
sources: ["[[Cours 11 - Multiple Linear Regression and F-statistic]]", "[[Cours 12 - ANOVA and F-statistic]]"]
maj: 2026-11-05
---

Rapport de deux carrés moyens (variances) : variation expliquée sur variation non expliquée. Elle suit une loi $F$ de Snedecor-Fisher à deux degrés de liberté, $v_1$ au numérateur et $v_2$ au dénominateur, qui décrit un rapport de deux variables du χ² divisées par leurs degrés de liberté. La statistique est positive, la zone de rejet est à droite.

**En ANOVA** : $F = \dfrac{SST_G/(k-1)}{SST_E/(N-k)}$. Voir [[ANOVA]].

**En régression** : $F = \dfrac{(TSS - RSS)/(p-1)}{RSS/(n-p)}$ avec $p$ paramètres constante comprise. Il teste $H_0 : \beta_1 = \dots = \beta_k = 0$, c'est-à-dire que le modèle ne fait pas mieux qu'un modèle réduit à l'ordonnée à l'origine. Les prédicteurs se jugent ensuite un à un par des tests $t$. Lien avec $R^2$ : $R^2 = 1 - \left(1 + F\dfrac{p-1}{n-p}\right)^{-1}$.

**Différence avec le test $t$** : le test $t$ juge une variable, le test F un groupe de variables ensemble.

**Décision** : rejeter $H_0$ si la p-value est inférieure à $\alpha$, ou si $F$ dépasse la valeur critique de la table.

Mise en garde : une diapositive de [[Cours 11 - Multiple Linear Regression and F-statistic (résumé)|Cours 11]] écrit le rapport à l'envers, voir les points à vérifier du résumé.

Liens : [[Régression linéaire]]
