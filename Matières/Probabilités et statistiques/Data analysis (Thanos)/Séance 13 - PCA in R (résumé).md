---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 13 : PCA in R.docx|Cours 13 - PCA in R]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 3/Data analysis (Thanos)/Cours 13 : PCA in R.docx|Cours 13 - PCA in R]], dans [[Data analysis (Thanos) (matière)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Les étapes de l'[[Analyse en composantes principales]] refaites en R sur un petit jeu à deux dimensions, puis la lecture d'un cercle des corrélations. Suite pratique de [[Séance 13 - Principal Components Analysis (résumé)|Cours 13 - Principal Components Analysis]].

## 1. Les données

Un jeu simple à deux dimensions pour illustrer l'ACP ([[Langage R]]) :

```r
x <- c(2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2, 1, 1.5, 1.1)
y <- c(2.4, 0.7, 2.9, 2.2, 3.0, 2.7, 1.6, 1.1, 1.6, 0.9)

plot(x, y, pch = 19)
```

## 2. Centrer les données

On calcule la moyenne de chaque dimension et on la soustrait à chaque valeur de cette dimension. Le cours appelle cela « [[Centrage et réduction|standardization]] » : les dimensions ont maintenant une moyenne nulle (c'est en fait un centrage, voir Points à vérifier).

```r
mean(x)
mean(y)

x1 <- x - mean(x)
x1
y1 <- y - mean(y)
y1

plot(x1, y1, pch = 19)
```

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

## 4. Vecteurs propres et valeurs propres

On cherche les [[Vecteur propre|vecteurs propres]] et [[Valeur propre|valeurs propres]] de la matrice de covariance. Un vecteur propre est une **direction** ; une valeur propre est un nombre qui indique **combien de variance** les données ont dans cette direction.

```r
e <- eigen(m)
e
```

## 5. Calculer les composantes principales

« La plus grande valeur propre est la première composante principale » (selon le cours) : on multiplie les valeurs centrées par le premier vecteur propre, stocké dans `e$vectors[,1]`.

```r
pc1 <- x1 * e$vectors[1,1] + y1 * e$vectors[2,1]
pc1

pc2 <- x1 * e$vectors[1,2] + y1 * e$vectors[2,2]
pc2
data.frame(PC1 = pc1, PC2 = pc2)

plot(pc1, pc2, pch = 19)
```

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

## Interpréter l'ACP : le cercle des corrélations

### La règle des angles

Sur un [[Cercle des corrélations]], entre deux flèches de variables :

- **angle très fermé** (variables proches) : corrélation **positive** (elles vont dans le même sens) ;
- **angle droit** (90°) : corrélation **nulle** (aucun rapport) ;
- **angle très ouvert** (opposées, ~180°) : corrélation **négative** (elles vont en sens inverse).

### Exemple : le décathlon

![[Séance 13 - PCA in R - image1.png]]

*Figure : cercle des corrélations (« PCA graph of variables ») du décathlon, Dim 1 (32,72 %) et Dim 2 (17,37 %) ; Rank et Points sont des variables supplémentaires en pointillés bleus.*

Variables : 400m, 110m.hurdle, 100m, 1500m, Discus, Shot.put, High.jump, Javeline, Pole.vault, Long.jump ; variables supplémentaires : Rank (à gauche) et Points (à droite, presque sur l'axe Dim 1).

Lecture de l'étudiant :

- les performances au 100 m, 400 m et 110 m haies sont très corrélées ;
- les performances au disque, au saut en hauteur et au poids sont très corrélées ;
- le saut en longueur et le disque n'ont aucune corrélation (angle droit) ;
- le 100 m et le saut en longueur sont négativement corrélés.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Les deux images ne sont pas ouvertes (la règle des angles, image de texte, est recopiée d'après la transcription).

1. **« Standardization »** : le cours appelle ainsi la soustraction de la moyenne. C'est un centrage ; la standardisation divise aussi par l'écart-type (complément). Voir le paragraphe sur la mise à l'échelle dans [[Séance 13 - Principal Components Analysis (résumé)|le cours théorique]].
2. **« La plus grande valeur propre est la première composante »** : c'est son vecteur propre qui donne la première composante (complément).
3. **Règle des angles** : elle ne vaut que pour des variables bien représentées dans le plan des deux premières dimensions. Ici, ces deux dimensions n'expliquent que 50 % de la variance (complément).
4. **Signe de la corrélation 100 m et saut en longueur** : une corrélation négative est naturelle, un temps court et une grande distance étant tous deux de bonnes performances. Le cours ne l'explique pas.
5. **Faute de frappe** : « 100m.burdle » pour « 110m.hurdle » dans les remarques de l'étudiant, sans conséquence.
6. **Résultats des commandes R** : la note ne montre aucune sortie, seulement les commandes.
