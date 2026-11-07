---
type: concept
tags: [year2, year3]
aliases: [Percentile d'une loi continue, (100p)th percentile, percentile of a distribution, median of a continuous distribution, médiane d'une loi continue, quantiles, z_α, percentile, percentiles]
matieres: [Probability, Statistics, Data analysis (Thanos)]
sources: ["[[chp 5 - Continuous random variable (résumé)|Chp 5 - Continuous random variable]]", "[[chp 4 - Part 2 - Inferential statistics (résumé)|Chp4 Part2 - Inferential statistics]]"]
maj: 2026-11-06
---

**Probability** : pour $0<p<1$, le $(100p)$-ième percentile $\eta_p$ de la loi continue de $X$ est défini par $p=F(\eta_p)$, soit $\eta_p=F^{-1}(p)$ si l'inverse existe. La **médiane** est $\eta_{0{,}5}$ : la moitié de l'aire sous la densité est à sa gauche. Pour une densité symétrique, la médiane est le centre de symétrie.

**Statistics** : le quantile $z_\alpha$ de la loi normale centrée réduite vérifie $P(Z > z_\alpha) = \alpha$, donc $P(-z_{\alpha/2} < Z < z_{\alpha/2}) = 1 - \alpha$. Valeurs usuelles de $z_{\alpha/2}$ :

| Niveau | $z_{\alpha/2}$ |
|---|---|
| 99,73 % | 3,00 |
| 99 % | 2,58 |
| 95 % | 1,96 |
| 90 % | 1,645 |
| 50 % | 0,6745 |

En R, la fonction `quantile()`.

Pour un échantillon, voir [[Quartiles et valeurs aberrantes]].

Notion parente : [[Fonction de répartition]]. Voir aussi : [[Méthode de la fonction de répartition inverse]], [[Valeur critique]], [[Intervalle de confiance]], [[Loi normale]].

Résumés : [[chp 5 - Continuous random variable (résumé)]], [[chp 4 - Part 2 - Inferential statistics (résumé)]], [[Summary functions in RStudio (résumé)]]
