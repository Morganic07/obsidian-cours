---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Summary functions in RStudio :.docx|Summary functions in RStudio]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 3/Data analysis (Thanos)/Summary functions in RStudio :.docx|Summary functions in RStudio]], dans [[Data analysis (Thanos) (index)]]. En cas d'écart, le cours fait foi.

Aide-mémoire du [[Langage R]] (sous RStudio), sans théorie : chaque commande est donnée avec ce qu'elle renvoie.

## Point de départ

```r
x <- rnorm(50)   # affecte à x un vecteur de 50 valeurs tirées d'une loi normale
```

## Autres fonctions (vecteurs)

| Commande | Effet |
|---|---|
| `n <- length(x)` | nombre d'éléments de `x` (ici 50, donc `n = 50`) |
| `sort(x)` | trie les valeurs de `x` par ordre croissant |
| `K[3]` | renvoie le 3e élément du vecteur `K` |
| `w <- c(60, 72, 57, 90, 95, 72)` | `c()` crée un vecteur (ici 6 éléments) ; il accepte toutes les valeurs, pas seulement numériques |
| `cat()` | affiche dans la console le contenu de quelque chose |
| `seq(4, 9)` | renvoie `4 5 6 7 8 9` |
| `seq(4, 10, 2)` | renvoie `4 6 8 10` (pas de 2) |

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

## Graphiques

```r
hist(x)        # histogramme
plot(ecdf(x))  # tracé de l'ECDF de x
qqnorm(x)      # QQ plot de x
boxplot(x)     # boîte à moustaches de x
```

Voir [[Histogramme]], [[Diagramme de probabilité]] (QQ plot), [[Quartiles et valeurs aberrantes]] (boxplot).

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

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **« 3 ? 4 matrix »** : le signe × a été perdu, il faut lire « 3 × 4 ».
2. **`Seq(4,10,2)`** : R distingue les majuscules, il faut écrire `seq` (complément).
3. **`K[3]`** : le vecteur `K` n'est jamais défini dans la note.
