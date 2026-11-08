---
type: concept
tags: [year3, year4]
aliases: [valeurs manquantes, missing values, données manquantes, missing data]
sources: ["[[Raw/Year 4/data mining/cours data mining du prof.pdf|cours data mining du prof.pdf]]", "[[Raw/Year 3/Data analysis (Thanos)/Cours 1 :.docx|Cours 1 (Data analysis)]]"]
maj: 2026-11-08
---

Les valeurs manquantes font partie de ce qu'on nettoie lors du [[Prétraitement des données]].

L'[[Algorithme C4.5]] les traite ainsi : si la valeur de l'attribut $a_i$ manque, l'exemple est affecté à chacun des $n$ groupes définis par les valeurs de $a_i$, avec une probabilité estimée par la fréquence du groupe ; cette probabilité entre dans le calcul du gain et se propage dans l'arbre.

## En R

(complément, hors du cours, d'après [[1 - Data analysis]])

- Une valeur manquante se note `NA` (*Not Available*).
- Elle se propage dans les calculs : `mean(c(1, NA, 3))` vaut `NA`.
- L'argument `na.rm = TRUE` l'ignore : `mean(x, na.rm = TRUE)`, de même pour `sum`, `sd`, `var`, `median`, `min`, `max`.
- `is.na(x)` repère les valeurs manquantes (vecteur de `TRUE`/`FALSE`) ; `sum(is.na(x))` les compte.
- `summary()` compte les `NA` de chaque variable d'un tableau.

Notion parente : [[Prétraitement des données]]. Voir aussi : [[Langage R]].

Résumés : [[1 - pdf du prof]], [[1 - intro to data mining]], [[1 - Data analysis]]
