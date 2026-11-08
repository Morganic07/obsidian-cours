---
type: concept
tags: [year2]
aliases: [conditional distribution, conditional pmf, conditional pdf, espérance conditionnelle, conditional expectation, densité conditionnelle]
sources: ["[[Raw/Year 2/Probability/Chp 6 : Joint probability distributions.docx|Chp 6 - Joint probability distributions]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : la loi de $Y$ sachant $X = x$, définie pour $p_X(x) > 0$ (ou $f_X(x) > 0$), est

$$p_{Y|X}(y \mid x) = \frac{p(x, y)}{p_X(x)} \quad \text{(discret)}, \qquad f_{Y|X}(y \mid x) = \frac{f(x, y)}{f_X(x)} \quad \text{(continu)},$$

où $p$ (ou $f$) est la [[Loi conjointe]] et $p_X$ (ou $f_X$) la loi marginale de $X$. Pour chaque $x$ fixé, c'est une loi de probabilité en $y$ : elle est positive, de somme (ou d'intégrale) égale à 1. Dans le cas discret, c'est la [[Probabilité conditionnelle]] $P(Y = y \mid X = x)$.

**Indépendance** : $X$ et $Y$ sont indépendantes si et seulement si la loi conditionnelle de $Y$ sachant $X = x$ ne dépend pas de $x$ et égale la marginale : $p_{Y|X}(y \mid x) = p_Y(y)$ (ou $f_{Y|X}(y \mid x) = f_Y(y)$) pour tout $x$ où elle est définie ([[Indépendance de variables aléatoires]]).

**Espérance conditionnelle** :

$$E(Y \mid X = x) = \sum_y y\,p_{Y|X}(y \mid x) \quad \text{ou} \quad \int y\,f_{Y|X}(y \mid x)\,dy.$$

Vue comme fonction de $x$, c'est la courbe de régression de $Y$ sur $X$, base de la [[Régression linéaire]].

**Exemple** : $p(0,0) = 0{,}2$, $p(0,1) = 0{,}3$, $p(1,0) = 0{,}1$, $p(1,1) = 0{,}4$. Alors $p_X(1) = 0{,}5$ et $P(Y = 1 \mid X = 1) = 0{,}4/0{,}5 = 0{,}8$, tandis que $p_X(0) = 0{,}5$ et $P(Y = 1 \mid X = 0) = 0{,}3/0{,}5 = 0{,}6$. La loi conditionnelle dépend de $x$ : $X$ et $Y$ sont dépendantes.

## Dans le cours

Le chapitre 6 de Probability ne la définit pas. Elle est ajoutée dans les compléments de [[6 - Joint probability distributions]].

Voir aussi : [[Loi conjointe]], [[Probabilité conditionnelle]], [[Indépendance de variables aléatoires]], [[Régression linéaire]], [[Covariance et corrélation]]

Résumés : [[6 - Joint probability distributions]]
