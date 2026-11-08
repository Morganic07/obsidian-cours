---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Statistics/Chp2 : Descriptive statistics.docx|Chp2 - Descriptive statistics]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Statistics/Chp2 : Descriptive statistics.docx|Chp2 - Descriptive statistics]], dans [[Cours/Probabilités et statistiques/Statistics/_index|Statistics]] : résumer un jeu de données par des graphiques, puis par des indicateurs de position (moyenne, médiane, quartiles) et de dispersion (étendue, variance, écart interquartile). Voir [[Statistique descriptive]]. Les images n'ont pas été ouvertes : seules leurs transcriptions ont été lues.

## Méthodes graphiques

### Diagramme tige et feuilles (*stem and leaf display*)

([[Diagramme tige et feuilles]])

Exemple du cours : 38 salaires de départ (de 50 128 \$ à 83 000 \$). Tige : 10 000 \$ ; feuille : 1 000 \$ ; chaque tige est dédoublée en partie basse (L, feuilles 0 à 4) et haute (H, feuilles 5 à 9).

```
5L | 02
5H | 5566788
6L | 000001112233
6H | 55556788
7L | 00002
7H | 5
8L | 003
```

Lecture : la ligne « 6L | 000001112233 » contient douze salaires entre 60 000 et 64 999 \$ (cinq à 60 000, trois à 61 000…). Contrairement à l'histogramme, le diagramme garde chaque valeur (au millier près) tout en montrant la forme de la distribution, tournée d'un quart de tour ; il convient aux petits jeux de données. [[Complément hors du cours|ⓘ]]

### Diagramme en points (*dotplot*)

([[Diagramme en points]])

![[Chp2 - Descriptive statistics - image16.png]]

*Figure : diagramme en points de l'indice Big Mac (en \$US) de 56 pays, sur un axe de 2,0 à 6,5 ; la valeur des États-Unis (5,58 \$) est signalée ; la plupart des points sont entre 2 et 4,6.*

### Histogramme

([[Histogramme]])

Exemple : dix mesures 2,1 ; 2,4 ; 2,2 ; 2,3 ; 2,7 ; 2,5 ; 2,4 ; 2,6 ; 2,6 ; 2,9. [[Erreurs du cours#^e-2-descriptive-statistics|✎]] Pour visualiser leur histogramme de [[Fréquence relative|fréquence relative]] :

1. diviser l'axe des mesures en intervalles de même largeur (ici 0,2, à partir de 2,05) ;
2. placer sur chaque intervalle un rectangle de hauteur proportionnelle à la fréquence ou à la fréquence relative des mesures qui y tombent.

Classes (*class intervals*) : chaque observation appartient à exactement une classe.

![[Chp2 - Descriptive statistics - image11.png]]

*Figure : histogramme de fréquence relative des dix mesures, classes de 2,05 à 3,05 de largeur 0,2.*

$$\text{Fréquence relative} = \frac{\text{nombre d'occurrences de la valeur}}{\text{nombre d'observations de l'échantillon}}$$

### Densité

$$\text{Densité d'une classe} = \frac{\text{fréquence relative de la classe}}{\text{largeur de la classe}}$$

Dans un histogramme (à classes inégales), la hauteur du rectangle de chaque classe est sa densité ; l'échelle verticale s'appelle alors **échelle de densité** (*density scale*).

Avec l'échelle de densité, c'est l'**aire** de chaque rectangle (densité × largeur) qui vaut la fréquence relative de la classe, et l'aire totale de l'histogramme vaut 1. C'est indispensable avec des classes inégales : en hauteur de fréquence, une classe deux fois plus large paraîtrait deux fois plus importante à densité égale. L'histogramme de densité annonce aussi la [[Variable aléatoire|densité]] d'une loi continue, dont l'aire sous la courbe vaut 1. [[Complément hors du cours|ⓘ]]

![[Chp2 - Descriptive statistics - image25.png]]

*Figure : histogramme de densité, à classes de largeurs inégales, du coût annuel de carburant attendu (centaines de dollars) ; pic d'environ 0,12 entre 15 et 17,5.*

Note du cours : si la valeur vaut 15 pile, elle va dans l'intervalle supérieur.

### Formes de distribution

([[Forme d'une distribution]])

![[Chp2 - Descriptive statistics - image19.png]]

*Figure : histogrammes lissés : (a) symétrique unimodal ; (b) bimodal ; (c) asymétrie positive (queue à droite) ; (d) asymétrie négative (queue à gauche).*

### Choix des classes

- Une observation peut tomber sur une borne de classe (par exemple 29,0) et n'appartenir alors à aucune classe unique.
- **Convention** : toute observation sur une borne va dans la classe **à sa droite** ; 29,0 va dans 29,0–29,5 et non dans 28,5–29,0.
- Plus il y a d'observations, plus il faut de classes. Règle raisonnable :
$$\text{nombre de classes} \approx \sqrt{\text{nombre d'observations}}$$

Une autre règle répandue est celle de **Sturges**, $k \approx 1 + \log_2 n$ (7 classes pour 64 observations, contre 8 avec la racine). Ce ne sont que des points de départ : trop peu de classes écrasent la forme de la distribution, trop de classes la rendent hachée, avec beaucoup de classes vides. [[Complément hors du cours|ⓘ]]

![[Chp2 - Descriptive statistics - image14.png]]

*Figure : choix des classes pour des points « étirés » : (a) beaucoup d'intervalles courts de même largeur ; (b) quelques intervalles larges de même largeur ; (c) intervalles de largeurs inégales.*

### Distribution de fréquences

Une **distribution de fréquences** est un tableau des fréquences et/ou des fréquences relatives. Exemple : salaires de départ annuels de 42 personnes (en milliers).

| Salaire | 57 | 58 | 59 | 60 | 61 | 62 | 63 | 64 | 66 | 67 | 70 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Fréquence (tableau 2.1) | 4 | 1 | 3 | 5 | 8 | 10 | 0 | 5 | 2 | 3 | 1 |
| Fréquence relative (tableau 2.2) | 4/42 = 0,0952 | 1/42 = 0,0238 | 3/42 | 5/42 | 8/42 | 10/42 | 0 | 5/42 | 2/42 | 3/42 | 1/42 |

On ajoute souvent les **fréquences cumulées** : la proportion d'observations inférieures ou égales à chaque valeur, obtenue en additionnant les fréquences relatives de proche en proche. Ici, $(4 + 1 + 3 + 5 + 8)/42 = 21/42 = 0{,}5$ des salaires sont $\le 61$, et 31/42 sont $\le 62$ : la 21e valeur est 61, la 22e est 62, et la médiane vaut $(61 + 62)/2 = 61{,}5$. Leur graphe est la [[Fonction de répartition empirique|fonction de répartition empirique]]. Les fréquences relatives d'un tableau ont toujours une somme égale à 1. [[Complément hors du cours|ⓘ]]

### Données catégorielles

Diagrammes circulaires (*pie charts*) et diagrammes en barres (*bar graphs*) : voir [[Diagramme en barres et diagramme circulaire]].

![[Chp2 - Descriptive statistics - image17.png]]

*Figure : diagramme circulaire des locuteurs natifs de l'anglais (USA, UK, Canada, Australia, Other) ; diagrammes en barres verticales et horizontales de la couleur des yeux (marron environ 13, vert 8, bleu 4, noir 1 ; « marron » est la modalité la plus fréquente).*

### Boîte à moustaches (*box plot*, *box-and-whiskers plot*)

([[Quartiles et valeurs aberrantes]])

Construction :

1. Tracer une échelle de mesure (horizontale ou verticale).
2. Tracer un rectangle le long de l'axe, de $q_1$ à $q_3$ (sa longueur vaut donc l'iqr).
3. Placer un segment à la médiane. Sa position par rapport aux deux bords renseigne sur l'asymétrie des 50 % centraux.
4. Repérer les valeurs aberrantes (*outliers*) et marquer chacune individuellement (symboles éventuellement différents pour les modérées et les extrêmes ; la plupart des logiciels ne les distinguent pas).
5. Tracer les « moustaches » depuis chaque bord du rectangle jusqu'à la plus petite et la plus grande observation **qui ne sont pas aberrantes**.

La boîte à moustaches dessine le **résumé en cinq nombres** : minimum, $q_1$, médiane, $q_3$, maximum (moustaches réduites aux valeurs non aberrantes). Elle sert surtout à comparer plusieurs distributions côte à côte sur une même échelle. Pour une loi normale, les bornes $q_1 - 1{,}5\,\text{iqr}$ et $q_3 + 1{,}5\,\text{iqr}$ tombent à environ $\pm 2{,}7$ écarts-types de la moyenne : moins de 1 % des valeurs (environ 0,7 %) sont alors signalées comme aberrantes. [[Complément hors du cours|ⓘ]]

**Exemple : charge quotidienne d'azote (57 valeurs).**

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| 9,69 | 13,16 | 17,09 | 18,12 | 23,70 | 24,07 | 24,29 | 26,43 |
| 30,75 | 31,54 | 35,07 | 36,99 | 40,32 | 42,51 | 45,64 | 48,22 |
| 49,98 | 50,06 | 55,02 | 57,00 | 58,41 | 61,31 | 64,25 | 65,24 |
| 66,14 | 67,68 | 81,40 | 90,80 | 92,17 | 92,42 | 100,82 | 101,94 |
| 103,61 | 106,28 | 106,80 | 108,69 | 114,61 | 120,86 | 124,54 | 143,27 |
| 143,75 | 149,64 | 167,79 | 182,50 | 192,55 | 193,53 | 271,57 | 292,61 |
| 312,45 | 352,09 | 371,47 | 444,68 | 460,86 | 563,92 | 690,11 | 826,54 |
| 1529,35 | | | | | | | |

- Résumé : médiane $\tilde{x} = 92{,}17$, $q_1 = 45{,}64$, $q_3 = 167{,}79$, $\text{iqr} = 122{,}15$, $1{,}5\,\text{iqr} = 183{,}225$, $3\,\text{iqr} = 366{,}45$. Les logiciels peuvent donner des valeurs légèrement différentes.
- En bas : $q_1 - 1{,}5\,\text{iqr} < 0$ et aucune observation n'est négative, donc pas de valeur aberrante basse.
- En haut : $q_3 + 1{,}5\,\text{iqr} = 351{,}015$ et $q_3 + 3\,\text{iqr} = 534{,}24$. Donc 563,92, 690,11, 826,54 et 1529,35 sont des aberrantes **extrêmes** ; 352,09, 371,47, 444,68 et 460,86 sont **modérées**.

![[Chp2 - Descriptive statistics - image22.png]]

*Figure : tableau des 57 charges d'azote et boîte à moustaches horizontale : boîte de 45 à 168, médiane vers 92, moustache jusqu'à 312 environ, aberrantes modérées en points pleins, extrêmes en cercles vides.*

### À retenir sur les variables

- Variables **qualitatives** (oui/non…) : on calcule une proportion $\hat{p} = \text{nombre de « oui »} / \text{nombre d'essais}$.
- Variables **quantitatives** : on calcule moyenne, écart-type et variance.
- ⚠ **Histogramme** : données quantitatives ; **diagramme en barres** : données qualitatives.

## Moyenne, médiane, écart-type, variance et écart interquartile

### Moyenne d'échantillon

**Définition** : la [[Moyenne empirique|moyenne d'échantillon]] (*sample mean*) de $x_1, \dots, x_n$ est
$$\bar{x} = \frac{x_1 + x_2 + \dots + x_n}{n} = \frac{\sum_{i=1}^{n} x_i}{n}.$$
Le numérateur s'écrit plus simplement $\sum x_i$, la somme portant sur toutes les observations. Voir [[Mesures de tendance centrale]].

La moyenne est le centre de gravité des données : c'est la valeur $c$ qui minimise $\sum (x_i - c)^2$. Elle est **sensible** aux valeurs extrêmes : une seule valeur très grande la tire vers le haut. [[Complément hors du cours|ⓘ]]

### Médiane d'échantillon

**Définition** : on ordonne les $n$ observations de la plus petite à la plus grande (valeurs répétées comprises). Alors
$$\tilde{x} = \begin{cases} \text{valeur de rang } \frac{n+1}{2} & \text{si } n \text{ impair} \\ \text{moyenne des valeurs de rangs } \frac{n}{2} \text{ et } \frac{n}{2}+1 & \text{si } n \text{ pair} \end{cases}$$

**Exemple** : 62,3 ; 62,8 ; 63,6 ; 65,2 ; 65,7 ; 66,4 ; 67,4 ; 68,4 ; 68,8 ; 70,8 ; 75,7 ; 79,0. Comme $n = 12$ est pair, la médiane est la moyenne des 6e et 7e valeurs :
$$\tilde{x} = \frac{66{,}4 + 67{,}4}{2} = 66{,}90 \text{ min}.$$

La médiane, au contraire, est **résistante** : remplacer 79,0 par 790 ne la change pas, alors que la moyenne de ces douze valeurs passerait d'environ 68,0 à environ 127,3. C'est pourquoi on donne la médiane pour des grandeurs très asymétriques comme les revenus ou les prix immobiliers. Elle minimise $\sum |x_i - c|$. [[Complément hors du cours|ⓘ]]

Deux autres indicateurs de position : le **mode**, valeur (ou classe) la plus fréquente, seul utilisable pour une variable nominale ; et la **moyenne tronquée** (*trimmed mean*), moyenne calculée après avoir retiré un pourcentage fixé des plus petites et des plus grandes valeurs (par exemple 10 % de chaque côté), compromis entre moyenne et médiane. [[Complément hors du cours|ⓘ]]

### Percentiles

([[Quantile]])

**Définition** : pour $0 < p < 1$, un $100p$-ième percentile est toute valeur $x_p$ telle qu'au moins $100p\,\%$ des données sont $\le x_p$ et au moins $100(1-p)\,\%$ sont $\ge x_p$.

**Théorème** : pour les données ordonnées, $x_{(i)}$ est le $100p$-ième percentile avec $p = (i - 1/2)/n$.

Exemple : pour $n = 10$ valeurs ordonnées, $x_{(3)}$ est le 25e percentile, puisque $(3 - 1/2)/10 = 0{,}25$ ; au moins 3 valeurs sur 10 sont $\le x_{(3)}$ et au moins 8 sur 10 sont $\ge x_{(3)}$. Il existe plusieurs conventions de calcul des percentiles et des quartiles (interpolation ou non entre deux valeurs) : c'est pourquoi les logiciels donnent des résultats un peu différents de la méthode « médiane des moitiés » vue plus bas. [[Complément hors du cours|ⓘ]]

- Le **quartile inférieur** est $x_{0{,}25}$ : 25 % des données sont en dessous ou égales, 75 % au-dessus ou égales.
- Le **quartile supérieur** est $x_{0{,}75}$ : 75 % des données sont en dessous ou égales, et « au-dessus ou égales » … (phrase coupée dans le cours).

### Moyenne et médiane de population

![[Chp2 - Descriptive statistics - image15.png]]

*Figure : trois formes de distribution de population : (a) asymétrie négative, $\mu < \tilde{\mu}$ ; (b) symétrique, $\mu = \tilde{\mu}$ ; (c) asymétrie positive, $\tilde{\mu} < \mu$.*

### Mesures de dispersion

- **Étendue** (*range*, voir [[Étendue (statistique)]]) :
$$\text{Range} = \max_{i=1,\dots,n}(x_i) - \min_{i=1,\dots,n}(x_i)$$
- **Somme des écarts à la moyenne** : $\sum_{i=1}^{n} (x_i - \bar{x}) = 0$.

L'étendue est simple mais ne dépend que des deux valeurs extrêmes, donc très sensible à une valeur aberrante. La somme des écarts est nulle parce que $\sum (x_i - \bar{x}) = \sum x_i - n\bar{x} = n\bar{x} - n\bar{x} = 0$ : les écarts positifs et négatifs se compensent, si bien que leur moyenne ne mesure pas la dispersion. On les élève donc au carré (variance) ou l'on prend leur valeur absolue (écart absolu moyen). [[Complément hors du cours|ⓘ]]

### Écart-type et variance d'échantillon

([[Variance et écart-type d'échantillon]])

**Définition** : soit $S_{xx} = \sum (x_i - \bar{x})^2$, la somme des carrés des écarts à la moyenne. L'**écart-type d'échantillon** (*sample standard deviation*) est
$$s = \sqrt{\frac{S_{xx}}{n-1}} = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n-1}},$$
et $s^2$ est la **variance d'échantillon** (*sample variance*).

**Proposition** (forme alternative du numérateur) :
$$S_{xx} = \sum (x_i - \bar{x})^2 = \sum x_i^2 - n\bar{x}^2 = \sum x_i^2 - \frac{\left(\sum x_i\right)^2}{n}$$

**Démonstration** (ajoutée dans la note) :
$$\sum (x_i - \bar{x})^2 = \sum \left(x_i^2 - 2x_i\bar{x} + \bar{x}^2\right) = \sum x_i^2 - 2\bar{x}\sum x_i + n\bar{x}^2$$
et comme $\sum x_i = n\bar{x}$ :
$$= \sum x_i^2 - 2n\bar{x}^2 + n\bar{x}^2 = \sum x_i^2 - n\bar{x}^2.$$

Exemple de calcul sur les dix mesures de l'histogramme : $\sum x_i = 24{,}7$, donc $\bar{x} = 2{,}47$ ; $\sum x_i^2 = 61{,}53$, donc $S_{xx} = 61{,}53 - 24{,}7^2/10 = 61{,}53 - 61{,}009 = 0{,}521$ ; puis $s^2 = 0{,}521/9 \approx 0{,}0579$ et $s \approx 0{,}241$. [[Complément hors du cours|ⓘ]]

La variance s'exprime dans le carré de l'unité des données ; l'écart-type, dans la même unité, se lit directement à côté de la moyenne. La forme $\sum x_i^2 - n\bar{x}^2$ est commode à la main mais, en machine, elle peut perdre de la précision quand les valeurs sont grandes et peu dispersées : les logiciels calculent plutôt à partir des écarts. [[Complément hors du cours|ⓘ]]

**Degrés de liberté** : on dit que $s$ repose sur $n - 1$ degrés de liberté (*df*). Les $n$ écarts $x_1 - \bar{x}, \dots, x_n - \bar{x}$ ont une somme nulle : en fixer $n - 1$ détermine le dernier. Exemple : $n = 4$, $x_1 - \bar{x} = 8$, $x_2 - \bar{x} = -6$, $x_4 - \bar{x} = -4$, donc forcément $x_3 - \bar{x} = 2$ : trois valeurs seulement sont « libres » (3 df).

**Correction de Bessel** (explication ajoutée dans la note) : avec un seul échantillon, on ne connaît pas $\mu$ et on l'estime par $\bar{x}$. Or $\bar{x}$ est calculée à partir des données elles-mêmes : elle « colle » aux données et réduit artificiellement la variabilité. Pour corriger ce biais, on divise par $n - 1$ au lieu de $n$.

Le résultat précis est que, pour des observations indépendantes de variance $\sigma^2$, $E(S^2) = \sigma^2$ : $S^2$ est un [[Estimateur|estimateur sans biais]] de $\sigma^2$, alors que $\frac{1}{n}\sum (X_i - \bar{X})^2$ a pour espérance $\frac{n-1}{n}\sigma^2$ et sous-estime donc la variance. L'écart vient de ce que $\sum (x_i - c)^2$ est minimale pour $c = \bar{x}$ : elle est toujours inférieure ou égale à $\sum (x_i - \mu)^2$. L'écart-type $s$, lui, reste légèrement biaisé, la racine ne conservant pas l'espérance. [[Complément hors du cours|ⓘ]]

**Ce que dit l'écart-type.** L'**inégalité de Bienaymé-Tchebychev**, valable pour toute distribution, garantit qu'au moins $1 - 1/k^2$ des valeurs sont à moins de $k$ écarts-types de la moyenne : au moins 75 % à moins de $2s$, au moins 89 % à moins de $3s$ (voir [[Espérance et variance]]). Pour une distribution en cloche, proche d'une [[Loi normale|loi normale]], la **règle empirique** est bien plus précise : environ 68 %, 95 % et 99,7 % des valeurs à moins de 1, 2 et 3 écarts-types. [[Complément hors du cours|ⓘ]]

### Moyenne et variance de population

Pour une population finie de taille $N$ :
$$\mu = \sum_{i=1}^{N} \frac{x_i}{N}, \qquad \sigma^2 = \sum_{i=1}^{N} \frac{(x_i - \mu)^2}{N}.$$
Pour une population infinie, on suppose une loi de probabilité associée aux valeurs de la variable : la variable est une [[Variable aléatoire|variable aléatoire]] de cette loi, sa moyenne est son espérance et sa variance celle de la variable aléatoire, comme au cours de probabilités ([[Espérance et variance]]).

### Écart interquartile et valeurs aberrantes

**Définition** : on ordonne les $n$ observations et on sépare la moitié inférieure de la moitié supérieure ; la médiane est dans les deux moitiés si $n$ est impair. Le **quartile inférieur** (premier quartile) $q_1$ est la médiane de la moitié inférieure ; le **quartile supérieur** (troisième quartile) $q_3$ est la médiane de la moitié supérieure.

Mesure de dispersion résistante aux valeurs aberrantes, l'**écart interquartile** :
$$\text{iqr} = q_3 - q_1$$

L'écart interquartile est la largeur de l'intervalle qui contient les 50 % centraux des données ; comme la médiane, il ne bouge pas si l'on modifie les valeurs extrêmes, à l'inverse de l'étendue et de l'écart-type. On l'associe donc à la médiane pour décrire une distribution asymétrique ou avec des valeurs aberrantes, et on réserve le couple moyenne et écart-type aux distributions à peu près symétriques. [[Complément hors du cours|ⓘ]]

**Définition** : toute observation à plus de $1{,}5\,\text{iqr}$ du quartile le plus proche est une **valeur aberrante** ; elle est **extrême** si elle est à plus de $3\,\text{iqr}$ du quartile le plus proche, **modérée** (*mild*) sinon. Autrement dit :
$$x < q_1 - 1{,}5\,\text{iqr} \quad \text{ou} \quad x > q_3 + 1{,}5\,\text{iqr}.$$

**Procédure du dessin** (« diviser les données en quatre groupes égaux et voir à quelle distance sont les groupes extrêmes ») :

1. Ranger les données par ordre croissant.
2. Couper les données à la médiane en deux groupes égaux : bas (*low*) et haut (*high*).
3. La médiane du groupe bas est le premier quartile $Q_1$.
4. La médiane du groupe haut est le troisième quartile $Q_3$ (la médiane est le deuxième quartile).

$IQR = Q_3 - Q_1$ ; une valeur aberrante tombe hors de $\left[Q_1 - \tfrac{3}{2}\text{IQR},\ Q_3 + \tfrac{3}{2}\text{IQR}\right]$.

![[Chp2 - Descriptive statistics - image6.png]]

*Figure : dessin manuscrit : colonne de données ordonnées coupée à la médiane en « lows » et « highs » ; $Q_1$ médiane des bas, $Q_3$ médiane des hauts.*
