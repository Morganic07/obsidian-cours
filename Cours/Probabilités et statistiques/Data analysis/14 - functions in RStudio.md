---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Summary functions in RStudio :.docx|Summary functions in RStudio]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Data analysis (Thanos)/Summary functions in RStudio :.docx|Summary functions in RStudio]], dans [[Cours/Probabilités et statistiques/Data analysis/_index|Data analysis]].
Aide-mémoire du [[Langage R]] (sous RStudio), sans théorie : chaque commande est donnée avec ce qu'elle renvoie.

## Point de départ

```r
x <- rnorm(50)   # affecte à x un vecteur de 50 valeurs tirées d'une loi normale
```

Sans autre argument, `rnorm(50)` tire dans la [[Loi normale|loi normale]] centrée réduite ; `rnorm(50, mean = 10, sd = 2)` change la moyenne et l'écart-type. Les tirages changent à chaque exécution ; `set.seed(42)` placé avant fixe le générateur et rend le résultat reproductible. Les autres lois suivent le même schéma de noms : `r` pour tirer, `d` pour la densité, `p` pour la fonction de répartition, `q` pour les quantiles (`dnorm`, `pnorm`, `qnorm`, `runif`, `rbinom`…). [[Complément hors du cours|ⓘ]]

L'aide d'une fonction s'ouvre avec `?rnorm` ou `help(rnorm)` (onglet *Help* de RStudio). [[Complément hors du cours|ⓘ]]

## Autres fonctions (vecteurs)

| Commande | Effet |
|---|---|
| `n <- length(x)` | nombre d'éléments de `x` (ici 50, donc `n = 50`) |
| `sort(x)` | trie les valeurs de `x` par ordre croissant |
| `K[3]` | renvoie le 3e élément du vecteur `K` |
| `w <- c(60, 72, 57, 90, 95, 72)` | `c()` crée un vecteur (ici 6 éléments) ; il accepte toutes les valeurs, pas seulement numériques |
| `cat()` | affiche dans la console le contenu de quelque chose |
| `seq(4, 9)` | renvoie `4 5 6 7 8 9` |
| `seq(4, 10, 2)` | renvoie `4 6 8 10` (pas de 2) [[Erreurs du cours#^e-14-functions-in-rstudio\|✎]] |

Précisions sur ces fonctions : [[Complément hors du cours|ⓘ]]
- **Indices** : en R, le premier élément est `K[1]` (et non `K[0]` comme en Python ou en C). Un indice négatif exclut (`K[-1]` : tout sauf le premier), un vecteur d'indices extrait plusieurs éléments (`K[c(1, 3)]`), et une condition filtre (`x[x > 0]` : les valeurs positives).
- **`c()` et les types** : un vecteur ne contient qu'un seul type. Si on mélange, R convertit tout vers le type le plus général : `c(1, "a", TRUE)` donne `"1" "a" "TRUE"`, trois chaînes. Pour mêler des types, il faut une liste (`list()`) ou un [[Data frame|data frame]].
- **Calcul vectorisé** : les opérations s'appliquent élément par élément, sans boucle : `w * 2`, `w - mean(w)`, `w > 70`.
- **`cat()` et `print()`** : `print()` affiche un objet comme R le représente (avec `[1]` et les guillemets) ; `cat()` concatène et écrit du texte brut, sans retour à la ligne final : `cat("n =", n, "\n")`.
- **Raccourcis** : `4:9` équivaut à `seq(4, 9)` ; `seq(0, 1, length.out = 5)` fixe le nombre de valeurs au lieu du pas ; `rep(1, 3)` répète (`1 1 1`) ; `sort(x, decreasing = TRUE)` trie par ordre décroissant.

On peut nommer les éléments d'un vecteur, puis lire ou modifier ces noms avec `names()` :

```r
x <- c(red="Huey", blue="Dewey", green="Louie")
x
#    red    blue   green
# "Huey" "Dewey" "Louie"
names(x)
# "red" "blue" "green"
```

## Fonctions statistiques

```r
mean(x)      # moyenne
sd(x)        # écart-type
var(x)       # variance
median(x)    # médiane
quantile(x)  # quantiles
ecdf(x)      # fonction de répartition empirique (empirical cumulative distribution)
```

Voir [[Mesures de tendance centrale]], [[Variance et écart-type d'échantillon]], [[Quantile]], [[Fonction de répartition empirique]].

Ce que renvoient ces fonctions : [[Complément hors du cours|ⓘ]]
- `var(x)` et `sd(x)` divisent par $n-1$ : ce sont la variance et l'écart-type **d'échantillon** $s^2 = \frac{1}{n-1}\sum (x_i - \bar{x})^2$, pas ceux de la population.
- `quantile(x)` renvoie par défaut cinq valeurs, aux niveaux 0 %, 25 %, 50 %, 75 % et 100 % : minimum, premier quartile, médiane, troisième quartile, maximum. `quantile(x, 0.9)` donne le 9e décile. R propose neuf méthodes de calcul (argument `type`, 7 par défaut), qui peuvent différer légèrement du calcul à la main.
- `summary(x)` donne d'un coup minimum, quartiles, médiane, moyenne et maximum ; sur un data frame, il résume chaque colonne.
- `ecdf(x)` renvoie une **fonction** : `Fn <- ecdf(x)` puis `Fn(0)` donne la proportion des valeurs $\leq 0$.
- En présence de valeurs manquantes (`NA`), ces fonctions renvoient `NA` ; `mean(x, na.rm = TRUE)` les ignore ([[Valeur manquante]]).

## Graphiques

```r
hist(x)        # histogramme
plot(ecdf(x))  # tracé de l'ECDF de x
qqnorm(x)      # QQ plot de x
boxplot(x)     # boîte à moustaches de x
```

Voir [[Histogramme]], [[Diagramme de probabilité]] (QQ plot), [[Quartiles et valeurs aberrantes]] (boxplot).

Lecture du QQ plot : `qqnorm(x)` place les quantiles observés de `x` en face des quantiles théoriques de la loi normale ; si les points suivent à peu près une droite, la normalité est plausible. `qqline(x)`, lancé juste après, trace cette droite de référence. Le boxplot de R marque comme points isolés les valeurs situées à plus de 1,5 écart interquartile des quartiles. [[Complément hors du cours|ⓘ]]

## Matrices et tableaux (*matrices and arrays*)

Une [[Matrice]] est un vecteur auquel on donne une dimension :

```r
x <- 1:12
dim(x) <- c(3,4)
x
#      [,1] [,2] [,3] [,4]
# [1,]    1    4    7   10
# [2,]    2    5    8   11
# [3,]    3    6    9   12
```

L'affectation `dim` fixe ou change l'attribut de dimension : R traite alors le vecteur de 12 nombres comme une matrice 3 × 4. Le rangement se fait **par colonnes** (*column-major*) : les éléments de la première colonne, puis ceux de la deuxième, etc.

La fonction `matrix` est plus pratique :

```r
matrix(1:12, nrow=3, byrow=T)
#      [,1] [,2] [,3] [,4]
# [1,]    1    2    3    4
# [2,]    5    6    7    8
# [3,]    9   10   11   12

matrix(1:12, nrow=3, byrow=F)
#      [,1] [,2] [,3] [,4]
# [1,]    1    4    7   10
# [2,]    2    5    8   11
# [3,]    3    6    9   12
```

`byrow=T` remplit la matrice ligne par ligne au lieu de colonne par colonne.

Pour lire un élément : `x[2, 3]` (ligne 2, colonne 3) ; `x[2, ]` renvoie toute la ligne 2, `x[, 3]` toute la colonne 3 ; `dim(x)`, `nrow(x)` et `ncol(x)` donnent les dimensions. [[Complément hors du cours|ⓘ]]

Fonctions utiles sur les matrices : `rownames`, `colnames` et `t` pour la [[Transposée]] (`t` minuscule, à ne pas confondre avec `T` majuscule qui veut dire `TRUE`) :

```r
x <- matrix(1:12, nrow=3, byrow=T)
rownames(x) <- LETTERS[1:3]
x
#   [,1] [,2] [,3] [,4]
# A    1    2    3    4
# B    5    6    7    8
# C    9   10   11   12
t(x)
#      A B  C
# [1,] 1 5  9
# [2,] 2 6 10
# [3,] 3 7 11
# [4,] 4 8 12
```

`LETTERS` est une constante de R qui contient les 26 lettres majuscules (`letters` pour les minuscules) ; `LETTERS[1:3]` vaut `"A" "B" "C"`. Mieux vaut écrire `TRUE` en entier plutôt que `T` : `T` n'est qu'une variable prédéfinie, qu'un script peut écraser par mégarde (`T <- 0`), alors que `TRUE` est un mot réservé. [[Complément hors du cours|ⓘ]]

Calcul matriciel : `*` multiplie **élément par élément** ; le [[Produit matriciel|produit matriciel]] s'écrit `%*%`. `t(X) %*% X` calcule donc $X^TX$, la base de la [[Matrice de covariance|matrice de covariance]] (voir [[13 - Principal Components Analysis]]) ; `solve(A)` donne l'inverse de $A$, `solve(A, b)` résout $Ax = b$, `diag(3)` crée la matrice identité 3 × 3, `eigen(A)` renvoie valeurs et vecteurs propres, `cov(X)` et `cor(X)` les matrices de covariance et de corrélation des colonnes. [[Complément hors du cours|ⓘ]]

`apply(x, 1, sum)` applique une fonction à chaque ligne (`1`) ou à chaque colonne (`2`) ; pour les cas courants, `rowSums`, `colSums`, `rowMeans` et `colMeans` font de même plus vite. [[Complément hors du cours|ⓘ]]

On peut « coller » des vecteurs par colonnes (`cbind`) ou par lignes (`rbind`) :

```r
cbind(A=1:4, B=5:8, C=9:12)
#      A B  C
# [1,] 1 5  9
# [2,] 2 6 10
# [3,] 3 7 11
# [4,] 4 8 12

rbind(A=1:4, B=5:8, C=9:12)
#   [,1] [,2] [,3] [,4]
# A    1    2    3    4
# B    5    6    7    8
# C    9   10   11   12
```

## Facteurs (*factors*)

- Les données statistiques contiennent souvent des **variables catégorielles** (classe sociale, sexe…), qui subdivisent les données ([[Type de variable statistique]]).
- Elles sont en général saisies avec un code numérique.
- En R, il faut les déclarer comme **facteurs** ([[Facteur (variable catégorielle)]]) : cette structure permet notamment de donner des noms parlants aux catégories.
- Certaines analyses exigent que R distingue un code de catégorie d'une variable dont la valeur a un vrai sens numérique.

Un facteur a un ensemble de **niveaux** (*levels*). En interne, un facteur à quatre niveaux est fait de deux éléments : (a) un vecteur d'entiers entre 1 et 4 ; (b) un vecteur de caractères de longueur 4 qui décrit les niveaux.

### Exemple : niveau de douleur de cinq patients

```r
pain <- c(0,3,2,2,1)
fpain <- factor(pain, levels=0:3)
levels(fpain) <- c("none","mild","medium","severe")
```

1. `pain` est un vecteur numérique qui code la douleur de cinq patients.
2. `factor` crée le facteur `fpain`. L'argument `levels=0:3` indique que le codage d'entrée utilise les valeurs 0 à 3. On pourrait l'omettre, car R prend par défaut les valeurs de `pain` triées, mais c'est une bonne habitude de le garder.
3. La dernière ligne remplace les noms des niveaux par les quatre chaînes données.

```r
fpain
# [1] none severe medium medium mild
# Levels: none mild medium severe
as.numeric(fpain)
# [1] 1 4 3 3 2
levels(fpain)
# [1] "none" "mild" "medium" "severe"
```

`as.numeric` extrait le codage numérique (1 à 4) et `levels` les noms des niveaux. Le codage d'origine 0–3 a disparu : la représentation interne d'un facteur **commence toujours à 1**.

Piège classique : si les niveaux d'un facteur sont eux-mêmes des nombres (par exemple `factor(c(10, 20, 10))`), `as.numeric(f)` renvoie les codes internes `1 2 1`, pas les valeurs ; il faut passer par le texte : `as.numeric(as.character(f))` donne `10 20 10`. [[Complément hors du cours|ⓘ]]

`table(fpain)` compte les effectifs de chaque niveau, dans l'ordre des niveaux et même pour un niveau absent des données (ici `none` 1, `mild` 1, `medium` 2, `severe` 1) ; `summary(fpain)` fait de même. C'est la manière normale de résumer une variable catégorielle, dont on ne calcule pas la moyenne. [[Complément hors du cours|ⓘ]]

Pour une variable **ordinale** ([[2 - Introduction statistics]]), on crée un facteur ordonné : `factor(pain, levels = 0:3, ordered = TRUE)` (ou `ordered()`). R sait alors comparer les niveaux (`fpain < "severe"`) et en tirer une médiane par `quantile(fpain, 0.5, type = 1)`, ce qui n'a pas de sens pour un facteur simple, purement nominal. [[Complément hors du cours|ⓘ]]
