---
type: concept
tags: [year2, year3]
aliases: [normal distribution, Gaussian distribution, loi gaussienne, loi normale centrée réduite, standard normal distribution, règle 68-95-99.7, variable normale, lognormal distribution, loi log-normale, standard normal random variable, table de la loi normale, quantile de la loi normale]
matieres: [Probability, Statistics, Data analysis (Thanos)]
sources: ["[[Chp 5 - Continuous random variable (résumé)|Chp 5 - Continuous random variable]]", "[[Chp3 - More on probability (résumé)|Chp3 - More on probability]]", "[[Chp4 Part2 - Inferential statistics (résumé)|Chp4 Part2 - Inferential statistics]]"]
maj: 2026-11-06
---

$X \sim N(\mu, \sigma)$ de densité $\dfrac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/(2\sigma^2)}$. Règle 68-95-99,7 : $P(|X - \mu| < k\sigma) \approx 68\,\%$, $95\,\%$, $99{,}73\,\%$ pour $k = 1, 2, 3$.

**Centrée réduite** : $Z \sim N(0, 1)$, de fonction de répartition $\Phi$. Si $X \sim N(\mu, \sigma)$, alors $Z = (X - \mu)/\sigma$ est centrée réduite et $P(a \le X \le b) = \Phi\!\left(\frac{b-\mu}{\sigma}\right) - \Phi\!\left(\frac{a-\mu}{\sigma}\right)$, ce qui permet d'utiliser la table de $\Phi$.

**Combinaisons** : toute combinaison linéaire de variables normales indépendantes est normale ([[Chp3 - More on probability (résumé)]]).

**Log-normale** : $X$ est log-normale si $\ln X$ est normale ($\mu$, $\sigma$ sont ceux de $\ln X$). $E(X) = e^{\mu + \sigma^2/2}$, $V(X) = e^{2\mu + \sigma^2}(e^{\sigma^2} - 1)$, $F(x) = \Phi\!\left(\frac{\ln x - \mu}{\sigma}\right)$ ([[Fonction de répartition]]).

**Quantiles usuels** ([[Quantile]]) : $z_{\alpha/2} = 1{,}645$ à 90 %, $1{,}96$ à 95 %, $2{,}58$ à 99 % ([[Chp4 Part2 - Inferential statistics (résumé)]], [[Séance 4 - Estimation (résumé)]]).

Le [[Théorème central limite]] explique son rôle ; voir aussi [[Approximation normale]]. Pour tester la normalité d'un échantillon, voir [[Diagramme de probabilité]].

Notion parente : [[Variable aléatoire]]. Liens : [[Espérance et variance]]

## À vérifier

- [[Chp 5 - Continuous random variable (résumé)|Chp 5 - Continuous random variable]] emploie deux notations dans le même chapitre : $N(\mu, \sigma)$ et $\mathcal{N}(\mu, \sigma^2)$.
- [[Chp3 - More on probability (résumé)|Chp3 - More on probability]] affirme sans preuve qu'une combinaison linéaire de normales indépendantes est normale.

Résumés : [[Chp 5 - Continuous random variable (résumé)]], [[Chp3 - More on probability (résumé)]], [[Chp4 Part2 - Inferential statistics (résumé)]], [[Séance 4 - Estimation (résumé)]]
