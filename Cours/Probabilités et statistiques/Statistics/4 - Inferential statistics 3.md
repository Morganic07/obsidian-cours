---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Statistics/Chp4 Part3 : Inferential statistics.docx|Chp4 Part3 - Inferential statistics]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Statistics/Chp4 Part3 : Inferential statistics.docx|Chp4 Part3 - Inferential statistics]], dans [[Cours/Probabilités et statistiques/Statistics/_index|Statistics]] : chapitre 4, partie 3, compléments sur les [[Intervalle de confiance|intervalles de confiance]] : taille d'échantillon, méthode générale du pivot, puis les cas où $\sigma$ est inconnu (loi de [[Loi de Student|Student]]), la variance (loi du [[Loi du khi-deux|khi-deux]]) et la proportion. Seule l'image du tableau récapitulatif des intervalles (image11) a été ouverte ; les autres transcriptions n'ont pas été comparées aux images.

## Taille de l'échantillon

**Taille d'échantillon pour une erreur donnée sur la moyenne, variance connue.** Si $\bar{x}$ estime $\mu$, on est confiant à $100(1-\alpha)\,\%$ que l'erreur $|\bar{x} - \mu|$ ne dépasse pas $E$ quand
$$n = \left(\frac{z_{\alpha/2}\,\sigma}{E}\right)^2.$$

![[Chp4 Part3 - Inferential statistics - image10.png]]

*Figure : l'erreur $E = |\bar{x} - \mu|$ sur l'axe, entre les bornes $l = \bar{x} - z_{\alpha/2}\sigma/\sqrt{n}$ et $u = \bar{x} + z_{\alpha/2}\sigma/\sqrt{n}$.*

D'où vient la formule : l'erreur maximale est la demi-longueur de l'intervalle, $E = z_{\alpha/2}\,\sigma/\sqrt{n}$ ; on isole $\sqrt{n} = z_{\alpha/2}\,\sigma/E$, puis on élève au carré. Comme $n$ doit être entier, on arrondit **toujours à l'entier supérieur** (arrondir en dessous donnerait une erreur un peu plus grande que $E$). Exemple : $\sigma = 10$, $E = 2$, confiance 95 % ($z_{0{,}025} = 1{,}96$) : $n = (1{,}96 \times 10/2)^2 = 96{,}04$, donc $n = 97$. [[Complément hors du cours|ⓘ]]

Relations entre taille $n$, longueur voulue $2E$, niveau $100(1-\alpha)$ et écart-type $\sigma$ :

- si la longueur $2E$ diminue ($\sigma$ et confiance fixés), $n$ augmente ;
- si $\sigma$ augmente ($2E$ et confiance fixés), $n$ augmente ;
- si le niveau de confiance augmente ($2E$ et $\sigma$ fixés), $n$ augmente.

$n$ varie comme $1/E^2$ : diviser l'erreur par 2 demande 4 fois plus d'observations, la diviser par 10 en demande 100 fois plus. C'est pourquoi la précision coûte cher. [[Complément hors du cours|ⓘ]]

## Intervalle pour la moyenne : loi quelconque, grand échantillon, $\sigma$ connu

Soit $X_1, \dots, X_n$ un échantillon d'une population quelconque de moyenne $\mu$ et d'écart-type $\sigma$. Pour $n$ grand, le [[Théorème central limite]] donne $\bar{X}$ approximativement normale, quelle que soit la population, donc $Z = (\bar{X} - \mu)/(\sigma/\sqrt{n})$ est approximativement normale centrée réduite :
$$P\left(-z_{\alpha/2} < \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} < z_{\alpha/2}\right) \approx 1 - \alpha.$$
D'où l'intervalle de grand échantillon, de niveau **approximatif** $100(1-\alpha)\,\%$ :
$$\left(\bar{x} - z_{\alpha/2}\frac{\sigma}{\sqrt{n}},\ \bar{x} + z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right) \qquad (*)$$

Si $\sigma$ est inconnu mais $n$ grand (règle usuelle des manuels : $n \ge 30$), on remplace $\sigma$ par l'écart-type d'échantillon $s$ dans (*) et l'intervalle reste approximativement de niveau $100(1-\alpha)\,\%$ : pour $n$ grand, $s$ est très proche de $\sigma$. Pour un petit échantillon, il faut la loi de Student (plus bas), et donc une population gaussienne. [[Complément hors du cours|ⓘ]]

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

**Interprétation.** Dans (B), ce sont $L$ et $U$ qui sont aléatoires, pas $\theta$, qui est un nombre fixe inconnu. Une fois l'échantillon observé, l'intervalle numérique $[l, u]$ contient $\theta$ ou ne le contient pas : on ne peut pas dire que « $\theta$ a 95 % de chances d'y être ». Le niveau $1 - \alpha$ qualifie la **méthode** : si l'on répétait l'expérience un grand nombre de fois, environ $100(1-\alpha)\,\%$ des intervalles obtenus contiendraient $\theta$. [[Complément hors du cours|ⓘ]]

$g$ s'appelle une **quantité pivot** (*pivotal quantity*) : on « pivote » autour d'elle pour passer de (A) à (B).

**Exemple** : $\theta = \mu$, $\sigma$ connu. $g = (\bar{X} - \mu)/(\sigma/\sqrt{n})$ vérifie les deux conditions (elle suit la loi normale centrée réduite). $C_L = -z_{\alpha/2}$, $C_U = z_{\alpha/2}$, d'où $L = \bar{X} - z_{\alpha/2}\sigma/\sqrt{n}$ et $U = \bar{X} + z_{\alpha/2}\sigma/\sqrt{n}$.

Le pivotement en détail : on part de $-z_{\alpha/2} \le \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \le z_{\alpha/2}$ ; on multiplie par $\sigma/\sqrt{n} > 0$, ce qui donne $-z_{\alpha/2}\sigma/\sqrt{n} \le \bar{X} - \mu \le z_{\alpha/2}\sigma/\sqrt{n}$ ; on retranche $\bar{X}$ puis on multiplie par $-1$, ce qui **inverse les inégalités** : $\bar{X} - z_{\alpha/2}\sigma/\sqrt{n} \le \mu \le \bar{X} + z_{\alpha/2}\sigma/\sqrt{n}$. Les deux encadrements décrivent le même événement, donc ont la même probabilité $1 - \alpha$. [[Complément hors du cours|ⓘ]]

## Application : moyenne quand $\sigma$ est inconnu

On remplace $\sigma$ dans $Z$ par l'écart-type d'échantillon $S$ :
$$T = \frac{\bar{X} - \mu}{S/\sqrt{n}}$$
Question du cours : est-ce une quantité pivot ? (La réponse vient avec le théorème de Gosset, plus bas.)

## Interlude : la loi du $\chi^2$

([[Loi du khi-deux]])

**Définition** : pour un entier $\nu > 0$, soient $Z_1, \dots, Z_\nu$ des normales centrées réduites iid. La loi du khi-deux à $\nu$ degrés de liberté (*df*) est la loi de
$$X = Z_1^2 + \dots + Z_\nu^2, \qquad \text{notée } X \sim \chi^2_\nu.$$

Espérance et variance : comme $E(Z_i^2) = \operatorname{Var}(Z_i) = 1$ et $\operatorname{Var}(Z_i^2) = E(Z_i^4) - 1 = 3 - 1 = 2$, on obtient par indépendance $E(X) = \nu$ et $\operatorname{Var}(X) = 2\nu$. La loi ne prend que des valeurs positives (somme de carrés) ; elle est asymétrique à droite et devient de plus en plus symétrique, proche d'une normale, quand $\nu$ grandit. [[Complément hors du cours|ⓘ]]

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

Pourquoi $n - 1$ et non $n$ [[Variance et écart-type d'échantillon|degrés de liberté]] : les $n$ écarts $X_i - \bar{X}$ ne sont pas libres, puisqu'ils vérifient toujours $\sum (X_i - \bar{X}) = 0$ ; connaissant $n - 1$ d'entre eux, on en déduit le dernier. Estimer $\mu$ par $\bar{X}$ « consomme » un degré de liberté. Avec $\mu$ connu, on aurait $\sum (X_i - \mu)^2/\sigma^2 \sim \chi^2_n$, directement par la définition. [[Complément hors du cours|ⓘ]]

Dans le cas gaussien, $\bar{X}$ et $S^2$ sont de plus **indépendantes** (théorème de Fisher, ou de Cochran). C'est ce résultat qui permet de construire la loi de Student à partir de $\bar{X}$ et $S$, plus bas. [[Complément hors du cours|ⓘ]]

**Notation** : $\chi^2_{\alpha,\nu}$, **valeur critique** du khi-deux ([[Valeur critique]]), est le nombre de l'axe tel que l'aire sous la courbe à $\nu$ df **à droite** de $\chi^2_{\alpha,\nu}$ vaut $\alpha$.

![[Chp4 Part3 - Inferential statistics - image5.png]]

*Figure : notation $\chi^2_{\alpha,\nu}$ : (a) aire $\alpha$ à droite de $\chi^2_{\alpha,\nu}$ ; (b) deux aires de 0,01, à gauche de $\chi^2_{0{,}99,\nu}$ et à droite de $\chi^2_{0{,}01,\nu}$.*

## Intervalle de confiance pour la variance (variable gaussienne)

Cas d'une moyenne $\mu$ inconnue. [[Erreurs du cours#^e-4-inferential-statistics-3|✎]]

Si $s^2$ est la variance d'un échantillon de $n$ observations d'une loi normale de variance inconnue $\sigma^2$, un intervalle de confiance à $100(1-\alpha)\,\%$ pour $\sigma^2$ est
$$\frac{(n-1)s^2}{\chi^2_{\alpha/2,\,n-1}} \le \sigma^2 \le \frac{(n-1)s^2}{\chi^2_{1-\alpha/2,\,n-1}} \qquad (1)$$
où $\chi^2_{\alpha/2,n-1}$ et $\chi^2_{1-\alpha/2,n-1}$ sont les points de pourcentage supérieur et inférieur $100\alpha/2$ du khi-deux à $n - 1$ df. Pour $\sigma$, on prend les racines carrées des bornes de (1).

D'où vient (1) : c'est la méthode du pivot avec $g = (n-1)S^2/\sigma^2 \sim \chi^2_{n-1}$, dont la loi ne dépend d'aucun paramètre. On part de $P\left(\chi^2_{1-\alpha/2,n-1} \le \frac{(n-1)S^2}{\sigma^2} \le \chi^2_{\alpha/2,n-1}\right) = 1 - \alpha$, puis on passe aux inverses, ce qui **inverse les inégalités** : la plus grande valeur critique, $\chi^2_{\alpha/2}$, se retrouve au dénominateur de la borne inférieure. [[Complément hors du cours|ⓘ]]

Contrairement à l'intervalle de la moyenne, cet intervalle n'est **pas symétrique** autour de $s^2$, puisque la loi du khi-deux ne l'est pas. Il est aussi très sensible à l'hypothèse de normalité : si la population n'est pas gaussienne, son niveau réel peut s'écarter nettement de $1 - \alpha$, même pour $n$ grand. [[Complément hors du cours|ⓘ]]

![[Chp4 Part3 - Inferential statistics - image7.png]]

*Figure : aires de queue du $\chi^2$ : aire $\alpha$ à droite de $\chi^2_{\alpha,k}$ ; aire $\alpha/2$ de chaque côté ; exemple à 10 df : $\chi^2_{0{,}95,10} = 3{,}94$ et $\chi^2_{0{,}05,10} = 18{,}31$.*

## Interlude : la loi $t$ (de Student)

([[Loi de Student]])

**Définition** : soit $Z$ normale centrée réduite et $Y \sim \chi^2_v$ indépendante de $Z$. La loi $t$ à $v$ degrés de liberté est la loi de
$$T = \frac{Z}{\sqrt{Y/v}}, \qquad \text{notée } T \sim t_v.$$

La loi a été publiée en 1908 par William Sealy Gosset, chimiste de la brasserie Guinness, sous le pseudonyme « Student » : d'où les deux noms, loi de Student et théorème de Gosset. Il travaillait sur de petits échantillons, où remplacer $\sigma$ par $s$ ne peut pas être négligé. [[Complément hors du cours|ⓘ]]

**Proposition** : la densité de $T \sim t_v$ est
$$f(t) = \frac{1}{\sqrt{\pi v}}\,\frac{\Gamma((v+1)/2)}{\Gamma(v/2)}\,\frac{1}{(1 + t^2/v)^{(v+1)/2}}, \quad -\infty < t < \infty.$$
Preuve : en devoir.

![[Chp4 Part3 - Inferential statistics - image6.png]]

*Figure : courbes $t$ à 1, 5 et 20 df comparées à la courbe $z$ : plus le nombre de df est grand, plus la courbe est proche de la normale ; à 1 df, les queues sont les plus épaisses.*

Propriétés : la loi $t_v$ est symétrique autour de 0 ; son espérance vaut 0 pour $v > 1$ et sa variance $\frac{v}{v-2}$ pour $v > 2$, toujours supérieure à 1 (celle de $Z$). À $v = 1$, c'est la loi de Cauchy, qui n'a pas d'espérance. Quand $v \to \infty$, $t_v$ tend vers la loi normale centrée réduite. [[Complément hors du cours|ⓘ]]

**Théorème de Gosset** : si $X_1, \dots, X_n$ est un échantillon d'une loi $N(\mu, \sigma)$, alors
$$\frac{\bar{X} - \mu}{S/\sqrt{n}} \sim t_{n-1}.$$
Preuve : en devoir.

Idée de la preuve, qui répond à la question posée plus haut : on écrit
$$\frac{\bar{X} - \mu}{S/\sqrt{n}} = \frac{\dfrac{\bar{X} - \mu}{\sigma/\sqrt{n}}}{\sqrt{\dfrac{(n-1)S^2/\sigma^2}{n-1}}} = \frac{Z}{\sqrt{Y/(n-1)}},$$
avec $Z \sim N(0, 1)$, $Y = (n-1)S^2/\sigma^2 \sim \chi^2_{n-1}$, et $Z$, $Y$ indépendantes puisque $\bar{X}$ et $S^2$ le sont. Les $\sigma$ se simplifient : c'est exactement la définition de $t_{n-1}$. Sa loi ne dépend ni de $\mu$ ni de $\sigma$, donc $T$ **est** une quantité pivot. [[Complément hors du cours|ⓘ]]

**Notation** : $t_{\alpha,\nu}$, **valeur critique** $t$, est le nombre de l'axe tel que l'aire sous la courbe $t$ à $\nu$ df à droite de $t_{\alpha,\nu}$ vaut $\alpha$.

![[Chp4 Part3 - Inferential statistics - image4.png]]

*Figure : courbe $t_\nu$ centrée en 0, aire ombrée $\alpha$ à droite de $t_{\alpha,\nu}$.*

## Intervalle pour la moyenne : variable gaussienne, variance inconnue

Si $\bar{x}$ et $s$ sont la moyenne et l'écart-type d'un échantillon d'une loi normale de variance inconnue, un intervalle de confiance à $100(1-\alpha)\,\%$ pour $\mu$ est
$$\bar{x} - t_{\alpha/2,\,n-1}\,\frac{s}{\sqrt{n}} \le \mu \le \bar{x} + t_{\alpha/2,\,n-1}\,\frac{s}{\sqrt{n}}$$
où $t_{\alpha/2,n-1}$ est le point de pourcentage supérieur $100\alpha/2$ de la loi $t$ à $n - 1$ df. Voir [[Test t]].

![[Chp4 Part3 - Inferential statistics - image2.png]]

*Figure : courbe $t$ avec la queue droite ombrée au-delà de $t_{\alpha/2}$, d'aire $\alpha/2$.*

Comme $t_{\alpha/2,n-1} > z_{\alpha/2}$, cet intervalle est plus large que celui à $\sigma$ connu : c'est le prix de l'incertitude sur $\sigma$. L'écart s'efface quand $n$ grandit : à 95 %, $t_{0{,}025,9} = 2{,}262$ pour $n = 10$, $t_{0{,}025,29} = 2{,}045$ pour $n = 30$, contre $z_{0{,}025} = 1{,}96$. L'intervalle reste assez fiable pour une population modérément non gaussienne si $n$ n'est pas trop petit, mais pas en présence de forte asymétrie ou de valeurs aberrantes. [[Complément hors du cours|ⓘ]]

### Tableau récapitulatif (échantillon gaussien)

$X_1, \dots, X_n \sim \mathcal{N}(\mu, \sigma^2)$, $\bar{X} = \sum X_i / n$, $S = \sqrt{\sum (X_i - \bar{X})^2/(n-1)}$. Intervalles à $100(1-\alpha)\,\%$, tels qu'écrits sur l'image :

| Hypothèse | Paramètre | Intervalle bilatéral | Intervalle inférieur | Intervalle supérieur |
|---|---|---|---|---|
| $\sigma^2$ connu | $\mu$ | $\bar{X} \pm z_{\alpha/2}\dfrac{\sigma}{\sqrt{n}}$ | $\left(-\infty,\ \bar{X} + z_\alpha\dfrac{\sigma}{\sqrt{n}}\right)$ | $\left(\bar{X} - z_\alpha\dfrac{\sigma}{\sqrt{n}},\ \infty\right)$ [[Erreurs du cours#^e-4-inferential-statistics-3\|✎]] |
| $\sigma^2$ inconnu | $\mu$ | $\bar{X} \pm t_{\alpha/2,n-1}\dfrac{S}{\sqrt{n}}$ | $\left(-\infty,\ \bar{X} + t_{\alpha,n-1}\dfrac{S}{\sqrt{n}}\right)$ | $\left(\bar{X} - t_{\alpha,n-1}\dfrac{S}{\sqrt{n}},\ \infty\right)$ |
| $\mu$ inconnu | $\sigma^2$ | $\left(\dfrac{(n-1)S^2}{\chi^2_{\alpha/2,n-1}},\ \dfrac{(n-1)S^2}{\chi^2_{1-\alpha/2,n-1}}\right)$ | $\left(0,\ \dfrac{(n-1)S^2}{\chi^2_{1-\alpha,n-1}}\right)$ | $\left(\dfrac{(n-1)S^2}{\chi^2_{\alpha,n-1}},\ \infty\right)$ |

Les intervalles unilatéraux utilisent $z_\alpha$ (ou $t_{\alpha,n-1}$, $\chi^2_{\alpha,n-1}$) et non $z_{\alpha/2}$ : tout le risque $\alpha$ est placé dans une seule queue. On s'en sert quand une seule direction compte, par exemple pour garantir qu'une teneur moyenne ne dépasse pas un seuil. [[Complément hors du cours|ⓘ]]

## Intervalle pour une proportion $p$

Rappel (TCL appliqué à une binomiale) : si $n$ est grand,
$$Z = \frac{X - np}{\sqrt{np(1-p)}} = \frac{\hat{P} - p}{\sqrt{p(1-p)/n}}$$
est approximativement normale centrée réduite. Voir [[Approximation normale]].

**Intervalle approché pour une proportion binomiale** : si $\hat{p}$ est la proportion d'observations d'un échantillon de taille $n$ qui appartiennent à une classe d'intérêt, un intervalle approché à $100(1-\alpha)\,\%$ pour la proportion $p$ de la population est
$$\hat{p} - z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}} \le p \le \hat{p} + z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$
où $z_{\alpha/2}$ est le point de pourcentage supérieur $\alpha/2$ de la loi normale centrée réduite.

Cet intervalle s'appelle **intervalle de Wald**. On remplace $p$ par $\hat{p}$ sous la racine parce que $p$ est inconnu. L'approximation n'est fiable que si l'échantillon contient assez de « succès » et d'« échecs » : règle usuelle $n\hat{p} \ge 5$ et $n(1-\hat{p}) \ge 5$ (certains manuels demandent 10). Pour un petit $n$ ou un $p$ proche de 0 ou de 1, son niveau réel est trop faible ; on lui préfère alors l'**intervalle de Wilson** ou l'intervalle exact de Clopper-Pearson. [[Complément hors du cours|ⓘ]]

### Taille d'échantillon pour estimer une proportion

Pour une erreur $E$ donnée :
$$n = \left(\frac{z_{\alpha/2}}{E}\right)^2 p(1-p).$$
$p(1-p)$ est maximal en $p = 0{,}5$, où il vaut $0{,}25$. Le cours conclut qu'« on peut appliquer le TCL tant que $n$ est plus grand que »
$$n = \left(\frac{z_{\alpha/2}}{E}\right)^2 \times 0{,}25.$$

Prendre $p(1-p) = 0{,}25$ est le choix **prudent** quand on n'a aucune idée de $p$ : la taille obtenue garantit l'erreur $E$ quelle que soit la vraie proportion. Si une étude antérieure donne une estimation de $p$, on peut l'utiliser à la place et obtenir un $n$ plus petit. [[Complément hors du cours|ⓘ]]

Application aux sondages : à 95 %, $1{,}96^2 \times 0{,}25 \approx 0{,}96 \approx 1$, donc $n \approx 1/E^2$ et, inversement, la marge d'erreur vaut environ $1/\sqrt{n}$. Un sondage de 1 000 personnes a une marge d'environ $\pm 3$ points ($1{,}96\sqrt{0{,}25/1000} \approx 0{,}031$). Cette marge ne dépend pas de la taille de la population, tant que celle-ci est grande devant l'échantillon, et elle suppose un échantillon aléatoire. [[Complément hors du cours|ⓘ]]
