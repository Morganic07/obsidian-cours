---
type: concept
tags:
  - year2
  - year3
aliases:
  - normal distribution
  - Gaussian distribution
  - loi gaussienne
  - loi normale centrée réduite
  - standard normal distribution
  - règle 68-95-99.7
  - variable normale
  - lognormal distribution
  - loi log-normale
  - standard normal random variable
  - table de la loi normale
  - quantile de la loi normale
matieres:
  - Probability
  - Statistics
  - Data analysis (Thanos)
sources:
  - "[[5 - Continuous random variable|Chp 5 - Continuous random variable]]"
  - "[[3 - More on probability|Chp3 - More on probability]]"
  - "[[4 - Inferential statistics 2|Chp4 Part2 - Inferential statistics]]"
maj: 2026-11-08
---

$X \sim N(\mu, \sigma)$ de densité $\dfrac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/(2\sigma^2)}$. Règle 68-95-99,7 : $P(|X - \mu| < k\sigma) \approx 68\,\%$, $95\,\%$, $99{,}73\,\%$ pour $k = 1, 2, 3$.

**Centrée réduite** : $Z \sim N(0, 1)$, de fonction de répartition $\Phi$. Si $X \sim N(\mu, \sigma)$, alors $Z = (X - \mu)/\sigma$ est centrée réduite et $P(a \le X \le b) = \Phi\!\left(\frac{b-\mu}{\sigma}\right) - \Phi\!\left(\frac{a-\mu}{\sigma}\right)$, ce qui permet d'utiliser la table de $\Phi$.

**Combinaisons** : toute combinaison linéaire de variables normales indépendantes est normale ([[3 - More on probability]]).

**Log-normale** : $X$ est log-normale si $\ln X$ est normale ($\mu$, $\sigma$ sont ceux de $\ln X$). $E(X) = e^{\mu + \sigma^2/2}$, $V(X) = e^{2\mu + \sigma^2}(e^{\sigma^2} - 1)$, $F(x) = \Phi\!\left(\frac{\ln x - \mu}{\sigma}\right)$ ([[Fonction de répartition]]). Densité, pour $x > 0$ : $f(x; \mu, \sigma) = \dfrac{1}{\sqrt{2\pi}\,\sigma x}\exp\!\left(-\dfrac{(\ln x - \mu)^2}{2\sigma^2}\right)$ ([[3 - More on probability]]).

*Complément (hors du cours)* : la médiane vaut $e^\mu$, inférieure à la moyenne $e^{\mu + \sigma^2/2}$ (asymétrie à droite). La loi log-normale apparaît quand une grandeur positive est le produit de nombreux facteurs indépendants : son logarithme est une somme, approximativement normale par le [[Théorème central limite]]. Elle modélise revenus, tailles de particules, durées de réparation. Elle n'a pas de [[Fonction génératrice des moments]] ($E(e^{tX})$ est infinie pour tout $t > 0$). Passer au logarithme correspond à la [[Transformation puissance]] de paramètre $p = 0$.

**Quantiles usuels** ([[Quantile]]) : $z_{\alpha/2} = 1{,}645$ à 90 %, $1{,}96$ à 95 %, $2{,}58$ à 99 % ([[4 - Inferential statistics 2]], [[4 - Estimation]]).

Le [[Théorème central limite]] explique son rôle ; voir aussi [[Approximation normale]]. Pour tester la normalité d'un échantillon, voir [[Diagramme de probabilité]].

Notion parente : [[Variable aléatoire]]. Liens : [[Espérance et variance]]

Résumés : [[5 - Continuous random variable]], [[3 - More on probability]], [[4 - Inferential statistics 2]], [[4 - Estimation]]
