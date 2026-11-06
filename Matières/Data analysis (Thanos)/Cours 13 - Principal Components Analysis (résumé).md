---
type: source
tags: [year3]
sources: ["[[Cours 13 - Principal Components Analysis]]"]
maj: 2026-11-05
---

Résumé de [[Cours 13 - Principal Components Analysis]], dans [[Data analysis (Thanos) (matière)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

L'[[Analyse en composantes principales]] (ACP, PCA) compresse beaucoup de variables en deux ou trois composantes qui gardent le maximum de variance. Le cours la construit d'abord géométriquement (meilleure droite à travers le nuage centré), puis algébriquement (vecteurs propres de la matrice de covariance, lien avec la [[Décomposition en valeurs singulières]]).

## Contenu, dans l'ordre du cours

- **Pourquoi** : visualiser 50 colonnes en 2 ou 3, et limiter le surapprentissage d'un modèle qui a trop de variables par rapport aux observations (il mémorise le bruit au lieu de la règle générale). Moins de « degrés de liberté » rend le modèle plus robuste.
- **Principe** : l'ACP trouve les composantes principales et transforme les données dans un nouveau système de coordonnées de dimension plus petite. Le premier axe est la composante qui explique le plus de variance.
- **Deux variables, six échantillons** (exemple du cours : variable 1 = 10, 11, 8, 3, 2, 1 ; variable 2 = 6, 4, 5, 3, 2,8, 1) :
  1. on calcule la moyenne de chaque variable, et on **centre** les données en déplaçant le centre à l'origine (les positions relatives ne changent pas) ;
  2. on cherche la droite qui passe par l'origine et s'ajuste le mieux : l'ACP projette les points sur la droite et cherche celle qui **minimise** les distances aux points, ce qui revient à **maximiser** les distances des projections à l'origine ;
  3. pour un point, $\|a_i\|^2 = \|w_ic\|^2 + \|a_i - w_ic\|^2$ (théorème de Pythagore, variance initiale = variance restante + variance perdue). Le premier terme du second membre se maximise, le deuxième se minimise, le total est constant. Maximiser la variance dans l'espace des composantes équivaut à minimiser l'erreur des moindres carrés (voir [[Projection orthogonale]] et [[Moindres carrés]]) ;
  4. **SS(distances de PC1) = valeur propre de PC1**, et la racine carrée de la valeur propre est la valeur singulière (voir [[Valeur propre]]). Le vecteur directeur de PC1 est le vecteur propre, ou vecteur singulier.
- **PC2** : en 2D, c'est la droite par l'origine perpendiculaire à PC1, sans optimisation. De même, SS(distances de PC2) = valeur propre de PC2.
- **Graphique final** : on tourne les axes pour que PC1 soit horizontal et on lit les coordonnées des échantillons sur les projections.
- **Pourcentages** : on convertit en variance autour de l'origine en divisant par $n-1$. Exemple : variance de PC1 = 15, de PC2 = 3, total 18, donc PC1 explique 15/18 = 83 % et PC2 17 %.
- **Trois variables** : même procédure. On ajoute PC3, perpendiculaire à PC1 et PC2. Le nombre de composantes est le plus petit entre le nombre de variables et le nombre d'échantillons. Les valeurs propres donnent la part de variation de chaque PC. Exemple : PC1 79 %, PC2 15 %, PC3 6 %, donc un graphique 2D (PC1, PC2) garde 94 %. Le **scree plot** est le diagramme en barres de ces parts. Les poids de PC1 (0,06 ; 0,15 ; 0,79) montrent que la variable 3 est la plus importante pour PC1.
- **Mise à l'échelle** : il faut mettre les variables sur la même échelle, en divisant par l'écart-type de chaque variable. Exemple : notes de maths sur 100 et d'histoire sur 10. Sans mise à l'échelle, les maths pèsent dix fois plus ; après division par 10, la PC1 suit la diagonale.
- **Vecteurs propres et valeurs propres** : les composantes principales sont les vecteurs propres de la matrice de covariance des données. Comme elle est [[Matrice symétrique|symétrique]], ces vecteurs sont orthogonaux. Chaque valeur propre indique la variance dans la direction de son vecteur. Une valeur propre nulle ou presque nulle : composante à écarter en réduction de dimension.
- **Matrice de covariance** : la diagonale donne les variances, hors diagonale les covariances. Avec $X \in \mathbb{R}^{n\times d}$ centrée (échantillons en lignes, variables en colonnes), $\Sigma = \dfrac{X^TX}{n}$ pour une population, $\dfrac{X^TX}{n-1}$ pour un échantillon.
- **Petit exemple** : deux étudiants, deux variables, matrice centrée $X = \begin{bmatrix}5 & 8\\-5 & -8\end{bmatrix}$, $X^TX = \begin{bmatrix}50 & 80\\80 & 128\end{bmatrix}$, divisé par $n-1 = 1$.
- **Loadings** : poids de chaque variable dans une PC (par exemple $PC1 = 0{,}9\,a_1 + 0{,}1\,a_2$). Le cours dit aussi que c'est le coefficient de corrélation entre la variable et la composante : proche de $+1$ ou $-1$, forte influence ; proche de 0, aucune.
- **Scores** : coordonnées d'un échantillon dans le système tourné, obtenues en multipliant les données par les loadings de l'axe.
- **Lien avec la SVD** : $A = U\Sigma V^T = \sigma_1u_1v_1^T + \dots + \sigma_ru_rv_r^T$ ; $V$ est la matrice des loadings, $U$ celle des scores. Le graphique des loadings trace les coefficients de PC1 contre ceux de PC2 ; le **biplot** superpose les loadings (vecteurs) et les scores (points).
- **Exemple de matrice de covariance, trois mesures sur quatre individus** : $X_1 = (1,2,1)$, $X_2 = (4,2,13)$, $X_3 = (7,8,1)$, $X_4 = (8,4,5)$. Moyenne $(5,4,5)$, $S = \begin{bmatrix}10&6&0\\6&8&-8\\0&-8&32\end{bmatrix}$. La variance totale est la trace de $S$ (50). La covariance entre $x_1$ et $x_3$ est nulle : variables non corrélées.
- **But de l'ACP (algèbre)** : trouver une matrice orthogonale $P$ avec $X = PY$, telle que les nouvelles variables $y_1,\dots,y_p$ soient non corrélées et rangées par variance décroissante. $Y_k = P^{-1}X_k = P^TX_k$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Images non ouvertes ; les calculs numériques de la matrice $S$ et de $X^TX$ ont été refaits et sont justes.

1. **Loading = corrélation, ou poids ?** Le cours donne les deux définitions. Les poids (coefficients de $V$) sont normés, de norme 1 ; la corrélation d'une variable avec une composante vaut le poids multiplié par l'écart-type de la composante et divisé par celui de la variable. Ce sont donc deux quantités différentes, que le cours confond (complément).
2. **« $U$ = matrice des scores »** : en SVD, les scores sont $U\Sigma$ (équivalent à $XV$). $U$ seule est normalisée (complément).
3. **« Maths a une variance 10 fois plus grande »** : si l'échelle est 10 fois plus grande, l'écart-type est 10 fois plus grand et la variance 100 fois (complément).
4. **Convention de « valeur propre »** : le cours dit « SS(distances) = valeur propre » (valeur propre de $X^TX$), puis « valeurs propres de la matrice de covariance » (SS divisé par $n-1$). Deux normalisations différentes, que le cours appelle toutes deux « eigenvalue » (complément).
5. **Nombre de composantes** : le cours dit « le plus petit entre variables et échantillons ». Après centrage, c'est plutôt $\min(d, n-1)$ (complément).
6. **Poids de PC1 et PC2 (trois variables)** : 0,06 ; 0,15 ; 0,79 puis 0,79 ; 0,06 ; 0,15. Ils sont donnés « pour l'exemple » et valent 1 en somme, alors qu'un vecteur propre unitaire a une somme de carrés égale à 1. Valeurs illustratives, pas des résultats calculés.
7. **Exemple de covariance, étiquettes** : le tableau parle d'« Heures » et de « Note », la suite du calcul de « Maths » et « Histoire ». Les nombres sont les mêmes.
8. **Flèche de PC2** (annotations $-0{,}242 \leftarrow -1$ et $4 \rightarrow 0{,}97$) : lecture incertaine d'après la transcription, image non ouverte.
9. **Bas d'image coupé** : la liste sur les scores peut continuer ; la dernière diapositive s'arrête sur la définition de $P$.
