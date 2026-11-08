---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Statistics/Chp3 : More on probability.docx|Chp3 - More on probability]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Statistics/Chp3 : More on probability.docx|Chp3 - More on probability]], dans [[Cours/Probabilités et statistiques/Statistics/_index|Statistics]]. Le chapitre complète la probabilité du cours de [[Cours/Probabilités et statistiques/Probability/_index|Probability]] avec ce qu'il faut pour l'inférence : combinaisons linéaires, échantillons iid, [[Théorème central limite]], diagrammes de probabilité, simulation par la fonction de répartition inverse, fonction génératrice des moments et deux lois d'appoint (Weibull, log-normale). Les images n'ont pas été ouvertes : seules leurs transcriptions ont été lues.

## Combinaisons linéaires de variables aléatoires

Pour **toute** famille de [[Variable aléatoire|variables aléatoires]] (*rv*) $X_1, \dots, X_n$ et des constantes $a_1, \dots, a_n, b \in \mathbb{R}$,
$$Y = a_1X_1 + \dots + a_nX_n + b$$
est une nouvelle variable aléatoire, avec sa propre loi, sa moyenne et son écart-type. Exemple : la [[Moyenne empirique|moyenne d'échantillon]] $\bar{X}$ s'obtient avec $a_1 = \dots = a_n = 1/n$ et $b = 0$.

### Théorème (variables quelconques)

Soient $X_1, \dots, X_n$ de moyennes $\mu_1, \dots, \mu_n$ et d'écarts-types $\sigma_1, \dots, \sigma_n$. **Indépendantes ou non** :
$$E(a_1X_1 + \dots + a_nX_n + b) = a_1\mu_1 + \dots + a_n\mu_n + b$$
$$\mathrm{Var}(a_1X_1 + \dots + a_nX_n + b) = \sum_{i=1}^{n}\sum_{j=1}^{n} a_ia_j\,\mathrm{Cov}(X_i, X_j) = \sum_{i=1}^{n} a_i^2\sigma_i^2 + 2\sum_{i<j} a_ia_j\,\mathrm{Cov}(X_i, X_j)$$
Voir [[Covariance et corrélation]] et [[Espérance et variance]].

La formule de la variance vient de la bilinéarité de la covariance : $\mathrm{Var}(Y) = \mathrm{Cov}(Y, Y)$, et en développant $\mathrm{Cov}\big(\sum_i a_iX_i + b,\ \sum_j a_jX_j + b\big)$ on obtient la double somme. La constante $b$ disparaît, car décaler une variable ne change pas sa dispersion ($\mathrm{Cov}(X, b) = 0$) ; les termes $i = j$ donnent $a_i^2\sigma_i^2$, puisque $\mathrm{Cov}(X_i, X_i) = \sigma_i^2$. [[Complément hors du cours|ⓘ]]

### Théorème (variables indépendantes)

Si $X_1, \dots, X_n$ sont [[Indépendance de variables aléatoires|indépendantes]] :
$$\mathrm{Var}(a_1X_1 + \dots + a_nX_n + b) = a_1^2\sigma_1^2 + \dots + a_n^2\sigma_n^2, \qquad \mathrm{SD}(\dots) = \sqrt{a_1^2\sigma_1^2 + \dots + a_n^2\sigma_n^2}$$

Ce cas découle du précédent : des variables indépendantes ont une covariance nulle, donc seuls les termes $i = j$ restent. La formule vaut d'ailleurs dès que les variables sont deux à deux non corrélées. La réciproque est fausse : une covariance nulle n'entraîne pas l'indépendance. Exemple classique : $X \sim \mathcal{N}(0, 1)$ et $Y = X^2$ ; $\mathrm{Cov}(X, Y) = E(X^3) - E(X)E(X^2) = 0$, alors que $Y$ dépend entièrement de $X$. [[Complément hors du cours|ⓘ]]

### Cas $n = 2$ (corollaire)

Pour deux variables quelconques et des constantes $a_1, a_2, b$ :
$$E(a_1X_1 + a_2X_2 + b) = a_1E(X_1) + a_2E(X_2) + b$$
$$\mathrm{Var}(a_1X_1 + a_2X_2 + b) = a_1^2\mathrm{Var}(X_1) + a_2^2\mathrm{Var}(X_2) + 2a_1a_2\mathrm{Cov}(X_1, X_2)$$

En particulier $E(X_1 \pm X_2) = E(X_1) \pm E(X_2)$, et si $X_1$, $X_2$ sont indépendantes, $\mathrm{Var}(X_1 + X_2) = \mathrm{Var}(X_1 - X_2) = \mathrm{Var}(X_1) + \mathrm{Var}(X_2)$.

Les variances s'ajoutent aussi pour une **différence**, car $\mathrm{Var}(-X_2) = (-1)^2\,\mathrm{Var}(X_2)$ : les soustraire est une erreur fréquente. Les écarts-types, eux, ne s'ajoutent pas : ce sont leurs carrés qui s'ajoutent. [[Complément hors du cours|ⓘ]]

Cette propriété s'écrit aussi $\mathrm{SD}(X_1)^2 + \mathrm{SD}(X_2)^2 = [\mathrm{SD}(X_1 + X_2)]^2$ ; à cause de la forme $a^2 + b^2 = c^2$, on l'appelle parfois le « [[Théorème de Pythagore]] » des statisticiens.

### Espérance et variance d'une loi binomiale

Une variable [[Loi binomiale|binomiale]] s'écrit $X = \sum_{i=1}^{n} X_i$, avec
$$X_i = \begin{cases} 1 & \text{si le } i\text{-ème essai est un succès} \\ 0 & \text{sinon} \end{cases}, \qquad b(x; n, p) = \begin{cases} \binom{n}{x} p^x (1-p)^{n-x} & x = 0, 1, \dots, n \\ 0 & \text{sinon} \end{cases}$$
Les $X_i$ sont indépendantes, avec $E(X_i) = p$ et $\mathrm{Var}(X_i) = p(1-p)$. D'où
$$E(X) = np, \qquad \mathrm{Var}(X) = np(1-p).$$

Calcul pour un essai : chaque $X_i$ suit une [[Loi binomiale|loi de Bernoulli]] de paramètre $p$ ([[Variable indicatrice]]). $E(X_i) = 1 \cdot p + 0 \cdot (1-p) = p$ ; comme $X_i^2 = X_i$, $E(X_i^2) = p$, donc $\mathrm{Var}(X_i) = E(X_i^2) - E(X_i)^2 = p - p^2 = p(1-p)$. Le théorème des variables indépendantes, avec $a_i = 1$ et $b = 0$, donne alors $E(X) = np$ et $\mathrm{Var}(X) = np(1-p)$. [[Complément hors du cours|ⓘ]]

## Loi d'une somme de variables aléatoires

- Connaître la moyenne et l'écart-type d'une variable $W$ ne suffit pas à fixer sa loi, donc à calculer $P(W > 10)$ ou $P(W \le -2)$.
- Pour des variables **indépendantes**, on peut déterminer la densité de la somme à partir des densités marginales.

**Théorème** : si $X$ et $Y$ sont indépendantes, continues, de densités marginales $f_X$ et $f_Y$, la densité de $W = X + Y$ est
$$f_W(w) = \int_{-\infty}^{\infty} f_X(x)\, f_Y(w - x)\, dx.$$
C'est la **convolution** de $f_X$ et $f_Y$, notée $f_W = f_X \star f_Y$. Les bornes d'intégration sont les $x$ pour lesquels $f_X(x) > 0$ et $f_Y(w - x) > 0$. Voir [[Loi conjointe]].

Exemple : $X$ et $Y$ indépendantes de [[Loi uniforme|loi uniforme]] sur $[0, 1]$. Il faut $0 \le x \le 1$ et $0 \le w - x \le 1$, soit $w - 1 \le x \le w$. Pour $0 \le w \le 1$, $f_W(w) = \int_0^w dx = w$ ; pour $1 \le w \le 2$, $f_W(w) = \int_{w-1}^1 dx = 2 - w$. La somme suit une loi **triangulaire** sur $[0, 2]$ : la somme de deux uniformes n'est pas uniforme, les valeurs centrales sont les plus probables, comme pour la somme de deux dés. [[Complément hors du cours|ⓘ]]

### Cas des variables normales

Si $X_1, \dots, X_n$ sont indépendantes et de [[Loi normale|loi normale]] (moyennes et écarts-types éventuellement différents), toute [[Combinaison linéaire|combinaison linéaire]] $Y = a_1X_1 + \dots + a_nX_n + b$ est normale.

Preuve donnée : la loi d'une somme de variables indépendantes (discrètes ou continues) est la convolution des lois marginales ; pour des lois normales, cette convolution est une densité normale. Voir [[Stabilité des lois par somme]].

Ses paramètres découlent de la première section : $Y \sim \mathcal{N}\big(\sum a_i\mu_i + b,\ \sqrt{\sum a_i^2\sigma_i^2}\big)$, le second paramètre étant l'écart-type comme dans le cours. Exemple : $X_1 \sim \mathcal{N}(10, 3)$ et $X_2 \sim \mathcal{N}(8, 4)$ indépendantes ; $X_1 - X_2 \sim \mathcal{N}(2, 5)$, car $\sqrt{3^2 + 4^2} = 5$, donc $P(X_1 > X_2) = P(X_1 - X_2 > 0) = P(Z > -0{,}4) = \Phi(0{,}4) \approx 0{,}655$. [[Complément hors du cours|ⓘ]]

## Variables indépendantes et identiquement distribuées

**Définition** : $X_1, \dots, X_n$ sont **iid** (*independent and identically distributed*) si

1. les $X_i$ sont indépendantes ;
2. toutes les $X_i$ ont la même loi.

Une telle famille s'appelle aussi un **échantillon aléatoire (simple)** de taille $n$ ([[Échantillonnage]]).

La notion imite le tirage aléatoire simple dans une population : $X_1$ est la valeur de la variable pour le premier individu tiré, $X_2$ pour le deuxième, etc. Avec un [[Tirage avec et sans remise|tirage avec remise]], ou dans une population (potentiellement) infinie, les conditions 1 et 2 sont exactement vérifiées. Sans remise, elles le sont approximativement si $n$ est bien plus petit que $N$ : en pratique, si $n/N \le 0{,}05$ (au plus 5 % de la population), on fait comme si les $X_i$ formaient un échantillon aléatoire.

Le seuil de 5 % s'explique par le facteur de correction pour population finie $\sqrt{(N-n)/(N-1)}$ de [[4 - Inferential statistics 1]] : pour $n/N \le 0{,}05$, il vaut au moins $\sqrt{0{,}95} \approx 0{,}975$, si bien que les formules de population infinie surestiment l'écart-type de moins de 3 %. [[Complément hors du cours|ⓘ]]

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

Calcul, avec le théorème des variables indépendantes : $a_i = 1$ pour $T$, $a_i = 1/n$ pour $\bar{X}$. Ainsi $E(\bar{X}) = n \cdot \frac{1}{n}\mu = \mu$ et $\mathrm{Var}(\bar{X}) = n \cdot \frac{1}{n^2}\sigma^2 = \sigma^2/n$. L'écart-type de la moyenne ne décroît qu'en $1/\sqrt{n}$ : pour diviser l'incertitude par 2, il faut quatre fois plus d'observations. [[Complément hors du cours|ⓘ]]

## Théorème central limite

**Théorème** ([[Théorème central limite]]) : soit $X_1, \dots, X_n$ un échantillon aléatoire d'une loi de moyenne $\mu$ et d'écart-type $\sigma$. Quand $n \to \infty$, les versions centrées réduites de $T$ et $\bar{X}$ suivent la loi normale centrée réduite :
$$\lim_{n\to\infty} P\left(\frac{T - n\mu}{\sqrt{n}\,\sigma} \le z\right) = \Phi(z), \qquad \lim_{n\to\infty} P\left(\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \le z\right) = \Phi(z)$$
où $Z$ est normale centrée réduite. On dit que $T$ et $\bar{X}$ sont **asymptotiquement normales** : pour $n$ assez grand, $T$ suit approximativement $\mathcal{N}(n\mu, \sqrt{n}\,\sigma)$ et $\bar{X}$ suit approximativement $\mathcal{N}(\mu, \sigma/\sqrt{n})$.

Note de l'étudiante : aucune hypothèse sur la loi, le théorème vaut pour toute loi (de moyenne et d'écart-type finis).

En pratique, l'approximation est jugée bonne pour $n > 30$ ; il en faut moins si la population est déjà proche d'une loi normale, davantage si elle est très asymétrique. Si la population est normale, $\bar{X}$ est exactement normale pour tout $n$ (section précédente). [[Complément hors du cours|ⓘ]]

Exemple : population de moyenne $\mu = 50$ et d'écart-type $\sigma = 12$, échantillon de taille $n = 36$. $\bar{X}$ suit approximativement $\mathcal{N}(50, 2)$, car $12/\sqrt{36} = 2$, donc $P(\bar{X} > 53) \approx P(Z > 1{,}5) = 1 - \Phi(1{,}5) \approx 0{,}067$. [[Complément hors du cours|ⓘ]]

Le TCL explique la place de la loi normale en statistique : une grandeur qui résulte de l'addition de nombreux petits effets indépendants (les erreurs de mesure, par exemple) est approximativement normale. Il complète la [[Loi des grands nombres]] : celle-ci dit que $\bar{X}$ se rapproche de $\mu$, le TCL décrit la forme de ses fluctuations autour de $\mu$, d'ordre $\sigma/\sqrt{n}$. [[Complément hors du cours|ⓘ]]

## Compléments du chapitre

### Diagramme de probabilité classique

([[Diagramme de probabilité]])

Points $(x, y)$ avec :

- $x$ : la $i$-ème plus petite **observation de l'échantillon** ;
- $y$ : le percentile $100(i - 0{,}5)/n$ de la **loi de la population** ([[Quantile]]).

Si le graphe a la forme $y = x$, les observations ont la même loi que la population.

Pourquoi $(i - 0{,}5)/n$ : chaque observation représente une part $1/n$ de l'échantillon, et la $i$-ème plus petite en occupe le milieu de la sienne, soit une proportion $(i - 0{,}5)/n$ des données en dessous. On évite ainsi les proportions 0 et 1, dont les percentiles seraient infinis pour une loi normale. [[Complément hors du cours|ⓘ]]

![[Chp3 - More on probability - image14.png]]

*Figure : diagramme quantile-quantile : dix points (valeur observée, percentile $z$) autour de la droite à 45°.*

### Diagramme de probabilité de Weibull

Même structure : ($i$-ème plus petite observation, percentile $[100(i - 0{,}5)/n]$ de la loi de la population), mais on trace
$$x' = \ln(x), \qquad y' = \ln(-\ln(1 - p)), \quad p = \frac{i - 0{,}5}{n},$$
avec $n$ la taille de l'échantillon.

Ce changement de variables rend la courbe linéaire. De $F(x) = 1 - e^{-(x/\beta)^\alpha}$ on tire $-\ln(1 - F(x)) = (x/\beta)^\alpha$, puis $\ln(-\ln(1 - F(x))) = \alpha\ln(x) - \alpha\ln(\beta)$. Si les données suivent une loi de Weibull, les points $(x', y')$ s'alignent donc sur une droite de pente $\alpha$ et d'ordonnée à l'origine $-\alpha\ln\beta$, ce qui donne aussi une estimation graphique des deux paramètres. [[Complément hors du cours|ⓘ]]

### Théorème de transformation

([[Théorème de transformation]])

Soit $X$ de densité $f_X$ et $Y = g(X)$, avec $g$ strictement monotone (croissante ou décroissante) sur l'ensemble des valeurs de $X$ ; elle a donc une réciproque $X = g^{-1}(Y) = h(Y)$. Si $h$ est dérivable :
$$f_Y(y) = f_X(h(y)) \cdot |h'(y)|$$

Idée de la preuve, pour $g$ croissante : $F_Y(y) = P(g(X) \le y) = P(X \le h(y)) = F_X(h(y))$, puis on dérive : $f_Y(y) = f_X(h(y))\,h'(y)$. Pour $g$ décroissante, l'inégalité s'inverse, $F_Y(y) = 1 - F_X(h(y))$, et la dérivée fait apparaître $-h'(y)$, positif : d'où la valeur absolue. [[Complément hors du cours|ⓘ]]

Exemple : $Y = aX + b$ avec $a \neq 0$ ; $h(y) = (y - b)/a$ et $h'(y) = 1/a$, donc $f_Y(y) = \frac{1}{|a|}\, f_X\!\left(\frac{y - b}{a}\right)$. Avec $X \sim \mathcal{N}(0, 1)$, on retrouve que $Y = \sigma X + \mu$ suit $\mathcal{N}(\mu, \sigma)$. [[Complément hors du cours|ⓘ]]

Voir aussi [[5 - Continuous random variable]].

### Simulation : méthode de la fonction de répartition inverse

**Théorème** : soit une loi continue de densité $f$ et de [[Fonction de répartition|fonction de répartition]] $F$, et $U \sim \mathrm{Unif}[0; 1)$. Alors $X = F^{-1}(U)$ a pour densité $f$.

Preuve, pour $F$ continue et strictement croissante : $P(X \le x) = P(F^{-1}(U) \le x) = P(U \le F(x)) = F(x)$, car $P(U \le u) = u$ pour une loi uniforme sur $[0; 1)$. $X$ a donc $F$ pour fonction de répartition. [[Complément hors du cours|ⓘ]]

**Méthode** ([[Méthode de la fonction de répartition inverse]], *inverse CDF method*) : pour obtenir $n$ valeurs d'une loi de densité $f$ et de fonction de répartition $F$, répéter $n$ fois :

1. tirer avec un générateur de nombres aléatoires (*RNG*) une valeur $u$ dans $[0; 1)$ ;
2. poser $x = F^{-1}(u)$.

Les valeurs $x_1, \dots, x_n$ simulent une variable de densité $f$.

Exemple : pour la [[Loi exponentielle|loi exponentielle]] de paramètre $\lambda$, $F(x) = 1 - e^{-\lambda x}$ ; en résolvant $u = 1 - e^{-\lambda x}$, on obtient $x = F^{-1}(u) = -\ln(1 - u)/\lambda$. Pour la loi normale, $F^{-1} = \Phi^{-1}$ n'a pas de formule explicite : on l'évalue numériquement, ou on emploie des méthodes de simulation dédiées. [[Complément hors du cours|ⓘ]]

![[Chp3 - More on probability - image17.png]]

*Figure : la méthode illustrée : sur la courbe de $F$, les valeurs $u_1$, $u_2$ de l'axe vertical renvoient à $F^{-1}(u_1)$, $F^{-1}(u_2)$ sur l'axe horizontal.*

### Famille de transformations puissance

([[Transformation puissance]])

$$Y = \frac{X^p - 1}{p} \ \text{ si } p > 0 \text{ et } X > 0, \qquad Y = \ln(X) \ \text{ si } p = 0 \text{ et } X > 0.$$

C'est la famille de **Box-Cox**. On l'emploie pour rapprocher d'une loi normale des données asymétriques à droite, ce que l'on contrôle avec un [[Diagramme de probabilité|diagramme de probabilité]], ou pour stabiliser leur variance. $p = 1$ ne fait que décaler les données, $p = 1/2$ revient à une racine carrée, $p = 0$ au logarithme : plus $p$ est petit, plus les grandes valeurs sont resserrées. Le cas $p = 0$ n'est pas arbitraire : $\lim_{p \to 0} (x^p - 1)/p = \ln x$, ce qui rend la famille continue en $p$. [[Complément hors du cours|ⓘ]]

### Fonction génératrice des moments

([[Fonction génératrice des moments]], *moment generating function*, mgf)

- Pour une variable continue $X$ : $M_X(t) = E(e^{tX})$.
- $\dfrac{d^n}{dt^n} M_X(t)\Big|_{t=0} = E(X^n)$. [[Erreurs du cours#^e-3-more-on-probability|✎]]

La définition vaut aussi pour une variable discrète : $M_X(t) = \sum_x e^{tx}\,p(x)$. Elle ne sert que si l'espérance est finie pour tous les $t$ d'un intervalle autour de 0 ; certaines lois n'ont pas de fonction génératrice des moments, comme la loi log-normale de l'annexe (espérance infinie pour tout $t > 0$). [[Complément hors du cours|ⓘ]]

Pourquoi la dérivée donne les moments : $e^{tX} = \sum_k t^kX^k/k!$, donc $M_X(t) = \sum_k E(X^k)\,t^k/k!$, et la $n$-ième dérivée en $t = 0$ ne garde que le terme $E(X^n)$. Par exemple $M_X'(0) = E(X)$ et $\mathrm{Var}(X) = M_X''(0) - M_X'(0)^2$. [[Complément hors du cours|ⓘ]]

**Propriétés** :

- $M_X$ détermine de façon unique la loi de $X$ ;
- si $X$ et $Y$ sont indépendantes, $M_{X+Y}(t) = M_X(t) \cdot M_Y(t)$ ;
- si $X$ et $Y$ sont indépendantes, $M_{aX+bY+c}(t) = M_X(at) \cdot M_Y(bt) \cdot e^{tc}$. [[Erreurs du cours#^e-3-more-on-probability|✎]]

Fonctions génératrices des lois usuelles : [[Complément hors du cours|ⓘ]]

| Loi | $M_X(t)$ |
|---|---|
| Bernoulli($p$) | $1 - p + pe^t$ |
| Binomiale($n$, $p$) | $(1 - p + pe^t)^n$ |
| Poisson($\mu$) | $e^{\mu(e^t - 1)}$ |
| Exponentielle($\lambda$) | $\dfrac{\lambda}{\lambda - t}$, pour $t < \lambda$ |
| Normale $\mathcal{N}(\mu, \sigma)$ | $e^{\mu t + \sigma^2t^2/2}$ |

**Proposition** : si les $X_i$ sont indépendantes et normales (moyennes et écarts-types différents), toute combinaison est normale :
$$a_1X_1 + \dots + a_nX_n + b \sim \mathcal{N}\big(E(a_1X_1 + \dots + b),\ \mathrm{SD}(a_1X_1 + \dots + b)\big)$$

**Proposition** : soient $X_1, \dots, X_n$ indépendantes de fonctions génératrices $M_{X_1}, \dots, M_{X_n}$. La fonction génératrice de $Y = a_1X_1 + \dots + a_nX_n + b$ est
$$M_Y(t) = e^{bt} \cdot M_{X_1}(a_1t) \cdot M_{X_2}(a_2t) \cdots M_{X_n}(a_nt).$$
Cas $a_i = 1$, $b = 0$ : $M_Y(t) = M_{X_1}(t) \cdots M_{X_n}(t)$. La fonction génératrice d'une somme de variables indépendantes est le **produit** des fonctions génératrices.

Application, preuve de la proposition sur les lois normales : pour $X_i \sim \mathcal{N}(\mu_i, \sigma_i)$ indépendantes, $M_Y(t) = e^{bt}\prod_i e^{\mu_ia_it + \sigma_i^2a_i^2t^2/2} = e^{(\sum a_i\mu_i + b)\,t + (\sum a_i^2\sigma_i^2)\,t^2/2}$. C'est la fonction génératrice d'une loi normale de moyenne $\sum a_i\mu_i + b$ et de variance $\sum a_i^2\sigma_i^2$, et l'unicité conclut. De même, le produit des $e^{\mu_i(e^t - 1)}$ montre qu'une somme de Poisson indépendantes est une Poisson de paramètre $\sum \mu_i$ ([[Stabilité des lois par somme]]). [[Complément hors du cours|ⓘ]]

## Annexe : deux lois

### Loi de Weibull

**Définition** : $X$ suit une loi de Weibull de paramètres $\alpha > 0$, $\beta > 0$ si sa densité est
$$f(x; \alpha, \beta) = \frac{\alpha}{\beta^\alpha}\, x^{\alpha - 1}\, e^{-(x/\beta)^\alpha}, \quad x > 0.$$

![[Chp3 - More on probability - image21.png]]

*Figure : densités de Weibull : à gauche $\alpha = 1, \beta = 1$ (exponentielle), $\alpha = 2, \beta = 1$, $\alpha = 2, \beta = 0{,}5$ ; à droite $\alpha = 10$ avec $\beta = 0{,}5$, $1$, $2$ (courbes en cloche de plus en plus larges).*

- $\beta$ est le [[Paramètre de position et d'échelle|paramètre d'échelle]] (*scale parameter*) ;
- $\alpha$ est le paramètre de forme (*shape parameter*) ;
- $\alpha = 1$ donne la [[Loi exponentielle]] ; fonction de répartition $F(x; \alpha, \beta) = 1 - e^{-(x/\beta)^\alpha}$.

Moments : $E(X) = \beta\,\Gamma(1 + 1/\alpha)$ et $V(X) = \beta^2\big[\Gamma(1 + 2/\alpha) - \Gamma(1 + 1/\alpha)^2\big]$, avec la [[Fonction Gamma|fonction gamma]] ; pour $\alpha = 1$, on retrouve $E(X) = \beta$, moyenne de l'exponentielle. [[Complément hors du cours|ⓘ]]

La [[Loi exponentielle|loi de Weibull]] sert surtout en fiabilité, pour la durée de vie d'un composant. Son **taux de défaillance** (*hazard rate*) $h(x) = \dfrac{f(x)}{1 - F(x)} = \dfrac{\alpha}{\beta^\alpha}\,x^{\alpha - 1}$ décroît si $\alpha < 1$ (défaillances de jeunesse), est constant si $\alpha = 1$ (loi exponentielle, sans mémoire : pannes accidentelles) et croît si $\alpha > 1$ (usure). [[Complément hors du cours|ⓘ]]

### Loi log-normale

**Définition** : une variable positive $X$ suit une loi log-normale si $Y = \ln(X)$ suit une loi normale. Si $\ln(X)$ est normale de paramètres $\mu$ et $\sigma$, la densité de $X$ est
$$f(x; \mu, \sigma) = \frac{1}{\sqrt{2\pi}\,\sigma x}\, e^{-[\ln(x) - \mu]^2/(2\sigma^2)}, \quad x > 0.$$

Attention : $\mu$ et $\sigma$ sont la moyenne et l'écart-type de $\ln(X)$, pas de $X$. On montre que
$$E(X) = e^{\mu + \sigma^2/2}, \qquad V(X) = e^{2\mu + \sigma^2}\,(e^{\sigma^2} - 1).$$

Pour $x > 0$, la fonction de répartition s'écrit avec $\Phi$ :
$$F(x; \mu, \sigma) = P[\ln X \le \ln x] = P\left[Z \le \frac{\ln(x) - \mu}{\sigma}\right] = \Phi\left[\frac{\ln(x) - \mu}{\sigma}\right].$$
En dérivant $F$ par rapport à $x$, on retrouve la densité.

La [[Loi normale|loi log-normale]] apparaît quand une grandeur positive est le **produit** de nombreux facteurs indépendants : son logarithme est alors une somme, approximativement normale par le [[Théorème central limite]]. Elle modélise des grandeurs positives très asymétriques à droite : revenus, tailles de particules, durées de réparation. Sa médiane vaut $e^\mu$, inférieure à sa moyenne $e^{\mu + \sigma^2/2}$. [[Complément hors du cours|ⓘ]]

## Cours de la feuille d'exercices 3 : diagramme de probabilité normal

**Définition** : le graphe des $n$ couples ($i$-ème plus petite observation, percentile $z$ d'ordre $[100(i - 0{,}5)/n]$) est un **diagramme de probabilité normal** (*normal probability plot*). Si l'échantillon vient d'une loi normale, les points sont proches d'une droite (pas forcément à 45°). Des points proches d'*une* droite rendent donc plausible l'hypothèse d'une population normale.

### Écarts à la normalité (*departures from normality*)

Une loi non normale entre souvent dans l'une de ces catégories :

1. symétrique, à **queues plus légères** que la normale (la densité décroît plus vite dans les queues) ;
2. symétrique, à **queues lourdes** ;
3. **asymétrique**.

![[Chp3 - More on probability - image5.png]]

*Figure : diagrammes de probabilité suggérant une loi non normale : (a) queues légères (S aplati au centre) ; (b) queues lourdes (S raide au centre) ; (c) asymétrie positive (courbe concave).*

Lecture : des queues lourdes donnent des observations extrêmes plus éloignées du centre que ne le prévoit la loi normale, donc des points qui s'écartent de la droite aux deux extrémités ; une asymétrie positive étire seulement la queue droite, d'où une courbure d'un seul côté. Sur un petit échantillon, même des données normales donnent des points assez irréguliers : ne conclure qu'à un écart net et systématique. [[Complément hors du cours|ⓘ]]

### Au-delà de la normalité

Soit une famille de lois à deux paramètres $\theta_1$, $\theta_2$, de fonction de répartition $F(x; \theta_1, \theta_2)$. Exemples :

- la famille normale : $\theta_1 = \mu$, $\theta_2 = \sigma$, $F(x; \mu, \sigma) = \Phi[(x - \mu)/\sigma]$ ;
- la famille de Weibull : $\theta_1 = \alpha$, $\theta_2 = \beta$, $F(x; \alpha, \beta) = 1 - e^{-(x/\beta)^\alpha}$ ;
- la famille gamma, dont la fonction de répartition est une intégrale de la fonction gamma incomplète, sans forme plus simple.

La [[Loi exponentielle|loi gamma]] de paramètres $\alpha > 0$ (forme) et $\beta > 0$ (échelle) a pour densité $f(x; \alpha, \beta) = \dfrac{x^{\alpha - 1}\,e^{-x/\beta}}{\beta^\alpha\,\Gamma(\alpha)}$ pour $x > 0$, avec la [[Fonction Gamma|fonction gamma]] $\Gamma$, et $E(X) = \alpha\beta$, $V(X) = \alpha\beta^2$. $\alpha = 1$ donne la loi exponentielle de moyenne $\beta$ ; la [[Loi du khi-deux|loi du χ²]] à $\nu$ degrés de liberté est la gamma de paramètres $\alpha = \nu/2$, $\beta = 2$. [[Complément hors du cours|ⓘ]]

$\theta_1$ et $\theta_2$ sont des paramètres de **position** et d'**échelle** si $F(x; \theta_1, \theta_2)$ est une fonction de $(x - \theta_1)/\theta_2$ ([[Paramètre de position et d'échelle]]). C'est le cas de $\mu$ et $\sigma$ pour la loi normale : changer $\mu$ décale la cloche, changer $\sigma$ étire ou comprime l'axe horizontal. Autre exemple :
$$F(x; \theta_1, \theta_2) = 1 - e^{-e^{(x - \theta_1)/\theta_2}}, \quad -\infty < x < \infty,$$
la [[Loi des valeurs extrêmes|loi des valeurs extrêmes]] (*extreme value distribution*), utilisée pour la durée de vie des composants et la résistance des matériaux.

C'est la loi de **Gumbel**, ici dans sa version pour les minimums. Elle est liée à la loi de Weibull : si $X$ suit une loi de Weibull de paramètres $\alpha$, $\beta$, alors $\ln X$ suit cette loi avec $\theta_1 = \ln\beta$ et $\theta_2 = 1/\alpha$, car $P(\ln X \le y) = 1 - e^{-(e^y/\beta)^\alpha} = 1 - e^{-e^{(y - \ln\beta)\alpha}}$. C'est pourquoi le diagramme de probabilité de Weibull passe par $\ln(x)$ : il ramène une famille sans paramètre de position à une famille de position et d'échelle. [[Complément hors du cours|ⓘ]]
