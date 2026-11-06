---
type: source
tags: [year2]
sources: ["[[Chp 5 - Continuous random variable]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Chp 5 - Continuous random variable]], dans [[Probability (matière)]]. En cas d'écart, le cours et ses images font foi. Les énoncés donnés en images sont recopiés ; les images qui portent une courbe ou un schéma sont intégrées à côté de leur énoncé.

## Idée générale

Reprendre le chapitre 4 pour les variables continues : les sommes deviennent des [[Intégrale|intégrales]] et la loi est une densité. Le chapitre présente aussi les lois uniforme, normale et exponentielle, la fonction génératrice des moments et le changement de variable.

## Densité de probabilité (*probability density function*, PDF)

À distinguer de la fonction de masse (*[[Variable aléatoire|probability mass function]]*), réservée aux variables discrètes.

**Définition.** Soit $X$ une variable aléatoire continue. Une **loi de probabilité** ou **densité** (*pdf*) de $X$ est une fonction $f(x)$ telle que, pour tous $a \le b$ :
$$P(a \le X \le b) = \int_a^b f(x)\,dx$$

Pour que $f$ soit une densité légitime, il faut :
1. $f(x) \ge 0$ pour tout $x$ ;
2. $\displaystyle\int_{-\infty}^{\infty} f(x)\,dx = [\text{aire sous tout le graphe de } f] = 1$.

## Loi uniforme (*uniform distribution*)

**Définition.** Une variable continue $X$ suit une **[[Loi uniforme|loi uniforme]]** sur $[A, B]$ si sa densité est
$$f(x; A, B) = \begin{cases} \dfrac{1}{B - A} & A \le x \le B \\ 0 & \text{sinon} \end{cases}$$
On note $X \sim \mathrm{Unif}[A, B]$.

## La probabilité d'un point est nulle

Pour une variable continue, la probabilité de prendre exactement une valeur est nulle :
$$P(X = c) = P(c \le X \le c) = \int_c^c f(x)\,dx = 0$$
Conséquence : inclure ou exclure les bornes de l'intégrale ne change rien :
$$P(a \le X \le b) = P(a < X < b) = P(a < X \le b) = P(a \le X < b)$$

## Fonction de répartition d'une variable continue (CDF)

**Définition.** La **[[Fonction de répartition|fonction de répartition]]** (*cumulative distribution function*) d'une variable continue $X$ est définie pour tout $x$ par :
$$F(x) = P(X \le x) = \int_{-\infty}^{x} f(y)\,dy$$

![[Cours/Year 2/Probability/medias/Chp 5 - Continuous random variable/image14.png]]
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

## Loi gaussienne ou normale (*Gaussian, normal distribution*)

**Définition.** Une variable continue $X$ suit une **[[Loi normale|loi normale]]** (ou gaussienne) de paramètres $\mu$ et $\sigma$, avec $-\infty < \mu < \infty$ et $\sigma > 0$, si sa densité est
$$f(x; \mu, \sigma) = \frac{1}{\sigma\sqrt{2\pi}}\, e^{-(x - \mu)^2/(2\sigma^2)}, \qquad -\infty < x < \infty \quad (3.3)$$
On abrège : $X \sim N(\mu, \sigma)$.

![[Cours/Year 2/Probability/medias/Chp 5 - Continuous random variable/image1.png]]
*Figure : définition et trois courbes de densité normale (*normal density curves*), graduées en $\mu$ et $\mu + \sigma$ — plus $\sigma$ est grand, plus la cloche est large et basse.*

**Règle 9.8 (règle 68-95-99,7 ou des trois sigmas).** Si $X \sim \mathcal{N}(\mu, \sigma^2)$ :
$$P(|X - \mu| < \sigma) \approx 68\,\%, \qquad P(|X - \mu| < 2\sigma) \approx 95\,\%, \qquad P(|X - \mu| < 3\sigma) \approx 99{,}73\,\%$$

## Loi normale centrée réduite (*standard normal distribution*)

**Définition.** La loi normale de paramètres $\mu = 0$ et $\sigma = 1$ est la **loi normale centrée réduite**. Une variable qui la suit est notée $Z$, de densité
$$f(z; 0, 1) = \frac{1}{\sqrt{2\pi}}\, e^{-z^2/2}, \qquad -\infty < z < \infty$$
Sa cdf est notée $\Phi$ :
$$\Phi(z) = P(Z \le z) = \int_{-\infty}^{z} \frac{1}{\sqrt{2\pi}}\, e^{-y^2/2}\,dy$$

![[Cours/Year 2/Probability/medias/Chp 5 - Continuous random variable/image6.png]]
*Figure : courbe normale centrée réduite (*standard normal (z) curve*) ; l'aire grisée à gauche de $z$ vaut $\Phi(z)$.*

## Passer d'une loi normale quelconque à la loi centrée réduite

**Proposition.** Si $X \sim N(\mu, \sigma)$, la variable **centrée réduite** (*standardized*)
$$Z = \frac{X - \mu}{\sigma}$$
suit la loi normale centrée réduite (voir [[Centrage et réduction]]). Donc :
$$P(a \le X \le b) = P\left(\frac{a - \mu}{\sigma} \le Z \le \frac{b - \mu}{\sigma}\right) = \Phi\left(\frac{b - \mu}{\sigma}\right) - \Phi\left(\frac{a - \mu}{\sigma}\right)$$
$$P(X \le a) = \Phi\left(\frac{a - \mu}{\sigma}\right), \qquad P(X \ge b) = 1 - \Phi\left(\frac{b - \mu}{\sigma}\right)$$
Réciproquement, si $Z \sim N(0, 1)$ et $\sigma > 0$, la variable « dé-réduite » $X = \mu + \sigma Z$ suit une loi normale de moyenne $\mu$ et d'écart-type $\sigma$.

![[Cours/Year 2/Probability/medias/Chp 5 - Continuous random variable/image24.png]]
*Figure : l'aire sous $N(\mu, \sigma)$ jusqu'à $x$ est égale à l'aire sous $N(0, 1)$ jusqu'à $(x - \mu)/\sigma$.*

Méthode : en centrant-réduisant, toute probabilité sur $X$ s'exprime avec $Z$, et on lit $\Phi$ dans la **table de $z$** (*z-table*).

## Loi exponentielle (*exponential distribution*)

**Définition.** $X$ suit une **[[Loi exponentielle|loi exponentielle]]** de paramètre $\lambda > 0$ si sa densité est
$$f(x; \lambda) = \begin{cases} \lambda e^{-\lambda x} & x > 0 \\ 0 & \text{sinon} \end{cases}$$

![[Cours/Year 2/Probability/medias/Chp 5 - Continuous random variable/image15.png]]
*Figure : densités exponentielles pour $\lambda = 2$, $1$ et $0{,}5$ ; chaque courbe part de $\lambda$ en $x = 0$ et décroît d'autant plus vite que $\lambda$ est grand.*

**Proposition.** Si $X$ suit une loi exponentielle de paramètre $\lambda$, sa cdf est
$$F(x; \lambda) = \begin{cases} 0 & x \le 0 \\ 1 - e^{-\lambda x} & x > 0 \end{cases}$$
et sa moyenne et son écart-type valent tous deux $1/\lambda$.

## Médiane et percentiles d'une variable continue

**Définition.** Soit $p \in [0, 1]$. Le **$(100p)$-ième percentile** ([[Quantile|percentile]]) de la loi d'une variable continue $X$, noté $\eta_p$, est défini implicitement par
$$p = F(\eta_p) = \int_{-\infty}^{\eta_p} f(y)\,dy \quad (3.2)$$
Si l'on peut inverser $F$ : $\eta_p = F^{-1}(p)$.

En particulier, la **médiane** est le 50ᵉ percentile, $\eta_{0{,}5} = F^{-1}(0{,}5)$ : la moitié de l'aire sous la densité est à gauche de la médiane, l'autre moitié à droite. On la note parfois simplement $\eta$.

**Interprétation.** Dire qu'un score est au 85ᵉ percentile de la population, c'est dire que 85 % des scores sont en dessous et 15 % au-dessus. De même, le 40ᵉ percentile dépasse 40 % des scores et est dépassé par 60 %. $\eta_p$ est la valeur de l'axe des $x$ telle que $100p\,\%$ de l'aire sous $f$ soit à sa gauche et $100(1-p)\,\%$ à sa droite. Exemple : $\eta_{0{,}75}$, le 75ᵉ percentile, laisse une aire 0,75 à sa gauche.

![[Cours/Year 2/Probability/medias/Chp 5 - Continuous random variable/image23.png]]
*Figure : le $(100p)$-ième percentile — aire grisée $p$ sous la densité à gauche de $\eta_p$ ; sur la cdf, les pointillés relient $\eta_p$ à $p = F(\eta_p)$.*

## Médiane d'une loi symétrique

Une loi continue dont la densité est symétrique a pour médiane $\eta$ le centre de symétrie, puisque la moitié de l'aire est de chaque côté de ce point.

![[Cours/Year 2/Probability/medias/Chp 5 - Continuous random variable/image12.png]]
*Figure : médianes de lois symétriques (uniforme sur $[A, B]$, triangulaire, en cloche) — $\eta$ est au centre de symétrie.*

## Loi d'une **fonction** d'une variable continue

**[[Théorème de transformation|Théorème de transformation]]** (*transformation theorem*). Soit $X$ de densité $f_X$ et $Y = g(X)$, où $g$ est monotone (strictement croissante ou strictement décroissante) sur l'ensemble des valeurs possibles de $X$, donc inversible : $X = h(Y)$. On suppose $h$ dérivable. Alors :
$$f_Y(y) = f_X(h(y)) \cdot |h'(y)| \quad (A)$$

Le chapitre ne contient pas d'exercice.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Notation de la loi normale** : le cours écrit $N(\mu, \sigma)$ (écart-type) pour la définition, puis $\mathcal{N}(\mu, \sigma^2)$ (variance) dans la règle 68-95-99,7. Il s'agit de la même loi, la seconde notation compte la variance. À ne pas confondre dans un exercice (complément).
2. **Tableau récapitulatif de la fonction génératrice** : il écrit $M_X^{(2)}(0) = E[X^2]$ puis « ... ». C'est cohérent avec $E(X^r) = M^{(r)}_X(0)$. Le chapitre précédent n'ayant pas de section sur la fonction génératrice, la phrase « as in the discrete case » renvoie à un cas absent des notes (complément).
3. **Deux alertes de lecture seulement** : le coin coupé de la proposition $F' = f$ et le « (A) » de la dernière image ne gênent pas le sens. Fausses alertes sur le fond.
4. **Percentile** : le $p$ lu sur le graphique de $F(x)$ (entre 0,2 et 0,4) est illisible. Aucun chiffre n'est repris dans le wiki.
5. **Définition du percentile** : l'image écrit « $p$ between 0 and 1 » ; pour $p = 0$ ou $p = 1$, $\eta_p$ n'est en général pas défini par une valeur finie (complément).
6. **Légende de l'image des lois symétriques** : la transcription signale « svmmetric » dans l'image, lu comme *symmetric*. Défaut de lecture, sans effet sur le fond.
