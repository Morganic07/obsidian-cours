---
type: source
tags:
  - year3
sources:
  - "[[Raw/Year 3/Data analysis (Thanos)/Cours 1 :.docx|Cours 1 (Data analysis)]]"
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Data analysis (Thanos)/Cours 1 :.docx|Cours 1 (Data analysis)]], dans [[Cours/Probabilités et statistiques/Data analysis/_index|Data analysis]].
## Idée générale

Premier contact avec le [[Langage R]] : un langage où tout passe par des fonctions et où tout est un objet. Le cours liste les structures de données, les fonctions de base et le sens des opérateurs dans une formule.

## Bases (*basics*)

- R est très **fonctionnel** : tout se fait par des fonctions.
- Arguments nommés stricts (*strict named arguments*).
- Les abréviations sont acceptées dans les arguments (`T` pour `TRUE`).
- **Orienté objet** : tout est un objet.
- Aide : `help("Topic")` ou `?topic`.
- Concrètement, R associe les arguments d'un appel dans cet ordre : d'abord par nom exact, puis par début de nom (dans `seq(1, 10, length = 4)`, `length` désigne l'argument `length.out`), enfin par position. Nommer les arguments rend l'appel lisible et indépendant de leur ordre. [[Complément hors du cours|ⓘ]]
- `T` et `F` ne sont pas des mots réservés mais des variables qui valent `TRUE` et `FALSE` : on peut les écraser (`T <- 0`), d'où l'habitude d'écrire `TRUE` et `FALSE` en entier dans un script. [[Complément hors du cours|ⓘ]]
- L'affectation s'écrit `<-` (`x <- 5`) ; `=` marche aussi au niveau du script, mais sert surtout à nommer les arguments dans un appel de fonction. [[Complément hors du cours|ⓘ]]

## Structures de données (*data structures*)

R accepte pratiquement tout type de données.

| | Linéaire (*linear*) | Rectangulaire (*rectangular*) |
|---|---|---|
| Même type (*all same type*) | vecteur (*vector*) | matrice (*matrix*) |
| Types mélangés (*mixed*) | liste (*list*) | [[Data frame]] |

Comparaison matrice / data frame (tableau du cours) :

| [[Matrice]] | Data frame |
|---|---|
| Ensemble de données rangées en rectangle à deux dimensions | Stocke des tables qui contiennent plusieurs types de données, en plusieurs colonnes appelées champs (*fields*) |
| Tableau $m \times n$ d'un seul type de données | Liste de vecteurs de même longueur ; forme généralisée de la matrice |
| Nombre fixe de lignes et de colonnes | Nombre variable de lignes et de colonnes |
| Les colonnes ne contiennent qu'un seul type | Les données doivent être de type numérique, caractère ou facteur |
| Homogène | Hétérogène |

![[Séance 1 - Data analysis (Thanos) - image10.png]]

*Figure : les structures de données de R (scalaire, vecteur, matrice, array, data frame, liste) et les types de données (numérique, caractère, logique).*

En R, un scalaire n'est qu'un vecteur de longueur 1, et les opérations sont **vectorisées** : `c(1, 2, 3) * 2` donne `2 4 6` sans boucle. Quand deux vecteurs n'ont pas la même longueur, le plus court est **recyclé** (`c(1, 2, 3, 4) + c(10, 20)` donne `11 22 13 24`), avec un avertissement si la longueur la plus grande n'est pas un multiple de l'autre. [[Complément hors du cours|ⓘ]]

Si l'on mélange des types dans un vecteur, R les convertit tous vers le type le plus général (logique → numérique → caractère) : `c(1, "a", TRUE)` donne trois chaînes de caractères. C'est pour garder des types différents qu'existent la liste et le data frame. [[Complément hors du cours|ⓘ]]

## Framework, bibliothèque, paquet, module

Voir [[Module, paquet, bibliothèque et framework]].

- **Module** : le plus petit morceau de logiciel ; un ensemble de méthodes ou de fonctions prêtes à être utilisées ailleurs.
- **Paquet** (*package*) : un ensemble de modules, en général de même but fonctionnel, pour les inclure tous d'un coup.
- **Bibliothèque** (*library*) : un ensemble de paquets ; elle offre des fonctionnalités prêtes à l'emploi, qu'on inclut dans son code. Elle n'impose aucun style de code.
- **Framework** : un ensemble de bibliothèques qui fournit aussi une **architecture** de développement. On n'inclut pas un framework : on intègre son code dedans. C'est l'ossature (*wire frame*) du projet, d'où le style de code qu'il impose.
- En R, les paquets viennent surtout du dépôt officiel CRAN : `install.packages("nom")` les télécharge une fois pour toutes, `library(nom)` les charge à chaque session. Dans le vocabulaire de R, la « library » est le dossier où sont installés les paquets. [[Complément hors du cours|ⓘ]]

## Quelques fonctions de base

```r
search()                              # répertoires et données chargés
ls()                                  # objets stockés
attach(NameOfTheDataset, expression)  # ajoute un jeu de données au chemin de recherche
detach(NameOfTheDataset)              # le retire après l'analyse
```

`attach` a un défaut : les colonnes attachées peuvent masquer, ou être masquées par, des objets de même nom déjà présents, et oublier `detach` laisse ce masquage en place. On lui préfère souvent `with(myframe, mean(age))`, qui ne vaut que pour l'expression évaluée. [[Complément hors du cours|ⓘ]]

### Lire des données

- directement par un vecteur : `x <- c(1,2,3...)` ;
- les fonctions `scan` et `read.table` ;
- `read.csv("fichier.csv")` est la variante de `read.table` réglée pour un [[Fichier CSV]] (séparateur virgule, première ligne d'en-tête) ; `read.csv2` pour le format à point-virgule et virgule décimale courant en France. [[Complément hors du cours|ⓘ]]
- `matrix` pour lire des matrices de données ;
- `data.frame` pour des données mixtes ;
- `library(foreign)` pour des données venant d'autres logiciels.

### Accéder aux variables

- `edit(<mydataobject>)` ;
- les indices (*subscripts*), outils essentiels :
  - `x[1]` : premier élément du vecteur `x` ;
  - `y[1,]` : première ligne de la matrice `y` ;
  - `y[,1]` : première colonne de la matrice `y` ;
  - les indices commencent à 1 (et non à 0 comme en C ou en Python), et un indice négatif **exclut** : `x[-1]` est `x` sans son premier élément. [[Complément hors du cours|ⓘ]]
- le signe `$` pour les listes et data frames : `myframe$age` donne la variable `age` de `myframe` ;
- `attach(dataframe)` : on accède ensuite aux variables par leur nom.

### Sous-ensembles (*subset data*)

- la fonction `subset()` découpe le data frame ;
- indices dans un data frame : `myframe[,1]` donne la première colonne ;
- un vecteur d'indices : `myframe[1:5, ]` donne les 5 premières lignes (sans la virgule, `myframe[1:5]` sélectionne les 5 premières colonnes) ; [[Erreurs du cours#^e-1-data-analysis|✎]]
- une expression logique : `myframe[myframe[,1] < 5, ]` donne toutes les lignes dont la première colonne contient une valeur inférieure à 5. [[Erreurs du cours#^e-1-data-analysis|✎]]

## Graphiques

- Tracer un objet : `plot(num.vec)` trace les valeurs en fonction de leur indice.
- `plot` envoie vers un périphérique graphique (*graphic device*) qu'on peut choisir : postscript, gif, jpeg… On les ouvre et on les ferme, par exemple `dev.off()`.
- Deux types de tracés :
  - **haut niveau** (*high level*) : graphique dessiné en un seul appel ;
  - **bas niveau** (*low level*) : ajoute des informations à un graphique existant.
- Exemples : `plot`, `hist`, `boxplot`, `barplot` sont de haut niveau (ils ouvrent un nouveau graphique) ; `points`, `lines`, `abline` (droite, par exemple `abline(lm(y ~ x))`), `text`, `legend` sont de bas niveau. Pour écrire dans un fichier : `png("figure.png")`, les appels de tracé, puis `dev.off()` qui ferme le fichier. [[Complément hors du cours|ⓘ]]

## Statistiques usuelles

R a des fonctions pour toutes les statistiques courantes :

- `summary()` : minimum, moyenne, médiane, premier et troisième [[Quartiles et valeurs aberrantes|quartiles]], maximum d'une variable numérique ;
- `stem()` : diagramme tige et feuilles ([[Diagramme tige et feuilles]]) ;
- `table()` : tableau d'effectifs d'une variable catégorielle.
- Une donnée absente se note `NA` ([[Valeur manquante]]). Elle se propage : `mean(c(1, NA, 3))` vaut `NA`, et il faut `mean(x, na.rm = TRUE)` pour l'ignorer ; `is.na(x)` repère les valeurs manquantes. `summary()` compte les `NA` de chaque variable. [[Complément hors du cours|ⓘ]]

## Facteurs et régresseurs

- **Facteurs** : variables catégorielles ; **régresseurs** : variables continues ([[Facteur (variable catégorielle)]]).
- Il **faut déclarer les facteurs**, sauf s'ils sont évidents pour R.
- R crée automatiquement les [[Variable indicatrice|variables indicatrices]] (*dummy variables*) des facteurs.
- Déclarer un facteur : `factor(x)` ou `as.factor(x)` ; `levels(f)` en donne les modalités. C'est indispensable quand des catégories sont codées par des nombres (régions 1, 2, 3) : sans déclaration, R les traiterait comme une variable continue. [[Complément hors du cours|ⓘ]]
- Pour un facteur à $k$ modalités, R crée $k - 1$ indicatrices et non $k$ : la première modalité sert de **référence**, et chaque coefficient mesure l'écart d'une modalité à cette référence. Avec $k$ indicatrices plus la constante, les colonnes seraient liées (leur somme vaut toujours 1) et le modèle ne pourrait pas être estimé. `relevel(f, ref = "B")` change la référence. [[Complément hors du cours|ⓘ]]

## Opérateurs dans R

Sens habituel et sens dans une formule de modèle ([[Formule de modèle en R]]) :

| Opérateur | Sens habituel | Sens dans une formule |
|---|---|---|
| `+` ou `-` | addition, soustraction | ajouter ou retirer des termes |
| `*` | multiplication | effets principaux et interactions |
| `/` | division | effet principal et imbrication (*nesting*) |
| `:` | suite (*sequence*) | interaction seule |
| `^` | puissance | limite la profondeur des interactions |
| `%in%` | pas de sens particulier | imbrication seule |

Une formule s'écrit `réponse ~ prédicteurs`, le tilde se lisant « expliqué par » : `lm(y ~ x1 + x2, data = myframe)`. Équivalences utiles : `a * b` vaut `a + b + a:b` ; `(a + b + c)^2` donne les trois effets principaux et toutes les interactions deux à deux, sans celle d'ordre 3 ; `a / b` vaut `a + b %in% a` ; `y ~ x - 1` retire l'ordonnée à l'origine. Pour qu'un opérateur garde son sens arithmétique dans une formule, on l'enveloppe dans `I()` : `y ~ x + I(x^2)` ajoute un terme au carré. [[Complément hors du cours|ⓘ]]
