---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 9 : Covariance and Correlation.docx|Cours 9 - Covariance and Correlation]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 3/Data analysis (Thanos)/Cours 9 : Covariance and Correlation.docx|Cours 9 - Covariance and Correlation]], dans [[Data analysis (index)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Mesurer la relation linéaire entre deux variables : covariance, corrélation de Pearson, coefficient de détermination, puis les corrélations de rang de Spearman et de Kendall.

## Modèles mathématiques

Voir [[Modèle déterministe et probabiliste]].

- **Modèles déterministes** : ils supposent des relations **exactes** ; adaptés quand l'erreur de prédiction est négligeable. Exemple : la force est exactement la masse fois l'accélération, $F = m \cdot a$.
- **Modèles probabilistes** : ils supposent **deux** composantes, (i) déterministe et (ii) erreur aléatoire. Exemple : le volume des ventes $y$ vaut 10 fois les dépenses de publicité $x$, plus une erreur aléatoire : $y = 10x + \varepsilon$ ; l'erreur peut venir d'autres facteurs que la publicité.

Les modèles probabilistes se divisent en **modèles de régression** et **modèles de corrélation**.

![[Séance 9 - Covariance and Correlation - image13.png]]

*Figure : les modèles probabilistes, divisés en modèles de régression et de corrélation.*

## Corrélation linéaire

- Dans ce cours, on mesure la corrélation d'une relation **linéaire** entre deux variables aléatoires.
- Corrélation linéaire = les variables sont liées.
- Mais une corrélation linéaire **n'implique pas** une relation de cause à effet ([[Corrélation et causalité]]).

## Loi conjointe et lois marginales

Voir [[Loi conjointe]].

**Définition** : soient $X$ et $Y$ deux variables aléatoires discrètes définies sur l'espace $\mathcal{S}$ d'une expérience. La **fonction de masse conjointe** (*joint pmf*) $p(x, y)$ est définie pour chaque couple $(x, y)$ par

$$p(x, y) = P(X = x \text{ et } Y = y)$$

Une fonction $p(x,y)$ est une pmf conjointe si (i) $p(x,y) \geq 0$ pour tous $x, y$ et (ii) $\sum_{x,y} p(x,y) = 1$. Pour un événement $A$ de $S \times S$ :

$$P((X,Y) \in A) = \sum_{(x,y) \in A} p(x,y)$$

**Définition** : les **fonctions de masse marginales** de $X$ et $Y$ sont

$$p_X(x) = \sum_y p(x, y) \qquad p_Y(y) = \sum_x p(x, y)$$

**Définition** : $X$ et $Y$ sont **indépendantes** si, pour tout couple $(x, y)$, $p(x, y) = p_X(x) \cdot p_Y(y)$ (cas discret). Si la pmf conjointe **ne s'écrit pas** comme le **produit des marginales**, les variables sont **dépendantes** ([[Indépendance de variables aléatoires]]).

## Espérance

Soient $X$ et $Y$ de pmf conjointe $p(x,y)$. L'[[Espérance et variance|espérance]] d'une fonction $h(X,Y)$, notée $E[h(X,Y)]$ ou $\mu_{h(X,Y)}$, est

$$E[h(X,Y)] = \sum_{x,y} h(x,y) \cdot p(x,y)$$

**Linéarité de l'espérance** : pour toutes fonctions $h_1$, $h_2$ et constantes $a_1$, $a_2$, $b$,

$$E[a_1 h_1(X,Y) + a_2 h_2(X,Y) + b] = a_1 E[h_1(X,Y)] + a_2 E[h_2(X,Y)] + b$$

**Théorème** : si $X$ et $Y$ sont **indépendantes** et $h(X,Y) = g_1(X) \cdot g_2(Y)$, alors

$$E[g_1(X) \cdot g_2(Y)] = E[g_1(X)] \cdot E[g_2(Y)]$$

## Point important : l'outil ne révèle que la LINÉARITÉ

**Proposition** :

1. Si $X$ et $Y$ sont indépendantes, alors $\rho = 0$ ; mais $\rho = 0$ **n'implique pas** l'indépendance (annotations de l'étudiant : flèche ⇒ sur « then », flèche ⇒ barrée sur « does »).
2. $\rho = 1$ ou $-1$ si et seulement si $Y = aX + b$ pour des nombres $a$ et $b$ avec $a \neq 0$.

$\rho$ mesure donc le **degré de relation linéaire** entre $X$ et $Y$, et ne dit rien d'une éventuelle relation **non linéaire**. Si $\rho = 0$, cela **n'implique pas** que $X$ et $Y$ sont indépendantes, seulement qu'il n'y a **pas de relation linéaire** ; il peut y avoir une forte relation non linéaire. Des variables de corrélation nulle sont dites **non corrélées** (*uncorrelated*).

**Proposition** : $X$ et $Y$ sont non corrélées si et seulement si $E[XY] = \mu_X \cdot \mu_Y$.

## Covariance

Voir [[Covariance et corrélation]].

La covariance indique si deux variables évoluent dans le même sens ou non :

- **positive** : les deux augmentent ensemble (plus il fait chaud, plus on vend de glaces) ;
- **négative** : l'une augmente quand l'autre diminue (plus il fait chaud, moins on vend de radiateurs) ;
- **zéro** : pas de relation linéaire évidente.

**Le problème** : sa valeur dépend des unités (mètres, kilos, euros). La covariance taille-poids en centimètres donne un chiffre énorme, en mètres un chiffre minuscule : impossible de dire si une covariance de « 50 » est forte ou faible.

**Définition** : quand $X$ et $Y$ ne sont **pas indépendantes**, on veut savoir **à quel point** elles sont liées. La **covariance** est

$$\text{Cov}(X,Y) = E[(X-\mu_X)(Y-\mu_Y)] = \sum_x \sum_y (x-\mu_X)(y-\mu_Y)p(x,y)$$

Covariance d'échantillon :

$$\text{cov}(x,y) = \frac{\sum_{i=1}^{n}(x_i - \bar{X})(y_i - \bar{Y})}{n-1}$$

**Proposition** : pour toutes variables $X$, $Y$ :

1. $\mathrm{Cov}(X, Y) = \mathrm{Cov}(Y, X)$ ;
2. $\mathrm{Cov}(X, X) = \mathrm{Var}(X)$ ;
3. formule raccourcie : $\mathrm{Cov}(X, Y) = E(XY) - \mu_X \cdot \mu_Y$ ;
4. distributivité : pour toute variable $Z$ et constantes $a, b, c$,
$$\mathrm{Cov}(aX + bY + c, Z) = a\,\mathrm{Cov}(X, Z) + b\,\mathrm{Cov}(Y, Z)$$

## Corrélation et coefficient d'échantillon (Pearson)

### Le paramètre ρ

La corrélation est une covariance « normalisée » : on divise la covariance par les écarts-types pour obtenir un score pur, **sans unité**, « compris strictement entre −1 et 1 » (selon la note, voir Points à vérifier) :

- **1** : relation positive parfaite (droite qui monte) ;
- **−1** : relation négative parfaite (droite qui descend) ;
- **0** : aucune relation.

Peu importe les unités : une corrélation de **0,9** signifie toujours une relation très forte.

**Définition** : le **coefficient de corrélation** de $X$ et $Y$, noté $\text{Corr}(X, Y)$, $\rho_{X,Y}$ ou $\rho$, est

$$\rho_{X,Y} = \frac{\text{Cov}(X, Y)}{\sigma_X \cdot \sigma_Y}$$

**Proposition** : pour toutes variables $X$, $Y$ :

1. $\mathrm{Corr}(X, Y) = \mathrm{Corr}(Y, X)$ ;
2. $\mathrm{Corr}(X, X) = 1$ ;
3. invariance d'échelle : si $a, b, c, d$ sont des constantes avec $ac > 0$, $\mathrm{Corr}(aX + b, cY + d) = \mathrm{Corr}(X, Y)$ ;
4. $-1 \leq \mathrm{Corr}(X, Y) \leq 1$.

*Corrélation linéaire* : si les valeurs de deux variables corrélées **varient à un taux constant** l'une par rapport à l'autre, elles ont une corrélation linéaire.

### L'estimateur r

- $r$, le coefficient de corrélation **d'échantillon**, est une **estimation** du coefficient de la population $\rho$ ([[Estimateur]]).
- On ne peut calculer $\rho$ qu'en recensant toute la population.

**Définition** : pour les couples $(x_i, y_i)$, $i = 1, \ldots, n$, avec $s_x$ et $s_y$ les écarts-types d'échantillon :

$$r = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{(n-1)\, s_x s_y} = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^2 \sum_{i=1}^{n} (y_i - \bar{y})^2}}$$

Si $r > 0$, les données sont *positivement corrélées* ; si $r < 0$, *négativement corrélées*.

Le coefficient de Pearson est une covariance standardisée (sans unité) :

$$r = \frac{\text{cov}(x, y)}{\sqrt{\text{var } x}\,\sqrt{\text{var } y}} = \frac{SS_{xy}}{\sqrt{SS_{xx} SS_{yy}}}$$

$$SS_{xx} = \sum x^2 - \frac{(\sum x)^2}{n} \qquad SS_{yy} = \sum y^2 - \frac{(\sum y)^2}{n} \qquad SS_{xy} = \sum xy - \frac{(\sum x)(\sum y)}{n}$$

![[Séance 9 - Covariance and Correlation - image25.png]]

*Figure : six nuages de points avec leur coefficient : $r = -1$, $-0{,}6$, $0$ (nuage dispersé), $+1$, $+0{,}3$, $0$ (points alignés sur une horizontale).*

## Coefficient de détermination R² et r²

Voir [[Coefficient de détermination]].

- Le coefficient de détermination $R^2$ va de **0 à 1** (0 % à 100 %) et **mesure la part de la variation de Y expliquée par X**.
- $R^2$ est égal à $r^2$, le **carré du coefficient de corrélation**.
- En **corrélation**, on ne se soucie pas de savoir qui est X et qui est Y : on ne cherche pas à prédire Y à partir de X.
- En **[[Régression linéaire|régression]]**, on cherche une équation reliant X à Y : il **faut préciser** quelle variable est Y (dépendante) et laquelle est X (indépendante). Le coefficient de corrélation est le même quel que soit le choix, mais **l'équation de régression change** si l'on inverse X et Y.

$$r^2 = (\text{coefficient de corrélation})^2 = \frac{\text{variation expliquée}}{\text{variation totale}} = \frac{SS_{yy} - SSE}{SS_{yy}}$$

- Si tous les points sont sur la droite, $r = 1$ (ou $-1$ pour une relation inverse) et $r^2 = 100\,\%$ : toute la variation de Y est expliquée par X, il n'y a **aucune variation inexpliquée**.
- $r = 0{,}30$ (ou $-0{,}30$) : $r^2 = 0{,}09$, 9 % expliqués, 91 % inexpliqués → corrélation **faible**, même si elle est significative.
- $r = 0{,}50$ : $r^2 = 0{,}25$, 25 % expliqués, 75 % inexpliqués → **modérée**.
- $r = 0{,}90$ : $r^2 = 0{,}81$, 81 % expliqués, 19 % inexpliqués → **très forte**.

## Coefficient de corrélation de Spearman

Voir [[Coefficient de corrélation de Spearman]].

- Le $\rho$ de Spearman (d'après Charles Spearman) est une **mesure non paramétrique de corrélation de rang** (dépendance statistique entre les classements de deux variables).
- Il évalue à quel point la relation entre deux variables peut être décrite par une **fonction monotone**.
- À retenir : il évalue une relation monotone entre deux variables **continues ou ordinales**, et **repose sur les rangs** de chaque variable plutôt que sur les données brutes.

![[Séance 9 - Covariance and Correlation - image10.png]]

*Figure : une fonction monotone croissante, une fonction monotone décroissante, et une fonction non monotone.*

Deux méthodes de calcul selon que :

1. les données **n'ont pas de rangs ex æquo** :
$$\rho = 1 - \frac{6\sum d_i^2}{n(n^2 - 1)}$$
avec $d_i$ la différence des rangs appariés et $n$ le nombre de cas ;
2. les données **ont des rangs ex æquo** (formule de Pearson appliquée aux rangs) :
$$\rho = \frac{\sum_i (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_i (x_i - \bar{x})^2 \sum_i (y_i - \bar{y})^2}}$$

**Hypothèses** : paires d'observations indépendantes ; variables mesurées sur une échelle ordinale, d'intervalle ou de ratio ; relation monotone entre les deux variables.

### Observations ex æquo (*tied observations*)

- Le terme *tie* s'emploie pour les statistiques de rang.
- Des **observations ex æquo** ont la même valeur, ce qui empêche de leur donner un rang unique.
- Solution : on leur attribue la **moyenne de leurs rangs hypothétiques**.

| Valeur | Rang sans traitement | Rang avec ex æquo |
|---|---|---|
| −2,0 | 1 | 1 |
| −1,0 | 2 | 2 |
| 1,0 | 3 | 3 |
| 2,2 | 4 | 5 |
| 2,2 | 5 | 5 |
| 2,2 | 6 | 5 |
| 5,3 | 7 | 7,5 |
| 5,3 | 8 | 7,5 |
| 7,0 | 9 | 9 |
| 8,1 | 10 | 10 |
| 8,2 | 11 | 11 |

## Pearson contre Spearman

1. Différence fondamentale : le coefficient de **Pearson** travaille avec une relation **linéaire**, celui de **Spearman** aussi avec des relations **monotones**.
2. **Pearson** utilise les **valeurs brutes**, **Spearman** les **rangs**.

- Si un nuage de points suggère une relation « peut-être monotone, peut-être linéaire », mieux vaut utiliser Spearman.
- Passer à Spearman ne fait aucun mal même si les données sont parfaitement linéaires.
- Mais si elles ne le sont pas exactement et qu'on utilise Pearson, on perd l'information que Spearman aurait captée.

![[Séance 9 - Covariance and Correlation - image6.png]]

*Figure : cinq nuages de points et leurs coefficients de Pearson et de Spearman.*

| Relation | Pearson | Spearman |
|---|---|---|
| droite croissante | +1 | +1 |
| monotone croissante (courbe en S) | +0,851 | +1 (« exactement 1 ») |
| sans tendance | −0,093 | −0,093 |
| droite décroissante | −1 | −1 |
| monotone décroissante | −0,799 | −1 (la diapositive écrit « exactly 1 », voir Points à vérifier) |

**Note** : aucun des deux coefficients ne capte d'autres relations non linéaires. Si le nuage montre une relation ni linéaire ni monotone, il ne faut utiliser aucun des deux pour mesurer la force de la relation.

## Coefficient tau de Kendall (corrélation de rang de Kendall)

Voir [[Tau de Kendall]].

### Quand l'utiliser

- La corrélation de rang de Kendall (**non paramétrique**) remplace celle de Pearson (paramétrique) **quand les données ne respectent pas une ou plusieurs hypothèses** de ce test.
- C'est aussi la meilleure alternative à Spearman **quand l'échantillon est petit** et **contient beaucoup d'ex æquo**.
- Elle teste la similarité de l'ordre des données classées.
- Les autres coefficients partent des observations ; celui de Kendall **utilise des paires d'observations** et mesure la force de l'association d'après la **concordance et la discordance** des paires.
- Le $\tau$ de Kendall a en général des valeurs **plus petites** que le $\rho$ de Spearman. Il est peu sensible aux erreurs, et ses p-values sont plus précises avec de petits échantillons.

### Comment l'utiliser

- **Paire concordante** : ordonnée de la même façon ; $(x_2 - x_1)$ et $(y_2 - y_1)$ ont le **même signe**.
- **Paire discordante** : ordonnée différemment ; $(x_2 - x_1)$ et $(y_2 - y_1)$ ont des **signes opposés**.

(Le cours ne donne pas la formule de $\tau$.)

## Résumé

Méthodes d'analyse de corrélation :

- **Corrélation de Pearson** ($r$) : mesure une dépendance **linéaire** entre $x$ et $y$. Test de corrélation **paramétrique**, car il dépend de la distribution des données ; selon le cours, il ne s'utilise que si $x$ et $y$ suivent des [[Loi normale|lois normales]]. Le tracé de $y = f(x)$ s'appelle la courbe de régression linéaire.
- **$\tau$ de Kendall et $\rho$ de Spearman** : coefficients fondés sur les **rangs** (non paramétriques) ([[Test paramétrique et non paramétrique]]).

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **« Spearman is exactly 1 » pour la relation décroissante** : image lue directement. La diapositive écrit bien « Spearman = −1 » sur la ligne puis « Spearman is exactly 1 » dans le commentaire. Il faut lire $-1$ (complément). Alerte de la transcription confirmée.
2. **« Compris strictement entre −1 et 1 »** : la note de commentaire du cours l'écrit, alors que $\pm 1$ sont atteints (relations parfaites) et que la proposition donne $-1 \le \mathrm{Corr} \le 1$. Il faut lire « entre $-1$ et $1$ » (complément).
3. **« $R^2 = r^2$ »** : vrai pour une régression linéaire simple. Avec plusieurs variables explicatives, $R^2$ n'est plus le carré d'un seul coefficient (complément, voir [[11 - Multiple Linear Regression and F-statistic (résumé)|Cours 11]]).
4. **Covariance d'échantillon à $n-1$** : l'image donne $\dfrac{\sum(x_i - \bar{X})(y_i - \bar{Y})}{n-1}$, alors que la covariance de population (définition) utilise l'espérance. Les deux sont présentées sans les distinguer.
5. **Images non ouvertes** : toutes, sauf celle du comparatif Pearson/Spearman. Les formules sont reprises des transcriptions, sans écart apparent avec les formules usuelles.
