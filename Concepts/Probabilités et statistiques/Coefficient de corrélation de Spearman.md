---
type: concept
tags: [year3]
aliases: [Spearman, rho de Spearman, Spearman's rank correlation, corrélation de Spearman, corrélation de rang, rank correlation, rangs ex æquo]
matieres: [Data analysis (Thanos)]
sources: ["[[9 - Covariance and Correlation|Cours 9 - Covariance and Correlation]]"]
maj: 2026-11-07
---

Corrélation de rang, non paramétrique, qui mesure une relation **monotone** entre variables continues ou ordinales.

- Sans ex æquo : $\rho = 1 - \dfrac{6\sum d_i^2}{n(n^2-1)}$, où $d_i$ est l'écart entre les rangs.
- Avec ex æquo : on applique la corrélation de Pearson aux rangs, chaque ex æquo recevant la moyenne des rangs concernés.

Exemple du cours : pour une relation monotone non linéaire, Pearson vaut 0,851 et Spearman 1.

Notion parente : [[Covariance et corrélation]]. Voir aussi : [[Tau de Kendall]], [[Test paramétrique et non paramétrique]].

## Erreurs du cours

- [[9 - Covariance and Correlation|Cours 9 - Covariance and Correlation]] (image vérifiée) écrit, pour la relation monotone décroissante (Pearson $= -0.799$, Spearman $= -1$), « → Spearman is exactly 1 » ; il faut « Spearman is exactly −1 ».

Résumés : [[9 - Covariance and Correlation]]
