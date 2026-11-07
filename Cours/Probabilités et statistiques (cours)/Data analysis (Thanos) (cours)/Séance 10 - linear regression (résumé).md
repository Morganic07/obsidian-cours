---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 10 : linear regression.docx|Cours 10 - linear regression]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 3/Data analysis (Thanos)/Cours 10 : linear regression.docx|Cours 10 - linear regression]], dans [[Data analysis (Thanos) (index)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Régression linéaire simple : modèle, ajustement par les [[Moindres carrés|moindres carrés]], décomposition de la variation, conditions de validité vérifiées sur les résidus, test de la pente. Voir [[Régression linéaire]].

## Types de modèles probabilistes

Les modèles probabilistes se divisent en **modèles de régression** (*regression models*) et **modèles de corrélation** (*correlation models*).

![[Séance 10 - linear regression - image25.png]]

*Figure : les modèles probabilistes, divisés en modèles de régression et de corrélation.*

## Quatuor d'Anscombe (*Anscombe's quartet*)

Le [[Quatuor d'Anscombe]] illustre un point crucial : **il ne faut jamais se fier uniquement aux calculs numériques, il faut toujours visualiser ses données**. Créé en 1973 par le statisticien Francis Anscombe, il se compose de quatre jeux de données identiques du point de vue des [[Statistique descriptive|statistiques descriptives]], mais radicalement différents une fois tracés.

| | I x | I y | II x | II y | III x | III y | IV x | IV y |
|---|---|---|---|---|---|---|---|---|
| | 10 | 8,04 | 10 | 9,14 | 10 | 7,46 | 8 | 6,58 |
| | 8 | 6,95 | 8 | 8,14 | 8 | 6,77 | 8 | 5,76 |
| | 13 | 7,58 | 13 | 8,74 | 13 | 12,74 | 8 | 7,71 |
| | 9 | 8,81 | 9 | 8,77 | 9 | 7,11 | 8 | 8,84 |
| | 11 | 8,33 | 11 | 9,26 | 11 | 7,81 | 8 | 8,47 |
| | 14 | 9,96 | 14 | 8,1 | 14 | 8,84 | 8 | 7,04 |
| | 6 | 7,24 | 6 | 6,13 | 6 | 6,08 | 8 | 5,25 |
| | 4 | 4,26 | 4 | 3,1 | 4 | 5,39 | 19 | 12,5 |
| | 12 | 10,84 | 12 | 9,13 | 12 | 8,15 | 8 | 5,56 |
| | 7 | 4,82 | 7 | 7,26 | 7 | 6,42 | 8 | 7,91 |
| | 5 | 5,68 | 5 | 4,74 | 5 | 5,73 | 8 | 6,89 |
| SUM | 99,00 | 82,51 | 99,00 | 82,51 | 99,00 | 82,50 | 99,00 | 82,51 |
| AVG | 9,00 | 7,50 | 9,00 | 7,50 | 9,00 | 7,50 | 9,00 | 7,50 |
| STDEV | 3,32 | 2,03 | 3,32 | 2,03 | 3,32 | 2,03 | 3,32 | 2,03 |

Pour chaque jeu : moyenne de $x$ = 9, moyenne de $y$ = 7,50, variance de $x$ = 11, variance de $y$ = 4,13, et [[Covariance et corrélation|coefficient de corrélation]] (force de la relation entre deux variables) entre $x$ et $y$ = 0,816.

![[Séance 10 - linear regression - image7.png]]

*Figure : les quatre nuages de points du quatuor, avec la même droite de régression.*

Les quatre jeux ont aussi la **même droite de régression**, mais chacun raconte une histoire différente :

- **Jeu I** : modèle linéaire propre et bien ajusté.
- **Jeu II** : « n'est pas distribué normalement » (selon le cours) ; les points suivent une courbe parabolique.
- **Jeu III** : la distribution est linéaire, mais la régression calculée est faussée par une [[Quartiles et valeurs aberrantes|valeur aberrante]] (*outlier*).
- **Jeu IV** : une seule valeur aberrante suffit à produire un coefficient de corrélation élevé (tous les points sont à $x = 8$ sauf un à $x = 19$).

Le quatuor souligne l'importance de la **visualisation** : regarder les données révèle leur structure.

## Modèles de régression

- Répondent à la question « quelle est la relation entre les variables ? ».
- Équation utilisée : $y = ax + b$.
  - Ce qu'on prédit ($y$) : **une** variable **dépendante** (réponse, *response*) **numérique**.
  - Prédite par : **une ou plusieurs** variables **indépendantes** (explicatives, *explanatory*), **numériques ou catégorielles** : $y = a_1x_1 + a_2x_2 + \cdots + a_nx_n + b$. Voir [[Variable cible et variable explicative]].
- Servent surtout à la **prédiction et l'estimation**.

Classement :

- **Simple** : 1 variable explicative → linéaire ou non linéaire ;
- **Multiple** : 2 variables explicatives ou plus → linéaire ou non linéaire.

Ce cours traite la régression **simple linéaire**.

![[Séance 10 - linear regression - image28.png]]

*Figure : arbre de classification des modèles de régression (simple / multiple, linéaire / non linéaire).*

## Modèle de régression linéaire

Voir [[Régression linéaire]].

$$y = \beta_0 + \beta_1 x + \varepsilon$$

- $y$ : variable dépendante (réponse) ;
- $\beta_0$ : ordonnée à l'origine de la population (*population y-intercept*) ;
- $\beta_1$ : pente de la population (*population slope*) ;
- $x$ : variable indépendante (explicative) ;
- $\varepsilon$ : erreur aléatoire (*random error*).

La **droite des moyennes** (*line of means*) est $E(y) = \beta_0 + \beta_1 x$ : $\beta_1$ est la pente (variation de $y$ sur variation de $x$), $\beta_0$ l'ordonnée à l'origine. Chaque observation s'écrit $y_i = \beta_0 + \beta_1 x_i + \varepsilon_i$, où $\varepsilon_i$ est l'écart vertical entre la valeur observée et la droite.

![[Séance 10 - linear regression - image29.png]]![[Séance 10 - linear regression - image1.png]]

*Figure : la droite des moyennes, sa pente et son ordonnée à l'origine ; à droite, l'erreur aléatoire $\varepsilon_i$ entre un point observé et la droite.*

## Méthode des moindres carrés (*least squares*)

Comment tracer une droite à travers les points, et laquelle « ajuste le mieux » ?

![[Séance 10 - linear regression - image3.png]]

*Figure : un nuage de six points traversé par plusieurs droites candidates.*

Le meilleur ajustement minimise l'écart entre les valeurs **réelles** de $y$ et les valeurs **prédites**. Mais les écarts positifs et négatifs se compensent : on minimise donc la **somme des carrés des erreurs** ([[Somme des carrés (SST, SSR, SSE)|SSE]]) :

$$\sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = \sum_{i=1}^{n} \hat{\varepsilon}_i^2$$

Voir [[Moindres carrés]]. Avec 4 points : on minimise $\hat{\varepsilon}_1^2 + \hat{\varepsilon}_2^2 + \hat{\varepsilon}_3^2 + \hat{\varepsilon}_4^2$, où $y_i = \hat{\beta}_0 + \hat{\beta}_1 x_i + \hat{\varepsilon}_i$ et $\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$.

![[Séance 10 - linear regression - image27.png]]

*Figure : les écarts $\hat{\varepsilon}_1$ à $\hat{\varepsilon}_4$ entre chaque point et sa valeur prédite sur la droite.*

### Méthode par les dérivées partielles

Points $(1,1)$, $(2,1)$, $(3,3)$ ; droite $y = b + mx$, où $b$ et $m$ sont les variables.

![[Séance 10 - linear regression - image12.png]]

*Figure : les trois points, la droite $y = b + mx$ et les distances verticales jusqu'aux points $(1, b+m)$, $(2, b+2m)$, $(3, b+3m)$.*

**But** : minimiser la fonction $f(b,m)$, somme des carrés des 3 distances verticales des points à la droite :

$$f(b,m) = [1-(b+m)]^2 + [1-(b+2m)]^2 + [3-(b+3m)]^2$$

On cherche les points critiques ([[Dérivée partielle]], [[Extremum local d'une fonction de deux variables]]) :

- $\dfrac{\partial f}{\partial b} = f_b(b,m) = -10 + 6b + 12m = 0$ (le cours écrit « $+12$ », voir Points à vérifier) ;
- $\dfrac{\partial f}{\partial m} = f_m(b,m) = -24 + 12b + 28m = 0$.

D'où $(b,m) = \left(-\dfrac{1}{3}, 1\right)$.

$D = f_{bb} f_{mm} - (f_{bm})^2 = 24 > 0$ (théorème de calcul multivariable / analyse dans $\mathbb{R}^n$) et $f_{bb} = 6 > 0$ : **minimum local**. Le graphe de $f$ est une « cuvette parabolique » (*parabolic bowl*), donc ce minimum local est aussi le **minimum global**.

Droite des moindres carrés : $y = x - \dfrac{1}{3}$.

## Équations des coefficients

Équation de prédiction : $\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x$.

**Pente** :

$$\hat{\beta}_1 = \frac{SS_{xy}}{SS_{xx}} = \frac{\sum_{i=1}^{n} x_i y_i - \dfrac{\left(\sum_{i=1}^{n} x_i\right)\left(\sum_{i=1}^{n} y_i\right)}{n}}{\sum_{i=1}^{n} x_i^2 - \dfrac{\left(\sum_{i=1}^{n} x_i\right)^2}{n}}$$

**Ordonnée à l'origine** : $\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$.

### Exemple : engrais et rendement

Économiste d'une coopérative de comté, on recueille ces données ; trouver la droite des moindres carrés reliant le rendement (*yield*) à l'engrais (*fertilizer*).

| $x_i$ (engrais, kg) | $y_i$ (rendement, kg) | $x_i^2$ | $y_i^2$ | $x_i y_i$ |
|---|---|---|---|---|
| 4 | 3,0 | 16 | 9,00 | 12 |
| 6 | 5,5 | 36 | 30,25 | 33 |
| 10 | 6,5 | 100 | 42,25 | 65 |
| 12 | 9,0 | 144 | 81,00 | 108 |
| **32** | **24,0** | **296** | **162,50** | **218** |

![[Séance 10 - linear regression - image16.png]]![[Séance 10 - linear regression - image26.png]]

*Figure : nuage des 4 observations (rendement croissant avec l'engrais), puis la droite ajustée $\hat{y} = 0{,}8 + 0{,}65x$.*

$$\hat{\beta}_1 = \frac{218 - \frac{(32)(24)}{4}}{296 - \frac{(32)^2}{4}} = 0{,}65 \qquad \hat{\beta}_0 = 6 - (0{,}65)(8) = 0{,}80$$

$$\hat{y} = 0{,}8 + 0{,}65x$$

Interprétation :

1. **Pente** : le rendement devrait augmenter de 0,65 kg pour chaque kg d'engrais supplémentaire.
2. **Ordonnée à l'origine** : le rendement moyen attendu est 0,8 kg sans engrais.

## Hypothèses sur l'erreur

I. La loi de probabilité de l'erreur $\varepsilon$ a une moyenne nulle.
II. Elle a une variance constante.
III. Elle est normale.
IV. Les erreurs sont indépendantes.

## Erreur standard de la régression

L'**erreur standard** de $y$ sachant $x$, notée $S_{y/x}$, est la **variabilité moyenne autour de la droite de régression** pour toute valeur de $x$.

![[Séance 10 - linear regression - image24.png]]

*Figure : à trois valeurs de $x$, les points se répartissent autour de la droite selon une courbe de distribution, de dispersion $S_{y/x}$.*

- Elle mesure la variation des $y$ réels autour des $\hat{y}$ prédits.
- Elle est mesurée par l'[[Erreur standard de la régression]] : l'[[Variance et écart-type d'échantillon|écart-type d'échantillon]] de $\hat{\varepsilon}$, noté $s$.
- Elle affecte la significativité des paramètres et la précision des prédictions.

### Décomposition de la variation

![[Séance 10 - linear regression - image10.png]]

*Figure : pour un point $x_i$, la SST va de $\bar{y}$ à $y_i$, la SSR de $\bar{y}$ à $\hat{y}_i$, la SSE de $\hat{y}_i$ à $y_i$.*

Voir [[Somme des carrés (SST, SSR, SSE)]].

- Somme totale des carrés (SST) : $\sum (y_i - \bar{y})^2$ ;
- Somme expliquée (SSR) : $\sum (\hat{y}_i - \bar{y})^2$ ;
- Somme non expliquée (SSE) : $\sum (y_i - \hat{y}_i)^2$.

$$s^2 = \frac{SSE}{n-2} \qquad s = \sqrt{s^2} = \sqrt{\frac{SSE}{n-2}}$$

## Résidus

$$e_i = Y_i - \hat{Y}_i$$

Le **[[Résidu (régression)|résidu]]** de l'observation $i$ est l'écart entre sa valeur observée et sa valeur prédite. On **vérifie les hypothèses de la régression en examinant les résidus** :

- **linéarité** ;
- **indépendance** ;
- **[[Loi normale|normalité]]** ;
- **variance constante** pour tous les niveaux de $X$ ([[Homoscédasticité|homoscédasticité]]).

### Linéarité

![[Séance 10 - linear regression - image13.png]]

*Figure : non linéaire (les résidus forment une arche) contre linéaire (résidus aléatoires dans une bande horizontale).*

### Indépendance

![[Séance 10 - linear regression - image9.png]]

*Figure : résidus non indépendants (bande montante, bande ondulante) contre indépendants (dispersion aléatoire autour de zéro).*

### Normalité

Sur un [[Diagramme de probabilité|diagramme de probabilité normale]], des erreurs normales s'alignent à peu près sur une droite.

![[Séance 10 - linear regression - image19.png]]

*Figure : diagramme de probabilité normale des résidus (pourcentage en fonction du résidu), points proches d'une droite.*

### Variance constante

![[Séance 10 - linear regression - image21.png]]

*Figure : variance non constante (dispersion en entonnoir) contre variance constante (bande de largeur fixe).*

## Test de significativité : test de la pente

Voir [[Test de la pente]] et [[Test d'hypothèse]].

- Montre s'il existe une relation linéaire entre $x$ et $y$.
- Porte sur la pente de la population $\beta_1$.
- Hypothèses :
  - $H_0 : \beta_1 = 0$ (pas de relation linéaire) ;
  - $H_a : \beta_1 \neq 0$ (relation linéaire).
- Base théorique : la distribution d'[[Échantillonnage|échantillonnage]] de la pente ([[Distribution d'échantillonnage]]).

Les **[[P-value|p-values]]** aident à savoir si les relations observées dans l'échantillon existent aussi dans la **population**. La p-value de chaque variable indépendante teste l'hypothèse nulle selon laquelle la variable n'a **aucune corrélation** avec la variable dépendante. Sans corrélation, les variations de la variable indépendante ne sont pas associées à celles de la variable dépendante : les preuves sont insuffisantes pour conclure à un effet au niveau de la population.

### Distribution d'échantillonnage des pentes

Chaque échantillon donne sa propre droite et sa propre pente (échantillon 1 : 2,5 ; 2 : 1,6 ; 3 : 1,8 ; 4 : 2,1 ; …). Un très grand nombre de pentes d'échantillons forme une distribution en cloche centrée sur $\beta_1$, d'écart-type $S_{\hat{\beta}_1}$.

![[Séance 10 - linear regression - image4.png]]

*Figure : droites d'échantillons autour de la droite de la population, et distribution d'échantillonnage des pentes $\hat{\beta}_1$.*

[[Statistique de test]] du coefficient de pente :

$$t = \frac{\hat{\beta}_1}{S_{\hat{\beta}_1}} = \frac{\hat{\beta}_1}{\dfrac{s}{\sqrt{SS_{xx}}}}, \qquad df = n - 2, \qquad SS_{xx} = \sum_{i=1}^{n} x_i^2 - \frac{\left(\sum_{i=1}^{n} x_i\right)^2}{n}$$

Elle suit une [[Loi de Student]] ([[Test t]]).

### Exemple : publicité et ventes de jouets

Analyste marketing d'une entreprise de jouets, on trouve $\hat{\beta}_0 = -0{,}1$, $\hat{\beta}_1 = 0{,}7$ et $s = 0{,}6055$ (écart-type d'échantillon de $\hat{\varepsilon}$). La relation est-elle **significative** au [[Seuil de signification|seuil]] 0,05 ?

| $x_i$ (pub, \$) | $y_i$ (ventes, unités) | $x_i^2$ | $y_i^2$ | $x_i y_i$ |
|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 4 | 1 | 2 |
| 3 | 2 | 9 | 4 | 6 |
| 4 | 2 | 16 | 4 | 8 |
| 5 | 4 | 25 | 16 | 20 |
| **15** | **10** | **55** | **26** | **37** |

$$S_{\hat{\beta}_1} = \frac{s}{\sqrt{SS_{xx}}} = \frac{0{,}6055}{\sqrt{55 - \frac{(15)^2}{5}}} = 0{,}1914 \qquad t = \frac{0{,}70}{0{,}1914} = 3{,}657$$

- $H_0 : \beta_1 = 0$ ; $H_a : \beta_1 \neq 0$ ;
- $\alpha = 0{,}05$, $df = 5 - 2 = 3$ ;
- [[Valeur critique|valeurs critiques]] : $-3{,}182$ et $3{,}182$ (0,025 dans chaque queue).

![[Séance 10 - linear regression - image23.png]]

*Figure : loi de Student à 3 degrés de liberté, zones de rejet au-delà de ±3,182.*

**Décision** : $3{,}657 > 3{,}182$, on rejette $H_0$ au seuil 0,05.
**Conclusion** : il y a une preuve de relation (linéaire) entre publicité et ventes.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Images non ouvertes ; calculs refaits à la main.

1. **Dérivée partielle $f_b$** : la transcription écrit « $-10 + 6b + 12 = 0$ ». Le terme $12m$ a perdu son $m$ : la forme correcte est $-10 + 6b + 12m = 0$ (complément).
2. **Somme de $y$ du jeu III d'Anscombe (82,50 contre 82,51)** : fausse alerte, la somme exacte des valeurs du tableau est 82,50, les autres sont arrondies.
3. **Points du graphique de l'exemple engrais** : la transcription note qu'ils semblent décalés par rapport au tableau. Le calcul, lui, est exact ; le graphique n'a pas été vérifié.
4. **« Dataset II is not distributed normally »** : le jeu II suit une courbe, c'est la relation qui n'est pas linéaire. La phrase du cours parle de distribution normale (complément).
5. **« Dataset IV : un point suffit à produire une forte corrélation »** : la corrélation de 0,816 est celle de tous les jeux. L'idée est correcte, la phrase la présente comme propre au jeu IV.
