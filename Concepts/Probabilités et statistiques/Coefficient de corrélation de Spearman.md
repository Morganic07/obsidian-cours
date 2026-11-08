---
type: concept
tags: [year3]
aliases: [Spearman, rho de Spearman, Spearman's rank correlation, corrélation de Spearman, corrélation de rang, rank correlation, rangs ex æquo]
matieres: [Data analysis (Thanos)]
sources: ["[[9 - Covariance and Correlation|Cours 9 - Covariance and Correlation]]"]
maj: 2026-11-08
---

Corrélation de rang, non paramétrique, qui mesure une relation **monotone** entre variables continues ou ordinales.

- Sans ex æquo : $\rho = 1 - \dfrac{6\sum d_i^2}{n(n^2-1)}$, où $d_i$ est l'écart entre les rangs.
- Avec ex æquo : on applique la corrélation de Pearson aux rangs, chaque ex æquo recevant la moyenne des rangs concernés.

Exemple du cours : pour une relation monotone non linéaire, Pearson vaut 0,851 et Spearman 1 ; pour une relation monotone décroissante, Pearson vaut −0,799 et Spearman exactement −1. [[Erreurs du cours#^e-coefficient-de-correlation-de-spearman|✎]]

**Lien avec Pearson (complément, hors du cours)** : la formule $1 - \dfrac{6\sum d_i^2}{n(n^2-1)}$ est un raccourci de la corrélation de Pearson appliquée aux rangs, obtenu parce que les rangs $1, \dots, n$ ont une moyenne et une variance connues. Sans ex æquo, les deux calculs donnent exactement le même résultat ; avec des ex æquo, seule la formule de Pearson sur les rangs est exacte.

**Exemple (complément, hors du cours)** : rangs $X = (1, 2, 3, 4, 5)$ et $Y = (2, 1, 4, 3, 5)$, d'où $d = (-1, 1, -1, 1, 0)$, $\sum d_i^2 = 4$ et $\rho = 1 - \dfrac{6 \times 4}{5 \times 24} = 1 - \dfrac{24}{120} = 0{,}8$. Sur les mêmes données, le [[Tau de Kendall]] vaut 0,6.

**Robustesse (complément, hors du cours)** : comme il ne retient que les rangs, le coefficient est peu sensible aux valeurs aberrantes, contrairement à Pearson (voir [[Quatuor d'Anscombe]]). En R : `cor(x, y, method = "spearman")`, et `cor.test(x, y, method = "spearman")` pour le test.

Notion parente : [[Covariance et corrélation]]. Voir aussi : [[Tau de Kendall]], [[Test paramétrique et non paramétrique]].

Résumés : [[9 - Covariance and Correlation]]
