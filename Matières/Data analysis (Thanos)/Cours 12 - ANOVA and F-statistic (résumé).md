---
type: source
tags: [year3]
sources: ["[[Cours 12 - ANOVA and F-statistic]]"]
maj: 2026-11-05
---

Résumé de [[Cours 12 - ANOVA and F-statistic]], dans [[Data analysis (Thanos) (matière)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

L'[[ANOVA]] teste si trois populations ou plus ont la même moyenne, en comparant la variation entre groupes à la variation dans les groupes. Sa statistique est la [[Statistique F]]. Le cours finit en reliant l'ANOVA à la régression simple.

## Contenu, dans l'ordre du cours

- **Définition** : technique pour tester si trois moyennes de population ou plus sont toutes égales. À un facteur, on compare des groupes sur une variable ; à deux facteurs, sur deux. On étudie l'effet de variables qualitatives (les facteurs, dont les caractéristiques sont les niveaux) sur une variable quantitative.
- **Hypothèse nulle** : toutes les moyennes de population sont exactement égales. Les moyennes d'échantillon diffèrent un peu par hasard, mais pas trop : si elles diffèrent beaucoup, on ne croit plus à l'égalité.
- **Exemple des QI** : trois écoles de 1000 enfants, échantillon de 10 par école. Moyennes 99,2 ; 112,6 ; 93,3 ; variances 111,1 ; 205,6 ; 160,5 ; total 101,7 pour 30 enfants. On voudrait montrer que l'hypothèse « mêmes moyennes » n'est pas crédible.
- **Trois scénarios théoriques** (variance intra-école 50, 100, 500) : plus la variance dans les écoles est grande, plus les moyennes d'échantillon peuvent différer entre elles.
- **ANOVA à un facteur** : on partage la variation totale en variation intra-groupe et variation inter-groupes. $H_0$ : pas de différence, moyennes égales. $H_1$ : au moins une différence.
- **Conditions** : normalité de chaque échantillon, indépendance des échantillons, égalité des variances, variable dépendante continue.
- **Lien avec F** : la statistique F sort d'une ANOVA ou d'une régression. Le test $t$ dit si une variable est significative, le test F si un groupe de variables l'est ensemble. $F = \dfrac{\text{variance inter-groupes}}{\text{variance intra-groupe}}$.
- **Rejet** : on rejette $H_0$ si la p-value est inférieure à $\alpha$.
- **Test $t$ contre test F** : le test $t$ compare deux moyennes (statistique de la loi de Student), le test F compare deux variances de populations normales (loi de Snedecor).
- **Tableau d'ANOVA** :

| Source | df | Somme des carrés | MS | F |
|---|---|---|---|---|
| Groupe | $k-1$ | $SST_G$ | $SST_G/(k-1)$ | $\dfrac{SST_G/(k-1)}{SST_E/(N-k)}$ |
| Erreur | $N-k$ | $SST_E$ | $SST_E/(N-k)$ | |
| Total | $N-1$ | $SST$ | | |

- **Exemple numérique** : trois échantillons de 5 valeurs, $SSW + SSB = SST$ avec $SSW = 54$, $SSB = 203{,}3$, $SST = 257{,}3$. $MS_B = 203{,}3/2 = 101{,}667$ ; $MS_W = 54/(15-3) = 4{,}5$ ; $F(2,12) = 22{,}59$. Valeur critique 3,89 lue dans la table ($df_1 = 2$, $df_2 = 12$) : rejet de $H_0$.
- **ANOVA contre $t$** : le $t$ compare deux populations, l'ANOVA plus de deux. Faire une suite de tests $t$ multiplie les comparaisons par paires, alors que l'ANOVA donne un seul F et une seule p-value.
- **ANOVA à deux facteurs** : chaque échantillon est classé de deux manières. Il y a trois paires d'hypothèses (effet de chaque facteur et effet de l'un sur l'autre). Conditions : variable dépendante continue, deux variables indépendantes catégorielles en groupes indépendants, indépendance, égalité des variances, normalité.
- **Régression simple et ANOVA** : la régression linéaire simple est un cas particulier d'ANOVA. On part de $y_i - \bar{y} = (y_i - \hat{y}_i) + (\hat{y}_i - \bar{y})$ ; le terme croisé s'annule (« en sautant un peu d'algèbre »), d'où $SST = SSR + SSE$. On divise ensuite par les degrés de liberté pour obtenir les carrés moyens. Voir [[Régression linéaire]].
- **Différence clé** (dernière diapositive) : en ANOVA, aucune hypothèse n'est faite sur la manière dont le prix et le volume de ventes sont liés.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **« F = 22,59, p > 0,05 »** : image lue directement, la diapositive l'écrit ainsi. Or $F = 22{,}59$ dépasse la valeur critique 3,89, donc $p < 0{,}05$ et le schéma même de la diapositive classe $F$ dans la région de rejet (complément). Alerte de la transcription confirmée. **À corriger avant un examen.**
2. **Sommes de l'exemple numérique** : image lue directement. Avec les valeurs affichées (2, 3, 7, 2, 6 ; 10, 3, 7, 2, 6 ; 10, 13, 14, 13, 15), je trouve $SSW = 77{,}2$, $SSB \approx 230{,}5$ et $SST \approx 307{,}7$, pas 54, 203,3 et 257,3 (complément). La structure $SSW + SSB = SST$ et les degrés de liberté sont justes, mais les valeurs affichées ne viennent pas de ces données ($F$ vaudrait alors environ 18, toujours dans la région de rejet). Ne pas refaire le calcul à l'examen avec ces nombres.
3. **Règle de rejet** : « on ne rejette pas $H_0$ si la valeur critique est plus petite que $F$ » est fausse, on rejette dans ce cas (complément, voir [[Cours 11 - Multiple Linear Regression and F-statistic (résumé)|Cours 11]]).
4. **Tableau $t$ contre F** : le test F est présenté comme test d'égalité de variances de deux populations, alors que l'ANOVA l'utilise pour comparer des moyennes. Les deux usages sont corrects, mais le cours ne fait pas le lien.
5. **Dernière diapositive coupée** : « KEY DIFFERENCE : in ANOVA → no assumption is made about the manner in which Price and Sales Volume are related » s'arrête là, sans le pendant côté régression (le contraste attendu est que la régression suppose une relation linéaire). Les mots « Price » et « Sales Volume » ne sont expliqués nulle part dans la note.
6. **Fragments illisibles** (numéros de page, bord d'image coupé) : sans importance.
