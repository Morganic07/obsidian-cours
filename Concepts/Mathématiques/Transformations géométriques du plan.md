---
type: concept
tags:
  - year2
aliases:
  - reflection
  - reflections
  - shear
  - shears
  - cisaillement
  - contraction and expansion
  - contraction et dilatation
  - projection onto the x1-axis
  - rotation du plan
  - matrice de rotation
  - rotation matrix
matieres:
  - Bilinear Algebra
sources:
  - "[[0 - Linear combination|Chp 0a - Linear combination]]"
  - "[[Raw/Year 2/Bilinear Algebra/Chp 0a - Linear combination .docx|Chp 0a - Linear combination]]"
maj: 2026-11-08
---

Le cours présente en tableaux (transformation, image du carré unité, matrice standard) les transformations linéaires usuelles du plan :

- **réflexions** (reflections) par rapport aux axes, à la droite $x_2=x_1$ (matrice $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$, symétrie orthogonale d'axe $x_1 = x_2$), à la droite $x_2=-x_1$ (matrice $\begin{bmatrix} 0 & -1 \\ -1 & 0 \end{bmatrix}$, symétrie orthogonale d'axe $x_2 = -x_1$), à l'origine ; [[Erreurs du cours#^e-transformations-geometriques-du-plan|✎]]
- **contractions et dilatations** (contraction and expansion) horizontales et verticales, avec $0<k<1$ ou $k>1$ ;
- **cisaillements** (shears) ;
- **projections** sur les axes.

## Rotation et méthode générale (complément, hors du cours)

**Méthode.** Les colonnes de la matrice standard sont les images des vecteurs $\mathbf{e}_1 = (1, 0)$ et $\mathbf{e}_2 = (0, 1)$ : $A = [\,T(\mathbf{e}_1)\ \ T(\mathbf{e}_2)\,]$ ([[Matrice d'une application linéaire]]). Il suffit donc de regarder où va le carré unité.

**Rotation d'angle $\theta$** autour de l'origine, dans le sens trigonométrique : elle envoie $\mathbf{e}_1$ sur $(\cos\theta, \sin\theta)$ et $\mathbf{e}_2$ sur $(-\sin\theta, \cos\theta)$, d'où
$$R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}.$$
Pour $\theta = 90°$, $R_\theta = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ ; pour $\theta = 180°$, $R_\theta = -I$, ce qui redonne la symétrie de centre $O$ (« réflexion par rapport à l'origine » du tableau). $R_\theta$ est une [[Matrice orthogonale|matrice orthogonale]] de déterminant 1 : elle conserve longueurs, angles, aires et orientation.

**Composition.** Appliquer $T_A$ puis $T_B$ donne $T_B(T_A(\mathbf{x})) = BA\,\mathbf{x}$ : la matrice de la composée est $BA$, dans cet ordre (la transformation appliquée en premier est à droite). Par exemple $R_\alpha R_\beta = R_{\alpha + \beta}$.

**Valeurs propres.** Une rotation d'angle $\theta \neq 0°, 180°$ (modulo $360°$) n'a aucune [[Valeur propre|valeur propre]] réelle : aucune direction n'est conservée. Son polynôme caractéristique $\lambda^2 - 2\cos\theta\,\lambda + 1$ a pour racines complexes $e^{\pm i\theta}$.

Notion parente : [[Transformation linéaire]]. Voir aussi : [[Projection orthogonale]], [[Matrice d'une application linéaire]], [[Produit matriciel]], [[Déterminant]], [[Matrice orthogonale]].

Résumés : [[0 - Linear combination]]
