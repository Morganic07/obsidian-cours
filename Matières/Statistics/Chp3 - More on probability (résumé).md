---
type: source
tags: [year3]
sources: ["[[Chp3 - More on probability]]"]
maj: 2026-11-05
---

Résumé de [[Chp3 - More on probability]], dans [[Statistics (matière)]]. En cas d'écart, le cours et ses images font foi. Les images n'ont pas été ouvertes : seules leurs transcriptions ont été lues.

## Idée générale

Compléter la probabilité du cours de [[Probability (matière)]] avec ce qu'il faut pour l'inférence : combinaisons linéaires, échantillons iid, [[Théorème central limite]], diagrammes de probabilité, simulation par la fonction de répartition inverse, fonction génératrice des moments et deux lois d'appoint (Weibull, log-normale).

## Contenu, dans l'ordre du cours

- **Combinaisons linéaires** : $Y = a_1X_1 + \dots + a_nX_n + b$ est une variable aléatoire. La moyenne empirique $\bar{X}$ prend $a_i = 1/n$, $b = 0$. Sans hypothèse d'indépendance, $E(Y) = \sum a_i\mu_i + b$ et $\mathrm{Var}(Y) = \sum_i\sum_j a_ia_j\mathrm{Cov}(X_i, X_j)$. Si les $X_i$ sont indépendantes, $\mathrm{Var}(Y) = \sum a_i^2\sigma_i^2$. Cas $n = 2$ : $\mathrm{SD}(X_1)^2 + \mathrm{SD}(X_2)^2 = \mathrm{SD}(X_1 + X_2)^2$ (« théorème de Pythagore »). Voir [[Covariance et corrélation]].
- **Espérance et variance d'une [[Loi binomiale]]** : $X = \sum X_i$ avec $X_i$ de Bernoulli indépendantes, $E(X_i) = p$, $\mathrm{Var}(X_i) = p(1-p)$, d'où $E(X) = np$ et $\mathrm{Var}(X) = np(1-p)$.
- **Somme de variables** : la moyenne et l'écart-type ne suffisent pas à fixer une loi. Si les variables sont indépendantes, la densité de la somme est la convolution des densités marginales.
- **Variables normales** : toute combinaison linéaire de variables normales indépendantes est normale. La note justifie : la convolution de lois normales est une densité normale.
- **iid** : variables indépendantes de même loi, c'est-à-dire un échantillon aléatoire simple. Si on tire sans remise, l'approximation est acceptée quand $n/N \le 0{,}05$.
- **Total et moyenne** : $T = \sum X_i$ et $\bar{X} = T/n$. $E(T) = n\mu$, $\mathrm{Var}(T) = n\sigma^2$, $E(\bar{X}) = \mu$, $\mathrm{Var}(\bar{X}) = \sigma^2/n$, $\mathrm{SD}(\bar{X}) = \sigma/\sqrt{n}$. Si les $X_i$ sont normales, $T$ et $\bar{X}$ le sont aussi.
- **Théorème central limite** : pour un échantillon d'une loi de moyenne $\mu$ et d'écart-type $\sigma$, $P\!\left(\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \le z\right) \to \Phi(z)$, et de même pour $(T - n\mu)/(\sqrt{n}\sigma)$. Pour $n$ grand, $T$ et $\bar{X}$ sont approximativement normales. Note de l'étudiant : le théorème vaut pour toute loi.
- **[[Diagramme de probabilité]]** : points $(x_{(i)}, y_i)$ où $x_{(i)}$ est la $i$-ème plus petite observation et $y_i$ le percentile $100(i - 0{,}5)/n$ de la loi de la population. Sur la droite $y = x$, l'échantillon suit cette loi. Diagramme de Weibull : on trace $x' = \ln x$ et $y' = \ln(-\ln(1-p))$ avec $p = (i - 0{,}5)/n$. Diagramme normal : des points proches d'une droite (pas forcément à 45°) rendent la normalité plausible. Écarts à la normalité : queues légères, queues lourdes, asymétrie.
- **Théorème de transformation** : voir [[Chp 5 - Continuous random variable (résumé)]]. $f_Y(y) = f_X(h(y))\,|h'(y)|$ pour $g$ strictement monotone d'inverse $h$.
- **[[Méthode de la fonction de répartition inverse]]** : si $U \sim \mathrm{Unif}[0, 1)$ et $X = F^{-1}(U)$, la densité de $X$ est $f$. Pour simuler, on tire $u$ puis on pose $x = F^{-1}(u)$.
- **Famille de puissances** : $Y = (X^p - 1)/p$ pour $p > 0$, $X > 0$ ; $Y = \ln X$ pour $p = 0$.
- **[[Fonction génératrice des moments]]** : $M_X(t) = E(e^{tX})$, dérivées $E(X^n)$ (en 0). Elle détermine la loi, $M_{X+Y} = M_XM_Y$ si indépendantes, et $M_Y(t) = e^{bt}\prod M_{X_i}(a_it)$ pour $Y = \sum a_iX_i + b$.
- **Annexe, Weibull** : $f(x; \alpha, \beta) = \frac{\alpha}{\beta^\alpha}x^{\alpha - 1}e^{-(x/\beta)^\alpha}$ pour $x > 0$, $\alpha$ paramètre de forme, $\beta$ paramètre d'échelle. $\alpha = 1$ donne l'exponentielle. Fonction de répartition $1 - e^{-(x/\beta)^\alpha}$.
- **Annexe, log-normale** : $X \ge 0$ est log-normale si $\ln X$ est normale de paramètres $\mu$, $\sigma$. $E(X) = e^{\mu + \sigma^2/2}$, $V(X) = e^{2\mu + \sigma^2}(e^{\sigma^2} - 1)$. $F(x) = \Phi\!\left(\frac{\ln x - \mu}{\sigma}\right)$. Les paramètres sont ceux de $\ln X$, pas de $X$.
- **Au-delà de la normalité** : paramètres de position et d'échelle si $F$ dépend de $(x - \theta_1)/\theta_2$ ; exemple de la loi des valeurs extrêmes, $F = 1 - e^{-e^{(x - \theta_1)/\theta_2}}$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Fonction génératrice, dérivées** : la note écrit $\frac{d^n}{dt^n}M_X(t) = E(X^n)$. Il faut évaluer en $t = 0$ : $M_X^{(n)}(0) = E(X^n)$, comme le dit le chapitre 5 de Probability (complément).
2. **$M_{aX+bY+x}$** : la note écrit $M_{aX+bY+x}(t) = M_X(at)M_Y(bt)e^{tc}$. Le « $x$ » est un $c$ mal écrit, et il faut $X$ et $Y$ indépendantes. La proposition de l'image, elle, est correcte (complément).
3. **Preuve de la normalité d'une combinaison** : « la convolution de lois normales est une densité normale » est affirmé, non démontré. La preuve par la fonction génératrice $M_X(t) = e^{\mu t + \sigma^2t^2/2}$ n'est pas dans la note (complément).
4. **Famille de puissances** : le cours donne $p > 0$ et $p = 0$ seulement. Le cas $p < 0$ n'y est pas, ni la raison d'être de la famille (stabiliser la variance, symétriser). Le wiki n'en dit pas plus.
5. **Binomiale** : la note finit par « Formule à rajouter chépa ou : E(x) = np, Var = np(1-p) » : note personnelle d'étudiant sur l'emplacement de la formule. Les formules sont justes.
6. **Légende du diagramme de probabilité** : l'image indique « (b) » deux fois, le troisième est « (c) ». Faute d'image, sans conséquence.
7. **Encadré coupé** : le texte bleu de la proposition sur $\bar{X}$ est coupé à gauche, mais le tableau de la proposition donne tout le contenu. Fausse alerte sur le fond.
8. **Fonction de répartition de Weibull** : le cas $x \le 0$ de la densité n'apparaît pas dans l'image. Convention usuelle : densité nulle. Non établi par le cours.
