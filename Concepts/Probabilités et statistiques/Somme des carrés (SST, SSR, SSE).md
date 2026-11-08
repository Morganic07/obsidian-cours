---
type: concept
tags: [year3]
aliases: [SST, SSR, SSE, TSS, RSS, sum of squares, somme des carrés totale, somme des carrés résiduelle, SSW, SSB, décomposition de la variation]
matieres: [Data analysis (Thanos)]
sources: ["[[10 - linear regression|Cours 10 - linear regression]]", "[[12 - ANOVA and F-statistic|Cours 12 - ANOVA and F-statistic]]"]
maj: 2026-11-08
---

En régression ([[10 - linear regression|Cours 10 - linear regression]]) :

- $SST = \sum (y_i - \bar y)^2$, variation totale ;
- $SSR = \sum (\hat y_i - \bar y)^2$, variation expliquée ;
- $SSE = \sum (y_i - \hat y_i)^2$, variation non expliquée.

On a $SST = SSR + SSE$, car le terme croisé s'annule.

[[11 - Multiple Linear Regression and F-statistic|Cours 11 - Multiple Linear Regression and F-statistic]] note TSS (« total sum of squares ») et RSS (« residual sum of squares ») : RSS y désigne la somme résiduelle, c'est-à-dire $SSE$, et non $SSR$.

En [[ANOVA]], $SST = SSW + SSB$ : variation intra-groupes et inter-groupes ([[12 - ANOVA and F-statistic|Cours 12 - ANOVA and F-statistic]]). Exemple du cours, échantillons 2, 3, 7, 2, 6 ; 10, 3, 7, 2, 6 ; 10, 13, 14, 13, 15 (moyennes 4 ; 5,6 ; 13 ; moyenne globale 7,53) : $SSW = 77{,}2$, $SSB \approx 230{,}5$ et $SST \approx 307{,}7$, d'où $F \approx 17{,}9$. [[Erreurs du cours#^e-somme-des-carres-sst-ssr-sse|✎]] On divise ensuite chaque somme par ses degrés de liberté pour obtenir les [[Carré moyen|carrés moyens]].

Notion parente : [[Régression linéaire]]. Voir aussi : [[ANOVA]], [[Statistique F]], [[Coefficient de détermination]], [[Carré moyen]].

Résumés : [[10 - linear regression]], [[11 - Multiple Linear Regression and F-statistic]], [[12 - ANOVA and F-statistic]]
