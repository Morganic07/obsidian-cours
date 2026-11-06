---
type: source
tags: [year3]
sources: ["[[Cours 11 - Multiple Linear Regression and F-statistic]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Cours 11 - Multiple Linear Regression and F-statistic]], dans [[Data analysis (Thanos) (matière)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Deux suites à la régression simple : prédire (intervalle de confiance d'une moyenne et [[Intervalle de prédiction]] d'un individu), puis passer à plusieurs variables explicatives et tester le modèle entier avec la [[Statistique F]]. La note s'ouvre sur un titre de l'étudiant : « quelle est la formule de F ? plein de formules différentes ? », et rassemble les formes de F dans l'ordre ci-dessous.

## Les formes de F (en tête de note)

La note commence par la question de l'étudiant « Quelle est la formule de F ? Plein de formules différentes ? » et réunit les diapositives suivantes.

La [[Statistique F]] compare la variation expliquée par le modèle à la variation qui reste inexpliquée. C'est un rapport de [[Carré moyen|carrés moyens]] (*mean squares*), donc de variances. La diapositive écrit :

$$F = \frac{\text{variance \textbf{not} explained by the model}}{\text{variance explained by the model}}$$

(formule inversée par rapport à l'usage et aux suivantes, voir Points à vérifier).

$$F = \frac{MS_{model}}{MS_{error}}$$

- $MS_{model}$ : variance expliquée par les prédicteurs ;
- $MS_{error}$ : variance inexpliquée restante.

$$F = \frac{\text{between-groups variance}}{\text{within-group variance}}$$

(variance inter-groupes sur variance intra-groupe).

En régression :

$$F = \frac{\dfrac{TSS - RSS}{p-1}}{\dfrac{RSS}{n-p}}$$

avec TSS la somme totale des carrés ([[Somme des carrés (SST, SSR, SSE)]]), RSS la somme des carrés des [[Résidu (régression)|résidus]], $p$ le nombre de prédicteurs **constante comprise**, $n$ le nombre d'observations.

### F en ANOVA à un facteur

En [[ANOVA]] à un facteur (*one way*), F aide à répondre à : « la variance entre les moyennes de deux populations ou plus est-elle significativement différente ? ». F détermine aussi la [[P-value|p-value]] : probabilité d'obtenir un résultat au moins aussi extrême que celui observé, si l'[[Test d'hypothèse|hypothèse nulle]] est vraie. La p-value est une probabilité, le rapport F une [[Statistique de test]] :

$$F = \frac{\text{variance des moyennes de groupes (Mean Square Between)}}{\text{moyenne des variances intra-groupe (Mean Squared Error)}}$$

**Quand rejeter $H_0$ ?** Quand la p-value est inférieure au seuil $\alpha$. La diapositive ajoute : « You should not reject the null if your critical f value is smaller than your F-value, unless you also have a small p-value » (voir Points à vérifier).

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

![[Séance 11 - Multiple Linear Regression and F-statistic - image25.png]]

*Figure : la valeur moyenne $E(y)$ en $x_p$, cible de l'intervalle de confiance.*

Facteurs qui jouent sur la largeur de l'intervalle :

1. Niveau de confiance $(1 - \alpha)$ : la largeur augmente avec la confiance.
2. Dispersion des données $(s)$ : la largeur augmente avec la variation.
3. Taille de l'échantillon : la largeur diminue quand $n$ augmente.
4. Distance de $x_p$ à $\bar{x}$ : la largeur augmente avec la distance.

**Exemple** (entreprise de jouets, mêmes données que la [[Séance 10 - linear regression (résumé)|séance 10]]) : $\hat{\beta}_0 = -0{,}1$, $\hat{\beta}_1 = 0{,}7$, $s = 0{,}6055$ ; données (pub \$, ventes) : (1,1), (2,1), (3,2), (4,2), (5,4) ; sommes $\sum x = 15$, $\sum y = 10$, $\sum x^2 = 55$, $\sum y^2 = 26$, $\sum xy = 37$. Trouver un intervalle de confiance à 95 % des ventes **moyennes** pour une publicité de 4 \$.

$$\hat{y} = -0{,}1 + (0{,}7)(4) = 2{,}7$$

$$2{,}7 \pm (3{,}182)(0{,}6055)\sqrt{\frac{1}{5} + \frac{(4-3)^2}{10}} \quad\Rightarrow\quad 1{,}645 \leq E(Y) \leq 3{,}755$$

### Intervalle de prédiction d'une valeur individuelle (*t-interval*)

Voir [[Intervalle de prédiction]].

$$\hat{y} \pm t_{\alpha/2}\, s \sqrt{\mathbf{1} + \frac{1}{n} + \frac{(x_p - \bar{x})^2}{SS_{xx}}}, \qquad df = n - 2$$

Le **1** (mis en évidence sur la diapositive) ajoute l'erreur aléatoire $\varepsilon$ entre la moyenne attendue et la valeur qu'on cherche à prédire.

![[Séance 11 - Multiple Linear Regression and F-statistic - image24.png]]

*Figure : la valeur à prédire (cible) s'écarte de la moyenne attendue de $\varepsilon$.*

**Exemple** : mêmes données, prédire les ventes pour une publicité de 4 \$ avec un intervalle de prédiction à 95 %.

$$2{,}7 \pm (3{,}182)(0{,}6055)\sqrt{1 + \frac{1}{5} + \frac{(4-3)^2}{10}}$$

La diapositive écrit « $4{,}897 \leq y_4 \leq 0{,}503$ » ; les bornes sont inversées : $0{,}503 \leq y_4 \leq 4{,}897$ (voir Points à vérifier).

### Intervalle de confiance contre intervalle de prédiction

![[Séance 11 - Multiple Linear Regression and F-statistic - image3.png]]

*Figure : la droite de régression encadrée par les limites de confiance (proches) et les limites de prédiction (plus éloignées).*

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

On estime les paramètres par les [[Moindres carrés|moindres carrés]], c'est-à-dire en minimisant l'erreur quadratique moyenne ([[Estimateur|MSE]], *Mean Square Error*) :

$$MSE = \frac{1}{n}\sum_{i=1}^{n}\left(Y_i - \hat{Y}_i\right)^2 = \frac{1}{n}\sum_{i=1}^{n}\left(Y_i - \hat{\beta}_0 - \hat{\beta}_1 X_1 - \cdots - \hat{\beta}_p X_p\right)^2$$

![[Séance 11 - Multiple Linear Regression and F-statistic - image2.png]]

*Figure : nuage de points en 3D ($Y$, $X_1$, $X_2$) et plan de régression ; les segments verticaux sont les résidus.*

Relation entre la droite de la population et celle des moindres carrés :

$$\text{Population : } Y_i = \beta_0 + \beta_1 X_1 + \cdots + \beta_p X_p + \varepsilon \qquad \text{Moindres carrés : } \hat{Y}_i = \hat{\beta}_0 + \hat{\beta}_1 X_1 + \cdots + \hat{\beta}_p X_p$$

On voudrait connaître $\beta_0, \dots, \beta_p$ (la droite de la population) ; on ne connaît que $\hat{\beta}_0, \dots, \hat{\beta}_p$. On les utilise comme estimations, et $\hat{Y}_i$ comme estimation de $Y_i$. Elles ne sont pas parfaites, de même que « $\hat{X}$ » (sans doute $\bar{X}$) n'est pas une estimation parfaite de $\mu$.

## La statistique F en régression

F teste si **le modèle explique mieux les données qu'un modèle sans prédicteur**. Le modèle de comparaison ne contient que l'ordonnée à l'origine et prédit la moyenne de la variable réponse : c'est le **test F de significativité globale** (*F-test of overall significance*).

- $H_0$ : le modèle sans prédicteur ajuste les données aussi bien que le modèle de régression ;
- $H_1$ : le modèle de régression ajuste mieux que le modèle réduit à l'ordonnée à l'origine.

Interprétation en régression multiple :

- le test F évalue la **significativité globale du modèle** ; l'hypothèse nulle dit que tous les coefficients sont nuls : $\beta_1 = \beta_2 = \cdots = \beta_k = 0$ ;
- **si F est assez grand, on rejette $H_0$** : au moins un prédicteur a un effet non nul sur la variable réponse ;
- **le test F juge le modèle dans son ensemble** ; ensuite, chaque prédicteur s'examine par un [[Test t|test t]].

## Relation entre le test F et $R^2$

- F est étroitement lié au [[Coefficient de détermination|$R^2$]], qui mesure la part de variation de la variable réponse expliquée par le modèle.
- Quand le modèle explique plus de variation, $R^2$ augmente, et F tend à augmenter aussi, car la variation expliquée grandit par rapport à la variation inexpliquée.
- Les deux mesures ont des rôles différents :
  - $R^2$ indique **combien** de variation le modèle explique ;
  - le test F évalue si cette variation expliquée est **statistiquement significative**.

À partir de $F = \dfrac{(TSS - RSS)/(p-1)}{RSS/(n-p)}$, un peu d'algèbre donne :

$$R^2 = 1 - \left(1 + F \cdot \frac{p-1}{n-p}\right)^{-1}$$

En pratique, un grand $R^2$ (modèle linéaire bien ajusté) va avec un grand F, donc une forte preuve qu'au moins certains coefficients sont non nuls.

## La loi F

**Loi F de Snedecor-Fisher** : elle sert à estimer le **rapport des variances de deux lois normales**. Soit un échantillon $X_1, \dots, X_{n_1}$ de loi $N(\mu_1, \sigma_1)$ et un échantillon $Y_1, \dots, Y_{n_2}$ de loi $N(\mu_2, \sigma_2)$. Leurs **variances d'échantillon** suivent des lois du $\chi^2$ mises à l'échelle ([[Loi du khi-deux]]) :

$$S_1^2 = \frac{\sum_{i=1}^{n_1}(X_i - \bar{X})^2}{n_1 - 1} \sim \frac{\sigma_1^2 \chi^2_{n_1-1}}{n_1 - 1} \qquad S_2^2 = \frac{\sum_{i=1}^{n_2}(Y_i - \bar{Y})^2}{n_2 - 1} \sim \frac{\sigma_2^2 \chi^2_{n_2-1}}{n_2 - 1}$$

Donc :

$$\frac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2} \sim \frac{\chi^2_{n_1-1}/(n_1 - 1)}{\chi^2_{n_2-1}/(n_2 - 1)} = F_{v_1, v_2}$$

La loi F décrit une variable aléatoire qui est un **rapport mis à l'échelle de deux $\chi^2$**, avec $v_1 = n_1 - 1$ degrés de liberté au numérateur et $v_2 = n_2 - 1$ au dénominateur.

## Méthode

1. **Calculer F** : rapport de deux carrés moyens ; la formule exacte dépend de la méthode (ANOVA ou régression).
2. **Se référer à la loi F**, définie par deux degrés de liberté : $df_1$ au numérateur, $df_2$ au dénominateur.
3. **Calculer la p-value** : probabilité d'observer une valeur de F au moins aussi grande que celle obtenue, **si l'hypothèse nulle est vraie**. Si elle est inférieure au [[Seuil de signification|seuil de signification]] choisi, le résultat est statistiquement significatif.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Formule de F, première diapositive** : image lue directement, elle écrit $F = \dfrac{\text{variance not explained}}{\text{variance explained}}$. C'est l'inverse de la définition usuelle, et de la formule $MS_{model}/MS_{error}$ donnée juste après, comme de la formule en $TSS$ et $RSS$. Il faut lire variance expliquée sur variance non expliquée (complément). **À corriger avant un examen.**
2. **Intervalle de prédiction de l'exemple** : image lue directement, la diapositive écrit « $4{,}897 \le y_4 \le 0{,}503$ ». Calcul refait : $3{,}182 \times 0{,}6055 \times \sqrt{1{,}3} \approx 2{,}20$, donc $0{,}503 \le y_4 \le 4{,}897$ (complément). **À corriger avant un examen.** L'intervalle de confiance voisin, $[1{,}645 ; 3{,}755]$, est exact.
3. **Règle de rejet** : « on ne rejette pas $H_0$ si la valeur critique est plus petite que la valeur $F$, sauf si la p-value est petite » (diapositive reprise dans le [[Séance 12 - ANOVA and F-statistic (résumé)|Cours 12]]). On rejette quand $F$ dépasse la valeur critique (complément). Image non ouverte, mais le texte de la note porte la même phrase.
4. **Notations de $p$ et $k$** : $p$ désigne les paramètres, constante comprise, dans la formule de F ($p-1$ et $n-p$), alors que la régression multiple parle de $k$ variables et de $n-(k+1)$ degrés de liberté. Avec $p = k+1$ les deux sont cohérents.
5. **$\hat{X}$ pour $\bar{X}$** : la transcription lit un chapeau, c'est vraisemblablement une barre. Image non ouverte.
6. **Couleurs de la figure de prédiction** : le texte de l'étudiant parle de droite violette pour $\hat{y}$ et orange pour $E(y)$ ; la transcription décrit $E(y)$ en rouge. Sans conséquence.
7. **Borne $n_{12}$** dans la somme de $S_2^2$ (diapositive de la loi F) : sans doute $n_2$. Les dénominateurs « $\chi^2_{n_1-1}/n_1 - 1$ » sont écrits sans parenthèses ; il faut lire $/(n_1-1)$ (complément).
8. **Figure confiance contre prédiction** : selon la transcription, les courbes ne sont ni symétriques ni resserrées autour de $\bar{x}$, contrairement à ce qu'on attendrait. Image non vérifiée en détail.
