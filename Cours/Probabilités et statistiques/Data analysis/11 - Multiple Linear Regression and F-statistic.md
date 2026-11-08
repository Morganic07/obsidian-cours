---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 11 : Multiple Linear Regression and F-statistic.docx|Cours 11 - Multiple Linear Regression and F-statistic]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Data analysis (Thanos)/Cours 11 : Multiple Linear Regression and F-statistic.docx|Cours 11 - Multiple Linear Regression and F-statistic]], dans [[Cours/Probabilités et statistiques/Data analysis/_index|Data analysis]].
## Idée générale

Deux suites à la régression simple : prédire (intervalle de confiance d'une moyenne et [[Intervalle de prédiction]] d'un individu), puis passer à plusieurs variables explicatives et tester le modèle entier avec la [[Statistique F]]. La note s'ouvre sur un titre de l'étudiant : « quelle est la formule de F ? plein de formules différentes ? », et rassemble les formes de F dans l'ordre ci-dessous.

## Les formes de F (en tête de note)

La note commence par la question de l'étudiant « Quelle est la formule de F ? Plein de formules différentes ? » et réunit les diapositives suivantes.

La [[Statistique F]] compare la variation expliquée par le modèle à la variation qui reste inexpliquée. C'est un rapport de [[Carré moyen|carrés moyens]] (*mean squares*), donc de variances. La diapositive écrit : [[Erreurs du cours#^e-11-multiple-linear-regression-and-f-statistic|✎]]

$$F = \frac{\text{variance explained by the model}}{\text{variance \textbf{not} explained by the model}}$$

$$F = \frac{MS_{model}}{MS_{error}}$$

- $MS_{model}$ : variance expliquée par les prédicteurs ;
- $MS_{error}$ : variance inexpliquée restante.

$$F = \frac{\text{between-groups variance}}{\text{within-group variance}}$$

(variance inter-groupes sur variance intra-groupe).

En régression :

$$F = \frac{\dfrac{TSS - RSS}{p-1}}{\dfrac{RSS}{n-p}}$$

avec TSS la somme totale des carrés ([[Somme des carrés (SST, SSR, SSE)]]), RSS la somme des carrés des [[Résidu (régression)|résidus]], $p$ le nombre de prédicteurs **constante comprise**, $n$ le nombre d'observations.

Attention aux sigles, qui changent d'un support à l'autre : ici **RSS** (*residual sum of squares*) est la somme des carrés des résidus, c'est-à-dire la **SSE** de la [[10 - linear regression|séance 10]], et $TSS - RSS$ est la somme expliquée, la **SSR** de la séance 10. Dans d'autres manuels, « SSR » désigne au contraire la somme résiduelle : il faut toujours vérifier la définition. [[Complément hors du cours|ⓘ]]

Avec $k$ variables explicatives, $p = k + 1$ : les degrés de liberté valent $p - 1 = k$ au numérateur et $n - p = n - (k+1)$ au dénominateur, ceux de la régression multiple plus bas. En régression simple ($k = 1$), on retrouve $1$ et $n - 2$. [[Complément hors du cours|ⓘ]]

### F en ANOVA à un facteur

En [[ANOVA]] à un facteur (*one way*), F aide à répondre à : « la variance entre les moyennes de deux populations ou plus est-elle significativement différente ? ». F détermine aussi la [[P-value|p-value]] : probabilité d'obtenir un résultat au moins aussi extrême que celui observé, si l'[[Test d'hypothèse|hypothèse nulle]] est vraie. La p-value est une probabilité, le rapport F une [[Statistique de test]] :

$$F = \frac{\text{variance des moyennes de groupes (Mean Square Between)}}{\text{moyenne des variances intra-groupe (Mean Squared Error)}}$$

**Quand rejeter $H_0$ ?** Quand la p-value est inférieure au seuil $\alpha$. De façon équivalente, on rejette $H_0$ quand la valeur de F dépasse la valeur critique de la loi F ; si F reste en dessous de la valeur critique, on ne rejette pas $H_0$. [[Erreurs du cours#^e-11-multiple-linear-regression-and-f-statistic|✎]]

| Source de variation | df | Somme des carrés | MS | F |
|---|---|---|---|---|
| Groupe | $k-1$ | $SST_G$ | $\dfrac{SST_G}{k-1}$ | $\dfrac{SST_G/(k-1)}{SST_E/(N-k)}$ |
| Erreur | $N-k$ | $SST_E$ | $\dfrac{SST_E}{N-k}$ | |
| Total | $N-1$ | $SST$ | | |

## Prédiction avec un modèle de régression

### Les deux types de prédiction

- **Réponse moyenne de la population** $E(y)$ pour un $x_p$ donné : un point de la droite de régression de la population. On cherche le résultat « en moyenne » de toutes les personnes qui ont la même valeur $x_p$. Exemple : « En moyenne, combien gagnent les gens qui ont 5 ans d'études ? »
- **Réponse individuelle** $y_i$ pour un $x_p$ donné : la valeur exacte d'un seul individu. Exemple : « Combien va gagner cet étudiant précis, qui a fait 5 ans d'études ? »

La prédiction ponctuelle est la même pour les deux, mais l'incertitude ([[Intervalle de confiance|intervalle]]) est bien plus grande pour l'individu.

Comme pour l'ordonnée à l'origine, une prédiction n'est fiable que pour un $x_p$ situé dans la plage des $x$ observés : au-delà (extrapolation), rien ne garantit que la relation reste linéaire, et les intervalles ci-dessous, déjà larges loin de $\bar{x}$, sous-estiment alors l'incertitude réelle. [[Complément hors du cours|ⓘ]]

![[Séance 11 - Multiple Linear Regression and F-statistic - image8.png]]

*Figure : à $x_P$, la prédiction $\hat{y}$ (droite estimée), la moyenne $E(y)$ (droite de population) et la valeur individuelle.*

Explications de la note :

- **A. La droite de prédiction** ($\hat{y}$, violette) : calculée avec les données de l'échantillon ; pour $x_p$ elle donne l'estimation $\hat{y}$, le « meilleur pari ».
- **B. La moyenne réelle** ($E(y) = \beta_0 + \beta_1 x$, orange) : la « vraie » droite théorique de la population, jamais connue parfaitement.
- **C. L'écart entre $\hat{y}$ et $E(y)$** : l'[[Erreur d'échantillonnage|erreur d'échantillonnage]].
- **D. L'individu** ($y_{\text{Individual}}$) : la valeur réelle d'un point précis. Même avec la moyenne parfaite, un individu ne tombe presque jamais dessus, à cause du bruit ou du hasard ($\varepsilon$). Prédire une seule personne est donc plus difficile et moins précis que prédire une moyenne.

### Plus on est près de la moyenne, moins il y a de variabilité

Les droites de deux échantillons se croisent en $(\bar{x}, \bar{y})$ ; leur écart est plus grand en $x_2$ (loin de $\bar{x}$) qu'en $x_1$ (près de $\bar{x}$). Cela vient de la variabilité des pentes estimées.

![[Séance 11 - Multiple Linear Regression and F-statistic - image4.png]]

*Figure : deux droites d'échantillon qui se croisent en $(\bar{x}, \bar{y})$ et s'écartent loin de la moyenne.*

### Intervalle de confiance de la valeur moyenne (*t-interval*)

Pour la valeur moyenne de $y$ en $x = x_p$ :

$$\hat{y} \pm t_{\alpha/2}\, s \sqrt{\frac{1}{n} + \frac{(x_p - \bar{x})^2}{SS_{xx}}}, \qquad df = n - 2$$

D'où vient la racine : la prédiction s'écrit $\hat{y} = \bar{y} + \hat{\beta}_1 (x_p - \bar{x})$, puisque la droite passe par $(\bar{x}, \bar{y})$. Les deux termes sont indépendants sous les hypothèses du modèle, avec $\mathrm{Var}(\bar{y}) = \sigma^2/n$ et $\mathrm{Var}(\hat{\beta}_1) = \sigma^2/SS_{xx}$, donc $\mathrm{Var}(\hat{y}) = \sigma^2 \left(\dfrac{1}{n} + \dfrac{(x_p - \bar{x})^2}{SS_{xx}}\right)$. On remplace $\sigma$ par son estimation $s$, d'où la loi de Student. Le terme en $(x_p - \bar{x})^2$ traduit l'incertitude sur la pente : c'est lui qui élargit l'intervalle loin de $\bar{x}$ et explique la figure précédente. [[Complément hors du cours|ⓘ]]

![[Séance 11 - Multiple Linear Regression and F-statistic - image25.png]]

*Figure : la valeur moyenne $E(y)$ en $x_p$, cible de l'intervalle de confiance.*

Facteurs qui jouent sur la largeur de l'intervalle :

1. Niveau de confiance $(1 - \alpha)$ : la largeur augmente avec la confiance.
2. Dispersion des données $(s)$ : la largeur augmente avec la variation.
3. Taille de l'échantillon : la largeur diminue quand $n$ augmente.
4. Distance de $x_p$ à $\bar{x}$ : la largeur augmente avec la distance.

**Exemple** (entreprise de jouets, mêmes données que la [[10 - linear regression|séance 10]]) : $\hat{\beta}_0 = -0{,}1$, $\hat{\beta}_1 = 0{,}7$, $s = 0{,}6055$ ; données (pub \$, ventes) : (1,1), (2,1), (3,2), (4,2), (5,4) ; sommes $\sum x = 15$, $\sum y = 10$, $\sum x^2 = 55$, $\sum y^2 = 26$, $\sum xy = 37$. Trouver un intervalle de confiance à 95 % des ventes **moyennes** pour une publicité de 4 \$.

$$\hat{y} = -0{,}1 + (0{,}7)(4) = 2{,}7$$

$$2{,}7 \pm (3{,}182)(0{,}6055)\sqrt{\frac{1}{5} + \frac{(4-3)^2}{10}} \quad\Rightarrow\quad 1{,}645 \leq E(Y) \leq 3{,}755$$

Détail : $\bar{x} = 15/5 = 3$, $SS_{xx} = 55 - 15^2/5 = 10$, $t_{0{,}025}$ à $5 - 2 = 3$ degrés de liberté vaut 3,182, et la demi-largeur vaut $3{,}182 \times 0{,}6055 \times \sqrt{0{,}3} \approx 1{,}055$. [[Complément hors du cours|ⓘ]]

### Intervalle de prédiction d'une valeur individuelle (*t-interval*)

Voir [[Intervalle de prédiction]].

$$\hat{y} \pm t_{\alpha/2}\, s \sqrt{\mathbf{1} + \frac{1}{n} + \frac{(x_p - \bar{x})^2}{SS_{xx}}}, \qquad df = n - 2$$

Le **1** (mis en évidence sur la diapositive) ajoute l'erreur aléatoire $\varepsilon$ entre la moyenne attendue et la valeur qu'on cherche à prédire.

En variances : l'écart à prévoir est $y - \hat{y} = (y - E(y)) + (E(y) - \hat{y})$, somme de l'erreur propre à l'individu, de variance $\sigma^2$, et de l'erreur d'estimation de la droite, indépendante de la première. Les variances s'additionnent : $\sigma^2 + \sigma^2\left(\dfrac{1}{n} + \dfrac{(x_p - \bar{x})^2}{SS_{xx}}\right)$, d'où le $1$ sous la racine. Quand $n$ grandit, les deux derniers termes tendent vers 0 mais le $1$ reste : c'est la « variabilité naturelle $\sigma$ » du tableau plus bas. [[Complément hors du cours|ⓘ]]

![[Séance 11 - Multiple Linear Regression and F-statistic - image24.png]]

*Figure : la valeur à prédire (cible) s'écarte de la moyenne attendue de $\varepsilon$.*

**Exemple** : mêmes données, prédire les ventes pour une publicité de 4 \$ avec un intervalle de prédiction à 95 %.

$$2{,}7 \pm (3{,}182)(0{,}6055)\sqrt{1 + \frac{1}{5} + \frac{(4-3)^2}{10}}$$

Soit $0{,}503 \leq y_4 \leq 4{,}897$. [[Erreurs du cours#^e-11-multiple-linear-regression-and-f-statistic|✎]]

### Intervalle de confiance contre intervalle de prédiction

![[Séance 11 - Multiple Linear Regression and F-statistic - image3.png]]

*Figure : la droite de régression encadrée par les limites de confiance (proches) et les limites de prédiction (plus éloignées) ; le dessin est schématique : les vraies limites sont symétriques autour de la droite et le plus resserrées en $\bar{x}$.* [[Erreurs du cours#^e-11-multiple-linear-regression-and-f-statistic|✎]]

- Intervalle de confiance : emplacement probable du vrai [[Paramètre et statistique|paramètre de la population]].
- Intervalle de prédiction : distribution des valeurs, et non incertitude sur la moyenne de la population.

| Caractéristique | Intervalle de confiance | Intervalle de prédiction |
|---|---|---|
| Cible | la moyenne ($\mu$ / $E(y)$) | un individu ($y_i$) |
| Incertitude | erreur d'échantillonnage seulement | erreur d'échantillonnage + variance résiduelle |
| Taille | plus étroit | plus large |
| Effet de $n$ | peut devenir très petit si $n$ est grand | ne descend jamais sous la variabilité naturelle $\sigma$ |

## Régression linéaire multiple

$$y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_k X_k + \varepsilon$$

où $k$ est le nombre de variables (ou paramètres). Les paramètres s'interprètent facilement :

- $\beta_0$ : ordonnée à l'origine, valeur moyenne de $y$ quand tous les $X$ valent zéro ;
- $\beta_j$ : pente de la $j$-ième variable $X_j$, c'est-à-dire l'augmentation moyenne de $y$ quand $X_j$ augmente de 1 **et que tous les autres $X$ restent constants**.

Avec $k$ variables explicatives, le nombre de [[Variance et écart-type d'échantillon|degrés de liberté]] est $n-(k+1)$.

Le « toutes choses égales par ailleurs » distingue la régression multiple d'une suite de régressions simples : le coefficient de $X_1$ dans le modèle multiple mesure l'effet de $X_1$ une fois tenu compte des autres variables, et peut différer beaucoup, voire changer de signe, par rapport à la pente d'une régression de $y$ sur $X_1$ seule (voir [[Paradoxe de Simpson]]). [[Complément hors du cours|ⓘ]]

Les variables explicatives peuvent être catégorielles, codées par des [[Variable indicatrice|variables indicatrices]], ou des transformations d'une même variable ($X$ et $X^2$) : le modèle reste « linéaire » car il est linéaire **en les paramètres** $\beta_j$, pas forcément en $x$. [[Complément hors du cours|ⓘ]]

Quand des variables explicatives sont fortement corrélées entre elles, on parle de [[Multicolinéarité|multicolinéarité]] : le modèle a du mal à séparer leurs effets, les erreurs standard des $\hat{\beta}_j$ gonflent et les coefficients deviennent instables (signe inattendu, aucun test $t$ significatif alors que le test F global l'est). On la mesure par le facteur d'inflation de la variance $VIF_j = \dfrac{1}{1 - R_j^2}$, où $R_j^2$ est le $R^2$ de la régression de $X_j$ sur les autres variables explicatives ; un VIF au-delà de 5 à 10 est l'alerte habituelle. [[Complément hors du cours|ⓘ]]

On estime les paramètres par les [[Moindres carrés|moindres carrés]], c'est-à-dire en minimisant l'erreur quadratique moyenne ([[Estimateur|MSE]], *Mean Square Error*) :

$$MSE = \frac{1}{n}\sum_{i=1}^{n}\left(Y_i - \hat{Y}_i\right)^2 = \frac{1}{n}\sum_{i=1}^{n}\left(Y_i - \hat{\beta}_0 - \hat{\beta}_1 X_1 - \cdots - \hat{\beta}_p X_p\right)^2$$

![[Séance 11 - Multiple Linear Regression and F-statistic - image2.png]]

*Figure : nuage de points en 3D ($Y$, $X_1$, $X_2$) et plan de régression ; les segments verticaux sont les résidus.*

Minimiser la MSE ou la somme $RSS = \sum (Y_i - \hat{Y}_i)^2$ revient au même (elles ne diffèrent que du facteur $1/n$). En revanche, pour **estimer** la variance des erreurs, on divise $RSS$ par $n - p$ et non par $n$ : $s^2 = RSS/(n-p)$, généralisation du $SSE/(n-2)$ de la [[10 - linear regression|séance 10]]. [[Complément hors du cours|ⓘ]]

En écriture matricielle, avec $X$ la matrice de plan (une colonne de 1 pour la constante, puis une colonne par variable) et $\mathbf{y}$ le vecteur des réponses, le modèle s'écrit $\mathbf{y} = X\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ et les estimations des moindres carrés sont la solution des équations normales $X^TX\hat{\boldsymbol{\beta}} = X^T\mathbf{y}$, soit $\hat{\boldsymbol{\beta}} = (X^TX)^{-1}X^T\mathbf{y}$ quand $X^TX$ est inversible ([[Moindres carrés]], [[Régression linéaire]]). C'est ce que calcule `lm(y ~ x1 + x2)` en R. [[Complément hors du cours|ⓘ]]

Relation entre la droite de la population et celle des moindres carrés :

$$\text{Population : } Y_i = \beta_0 + \beta_1 X_1 + \cdots + \beta_p X_p + \varepsilon \qquad \text{Moindres carrés : } \hat{Y}_i = \hat{\beta}_0 + \hat{\beta}_1 X_1 + \cdots + \hat{\beta}_p X_p$$

On voudrait connaître $\beta_0, \dots, \beta_p$ (la droite de la population) ; on ne connaît que $\hat{\beta}_0, \dots, \hat{\beta}_p$. On les utilise comme estimations, et $\hat{Y}_i$ comme estimation de $Y_i$. Elles ne sont pas parfaites, de même que $\bar{X}$ n'est pas une estimation parfaite de $\mu$. [[Erreurs du cours#^e-11-multiple-linear-regression-and-f-statistic|✎]]

## La statistique F en régression

F teste si **le modèle explique mieux les données qu'un modèle sans prédicteur**. Le modèle de comparaison ne contient que l'ordonnée à l'origine et prédit la moyenne de la variable réponse : c'est le **test F de significativité globale** (*F-test of overall significance*).

- $H_0$ : le modèle sans prédicteur ajuste les données aussi bien que le modèle de régression ;
- $H_1$ : le modèle de régression ajuste mieux que le modèle réduit à l'ordonnée à l'origine.

Interprétation en régression multiple :

- le test F évalue la **significativité globale du modèle** ; l'hypothèse nulle dit que tous les coefficients sont nuls : $\beta_1 = \beta_2 = \cdots = \beta_k = 0$ ;
- **si F est assez grand, on rejette $H_0$** : au moins un prédicteur a un effet non nul sur la variable réponse ;
- **le test F juge le modèle dans son ensemble** ; ensuite, chaque prédicteur s'examine par un [[Test t|test t]].

Pourquoi un test global plutôt que $k$ tests $t$ : en faisant $k$ tests au seuil 5 %, la probabilité qu'au moins l'un soit significatif par hasard dépasse nettement 5 % (environ 40 % pour 10 tests indépendants, $1 - 0{,}95^{10}$). Le test F contrôle ce risque pour l'ensemble des coefficients ([[Erreur de type I et de type II]]). [[Complément hors du cours|ⓘ]]

Les calculs se présentent dans un tableau d'ANOVA de la régression, construit comme celui de l'ANOVA à un facteur plus haut : [[Complément hors du cours|ⓘ]]

| Source | df | Somme des carrés | Carré moyen | F |
|---|---|---|---|---|
| Régression | $p - 1$ | $TSS - RSS$ | $\dfrac{TSS - RSS}{p-1}$ | $\dfrac{(TSS - RSS)/(p-1)}{RSS/(n-p)}$ |
| Résidus | $n - p$ | $RSS$ | $\dfrac{RSS}{n-p}$ | |
| Total | $n - 1$ | $TSS$ | | |

Exemple sur les données des jouets ($n = 5$, $p = 2$) : $TSS = 26 - 10^2/5 = 6$ et $RSS = 1{,}1$, donc $F = \dfrac{4{,}9/1}{1{,}1/3} \approx 13{,}36$, à comparer à la loi $F_{1,3}$. On trouve $F = t^2 = 3{,}657^2$, avec la même p-value (environ 0,035) que le test de la pente : en régression simple, test F global et test $t$ de la pente sont un seul et même test. [[Complément hors du cours|ⓘ]]

Le même principe compare deux **modèles emboîtés** (le petit est le grand privé de $q$ variables) : $F = \dfrac{(RSS_{\text{réduit}} - RSS_{\text{complet}})/q}{RSS_{\text{complet}}/(n-p)}$, à $q$ et $n - p$ degrés de liberté, où $p$ compte les paramètres du modèle complet. Le test global en est le cas où le modèle réduit ne garde que la constante ($RSS_{\text{réduit}} = TSS$). En R : `anova(modele_reduit, modele_complet)` ; la dernière ligne de `summary(lm(...))` donne le F global, ses degrés de liberté et sa p-value. [[Complément hors du cours|ⓘ]]

## Relation entre le test F et $R^2$

- F est étroitement lié au [[Coefficient de détermination|$R^2$]], qui mesure la part de variation de la variable réponse expliquée par le modèle.
- Quand le modèle explique plus de variation, $R^2$ augmente, et F tend à augmenter aussi, car la variation expliquée grandit par rapport à la variation inexpliquée.
- Les deux mesures ont des rôles différents :
  - $R^2$ indique **combien** de variation le modèle explique ;
  - le test F évalue si cette variation expliquée est **statistiquement significative**.

À partir de $F = \dfrac{(TSS - RSS)/(p-1)}{RSS/(n-p)}$, un peu d'algèbre donne :

$$R^2 = 1 - \left(1 + F \cdot \frac{p-1}{n-p}\right)^{-1}$$

L'algèbre en question : $F \cdot \dfrac{p-1}{n-p} = \dfrac{TSS - RSS}{RSS} = \dfrac{TSS}{RSS} - 1$, donc $1 + F\dfrac{p-1}{n-p} = \dfrac{TSS}{RSS}$, dont l'inverse est $\dfrac{RSS}{TSS}$. Comme $R^2 = 1 - \dfrac{RSS}{TSS}$, la formule suit. Sur l'exemple des jouets : $1 - (1 + 13{,}36/3)^{-1} \approx 0{,}82 = 4{,}9/6$. [[Complément hors du cours|ⓘ]]

Inversement, $F = \dfrac{R^2/(p-1)}{(1-R^2)/(n-p)}$ : à $R^2$ égal, F grandit avec $n$. Avec beaucoup d'observations, un $R^2$ modeste peut être très significatif ; avec peu d'observations, un $R^2$ élevé peut ne pas l'être. [[Complément hors du cours|ⓘ]]

Le $R^2$ a un défaut en régression multiple : il **augmente toujours** (ou reste égal) quand on ajoute une variable, même sans rapport avec $y$. Pour comparer des modèles de tailles différentes, on utilise le **$R^2$ ajusté**, $\bar{R}^2 = 1 - (1 - R^2)\dfrac{n-1}{n-p}$, qui pénalise le nombre de paramètres et peut baisser quand une variable inutile est ajoutée ([[Coefficient de détermination]]). Sur l'exemple des jouets : $1 - 0{,}183 \times 4/3 \approx 0{,}76$. [[Complément hors du cours|ⓘ]]

En pratique, un grand $R^2$ (modèle linéaire bien ajusté) va avec un grand F, donc une forte preuve qu'au moins certains coefficients sont non nuls.

## La loi F

**Loi F de Snedecor-Fisher** : elle sert à estimer le **rapport des variances de deux lois normales**. Soit un échantillon $X_1, \dots, X_{n_1}$ de loi $N(\mu_1, \sigma_1)$ et un échantillon $Y_1, \dots, Y_{n_2}$ de loi $N(\mu_2, \sigma_2)$. Leurs **variances d'échantillon** suivent des lois du $\chi^2$ mises à l'échelle ([[Loi du khi-deux]]) : [[Erreurs du cours#^e-11-multiple-linear-regression-and-f-statistic|✎]]

$$S_1^2 = \frac{\sum_{i=1}^{n_1}(X_i - \bar{X})^2}{n_1 - 1} \sim \frac{\sigma_1^2 \chi^2_{n_1-1}}{n_1 - 1} \qquad S_2^2 = \frac{\sum_{i=1}^{n_2}(Y_i - \bar{Y})^2}{n_2 - 1} \sim \frac{\sigma_2^2 \chi^2_{n_2-1}}{n_2 - 1}$$

Donc :

$$\frac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2} \sim \frac{\chi^2_{n_1-1}/(n_1 - 1)}{\chi^2_{n_2-1}/(n_2 - 1)} = F_{v_1, v_2}$$

La loi F décrit une variable aléatoire qui est un **rapport mis à l'échelle de deux $\chi^2$**, avec $v_1 = n_1 - 1$ degrés de liberté au numérateur et $v_2 = n_2 - 1$ au dénominateur.

Sous l'hypothèse $\sigma_1 = \sigma_2$, les $\sigma^2$ se simplifient et $S_1^2/S_2^2$ suit directement $F_{n_1-1,\, n_2-1}$ : c'est le **test F d'égalité de deux variances** (test de Fisher), qu'on fait par exemple avant un test $t$ à variances égales. En R : `var.test(x, y)`. [[Complément hors du cours|ⓘ]]

Propriétés utiles : une variable F ne prend que des valeurs positives et sa loi est asymétrique, étalée à droite ; le test F de la régression et de l'ANOVA est donc **unilatéral à droite** (seules les grandes valeurs de F mènent au rejet). Si $T$ suit une loi de Student à $v$ degrés de liberté, $T^2$ suit $F_{1, v}$, ce qui explique l'égalité $F = t^2$ en régression simple. Enfin, si $X \sim F_{v_1, v_2}$, alors $1/X \sim F_{v_2, v_1}$, d'où l'importance de l'ordre des degrés de liberté. [[Complément hors du cours|ⓘ]]

## Méthode

1. **Calculer F** : rapport de deux carrés moyens ; la formule exacte dépend de la méthode (ANOVA ou régression).
2. **Se référer à la loi F**, définie par deux degrés de liberté : $df_1$ au numérateur, $df_2$ au dénominateur.
3. **Calculer la p-value** : probabilité d'observer une valeur de F au moins aussi grande que celle obtenue, **si l'hypothèse nulle est vraie**. Si elle est inférieure au [[Seuil de signification|seuil de signification]] choisi, le résultat est statistiquement significatif.
