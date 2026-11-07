---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Statistics/Chp3 : More on probability.docx|Chp3 - More on probability]]"]
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 3/Statistics/Chp3 : More on probability.docx|Chp3 - More on probability]], dans [[Cours/Probabilités et statistiques/Statistics/_index|Statistics]]. Le chapitre complète la probabilité du cours de [[Cours/Probabilités et statistiques/Probability/_index|Probability]] avec ce qu'il faut pour l'inférence : combinaisons linéaires, échantillons iid, [[Théorème central limite]], diagrammes de probabilité, simulation par la fonction de répartition inverse, fonction génératrice des moments et deux lois d'appoint (Weibull, log-normale). En cas d'écart, le cours et ses images font foi. Les images n'ont pas été ouvertes : seules leurs transcriptions ont été lues.

## Combinaisons linéaires de variables aléatoires

Pour **toute** famille de [[Variable aléatoire|variables aléatoires]] (*rv*) $X_1, \dots, X_n$ et des constantes $a_1, \dots, a_n, b \in \mathbb{R}$,
$$Y = a_1X_1 + \dots + a_nX_n + b$$
est une nouvelle variable aléatoire, avec sa propre loi, sa moyenne et son écart-type. Exemple : la [[Moyenne empirique|moyenne d'échantillon]] $\bar{X}$ s'obtient avec $a_1 = \dots = a_n = 1/n$ et $b = 0$.

### Théorème (variables quelconques)

Soient $X_1, \dots, X_n$ de moyennes $\mu_1, \dots, \mu_n$ et d'écarts-types $\sigma_1, \dots, \sigma_n$. **Indépendantes ou non** :
$$E(a_1X_1 + \dots + a_nX_n + b) = a_1\mu_1 + \dots + a_n\mu_n + b$$
$$\mathrm{Var}(a_1X_1 + \dots + a_nX_n + b) = \sum_{i=1}^{n}\sum_{j=1}^{n} a_ia_j\,\mathrm{Cov}(X_i, X_j) = \sum_{i=1}^{n} a_i^2\sigma_i^2 + 2\sum_{i<j} a_ia_j\,\mathrm{Cov}(X_i, X_j)$$
Voir [[Covariance et corrélation]] et [[Espérance et variance]].

### Théorème (variables indépendantes)

Si $X_1, \dots, X_n$ sont [[Indépendance de variables aléatoires|indépendantes]] :
$$\mathrm{Var}(a_1X_1 + \dots + a_nX_n + b) = a_1^2\sigma_1^2 + \dots + a_n^2\sigma_n^2, \qquad \mathrm{SD}(\dots) = \sqrt{a_1^2\sigma_1^2 + \dots + a_n^2\sigma_n^2}$$

### Cas $n = 2$ (corollaire)

Pour deux variables quelconques et des constantes $a_1, a_2, b$ :
$$E(a_1X_1 + a_2X_2 + b) = a_1E(X_1) + a_2E(X_2) + b$$
$$\mathrm{Var}(a_1X_1 + a_2X_2 + b) = a_1^2\mathrm{Var}(X_1) + a_2^2\mathrm{Var}(X_2) + 2a_1a_2\mathrm{Cov}(X_1, X_2)$$

En particulier $E(X_1 \pm X_2) = E(X_1) \pm E(X_2)$, et si $X_1$, $X_2$ sont indépendantes, $\mathrm{Var}(X_1 + X_2) = \mathrm{Var}(X_1 - X_2) = \mathrm{Var}(X_1) + \mathrm{Var}(X_2)$.

Cette propriété s'écrit aussi $\mathrm{SD}(X_1)^2 + \mathrm{SD}(X_2)^2 = [\mathrm{SD}(X_1 + X_2)]^2$ ; à cause de la forme $a^2 + b^2 = c^2$, on l'appelle parfois le « [[Théorème de Pythagore]] » des statisticiens.

### Espérance et variance d'une loi binomiale

Une variable [[Loi binomiale|binomiale]] s'écrit $X = \sum_{i=1}^{n} X_i$, avec
$$X_i = \begin{cases} 1 & \text{si le } i\text{-ème essai est un succès} \\ 0 & \text{sinon} \end{cases}, \qquad b(x; n, p) = \begin{cases} \binom{n}{x} p^x (1-p)^{n-x} & x = 0, 1, \dots, n \\ 0 & \text{sinon} \end{cases}$$
Les $X_i$ sont indépendantes, avec $E(X_i) = p$ et $\mathrm{Var}(X_i) = p(1-p)$. D'où
$$E(X) = np, \qquad \mathrm{Var}(X) = np(1-p).$$

## Loi d'une somme de variables aléatoires

- Connaître la moyenne et l'écart-type d'une variable $W$ ne suffit pas à fixer sa loi, donc à calculer $P(W > 10)$ ou $P(W \le -2)$.
- Pour des variables **indépendantes**, on peut déterminer la densité de la somme à partir des densités marginales.

**Théorème** : si $X$ et $Y$ sont indépendantes, continues, de densités marginales $f_X$ et $f_Y$, la densité de $W = X + Y$ est
$$f_W(w) = \int_{-\infty}^{\infty} f_X(x)\, f_Y(w - x)\, dx.$$
C'est la **convolution** de $f_X$ et $f_Y$, notée $f_W = f_X \star f_Y$. Les bornes d'intégration sont les $x$ pour lesquels $f_X(x) > 0$ et $f_Y(w - x) > 0$. Voir [[Loi conjointe]].

### Cas des variables normales

Si $X_1, \dots, X_n$ sont indépendantes et de [[Loi normale|loi normale]] (moyennes et écarts-types éventuellement différents), toute [[Combinaison linéaire|combinaison linéaire]] $Y = a_1X_1 + \dots + a_nX_n + b$ est normale.

Preuve donnée : la loi d'une somme de variables indépendantes (discrètes ou continues) est la convolution des lois marginales ; pour des lois normales, cette convolution est une densité normale. Voir [[Stabilité des lois par somme]].

## Variables indépendantes et identiquement distribuées

**Définition** : $X_1, \dots, X_n$ sont **iid** (*independent and identically distributed*) si

1. les $X_i$ sont indépendantes ;
2. toutes les $X_i$ ont la même loi.

Une telle famille s'appelle aussi un **échantillon aléatoire (simple)** de taille $n$ ([[Échantillonnage]]).

La notion imite le tirage aléatoire simple dans une population : $X_1$ est la valeur de la variable pour le premier individu tiré, $X_2$ pour le deuxième, etc. Avec un [[Tirage avec et sans remise|tirage avec remise]], ou dans une population (potentiellement) infinie, les conditions 1 et 2 sont exactement vérifiées. Sans remise, elles le sont approximativement si $n$ est bien plus petit que $N$ : en pratique, si $n/N \le 0{,}05$ (au plus 5 % de la population), on fait comme si les $X_i$ formaient un échantillon aléatoire.

### Total et moyenne d'échantillon

$$T = X_1 + \dots + X_n = \sum_{i=1}^{n} X_i, \qquad \bar{X} = \frac{X_1 + \dots + X_n}{n} = \frac{T}{n}$$

**Proposition** : si $X_1, \dots, X_n$ sont iid de moyenne $\mu$ et d'écart-type $\sigma$ :

| Total $T$ | Moyenne $\bar{X}$ |
|---|---|
| $E(T) = n\mu$ | $E(\bar{X}) = \mu$ |
| $\mathrm{Var}(T) = n\sigma^2$, $\mathrm{SD}(T) = \sqrt{n}\,\sigma$ | $\mathrm{Var}(\bar{X}) = \sigma^2/n$, $\mathrm{SD}(\bar{X}) = \sigma/\sqrt{n}$ |
| Si les $X_i$ sont normales, $T$ est normale | Si les $X_i$ sont normales, $\bar{X}$ est normale |

![[Chp3 - More on probability - image25.png]]

*Figure : loi de la population et lois de $\bar{X}$ pour $n = 4$ et $n = 10$ : même centre, courbe d'autant plus étroite que $n$ est grand.*

Voir [[Distribution d'échantillonnage]].

## Théorème central limite

**Théorème** ([[Théorème central limite]]) : soit $X_1, \dots, X_n$ un échantillon aléatoire d'une loi de moyenne $\mu$ et d'écart-type $\sigma$. Quand $n \to \infty$, les versions centrées réduites de $T$ et $\bar{X}$ suivent la loi normale centrée réduite :
$$\lim_{n\to\infty} P\left(\frac{T - n\mu}{\sqrt{n}\,\sigma} \le z\right) = \Phi(z), \qquad \lim_{n\to\infty} P\left(\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \le z\right) = \Phi(z)$$
où $Z$ est normale centrée réduite. On dit que $T$ et $\bar{X}$ sont **asymptotiquement normales** : pour $n$ assez grand, $T$ suit approximativement $\mathcal{N}(n\mu, \sqrt{n}\,\sigma)$ et $\bar{X}$ suit approximativement $\mathcal{N}(\mu, \sigma/\sqrt{n})$.

Note de l'étudiante : aucune hypothèse sur la loi, le théorème vaut pour toute loi (de moyenne et d'écart-type finis).

## Compléments du chapitre

### Diagramme de probabilité classique

([[Diagramme de probabilité]])

Points $(x, y)$ avec :

- $x$ : la $i$-ème plus petite **observation de l'échantillon** ;
- $y$ : le percentile $100(i - 0{,}5)/n$ de la **loi de la population** ([[Quantile]]).

Si le graphe a la forme $y = x$, les observations ont la même loi que la population.

![[Chp3 - More on probability - image14.png]]

*Figure : diagramme quantile-quantile : dix points (valeur observée, percentile $z$) autour de la droite à 45°.*

### Diagramme de probabilité de Weibull

Même structure : ($i$-ème plus petite observation, percentile $[100(i - 0{,}5)/n]$ de la loi de la population), mais on trace
$$x' = \ln(x), \qquad y' = \ln(-\ln(1 - p)), \quad p = \frac{i - 0{,}5}{n},$$
avec $n$ la taille de l'échantillon.

### Théorème de transformation

([[Théorème de transformation]])

Soit $X$ de densité $f_X$ et $Y = g(X)$, avec $g$ strictement monotone (croissante ou décroissante) sur l'ensemble des valeurs de $X$ ; elle a donc une réciproque $X = g^{-1}(Y) = h(Y)$. Si $h$ est dérivable :
$$f_Y(y) = f_X(h(y)) \cdot |h'(y)|$$

Voir aussi [[5 - Continuous random variable]].

### Simulation : méthode de la fonction de répartition inverse

**Théorème** : soit une loi continue de densité $f$ et de [[Fonction de répartition|fonction de répartition]] $F$, et $U \sim \mathrm{Unif}[0; 1)$. Alors $X = F^{-1}(U)$ a pour densité $f$.

**Méthode** ([[Méthode de la fonction de répartition inverse]], *inverse CDF method*) : pour obtenir $n$ valeurs d'une loi de densité $f$ et de fonction de répartition $F$, répéter $n$ fois :

1. tirer avec un générateur de nombres aléatoires (*RNG*) une valeur $u$ dans $[0; 1)$ ;
2. poser $x = F^{-1}(u)$.

Les valeurs $x_1, \dots, x_n$ simulent une variable de densité $f$.

![[Chp3 - More on probability - image17.png]]

*Figure : la méthode illustrée : sur la courbe de $F$, les valeurs $u_1$, $u_2$ de l'axe vertical renvoient à $F^{-1}(u_1)$, $F^{-1}(u_2)$ sur l'axe horizontal.*

### Famille de transformations puissance

([[Transformation puissance]])

$$Y = \frac{X^p - 1}{p} \ \text{ si } p > 0 \text{ et } X > 0, \qquad Y = \ln(X) \ \text{ si } p = 0 \text{ et } X > 0.$$

### Fonction génératrice des moments

([[Fonction génératrice des moments]], *moment generating function*, mgf)

- Pour une variable continue $X$ : $M_X(t) = E(e^{tX})$.
- $\dfrac{d^n}{dt^n} M_X(t)\Big|_{t=0} = E(X^n)$ (la note omet « en $t = 0$ », voir « Erreurs du cours »).

**Propriétés** :

- $M_X$ détermine de façon unique la loi de $X$ ;
- si $X$ et $Y$ sont indépendantes, $M_{X+Y}(t) = M_X(t) \cdot M_Y(t)$ ;
- $M_{aX+bY+c}(t) = M_X(at) \cdot M_Y(bt) \cdot e^{tc}$ (la note écrit $M_{aX+bY+x}$, voir « Erreurs du cours »).

**Proposition** : si les $X_i$ sont indépendantes et normales (moyennes et écarts-types différents), toute combinaison est normale :
$$a_1X_1 + \dots + a_nX_n + b \sim \mathcal{N}\big(E(a_1X_1 + \dots + b),\ \mathrm{SD}(a_1X_1 + \dots + b)\big)$$

**Proposition** : soient $X_1, \dots, X_n$ indépendantes de fonctions génératrices $M_{X_1}, \dots, M_{X_n}$. La fonction génératrice de $Y = a_1X_1 + \dots + a_nX_n + b$ est
$$M_Y(t) = e^{bt} \cdot M_{X_1}(a_1t) \cdot M_{X_2}(a_2t) \cdots M_{X_n}(a_nt).$$
Cas $a_i = 1$, $b = 0$ : $M_Y(t) = M_{X_1}(t) \cdots M_{X_n}(t)$. La fonction génératrice d'une somme de variables indépendantes est le **produit** des fonctions génératrices.

## Annexe : deux lois

### Loi de Weibull

**Définition** : $X$ suit une loi de Weibull de paramètres $\alpha > 0$, $\beta > 0$ si sa densité est
$$f(x; \alpha, \beta) = \frac{\alpha}{\beta^\alpha}\, x^{\alpha - 1}\, e^{-(x/\beta)^\alpha}, \quad x > 0.$$

![[Chp3 - More on probability - image21.png]]

*Figure : densités de Weibull : à gauche $\alpha = 1, \beta = 1$ (exponentielle), $\alpha = 2, \beta = 1$, $\alpha = 2, \beta = 0{,}5$ ; à droite $\alpha = 10$ avec $\beta = 0{,}5$, $1$, $2$ (courbes en cloche de plus en plus larges).*

- $\beta$ est le [[Paramètre de position et d'échelle|paramètre d'échelle]] (*scale parameter*) ;
- $\alpha$ est le paramètre de forme (*shape parameter*) ;
- $\alpha = 1$ donne la [[Loi exponentielle]] ; fonction de répartition $F(x; \alpha, \beta) = 1 - e^{-(x/\beta)^\alpha}$.

### Loi log-normale

**Définition** : une variable positive $X$ suit une loi log-normale si $Y = \ln(X)$ suit une loi normale. Si $\ln(X)$ est normale de paramètres $\mu$ et $\sigma$, la densité de $X$ est
$$f(x; \mu, \sigma) = \frac{1}{\sqrt{2\pi}\,\sigma x}\, e^{-[\ln(x) - \mu]^2/(2\sigma^2)}, \quad x > 0.$$

Attention : $\mu$ et $\sigma$ sont la moyenne et l'écart-type de $\ln(X)$, pas de $X$. On montre que
$$E(X) = e^{\mu + \sigma^2/2}, \qquad V(X) = e^{2\mu + \sigma^2}\,(e^{\sigma^2} - 1).$$

Pour $x > 0$, la fonction de répartition s'écrit avec $\Phi$ :
$$F(x; \mu, \sigma) = P[\ln X \le \ln x] = P\left[Z \le \frac{\ln(x) - \mu}{\sigma}\right] = \Phi\left[\frac{\ln(x) - \mu}{\sigma}\right].$$
En dérivant $F$ par rapport à $x$, on retrouve la densité.

## Cours de la feuille d'exercices 3 : diagramme de probabilité normal

**Définition** : le graphe des $n$ couples ($i$-ème plus petite observation, percentile $z$ d'ordre $[100(i - 0{,}5)/n]$) est un **diagramme de probabilité normal** (*normal probability plot*). Si l'échantillon vient d'une loi normale, les points sont proches d'une droite (pas forcément à 45°). Des points proches d'*une* droite rendent donc plausible l'hypothèse d'une population normale.

### Écarts à la normalité (*departures from normality*)

Une loi non normale entre souvent dans l'une de ces catégories :

1. symétrique, à **queues plus légères** que la normale (la densité décroît plus vite dans les queues) ;
2. symétrique, à **queues lourdes** ;
3. **asymétrique**.

![[Chp3 - More on probability - image5.png]]

*Figure : diagrammes de probabilité suggérant une loi non normale : (a) queues légères (S aplati au centre) ; (b) queues lourdes (S raide au centre) ; (c) asymétrie positive (courbe concave).*

### Au-delà de la normalité

Soit une famille de lois à deux paramètres $\theta_1$, $\theta_2$, de fonction de répartition $F(x; \theta_1, \theta_2)$. Exemples :

- la famille normale : $\theta_1 = \mu$, $\theta_2 = \sigma$, $F(x; \mu, \sigma) = \Phi[(x - \mu)/\sigma]$ ;
- la famille de Weibull : $\theta_1 = \alpha$, $\theta_2 = \beta$, $F(x; \alpha, \beta) = 1 - e^{-(x/\beta)^\alpha}$ ;
- la famille gamma, dont la fonction de répartition est une intégrale de la fonction gamma incomplète, sans forme plus simple.

$\theta_1$ et $\theta_2$ sont des paramètres de **position** et d'**échelle** si $F(x; \theta_1, \theta_2)$ est une fonction de $(x - \theta_1)/\theta_2$ ([[Paramètre de position et d'échelle]]). C'est le cas de $\mu$ et $\sigma$ pour la loi normale : changer $\mu$ décale la cloche, changer $\sigma$ étire ou comprime l'axe horizontal. Autre exemple :
$$F(x; \theta_1, \theta_2) = 1 - e^{-e^{(x - \theta_1)/\theta_2}}, \quad -\infty < x < \infty,$$
la [[Loi des valeurs extrêmes|loi des valeurs extrêmes]] (*extreme value distribution*), utilisée pour la durée de vie des composants et la résistance des matériaux.

## Erreurs du cours

- [[Raw/Year 3/Statistics/Chp3 : More on probability.docx|Chp3 - More on probability]] écrit « dⁿ/dtⁿ M_X(t) = E(Xⁿ) » ; il faut évaluer en $t = 0$ : $M_X^{(n)}(0) = E(X^n)$.
- [[Raw/Year 3/Statistics/Chp3 : More on probability.docx|Chp3 - More on probability]] écrit « M_{aX+bY+x}(t) = M_X(at) x M_y(bt) x e^{tc} » ; il faut $M_{aX+bY+c}(t) = M_X(at)\,M_Y(bt)\,e^{tc}$, pour $X$ et $Y$ indépendantes, comme dans la proposition de l'image qui suit.
