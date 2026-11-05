---
type: source
sources: ["[[Chp 6 - Joint probability distributions]]"]
maj: 2026-11-05
---

Résumé de [[Chp 6 - Joint probability distributions]], dans [[Year 2 - Probability]]. En cas d'écart, le cours et ses images font foi. Les images n'ont pas été ouvertes : seules leurs transcriptions ont été lues.

## Idée générale

Étudier plusieurs variables à la fois : loi conjointe, lois marginales, indépendance, covariance, corrélation, combinaisons linéaires et loi d'une somme.

## Contenu, dans l'ordre du cours

- **[[Loi conjointe]]** : pour deux variables discrètes, $p(x, y) = P(X = x \text{ et } Y = y)$, avec $p \ge 0$ et $\sum p = 1$, et $P((X,Y) \in A) = \sum_A p$. Pour deux variables continues, la densité conjointe $f$ vérifie $P((X, Y) \in A) = \iint_A f$ ; sur un rectangle, $\int_a^b\int_c^d f\,dy\,dx$. La définition s'étend à $n$ variables.
- **Lois marginales** : $p_X(x) = \sum_y p(x, y)$, $p_Y(y) = \sum_x p(x, y)$ ; $f_X(x) = \int f(x, y)\,dy$, $f_Y(y) = \int f(x, y)\,dx$.
- **Indépendance** : $X$ et $Y$ sont indépendantes si $p(x, y) = p_X(x)p_Y(y)$ (discret) ou $f(x, y) = f_X(x)f_Y(y)$ (continu) pour tout couple. Sinon elles sont dépendantes.
- **Espérance d'une fonction de deux variables** : $E[h(X, Y)] = \sum\sum h\,p$ ou $\iint h f$. La linéarité reste vraie. Si $X$ et $Y$ sont indépendantes, $E[g_1(X)g_2(Y)] = E[g_1(X)]E[g_2(Y)]$.
- **[[Covariance et corrélation]]** : $\mathrm{Cov}(X, Y) = E[(X-\mu_X)(Y-\mu_Y)]$. Propriétés : symétrie, $\mathrm{Cov}(X, X) = \mathrm{Var}(X)$, formule raccourcie $E(XY) - \mu_X\mu_Y$, et $\mathrm{Cov}(aX + bY + c, Z) = a\mathrm{Cov}(X, Z) + b\mathrm{Cov}(Y, Z)$. Un nuage qui monte donne une covariance positive, un nuage qui descend une covariance négative.
- **Corrélation** : $\rho_{X,Y} = \mathrm{Cov}(X, Y)/(\sigma_X\sigma_Y)$. Si $X$ et $Y$ sont indépendantes, $\rho = 0$, mais $\rho = 0$ n'entraîne pas l'indépendance. $\rho = \pm 1$ si et seulement si $Y = aX + b$ avec $a \ne 0$. Corrélation n'est pas causalité (exemple : vocabulaire et caries chez l'enfant, liés par l'âge).
- **Non corrélées** : $X$ et $Y$ le sont si et seulement si $E[XY] = \mu_X\mu_Y$.
- **Combinaisons linéaires** : $a_1X_1 + \dots + a_nX_n + b$, dont la moyenne empirique $\bar{X}$ avec $a_i = 1/n$. Sans hypothèse d'indépendance, $E = \sum a_i\mu_i + b$ et $\mathrm{Var} = \sum_i\sum_j a_ia_j\mathrm{Cov}(X_i, X_j)$. Si les $X_i$ sont indépendantes, $\mathrm{Var} = \sum a_i^2\sigma_i^2$. Pour $n = 2$ : $\mathrm{Var}(X_1 \pm X_2) = \mathrm{Var}(X_1) + \mathrm{Var}(X_2)$ si indépendantes.
- **Loi d'une somme** : si $X$ et $Y$ sont indépendantes et continues, $f_W(w) = \int f_X(x)f_Y(w - x)\,dx$ pour $W = X + Y$ (produit de convolution). Les bornes sont celles où $f_X(x) > 0$ et $f_Y(w - x) > 0$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **« $b = 0$ » dans la combinaison linéaire** : la note écrit « constants $a_1, \dots, a_n$, $b = 0$ » alors que $b$ est une constante quelconque dans le théorème qui suit. Seule la moyenne empirique impose $b = 0$ (complément).
2. **Distributivité de la covariance** : l'énoncé donne $\mathrm{Cov}(aX + bY + c, Z) = a\mathrm{Cov}(X, Z) + b\mathrm{Cov}(Y, Z)$. C'est juste, la constante $c$ disparaissant (complément).
3. **Événement sur $S \times S$** : la phrase sur $P((X, Y) \in A)$ parle d'un événement de « $S \times S$ ». Le cadre est celui des couples de valeurs $(x, y)$, pas de l'espace $S$ lui-même. À vérifier sur l'image, non ouverte.
4. **Images tronquées** : le « $y$ » isolé après les lois marginales est le début d'un schéma coupé. Rien n'en est repris.
