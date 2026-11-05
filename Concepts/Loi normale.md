---
type: concept
aliases: [normal distribution, Gaussian distribution, loi gaussienne, loi normale centrée réduite, standard normal distribution, règle 68-95-99.7, variable normale, lognormal distribution, loi log-normale]
matieres: [Probability, Statistics]
sources: ["[[Chp 5 - Continuous random variable]]", "[[Chp3 - More on probability]]"]
maj: 2026-11-05
---

$X \sim N(\mu, \sigma)$ de densité $\dfrac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/(2\sigma^2)}$. Règle 68-95-99,7 : $P(|X - \mu| < k\sigma) \approx 68\,\%$, $95\,\%$, $99{,}73\,\%$ pour $k = 1, 2, 3$.

**Centrée réduite** : $Z \sim N(0, 1)$, de fonction de répartition $\Phi$. Si $X \sim N(\mu, \sigma)$, alors $Z = (X - \mu)/\sigma$ est centrée réduite et $P(a \le X \le b) = \Phi\!\left(\frac{b-\mu}{\sigma}\right) - \Phi\!\left(\frac{a-\mu}{\sigma}\right)$, ce qui permet d'utiliser la table de $\Phi$.

**Combinaisons** : toute combinaison linéaire de variables normales indépendantes est normale ([[Chp3 - More on probability (résumé)]]).

**Log-normale** : $X$ est log-normale si $\ln X$ est normale ($\mu$, $\sigma$ sont ceux de $\ln X$). $E(X) = e^{\mu + \sigma^2/2}$, $F(x) = \Phi\!\left(\frac{\ln x - \mu}{\sigma}\right)$.

Le [[Théorème central limite]] explique son rôle. Pour tester la normalité d'un échantillon, voir [[Diagramme de probabilité]].

Liens : [[Variable aléatoire]], [[Espérance et variance]]

Résumés : [[Chp 5 - Continuous random variable (résumé)]], [[Chp3 - More on probability (résumé)]]
