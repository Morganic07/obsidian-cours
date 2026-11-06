---
type: source
tags: [year3]
sources: ["[[Chp2 - Descriptive statistics]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Chp2 - Descriptive statistics]], dans [[Statistics (matière)]] : résumer un jeu de données par des graphiques, puis par des indicateurs de position (moyenne, médiane, quartiles) et de dispersion (étendue, variance, écart interquartile). Voir [[Statistique descriptive]]. En cas d'écart, le cours et ses images font foi. Les images n'ont pas été ouvertes : seules leurs transcriptions ont été lues.

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

### Diagramme en points (*dotplot*)

([[Diagramme en points]])

![[Cours/Year 3/Statistics/medias/Chp2 - Descriptive statistics/image16.png]]

*Figure : diagramme en points de l'indice Big Mac (en \$US) de 56 pays, sur un axe de 2,0 à 6,5 ; la valeur des États-Unis (5,58 \$) est signalée ; la plupart des points sont entre 2 et 4,6.*

### Histogramme

([[Histogramme]])

Exemple : dix mesures 2,1 ; 2,4 ; 2,2 ; 2,3 ; 2,7 ; « .2.5 » (sic, sans doute 2,5) ; 2,4 ; 2,6 ; 2,6 ; 2,9. Pour visualiser leur histogramme de [[Fréquence relative|fréquence relative]] :

1. diviser l'axe des mesures en intervalles de même largeur (ici 0,2, à partir de 2,05) ;
2. placer sur chaque intervalle un rectangle de hauteur proportionnelle à la fréquence ou à la fréquence relative des mesures qui y tombent.

Classes (*class intervals*) : chaque observation appartient à exactement une classe.

![[Cours/Year 3/Statistics/medias/Chp2 - Descriptive statistics/image11.png]]

*Figure : histogramme de fréquence relative des dix mesures, classes de 2,05 à 3,05 de largeur 0,2.*

$$\text{Fréquence relative} = \frac{\text{nombre d'occurrences de la valeur}}{\text{nombre d'observations de l'échantillon}}$$

### Densité

$$\text{Densité d'une classe} = \frac{\text{fréquence relative de la classe}}{\text{largeur de la classe}}$$

Dans un histogramme (à classes inégales), la hauteur du rectangle de chaque classe est sa densité ; l'échelle verticale s'appelle alors **échelle de densité** (*density scale*).

![[Cours/Year 3/Statistics/medias/Chp2 - Descriptive statistics/image25.png]]

*Figure : histogramme de densité, à classes de largeurs inégales, du coût annuel de carburant attendu (centaines de dollars) ; pic d'environ 0,12 entre 15 et 17,5.*

Note du cours : si la valeur vaut 15 pile, elle va dans l'intervalle supérieur.

### Formes de distribution

([[Forme d'une distribution]])

![[Cours/Year 3/Statistics/medias/Chp2 - Descriptive statistics/image19.png]]

*Figure : histogrammes lissés : (a) symétrique unimodal ; (b) bimodal ; (c) asymétrie positive (queue à droite) ; (d) asymétrie négative (queue à gauche).*

### Choix des classes

- Une observation peut tomber sur une borne de classe (par exemple 29,0) et n'appartenir alors à aucune classe unique.
- **Convention** : toute observation sur une borne va dans la classe **à sa droite** ; 29,0 va dans 29,0–29,5 et non dans 28,5–29,0.
- Plus il y a d'observations, plus il faut de classes. Règle raisonnable :
$$\text{nombre de classes} \approx \sqrt{\text{nombre d'observations}}$$

![[Cours/Year 3/Statistics/medias/Chp2 - Descriptive statistics/image14.png]]

*Figure : choix des classes pour des points « étirés » : (a) beaucoup d'intervalles courts de même largeur ; (b) quelques intervalles larges de même largeur ; (c) intervalles de largeurs inégales.*

### Distribution de fréquences

Une **distribution de fréquences** est un tableau des fréquences et/ou des fréquences relatives. Exemple : salaires de départ annuels de 42 personnes (en milliers).

| Salaire | 57 | 58 | 59 | 60 | 61 | 62 | 63 | 64 | 66 | 67 | 70 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Fréquence (tableau 2.1) | 4 | 1 | 3 | 5 | 8 | 10 | 0 | 5 | 2 | 3 | 1 |
| Fréquence relative (tableau 2.2) | 4/42 = 0,0952 | 1/42 = 0,0238 | 3/42 | 5/42 | 8/42 | 10/42 | 0 | 5/42 | 2/42 | 3/42 | 1/42 |

### Données catégorielles

Diagrammes circulaires (*pie charts*) et diagrammes en barres (*bar graphs*) : voir [[Diagramme en barres et diagramme circulaire]].

![[Cours/Year 3/Statistics/medias/Chp2 - Descriptive statistics/image17.png]]

*Figure : diagramme circulaire des locuteurs natifs de l'anglais (USA, UK, Canada, Australia, Other) ; diagrammes en barres verticales et horizontales de la couleur des yeux (marron environ 13, vert 8, bleu 4, noir 1 ; « marron » est la modalité la plus fréquente).*

### Boîte à moustaches (*box plot*, *box-and-whiskers plot*)

([[Quartiles et valeurs aberrantes]])

Construction :

1. Tracer une échelle de mesure (horizontale ou verticale).
2. Tracer un rectangle le long de l'axe, de $q_1$ à $q_3$ (sa longueur vaut donc l'iqr).
3. Placer un segment à la médiane. Sa position par rapport aux deux bords renseigne sur l'asymétrie des 50 % centraux.
4. Repérer les valeurs aberrantes (*outliers*) et marquer chacune individuellement (symboles éventuellement différents pour les modérées et les extrêmes ; la plupart des logiciels ne les distinguent pas).
5. Tracer les « moustaches » depuis chaque bord du rectangle jusqu'à la plus petite et la plus grande observation **qui ne sont pas aberrantes**.

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

- Résumé : « $\bar{x} = 92{,}17$ » (en fait la médiane, voir les points à vérifier), $q_1 = 45{,}64$, $q_3 = 167{,}79$, $\text{iqr} = 122{,}15$, $1{,}5\,\text{iqr} = 183{,}225$, $3\,\text{iqr} = 366{,}45$. Les logiciels peuvent donner des valeurs légèrement différentes.
- En bas : $q_1 - 1{,}5\,\text{iqr} < 0$ et aucune observation n'est négative, donc pas de valeur aberrante basse.
- En haut : $q_3 + 1{,}5\,\text{iqr} = 351{,}015$ et $q_3 + 3\,\text{iqr} = 534{,}24$. Donc 563,92, 690,11, 826,54 et 1529,35 sont des aberrantes **extrêmes** ; 352,09, 371,47, 444,68 et 460,86 sont **modérées**.

![[Cours/Year 3/Statistics/medias/Chp2 - Descriptive statistics/image22.png]]

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

### Médiane d'échantillon

**Définition** : on ordonne les $n$ observations de la plus petite à la plus grande (valeurs répétées comprises). Alors
$$\tilde{x} = \begin{cases} \text{valeur de rang } \frac{n+1}{2} & \text{si } n \text{ impair} \\ \text{moyenne des valeurs de rangs } \frac{n}{2} \text{ et } \frac{n}{2}+1 & \text{si } n \text{ pair} \end{cases}$$

**Exemple** : 62,3 ; 62,8 ; 63,6 ; 65,2 ; 65,7 ; 66,4 ; 67,4 ; 68,4 ; 68,8 ; 70,8 ; 75,7 ; 79,0. Comme $n = 12$ est pair, la médiane est la moyenne des 6e et 7e valeurs :
$$\tilde{x} = \frac{66{,}4 + 67{,}4}{2} = 66{,}90 \text{ min}.$$

### Percentiles

([[Quantile]])

**Définition** : pour $0 < p < 1$, un $100p$-ième percentile est toute valeur $x_p$ telle qu'au moins $100p\,\%$ des données sont $\le x_p$ et au moins $100(1-p)\,\%$ sont $\ge x_p$.

**Théorème** : pour les données ordonnées, $x_{(i)}$ est le $100p$-ième percentile avec $p = (i - 1/2)/n$.

- Le **quartile inférieur** est $x_{0{,}25}$ : 25 % des données sont en dessous ou égales, 75 % au-dessus ou égales.
- Le **quartile supérieur** est $x_{0{,}75}$ : 75 % des données sont en dessous ou égales, et « au-dessus ou égales » … (phrase coupée dans le cours).

### Moyenne et médiane de population

![[Cours/Year 3/Statistics/medias/Chp2 - Descriptive statistics/image15.png]]

*Figure : trois formes de distribution de population : (a) asymétrie négative, $\mu < \tilde{\mu}$ ; (b) symétrique, $\mu = \tilde{\mu}$ ; (c) asymétrie positive, $\tilde{\mu} < \mu$.*

### Mesures de dispersion

- **Étendue** (*range*, voir [[Étendue (statistique)]]) :
$$\text{Range} = \max_{i=1,\dots,n}(x_i) - \min_{i=1,\dots,n}(x_i)$$
- **Somme des écarts à la moyenne** : $\sum_{i=1}^{n} (x_i - \bar{x}) = 0$.

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

**Degrés de liberté** : on dit que $s$ repose sur $n - 1$ degrés de liberté (*df*). Les $n$ écarts $x_1 - \bar{x}, \dots, x_n - \bar{x}$ ont une somme nulle : en fixer $n - 1$ détermine le dernier. Exemple : $n = 4$, $x_1 - \bar{x} = 8$, $x_2 - \bar{x} = -6$, $x_4 - \bar{x} = -4$, donc forcément $x_3 - \bar{x} = 2$ : trois valeurs seulement sont « libres » (3 df).

**Correction de Bessel** (explication ajoutée dans la note) : avec un seul échantillon, on ne connaît pas $\mu$ et on l'estime par $\bar{x}$. Or $\bar{x}$ est calculée à partir des données elles-mêmes : elle « colle » aux données et réduit artificiellement la variabilité. Pour corriger ce biais, on divise par $n - 1$ au lieu de $n$.

### Moyenne et variance de population

Pour une population finie de taille $N$ :
$$\mu = \sum_{i=1}^{N} \frac{x_i}{N}, \qquad \sigma^2 = \sum_{i=1}^{N} \frac{(x_i - \mu)^2}{N}.$$
Pour une population infinie, on suppose une loi de probabilité associée aux valeurs de la variable : la variable est une [[Variable aléatoire|variable aléatoire]] de cette loi, sa moyenne est son espérance et sa variance celle de la variable aléatoire, comme au cours de probabilités ([[Espérance et variance]]).

### Écart interquartile et valeurs aberrantes

**Définition** : on ordonne les $n$ observations et on sépare la moitié inférieure de la moitié supérieure ; la médiane est dans les deux moitiés si $n$ est impair. Le **quartile inférieur** (premier quartile) $q_1$ est la médiane de la moitié inférieure ; le **quartile supérieur** (troisième quartile) $q_3$ est la médiane de la moitié supérieure.

Mesure de dispersion résistante aux valeurs aberrantes, l'**écart interquartile** :
$$\text{iqr} = q_3 - q_1$$

**Définition** : toute observation à plus de $1{,}5\,\text{iqr}$ du quartile le plus proche est une **valeur aberrante** ; elle est **extrême** si elle est à plus de $3\,\text{iqr}$ du quartile le plus proche, **modérée** (*mild*) sinon. Autrement dit :
$$x < q_1 - 1{,}5\,\text{iqr} \quad \text{ou} \quad x > q_3 + 1{,}5\,\text{iqr}.$$

**Procédure du dessin** (« diviser les données en quatre groupes égaux et voir à quelle distance sont les groupes extrêmes ») :

1. Ranger les données par ordre croissant.
2. Couper les données à la médiane en deux groupes égaux : bas (*low*) et haut (*high*).
3. La médiane du groupe bas est le premier quartile $Q_1$.
4. La médiane du groupe haut est le troisième quartile $Q_3$ (la médiane est le deuxième quartile).

$IQR = Q_3 - Q_1$ ; une valeur aberrante tombe hors de $\left[Q_1 - \tfrac{3}{2}\text{IQR},\ Q_3 + \tfrac{3}{2}\text{IQR}\right]$.

![[Cours/Year 3/Statistics/medias/Chp2 - Descriptive statistics/image6.png]]

*Figure : dessin manuscrit : colonne de données ordonnées coupée à la médiane en « lows » et « highs » ; $Q_1$ médiane des bas, $Q_3$ médiane des hauts.*

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Exemple de la boîte à moustaches : « $\bar{x} = 92{,}17$ »** : image non ouverte pour ce point, mais le calcul tranche. 92,17 est la 29e des 57 valeurs triées : c'est la médiane, pas la moyenne. Le symbole devrait être $\tilde{x}$ (complément).
2. **Définition des quartiles, deux versions** : la définition ($q_1$, $q_3$ médianes des moitiés, médiane incluse si $n$ impair) diffère de la procédure du dessin (« divide the data at the median into two equal groups »), qui ne dit rien de la médiane. Les logiciels donnent d'ailleurs des valeurs légèrement différentes, comme le cours le dit.
3. **Phrase coupée** : la note de définition des percentiles s'arrête net : « The upper quartile is $x_{0.75}$, the value “at or below” which 75 % of the data points lie, and “at or above” which ». La suite (25 % des données) manque.
4. **Alertes de la transcription** : la valeur 65 absente des tableaux de salaires (de 64 à 66) et le « .2.5 » de l'histogramme sont des défauts de l'image, non des erreurs de fond. Image non ouverte, ne rien reprendre de ces valeurs.
5. **Tableau de salaires** : les fréquences du tableau 2.1 somment à 42, comme l'indique le dénominateur du tableau 2.2 ; la transcription signale que 3, 5, 8 et 0 sont flous sur l'image.
6. **Données du tige et feuilles** : la transcription signale des lignes de longueurs inégales (10 et 8 valeurs) ; le tableau compte 38 valeurs. Ne pas s'y fier pour un calcul sans ouvrir l'image.
7. **Lien automatique « sample median »** : dans la note, « sample median » pointe vers [[Variance et écart-type d'échantillon]] ; c'est un faux lien (la médiane relève des [[Mesures de tendance centrale]]).
