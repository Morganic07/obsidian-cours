---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 12 : ANOVA and F-statistic .docx|Cours 12 - ANOVA and F-statistic]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 3/Data analysis (Thanos)/Cours 12 : ANOVA and F-statistic .docx|Cours 12 - ANOVA and F-statistic]], dans [[Data analysis (Thanos) (matière)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

L'[[ANOVA]] teste si trois populations ou plus ont la même moyenne, en comparant la variation entre groupes à la variation dans les groupes. Sa statistique est la [[Statistique F]]. Le cours finit en reliant l'ANOVA à la régression simple.

## Introduction à l'ANOVA (*ANalysis Of VAriance*)

- Technique statistique pour tester si **trois moyennes de population ou plus** sont toutes égales.
  - **ANOVA à un facteur** (*one-way*) : comparer 3 groupes ou plus sur 1 variable.
  - **ANOVA à deux facteurs** (*two-way*) : comparer 3 groupes ou plus sur 2 variables.
- On étudie l'effet d'une ou plusieurs **variables qualitatives** sur une **variable quantitative** (réponse).
- Les variables qualitatives s'appellent des **facteurs** ([[Facteur (variable catégorielle)]]) ; les caractéristiques qui différencient les facteurs s'appellent des **niveaux** (*levels*).

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

## ANOVA à un facteur (*one-way ANOVA*)

Test qui compare la variance des moyennes de groupes dans un échantillon, en ne considérant qu'**une** variable indépendante (facteur).

Idée de base : **partager la variation totale** des données en deux sources :

1. la variation **à l'intérieur** des niveaux (intra-groupe) ;
2. la variation **entre** les niveaux (inter-groupes).

### Hypothèses

- $H_0$ : pas de différence entre les groupes, moyennes égales.
- $H_1$ : il existe une différence entre les moyennes des groupes.

### Conditions

- **Normalité** : chaque échantillon vient d'une population normale.
- **Indépendance des échantillons** : chacun a été tiré indépendamment des autres.
- **Égalité des variances** : la variance des données est la même dans les différents groupes ([[Homoscédasticité]]).
- La variable dépendante est **continue**.

## Lien avec le test F, la statistique F et la loi F

Une **statistique F** est la valeur obtenue par une ANOVA **ou** une analyse de régression pour savoir si les moyennes de populations diffèrent significativement. Elle ressemble à la statistique $t$ d'un [[Test t|test t]] :

- le test $t$ dit si **une seule** variable est statistiquement significative ;
- le test F dit si un **groupe** de variables est **conjointement** significatif.

La **loi F** ([[Statistique F]]) est une loi de probabilité continue qui apparaît souvent comme loi sous l'hypothèse nulle d'une [[Statistique de test|statistique de test]], surtout en ANOVA. Ses paramètres $d_1, d_2 > 0$ sont des [[Variance et écart-type d'échantillon|degrés de liberté]] (nombre de valeurs libres de varier dans le calcul final d'une statistique).

![[Séance 12 - ANOVA and F-statistic - image6.png]]

*Figure : densité de la loi F avec la zone de rejet $\alpha$ au-delà de $F_{critical}$, et densités pour plusieurs couples $(d_1, d_2)$.*

$$F = \frac{\text{variance inter-groupes (between-groups)}}{\text{variance intra-groupe (within-group)}}$$

Le F d'une ANOVA à un facteur aide à répondre à : « la variance entre les moyennes de deux populations ou plus est-elle significativement différente ? ». Il détermine aussi la [[P-value|p-value]], probabilité d'obtenir un résultat au moins aussi extrême que celui observé si l'hypothèse nulle est vraie. La p-value est une probabilité, le rapport F une statistique de test :

$$F = \frac{\text{variance des moyennes de groupes (Mean Square Between)}}{\text{moyenne des variances intra-groupe (Mean Squared Error)}}$$

**Quand rejeter $H_0$ ?** Quand la p-value est inférieure au seuil $\alpha$. La diapositive ajoute : « You should not reject the null if your critical f value is smaller than your F-value, unless you also have a small p-value » (voir Points à vérifier).

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

$$SSW + SSB = SST : \quad 54 + 203{,}3 = 257{,}3 \text{ (valeurs de la diapositive, voir Points à vérifier)}$$

Carrés moyens :

$$\frac{SSB}{d.o.f.} = \frac{SSB}{(\text{nb d'échantillons}) - 1} = \frac{203{,}3}{2} = 101{,}667$$

$$\frac{SSW}{d.o.f.} = \frac{SSW}{(\text{nb d'observations}) - (\text{nb d'échantillons})} = \frac{54}{15 - 3} = 4{,}5$$

$$F = F(2, 12) = \frac{101{,}667}{4{,}5} = 22{,}59$$

(la diapositive ajoute « $p > 0{,}05$ », voir Points à vérifier).

Dans la table de la loi F, colonne $df_1 = 2$ (numérateur) et ligne $df_2 = 12$ (dénominateur) : **valeur critique = 3,89**. $F = 22{,}59$ tombe dans la région de rejet : on rejette $H_0$.

![[Séance 12 - ANOVA and F-statistic - image9.png]]

*Figure : courbe de la loi F avec la région de rejet au-delà de 3,89 et la position de F = 22,59 ; table des valeurs critiques où l'on lit 3,89 à l'intersection colonne 2 / ligne 12.*

Extrait de la table des valeurs critiques de F ($\alpha = 0{,}05$) donnée par le cours (lignes : $df_2$, colonnes : $df_1$) :

| $df_2$ \\ $df_1$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 10 | 4,96 | 4,10 | 3,71 | 3,48 | 3,33 |
| 11 | 4,84 | 3,98 | 3,59 | 3,36 | 3,20 |
| 12 | 4,75 | **3,89** | 3,49 | 3,26 | 3,11 |
| 13 | 4,67 | 3,81 | 3,41 | 3,18 | 3,03 |
| 14 | 4,60 | 3,74 | 3,34 | 3,11 | 2,96 |

## ANOVA contre test t

| Base de comparaison | Test t | ANOVA |
|---|---|---|
| Sens | Test d'hypothèse pour comparer les moyennes de **deux** populations | Technique pour comparer les moyennes de **plus de deux** populations |
| Statistique de test | $(\bar{x}-\mu)/(s/\sqrt{n})$ | variance inter-échantillons / variance intra-échantillon |

On *pourrait* faire une série de tests $t$, mais quand le nombre de groupes augmente, le nombre de comparaisons par paires explose. L'ANOVA donne **un seul nombre** (la statistique F) et **une seule p-value** pour accepter ou rejeter l'hypothèse nulle.

## ANOVA à deux facteurs (*two-way ANOVA*)

Chaque échantillon est défini de deux manières, et donc rangé dans deux groupes catégoriels.

### Hypothèses

Comme l'ANOVA à deux facteurs considère l'effet de deux facteurs catégoriels **et** leur effet l'un sur l'autre, il y a **trois paires** d'hypothèses nulle / alternative (le cours ne les écrit pas).

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

On obtient les [[Carré moyen|carrés moyens]] en divisant ces sommes par leurs degrés de liberté : c'est le lien entre régression linéaire simple et ANOVA.

**Différence clé** (dernière diapositive) : en ANOVA, **aucune hypothèse** n'est faite sur la manière dont le prix (*Price*) et le volume de ventes (*Sales Volume*) sont liés.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **« F = 22,59, p > 0,05 »** : image lue directement, la diapositive l'écrit ainsi. Or $F = 22{,}59$ dépasse la valeur critique 3,89, donc $p < 0{,}05$ et le schéma même de la diapositive classe $F$ dans la région de rejet (complément). Alerte de la transcription confirmée. **À corriger avant un examen.**
2. **Sommes de l'exemple numérique** : image lue directement. Avec les valeurs affichées (2, 3, 7, 2, 6 ; 10, 3, 7, 2, 6 ; 10, 13, 14, 13, 15), je trouve $SSW = 77{,}2$, $SSB \approx 230{,}5$ et $SST \approx 307{,}7$, pas 54, 203,3 et 257,3 (complément). La structure $SSW + SSB = SST$ et les degrés de liberté sont justes, mais les valeurs affichées ne viennent pas de ces données ($F$ vaudrait alors environ 18, toujours dans la région de rejet). Ne pas refaire le calcul à l'examen avec ces nombres.
3. **Règle de rejet** : « on ne rejette pas $H_0$ si la valeur critique est plus petite que $F$ » est fausse, on rejette dans ce cas (complément, voir [[Séance 11 - Multiple Linear Regression and F-statistic (résumé)|Cours 11]]).
4. **Tableau $t$ contre F** : le test F est présenté comme test d'égalité de variances de deux populations, alors que l'ANOVA l'utilise pour comparer des moyennes. Les deux usages sont corrects, mais le cours ne fait pas le lien.
5. **Dernière diapositive coupée** : « KEY DIFFERENCE : in ANOVA → no assumption is made about the manner in which Price and Sales Volume are related » s'arrête là, sans le pendant côté régression (le contraste attendu est que la régression suppose une relation linéaire). Les mots « Price » et « Sales Volume » ne sont expliqués nulle part dans la note.
6. **Fragments illisibles** (numéros de page, bord d'image coupé) : sans importance.
