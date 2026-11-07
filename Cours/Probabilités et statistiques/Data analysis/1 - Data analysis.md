---
type: source
tags:
  - year3
sources:
  - "[[Raw/Year 3/Data analysis (Thanos)/Cours 1 :.docx|Cours 1 (Data analysis)]]"
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 3/Data analysis (Thanos)/Cours 1 :.docx|Cours 1 (Data analysis)]], dans [[Cours/Probabilités et statistiques/Data analysis/_index|Data analysis]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Premier contact avec le [[Langage R]] : un langage où tout passe par des fonctions et où tout est un objet. Le cours liste les structures de données, les fonctions de base et le sens des opérateurs dans une formule.

## Bases (*basics*)

- R est très **fonctionnel** : tout se fait par des fonctions.
- Arguments nommés stricts (*strict named arguments*).
- Les abréviations sont acceptées dans les arguments (`T` pour `TRUE`).
- **Orienté objet** : tout est un objet.
- Aide : `help("Topic")` ou `?topic`.

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

## Framework, bibliothèque, paquet, module

Voir [[Module, paquet, bibliothèque et framework]].

- **Module** : le plus petit morceau de logiciel ; un ensemble de méthodes ou de fonctions prêtes à être utilisées ailleurs.
- **Paquet** (*package*) : un ensemble de modules, en général de même but fonctionnel, pour les inclure tous d'un coup.
- **Bibliothèque** (*library*) : un ensemble de paquets ; elle offre des fonctionnalités prêtes à l'emploi, qu'on inclut dans son code. Elle n'impose aucun style de code.
- **Framework** : un ensemble de bibliothèques qui fournit aussi une **architecture** de développement. On n'inclut pas un framework : on intègre son code dedans. C'est l'ossature (*wire frame*) du projet, d'où le style de code qu'il impose.

## Quelques fonctions de base

```r
search()                              # répertoires et données chargés
ls()                                  # objets stockés
attach(NameOfTheDataset, expression)  # ajoute un jeu de données au chemin de recherche
detach(NameOfTheDataset)              # le retire après l'analyse
```

### Lire des données

- directement par un vecteur : `x <- c(1,2,3...)` ;
- les fonctions `scan` et `read.table` ;
- `matrix` pour lire des matrices de données ;
- `data.frame` pour des données mixtes ;
- `library(foreign)` pour des données venant d'autres logiciels.

### Accéder aux variables

- `edit(<mydataobject>)` ;
- les indices (*subscripts*), outils essentiels :
  - `x[1]` : premier élément du vecteur `x` ;
  - `y[1,]` : première ligne de la matrice `y` ;
  - `y[,1]` : première colonne de la matrice `y` ;
- le signe `$` pour les listes et data frames : `myframe$age` donne la variable `age` de `myframe` ;
- `attach(dataframe)` : on accède ensuite aux variables par leur nom.

### Sous-ensembles (*subset data*)

- la fonction `subset()` découpe le data frame ;
- indices dans un data frame : `myframe[,1]` donne la première colonne ;
- un vecteur d'indices : `myframe[1:5]` « donne les 5 premières lignes » (selon le cours ; il faut `myframe[1:5, ]`, voir « Erreurs du cours ») ;
- une expression logique : `myframe[myframe[,1], < 5,]` « donne toutes les lignes dont la première colonne contient une valeur inférieure à 5 » (écriture du cours, invalide en R : voir « Erreurs du cours »).

## Graphiques

- Tracer un objet : `plot(num.vec)` trace les valeurs en fonction de leur indice.
- `plot` envoie vers un périphérique graphique (*graphic device*) qu'on peut choisir : postscript, gif, jpeg… On les ouvre et on les ferme, par exemple `dev.off()`.
- Deux types de tracés :
  - **haut niveau** (*high level*) : graphique dessiné en un seul appel ;
  - **bas niveau** (*low level*) : ajoute des informations à un graphique existant.

## Statistiques usuelles

R a des fonctions pour toutes les statistiques courantes :

- `summary()` : minimum, moyenne, médiane, premier et troisième [[Quartiles et valeurs aberrantes|quartiles]], maximum d'une variable numérique ;
- `stem()` : diagramme tige et feuilles ([[Diagramme tige et feuilles]]) ;
- `table()` : tableau d'effectifs d'une variable catégorielle.

## Facteurs et régresseurs

- **Facteurs** : variables catégorielles ; **régresseurs** : variables continues ([[Facteur (variable catégorielle)]]).
- Il **faut déclarer les facteurs**, sauf s'ils sont évidents pour R.
- R crée automatiquement les [[Variable indicatrice|variables indicatrices]] (*dummy variables*) des facteurs.

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

## Erreurs du cours

- [[Raw/Year 3/Data analysis (Thanos)/Cours 1 :.docx|Cours 1 (Data analysis)]] écrit « `myframe[myframe[,1], < 5,]` » (vérifié sur l'image) ; il faut « `myframe[myframe[,1] < 5, ]` » : la virgule avant `< 5` rend l'expression invalide en R.
- [[Raw/Year 3/Data analysis (Thanos)/Cours 1 :.docx|Cours 1 (Data analysis)]] écrit « `myframe[1:5]` gives first 5 rows of data » (vérifié sur l'image) ; sur un data frame, cette écriture sélectionne les 5 premières **colonnes**. Pour les 5 premières lignes, il faut `myframe[1:5, ]`.
