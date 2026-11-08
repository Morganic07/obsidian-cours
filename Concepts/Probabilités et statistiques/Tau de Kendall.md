---
type: concept
tags: [year3]
aliases: [Kendall, Kendall tau, Kendall's tau, τ de Kendall, paires concordantes, paires discordantes, concordant pairs, discordant pairs, tau-b de Kendall, Kendall tau-b]
matieres: [Data analysis (Thanos)]
sources: ["[[9 - Covariance and Correlation|Cours 9 - Covariance and Correlation]]"]
maj: 2026-11-08
---

Coefficient de corrélation non paramétrique fondé sur les rangs. C'est une alternative à Pearson quand ses hypothèses ne sont pas remplies, et au [[Coefficient de corrélation de Spearman|ρ de Spearman]] pour un petit échantillon avec beaucoup d'ex æquo. Il compte les paires concordantes (écarts de même signe) et discordantes. Il est en général plus petit que le ρ de Spearman ([[9 - Covariance and Correlation|Cours 9 - Covariance and Correlation]]).

**Formule (complément, hors du cours ; le cours ne la donne pas)** : sans ex æquo, avec $n_c$ paires concordantes et $n_d$ paires discordantes parmi les $\binom{n}{2}$ paires,

$$\tau = \frac{n_c - n_d}{n(n-1)/2}$$

$\tau$ vaut 1 si toutes les paires sont concordantes et $-1$ si toutes sont discordantes. Il s'interprète directement : $\tau = P(\text{paire concordante}) - P(\text{paire discordante})$. Avec des ex æquo, on utilise le $\tau_b$, qui corrige le dénominateur des paires ex æquo sur $X$ ou sur $Y$ : $\tau_b = \dfrac{n_c - n_d}{\sqrt{(n_0 - n_1)(n_0 - n_2)}}$, avec $n_0 = n(n-1)/2$ et $n_1$, $n_2$ les nombres de paires ex æquo sur $X$ et sur $Y$. En R : `cor(x, y, method = "kendall")`.

**Exemple (complément, hors du cours)** : rangs $X = (1, 2, 3, 4, 5)$ et $Y = (2, 1, 4, 3, 5)$. Seules les paires (1, 2) et (3, 4) sont discordantes : $n_c = 8$, $n_d = 2$, donc $\tau = \dfrac{8 - 2}{10} = 0{,}6$, contre un [[Coefficient de corrélation de Spearman|ρ de Spearman]] de 0,8 sur les mêmes données.

Notion parente : [[Covariance et corrélation]]. Voir aussi : [[Coefficient de corrélation de Spearman]].

Résumés : [[9 - Covariance and Correlation]]
