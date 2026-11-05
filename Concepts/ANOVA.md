---
type: concept
aliases: [analysis of variance, analyse de la variance, one-way ANOVA, two-way ANOVA, ANOVA à un facteur, ANOVA à deux facteurs]
matieres: [Data analysis (Thanos)]
sources: ["[[Cours 12 - ANOVA and F-statistic]]", "[[Cours 11 - Multiple Linear Regression and F-statistic]]"]
maj: 2026-11-05
---

Technique qui teste si trois populations ou plus ont la même moyenne. On étudie l'effet d'une ou plusieurs variables qualitatives (les **facteurs**, dont les valeurs sont les **niveaux**) sur une variable quantitative.

**Idée** : on partage la variation totale en variation entre groupes et variation dans les groupes. $H_0$ : toutes les moyennes de population sont égales. $H_1$ : au moins une diffère. La statistique est la [[Statistique F]] : variance inter-groupes sur variance intra-groupe, avec $k-1$ et $N-k$ degrés de liberté pour $k$ groupes et $N$ observations.

**Conditions** : normalité de chaque échantillon, indépendance, égalité des variances, variable dépendante continue.

**Pourquoi pas plusieurs tests $t$** : ils multiplient les comparaisons par paires, alors que l'ANOVA donne un seul F et une seule p-value.

**Deux facteurs** : chaque échantillon est classé de deux manières, avec trois paires d'hypothèses (effet de chaque facteur et interaction).

**Lien avec la régression** : la [[Régression linéaire]] simple est un cas particulier d'ANOVA, avec $SST = SSR + SSE$.

Résumé : [[Cours 12 - ANOVA and F-statistic (résumé)]]
