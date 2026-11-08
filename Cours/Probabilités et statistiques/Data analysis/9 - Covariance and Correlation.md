---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 9 : Covariance and Correlation.docx|Cours 9 - Covariance and Correlation]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Data analysis (Thanos)/Cours 9 : Covariance and Correlation.docx|Cours 9 - Covariance and Correlation]], dans [[Cours/Probabilités et statistiques/Data analysis/_index|Data analysis]].
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
- Trois raisons classiques à une corrélation sans causalité directe : une **variable confondante** qui agit sur les deux (les ventes de glaces et les noyades montent ensemble parce que toutes deux dépendent de la chaleur), une **causalité inverse** (c'est $Y$ qui agit sur $X$), ou le **hasard** quand on teste beaucoup de couples de variables. Une corrélation peut même s'inverser quand on sépare les données en groupes : c'est le [[Paradoxe de Simpson]]. [[Complément hors du cours|ⓘ]]

## Loi conjointe et lois marginales

Voir [[Loi conjointe]].

**Définition** : soient $X$ et $Y$ deux variables aléatoires discrètes définies sur l'espace $\mathcal{S}$ d'une expérience. La **fonction de masse conjointe** (*joint pmf*) $p(x, y)$ est définie pour chaque couple $(x, y)$ par

$$p(x, y) = P(X = x \text{ et } Y = y)$$

Une fonction $p(x,y)$ est une pmf conjointe si (i) $p(x,y) \geq 0$ pour tous $x, y$ et (ii) $\sum_{x,y} p(x,y) = 1$. Pour un événement $A$ de $S \times S$ :

$$P((X,Y) \in A) = \sum_{(x,y) \in A} p(x,y)$$

**Définition** : les **fonctions de masse marginales** de $X$ et $Y$ sont

$$p_X(x) = \sum_y p(x, y) \qquad p_Y(y) = \sum_x p(x, y)$$

**Définition** : $X$ et $Y$ sont **indépendantes** si, pour tout couple $(x, y)$, $p(x, y) = p_X(x) \cdot p_Y(y)$ (cas discret). Si la pmf conjointe **ne s'écrit pas** comme le **produit des marginales**, les variables sont **dépendantes** ([[Indépendance de variables aléatoires]]).

Pour des variables **continues**, on remplace la pmf par une **densité conjointe** $f(x, y) \geq 0$, d'intégrale totale égale à 1, et les sommes par des intégrales : $P((X,Y) \in A) = \iint_A f(x,y)\,dx\,dy$, $f_X(x) = \int f(x,y)\,dy$, et l'indépendance s'écrit $f(x,y) = f_X(x) f_Y(y)$. [[Complément hors du cours|ⓘ]]

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

Pourquoi l'indépendance donne $\rho = 0$ : le théorème de la section précédente, avec $g_1(X) = X$ et $g_2(Y) = Y$, donne $E[XY] = \mu_X \mu_Y$, donc $\mathrm{Cov}(X,Y) = E[XY] - \mu_X\mu_Y = 0$ (formule raccourcie ci-dessous), donc $\rho = 0$. [[Complément hors du cours|ⓘ]]

Contre-exemple classique de la réciproque : $X$ prend les valeurs $-1$, $0$, $1$ avec probabilité $1/3$ chacune, et $Y = X^2$. $Y$ dépend entièrement de $X$, mais $\mu_X = 0$ et $E[XY] = E[X^3] = \frac{-1 + 0 + 1}{3} = 0$, donc $\mathrm{Cov}(X,Y) = 0$ : les variables sont non corrélées sans être indépendantes (la relation est une parabole, pas une droite). [[Complément hors du cours|ⓘ]]

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

On divise par $n-1$ et non par $n$ pour la même raison que dans la [[Variance et écart-type d'échantillon|variance d'échantillon]] : les écarts sont pris par rapport à $\bar X$ et $\bar Y$, eux-mêmes estimés sur les données, ce qui fait perdre un degré de liberté ; avec $n - 1$, l'estimateur est sans biais. [[Complément hors du cours|ⓘ]]

Lecture du signe : chaque terme $(x_i - \bar X)(y_i - \bar Y)$ est positif quand le point est en haut à droite ou en bas à gauche du point moyen $(\bar X, \bar Y)$, négatif dans les deux autres quadrants. La covariance est positive quand les premiers l'emportent. [[Complément hors du cours|ⓘ]]

**Proposition** : pour toutes variables $X$, $Y$ :

1. $\mathrm{Cov}(X, Y) = \mathrm{Cov}(Y, X)$ ;
2. $\mathrm{Cov}(X, X) = \mathrm{Var}(X)$ ;
3. formule raccourcie : $\mathrm{Cov}(X, Y) = E(XY) - \mu_X \cdot \mu_Y$ ;
4. distributivité : pour toute variable $Z$ et constantes $a, b, c$,
$$\mathrm{Cov}(aX + bY + c, Z) = a\,\mathrm{Cov}(X, Z) + b\,\mathrm{Cov}(Y, Z)$$

La formule raccourcie s'obtient en développant : $E[(X-\mu_X)(Y-\mu_Y)] = E[XY] - \mu_X E[Y] - \mu_Y E[X] + \mu_X\mu_Y = E[XY] - \mu_X\mu_Y$, par linéarité de l'espérance. [[Complément hors du cours|ⓘ]]

Conséquence importante, la **variance d'une somme** : $\mathrm{Var}(aX + bY) = a^2\,\mathrm{Var}(X) + b^2\,\mathrm{Var}(Y) + 2ab\,\mathrm{Cov}(X, Y)$. En particulier $\mathrm{Var}(X + Y) = \mathrm{Var}(X) + \mathrm{Var}(Y)$ seulement si $X$ et $Y$ sont non corrélées (par exemple indépendantes). C'est la base de la diversification en finance : deux placements de covariance négative ont une somme moins variable que chacun pris seul. [[Complément hors du cours|ⓘ]]

Pour plusieurs variables, on range toutes les variances et covariances dans la [[Matrice de covariance]] (variances sur la diagonale) ; en divisant chaque covariance par le produit des écarts-types, on obtient la **matrice de corrélation**, de diagonale 1, utilisée par exemple en [[Analyse en composantes principales]]. [[Complément hors du cours|ⓘ]]

## Corrélation et coefficient d'échantillon (Pearson)

### Le paramètre ρ

La corrélation est une covariance « normalisée » : on divise la covariance par les écarts-types pour obtenir un score pur, **sans unité**, compris entre −1 et 1, bornes comprises : [[Erreurs du cours#^e-9-covariance-and-correlation|✎]]

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

Si $ac < 0$, le signe s'inverse : $\mathrm{Corr}(aX + b, cY + d) = -\mathrm{Corr}(X, Y)$. C'est ce qui rend la corrélation indépendante des unités : passer des centimètres aux mètres ou des degrés Celsius aux degrés Fahrenheit ne la change pas. [[Complément hors du cours|ⓘ]]

Pourquoi $|\rho| \leq 1$ : c'est l'[[Inégalité de Cauchy-Schwarz]] appliquée aux variables centrées, $|E[(X-\mu_X)(Y-\mu_Y)]| \leq \sqrt{E[(X-\mu_X)^2]\,E[(Y-\mu_Y)^2]} = \sigma_X\sigma_Y$, avec égalité si et seulement si $Y - \mu_Y$ est proportionnelle à $X - \mu_X$, c'est-à-dire $Y = aX + b$. Géométriquement, $r$ est le cosinus de l'angle entre les vecteurs centrés $(x_i - \bar x)_i$ et $(y_i - \bar y)_i$. [[Complément hors du cours|ⓘ]]

Exemple de calcul à partir d'une pmf conjointe : $X$ et $Y$ valent 0 ou 1, avec $p(0,0) = p(1,1) = 0{,}4$ et $p(0,1) = p(1,0) = 0{,}1$. Les marginales donnent $\mu_X = \mu_Y = 0{,}5$ et $\sigma_X^2 = \sigma_Y^2 = 0{,}5 - 0{,}5^2 = 0{,}25$. Seul le couple $(1,1)$ compte dans $E[XY] = 0{,}4$, d'où $\mathrm{Cov}(X,Y) = 0{,}4 - 0{,}25 = 0{,}15$ et $\rho = \frac{0{,}15}{0{,}5 \times 0{,}5} = 0{,}6$ : les variables sont dépendantes ($p(0,0) = 0{,}4 \neq p_X(0)p_Y(0) = 0{,}25$) et positivement corrélées. [[Complément hors du cours|ⓘ]]

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

*Figure : six nuages de points avec leur coefficient : $r = -1$, $-0{,}6$, $0$ (nuage dispersé), $+1$, $+0{,}3$, et $r$ non défini (points alignés sur une horizontale).* [[Erreurs du cours#^e-9-covariance-and-correlation|✎]]

Dans le dernier cas, $Y$ est constant : $s_y = 0$ et la formule de $r$ divise par zéro ; il n'y a de toute façon aucune covariation. [[Complément hors du cours|ⓘ]]

**Tester si la corrélation est significative.** Un $r$ non nul peut venir du hasard de l'échantillon. Pour tester $H_0 : \rho = 0$ contre $H_1 : \rho \neq 0$, quand les couples sont tirés d'une loi normale bivariée, on utilise la statistique $t = \dfrac{r\sqrt{n-2}}{\sqrt{1-r^2}}$, qui suit sous $H_0$ une [[Loi de Student]] à $n - 2$ degrés de liberté ([[Test t]]). Avec un grand échantillon, une corrélation faible peut être significative : significativité et force de la relation sont deux questions différentes (voir $r^2$ ci-dessous). [[Complément hors du cours|ⓘ]]

**Sensibilité aux valeurs extrêmes.** Comme $r$ repose sur des écarts à la moyenne, un seul [[Quartiles et valeurs aberrantes|point aberrant]] peut créer ou masquer une forte corrélation ; le [[Quatuor d'Anscombe]] montre quatre nuages très différents de même $r = 0{,}816$. D'où la règle : toujours regarder le nuage de points avant d'interpréter $r$. Les coefficients de rang (Spearman, Kendall) sont beaucoup moins sensibles à ces points. [[Complément hors du cours|ⓘ]]

## Coefficient de détermination R² et r²

Voir [[Coefficient de détermination]].

- Le coefficient de détermination $R^2$ va de **0 à 1** (0 % à 100 %) et **mesure la part de la variation de Y expliquée par X**.
- $R^2$ est égal à $r^2$, le **carré du coefficient de corrélation**.
- En **corrélation**, on ne se soucie pas de savoir qui est X et qui est Y : on ne cherche pas à prédire Y à partir de X.
- En **[[Régression linéaire|régression]]**, on cherche une équation reliant X à Y : il **faut préciser** quelle variable est Y (dépendante) et laquelle est X (indépendante). Le coefficient de corrélation est le même quel que soit le choix, mais **l'équation de régression change** si l'on inverse X et Y.

$$r^2 = (\text{coefficient de corrélation})^2 = \frac{\text{variation expliquée}}{\text{variation totale}} = \frac{SS_{yy} - SSE}{SS_{yy}}$$

Dans cette formule, $SS_{yy} = \sum (y_i - \bar y)^2$ est la variation totale de $Y$ autour de sa moyenne, et $SSE = \sum (y_i - \hat y_i)^2$ (*sum of squared errors*) la variation qui reste autour de la droite de [[Régression linéaire|régression]], c'est-à-dire la somme des carrés des [[Résidu (régression)|résidus]]. $SS_{yy} - SSE$ est donc la part que la droite explique. L'égalité $R^2 = r^2$ vaut pour la régression linéaire **simple** (une seule variable explicative). [[Complément hors du cours|ⓘ]]

Lien avec la pente : la droite des moindres carrés de $Y$ en $X$ a pour pente $b_1 = r\,\dfrac{s_y}{s_x}$. La pente a donc toujours le signe de $r$, mais sa valeur dépend des unités, alors que $r$ n'en dépend pas. [[Complément hors du cours|ⓘ]]

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

Dans la seconde formule, $x_i$ et $y_i$ désignent les **rangs**, pas les valeurs brutes. Sans ex æquo, les deux formules donnent exactement le même résultat : la première n'est qu'un raccourci de calcul. [[Complément hors du cours|ⓘ]]

Exemple sans ex æquo : cinq candidats classés par deux jurys, rangs $X = (1, 2, 3, 4, 5)$ et $Y = (2, 1, 4, 3, 5)$. Les différences sont $d = (-1, 1, -1, 1, 0)$, d'où $\sum d_i^2 = 4$ et $\rho = 1 - \frac{6 \times 4}{5(25 - 1)} = 1 - 0{,}2 = 0{,}8$ : les deux classements concordent fortement. [[Complément hors du cours|ⓘ]]

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
| monotone décroissante | −0,799 | −1 (« exactement −1 ») [[Erreurs du cours#^e-9-covariance-and-correlation\|✎]] |

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

Formule de base, sans ex æquo : avec $n_c$ paires concordantes et $n_d$ paires discordantes parmi les $\binom{n}{2} = \frac{n(n-1)}{2}$ paires possibles, [[Complément hors du cours|ⓘ]]

$$\tau = \frac{n_c - n_d}{n(n-1)/2}$$

$\tau$ vaut 1 si toutes les paires sont concordantes, $-1$ si toutes sont discordantes, et s'interprète directement : c'est la différence entre la probabilité qu'une paire soit concordante et celle qu'elle soit discordante. Avec des ex æquo, on utilise une version corrigée, le $\tau_b$, qui retire du dénominateur les paires ex æquo sur $X$ ou sur $Y$. [[Complément hors du cours|ⓘ]]

Sur l'exemple des deux jurys ci-dessus ($Y = (2, 1, 4, 3, 5)$), seules les paires de candidats (1, 2) et (3, 4) sont discordantes : $n_c = 8$, $n_d = 2$ sur 10 paires, donc $\tau = \frac{8 - 2}{10} = 0{,}6$, plus petit que le $\rho$ de Spearman de 0,8, comme l'annonce le cours. [[Complément hors du cours|ⓘ]]

## Résumé

Méthodes d'analyse de corrélation :

- **Corrélation de Pearson** ($r$) : mesure une dépendance **linéaire** entre $x$ et $y$. Test de corrélation **paramétrique**, car son test de significativité suppose que $x$ et $y$ suivent des [[Loi normale|lois normales]]. [[Erreurs du cours#^e-9-covariance-and-correlation|✎]] Le tracé de $y = f(x)$ s'appelle la courbe de régression linéaire.
- **$\tau$ de Kendall et $\rho$ de Spearman** : coefficients fondés sur les **rangs** (non paramétriques) ([[Test paramétrique et non paramétrique]]).

Précision sur l'hypothèse de normalité : le **calcul** de $r$ ne suppose aucune loi, il décrit toujours le degré de liaison linéaire de l'échantillon. La normalité (bivariée) n'est requise que pour le **test** de significativité de $r$ et ses intervalles de confiance. En R, les trois coefficients se calculent avec `cor(x, y, method = "pearson")` (ou `"spearman"`, `"kendall"`), et le test avec `cor.test()`. [[Complément hors du cours|ⓘ]]
