---
type: source
tags: [year3]
sources: ["[[Summary functions in RStudio]]"]
maj: 2026-11-05
---

Résumé de [[Summary functions in RStudio]], dans [[Data analysis (Thanos) (matière)]]. En cas d'écart, le cours fait foi.

Aide-mémoire du langage R, sans théorie.

## Contenu, dans l'ordre du cours

- **Vecteurs** : `c()` crée un vecteur, éventuellement avec des noms lus par `names()`. `length()`, `sort()`, `seq(4, 10, 2)`, et l'accès par `x[3]`. `cat()` affiche dans la console.
- **Statistiques** : `mean`, `sd`, `var`, `median`, `quantile`, et `ecdf` pour la fonction de répartition empirique.
- **Graphiques** : `hist`, `plot(ecdf(x))`, `qqnorm`, `boxplot`.
- **Matrices** : un vecteur auquel on donne `dim()`, rangé par colonnes. `matrix(1:12, nrow=3, byrow=T)` remplit par lignes. `rownames`, `colnames` et `t()` pour la transposée. `cbind` et `rbind` collent des vecteurs par colonnes ou par lignes.
- **Facteurs** : ils représentent une variable catégorielle. `factor(pain, levels=0:3)`, puis `levels()` nomme les catégories. `as.numeric()` renvoie le code interne, qui commence toujours à 1, même si le codage d'origine commençait à 0.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **« 3 ? 4 matrix »** : le signe × a été perdu, il faut lire « 3 × 4 ».
2. **`Seq(4,10,2)`** : R distingue les majuscules, il faut écrire `seq` (complément).
3. **`K[3]`** : le vecteur `K` n'est jamais défini dans la note.
