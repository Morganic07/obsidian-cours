---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 12 : ANOVA and F-statistic .docx|Cours 12 - ANOVA and F-statistic]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Data analysis (Thanos)/Cours 12 : ANOVA and F-statistic .docx|Cours 12 - ANOVA and F-statistic]], dans [[Cours/Probabilités et statistiques/Data analysis/_index|Data analysis]].
## Idée générale

L'[[ANOVA]] teste si trois populations ou plus ont la même moyenne, en comparant la variation entre groupes à la variation dans les groupes. Sa statistique est la [[Statistique F]]. Le cours finit en reliant l'ANOVA à la régression simple.

## Introduction à l'ANOVA (*ANalysis Of VAriance*)

- Technique statistique pour tester si **trois moyennes de population ou plus** sont toutes égales.
  - **ANOVA à un facteur** (*one-way*) : comparer 3 groupes ou plus sur 1 variable.
  - **ANOVA à deux facteurs** (*two-way*) : comparer 3 groupes ou plus sur 2 variables.
- On étudie l'effet d'une ou plusieurs **variables qualitatives** sur une **variable quantitative** (réponse).
- Les variables qualitatives s'appellent des **facteurs** ([[Facteur (variable catégorielle)]]) ; les caractéristiques qui différencient les facteurs s'appellent des **niveaux** (*levels*).
- Exemple : dans l'exemple des écoles ci-dessous, le facteur est « l'école », ses trois niveaux sont A, B et C, et la réponse est le QI. Le modèle de l'ANOVA à un facteur s'écrit $x_{ij} = \mu + \alpha_i + \varepsilon_{ij}$ : l'observation $j$ du groupe $i$ est la moyenne générale $\mu$, plus l'effet $\alpha_i$ du niveau $i$, plus une erreur aléatoire $\varepsilon_{ij} \sim \mathcal{N}(0, \sigma^2)$, de même variance dans tous les groupes. Tester l'égalité des moyennes revient à tester $\alpha_1 = \dots = \alpha_k = 0$. [[Complément hors du cours|ⓘ]]

### Le test ANOVA

Un test ANOVA permet de savoir si les résultats d'une enquête ou d'une expérience sont significatifs, c'est-à-dire s'il faut rejeter l'[[Test d'hypothèse|hypothèse nulle]] et accepter l'hypothèse alternative. On teste des groupes pour voir s'il existe une différence entre eux.

### Hypothèses

- L'hypothèse nulle de **toute** ANOVA : **toutes les moyennes de population sont exactement égales**.
- Même si c'est vrai, les **moyennes d'échantillon** différeront probablement un peu : les échantillons diffèrent toujours un peu des populations qu'ils représentent.
- Mais elles ne devraient pas différer **trop** : un tel résultat serait improbable sous l'hypothèse nulle de moyennes égales.
- Si on observe malgré tout de grandes différences, on ne croit plus que les moyennes de population étaient vraiment égales.

## Exemple : QI de trois écoles

Un scientifique veut savoir si les enfants des écoles A, B et C ont le même QI moyen. Chaque école a 1 000 enfants ; tester les 3 000 coûte trop cher, on teste donc un [[Échantillonnage|échantillon aléatoire simple]] de $N = 10$ enfants par école.

| École | N | Moyenne | Variance |
|---|---|---|---|
| A | 10 | 99,2 | 111,1 |
| B | 10 | 112,6 | 205,6 |
| C | 10 | 93,3 | 160,5 |
| Total | 30 | 101,7 | 215,5 |

![[Séance 12 - ANOVA and F-statistic - image4.png]]

*Figure : tableau des résultats et diagramme en barres des QI moyens par école (n = 10 par école).*

Le problème : ces moyennes reposent sur de tout petits échantillons. Les 1 000 enfants de chaque école pourraient-ils avoir le même QI moyen, et aurait-on seulement tiré par hasard les enfants les plus forts de l'école B et les plus faibles de l'école C ? « On va essayer de montrer que cette affirmation — l'hypothèse nulle — n'est pas crédible au vu des données. »

### Trois scénarios théoriques

![[Séance 12 - ANOVA and F-statistic - image15.png]]

*Figure : histogrammes des QI des trois écoles (1 000 enfants chacune), tous centrés sur 100, pour une variance intra-école de 50, 100 et 500.*

- Les 3 histogrammes de gauche sont **étroits** : faible variance dans chaque école. Avec $n = 10$ élèves par école, les moyennes d'échantillon seront proches des moyennes de population (égales) ; elles ont peu de place pour fluctuer, donc pour différer.
- Les 3 histogrammes de droite montrent le scénario **opposé** : larges, grande variance dans chaque école. Les moyennes d'échantillon peuvent alors facilement beaucoup différer.
- En bref, **une plus grande variance dans les écoles entraîne probablement une plus grande variance entre les moyennes d'échantillon**.

C'est tout le principe du test : on ne juge pas l'écart entre les moyennes dans l'absolu, mais **rapporté à la variance intra-groupe**. Sous $H_0$, la variance des moyennes d'échantillon vaut $\sigma^2/n$ ; donc $n$ fois la variance observée des moyennes estime $\sigma^2$, tout comme la moyenne des variances intra-groupe. Les deux estimations doivent alors être du même ordre, et leur rapport $F$ proche de 1. [[Complément hors du cours|ⓘ]]

Le calcul sur les données des trois écoles (non fait dans le cours) : moyenne des variances intra-école $MS_E = (111{,}1 + 205{,}6 + 160{,}5)/3 \approx 159{,}1$ ; variance inter-écoles $MS_G = \dfrac{10\left[(99{,}2-101{,}7)^2 + (112{,}6-101{,}7)^2 + (93{,}3-101{,}7)^2\right]}{3-1} \approx \dfrac{1956}{2} = 978$ ; d'où $F(2, 27) \approx 978/159{,}1 \approx 6{,}15$. La valeur critique à 5 % de $F(2, 27)$ est 3,35 (et 5,49 à 1 %) : $p < 0{,}01$, on rejette l'hypothèse de QI moyens égaux. Contrôle : $SS_G + SS_E = 1956 + 9 \times 477{,}2 \approx 6251 = 29 \times 215{,}5$, la variance totale du tableau. [[Complément hors du cours|ⓘ]]

## ANOVA à un facteur (*one-way ANOVA*)

Test qui compare la variance des moyennes de groupes dans un échantillon, en ne considérant qu'**une** variable indépendante (facteur).

Idée de base : **partager la variation totale** des données en deux sources :

1. la variation **à l'intérieur** des niveaux (intra-groupe) ;
2. la variation **entre** les niveaux (inter-groupes).

### Hypothèses

- $H_0$ : pas de différence entre les groupes, moyennes égales.
- $H_1$ : il existe une différence entre les moyennes des groupes.
- $H_1$ signifie « **au moins une** moyenne diffère des autres », pas « toutes les moyennes sont différentes ». Rejeter $H_0$ ne dit donc pas **quels** groupes diffèrent : il faut pour cela des comparaisons a posteriori (voir plus bas). [[Complément hors du cours|ⓘ]]

### Conditions

- **Normalité** : chaque échantillon vient d'une population normale.
- **Indépendance des échantillons** : chacun a été tiré indépendamment des autres.
- **Égalité des variances** : la variance des données est la même dans les différents groupes ([[Homoscédasticité]]).
- La variable dépendante est **continue**.
- Ces conditions se vérifient en pratique : la normalité sur les résidus (graphique quantile-quantile, test de Shapiro-Wilk), l'égalité des variances par le test de Levene ou de Bartlett ; une règle d'usage tolère un rapport de 1 à 4 entre la plus petite et la plus grande variance quand les groupes ont la même taille. L'ANOVA résiste assez bien à un léger défaut de normalité, surtout avec des groupes équilibrés, beaucoup moins à des variances inégales avec des groupes de tailles différentes. [[Complément hors du cours|ⓘ]]
- Si les conditions ne tiennent pas : l'**ANOVA de Welch** se passe de l'égalité des variances, et le [[Test de Kruskal-Wallis|test de Kruskal-Wallis]], version [[Test paramétrique et non paramétrique|non paramétrique]] fondée sur les rangs, se passe de la normalité (il généralise le [[Test de Mann-Whitney|test de Mann-Whitney]] à plus de deux groupes). [[Complément hors du cours|ⓘ]]

## Lien avec le test F, la statistique F et la loi F

Une **statistique F** est la valeur obtenue par une ANOVA **ou** une analyse de régression pour savoir si les moyennes de populations diffèrent significativement. Elle ressemble à la statistique $t$ d'un [[Test t|test t]] :

- le test $t$ dit si **une seule** variable est statistiquement significative ;
- le test F dit si un **groupe** de variables est **conjointement** significatif.

La **loi F** ([[Statistique F]]) est une loi de probabilité continue qui apparaît souvent comme loi sous l'hypothèse nulle d'une [[Statistique de test|statistique de test]], surtout en ANOVA. Ses paramètres $d_1, d_2 > 0$ sont des [[Variance et écart-type d'échantillon|degrés de liberté]] (nombre de valeurs libres de varier dans le calcul final d'une statistique).

Définition de la loi F : si $U \sim \chi^2_{d_1}$ et $V \sim \chi^2_{d_2}$ sont indépendantes ([[Loi du khi-deux]]), alors $\dfrac{U/d_1}{V/d_2}$ suit la loi $F(d_1, d_2)$. Elle ne prend que des valeurs positives et sa moyenne, $\dfrac{d_2}{d_2 - 2}$ pour $d_2 > 2$, est proche de 1. En ANOVA, seul un $F$ **grand** contredit $H_0$ (variance entre groupes trop forte), d'où un test unilatéral à droite. [[Complément hors du cours|ⓘ]]

![[Séance 12 - ANOVA and F-statistic - image6.png]]

*Figure : densité de la loi F avec la zone de rejet $\alpha$ au-delà de $F_{critical}$, et densités pour plusieurs couples $(d_1, d_2)$.*

$$F = \frac{\text{variance inter-groupes (between-groups)}}{\text{variance intra-groupe (within-group)}}$$

Le F d'une ANOVA à un facteur aide à répondre à : « la variance entre les moyennes de deux populations ou plus est-elle significativement différente ? ». Il détermine aussi la [[P-value|p-value]], probabilité d'obtenir un résultat au moins aussi extrême que celui observé si l'hypothèse nulle est vraie. La p-value est une probabilité, le rapport F une statistique de test :

$$F = \frac{\text{variance des moyennes de groupes (Mean Square Between)}}{\text{moyenne des variances intra-groupe (Mean Squared Error)}}$$

**Quand rejeter $H_0$ ?** Quand la p-value est inférieure au seuil $\alpha$. De façon équivalente, on rejette $H_0$ quand la valeur de F dépasse la valeur critique de la loi F ; si F reste en dessous de la valeur critique, on ne rejette pas $H_0$. [[Erreurs du cours#^e-12-anova-and-f-statistic|✎]]

## Comparaison test t / test F

| Base de comparaison | Test t | Test F |
|---|---|---|
| Sens | Test d'hypothèse univarié, appliqué quand l'[[Espérance et variance|écart-type]] est inconnu et l'échantillon petit | Test qui détermine l'égalité des variances de deux populations normales |
| Statistique de test | Suit une [[Loi de Student]] sous $H_0$ | Suit une loi F de Snedecor sous $H_0$ |
| Application | Comparer les moyennes de deux populations | Comparer deux variances de population |

## Tableau d'ANOVA

| Source de variation | df | [[Somme des carrés (SST, SSR, SSE)\|Somme des carrés]] | MS | F |
|---|---|---|---|---|
| Groupe | $k-1$ | $SST_G$ | $\dfrac{SST_G}{k-1}$ | $\dfrac{SST_G/(k-1)}{SST_E/(N-k)}$ |
| Erreur | $N-k$ | $SST_E$ | $\dfrac{SST_E}{N-k}$ | |
| Total | $N-1$ | $SST$ | | |

($k$ groupes, $N$ observations au total ; MS = [[Carré moyen]].)

Formules de calcul, pour des groupes de tailles $n_i$, de moyennes $\bar{x}_i$ et de variances $s_i^2$, avec $\bar{x}$ la moyenne globale : $SST_G = \sum_i n_i(\bar{x}_i - \bar{x})^2$ et $SST_E = \sum_i \sum_j (x_{ij} - \bar{x}_i)^2 = \sum_i (n_i - 1)s_i^2$. Les degrés de liberté s'additionnent comme les sommes de carrés : $(k-1) + (N-k) = N-1$. Le tableau convient aussi à des groupes de tailles inégales. [[Complément hors du cours|ⓘ]]

## Exemple numérique

Trois échantillons de 5 valeurs :

- échantillon 1 : 2, 3, 7, 2, 6 ;
- échantillon 2 : 10, 3, 7, 2, 6 ;
- échantillon 3 : 10, 13, 14, 13, 15.

![[Séance 12 - ANOVA and F-statistic - image3.png]]

*Figure : décomposition de la somme totale des carrés en SSW (autour de chaque moyenne d'échantillon), SSB (moyennes d'échantillon autour de la moyenne globale, ×5) et SST (15 valeurs autour de la moyenne globale).*

- **SSW** (*Sum of Squares Within samples*) : $\sum (x_i - \bar{x}_1)^2 + \sum (x_i - \bar{x}_2)^2 + \sum (x_i - \bar{x}_3)^2$ ;
- **SSB** (*Sum of Squares Between samples*) : $5 \times \left[(\bar{x}_1 - \bar{x})^2 + (\bar{x}_2 - \bar{x})^2 + (\bar{x}_3 - \bar{x})^2\right]$ ;
- **SST** (*Total Sum of Squares*) : $\sum (x_i - \bar{x})^2$ sur les 15 valeurs, $\bar{x}$ moyenne globale.
- Les moyennes de ces données : $\bar{x}_1 = 20/5 = 4$, $\bar{x}_2 = 28/5 = 5{,}6$, $\bar{x}_3 = 65/5 = 13$, et $\bar{x} = 113/15 \approx 7{,}53$. D'où $SSW = 22 + 41{,}2 + 14 = 77{,}2$ et $SSB = 5\left[(4 - 7{,}53)^2 + (5{,}6 - 7{,}53)^2 + (13 - 7{,}53)^2\right] \approx 230{,}5$. [[Complément hors du cours|ⓘ]]

Avec ces données : [[Erreurs du cours#^e-12-anova-and-f-statistic|✎]]

$$SSW + SSB = SST : \quad 77{,}2 + 230{,}5 = 307{,}7$$

Carrés moyens : [[Erreurs du cours#^e-12-anova-and-f-statistic|✎]]

$$\frac{SSB}{d.o.f.} = \frac{SSB}{(\text{nb d'échantillons}) - 1} = \frac{230{,}5}{2} \approx 115{,}27$$

$$\frac{SSW}{d.o.f.} = \frac{SSW}{(\text{nb d'observations}) - (\text{nb d'échantillons})} = \frac{77{,}2}{15 - 3} \approx 6{,}43$$

$$F = F(2, 12) = \frac{115{,}27}{6{,}43} \approx 17{,}92, \quad p < 0{,}05$$

Dans la table de la loi F, colonne $df_1 = 2$ (numérateur) et ligne $df_2 = 12$ (dénominateur) : **valeur critique = 3,89**. $F \approx 17{,}92$ tombe dans la région de rejet : on rejette $H_0$. [[Erreurs du cours#^e-12-anova-and-f-statistic|✎]]

![[Séance 12 - ANOVA and F-statistic - image9.png]]

*Figure : courbe de la loi F avec la région de rejet au-delà de 3,89 et la position de F, loin dans cette région ; table des valeurs critiques où l'on lit 3,89 à l'intersection colonne 2 / ligne 12.*

Extrait de la table des valeurs critiques de F ($\alpha = 0{,}05$) donnée par le cours (lignes : $df_2$, colonnes : $df_1$) :

| $df_2$ \\ $df_1$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 10 | 4,96 | 4,10 | 3,71 | 3,48 | 3,33 |
| 11 | 4,84 | 3,98 | 3,59 | 3,36 | 3,20 |
| 12 | 4,75 | **3,89** | 3,49 | 3,26 | 3,11 |
| 13 | 4,67 | 3,81 | 3,41 | 3,18 | 3,03 |
| 14 | 4,60 | 3,74 | 3,34 | 3,11 | 2,96 |

**Taille d'effet.** Un $F$ significatif dit qu'une différence existe, pas qu'elle est grande. On la mesure par $\eta^2 = \dfrac{SSB}{SST}$, la part de la variation totale expliquée par le facteur : c'est l'équivalent du $R^2$ de la régression ([[Coefficient de détermination]]). Sur l'exemple, $\eta^2 \approx 230{,}5 / 307{,}7 \approx 0{,}75$ : le groupe explique les trois quarts de la variation. [[Complément hors du cours|ⓘ]]

**En R**, l'ANOVA à un facteur s'écrit avec une [[Formule de modèle en R|formule de modèle]], le groupe devant être un [[Facteur (variable catégorielle)|facteur]] : [[Complément hors du cours|ⓘ]]

```r
valeurs <- c(2, 3, 7, 2, 6,  10, 3, 7, 2, 6,  10, 13, 14, 13, 15)
groupe  <- factor(rep(c("e1", "e2", "e3"), each = 5))
modele  <- aov(valeurs ~ groupe)
summary(modele)      # tableau d'ANOVA : Df, Sum Sq, Mean Sq, F value, Pr(>F)
TukeyHSD(modele)     # comparaisons des groupes deux à deux
qf(0.95, 2, 12)      # valeur critique à 5 % : 3,885
```

## ANOVA contre test t

| Base de comparaison | Test t | ANOVA |
|---|---|---|
| Sens | Test d'hypothèse pour comparer les moyennes de **deux** populations | Technique pour comparer les moyennes de **plus de deux** populations |
| Statistique de test | $(\bar{x}-\mu)/(s/\sqrt{n})$ | variance inter-échantillons / variance intra-échantillon |

On *pourrait* faire une série de tests $t$, mais quand le nombre de groupes augmente, le nombre de comparaisons par paires explose. L'ANOVA donne **un seul nombre** (la statistique F) et **une seule p-value** pour accepter ou rejeter l'hypothèse nulle.

La vraie raison est le risque d'erreur : avec $k$ groupes, il y a $\binom{k}{2}$ paires, et chaque test $t$ au seuil $\alpha$ a une chance $\alpha$ de conclure à tort à une différence ([[Erreur de type I et de type II|erreur de type I]]). Pour $m$ tests indépendants, le risque d'au moins une fausse alerte vaut $1 - (1 - \alpha)^m$ : déjà $1 - 0{,}95^3 \approx 14\ \%$ pour 3 groupes, et $1 - 0{,}95^{10} \approx 40\ \%$ pour 5 groupes. L'ANOVA garde un risque global de $\alpha$. [[Complément hors du cours|ⓘ]]

Après un $F$ significatif, on cherche quels groupes diffèrent par des [[Comparaisons multiples|comparaisons multiples]] (tests *post hoc*), qui corrigent ce risque : méthode de **Tukey** (HSD, toutes les paires), correction de **Bonferroni** (chaque test au seuil $\alpha/m$). [[Complément hors du cours|ⓘ]]

Avec **deux** groupes seulement, l'ANOVA et le [[Test t|test $t$]] bilatéral à variances égales donnent la même conclusion : $F = t^2$, et la loi $F(1, \nu)$ est celle du carré d'une variable de Student à $\nu$ degrés de liberté. [[Complément hors du cours|ⓘ]]

## ANOVA à deux facteurs (*two-way ANOVA*)

Chaque échantillon est défini de deux manières, et donc rangé dans deux groupes catégoriels.

### Hypothèses

Comme l'ANOVA à deux facteurs considère l'effet de deux facteurs catégoriels **et** leur effet l'un sur l'autre, il y a **trois paires** d'hypothèses nulle / alternative (le cours ne les écrit pas).

Pour deux facteurs A et B, les trois paires sont : [[Complément hors du cours|ⓘ]]
1. $H_0$ : les moyennes sont égales pour tous les niveaux de A (pas d'effet principal de A) ; $H_1$ : au moins une diffère ;
2. $H_0$ : pas d'effet principal de B ; $H_1$ : au moins une moyenne de B diffère ;
3. $H_0$ : pas d'**interaction** entre A et B ; $H_1$ : il y a une interaction.

Il y a **interaction** quand l'effet d'un facteur dépend du niveau de l'autre : par exemple un engrais qui fait pousser une plante au soleil mais pas à l'ombre. Sur un graphique d'interaction (moyennes de la réponse selon A, une courbe par niveau de B), des courbes parallèles signalent l'absence d'interaction ; quand elle existe, les effets principaux pris seuls peuvent tromper. Chaque hypothèse a son propre $F$ ; avec $a$ niveaux pour A, $b$ pour B et $r$ répétitions par case, les degrés de liberté sont $a-1$, $b-1$, $(a-1)(b-1)$ et $ab(r-1)$ pour l'erreur. En R : `aov(y ~ A * B)`. [[Complément hors du cours|ⓘ]]

### Conditions

- La variable dépendante est continue.
- Les deux variables indépendantes sont en groupes catégoriels et indépendants.
- Indépendance des échantillons.
- Égalité des variances entre groupes.
- Normalité : chaque échantillon vient d'une population normale.

### Un facteur contre deux facteurs

| | ANOVA à un facteur | ANOVA à deux facteurs |
|---|---|---|
| Définition | Comparer les moyennes de trois groupes de données ou plus | Comparer les moyennes de trois groupes ou plus, en considérant deux variables indépendantes |
| Nombre de variables indépendantes | Une | Deux |
| Ce qu'on compare | Les moyennes de trois groupes ou plus d'une variable indépendante sur une variable dépendante | L'effet de plusieurs groupes de deux variables indépendantes sur une variable dépendante et l'une sur l'autre |
| Nombre de groupes d'échantillons | Trois ou plus | Chaque variable doit avoir plusieurs échantillons |

## Régression linéaire simple et ANOVA

Fait peu évident : la [[Régression linéaire|régression linéaire]] simple (par [[Moindres carrés|moindres carrés]] ordinaires), dans les conditions standard, est **un cas particulier d'ANOVA**.

La variation des $y_i$ se mesure par les écarts $y_i - \bar{y}$. La variation totale est

$$SST = \sum (y_i - \bar{y})^2$$

Si $SST = 0$, toutes les observations sont identiques (aucune variabilité) ; plus SST est grand, plus les $y$ varient. Avec le modèle de régression, on mesure la variabilité des $y$ autour de la droite ajustée : $y_i - \hat{y}_i$.

$$y_i - \bar{y} = (y_i - \hat{y}_i) + (\hat{y}_i - \bar{y})$$

$$\sum (y_i - \bar{y})^2 = \sum (y_i - \hat{y}_i)^2 + \sum (\hat{y}_i - \bar{y})^2 + 2\sum (y_i - \hat{y}_i)(\hat{y}_i - \bar{y}) \quad (1)$$

$$\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x \quad (2)$$

En substituant (2) dans (1) « et en sautant un peu d'algèbre », le terme croisé disparaît :

$$\sum (y_i - \bar{y})^2 = \sum (\hat{y}_i - \bar{y})^2 + \sum (y_i - \hat{y}_i)^2 \qquad SST = SSR + SSE$$

L'algèbre sautée : les estimateurs des moindres carrés annulent les dérivées de $\sum e_i^2$ par rapport à $\hat\beta_0$ et $\hat\beta_1$, ce qui donne les équations normales $\sum e_i = 0$ et $\sum x_i e_i = 0$, avec $e_i = y_i - \hat{y}_i$ ([[Résidu (régression)|résidus]]). Comme $\hat{y}_i - \bar{y} = \hat\beta_0 + \hat\beta_1 x_i - \bar{y}$, le terme croisé vaut $(\hat\beta_0 - \bar{y})\sum e_i + \hat\beta_1 \sum x_i e_i = 0$. [[Complément hors du cours|ⓘ]]

Le tableau d'ANOVA de la régression simple a $1$ degré de liberté pour SSR et $n-2$ pour SSE, d'où $F = \dfrac{SSR/1}{SSE/(n-2)}$, qui teste $H_0 : \beta_1 = 0$. Ce $F$ est le carré du $t$ du [[Test de la pente|test de la pente]], et $R^2 = SSR/SST$ ([[Coefficient de détermination]]). [[Complément hors du cours|ⓘ]]

On obtient les [[Carré moyen|carrés moyens]] en divisant ces sommes par leurs degrés de liberté : c'est le lien entre régression linéaire simple et ANOVA.

**Différence clé** (dernière diapositive) : en ANOVA, **aucune hypothèse** n'est faite sur la manière dont le prix (*Price*) et le volume de ventes (*Sales Volume*) sont liés.

Autrement dit, l'ANOVA traite la variable explicative comme **qualitative** : chaque niveau (chaque prix) reçoit sa propre moyenne, sans forme imposée, alors que la régression impose une droite $\beta_0 + \beta_1 x$. Les deux relèvent du même cadre, le **modèle linéaire** : une ANOVA est une régression sur des variables indicatrices des niveaux, et R ajuste les deux avec `lm()`. [[Complément hors du cours|ⓘ]]
