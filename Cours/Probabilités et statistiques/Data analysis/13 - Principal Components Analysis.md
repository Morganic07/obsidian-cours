---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 13 : Principal Components Analysis.docx|Cours 13 - Principal Components Analysis]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Data analysis (Thanos)/Cours 13 : Principal Components Analysis.docx|Cours 13 - Principal Components Analysis]], dans [[Cours/Probabilités et statistiques/Data analysis/_index|Data analysis]]. Les encadrés en français de la note (exemple heures/note, loadings, scores) ne sont pas des diapositives : ce sont des captures d'un texte produit par un outil de génération de texte (bouton « Export to Sheets » visible sur l'image).

## Idée générale

L'[[Analyse en composantes principales]] (ACP, PCA) compresse beaucoup de variables en deux ou trois composantes qui gardent le maximum de variance. Le cours la construit d'abord géométriquement (meilleure droite à travers le nuage centré), puis algébriquement (vecteurs propres de la matrice de covariance, lien avec la [[Décomposition en valeurs singulières]]).

## Qu'est-ce que l'ACP ?

### Description

- Méthode statistique incontournable pour **simplifier et visualiser** des jeux de données complexes. Un tableau de 50 colonnes (variables) est impossible à visualiser ; l'ACP le « compresse » en 2 ou 3 colonnes en gardant le maximum d'information ([[Réduction de dimension]]).
- Elle sert aussi à **optimiser les algorithmes** : avec trop de variables par rapport au nombre d'observations, un modèle risque de « mémoriser » le bruit et les particularités inutiles au lieu d'apprendre la règle générale ([[Surapprentissage]]). En réduisant les « [[Variance et écart-type d'échantillon|degrés de liberté]] » (le nombre de variables indépendantes), on force le modèle à se concentrer sur les grandes tendances, ce qui le rend plus robuste face à de nouvelles données.

### Comment ça marche

- L'ACP trouve les **composantes principales** du jeu de données.
- Elle transforme les données dans un nouveau [[Sous-espace vectoriel|sous-espace]] de dimension plus petite, avec un nouveau système de coordonnées.
- Dans ce système, le premier axe est la **première composante principale**, celle qui explique la plus grande part de la variance des données.
- La méthode remonte à Karl Pearson (1901), qui cherchait la droite et le plan « les plus proches » d'un nuage de points, et à Harold Hotelling (1933), qui lui a donné son nom et sa forme par les vecteurs propres. C'est une méthode **non supervisée** ([[Apprentissage non supervisé]]) : elle n'utilise aucune variable à prédire. [[Complément hors du cours|ⓘ]]

## ACP sur DEUX variables

Données de l'exemple :

| | S1 | S2 | S3 | S4 | S5 | S6 |
|---|---|---|---|---|---|---|
| Variable 1 | 10 | 11 | 8 | 3 | 2 | 1 |
| Variable 2 | 6 | 4 | 5 | 3 | 2,8 | 1 |

### Trouver la droite d'ajustement optimale (la composante principale)

1. On calcule la moyenne de la variable 1, puis celle de la variable 2 : elles donnent le **centre des données**.
2. On **centre** les données : on déplace ce centre à l'origine (0,0). Ce déplacement ne change pas la position relative des points ([[Centrage et réduction]]).

![[Séance 13 - Principal Components Analysis - image48.png]]![[Séance 13 - Principal Components Analysis - image49.png]]![[Séance 13 - Principal Components Analysis - image45.png]]![[Séance 13 - Principal Components Analysis - image44.png]]

*Figure : moyenne de la variable 1, moyenne de la variable 2, centre des données, puis données déplacées vers l'origine.*

3. On essaie d'ajuster une droite passant par l'origine.

![[Séance 13 - Principal Components Analysis - image47.png]]![[Séance 13 - Principal Components Analysis - image50.png]]

*Figure : une première droite candidate, puis une droite qui semble bien ajustée ; « comment l'ACP obtient-elle cet ajustement ? »*

4. L'ACP **projette** les données sur la droite. Elle mesure les distances des points à la droite et cherche la droite qui **minimise** ces distances. C'est équivalent à chercher la droite qui **maximise** les distances des points projetés à l'origine.

![[Séance 13 - Principal Components Analysis - image3.png]]

*Figure : projection des six points sur la droite candidate ; minimiser les distances aux points revient à maximiser les distances des projections à l'origine.*

Ces distances sont **perpendiculaires** à la droite, ce qui distingue PC1 de la droite de [[Régression linéaire|régression]] de la variable 2 sur la variable 1 : la régression minimise les écarts **verticaux** (elle traite les deux variables de façon asymétrique, l'une expliquant l'autre), alors que l'ACP traite les deux variables à égalité. Les deux droites passent par le centre des données, mais n'ont en général pas la même pente. [[Complément hors du cours|ⓘ]]

**Deux visions équivalentes de l'ACP** : **maximiser** la variance (distance au carré) des points projetés dans cette direction, ou **minimiser** les [[Résidu (régression)|résidus]] (distance au carré) à cette direction.

![[Séance 13 - Principal Components Analysis - image13.png]]

*Figure : à gauche, maximiser la variance des projections le long de la droite ; à droite, minimiser les résidus perpendiculaires.*

Justification par le [[Théorème de Pythagore]] : pour un point, $D_3$ (origine → point), $D_1$ (origine → point projeté) et $D_2$ (point projeté → point) forment un triangle rectangle ([[Projection orthogonale]]) :

$$D_3^2 = D_1^2 + D_2^2 \qquad \text{variance initiale} = \text{variance restante} + \text{variance perdue}$$

$$\|\mathbf{a}_i\|^2 = \|w_i \mathbf{c}\|^2 + \|\mathbf{a}_i - w_i \mathbf{c}\|^2$$

- $\|\mathbf{a}_i\|^2$ est **constant** ;
- on **maximise** $\|w_i \mathbf{c}\|^2$, **ou** on **minimise** $\|\mathbf{a}_i - w_i \mathbf{c}\|^2$.

**Maximiser la variance dans l'espace des composantes équivaut à minimiser l'erreur des [[Moindres carrés|moindres carrés]].**

![[Séance 13 - Principal Components Analysis - image1.png]]

*Figure : un point, sa projection sur la composante, et les segments $D_1$, $D_2$, $D_3$.*

5. Valeur propre et valeur singulière :

$$SS(\text{distances PC1}) = \text{valeur propre de PC1} \qquad \sqrt{\text{valeur propre de PC1}} = \text{valeur singulière de PC1}$$

L'ACP trouve la somme des carrés des distances (SS) pour la droite la mieux ajustée : c'est la [[Valeur propre]] de PC1 ; sa racine est la valeur singulière ([[Décomposition en valeurs singulières]]).

![[Séance 13 - Principal Components Analysis - image33.png]]

*Figure : la droite PC1 et le vecteur unitaire qui la porte.*

### Trouver PC2

En 2D, **PC2 est simplement la droite passant par l'origine et perpendiculaire à PC1** : aucune optimisation n'est nécessaire. Son vecteur directeur est le **vecteur singulier** de PC2, ou [[Vecteur propre|vecteur propre]] de PC2 (annotations de la figure : $-0{,}242 \leftarrow -1$ et $4 \rightarrow 0{,}97$).

![[Séance 13 - Principal Components Analysis - image15.png]]

*Figure : PC1 (orange) et PC2 (verte, perpendiculaire) passant par l'origine, avec le vecteur propre de PC2.*

Lecture des annotations : la direction de PC2 est donnée par le vecteur $(-1, 4)$ (une unité à gauche, quatre vers le haut). On le **normalise** pour obtenir un [[Vecteur unitaire|vecteur unitaire]] : sa norme vaut $\sqrt{(-1)^2 + 4^2} = \sqrt{17} \approx 4{,}12$, d'où $\left(\tfrac{-1}{4{,}12}, \tfrac{4}{4{,}12}\right) \approx (-0{,}242\,;\ 0{,}970)$. Par perpendicularité, PC1 est alors portée par $(0{,}970\,;\ 0{,}242)$, de pente $1/4$. Ces coordonnées sont les **loadings** : avec un poids de 0,970 contre 0,242, la variable 1 domine PC1, et la variable 2 domine PC2. [[Complément hors du cours|ⓘ]]

$$d_1^2 + d_2^2 + \dots + d_6^2 = SS(\text{distances}) \qquad SS(\text{distances PC2}) = \text{valeur propre de PC2} \qquad \sqrt{\text{valeur propre de PC2}} = \text{valeur singulière de PC2}$$

La valeur propre de PC2 est la somme des (carrés des) distances entre les points projetés et l'origine.

![[Séance 13 - Principal Components Analysis - image29.png]]

*Figure : projections des six points sur PC2 et distances $d_i$ à l'origine.*

### Le graphique final de l'ACP

On fait tourner les axes pour que PC1 soit horizontal, puis on utilise les points projetés pour placer chaque échantillon dans le graphique (exemple : S6, placé à partir de ses projections sur PC1 et PC2).

![[Séance 13 - Principal Components Analysis - image46.png]]![[Séance 13 - Principal Components Analysis - image43.png]]

*Figure : rotation des axes (PC1 horizontal) et placement de S6 à partir de ses deux projections.*

On convertit les valeurs propres en **variation autour de l'origine** :

$$\frac{SS(\text{distances PC1})}{n-1} \qquad \frac{SS(\text{distances PC2})}{n-1} \qquad (n \text{ : taille de l'échantillon})$$

C'est la variance d'échantillon $S^2 = \dfrac{\sum (x_i - \bar{x})^2}{n-1}$ ($x_i$ une observation, $\bar{x}$ la moyenne, $n$ le nombre d'observations).

Deux conventions coexistent donc pour la « valeur propre » : la somme des carrés $SS$ (valeur propre de $X^TX$) ou la variance $SS/(n-1)$ (valeur propre de la [[Matrice de covariance|matrice de covariance]]). Elles diffèrent d'un facteur constant, si bien que les pourcentages de variance expliquée sont les mêmes ; les logiciels affichent en général la seconde. [[Complément hors du cours|ⓘ]]

**Exemple** : si var(PC1) = 15 et var(PC2) = 3, la variance totale des PC vaut 18 ; **PC1** explique $15/18 = 83\,\%$ et **PC2** $3/18 = 17\,\%$ de la variance totale.

![[Séance 13 - Principal Components Analysis - image35.png]]

*Figure : le graphique de l'ACP, PC1 (83 %) horizontal et PC2 (17 %) vertical.*

## ACP sur TROIS variables

| | S1 | S2 | S3 | S4 | S5 | S6 |
|---|---|---|---|---|---|---|
| Variable 1 | 10 | 11 | 8 | 3 | 2 | 1 |
| Variable 2 | 6 | 4 | 5 | 3 | 2,8 | 1 |
| Variable 3 | 12 | 9 | 10 | 2,5 | 1,3 | 2 |

Procédure semblable : d'abord **centrer** les données.

![[Séance 13 - Principal Components Analysis - image14.png]]

*Figure : les six échantillons dans l'espace des trois variables.*

![[Séance 13 - Principal Components Analysis - image34.png]]

*Figure : les données centrées.*

### Trouver PC1

Trouver la droite la mieux ajustée passant par l'origine. Avec 3 variables, le vecteur de projection a 3 coordonnées, dont les carrés totalisent 1 (vecteur unitaire) ; si ces carrés valent par exemple 0,06 (variable 1), 0,15 (variable 2), **0,79 (variable 3)**, **la variable 3 est la plus importante** pour PC1. [[Erreurs du cours#^e-13-principal-components-analysis|✎]]

![[Séance 13 - Principal Components Analysis - image20.png]]

*Figure : PC1 en 3D, proche de l'axe de la variable 3.*

### Trouver PC2

PC2 : la droite la mieux ajustée qui passe par l'origine **et** est perpendiculaire à PC1. Exemple, toujours en carrés des coordonnées : 0,79 (variable 1), 0,06 (variable 2), 0,15 (variable 3) : la variable 1 est la plus importante. [[Erreurs du cours#^e-13-principal-components-analysis|✎]]

![[Séance 13 - Principal Components Analysis - image25.png]]

*Figure : PC1 et PC2 perpendiculaires en 3D.*

### Trouver PC3

PC3 : la droite la mieux ajustée qui passe par l'origine et est perpendiculaire à PC1 et PC2.

**Le nombre total de composantes** utiles est égal au nombre de variables ou au nombre d'échantillons moins un, **le plus petit des deux**. [[Erreurs du cours#^e-13-principal-components-analysis|✎]]

Plus précisément, le nombre de composantes de variance non nulle est au plus $\min(d,\ n-1)$ pour $d$ variables et $n$ échantillons : une fois les données centrées, $n$ points n'engendrent qu'un espace de dimension $n-1$ au plus (deux points centrés sont symétriques par rapport à l'origine, donc sur une même droite : une seule composante utile). C'est le [[Rang d'une matrice|rang]] de la matrice centrée. [[Complément hors du cours|ⓘ]]

![[Séance 13 - Principal Components Analysis - image36.png]]

*Figure : PC1, PC2 et PC3, deux à deux perpendiculaires.*

Une fois toutes les PC calculées, on utilise les valeurs propres [SS(distances)] pour calculer la proportion de variation expliquée par chaque PC.

Exemple : PC1 79 %, PC2 15 %, PC3 6 %. PC1 et PC2 expliquent la grande majorité de la variation : un graphique 2D (PC1, PC2) est une « bonne approximation » du graphique 3D, il rend compte de **94 %** de la variation. Le **scree plot** est le diagramme en barres de ces pourcentages.

![[Séance 13 - Principal Components Analysis - image18.png]]

*Figure : les trois PC en 3D et le scree plot (PC1 ≈ 79, PC2 ≈ 15, PC3 ≈ 6).*

Combien de composantes garder ? Trois règles usuelles, à croiser : [[Complément hors du cours|ⓘ]]
- **le coude** (*elbow*) du scree plot (en français, « diagramme des valeurs propres » ou « éboulis ») : on garde les composantes situées avant la cassure, là où les barres cessent de décroître fortement ;
- **la part cumulée** : on garde assez de composantes pour atteindre un seuil fixé à l'avance, souvent 70 à 90 % de la variance totale (ici PC1 et PC2, 94 %) ;
- **le critère de Kaiser**, pour une ACP sur données réduites : on garde les composantes de valeur propre supérieure à 1, c'est-à-dire celles qui résument plus de variance qu'une seule variable d'origine (chacune a une variance de 1 après réduction).

### Passer du graphique 3D au graphique 2D de l'ACP

1. On retire tout sauf les données, PC1 et PC2.
2. On projette les échantillons sur PC1 et PC2.
3. On fait tourner pour que PC1 soit horizontal et PC2 vertical (plus lisible), et on place chaque échantillon (exemple : S6).

![[Séance 13 - Principal Components Analysis - image9.png]]![[Séance 13 - Principal Components Analysis - image10.png]]

*Figure : les données avec PC1 (79 %) et PC2 (15 %) seulement, puis leurs projections.*

![[Séance 13 - Principal Components Analysis - image4.png]]

*Figure : le graphique 2D final, PC1 horizontal et PC2 vertical, avec l'exemple de S6.*

## Mise à l'échelle des données (*scaling*)

**Mise à l'échelle : diviser par l'[[Espérance et variance|écart-type]] de la variable.** Il faut toujours vérifier que les variables sont sur la **même échelle** (mêmes unités) ; sinon, les mettre à l'échelle.

Exemple : notes de maths (de 0 à 100) et d'histoire (de 0 à 10).

| | Étudiant 1 | Étudiant 2 | Étudiant 3 | Étudiant 4 | … |
|---|---|---|---|---|---|
| Maths | 95 | 88 | 93 | 75 | … |
| Histoire | 9 | 8 | 10 | 7 | … |

![[Séance 13 - Principal Components Analysis - image23.png]]

*Figure : les points s'étalent le long de l'axe des maths (0 à 100) et très peu sur celui de l'histoire (0 à 10).*

Après centrage, l'ACP donne à la variable « Maths » une variance (importance) environ 100 fois plus grande que celle de l'histoire (écart-type 10 fois plus grand, donc variance 100 fois plus grande) : PC1 est presque horizontale. [[Erreurs du cours#^e-13-principal-components-analysis|✎]]

![[Séance 13 - Principal Components Analysis - image6.png]]

*Figure : sans mise à l'échelle, PC1 suit presque l'axe des maths.*

Si on divise les notes de maths par 10 (9,5 ; 8,8 ; 9,3 ; 7,5 ; …) et qu'on relance l'ACP, PC1 suit la diagonale des points.

![[Séance 13 - Principal Components Analysis - image30.png]]

*Figure : après mise à l'échelle, PC1 suit la diagonale ascendante.*

En pratique, on **centre et réduit** chaque variable : $z = \dfrac{x - \bar{x}}{s}$ ([[Centrage et réduction]]). Chaque variable a alors une variance de 1, et la matrice de covariance des données réduites est la **matrice de corrélation** des données d'origine ([[Covariance et corrélation]]) : une ACP sur données réduites (dite **ACP normée**) est une ACP sur la matrice de corrélation. La variance totale vaut alors le nombre $d$ de variables. Sans réduction, on parle d'ACP sur la matrice de covariance, légitime seulement si toutes les variables ont la même unité et des dispersions comparables. [[Complément hors du cours|ⓘ]]

## Vecteurs propres et valeurs propres

- **Mathématiquement**, les composantes principales sont les **[[Vecteur propre|vecteurs propres]] de la [[Matrice de covariance|matrice de covariance]]** du jeu de données d'origine.
- Comme la matrice de covariance est **[[Matrice symétrique|symétrique]]**, ses vecteurs propres sont **orthogonaux** ([[Théorème spectral]]).
- Les composantes principales (vecteurs propres) correspondent aux directions (dans l'espace d'origine à $n$ dimensions) de plus grande variance.
- Chaque vecteur propre a une [[Valeur propre|valeur propre]] associée, un scalaire. Le vecteur propre est une direction ; la valeur propre indique **combien de variance** les données ont le long de ce vecteur (de cette composante).
- Plus la valeur propre est grande, plus la composante explique de variance. Une composante de très petite valeur propre explique mal la variance ; une valeur propre nulle signifie qu'elle n'en explique aucune.
- En [[Réduction de dimension|réduction de dimension]], on écarte en général les composantes de valeur propre nulle ou presque nulle.
- Définition à garder en tête : $\mathbf{v}$ (non nul) est vecteur propre de la matrice de covariance $\Sigma$, de valeur propre $\lambda$, si $\Sigma\mathbf{v} = \lambda\mathbf{v}$. Pour un vecteur unitaire $\mathbf{v}$, la variance des données projetées sur $\mathbf{v}$ vaut $\mathbf{v}^T\Sigma\mathbf{v}$ ; elle est maximale, égale à la plus grande valeur propre $\lambda_1$, quand $\mathbf{v}$ est le vecteur propre associé. C'est pourquoi PC1 est ce vecteur propre. [[Complément hors du cours|ⓘ]]
- La somme des valeurs propres est égale à la [[Trace d'une matrice|trace]] de $\Sigma$, c'est-à-dire à la variance totale : la part de variance expliquée par la composante $k$ est $\lambda_k / (\lambda_1 + \dots + \lambda_d)$. [[Complément hors du cours|ⓘ]]
- Le **signe** d'un vecteur propre est arbitraire ($-\mathbf{v}$ est aussi vecteur propre) : deux logiciels peuvent donner des composantes de signes opposés, ce qui retourne le graphique sans changer l'interprétation. [[Complément hors du cours|ⓘ]]

## Matrice de covariance

| | $x_1$ | $x_2$ | $x_3$ | $x_4$ |
|---|---|---|---|---|
| $x_1$ | $Var(x_1)$ | $Cov(x_1,x_2)$ | $Cov(x_1,x_3)$ | $Cov(x_1,x_4)$ |
| $x_2$ | | $Var(x_2)$ | $Cov(x_2,x_3)$ | $Cov(x_2,x_4)$ |
| $x_3$ | | | $Var(x_3)$ | $Cov(x_3,x_4)$ |
| $x_4$ | | | | $Var(x_4)$ |

La **diagonale** donne la variance de chaque variable (la partie sous la diagonale est symétrique, laissée en noir sur la diapositive).

Calcul :

- Soit une matrice de données $X$, avec les **échantillons en lignes** et les **variables (features) en colonnes**, et chaque variable de moyenne nulle (« **de-meaning** », centrage) :
$$X = \begin{pmatrix} | & | & & | \\ X_1 & X_2 & \cdots & X_d \\ | & | & & | \end{pmatrix} \in \mathbb{R}^{n \times d}$$
- On calcule la covariance par un [[Produit scalaire|produit scalaire]] (*dot product*), c'est-à-dire le produit matriciel $X^TX$ (lignes $X_1, \dots, X_d$ de $X^T$ fois colonnes $X_1, \dots, X_d$ de $X$).
- $(X^TX)_{ij}$ mesure la similarité des variations de la $i$-ème et de la $j$-ème variable. Cette valeur grandit avec le nombre d'échantillons $n$ ; on divise donc par $n$ :

$$\Sigma = cov(X) \equiv \frac{X^T X}{n} \text{ (population entière)} \qquad cov(X) \equiv \frac{X^T X}{n-1} \text{ (échantillon)}$$

### Exemple : heures de révision et note à l'examen

Deux étudiants (S1 et S2), deux variables :

| Étudiant | Heures ($x_1$) | Note ($x_2$) |
|---|---|---|
| S1 | 15 | 18 |
| S2 | 05 | 02 |

**Étape 1 : centrage** (*de-meaning*). Moyenne des heures : $(15+5)/2 = 10$ ; moyenne des notes : $(18+2)/2 = 10$. S1 : $+5$ (heures), $+8$ (note) ; S2 : $-5$, $-8$.

$$X = \begin{bmatrix} 5 & 8 \\ -5 & -8 \end{bmatrix} \qquad X^T = \begin{bmatrix} 5 & -5 \\ 8 & -8 \end{bmatrix}$$

(la suite du calcul appelle les deux colonnes « Maths » et « Histoire »).

**Étape B : produit $X^T X$** (ligne de $X^T$ × colonne de $X$) :

- haut-gauche : $(5 \times 5) + (-5 \times -5) = 50$ ;
- haut-droite : $(5 \times 8) + (-5 \times -8) = 80$ ;
- bas-gauche : $(8 \times 5) + (-8 \times -5) = 80$ ;
- bas-droite : $(8 \times 8) + (-8 \times -8) = 128$.

**Étape C : division par $n - 1$** ($n = 2$, donc $n - 1 = 1$) :

$$\Sigma = \begin{bmatrix} 50 & 80 \\ 80 & 128 \end{bmatrix}$$

**Suite de l'exemple : les composantes.** Les valeurs propres sont les racines de $\det(\Sigma - \lambda I) = \lambda^2 - \text{tr}(\Sigma)\,\lambda + \det(\Sigma) = 0$. Ici $\text{tr}(\Sigma) = 178$ et $\det(\Sigma) = 50 \times 128 - 80^2 = 0$, donc $\lambda_1 = 178$ et $\lambda_2 = 0$. Le vecteur propre de $\lambda_1$ est porté par $(5, 8)$ (vérification : $\Sigma \binom{5}{8} = \binom{890}{1424} = 178 \binom{5}{8}$), soit, normalisé, $(0{,}530\,;\ 0{,}848)$. PC1 explique 100 % de la variance et PC2 rien : avec deux étudiants, les deux points centrés sont alignés avec l'origine, et il n'y a qu'une composante utile ($n - 1 = 1$). [[Complément hors du cours|ⓘ]]

## Loadings et scores de l'ACP

Voir [[Loadings et scores (ACP)]].

### Loadings

1. **Le poids des variables** (*weighting*) : chaque composante est une nouvelle variable, combinaison des variables d'origine ($a_1, a_2, \ldots$). Le **loading** indique **quelle quantité** de chaque variable entre dans le mélange. Exemple : si $PC1 = 0{,}9 \times a_1 + 0{,}1 \times a_2$, alors 0,9 et 0,1 sont les loadings ; $a_1$ est le « moteur » de PC1, $a_2$ un ingrédient mineur.
2. **La corrélation avec l'axe** : dans une seconde convention, le mot loading désigne le [[Covariance et corrélation|coefficient de corrélation]] entre la variable d'origine et la composante ; ce n'est pas la même quantité que le poids : la corrélation vaut le poids multiplié par l'écart-type de la composante et divisé par celui de la variable. [[Erreurs du cours#^e-13-principal-components-analysis|✎]] Lecture de cette corrélation :
   - proche de $+1$ : variable et PC fortement liées, elles montent ensemble ;
   - proche de $-1$ : liées inversement, quand la variable monte, le score de la PC descend ;
   - proche de 0 : la variable n'a aucune influence sur cette PC, elle « parle » d'autre chose.

### Scores

1. **Les nouvelles coordonnées** : le score est la valeur d'un échantillon (individu, objet) une fois projeté sur une composante principale. Avant l'ACP, l'échantillon est défini par ses variables d'origine ($a_1, \dots, a_5$) ; après, par ses scores (score PC1, score PC2). C'est sa position dans le nouveau système de coordonnées pivoté.
2. **Le calcul** : pour le score d'un individu sur PC1, on multiplie ses données d'origine par les loadings de cet axe :
$$\text{Score} = \text{Donnée}_1 \times \text{Loading}_1 + \text{Donnée}_2 \times \text{Loading}_2 + \dots$$
Plusieurs colonnes deviennent un seul chiffre récapitulatif.

### Matrices des loadings et des scores (lien avec la SVD)

Par la [[Décomposition en valeurs singulières]] d'une matrice $A$ ($m \times n$) :

$$A = U S V^T = \sigma_1 u_1 v_1^T + \dots + \sigma_r u_r v_r^T$$

avec $U$ ($m \times m$), $S$ ($m \times n$, diagonale $\sigma_1, \dots, \sigma_r$ puis zéros), $V^T$ ($n \times n$) ; $V$ et $U$ sont **orthogonales**.

- **$V$ est la matrice des loadings** : $v_{ij}$ est le poids de chaque variable d'origine dans le calcul de la PC, c'est-à-dire sa contribution. Un **grand** loading (+ ou −) indique une forte relation entre la variable et la PC ; son **signe** dit si la corrélation est positive ou négative.
- **$US$ (soit $AV$) est la matrice des scores** : elle représente les données d'origine dans un **système de coordonnées tourné** ; $U$ seule en est la version normalisée (chaque colonne divisée par $\sigma_j$). [[Erreurs du cours#^e-13-principal-components-analysis|✎]]

**Graphique des loadings** (*loading plot*, → matrice de corrélation) : il trace les coefficients de chaque variable pour la première composante contre ceux de la deuxième. Il sert à **identifier les variables qui ont le plus d'effet sur chaque composante**. Les loadings vont de $-1$ à $+1$ : près de $\pm 1$, la variable influence fortement la composante ; près de 0, faiblement.

## Biplot

Le **biplot** superpose dans une seule figure :

- les **loadings** sous forme de **vecteurs** ;
- les **scores** des composantes sous forme de **points**, notés par le numéro d'observation.

Il sert à juger la structure des données et les loadings des deux premières composantes sur un seul graphique.

![[Séance 13 - Principal Components Analysis - image38.png]]

*Figure : biplot R des deux premières composantes ; numéros d'observations au centre et vecteurs rouges de loadings (a1 à a5).*

## Exemple : calculer la matrice de covariance

**Exemple 3** : trois mesures sur chacun de quatre individus d'un échantillon aléatoire. Vecteurs d'observation :

$$\mathbf{X}_1 = \begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix},\quad \mathbf{X}_2 = \begin{bmatrix} 4 \\ 2 \\ 13 \end{bmatrix},\quad \mathbf{X}_3 = \begin{bmatrix} 7 \\ 8 \\ 1 \end{bmatrix},\quad \mathbf{X}_4 = \begin{bmatrix} 8 \\ 4 \\ 5 \end{bmatrix}$$

Calculer la [[Moyenne empirique|moyenne d'échantillon]] et la matrice de covariance.

**Solution.** Moyenne :

$$\mathbf{M} = \frac{1}{4}\begin{bmatrix}20\\16\\20\end{bmatrix} = \begin{bmatrix}5\\4\\5\end{bmatrix}$$

Données centrées :

$$\hat{\mathbf{X}}_1 = \begin{bmatrix}-4\\-2\\-4\end{bmatrix},\ \hat{\mathbf{X}}_2 = \begin{bmatrix}-1\\-2\\8\end{bmatrix},\ \hat{\mathbf{X}}_3 = \begin{bmatrix}2\\4\\-4\end{bmatrix},\ \hat{\mathbf{X}}_4 = \begin{bmatrix}3\\0\\0\end{bmatrix} \qquad B = \begin{bmatrix}-4 & -1 & 2 & 3\\ -2 & -2 & 4 & 0\\ -4 & 8 & -4 & 0\end{bmatrix}$$

Matrice de covariance d'échantillon ($N - 1 = 3$) :

$$S = \frac{1}{3} B B^T = \frac{1}{3}\begin{bmatrix}30 & 18 & 0\\ 18 & 24 & -24\\ 0 & -24 & 96\end{bmatrix} = \begin{bmatrix}10 & 6 & 0\\ 6 & 8 & -8\\ 0 & -8 & 32\end{bmatrix}$$

**Lecture des coefficients de $S = [s_{ij}]$** : soit $\mathbf{X}$ un vecteur qui parcourt les vecteurs d'observation, de coordonnées $x_1, \ldots, x_p$ ($x_1$ parcourt les premières coordonnées de $\mathbf{X}_1, \ldots, \mathbf{X}_N$).

- Le coefficient diagonal $s_{jj}$ est la **variance** de $x_j$ ; elle mesure la dispersion des valeurs de $x_j$.
- La **variance totale** est la somme des variances de la diagonale, c'est-à-dire la **[[Trace d'une matrice|trace]]** de $S$ : $\text{tr}(S) = \sum_{i} s_{ii}$. Ici $\text{tr}(S) = 10 + 8 + 32 = 50$.
- Le coefficient $s_{ij}$ ($i \neq j$) est la **covariance** de $x_i$ et $x_j$. Dans l'exemple, la covariance entre $x_1$ et $x_3$ est 0 (coefficient (1,3)) : $x_1$ et $x_3$ sont **non corrélées**.
- L'analyse de données multivariées est très simplifiée quand la plupart des variables sont non corrélées, c'est-à-dire quand la matrice de covariance est (presque) **diagonale**.
- Le calcul se fait aussi variable par variable : $s_{12} = \frac{1}{3}\big[(-4)(-2) + (-1)(-2) + (2)(4) + (3)(0)\big] = \frac{18}{3} = 6$, et la corrélation correspondante vaut $r_{12} = \dfrac{s_{12}}{\sqrt{s_{11}\,s_{22}}} = \dfrac{6}{\sqrt{80}} \approx 0{,}67$ ([[Covariance et corrélation]]). [[Complément hors du cours|ⓘ]]
- Pour cet exemple, les valeurs propres de $S$ (calcul numérique) sont environ $34{,}55$, $13{,}84$ et $1{,}61$ ; leur somme vaut bien la trace, 50. PC1 explique donc environ 69 % de la variance, PC2 28 % et PC3 3 % : un plan (PC1, PC2) garde environ 97 % de l'information. [[Complément hors du cours|ⓘ]]

## But de l'ACP (formulation algébrique)

On suppose la matrice $[\mathbf{X}_1 \cdots \mathbf{X}_N]$ déjà centrée (*mean-deviation form*). Le but de l'ACP est de trouver une **matrice orthogonale** $P = [\mathbf{u}_1 \cdots \mathbf{u}_p]$ ($p \times p$, [[Matrice orthogonale]]) qui définit un [[Changement de base|changement de variable]] $\mathbf{X} = P\mathbf{Y}$ :

$$\begin{bmatrix} x_1 \\ \vdots \\ x_p \end{bmatrix} = [\mathbf{u}_1 \ \cdots \ \mathbf{u}_p] \begin{bmatrix} y_1 \\ \vdots \\ y_p \end{bmatrix}$$

telle que les nouvelles variables $y_1, \ldots, y_p$ soient **non corrélées** et rangées par **variance décroissante**.

Chaque vecteur d'observation $\mathbf{X}_k$ reçoit un « nouveau nom » $\mathbf{Y}_k$ tel que $\mathbf{X}_k = P\mathbf{Y}_k$ : $\mathbf{Y}_k$ est le vecteur de coordonnées de $\mathbf{X}_k$ dans la base des colonnes de $P$, et

$$\mathbf{Y}_k = P^{-1}\mathbf{X}_k = P^T\mathbf{X}_k, \quad k = 1, \ldots, N$$

$P^{-1} = P^T$ parce que $P$ est orthogonale : ses colonnes sont orthonormées, donc $P^TP = I$. [[Complément hors du cours|ⓘ]]

Pourquoi une telle $P$ existe, et comment la trouver : la matrice de covariance des nouvelles variables est $P^TSP$. Comme $S$ est symétrique, le [[Théorème spectral]] fournit une matrice orthogonale $P$ dont les colonnes sont des vecteurs propres unitaires de $S$ et telle que $P^TSP = D$, diagonale, avec les valeurs propres $\lambda_1 \geq \dots \geq \lambda_p$ sur la diagonale ([[Théorème des axes principaux]]). Les $y_i$ sont alors non corrélées (coefficients hors diagonale nuls), de variances $\lambda_1, \dots, \lambda_p$ décroissantes : les colonnes $\mathbf{u}_1, \dots, \mathbf{u}_p$ de $P$ sont les composantes principales, et $y_1 = \mathbf{u}_1^T\mathbf{X}$ est le score sur PC1. [[Complément hors du cours|ⓘ]]

## Limites de l'ACP

- L'ACP ne capte que des relations **linéaires** : un nuage en forme de cercle ou de courbe est mal résumé par des droites ; des méthodes non linéaires (ACP à noyau, t-SNE, UMAP) servent alors à la visualisation. [[Complément hors du cours|ⓘ]]
- Elle est sensible aux **valeurs aberrantes**, qui gonflent la variance dans leur direction et peuvent capter une composante à elles seules ([[Quartiles et valeurs aberrantes]]). [[Complément hors du cours|ⓘ]]
- Les composantes sont des mélanges de toutes les variables : elles sont souvent difficiles à **interpréter**, d'où l'usage des loadings, du biplot et du [[Cercle des corrélations|cercle des corrélations]]. [[Complément hors du cours|ⓘ]]
- Une forte variance n'est pas forcément une information utile : pour prédire une variable cible, la composante la plus variable n'est pas forcément la plus prédictive. [[Complément hors du cours|ⓘ]]
- Elle s'applique à des variables **quantitatives** ; pour des variables qualitatives, on utilise l'analyse des correspondances (AFC pour deux variables, ACM pour plusieurs), méthodes très développées dans l'école française d'analyse des données. [[Complément hors du cours|ⓘ]]
