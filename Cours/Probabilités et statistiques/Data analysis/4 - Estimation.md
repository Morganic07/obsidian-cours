---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 4 : Estimation.docx|Cours 4 - Estimation]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Data analysis (Thanos)/Cours 4 : Estimation.docx|Cours 4 - Estimation]], dans [[Cours/Probabilités et statistiques/Data analysis/_index|Data analysis]].
## Idée générale

Estimer un paramètre de population par un point, puis par un intervalle de confiance, et savoir lire cet intervalle.

## Mode, médiane et moyenne

Voir [[Mesures de tendance centrale]].

- **Mode** : la valeur la plus fréquente.
- **Médiane** : la valeur du milieu (50 % de l'aire de chaque côté).
- **Moyenne** : la valeur moyenne (« *average or norm* »).

![[Séance 4 - Estimation - image1.png]]

*Figure : sur une distribution asymétrique à droite, le mode est au sommet, la médiane partage l'aire en deux moitiés, la moyenne est plus à droite.*

La moyenne est tirée du côté de la queue longue parce qu'elle tient compte de la valeur exacte de chaque observation : quelques très grandes valeurs suffisent à la déplacer. La médiane, qui ne dépend que du rang, y résiste (elle est dite **robuste**). D'où l'ordre habituel mode < médiane < moyenne pour une distribution asymétrique à droite (revenus, prix immobiliers), l'ordre inverse à gauche, et les trois confondus pour une distribution symétrique unimodale comme la [[Loi normale|loi normale]]. C'est pourquoi les revenus se résument plutôt par leur médiane. [[Complément hors du cours|ⓘ]]

## Pourquoi des intervalles plutôt que des points ?

Utiliser une seule valeur (comme la moyenne d'échantillon $\bar{X}$) pour estimer un [[Paramètre et statistique|paramètre de population]] $\mu$ s'appelle une **[[Estimateur|estimation ponctuelle]]**.

Le défaut d'une estimation ponctuelle est qu'elle ne dit rien de sa précision : $\bar{X}$ varie d'un échantillon à l'autre et ne tombe pour ainsi dire jamais exactement sur $\mu$ (pour une variable continue, $P(\bar{X} = \mu) = 0$). L'intervalle ajoute cette information de précision. On distingue l'**estimateur** (la formule, variable aléatoire, comme $\bar{X}$) de l'**estimation** (sa valeur sur l'échantillon observé, comme $\bar{x} = 38\,000$ €). [[Complément hors du cours|ⓘ]]

## Les estimateurs par intervalle de confiance

La largeur de l'[[Intervalle de confiance]] dépend du **niveau de confiance** souhaité : plus l'intervalle est **large**, plus on a **confiance** qu'il contient le vrai paramètre $\mu$.

| Niveau de confiance | Exemple d'intervalle (revenu) | Note |
|---|---|---|
| 100 % | de 0 € à +∞ € | totalement certain, mais inutile |
| 95 % | de 35 000 € à 41 000 € | standard des statisticiens |
| 0 % | 38 000 € | une estimation ponctuelle |

Formule de l'intervalle de confiance bilatéral de niveau $1-\alpha$ pour $\mu$ : [[Erreurs du cours#^e-4-estimation|✎]]

$$\bar{X} \pm Z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$$

**D'où vient la formule.** Si la population est normale, ou si $n$ est assez grand pour appliquer le [[Théorème central limite|théorème central limite]], $\bar{X}$ suit (approximativement) la loi $\mathcal{N}\!\left(\mu, \sigma^2/n\right)$. Sa dispersion autour de $\mu$ est l'**erreur standard** $\sigma/\sqrt{n}$, et la variable centrée réduite $Z = \dfrac{\bar{X} - \mu}{\sigma/\sqrt{n}}$ suit la loi $\mathcal{N}(0,1)$. Par définition de $z_{\alpha/2}$ : [[Complément hors du cours|ⓘ]]
$$P\!\left(-z_{\alpha/2} \le \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \le z_{\alpha/2}\right) = 1 - \alpha \iff P\!\left(\bar{X} - z_{\alpha/2}\frac{\sigma}{\sqrt{n}} \le \mu \le \bar{X} + z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right) = 1 - \alpha$$
La quantité $E = z_{\alpha/2}\,\sigma/\sqrt{n}$ est la **marge d'erreur** : l'intervalle s'écrit « estimation ± marge d'erreur ». [[Complément hors du cours|ⓘ]]

Les valeurs de $z_{\alpha/2}$ à connaître, lues dans la table de la loi normale centrée réduite : [[Complément hors du cours|ⓘ]]

| Niveau de confiance $1-\alpha$ | 90 % | 95 % | 99 % |
|---|---|---|---|
| $z_{\alpha/2}$ | 1,645 | 1,96 | 2,576 |

Exemple : $n = 100$, $\bar{x} = 38\,000$ €, $\sigma = 15\,000$ €. Erreur standard $15\,000/\sqrt{100} = 1\,500$ €, marge à 95 % $1{,}96 \times 1\,500 = 2\,940$ €, d'où l'intervalle $[35\,060 \text{ €} ; 40\,940 \text{ €}]$. [[Complément hors du cours|ⓘ]]

**Note importante** : si $\sigma$ est inconnu, on utilise l'[[Espérance et variance|écart-type]] de l'échantillon $s$, à condition que l'échantillon soit grand : $n \geq 30$.

Pour un petit échantillon ($n < 30$) issu d'une population normale, avec $\sigma$ inconnu, on remplace $z_{\alpha/2}$ par le quantile $t_{\alpha/2,\,n-1}$ de la [[Loi de Student|loi de Student]] à $n-1$ degrés de liberté : $\bar{X} \pm t_{\alpha/2,\,n-1}\,\dfrac{s}{\sqrt{n}}$. Ce quantile est plus grand que $z_{\alpha/2}$ (l'intervalle est plus large, pour payer l'incertitude sur $\sigma$) et s'en rapproche quand $n$ grandit. C'est le cadre du [[Test t|t-test]]. [[Complément hors du cours|ⓘ]]

**Intervalle pour une proportion.** Pour estimer une proportion $p$ (part d'électeurs, taux de défaut) à partir de la fréquence observée $\hat{p}$, l'intervalle de niveau $1-\alpha$ est $\hat{p} \pm z_{\alpha/2}\sqrt{\dfrac{\hat{p}(1-\hat{p})}{n}}$, valable quand $n\hat{p}$ et $n(1-\hat{p})$ sont assez grands (au moins 5 selon la règle usuelle, voir [[Approximation normale]]). C'est le calcul des sondages : avec $n = 1\,000$ et $\hat{p}$ proche de 50 %, la marge à 95 % vaut $1{,}96\sqrt{0{,}25/1\,000} \approx 3$ points. [[Complément hors du cours|ⓘ]]

## Interprétation et application

### 1. L'interprétation correcte

Un intervalle de confiance à 95 % (exemple : 11,01 à 11,99 ans) signifie que **dans 95 échantillons sur 100**, la moyenne de la population se trouverait dans les intervalles construits avec la même procédure.

**Erreur à éviter** : il est incorrect de dire qu'il y a 95 % de chances que la moyenne « tombe » dans cet intervalle précis, car $\mu$ est une valeur **fixe**, pas une variable aléatoire.

Ce qui est aléatoire, ce sont les bornes : avant le tirage, l'intervalle $\bar{X} \pm 1{,}96\,\sigma/\sqrt{n}$ a 95 % de chances de contenir $\mu$ ; une fois l'échantillon tiré, l'intervalle calculé contient $\mu$ ou ne le contient pas, sans qu'on sache lequel. Le 95 % qualifie la **méthode**, pas un intervalle particulier. [[Complément hors du cours|ⓘ]]

### 2. Comment réduire la largeur d'un intervalle ?

Pour un intervalle plus étroit (plus précis) sans diminuer la confiance :

1. **augmenter la taille de l'échantillon $n$** : on divise par $\sqrt{n}$, donc un $n$ plus grand réduit l'erreur ;
2. **réduire la variabilité**, par des procédures d'[[Échantillonnage|échantillonnage]] plus efficaces comme la **stratification**.

Comme la largeur varie en $1/\sqrt{n}$, diviser la marge d'erreur par 2 demande un échantillon **4 fois** plus grand. En renversant la formule, la taille d'échantillon nécessaire pour une marge $E$ donnée est $n = \left(\dfrac{z_{\alpha/2}\,\sigma}{E}\right)^2$, arrondie à l'entier supérieur. Exemple : $\sigma = 15\,000$ €, marge voulue 1 000 € à 95 % : $n = (1{,}96 \times 15)^2 \approx 864{,}4$, soit 865 personnes. [[Complément hors du cours|ⓘ]]

La stratification consiste à découper la population en sous-groupes homogènes (strates : âge, région…) et à tirer un échantillon dans chacun ; la variabilité restante est surtout celle à l'intérieur des strates, plus faible que la variabilité totale. [[Complément hors du cours|ⓘ]]

## Percentiles et valeurs Z

Un **[[Quantile|percentile]]** est une valeur de la distribution en dessous de laquelle se trouve un certain pourcentage de la population. Formule :

$$X = \mu + Z \cdot \sigma$$

Voir [[Centrage et réduction]] et [[Loi normale]].

La formule renverse le centrage-réduction $Z = \dfrac{X - \mu}{\sigma}$ : on lit dans la table la valeur $z$ qui laisse le pourcentage voulu à sa gauche, puis on revient à l'échelle d'origine. Exemple : pour une loi normale de moyenne 100 et d'écart-type 15, le 95ᵉ percentile vaut $100 + 1{,}645 \times 15 \approx 124{,}7$ ($z = 1{,}645$ laisse 95 % de l'aire à gauche). Repères : le 50ᵉ percentile est la médiane ($z = 0$), les 25ᵉ et 75ᵉ sont les quartiles ($z \approx \pm 0{,}674$). [[Complément hors du cours|ⓘ]]

## Points clés à retenir

- Dès qu'on travaille sur un échantillon, la certitude à 100 % est impossible.
- Pour une certitude absolue, il faut un **recensement** (étudier toute la population).
- Le niveau de confiance standard est **95 %**.
- $s^2$ est un **estimateur sans biais** de $\sigma^2$ ([[Variance et écart-type d'échantillon]]).
- Sans biais signifie que $E(s^2) = \sigma^2$ : en moyenne sur tous les échantillons possibles, l'estimateur tombe juste. C'est pourquoi on divise par $n-1$ : $s^2 = \dfrac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2$. Les écarts sont mesurés à $\bar{x}$, qui est par construction plus proche des données que $\mu$ ; diviser par $n$ sous-estimerait $\sigma^2$ d'un facteur $\frac{n-1}{n}$. En revanche, $s$ n'est pas un estimateur sans biais de $\sigma$ (il le sous-estime légèrement). [[Complément hors du cours|ⓘ]]
