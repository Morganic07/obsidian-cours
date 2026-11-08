---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 13 : PCA in R.docx|Cours 13 - PCA in R]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Data analysis (Thanos)/Cours 13 : PCA in R.docx|Cours 13 - PCA in R]], dans [[Cours/Probabilités et statistiques/Data analysis/_index|Data analysis]].
## Idée générale

Les étapes de l'[[Analyse en composantes principales]] refaites en R sur un petit jeu à deux dimensions, puis la lecture d'un cercle des corrélations. Suite pratique de [[13 - Principal Components Analysis|Cours 13 - Principal Components Analysis]].

## 1. Les données

Un jeu simple à deux dimensions pour illustrer l'ACP ([[Langage R]]) :

```r
x <- c(2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2, 1, 1.5, 1.1)
y <- c(2.4, 0.7, 2.9, 2.2, 3.0, 2.7, 1.6, 1.1, 1.6, 0.9)

plot(x, y, pch = 19)
```

## 2. Centrer les données

On calcule la moyenne de chaque dimension et on la soustrait à chaque valeur de cette dimension. C'est un [[Centrage et réduction|centrage]] (la standardisation diviserait en plus par l'écart-type) : les dimensions ont maintenant une moyenne nulle. [[Erreurs du cours#^e-13-pca-in-r|✎]]

```r
mean(x)
mean(y)

x1 <- x - mean(x)
x1
y1 <- y - mean(y)
y1

plot(x1, y1, pch = 19)
```

Ici $\bar{x} = 1{,}81$ et $\bar{y} = 1{,}91$. Centrer place l'origine au centre du nuage : les composantes sont des droites passant par l'origine, elles doivent donc passer par le centre de gravité des points. Le centrage ne change pas les covariances. La même opération s'écrit `scale(cbind(x, y), center = TRUE, scale = FALSE)` ; avec `scale = TRUE`, on divise aussi par l'écart-type (vraie standardisation), ce qui s'impose quand les variables n'ont pas la même unité. [[Complément hors du cours|ⓘ]]

## 3. Matrice de covariance

La [[Covariance et corrélation|covariance]] mesure comment les dimensions varient l'une par rapport à l'autre ; la [[Matrice de covariance]] contient toutes les covariances entre toutes les dimensions.

```r
cov(x1, y1)
cov(x1, x1)
cov(y1, y1)

m <- matrix(c(cov(x1, x1), cov(x1, y1), cov(y1, x1), cov(y1, y1)),
            nrow=2,
            ncol=2,
            byrow=TRUE,
            dimnames=list(c("x","y"),c("x","y")))

m
```

Résultat : $m \approx \begin{pmatrix} 0{,}6166 & 0{,}6154 \\ 0{,}6154 & 0{,}7166 \end{pmatrix}$. La diagonale contient les variances, les deux termes hors diagonale sont égaux ($\text{cov}(x, y) = \text{cov}(y, x)$) : la matrice est symétrique. La covariance positive dit que $x$ et $y$ augmentent ensemble. `cov()` divise par $n - 1$, et `cov(data.frame(x1, y1))` donne directement toute la matrice. [[Complément hors du cours|ⓘ]]

## 4. Vecteurs propres et valeurs propres

On cherche les [[Vecteur propre|vecteurs propres]] et [[Valeur propre|valeurs propres]] de la matrice de covariance. Un vecteur propre est une **direction** ; une valeur propre est un nombre qui indique **combien de variance** les données ont dans cette direction.

```r
e <- eigen(m)
e
```

Un vecteur propre $v$ vérifie $m\,v = \lambda\,v$ : la matrice ne fait que l'allonger d'un facteur $\lambda$. Les valeurs propres sont les racines de $\det(m - \lambda I) = 0$. Ici $\lambda_1 \approx 1{,}284$ et $\lambda_2 \approx 0{,}049$, de vecteurs propres $(0{,}678 ;\ 0{,}735)$ et $(-0{,}735 ;\ 0{,}678)$ au signe près. `eigen()` les range par valeur décroissante et les norme à 1 ; la matrice étant symétrique, ils sont orthogonaux. [[Complément hors du cours|ⓘ]]

La somme des valeurs propres est égale à la variance totale, $0{,}6166 + 0{,}7166 = 1{,}333$ (la trace de $m$). La part de variance de la première composante est donc $1{,}284 / 1{,}333 \approx 96{,}3\ \%$ : le nuage est presque une droite, et une seule dimension suffit à le résumer. [[Complément hors du cours|ⓘ]]

## 5. Calculer les composantes principales

Le vecteur propre associé à la plus grande valeur propre donne la première composante principale : on multiplie les valeurs centrées par le premier vecteur propre, stocké dans `e$vectors[,1]`. [[Erreurs du cours#^e-13-pca-in-r|✎]]

```r
pc1 <- x1 * e$vectors[1,1] + y1 * e$vectors[2,1]
pc1

pc2 <- x1 * e$vectors[1,2] + y1 * e$vectors[2,2]
pc2
data.frame(PC1 = pc1, PC2 = pc2)

plot(pc1, pc2, pch = 19)
```

Chaque score est le [[Produit scalaire|produit scalaire]] du point centré avec un vecteur propre, c'est-à-dire sa coordonnée sur le nouvel axe : l'ACP n'est qu'une **rotation** du repère. Le même calcul s'écrit en une ligne sous forme matricielle, `cbind(x1, y1) %*% e$vectors`. Contrôles : `var(pc1)` redonne $\lambda_1$, `var(pc2)` redonne $\lambda_2$, et `cov(pc1, pc2)` vaut 0, les nouvelles variables n'étant pas corrélées. [[Complément hors du cours|ⓘ]]

Voir [[Data frame]] et [[Loadings et scores (ACP)]].

## 6. ACP avec `prcomp()`

```r
data <- data.frame(x,y)
data.pca <- prcomp(data)
data.pca

names(data.pca)
data.pca$x                                     # les scores
plot(data.pca$x[,1], data.pca$x[,2], pch = 19)
eigen(m)                                       # à comparer avec le calcul à la main
data.pca
```

Contenu de l'objet renvoyé par `prcomp()` : [[Complément hors du cours|ⓘ]]

| Élément | Contenu | Lien avec le calcul à la main |
|---|---|---|
| `sdev` | écarts-types des composantes | $\sqrt{\lambda_k}$ : ici 1,133 et 0,221 |
| `rotation` | matrice des loadings, une colonne par composante | `e$vectors` |
| `x` | scores des observations | `pc1`, `pc2` |
| `center`, `scale` | moyennes soustraites, écarts-types utilisés (`FALSE` par défaut) | `mean(x)`, `mean(y)` |

Les colonnes de `rotation` et de `x` peuvent avoir le **signe opposé** à celui du calcul par `eigen()` : un vecteur propre n'est défini qu'au signe près, l'axe est le même et seule son orientation change. `prcomp()` passe par la [[Décomposition en valeurs singulières]] des données centrées plutôt que par la matrice de covariance, ce qui est numériquement plus sûr. [[Complément hors du cours|ⓘ]]

Fonctions utiles en complément : `summary(data.pca)` donne la part de variance de chaque composante (*Proportion of Variance*) et sa part cumulée ; `screeplot(data.pca)` trace l'éboulis des valeurs propres ; `biplot(data.pca)` superpose scores et loadings ; `prcomp(data, scale. = TRUE)` fait l'ACP sur données réduites, c'est-à-dire sur la matrice des corrélations. [[Complément hors du cours|ⓘ]]

Combien de composantes garder ? Deux règles d'usage : garder assez de composantes pour atteindre une part cumulée fixée (souvent 70 à 90 %), ou, pour une ACP réduite, garder celles dont la valeur propre dépasse 1, soit plus que la variance d'une variable d'origine (critère de Kaiser) ; on regarde aussi le « coude » de l'éboulis. [[Complément hors du cours|ⓘ]]

## Interpréter l'ACP : le cercle des corrélations

### La règle des angles

Sur un [[Cercle des corrélations]], entre deux flèches de variables :

- **angle très fermé** (variables proches) : corrélation **positive** (elles vont dans le même sens) ;
- **angle droit** (90°) : corrélation **nulle** (aucun rapport) ;
- **angle très ouvert** (opposées, ~180°) : corrélation **négative** (elles vont en sens inverse).

Ce que montre le cercle : dans une ACP réduite, la flèche d'une variable a pour coordonnées ses [[Covariance et corrélation|corrélations]] avec Dim 1 et Dim 2 ; elle reste donc dans le cercle de rayon 1. Le cosinus de l'angle entre deux flèches approche alors leur corrélation : $\cos 0° = 1$, $\cos 90° = 0$, $\cos 180° = -1$, d'où la règle des angles. [[Complément hors du cours|ⓘ]]

La règle ne vaut que pour les variables **bien représentées**, dont la flèche touche presque le cercle. Une flèche courte signifie que la variable est mal projetée sur ce plan et liée surtout à d'autres dimensions : deux flèches courtes proches ne sont pas forcément corrélées. La qualité de représentation se mesure par le $\cos^2$, carré de la longueur de la flèche. [[Complément hors du cours|ⓘ]]

### Exemple : le décathlon

![[Séance 13 - PCA in R - image1.png]]

*Figure : cercle des corrélations (« PCA graph of variables ») du décathlon, Dim 1 (32,72 %) et Dim 2 (17,37 %) ; Rank et Points sont des variables supplémentaires en pointillés bleus.*

Variables : 400m, 110m.hurdle, 100m, 1500m, Discus, Shot.put, High.jump, Javeline, Pole.vault, Long.jump ; variables supplémentaires : Rank (à gauche) et Points (à droite, presque sur l'axe Dim 1).

Une **variable supplémentaire** ne sert pas à construire les axes : on la projette ensuite sur le plan pour aider à l'interpréter. Ici, Points presque confondu avec Dim 1 montre que le premier axe mesure la **performance globale** au décathlon ; Rank est opposé à Points, puisqu'un petit rang est un bon classement. Le plan (Dim 1, Dim 2) conserve $32{,}72 + 17{,}37 \approx 50\ \%$ de l'inertie totale : la lecture du graphe n'en résume que la moitié. [[Complément hors du cours|ⓘ]]

Ce graphe est celui du paquet R **FactoMineR**, qui contient ce jeu de données `decathlon` (épreuves en colonnes 1 à 10, Rank et Points en 11 et 12, type de compétition en 13) : `res <- PCA(decathlon, quanti.sup = 11:12, quali.sup = 13)` trace le cercle des corrélations et le nuage des individus ; la fonction réduit les variables par défaut. [[Complément hors du cours|ⓘ]]

Lecture de l'étudiant :

- les performances au 100 m, 400 m et 110 m haies sont très corrélées ;
- les performances au disque, au saut en hauteur et au poids sont très corrélées ;
- le saut en longueur et le disque n'ont aucune corrélation (angle droit) ;
- le 100 m et le saut en longueur sont négativement corrélés.

Attention au sens des mesures : les courses sont des **temps** (plus petit = meilleur), les sauts et lancers des **distances ou hauteurs** (plus grand = meilleur). La corrélation négative entre 100 m et saut en longueur signifie donc que les athlètes rapides au sprint sautent aussi loin : leurs **performances** vont dans le même sens. C'est pour cela que les sprints (100 m, 110 m haies, 400 m) pointent vers la gauche, du côté de Rank, et le saut en longueur, le saut en hauteur et les lancers vers la droite, du côté de Points. Le 1500 m, le saut à la perche et le javelot ont des flèches courtes : ils sont mal représentés sur ce plan, et la règle des angles ne permet pas de conclure à leur sujet. [[Complément hors du cours|ⓘ]]
