---
type: concept
tags: [year2, year3]
aliases: [exponential distribution, exponential random variable, loi gamma, gamma distribution, loi de Weibull, Weibull distribution]
matieres: [Probability, Statistics]
sources: ["[[Chp 5 - Continuous random variable (résumé)|Chp 5 - Continuous random variable]]", "[[Chp4 Part 1 - Inferential statistics (résumé)|Chp4 Part 1 - Inferential statistics]]", "[[Chp3 - More on probability (résumé)|Chp3 - More on probability]]"]
maj: 2026-11-06
---

**Exponentielle** de paramètre $\lambda > 0$ : $f(x) = \lambda e^{-\lambda x}$ pour $x > 0$. $F(x) = 1 - e^{-\lambda x}$ pour $x > 0$. Moyenne et écart-type valent $1/\lambda$.

**Gamma** : la somme de $n$ exponentielles indépendantes de paramètre $\lambda$ suit une gamma $(\alpha = n, \beta = 1/\lambda)$ ; la somme de gammas de même $\beta$ est une gamma $(\alpha_1 + \alpha_2, \beta)$. La [[Loi du khi-deux]] est la gamma $(\nu/2, 2)$.

**Weibull** : $f(x; \alpha, \beta) = \frac{\alpha}{\beta^\alpha}x^{\alpha-1}e^{-(x/\beta)^\alpha}$ pour $x > 0$, $\alpha$ paramètre de forme, $\beta$ paramètre d'échelle. $\alpha = 1$ redonne l'exponentielle de paramètre $1/\beta$ (complément). Elle sert dans le diagramme de Weibull ([[Diagramme de probabilité]]).

Notion parente : [[Variable aléatoire]]. Voir aussi : [[Fonction de répartition]], [[Stabilité des lois par somme]], [[Diagramme de probabilité]], [[Fonction Gamma]].

Résumés : [[Chp 5 - Continuous random variable (résumé)]], [[Chp4 Part 1 - Inferential statistics (résumé)]], [[Chp3 - More on probability (résumé)]]
