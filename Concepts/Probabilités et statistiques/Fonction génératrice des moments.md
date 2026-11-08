---
type: concept
tags: [year2, year3]
aliases: [moment generating function, mgf, MGF]
matieres: [Probability, Statistics]
sources: ["[[5 - Continuous random variable|Chp 5 - Continuous random variable]]", "[[3 - More on probability|Chp3 - More on probability]]", "[[Raw/Year 3/Statistics/Chp3 : More on probability.docx|Chp3 - More on probability]]"]
maj: 2026-11-08
---

$M_X(t) = E(e^{tX})$, définie par $\int e^{tx}f(x)\,dx$ pour une variable continue. Elle existe si elle est définie sur un intervalle contenant 0, avec des $t$ positifs et négatifs. $M_X(0) = 1$ et $E(X^r) = M_X^{(r)}(0)$ (dérivée évaluée en 0). [[Erreurs du cours#^e-fonction-generatrice-des-moments|✎]]

Elle détermine la loi : deux lois ayant la même fonction génératrice (si elle existe) sont égales.

Pour des variables indépendantes, $M_{X+Y}(t) = M_X(t)M_Y(t)$, et pour $Y = \sum a_iX_i + b$, $M_Y(t) = e^{bt}\prod M_{X_i}(a_it)$ ; par exemple $M_{aX+bY+c}(t) = M_X(at)\,M_Y(bt)\,e^{ct}$. [[Erreurs du cours#^e-fonction-generatrice-des-moments|✎]]

**Cas discret** : $M_X(t) = E(e^{tX}) = \sum_x e^{tx}\,p(x)$, la somme portant sur les valeurs possibles de $X$. [[Complément hors du cours|ⓘ]]

**Pourquoi les dérivées en 0 donnent les moments** : en développant l'exponentielle en [[Série entière|série entière]], $e^{tX} = \sum_{k \ge 0} \frac{t^k X^k}{k!}$, donc, quand on peut échanger espérance et somme (c'est le cas si $M_X$ existe), [[Complément hors du cours|ⓘ]]
$$M_X(t) = \sum_{k \ge 0} \frac{E(X^k)}{k!}\,t^k = 1 + E(X)\,t + \frac{E(X^2)}{2}\,t^2 + \cdots$$
Le coefficient de $t^k/k!$ est le moment d'ordre $k$, d'où $M_X^{(k)}(0) = E(X^k)$ ; c'est l'origine du nom. En particulier $E(X) = M_X'(0)$ et $V(X) = E(X^2) - E(X)^2 = M_X''(0) - M_X'(0)^2$ ([[Espérance et variance]]). [[Complément hors du cours|ⓘ]]

**Lois usuelles** : [[Complément hors du cours|ⓘ]]

| Loi | $M_X(t)$ | Domaine |
|---|---|---|
| Bernoulli $\mathcal{B}(p)$ | $1 - p + pe^t$ | $t \in \mathbb{R}$ |
| [[Loi binomiale\|Binomiale]] $\mathrm{Bin}(n, p)$ | $(1 - p + pe^t)^n$ | $t \in \mathbb{R}$ |
| [[Loi de Poisson\|Poisson]] $\mathcal{P}(\mu)$ | $e^{\mu(e^t - 1)}$ | $t \in \mathbb{R}$ |
| [[Loi exponentielle\|Exponentielle]] $\mathcal{E}(\lambda)$ | $\dfrac{\lambda}{\lambda - t}$ | $t < \lambda$ |
| [[Loi normale\|Normale]] $N(\mu, \sigma)$ | $e^{\mu t + \sigma^2 t^2/2}$ | $t \in \mathbb{R}$ |

Exemple : pour l'exponentielle, $M'(t) = \frac{\lambda}{(\lambda - t)^2}$ et $M''(t) = \frac{2\lambda}{(\lambda - t)^3}$, d'où $E(X) = 1/\lambda$, $E(X^2) = 2/\lambda^2$ et $V(X) = 1/\lambda^2$. [[Complément hors du cours|ⓘ]]

**Elle n'existe pas toujours** : pour la loi log-normale (loi de $e^Y$ avec $Y$ normale), $E(e^{tX})$ est infinie pour tout $t > 0$, bien que tous les moments $E(X^k)$ soient finis. Il faut alors d'autres outils, comme la fonction caractéristique $E(e^{itX})$, qui existe toujours. [[Complément hors du cours|ⓘ]]

**Application, [[Stabilité des lois par somme|stabilité par somme]]** : grâce au produit pour des variables indépendantes et à l'unicité, on identifie la loi d'une somme en reconnaissant sa fonction génératrice : [[Complément hors du cours|ⓘ]]
- combinaison linéaire de normales indépendantes $X_i \sim N(\mu_i, \sigma_i)$ : $M_{\sum a_iX_i + b}(t) = e^{bt}\prod_i e^{a_i\mu_i t + a_i^2\sigma_i^2t^2/2} = e^{(b + \sum a_i\mu_i)t + (\sum a_i^2\sigma_i^2)t^2/2}$, celle d'une normale de moyenne $b + \sum a_i\mu_i$ et de variance $\sum a_i^2\sigma_i^2$ ;
- somme de Poisson indépendantes $\mathcal{P}(\mu_i)$ : $\prod_i e^{\mu_i(e^t - 1)} = e^{(\sum \mu_i)(e^t - 1)}$, donc une Poisson $\mathcal{P}(\sum \mu_i)$ ;
- somme de binomiales indépendantes $\mathrm{Bin}(n_i, p)$ de **même** $p$ : $\prod_i (1 - p + pe^t)^{n_i} = (1 - p + pe^t)^{\sum n_i}$, donc une $\mathrm{Bin}(\sum n_i, p)$. Avec des $p$ différents, le produit n'a plus cette forme et la somme n'est pas binomiale.

Notion parente : [[Espérance et variance]]. Voir aussi : [[Variable aléatoire]], [[Loi normale]].

Résumés : [[5 - Continuous random variable]], [[3 - More on probability]]
