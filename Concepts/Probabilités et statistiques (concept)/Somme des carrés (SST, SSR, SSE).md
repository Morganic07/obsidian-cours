---
type: concept
tags: [year3]
aliases: [SST, SSR, SSE, TSS, RSS, sum of squares, somme des carrés totale, somme des carrés résiduelle, SSW, SSB, décomposition de la variation]
matieres: [Data analysis (Thanos)]
sources: ["[[Séance 10 - linear regression (résumé)|Cours 10 - linear regression]]", "[[Séance 12 - ANOVA and F-statistic (résumé)|Cours 12 - ANOVA and F-statistic]]"]
maj: 2026-11-06
---

En régression ([[Séance 10 - linear regression (résumé)|Cours 10 - linear regression]]) :

- $SST = \sum (y_i - \bar y)^2$, variation totale ;
- $SSR = \sum (\hat y_i - \bar y)^2$, variation expliquée ;
- $SSE = \sum (y_i - \hat y_i)^2$, variation non expliquée.

On a $SST = SSR + SSE$, car le terme croisé s'annule.

En [[ANOVA]], $SST = SSW + SSB$ : variation intra-groupes et inter-groupes ([[Séance 12 - ANOVA and F-statistic (résumé)|Cours 12 - ANOVA and F-statistic]]). On divise ensuite chaque somme par ses degrés de liberté pour obtenir les [[Carré moyen|carrés moyens]].

Notion parente : [[Régression linéaire]]. Voir aussi : [[ANOVA]], [[Statistique F]], [[Coefficient de détermination]], [[Carré moyen]].

## À vérifier

- Les valeurs SSW = 54 et SSB = 203,3 de l'exemple de Cours 12 ne correspondent pas aux données affichées : on recalcule 77,2 et environ 230,5.
- RSS désigne ici la somme résiduelle : à ne pas confondre avec SSR, la somme expliquée.

Résumés : [[Séance 10 - linear regression (résumé)]], [[Séance 11 - Multiple Linear Regression and F-statistic (résumé)]], [[Séance 12 - ANOVA and F-statistic (résumé)]]
