---
type: source
sources: ["[[Cours/Year 3/Data analysis (Thanos)/Cours 1|Cours 1 (Data analysis)]]"]
maj: 2026-11-05
---

Résumé de [[Cours/Year 3/Data analysis (Thanos)/Cours 1|Cours 1 (Data analysis)]], dans [[Year 3 - Data analysis (Thanos)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Premier contact avec R : un langage où tout passe par des fonctions et où tout est un objet. Le cours liste les structures de données, les fonctions de base et le sens des opérateurs dans une formule.

## Contenu, dans l'ordre du cours

- **Bases** : arguments nommés stricts, abréviations acceptées (`T` pour `TRUE`), aide par `help("Sujet")` ou `?sujet`.
- **Structures de données** (tableau du cours) :

| | Linéaire | Rectangulaire |
|---|---|---|
| Même type | vecteur | matrice |
| Types mélangés | liste | data frame |

  La matrice est homogène avec un nombre fixe de lignes et de colonnes. Le data frame est une liste de vecteurs de même longueur, hétérogène.
- **Module, paquet, bibliothèque, framework** : un module est le plus petit morceau de logiciel, un paquet en regroupe plusieurs, une bibliothèque regroupe des paquets sans imposer de style, un framework impose son architecture : on y intègre son code.
- **Fonctions de base** : `search()`, `ls()`, `attach()` et `detach()` d'un jeu de données.
- **Lire des données** : `c()`, `scan`, `read.table`, `matrix`, `data.frame`, `library(foreign)` pour d'autres logiciels.
- **Accéder aux variables** : `x[1]`, `y[1,]`, `y[,1]`, `myframe$age`, `edit()`.
- **Sous-ensembles** : `subset()`, indices, expressions logiques.
- **Graphiques** : `plot()`, périphériques graphiques (`dev.off()`), graphiques de haut niveau (un seul appel) ou de bas niveau (ajouts sur un graphique existant).
- **Statistiques usuelles** : `summary()`, `stem()`, `table()`.
- **Facteurs et régresseurs** : un facteur est catégoriel, un régresseur est continu. Il faut déclarer les facteurs, et R crée alors les variables indicatrices (dummy) tout seul.
- **Opérateurs dans une formule** : `+`/`-` ajoutent ou retirent des termes, `*` donne effets principaux et interactions, `/` effet principal et imbrication, `:` interaction seule, `^` limite la profondeur des interactions, `%in%` imbrication seule.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Images de ce cours non ouvertes : les transcriptions sont reprises telles quelles.

1. **`myframe[myframe[,1], < 5,]`** : l'expression recopiée est fausse en R, à cause de la virgule avant `< 5`. La forme correcte serait `myframe[myframe[,1] < 5, ]` (complément). Alerte de la transcription, vraisemblable mais image non ouverte.
2. **`myframe[1:5]`** donné comme « les 5 premières lignes » : en R, cette écriture sélectionne les 5 premières colonnes. Pour des lignes, il faut `myframe[1:5, ]` (complément).
3. **Soulignements et couleurs** de la diapositive sur les facteurs (« you must specify » souligné, « factors » en rouge) : perdus par la transcription, sans conséquence sur le sens.
