---
type: concept
tags: [year2]
aliases: [geometric distribution, geometric random variable]
sources: ["[[Raw/Year 2/Probability/Chp 3 : Important discrete distributions.docx|Chp 3 - Important discrete distributions]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : on répète des épreuves de Bernoulli indépendantes de même probabilité de succès $p \in ]0, 1]$. La variable $X$ = nombre d'essais nécessaires pour obtenir le **premier** succès (celui-ci compris) suit la loi géométrique de paramètre $p$, notée $\mathcal{G}(p)$.

**Loi** : il faut $x - 1$ échecs puis un succès, d'où
$$P(X = x) = (1-p)^{x-1}\,p, \qquad x = 1, 2, \dots$$
et, puisque $X > k$ signifie « $k$ premiers essais ratés », $P(X > k) = (1-p)^k$, donc $F(k) = 1 - (1-p)^k$.

**Moments** :
$$E(X) = \frac1p, \qquad \mathrm{Var}(X) = \frac{1-p}{p^2}.$$

**Lien avec la binomiale négative** : c'est la [[Loi binomiale négative]] pour $r = 1$. Inversement, une binomiale négative $(r, p)$ est la somme de $r$ géométriques indépendantes (attente du 1ᵉʳ succès, puis du 2ᵉ, etc.), d'où $E = r/p$ et $\mathrm{Var} = r(1-p)/p^2$.

**Variante** : certains manuels comptent le nombre $Y = X - 1$ d'**échecs** avant le premier succès, à valeurs dans $0, 1, 2, \dots$ : $P(Y = y) = (1-p)^y p$ et $E(Y) = (1-p)/p$. Vérifier la convention avant d'appliquer une formule.

**Absence de mémoire** : pour $s, t$ entiers positifs,
$$P(X > s + t \mid X > s) = \frac{(1-p)^{s+t}}{(1-p)^s} = (1-p)^t = P(X > t).$$
Avoir déjà échoué $s$ fois ne rapproche pas du succès : croire qu'un numéro « doit » sortir après une longue absence est l'**erreur du joueur**. C'est la seule loi discrète (sur $\{1, 2, \dots\}$) sans mémoire, l'analogue discret de la [[Loi exponentielle]].

**Exemple** : nombre de lancers d'un dé équilibré pour obtenir le premier 6, $p = 1/6$ : $E(X) = 6$, $\mathrm{Var}(X) = (5/6)/(1/36) = 30$, et $P(X > 6) = (5/6)^6 \approx 0{,}335$.

## Dans le cours

Le cours ne la traite pas en tant que telle. Elle apparaît comme cas $r = 1$ de la binomiale négative dans les compléments de [[3 - Important discrete distributions]].

Voir aussi : [[Loi binomiale négative]], [[Loi exponentielle]], [[Loi binomiale]], [[Variable aléatoire]].

Résumés : [[3 - Important discrete distributions]]
