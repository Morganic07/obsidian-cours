---
type: concept
tags: [year2, year3]
aliases: [least-squares, least squares, least square, moindre carré, normal equations, équations normales, least-squares solution, least-squares error, least square problem]
sources: ["[[1 - Orthogonality|chp 1 - Orthogonality]]", "[[10 - linear regression|Cours 10 - linear regression]]", "[[13 - Principal Components Analysis|Cours 13 - Principal Components Analysis]]"]
maj: 2026-11-08
---

Quand $A\mathbf{x} = \mathbf{b}$ n'a pas de solution, on cherche un $\hat{\mathbf{x}}$ qui minimise $\|\mathbf{b} - A\mathbf{x}\|$. Ce minimum $\|\mathbf{b} - A\hat{\mathbf{x}}\|$ est la least-square error. Comme $A\mathbf{x}$ est toujours dans Col $A$, le meilleur choix est le [[Projection orthogonale|projeté orthogonal]] de $\mathbf{b}$ sur Col $A$, c'est-à-dire $A\hat{\mathbf{x}}$ (et non $\hat{\mathbf{x}}$, qui est dans $\mathbb{R}^n$). [[Erreurs du cours#^e-moindres-carres|✎]]

Les solutions sont celles des équations normales $A^TA\mathbf{x} = A^T\mathbf{b}$. La solution est unique pour tout $\mathbf{b}$ si et seulement si les colonnes de $A$ sont indépendantes, ou de façon équivalente si $A^TA$ est inversible. Alors $\hat{\mathbf{x}} = (A^TA)^{-1}A^T\mathbf{b}$.

**Origine des équations normales (complément, hors du cours)** : le résidu $\mathbf{b} - A\hat{\mathbf{x}}$ est orthogonal à Col $A$, donc il appartient à $(\text{Col } A)^\perp = \text{Nul } A^T$ ([[Sous-espaces fondamentaux]]). D'où $A^T(\mathbf{b} - A\hat{\mathbf{x}}) = \mathbf{0}$, soit $A^TA\hat{\mathbf{x}} = A^T\mathbf{b}$. Le nom vient de là : le résidu est « normal », c'est-à-dire perpendiculaire, à Col $A$.

**Via la [[Factorisation QR]] (complément, hors du cours)** : si $A = QR$ (colonnes indépendantes), alors $\hat{\mathbf{x}} = R^{-1}Q^T\mathbf{b}$, qu'on obtient en pratique en résolvant le système triangulaire $R\hat{\mathbf{x}} = Q^T\mathbf{b}$. C'est la méthode préférée numériquement, car former $A^TA$ élève au carré le [[Conditionnement d'une matrice|conditionnement]]. Quand les colonnes sont dépendantes, la [[Pseudo-inverse]] donne la solution de plus petite norme, $\hat{\mathbf{x}} = A^+\mathbf{b}$.

**Régression linéaire simple (complément, hors du cours)** : pour ajuster $y = \beta_0 + \beta_1 x$ aux points $(x_j, y_j)$, la matrice $X$ a une colonne de 1 et une colonne des $x_j$, et l'on résout $X^TX\boldsymbol{\beta} = X^T\mathbf{y}$. On obtient
$$\hat\beta_1 = \frac{\sum_j (x_j - \bar x)(y_j - \bar y)}{\sum_j (x_j - \bar x)^2}, \qquad \hat\beta_0 = \bar y - \hat\beta_1 \bar x.$$
La droite passe donc par le point moyen $(\bar x, \bar y)$, et la somme des [[Résidu (régression)|résidus]] est nulle (c'est l'équation normale associée à la colonne de 1).

*Exemple* : pour les points $(0,0)$, $(1,1)$, $(2,1)$, on a $\bar x = 1$, $\bar y = \frac23$, $\sum (x_j - \bar x)(y_j - \bar y) = 1$ et $\sum (x_j - \bar x)^2 = 2$, d'où $\hat\beta_1 = \frac12$, $\hat\beta_0 = \frac16$ : la droite est $y = \frac16 + \frac{x}{2}$, avec les résidus $-\frac16$, $\frac13$, $-\frac16$ (de somme nulle).

Le même cadre couvre tout modèle **linéaire en $\boldsymbol{\beta}$** : régression multiple (une colonne par variable explicative), ajustement polynomial (colonnes $1, x, x^2, \dots$), etc. (complément, hors du cours).
**En Data analysis (Thanos)** : pour ajuster une droite, on minimise la somme des carrés des écarts $SSE = \sum (y_i - \hat y_i)^2$, car les écarts positifs et négatifs se compenseraient dans une simple somme. [[10 - linear regression|Cours 10 - linear regression]] le fait aussi par [[Dérivée partielle|dérivées partielles]] sur trois points (la condition $f_b = -10 + 6b + 12m = 0$ et son analogue en $m$ donnent la droite $y = x - \frac13$), [[Erreurs du cours#^e-moindres-carres|✎]] avec le critère de minimum $f_{bb}f_{mm} - f_{bm}^2 > 0$ et $f_{bb} > 0$. En [[Analyse en composantes principales|ACP]], maximiser la variance projetée équivaut à minimiser l'erreur des moindres carrés ([[13 - Principal Components Analysis|Cours 13 - Principal Components Analysis]]).

Notion parente : [[Projection orthogonale]]. Voir aussi : [[Orthogonalité]], [[Espace des colonnes]], [[Régression linéaire]], [[Analyse en composantes principales]], [[Dérivée partielle]], [[Factorisation QR]], [[Pseudo-inverse]], [[Résidu (régression)]]

Résumés : [[1 - Orthogonality]], [[10 - linear regression]] (méthode par dérivées partielles), [[11 - Multiple Linear Regression and F-statistic]], [[13 - Principal Components Analysis]]
