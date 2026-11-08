---
type: concept
tags: [year3]
aliases: [F-statistic, F statistic, F-test, F-value, F-distribution, F distribution, loi de Fisher-Snedecor, test F, loi de Snedecor, Snedecor-Fisher, test de Fisher, test F d'égalité des variances, F-test for equality of variances, test F partiel, partial F-test, nested models F-test]
matieres: [Data analysis (Thanos)]
sources: ["[[11 - Multiple Linear Regression and F-statistic|Cours 11 - Multiple Linear Regression and F-statistic]]", "[[12 - ANOVA and F-statistic|Cours 12 - ANOVA and F-statistic]]"]
maj: 2026-11-08
---

Rapport de deux [[Carré moyen|carrés moyens]] (variances), $MS_{model}/MS_{error}$ : variation expliquée sur variation non expliquée [[Erreurs du cours#^e-statistique-f|✎]], ou variance inter-groupes sur variance intra-groupe. Elle suit une loi $F$ de Snedecor-Fisher à deux degrés de liberté, $v_1$ au numérateur et $v_2$ au dénominateur, qui décrit un rapport de deux variables du χ² divisées par leurs degrés de liberté. Pour deux échantillons normaux, c'est la loi de $\dfrac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2}$ ([[11 - Multiple Linear Regression and F-statistic|Cours 11 - Multiple Linear Regression and F-statistic]]). La statistique est positive, la zone de rejet est à droite.

**En ANOVA** : $F = \dfrac{SST_G/(k-1)}{SST_E/(N-k)}$. Voir [[ANOVA]].

**En régression** : $F = \dfrac{(TSS - RSS)/(p-1)}{RSS/(n-p)}$ avec $p$ paramètres constante comprise. Il teste $H_0 : \beta_1 = \dots = \beta_k = 0$, c'est-à-dire que le modèle ne fait pas mieux qu'un modèle réduit à l'ordonnée à l'origine. Les prédicteurs se jugent ensuite un à un par des tests $t$. Lien avec $R^2$ ([[Coefficient de détermination]]) : $R^2 = 1 - \left(1 + F\dfrac{p-1}{n-p}\right)^{-1}$.

**Différence avec le test $t$** : le test $t$ juge une variable, le test F un groupe de variables ensemble.

**Décision** ([[Test d'hypothèse]]) : rejeter $H_0$ si la p-value est inférieure à $\alpha$, ou si $F$ dépasse la valeur critique de la table ; si $F$ reste sous la valeur critique, on ne rejette pas $H_0$. [[Erreurs du cours#^e-statistique-f|✎]] Dans l'exemple d'ANOVA du cours, $F(2, 12) \approx 17{,}92 > 3{,}89$, donc $p < 0{,}05$ (voir [[Somme des carrés (SST, SSR, SSE)]]). [[Erreurs du cours#^e-statistique-f|✎]]

## Compléments

- **Attention aux sigles** : $RSS$ (séance 11, *residual sum of squares*) est la $SSE$ de la séance 10, et $TSS - RSS$ est la $SSR$ de la séance 10 (voir [[Somme des carrés (SST, SSR, SSE)]]). Le « R » de RSS veut dire *residual*, celui de SSR *regression*. [[Complément hors du cours|ⓘ]]
- **Tableau d'ANOVA de la régression** ($p$ paramètres, constante comprise) : [[Complément hors du cours|ⓘ]]

| Source | ddl | Somme des carrés | Carré moyen | $F$ |
|---|---|---|---|---|
| Régression | $p - 1$ | $TSS - RSS$ | $\dfrac{TSS - RSS}{p-1}$ | $\dfrac{(TSS - RSS)/(p-1)}{RSS/(n-p)}$ |
| Résidus | $n - p$ | $RSS$ | $\dfrac{RSS}{n-p}$ | |
| Total | $n - 1$ | $TSS$ | | |

- **En régression simple, $F = t^2$** : le test F global et le [[Test de la pente|test $t$ de la pente]] sont un même test, avec la même p-value. La raison : si $T$ suit une [[Loi de Student]] à $v$ degrés de liberté, $T^2$ suit $F(1, v)$. Exemple des jouets ($n = 5$, $p = 2$) : $F = \dfrac{4{,}9/1}{1{,}1/3} \approx 13{,}36 \approx 3{,}657^2$, $p \approx 0{,}035$. [[Complément hors du cours|ⓘ]]
- **Test F de modèles emboîtés** : pour savoir si $q$ variables ajoutées améliorent un modèle, on compare le modèle réduit au modèle complet ($p$ paramètres) :
$$F = \frac{(RSS_{\text{réduit}} - RSS_{\text{complet}})/q}{RSS_{\text{complet}}/(n-p)},$$
qui suit $F(q, n-p)$ sous $H_0$ (les $q$ coefficients ajoutés sont nuls). Le test global du cours en est le cas où le modèle réduit ne garde que la constante ($RSS_{\text{réduit}} = TSS$, $q = p - 1$). En R : `anova(m_reduit, m_complet)`. [[Complément hors du cours|ⓘ]]
- **Test F d'égalité de deux variances** (test de Fisher) : pour deux échantillons normaux indépendants, sous $H_0 : \sigma_1 = \sigma_2$, $S_1^2/S_2^2$ suit $F(n_1 - 1, n_2 - 1)$. On l'utilise par exemple avant un [[Test t]] à variances égales ; il est très sensible à la non-normalité. En R : `var.test(x, y)`. [[Complément hors du cours|ⓘ]]
- **Forme de la loi** : la loi $F$ ne prend que des valeurs positives et est étalée à droite ; un rapport proche de 1 signifie que le modèle n'explique pas plus que le bruit. Le test F de régression et d'ANOVA est donc **unilatéral à droite** ([[Test unilatéral et bilatéral]]). Si $X$ suit $F(v_1, v_2)$, alors $1/X$ suit $F(v_2, v_1)$, ce qui permet de lire dans les tables les quantiles du côté gauche : $F_{1-\alpha}(v_1, v_2) = 1/F_{\alpha}(v_2, v_1)$ (quantiles d'ordre $\alpha$ et $1-\alpha$). Définition formelle : si $U \sim \chi^2(v_1)$ et $V \sim \chi^2(v_2)$ sont indépendantes, $\dfrac{U/v_1}{V/v_2} \sim F(v_1, v_2)$ ([[Loi du khi-deux]]). En R : `pf()`, `qf()`. [[Complément hors du cours|ⓘ]]

Voir aussi : [[ANOVA]], [[Régression linéaire]], [[Carré moyen]], [[Coefficient de détermination]], [[Test d'hypothèse]], [[Test de la pente]], [[Loi de Student]], [[Loi du khi-deux]], [[Multicolinéarité]]

Résumés : [[11 - Multiple Linear Regression and F-statistic]], [[12 - ANOVA and F-statistic]], [[5 - Hypothesis Testing]], [[6 - T-Test]], [[7 - Z-Test]]
