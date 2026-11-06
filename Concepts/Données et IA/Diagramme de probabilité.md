---
type: concept
tags: [year3]
aliases: [probability plot, normal probability plot, diagramme de probabilité normal, Weibull probability plot, diagramme de Weibull, Q-Q plot, qqnorm, QQ plot]
matieres: [Statistics, Data analysis (Thanos)]
sources: ["[[Chp3 - More on probability]]"]
maj: 2026-11-06
---

On trace les $n$ points $(x_{(i)}, y_i)$ : $x_{(i)}$ est la $i$-ème plus petite observation, $y_i$ le percentile $100(i - 0{,}5)/n$ de la loi de la population. Si les points suivent $y = x$, l'échantillon suit cette loi.

**Diagramme normal** : si les observations sont normales, les points sont proches d'une droite (pas forcément à 45°). Des écarts classent la loi : queues légères, queues lourdes ou asymétrique.

**Diagramme de Weibull** : on trace $x' = \ln x$ contre $y' = \ln(-\ln(1-p))$, avec $p = (i - 0{,}5)/n$ ([[Loi exponentielle]]).

**En Data analysis** : le diagramme normal sert à contrôler la normalité des résidus d'une régression ([[Résidu (régression)]]) ; en R, il s'obtient avec `qqnorm`.

Liens : [[Loi normale]], [[Quartiles et valeurs aberrantes]], [[Forme d'une distribution]]

Résumés : [[Chp3 - More on probability (résumé)]], [[Séance 10 - linear regression (résumé)]], [[Summary functions in RStudio (résumé)]]
