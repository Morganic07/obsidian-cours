---
type: concept
tags:
  - year2
  - year3
aliases:
  - exponential distribution
  - exponential random variable
  - loi gamma
  - gamma distribution
  - loi de Weibull
  - Weibull distribution
matieres:
  - Probability
  - Statistics
sources:
  - "[[5 - Continuous random variable|Chp 5 - Continuous random variable]]"
  - "[[4 - Inferential statistics 1|Chp4 Part 1 - Inferential statistics]]"
  - "[[3 - More on probability|Chp3 - More on probability]]"
  - "[[Raw/Year 2/Probability/Chp 5 : Continuous random variable.docx|Chp 5 - Continuous random variable]]"
  - "[[Raw/Year 3/Statistics/Chp3 : More on probability.docx|Chp3 - More on probability]]"
maj: 2026-11-08
---

**Exponentielle** de paramètre $\lambda > 0$ : $f(x) = \lambda e^{-\lambda x}$ pour $x > 0$. $F(x) = 1 - e^{-\lambda x}$ pour $x > 0$. Moyenne et écart-type valent $1/\lambda$.

**Gamma** : la somme de $n$ exponentielles indépendantes de paramètre $\lambda$ suit une gamma $(\alpha = n, \beta = 1/\lambda)$ ; la somme de gammas de même $\beta$ est une gamma $(\alpha_1 + \alpha_2, \beta)$. La [[Loi du khi-deux]] est la gamma $(\nu/2, 2)$.

**Weibull** : $f(x; \alpha, \beta) = \frac{\alpha}{\beta^\alpha}x^{\alpha-1}e^{-(x/\beta)^\alpha}$ pour $x > 0$, $\alpha$ paramètre de forme, $\beta$ paramètre d'échelle. $\alpha = 1$ redonne l'exponentielle de paramètre $1/\beta$ (complément). Elle sert dans le diagramme de Weibull ([[Diagramme de probabilité]]).

## Compléments (hors du cours)

**Exponentielle** :
- $\mathrm{Var}(X) = 1/\lambda^2$ ; fonction génératrice des moments $M_X(t) = \dfrac{\lambda}{\lambda - t}$ pour $t < \lambda$ ([[Fonction génératrice des moments]]).
- **Absence de mémoire** : $P(X > s + t \mid X > s) = \dfrac{e^{-\lambda(s+t)}}{e^{-\lambda s}} = e^{-\lambda t} = P(X > t)$. Un appareil qui a déjà fonctionné $s$ heures a la même loi de durée de vie restante qu'un neuf. C'est la seule loi continue (sur $]0, +\infty[$) qui a cette propriété, l'analogue continu de la [[Loi géométrique]].
- **Usages** : durée d'attente, durée de vie sans usure ; $\lambda$ est un taux (événements par unité de temps), $1/\lambda$ la durée moyenne.
- **Lien avec la [[Loi de Poisson]]** : si le nombre d'événements par unité de temps suit une loi de Poisson de paramètre $\lambda$ (processus de Poisson), le temps entre deux événements consécutifs suit une exponentielle de paramètre $\lambda$.
- **Percentiles** : $F(\eta_p) = p$ donne $\eta_p = -\ln(1-p)/\lambda$. La médiane vaut $\ln 2/\lambda \approx 0{,}693/\lambda$ (la demi-vie en physique), inférieure à la moyenne $1/\lambda$ : la loi est asymétrique à droite.
- **Simulation par inversion** ([[Méthode de la fonction de répartition inverse]]) : si $U \sim \text{Unif}[0, 1)$, $X = -\ln(1 - U)/\lambda$ suit une exponentielle de paramètre $\lambda$.

**Gamma** : densité
$$f(x; \alpha, \beta) = \frac{x^{\alpha-1}e^{-x/\beta}}{\beta^\alpha\,\Gamma(\alpha)}, \quad x > 0,$$
où $\Gamma$ est la [[Fonction Gamma]] ; $E(X) = \alpha\beta$, $\mathrm{Var}(X) = \alpha\beta^2$. Pour $\alpha = 1$, c'est l'exponentielle de moyenne $\beta$ ; la [[Loi du khi-deux]] à $\nu$ degrés de liberté est la gamma $\alpha = \nu/2$, $\beta = 2$.

**Weibull** :
- $E(X) = \beta\,\Gamma\!\left(1 + \frac1\alpha\right)$, $\mathrm{Var}(X) = \beta^2\left[\Gamma\!\left(1 + \frac2\alpha\right) - \Gamma\!\left(1 + \frac1\alpha\right)^2\right]$.
- **Taux de défaillance** $h(x) = \dfrac{f(x)}{1 - F(x)} = \dfrac{\alpha}{\beta^\alpha}x^{\alpha-1}$ : décroissant si $\alpha < 1$ (défaillances de jeunesse), constant si $\alpha = 1$ (exponentielle, sans mémoire), croissant si $\alpha > 1$ (usure). C'est ce qui fait de Weibull la loi de référence en fiabilité.
- Si $X$ suit une Weibull $(\alpha, \beta)$, $\ln X$ suit la [[Loi des valeurs extrêmes]] avec $\theta_1 = \ln\beta$ et $\theta_2 = 1/\alpha$.

Notion parente : [[Variable aléatoire]]. Voir aussi : [[Fonction de répartition]], [[Stabilité des lois par somme]], [[Diagramme de probabilité]], [[Fonction Gamma]].

Résumés : [[5 - Continuous random variable]], [[4 - Inferential statistics 1]], [[3 - More on probability]]
