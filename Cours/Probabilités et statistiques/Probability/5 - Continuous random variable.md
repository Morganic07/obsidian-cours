---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Probability/Chp 5 : Continuous random variable.docx|Chp 5 - Continuous random variable]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Probability/Chp 5 : Continuous random variable.docx|Chp 5 - Continuous random variable]], dans [[Cours/Probabilités et statistiques/Probability/_index|Probability]]. Les énoncés donnés en images sont recopiés ; les images qui portent une courbe ou un schéma sont intégrées à côté de leur énoncé. Les passages ajoutés finissent par ⓘ.

## Idée générale

Reprendre le chapitre 4 pour les variables continues : les sommes deviennent des [[Intégrale|intégrales]] et la loi est une densité. Le chapitre présente aussi les lois uniforme, normale et exponentielle, la fonction génératrice des moments et le changement de variable.

## Densité de probabilité (*probability density function*, PDF)

À distinguer de la fonction de masse (*[[Variable aléatoire|probability mass function]]*), réservée aux variables discrètes.

**Définition.** Soit $X$ une variable aléatoire continue. Une **loi de probabilité** ou **densité** (*pdf*) de $X$ est une fonction $f(x)$ telle que, pour tous $a \le b$ :
$$P(a \le X \le b) = \int_a^b f(x)\,dx$$

Pour que $f$ soit une densité légitime, il faut :
1. $f(x) \ge 0$ pour tout $x$ ;
2. $\displaystyle\int_{-\infty}^{\infty} f(x)\,dx = [\text{aire sous tout le graphe de } f] = 1$.

Une probabilité est donc une **aire** sous la courbe de $f$, et $f(x)$ elle-même n'est pas une probabilité : c'est une probabilité **par unité de longueur**, qui peut dépasser 1 (la densité de $\mathrm{Unif}[0;\, 0{,}5]$ vaut 2). Pour un petit $\Delta x$, $P(x \le X \le x + \Delta x) \approx f(x)\,\Delta x$ : là où $f$ est grande, $X$ tombe plus souvent. [[Complément hors du cours|ⓘ]]

## Loi uniforme (*uniform distribution*)

**Définition.** Une variable continue $X$ suit une **[[Loi uniforme|loi uniforme]]** sur $[A, B]$ si sa densité est
$$f(x; A, B) = \begin{cases} \dfrac{1}{B - A} & A \le x \le B \\ 0 & \text{sinon} \end{cases}$$
On note $X \sim \mathrm{Unif}[A, B]$.

La densité est constante : la probabilité de tomber dans un sous-intervalle de $[A, B]$ ne dépend que de sa longueur, $P(c \le X \le d) = \frac{d - c}{B - A}$ pour $A \le c \le d \le B$. Avec les formules de la suite du chapitre, on obtient : [[Complément hors du cours|ⓘ]]
$$F(x) = \frac{x - A}{B - A} \text{ pour } A \le x \le B \ (0 \text{ avant}, 1 \text{ après}), \qquad E(X) = \frac{A + B}{2}, \qquad \mathrm{Var}(X) = \frac{(B - A)^2}{12}$$
Par exemple, $E(X) = \int_A^B \frac{x}{B - A}\,dx = \frac{B^2 - A^2}{2(B - A)} = \frac{A + B}{2}$, le milieu de l'intervalle. Exemple : un bus passe toutes les 10 minutes et l'on arrive à un instant quelconque ; l'attente suit $\mathrm{Unif}[0, 10]$, dure 5 minutes en moyenne, et dépasse 7 minutes avec probabilité $3/10$. [[Complément hors du cours|ⓘ]]

## La probabilité d'un point est nulle

Pour une variable continue, la probabilité de prendre exactement une valeur est nulle :
$$P(X = c) = P(c \le X \le c) = \int_c^c f(x)\,dx = 0$$
Conséquence : inclure ou exclure les bornes de l'intégrale ne change rien :
$$P(a \le X \le b) = P(a < X < b) = P(a < X \le b) = P(a \le X < b)$$

## Fonction de répartition d'une variable continue (CDF)

**Définition.** La **[[Fonction de répartition|fonction de répartition]]** (*cumulative distribution function*) d'une variable continue $X$ est définie pour tout $x$ par :
$$F(x) = P(X \le x) = \int_{-\infty}^{x} f(y)\,dy$$

![[Chp 5 - Continuous random variable - image14.png]]
*Figure : exemple — une densité nulle hors de $[6, 10]$ (maximum ≈ 0,5 vers 8,6), l'aire grisée de 6 à 8 vaut $F(8)$ ; à droite, la cdf associée croît de 0 à 1, avec $F(8) \approx 0{,}3$.*

## De la PDF à la CDF

La CDF est une **[[Primitive|primitive]]** de la PDF.

**Proposition.** Soit $X$ continue de densité $f$ et de cdf $F$. Pour tout $a$ :
$$P(X > a) = 1 - F(a)$$
et pour tous $a < b$ :
$$P(a \le X \le b) = F(b) - F(a)$$

**Proposition.** Si $X$ est continue de densité $f$ et de cdf $F$, alors en tout $x$ où la dérivée $F'(x)$ existe, $F'(x) = f(x)$.

## Espérance et variance d'une variable continue

**Définition.** L'**espérance** (*[[Espérance et variance|expected value]]*, *mean value*) de $X$ continue de densité $f$ est
$$\mu = \mu_X = E(X) = \int_{-\infty}^{\infty} x \cdot f(x)\,dx$$

**Proposition.** Pour toute fonction $h(X)$ :
$$\mu_{h(X)} = E[h(X)] = \int_{-\infty}^{\infty} h(x) \cdot f(x)\,dx$$

**Définition.** La **variance** de $X$ continue, de densité $f$ et de moyenne $\mu$, est
$$\sigma_X^2 = \mathrm{Var}(X) = \int_{-\infty}^{\infty} (x - \mu)^2 \cdot f(x)\,dx = E\left[(X - \mu)^2\right]$$
et l'**écart-type** (*standard deviation*) est $\sigma_X = \mathrm{SD}(X) = \sqrt{\mathrm{Var}(X)}$.

**Proposition.** Soit $X$ continue, de densité $f$, de moyenne $\mu$ et d'écart-type $\sigma$.
1. **Formule raccourcie** (*variance shortcut*) :
$$\mathrm{Var}(X) = E(X^2) - \mu^2 = \int_{-\infty}^{\infty} x^2 f(x)\,dx - \left(\int_{-\infty}^{\infty} x f(x)\,dx\right)^2$$
2. **Inégalité de Tchebychev** (*Chebyshev's inequality*) : pour toute constante $k \ge 1$,
$$P(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}$$
   Elle vaut pour **toute** loi ayant une variance, discrète ou continue : quelle que soit la loi, au plus 25 % des valeurs s'écartent de la moyenne de 2 écarts-types ou plus ($k = 2$), au plus 11 % de 3 écarts-types. La borne est grossière (pour une loi normale, ces proportions sont d'environ 5 % et 0,3 %, voir la règle 68-95-99,7 plus bas), mais elle ne suppose rien sur la forme de la loi. Elle découle de l'**inégalité de Markov**, $P(Y \ge a) \le E(Y)/a$ pour $Y \ge 0$ et $a > 0$, appliquée à $Y = (X - \mu)^2$ et $a = k^2\sigma^2$. Elle sert à démontrer la [[Loi des grands nombres|loi faible des grands nombres]]. [[Complément hors du cours|ⓘ]]
3. **Linéarité de l'espérance** : pour toutes fonctions $h_1, h_2$ et constantes $a_1, a_2, b$,
$$E[a_1 h_1(X) + a_2 h_2(X) + b] = a_1 E[h_1(X)] + a_2 E[h_2(X)] + b$$
4. **Changement d'échelle** (*rescaling*) : pour toutes constantes $a, b$,
$$E(aX + b) = a\mu + b, \qquad \mathrm{Var}(aX + b) = a^2\sigma^2, \qquad \sigma_{aX+b} = |a|\sigma$$

## Fonction génératrice des moments (*moment generating function*, MGF)

**Définition.** La **[[Fonction génératrice des moments|fonction génératrice des moments]]** (mgf) d'une variable continue $X$ est
$$M_X(t) = E(e^{tX}) = \int_{-\infty}^{\infty} e^{tx} f(x)\,dx$$
Comme dans le cas discret, elle existe si et seulement si $M_X(t)$ est définie sur un intervalle qui contient 0 ainsi que des valeurs positives et négatives de $t$.

En $t = 0$, elle vaut toujours 1 :
$$M_X(0) = E(e^{0X}) = \int_{-\infty}^{\infty} e^{0x} f(x)\,dx = \int_{-\infty}^{\infty} f(x)\,dx = 1$$

- **Unicité** : deux lois ont la même densité si et seulement si elles ont la même mgf, à condition qu'elle existe.
- **Moments** : le moment d'ordre $r$ est $E(X^r) = M_X^{(r)}(0)$.

| Élément | Rôle |
|---|---|
| $M_X(t) = E[e^{tX}]$ | La définition |
| $M_X(0) = 1$ | Toujours vrai |
| $M_X^{(1)}(0) = E[X]$ | L'espérance |
| $M_X^{(2)}(0) = E[X^2]$ | Le second moment |
| … | Moments d'ordre supérieur |

Pourquoi les dérivées donnent les moments : en dérivant sous l'intégrale, $M_X'(t) = \int x\,e^{tx}f(x)\,dx = E(Xe^{tX})$, qui vaut $E(X)$ en $t = 0$ ; de même $M_X^{(r)}(t) = E(X^r e^{tX})$. Autrement dit, $M_X(t) = \sum_{r \ge 0} E(X^r)\,\frac{t^r}{r!}$ : les moments sont les coefficients du [[Développement limité|développement]] de $M_X$ en 0, d'où le nom. On en tire la variance : $\mathrm{Var}(X) = M_X''(0) - M_X'(0)^2$. [[Complément hors du cours|ⓘ]]

Exemple (loi exponentielle, définie plus bas) : pour $t < \lambda$, $M_X(t) = \int_0^\infty e^{tx}\lambda e^{-\lambda x}\,dx = \frac{\lambda}{\lambda - t}$. Alors $M_X'(t) = \frac{\lambda}{(\lambda - t)^2}$ et $M_X''(t) = \frac{2\lambda}{(\lambda - t)^3}$, d'où $E(X) = 1/\lambda$, $E(X^2) = 2/\lambda^2$ et $\mathrm{Var}(X) = 1/\lambda^2$. Pour la loi normale $N(\mu, \sigma)$, $M_X(t) = e^{\mu t + \sigma^2t^2/2}$ pour tout $t$. [[Complément hors du cours|ⓘ]]

## Loi gaussienne ou normale (*Gaussian, normal distribution*)

**Définition.** Une variable continue $X$ suit une **[[Loi normale|loi normale]]** (ou gaussienne) de paramètres $\mu$ et $\sigma$, avec $-\infty < \mu < \infty$ et $\sigma > 0$, si sa densité est
$$f(x; \mu, \sigma) = \frac{1}{\sigma\sqrt{2\pi}}\, e^{-(x - \mu)^2/(2\sigma^2)}, \qquad -\infty < x < \infty \quad (3.3)$$
On abrège : $X \sim N(\mu, \sigma)$.

Les paramètres sont l'espérance et l'écart-type : $E(X) = \mu$ et $\mathrm{Var}(X) = \sigma^2$. La courbe est une cloche symétrique autour de $\mu$, qui est aussi la médiane et le mode, avec des points d'inflexion en $\mu \pm \sigma$. Attention aux notations : cette section note $N(\mu, \sigma)$ (écart-type en second paramètre), mais la règle 9.8 ci-dessous et beaucoup de manuels écrivent $\mathcal{N}(\mu, \sigma^2)$ (variance en second paramètre) ; $N(0, 4)$ n'a donc pas le même sens selon la convention. Le rôle central de cette loi vient du [[Théorème central limite]] : une somme de nombreux petits effets indépendants est approximativement normale. [[Complément hors du cours|ⓘ]]

![[Chp 5 - Continuous random variable - image1.png]]
*Figure : définition et trois courbes de densité normale (*normal density curves*), graduées en $\mu$ et $\mu + \sigma$ — plus $\sigma$ est grand, plus la cloche est large et basse.*

**Règle 9.8 (règle 68-95-99,7 ou des trois sigmas).** Si $X \sim \mathcal{N}(\mu, \sigma^2)$ :
$$P(|X - \mu| < \sigma) \approx 68\,\%, \qquad P(|X - \mu| < 2\sigma) \approx 95\,\%, \qquad P(|X - \mu| < 3\sigma) \approx 99{,}73\,\%$$

## Loi normale centrée réduite (*standard normal distribution*)

**Définition.** La loi normale de paramètres $\mu = 0$ et $\sigma = 1$ est la **loi normale centrée réduite**. Une variable qui la suit est notée $Z$, de densité
$$f(z; 0, 1) = \frac{1}{\sqrt{2\pi}}\, e^{-z^2/2}, \qquad -\infty < z < \infty$$
Sa cdf est notée $\Phi$ :
$$\Phi(z) = P(Z \le z) = \int_{-\infty}^{z} \frac{1}{\sqrt{2\pi}}\, e^{-y^2/2}\,dy$$

Cette intégrale n'a pas d'expression à l'aide des fonctions usuelles, d'où l'usage d'une table (ou d'un logiciel). Les tables ne donnent souvent que $z \ge 0$ : la symétrie de la courbe donne $\Phi(-z) = 1 - \Phi(z)$, donc $\Phi(0) = 0{,}5$ et $P(|Z| \le z) = 2\Phi(z) - 1$. Valeurs à connaître : $\Phi(1{,}645) \approx 0{,}95$, $\Phi(1{,}96) \approx 0{,}975$, $\Phi(2{,}576) \approx 0{,}995$, qui servent aux [[Intervalle de confiance|intervalles de confiance]] à 90, 95 et 99 %. [[Complément hors du cours|ⓘ]]

![[Chp 5 - Continuous random variable - image6.png]]
*Figure : courbe normale centrée réduite (*standard normal (z) curve*) ; l'aire grisée à gauche de $z$ vaut $\Phi(z)$.*

## Passer d'une loi normale quelconque à la loi centrée réduite

**Proposition.** Si $X \sim N(\mu, \sigma)$, la variable **centrée réduite** (*standardized*)
$$Z = \frac{X - \mu}{\sigma}$$
suit la loi normale centrée réduite (voir [[Centrage et réduction]]). Donc :
$$P(a \le X \le b) = P\left(\frac{a - \mu}{\sigma} \le Z \le \frac{b - \mu}{\sigma}\right) = \Phi\left(\frac{b - \mu}{\sigma}\right) - \Phi\left(\frac{a - \mu}{\sigma}\right)$$
$$P(X \le a) = \Phi\left(\frac{a - \mu}{\sigma}\right), \qquad P(X \ge b) = 1 - \Phi\left(\frac{b - \mu}{\sigma}\right)$$
Réciproquement, si $Z \sim N(0, 1)$ et $\sigma > 0$, la variable « dé-réduite » $X = \mu + \sigma Z$ suit une loi normale de moyenne $\mu$ et d'écart-type $\sigma$.

![[Chp 5 - Continuous random variable - image24.png]]
*Figure : l'aire sous $N(\mu, \sigma)$ jusqu'à $x$ est égale à l'aire sous $N(0, 1)$ jusqu'à $(x - \mu)/\sigma$.*

Méthode : en centrant-réduisant, toute probabilité sur $X$ s'exprime avec $Z$, et on lit $\Phi$ dans la **table de $z$** (*z-table*).

Exemple : des scores suivent $N(100, 15)$. $P(X \le 130) = \Phi\left(\frac{130 - 100}{15}\right) = \Phi(2) \approx 0{,}977$, et $P(85 \le X \le 115) = \Phi(1) - \Phi(-1) = 2\Phi(1) - 1 \approx 0{,}683$, ce qui retrouve le « 68 % » de la règle des trois sigmas. [[Complément hors du cours|ⓘ]]

## Loi exponentielle (*exponential distribution*)

**Définition.** $X$ suit une **[[Loi exponentielle|loi exponentielle]]** de paramètre $\lambda > 0$ si sa densité est
$$f(x; \lambda) = \begin{cases} \lambda e^{-\lambda x} & x > 0 \\ 0 & \text{sinon} \end{cases}$$

![[Chp 5 - Continuous random variable - image15.png]]
*Figure : densités exponentielles pour $\lambda = 2$, $1$ et $0{,}5$ ; chaque courbe part de $\lambda$ en $x = 0$ et décroît d'autant plus vite que $\lambda$ est grand.*

**Proposition.** Si $X$ suit une loi exponentielle de paramètre $\lambda$, sa cdf est
$$F(x; \lambda) = \begin{cases} 0 & x \le 0 \\ 1 - e^{-\lambda x} & x > 0 \end{cases}$$
et sa moyenne et son écart-type valent tous deux $1/\lambda$.

La cdf s'obtient en intégrant la densité : $F(x) = \int_0^x \lambda e^{-\lambda y}\,dy = \left[-e^{-\lambda y}\right]_0^x = 1 - e^{-\lambda x}$, d'où $P(X > x) = e^{-\lambda x}$. La variance vaut $1/\lambda^2$ (calcul par la fonction génératrice ci-dessus). La loi exponentielle modélise une **durée d'attente** ou une **durée de vie** sans usure : temps entre deux arrivées de clients, entre deux désintégrations radioactives, avant la panne d'un composant électronique. $\lambda$ est un taux (événements par unité de temps) et $1/\lambda$ la durée moyenne. Si le nombre d'événements par unité de temps suit une [[Loi de Poisson|loi de Poisson]] de paramètre $\lambda$, le temps entre deux événements suit l'exponentielle de paramètre $\lambda$ (voir [[3 - Important discrete distributions]]). [[Complément hors du cours|ⓘ]]

**Absence de mémoire** : pour tous $s, t \ge 0$, $P(X > s + t \mid X > s) = \frac{e^{-\lambda(s+t)}}{e^{-\lambda s}} = e^{-\lambda t} = P(X > t)$. Un composant qui a déjà fonctionné $s$ heures a la même probabilité de tenir encore $t$ heures qu'un composant neuf ; c'est la seule loi continue qui a cette propriété, l'analogue continu de la [[Loi géométrique|loi géométrique]]. Elle ne convient donc pas à un matériel qui s'use, pour lequel on utilise par exemple la loi de Weibull ([[Loi exponentielle]]). [[Complément hors du cours|ⓘ]]

## Médiane et percentiles d'une variable continue

**Définition.** Soit $p \in [0, 1]$. Le **$(100p)$-ième percentile** ([[Quantile|percentile]]) de la loi d'une variable continue $X$, noté $\eta_p$, est défini implicitement par
$$p = F(\eta_p) = \int_{-\infty}^{\eta_p} f(y)\,dy \quad (3.2)$$
Si l'on peut inverser $F$ : $\eta_p = F^{-1}(p)$.

En particulier, la **médiane** est le 50ᵉ percentile, $\eta_{0{,}5} = F^{-1}(0{,}5)$ : la moitié de l'aire sous la densité est à gauche de la médiane, l'autre moitié à droite. On la note parfois simplement $\eta$.

**Interprétation.** Dire qu'un score est au 85ᵉ percentile de la population, c'est dire que 85 % des scores sont en dessous et 15 % au-dessus. De même, le 40ᵉ percentile dépasse 40 % des scores et est dépassé par 60 %. $\eta_p$ est la valeur de l'axe des $x$ telle que $100p\,\%$ de l'aire sous $f$ soit à sa gauche et $100(1-p)\,\%$ à sa droite. Exemple : $\eta_{0{,}75}$, le 75ᵉ percentile, laisse une aire 0,75 à sa gauche.

Calcul d'un percentile : résoudre $F(\eta_p) = p$. Pour la loi exponentielle, $1 - e^{-\lambda\eta_p} = p$ donne $\eta_p = -\frac{\ln(1 - p)}{\lambda}$, et la médiane vaut $\frac{\ln 2}{\lambda} \approx \frac{0{,}693}{\lambda}$, inférieure à la moyenne $1/\lambda$ : la loi est asymétrique, avec une longue queue à droite qui tire la moyenne vers le haut. En physique, cette médiane est la **demi-vie** d'un élément radioactif. Pour une loi normale, $\eta_p = \mu + z_p\,\sigma$, où $z_p$ est le percentile de $Z$ lu dans la table (par exemple $\eta_{0{,}95} \approx \mu + 1{,}645\,\sigma$). Les 25ᵉ et 75ᵉ percentiles sont les [[Quartiles et valeurs aberrantes|quartiles]]. [[Complément hors du cours|ⓘ]]

![[Chp 5 - Continuous random variable - image23.png]]
*Figure : le $(100p)$-ième percentile — aire grisée $p$ sous la densité à gauche de $\eta_p$ ; sur la cdf, les pointillés relient $\eta_p$ à $p = F(\eta_p)$.*

## Médiane d'une loi symétrique

Une loi continue dont la densité est symétrique a pour médiane $\eta$ le centre de symétrie, puisque la moitié de l'aire est de chaque côté de ce point.

![[Chp 5 - Continuous random variable - image12.png]]
*Figure : médianes de lois symétriques (uniforme sur $[A, B]$, triangulaire, en cloche) — $\eta$ est au centre de symétrie.*

## Loi d'une **fonction** d'une variable continue

**[[Théorème de transformation|Théorème de transformation]]** (*transformation theorem*). Soit $X$ de densité $f_X$ et $Y = g(X)$, où $g$ est monotone (strictement croissante ou strictement décroissante) sur l'ensemble des valeurs possibles de $X$, donc inversible : $X = h(Y)$. On suppose $h$ dérivable. Alors :
$$f_Y(y) = f_X(h(y)) \cdot |h'(y)| \quad (A)$$

D'où vient la formule : si $g$ est croissante, $F_Y(y) = P(g(X) \le y) = P(X \le h(y)) = F_X(h(y))$, et l'on dérive avec la [[Dérivation en chaîne|dérivation en chaîne]] : $f_Y(y) = f_X(h(y))\,h'(y)$. Si $g$ est décroissante, l'inégalité s'inverse, $F_Y(y) = 1 - F_X(h(y))$, et la dérivée fait apparaître $-h'(y) = |h'(y)|$. Le facteur $|h'(y)|$ corrige l'étirement ou la compression de l'axe par $g$, pour que l'aire totale reste 1. [[Complément hors du cours|ⓘ]]

Exemple : si $Y = aX + b$ avec $a \ne 0$, alors $h(y) = (y - b)/a$ et $f_Y(y) = \frac{1}{|a|}f_X\left(\frac{y - b}{a}\right)$. Appliqué à $Z \sim N(0, 1)$ et $X = \mu + \sigma Z$, cela redonne la densité de $N(\mu, \sigma)$ à partir de celle de $Z$. Quand $g$ n'est pas monotone, on revient à la fonction de répartition : pour $Y = X^2$ et $y > 0$, $F_Y(y) = P(-\sqrt{y} \le X \le \sqrt{y}) = F_X(\sqrt{y}) - F_X(-\sqrt{y})$, que l'on dérive. [[Complément hors du cours|ⓘ]]

Le chapitre ne contient pas d'exercice.
