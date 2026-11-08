---
type: concept
tags: [year3]
aliases: [analysis of variance, analyse de la variance, one-way ANOVA, two-way ANOVA, ANOVA à un facteur, ANOVA à deux facteurs, tableau d'ANOVA, ANOVA table, ANOVA de Welch, Welch's ANOVA, êta carré, eta squared]
matieres: [Data analysis (Thanos)]
sources: ["[[12 - ANOVA and F-statistic|Cours 12 - ANOVA and F-statistic]]", "[[11 - Multiple Linear Regression and F-statistic|Cours 11 - Multiple Linear Regression and F-statistic]]", "[[Raw/Year 3/Data analysis (Thanos)/Cours 12 : ANOVA and F-statistic .docx|Cours 12 - ANOVA and F-statistic]]"]
maj: 2026-11-08
---

Technique qui teste si trois populations ou plus ont la même moyenne. On étudie l'effet d'une ou plusieurs variables qualitatives (les **facteurs**, dont les valeurs sont les **niveaux**) sur une variable quantitative.

**Idée** : on partage la variation totale en variation entre groupes et variation dans les groupes. $H_0$ : toutes les moyennes de population sont égales. $H_1$ : au moins une diffère. La statistique est la [[Statistique F]] : variance inter-groupes sur variance intra-groupe, avec $k-1$ et $N-k$ degrés de liberté pour $k$ groupes et $N$ observations.

**Conditions** : normalité de chaque échantillon, indépendance, égalité des variances, variable dépendante continue.

**Pourquoi pas plusieurs tests $t$** : ils multiplient les comparaisons par paires, alors que l'ANOVA donne un seul F et une seule p-value.

**Deux facteurs** : chaque échantillon est classé de deux manières, avec trois paires d'hypothèses (effet de chaque facteur et interaction).

**Lien avec la régression** : la [[Régression linéaire]] simple est un cas particulier d'ANOVA, avec $SST = SSR + SSE$. Différence clé selon le cours : en ANOVA, aucune hypothèse n'est faite sur la manière dont les variables sont liées (dans l'exemple, le prix et le volume de ventes).

**Tableau d'ANOVA** : degrés de liberté $k-1$ pour les groupes, $N-k$ pour l'erreur, $N-1$ au total.

## Compléments (hors du cours)

**Modèle** : l'ANOVA à un facteur s'écrit $x_{ij} = \mu + \alpha_i + \varepsilon_{ij}$, où $x_{ij}$ est la $j$-ième observation du groupe $i$, $\mu$ la moyenne générale, $\alpha_i$ l'effet du niveau $i$ (avec $\sum_i n_i \alpha_i = 0$) et $\varepsilon_{ij} \sim \mathcal{N}(0, \sigma^2)$ des erreurs indépendantes. $H_0$ s'écrit alors $\alpha_1 = \dots = \alpha_k = 0$.

**Après un $F$ significatif** : $H_1$ signifie seulement « au moins une moyenne diffère », pas « toutes diffèrent ». Pour savoir lesquelles, on fait des [[Comparaisons multiples|comparaisons multiples]] (tests *post hoc* : Tukey, Bonferroni).

**Taille d'effet** : un $F$ significatif ne dit pas que la différence est grande. On la mesure par $\eta^2 = \dfrac{SSB}{SST}$, part de la variation totale expliquée par le facteur, équivalent du $R^2$ de la régression ([[Coefficient de détermination]]).

**Deux groupes** : avec $k = 2$, l'ANOVA équivaut au [[Test t|test t]] à variances égales : $F = t^2$, et les deux p-values sont identiques.

**Si les conditions tombent** : l'**ANOVA de Welch**, qui étend le [[Test de Welch|test t de Welch]] à $k$ groupes, se passe de l'égalité des variances ([[Homoscédasticité]]) ; le [[Test de Kruskal-Wallis|test de Kruskal-Wallis]], fondé sur les rangs, se passe de la normalité.

**Interaction (deux facteurs)** : il y a interaction quand l'effet d'un facteur dépend du niveau de l'autre. Sur le graphe des moyennes par cellule (un niveau de A en abscisse, une courbe par niveau de B), les courbes ne sont pas parallèles. Avec $a$ niveaux pour A, $b$ pour B et $r$ répétitions par cellule ($N = abr$), les degrés de liberté sont :

| Source | ddl |
|---|---|
| Facteur A | $a-1$ |
| Facteur B | $b-1$ |
| Interaction A×B | $(a-1)(b-1)$ |
| Erreur | $ab(r-1)$ |
| Total | $abr-1$ |

Quand l'interaction est significative, les effets principaux s'interprètent avec prudence.

**En R** :

```r
modele <- aov(y ~ groupe, data = df)   # un facteur
summary(modele)                         # tableau d'ANOVA
TukeyHSD(modele)                        # comparaisons deux à deux
aov(y ~ A * B, data = df)              # deux facteurs avec interaction
oneway.test(y ~ groupe, data = df)     # ANOVA de Welch
```

Voir aussi : [[Carré moyen]], [[Somme des carrés (SST, SSR, SSE)]], [[Test t]], [[Homoscédasticité]], [[Comparaisons multiples]], [[Test de Kruskal-Wallis]], [[Coefficient de détermination]].

Résumés : [[12 - ANOVA and F-statistic]], [[11 - Multiple Linear Regression and F-statistic]]
