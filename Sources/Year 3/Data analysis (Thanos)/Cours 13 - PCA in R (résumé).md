---
type: source
sources: ["[[Cours 13 - PCA in R]]"]
maj: 2026-11-05
---

Résumé de [[Cours 13 - PCA in R]], dans [[Year 3 - Data analysis (Thanos)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Les étapes de l'[[Analyse en composantes principales]] refaites en R sur un petit jeu à deux dimensions, puis la lecture d'un cercle des corrélations. Suite pratique de [[Cours 13 - Principal Components Analysis (résumé)|Cours 13 - Principal Components Analysis]].

## Contenu, dans l'ordre du cours

- **Données** : deux vecteurs de 10 valeurs, `x` et `y`, tracés avec `plot(x, y, pch = 19)`.
- **Centrage** : soustraire la moyenne de chaque dimension (`x1 <- x - mean(x)`, `y1 <- y - mean(y)`).
- **Matrice de covariance** : `cov(x1, y1)`, `cov(x1, x1)`, `cov(y1, y1)`, assemblées dans une matrice 2 par 2 avec `matrix(..., byrow = TRUE, dimnames = ...)`.
- **Valeurs et vecteurs propres** : `e <- eigen(m)`. Un vecteur propre est une direction, une valeur propre indique la variance dans cette direction (voir [[Valeur propre]] et [[Vecteur propre]]).
- **Composantes** : on multiplie les valeurs centrées par le vecteur propre (`pc1 <- x1 * e$vectors[1,1] + y1 * e$vectors[2,1]`, de même pour `pc2` avec la colonne 2), puis `plot(pc1, pc2)`.
- **Avec `prcomp`** : `data.pca <- prcomp(data.frame(x, y))`, avec `data.pca$x` pour les scores. Le cours recommande de comparer le résultat à `eigen(m)`.
- **Interpréter un cercle des corrélations** (règle des angles, annotation de l'étudiant) : angle très fermé, corrélation positive ; angle droit, corrélation nulle ; angle très ouvert (environ 180°), corrélation négative.
- **Exemple (décathlon)** : cercle « PCA graph of variables », Dim 1 à 32,72 % et Dim 2 à 17,37 %, avec 400 m, 110 m haies, 100 m, 1500 m, disque, poids, saut en hauteur, javelot, saut à la perche, saut en longueur, et deux variables supplémentaires en pointillés bleus, Rank et Points. Lecture de l'étudiant : 100 m, 400 m et 110 m haies très corrélés ; disque, saut en hauteur et poids très corrélés ; saut en longueur et disque sans corrélation (angle droit) ; 100 m et saut en longueur négativement corrélés.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Les deux images ne sont pas ouvertes.

1. **« Standardization »** : le cours appelle ainsi la soustraction de la moyenne. C'est un centrage ; la standardisation divise aussi par l'écart-type (complément). Voir le paragraphe sur la mise à l'échelle dans [[Cours 13 - Principal Components Analysis (résumé)|le cours théorique]].
2. **« La plus grande valeur propre est la première composante »** : c'est son vecteur propre qui donne la première composante (complément).
3. **Règle des angles** : elle ne vaut que pour des variables bien représentées dans le plan des deux premières dimensions. Ici, ces deux dimensions n'expliquent que 50 % de la variance (complément).
4. **Signe de la corrélation 100 m et saut en longueur** : une corrélation négative est naturelle, un temps court et une grande distance étant tous deux de bonnes performances. Le cours ne l'explique pas.
5. **Faute de frappe** : « 100m.burdle » pour « 110m.hurdle » dans les remarques de l'étudiant, sans conséquence.
6. **Résultats des commandes R** : la note ne montre aucune sortie, seulement les commandes.
