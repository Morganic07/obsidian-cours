---
type: source
tags: [year3]
sources: ["[[Cours 11 - Multiple Linear Regression and F-statistic]]"]
maj: 2026-11-05
---

Résumé de [[Cours 11 - Multiple Linear Regression and F-statistic]], dans [[Data analysis (Thanos) (matière)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Deux suites à la régression simple : prédire (intervalle de confiance d'une moyenne et [[Intervalle de prédiction]] d'un individu), puis passer à plusieurs variables explicatives et tester le modèle entier avec la [[Statistique F]]. La note s'ouvre sur un titre de l'étudiant : « quelle est la formule de F ? plein de formules différentes ? », et rassemble les formes de F dans l'ordre ci-dessous.

## Contenu, dans l'ordre du cours

- **Formes de F** (en tête de note) : variance non expliquée sur variance expliquée (voir points à vérifier), $MS_{model}/MS_{error}$, variance inter-groupes sur variance intra-groupe, et en régression $F = \dfrac{(TSS - RSS)/(p-1)}{RSS/(n-p)}$ avec $p$ nombre de paramètres constante comprise. En ANOVA à un facteur : $F = \dfrac{\text{variance des moyennes de groupes (MS between)}}{\text{moyenne des variances intra-groupe (MSE)}}$, et tableau $df$ : groupes $k-1$, erreur $N-k$, total $N-1$. Voir [[ANOVA]].
- **Deux types de prédiction** : la réponse moyenne $E(y)$ pour un $x_p$ donné (point de la droite de population), et la réponse individuelle $y_i$. La prédiction ponctuelle est la même, mais l'incertitude est bien plus grande pour l'individu : même avec la droite parfaite, un individu s'écarte à cause de l'erreur $\varepsilon$.
- **Plus on est près de la moyenne, moins il y a de variabilité** : les droites de deux échantillons se croisent en $(\bar{x}, \bar{y})$ et s'écartent loin de $\bar{x}$, à cause de la variabilité de la pente estimée.
- **Intervalle de confiance de la moyenne** : $\hat{y} \pm t_{\alpha/2}\,s\sqrt{\dfrac{1}{n} + \dfrac{(x_p - \bar{x})^2}{SS_{xx}}}$, $df = n-2$. La largeur augmente avec le niveau de confiance, la dispersion $s$ et la distance de $x_p$ à $\bar{x}$, et diminue avec la taille de l'échantillon.
- **Exemple (publicité 4 \$)** : $\hat{y} = -0{,}1 + 0{,}7 \times 4 = 2{,}7$, $2{,}7 \pm 3{,}182 \times 0{,}6055\sqrt{1/5 + 1/10}$, soit $1{,}645 \le E(Y) \le 3{,}755$.
- **Intervalle de prédiction d'un individu** : $\hat{y} \pm t_{\alpha/2}\,s\sqrt{\mathbf{1} + \dfrac{1}{n} + \dfrac{(x_p - \bar{x})^2}{SS_{xx}}}$, $df = n-2$. Le « 1 » ajoute l'erreur aléatoire. Même exemple : $2{,}7 \pm 3{,}182 \times 0{,}6055\sqrt{1 + 1/5 + 1/10}$.
- **Confiance contre prédiction** :

| | Intervalle de confiance | Intervalle de prédiction |
|---|---|---|
| Cible | la moyenne $E(y)$ | un individu $y_i$ |
| Incertitude | erreur d'échantillonnage seule | erreur d'échantillonnage et variance résiduelle |
| Taille | plus étroit | plus large |
| Effet de $n$ | peut devenir très petit | ne descend jamais sous la variabilité naturelle $\sigma$ |

- **Régression linéaire multiple** : $y = \beta_0 + \beta_1X_1 + \dots + \beta_kX_k + \varepsilon$. $\beta_0$ est la valeur moyenne de $y$ quand tous les $X$ valent zéro, $\beta_j$ l'augmentation moyenne de $y$ quand $X_j$ augmente de 1 **toutes les autres variables restant fixes**. Degrés de liberté : $n-(k+1)$. Estimation par les [[Moindres carrés|moindres carrés]] : on minimise $MSE = \frac{1}{n}\sum(Y_i - \hat{Y}_i)^2$. On voudrait connaître les $\beta$ de la population, on n'a que les $\hat{\beta}$ de l'échantillon.
- **F en régression** : il teste si le modèle explique mieux les données qu'un modèle sans variable explicative (seulement l'ordonnée à l'origine). $H_0 : \beta_1 = \dots = \beta_k = 0$. Si $F$ est assez grand, au moins un prédicteur a un effet non nul. Le F juge le modèle entier, puis les prédicteurs se jugent un à un par des tests $t$.
- **F et $R^2$** : plus le modèle explique, plus $R^2$ et $F$ augmentent. $R^2$ dit combien de variation est expliquée, F dit si c'est statistiquement significatif. Relation du cours : $R^2 = 1 - \left(1 + F\dfrac{p-1}{n-p}\right)^{-1}$.
- **Loi F (Snedecor-Fisher)** : rapport des variances de deux échantillons normaux. Avec $S_i^2 \sim \sigma_i^2\chi^2_{n_i-1}/(n_i-1)$, le rapport $\dfrac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2}$ suit une loi $F_{v_1,v_2}$ avec $v_1 = n_1-1$ et $v_2 = n_2-1$.
- **Méthode** : calculer F (rapport de deux carrés moyens), le situer dans la loi $F$ à deux degrés de liberté ($df_1$ au numérateur, $df_2$ au dénominateur), calculer la p-value : probabilité d'une valeur au moins aussi grande si $H_0$ est vraie.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Formule de F, première diapositive** : image lue directement, elle écrit $F = \dfrac{\text{variance not explained}}{\text{variance explained}}$. C'est l'inverse de la définition usuelle, et de la formule $MS_{model}/MS_{error}$ donnée juste après, comme de la formule en $TSS$ et $RSS$. Il faut lire variance expliquée sur variance non expliquée (complément). **À corriger avant un examen.**
2. **Intervalle de prédiction de l'exemple** : image lue directement, la diapositive écrit « $4{,}897 \le y_4 \le 0{,}503$ ». Calcul refait : $3{,}182 \times 0{,}6055 \times \sqrt{1{,}3} \approx 2{,}20$, donc $0{,}503 \le y_4 \le 4{,}897$ (complément). **À corriger avant un examen.** L'intervalle de confiance voisin, $[1{,}645 ; 3{,}755]$, est exact.
3. **Règle de rejet** : « on ne rejette pas $H_0$ si la valeur critique est plus petite que la valeur $F$, sauf si la p-value est petite » (diapositive reprise dans le [[Cours 12 - ANOVA and F-statistic (résumé)|Cours 12]]). On rejette quand $F$ dépasse la valeur critique (complément). Image non ouverte, mais le texte de la note porte la même phrase.
4. **Notations de $p$ et $k$** : $p$ désigne les paramètres, constante comprise, dans la formule de F ($p-1$ et $n-p$), alors que la régression multiple parle de $k$ variables et de $n-(k+1)$ degrés de liberté. Avec $p = k+1$ les deux sont cohérents.
5. **$\hat{X}$ pour $\bar{X}$** : la transcription lit un chapeau, c'est vraisemblablement une barre. Image non ouverte.
6. **Couleurs de la figure de prédiction** : le texte de l'étudiant parle de droite violette pour $\hat{y}$ et orange pour $E(y)$ ; la transcription décrit $E(y)$ en rouge. Sans conséquence.
