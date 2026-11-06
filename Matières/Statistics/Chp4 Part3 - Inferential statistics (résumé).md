---
type: source
tags: [year3]
sources: ["[[Chp4 Part3 - Inferential statistics]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Chp4 Part3 - Inferential statistics]], dans [[Statistics (matière)]] : chapitre 4, partie 3, compléments sur les [[Intervalle de confiance|intervalles de confiance]] : taille d'échantillon, méthode générale du pivot, puis les cas où $\sigma$ est inconnu (loi de [[Loi de Student|Student]]), la variance (loi du [[Loi du khi-deux|khi-deux]]) et la proportion. En cas d'écart, le cours et ses images font foi. Seule l'image du tableau récapitulatif des intervalles (image11) a été ouverte ; les autres transcriptions n'ont pas été comparées aux images.

## Taille de l'échantillon

**Taille d'échantillon pour une erreur donnée sur la moyenne, variance connue.** Si $\bar{x}$ estime $\mu$, on est confiant à $100(1-\alpha)\,\%$ que l'erreur $|\bar{x} - \mu|$ ne dépasse pas $E$ quand
$$n = \left(\frac{z_{\alpha/2}\,\sigma}{E}\right)^2.$$

![[Chp4 Part3 - Inferential statistics - image10.png]]

*Figure : l'erreur $E = |\bar{x} - \mu|$ sur l'axe, entre les bornes $l = \bar{x} - z_{\alpha/2}\sigma/\sqrt{n}$ et $u = \bar{x} + z_{\alpha/2}\sigma/\sqrt{n}$.*

Relations entre taille $n$, longueur voulue $2E$, niveau $100(1-\alpha)$ et écart-type $\sigma$ :

- si la longueur $2E$ diminue ($\sigma$ et confiance fixés), $n$ augmente ;
- si $\sigma$ augmente ($2E$ et confiance fixés), $n$ augmente ;
- si le niveau de confiance augmente ($2E$ et $\sigma$ fixés), $n$ augmente.

## Intervalle pour la moyenne : loi quelconque, grand échantillon, $\sigma$ connu

Soit $X_1, \dots, X_n$ un échantillon d'une population quelconque de moyenne $\mu$ et d'écart-type $\sigma$. Pour $n$ grand, le [[Théorème central limite]] donne $\bar{X}$ approximativement normale, quelle que soit la population, donc $Z = (\bar{X} - \mu)/(\sigma/\sqrt{n})$ est approximativement normale centrée réduite :
$$P\left(-z_{\alpha/2} < \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} < z_{\alpha/2}\right) \approx 1 - \alpha.$$
D'où l'intervalle de grand échantillon, de niveau **approximatif** $100(1-\alpha)\,\%$ :
$$\left(\bar{x} - z_{\alpha/2}\frac{\sigma}{\sqrt{n}},\ \bar{x} + z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right) \qquad (*)$$

## Méthode générale pour construire un intervalle de confiance

Soit $X_1, \dots, X_n$ un échantillon aléatoire. On cherche une statistique $g(X_1, \dots, X_n; \theta)$ telle que :

1. $g$ dépend à la fois de l'échantillon et de $\theta$ ;
2. la loi de $g$ ne dépend ni de $\theta$ ni d'aucun autre paramètre inconnu.

Étapes :

1. Trouver des constantes $C_L$ et $C_U$ (qui ne dépendent pas de $\theta$, par la propriété 2) telles que
$$P[C_L \le g(X_1, \dots, X_n; \theta) \le C_U] = 1 - \alpha \qquad \text{(A)}$$
2. Manipuler les inégalités pour isoler $\theta$ :
$$P[L(X_1, \dots, X_n) \le \theta \le U(X_1, \dots, X_n)] = 1 - \alpha \qquad \text{(B)}$$
3. $L$ et $U$ sont les bornes inférieure et supérieure de l'intervalle à $100(1-\alpha)\,\%$.

$g$ s'appelle une **quantité pivot** (*pivotal quantity*) : on « pivote » autour d'elle pour passer de (A) à (B).

**Exemple** : $\theta = \mu$, $\sigma$ connu. $g = (\bar{X} - \mu)/(\sigma/\sqrt{n})$ vérifie les deux conditions (elle suit la loi normale centrée réduite). $C_L = -z_{\alpha/2}$, $C_U = z_{\alpha/2}$, d'où $L = \bar{X} - z_{\alpha/2}\sigma/\sqrt{n}$ et $U = \bar{X} + z_{\alpha/2}\sigma/\sqrt{n}$.

## Application : moyenne quand $\sigma$ est inconnu

On remplace $\sigma$ dans $Z$ par l'écart-type d'échantillon $S$ :
$$T = \frac{\bar{X} - \mu}{S/\sqrt{n}}$$
Question du cours : est-ce une quantité pivot ? (La réponse vient avec le théorème de Gosset, plus bas.)

## Interlude : la loi du $\chi^2$

([[Loi du khi-deux]])

**Définition** : pour un entier $\nu > 0$, soient $Z_1, \dots, Z_\nu$ des normales centrées réduites iid. La loi du khi-deux à $\nu$ degrés de liberté (*df*) est la loi de
$$X = Z_1^2 + \dots + Z_\nu^2, \qquad \text{notée } X \sim \chi^2_\nu.$$

**Proposition** : $\chi^2_\nu$ est la loi gamma de paramètres $\alpha = \nu/2$ et $\beta = 2$. Sa densité est
$$f(x; \nu) = \frac{1}{2^{\nu/2}\,\Gamma(\nu/2)}\, x^{(\nu/2) - 1}\, e^{-x/2}, \quad x > 0.$$

**Proposition** :

1. si $X_3 = X_1 + X_2$, avec $X_1 \sim \chi^2_{\nu_1}$ et $X_2 \sim \chi^2_{\nu_2}$ indépendantes, alors $X_3 \sim \chi^2_{\nu_1 + \nu_2}$ : la loi est **additive** ;
2. si $X_3 = X_1 + X_2$, avec $X_1$, $X_2$ indépendantes, $X_1 \sim \chi^2_{\nu_1}$ et $X_3 \sim \chi^2_{\nu_3}$, $\nu_3 > \nu_1$, alors $X_2 \sim \chi^2_{\nu_3 - \nu_1}$ : elle est **soustractive**.

![[Chp4 Part3 - Inferential statistics - image13.png]]

*Figure : densités du $\chi^2$ pour 1, 2, 3 et 5 degrés de liberté : à 1 et 2 df la courbe décroît depuis 0 ; à 3 et 5 df elle a un pic décalé vers la droite et une queue longue.*

**Proposition** (distribution d'échantillonnage de la variance, cas gaussien) : si $X_1, \dots, X_n$ est un échantillon d'une loi $N(\mu, \sigma)$, alors
$$\frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}.$$
Preuve : en devoir (*HW*). La variance d'échantillon est donc un khi-deux (remis à l'échelle) à $n - 1$ degrés de liberté. Voir [[Distribution d'échantillonnage]].

**Notation** : $\chi^2_{\alpha,\nu}$, **valeur critique** du khi-deux ([[Valeur critique]]), est le nombre de l'axe tel que l'aire sous la courbe à $\nu$ df **à droite** de $\chi^2_{\alpha,\nu}$ vaut $\alpha$.

![[Chp4 Part3 - Inferential statistics - image5.png]]

*Figure : notation $\chi^2_{\alpha,\nu}$ : (a) aire $\alpha$ à droite de $\chi^2_{\alpha,\nu}$ ; (b) deux aires de 0,01, à gauche de $\chi^2_{0{,}99,\nu}$ et à droite de $\chi^2_{0{,}01,\nu}$.*

## Intervalle de confiance pour la variance (variable gaussienne)

(Titre du cours : « mean known », voir les points à vérifier.)

Si $s^2$ est la variance d'un échantillon de $n$ observations d'une loi normale de variance inconnue $\sigma^2$, un intervalle de confiance à $100(1-\alpha)\,\%$ pour $\sigma^2$ est
$$\frac{(n-1)s^2}{\chi^2_{\alpha/2,\,n-1}} \le \sigma^2 \le \frac{(n-1)s^2}{\chi^2_{1-\alpha/2,\,n-1}} \qquad (1)$$
où $\chi^2_{\alpha/2,n-1}$ et $\chi^2_{1-\alpha/2,n-1}$ sont les points de pourcentage supérieur et inférieur $100\alpha/2$ du khi-deux à $n - 1$ df. Pour $\sigma$, on prend les racines carrées des bornes de (1).

![[Chp4 Part3 - Inferential statistics - image7.png]]

*Figure : aires de queue du $\chi^2$ : aire $\alpha$ à droite de $\chi^2_{\alpha,k}$ ; aire $\alpha/2$ de chaque côté ; exemple à 10 df : $\chi^2_{0{,}95,10} = 3{,}94$ et $\chi^2_{0{,}05,10} = 18{,}31$.*

## Interlude : la loi $t$ (de Student)

([[Loi de Student]])

**Définition** : soit $Z$ normale centrée réduite et $Y \sim \chi^2_v$ indépendante de $Z$. La loi $t$ à $v$ degrés de liberté est la loi de
$$T = \frac{Z}{\sqrt{Y/v}}, \qquad \text{notée } T \sim t_v.$$

**Proposition** : la densité de $T \sim t_v$ est
$$f(t) = \frac{1}{\sqrt{\pi v}}\,\frac{\Gamma((v+1)/2)}{\Gamma(v/2)}\,\frac{1}{(1 + t^2/v)^{(v+1)/2}}, \quad -\infty < t < \infty.$$
Preuve : en devoir.

![[Chp4 Part3 - Inferential statistics - image6.png]]

*Figure : courbes $t$ à 1, 5 et 20 df comparées à la courbe $z$ : plus le nombre de df est grand, plus la courbe est proche de la normale ; à 1 df, les queues sont les plus épaisses.*

**Théorème de Gosset** : si $X_1, \dots, X_n$ est un échantillon d'une loi $N(\mu, \sigma)$, alors
$$\frac{\bar{X} - \mu}{S/\sqrt{n}} \sim t_{n-1}.$$
Preuve : en devoir.

**Notation** : $t_{\alpha,\nu}$, **valeur critique** $t$, est le nombre de l'axe tel que l'aire sous la courbe $t$ à $\nu$ df à droite de $t_{\alpha,\nu}$ vaut $\alpha$.

![[Chp4 Part3 - Inferential statistics - image4.png]]

*Figure : courbe $t_\nu$ centrée en 0, aire ombrée $\alpha$ à droite de $t_{\alpha,\nu}$.*

## Intervalle pour la moyenne : variable gaussienne, variance inconnue

Si $\bar{x}$ et $s$ sont la moyenne et l'écart-type d'un échantillon d'une loi normale de variance inconnue, un intervalle de confiance à $100(1-\alpha)\,\%$ pour $\mu$ est
$$\bar{x} - t_{\alpha/2,\,n-1}\,\frac{s}{\sqrt{n}} \le \mu \le \bar{x} + t_{\alpha/2,\,n-1}\,\frac{s}{\sqrt{n}}$$
où $t_{\alpha/2,n-1}$ est le point de pourcentage supérieur $100\alpha/2$ de la loi $t$ à $n - 1$ df. Voir [[Test t]].

![[Chp4 Part3 - Inferential statistics - image2.png]]

*Figure : courbe $t$ avec la queue droite ombrée au-delà de $t_{\alpha/2}$, d'aire $\alpha/2$.*

### Tableau récapitulatif (échantillon gaussien)

$X_1, \dots, X_n \sim \mathcal{N}(\mu, \sigma^2)$, $\bar{X} = \sum X_i / n$, $S = \sqrt{\sum (X_i - \bar{X})^2/(n-1)}$. Intervalles à $100(1-\alpha)\,\%$, tels qu'écrits sur l'image :

| Hypothèse | Paramètre | Intervalle bilatéral | Intervalle inférieur | Intervalle supérieur |
|---|---|---|---|---|
| $\sigma^2$ connu | $\mu$ | $\bar{X} \pm z_{\alpha/2}\dfrac{\sigma}{\sqrt{n}}$ | $\left(-\infty,\ \bar{X} + z_\alpha\dfrac{\sigma}{\sqrt{n}}\right)$ | $\left(\bar{X} + z_\alpha\dfrac{\sigma}{\sqrt{n}},\ \infty\right)$ (sic, voir point 1) |
| $\sigma^2$ inconnu | $\mu$ | $\bar{X} \pm t_{\alpha/2,n-1}\dfrac{S}{\sqrt{n}}$ | $\left(-\infty,\ \bar{X} + t_{\alpha,n-1}\dfrac{S}{\sqrt{n}}\right)$ | $\left(\bar{X} - t_{\alpha,n-1}\dfrac{S}{\sqrt{n}},\ \infty\right)$ |
| $\mu$ inconnu | $\sigma^2$ | $\left(\dfrac{(n-1)S^2}{\chi^2_{\alpha/2,n-1}},\ \dfrac{(n-1)S^2}{\chi^2_{1-\alpha/2,n-1}}\right)$ | $\left(0,\ \dfrac{(n-1)S^2}{\chi^2_{1-\alpha,n-1}}\right)$ | $\left(\dfrac{(n-1)S^2}{\chi^2_{\alpha,n-1}},\ \infty\right)$ |

## Intervalle pour une proportion $p$

Rappel (TCL appliqué à une binomiale) : si $n$ est grand,
$$Z = \frac{X - np}{\sqrt{np(1-p)}} = \frac{\hat{P} - p}{\sqrt{p(1-p)/n}}$$
est approximativement normale centrée réduite. Voir [[Approximation normale]].

**Intervalle approché pour une proportion binomiale** : si $\hat{p}$ est la proportion d'observations d'un échantillon de taille $n$ qui appartiennent à une classe d'intérêt, un intervalle approché à $100(1-\alpha)\,\%$ pour la proportion $p$ de la population est
$$\hat{p} - z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}} \le p \le \hat{p} + z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$
où $z_{\alpha/2}$ est le point de pourcentage supérieur $\alpha/2$ de la loi normale centrée réduite.

### Taille d'échantillon pour estimer une proportion

Pour une erreur $E$ donnée :
$$n = \left(\frac{z_{\alpha/2}}{E}\right)^2 p(1-p).$$
$p(1-p)$ est maximal en $p = 0{,}5$, où il vaut $0{,}25$. Le cours conclut qu'« on peut appliquer le TCL tant que $n$ est plus grand que »
$$n = \left(\frac{z_{\alpha/2}}{E}\right)^2 \times 0{,}25.$$

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Tableau récapitulatif, ligne « $\sigma^2$ connu »** : image11 ouverte, l'alerte est fondée. Les intervalles inférieur et supérieur portent tous deux $\bar{X} + z_\alpha\sigma/\sqrt{n}$, ce qui est écrit sur l'image. L'intervalle supérieur devrait être $(\bar{X} - z_\alpha\sigma/\sqrt{n}, \infty)$, comme dans la ligne « $\sigma^2$ inconnu » (complément). **À corriger avant un examen.**
2. **Titre de la section sur la variance** : « Gaussian distributed rv, mean known ». Les formules utilisent $s^2$ et $\chi^2_{n-1}$, donc la moyenne est inconnue et estimée par $\bar{x}$. Le tableau récapitulatif écrit d'ailleurs « $\mu$ unknown ». « Mean known » est une erreur de titre (complément). **À corriger avant un examen.**
3. **Quantité pivot de $T$** : la question « is this a pivotal quantity ? » reste sans réponse écrite dans la note. Le théorème de Gosset y répond : $T \sim t_{n-1}$, une loi qui ne dépend d'aucun paramètre inconnu, donc oui (complément, pour un échantillon normal).
4. **Hypothèses de Student** : le théorème de Gosset et l'intervalle de Student supposent un échantillon normal. Le cours le dit pour le théorème, non pour la section sur la proportion ou le TCL : l'intervalle $t$ pour une loi quelconque n'est pas traité.
5. **Figure de $\chi^2$** : la transcription note un « X » majuscule à la place de $\chi$ dans la figure. Défaut de police sans conséquence.
6. **Taille pour une proportion** : « on peut appliquer le TCL tant que $n$ est plus grand que… » mélange deux choses. Avec $p(1-p) \le 0{,}25$, la formule donne la taille suffisante pour une erreur $E$, ce qui n'a pas de lien direct avec la condition du TCL (complément).
7. **Faux liens automatiques** : dans la note, « gamma distribution » pointe vers [[Loi exponentielle]], « degrees of freedom » vers [[Variance et écart-type d'échantillon]] et « iid » vers [[Échantillonnage]] : liens approximatifs.
