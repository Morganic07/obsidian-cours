---
type: concept
tags: [year3]
aliases: [Spearman, rho de Spearman, Spearman's rank correlation, corrélation de Spearman, corrélation de rang, rank correlation, rangs ex æquo]
matieres: [Data analysis (Thanos)]
sources: ["[[Cours 9 - Covariance and Correlation]]"]
maj: 2026-11-06
---

Corrélation de rang, non paramétrique, qui mesure une relation **monotone** entre variables continues ou ordinales.

- Sans ex æquo : $\rho = 1 - \dfrac{6\sum d_i^2}{n(n^2-1)}$, où $d_i$ est l'écart entre les rangs.
- Avec ex æquo : on applique la corrélation de Pearson aux rangs, chaque ex æquo recevant la moyenne des rangs concernés.

Exemple du cours : pour une relation monotone non linéaire, Pearson vaut 0,851 et Spearman 1.

Notion parente : [[Covariance et corrélation]]. Voir aussi : [[Tau de Kendall]], [[Test paramétrique et non paramétrique]].

## À vérifier

Pour une relation décroissante, le cours écrit « Spearman is exactly 1 » au lieu de −1.

Résumés : [[Séance 9 - Covariance and Correlation (résumé)]]
