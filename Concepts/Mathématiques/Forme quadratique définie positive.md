---
type: concept
tags: [year2]
aliases: [positive definite, negative definite, indefinite, positive semidefinite, définie positive, définie négative, indéfinie, semi-définie positive, positive definite matrix, semi-définie négative, negative semidefinite, critère de Sylvester, Sylvester's criterion, décomposition de Cholesky, Cholesky decomposition]
matieres: [Bilinear Algebra]
sources: ["[[2 - Symmetric matrices and quadratic forms|Chp2 - Symmetric matrices and quadratic forms]]"]
maj: 2026-11-08
---

Une forme quadratique $Q$ est :

- **définie positive** si $Q(\mathbf{x})>0$ pour tout $\mathbf{x}\ne\mathbf{0}$ ;
- **définie négative** si $Q(\mathbf{x})<0$ pour tout $\mathbf{x}\ne\mathbf{0}$ ; [[Erreurs du cours#^e-forme-quadratique-definie-positive|✎]]
- **indéfinie** si elle prend des valeurs des deux signes (surface en selle).

**Théorème** : $Q(\mathbf{x})=\mathbf{x}^TA\mathbf{x}$ est définie positive ssi toutes les valeurs propres de $A$ sont positives, définie négative ssi elles sont toutes négatives, indéfinie ssi $A$ a des valeurs propres des deux signes.

Une matrice est définie positive si sa forme quadratique l'est ; semi-définie positive se définit de même.

## Compléments (hors du cours)

- **Cas semi-défini** : $Q$ est semi-définie positive ($Q(\mathbf{x}) \ge 0$ pour tout $\mathbf{x}$) ssi toutes les valeurs propres de $A$ sont $\ge 0$, et semi-définie négative ($Q(\mathbf{x}) \le 0$) ssi elles sont toutes $\le 0$.
- **Dimension 2** : pour $A = \begin{pmatrix} a & b \\ b & c \end{pmatrix}$, on a $\det A = \lambda_1\lambda_2$ et $\text{tr}\,A = a + c = \lambda_1 + \lambda_2$, d'où :
  - $\det A > 0$ et $a > 0$ : définie positive ;
  - $\det A > 0$ et $a < 0$ : définie négative ;
  - $\det A < 0$ : indéfinie ;
  - $\det A = 0$ : semi-définie (une valeur propre nulle).
- **Critère de Sylvester** : soit $\Delta_k$ le déterminant de la sous-matrice formée des $k$ premières lignes et colonnes de $A$ (mineurs principaux dominants). $A$ est définie positive ssi $\Delta_k > 0$ pour tout $k = 1, \dots, n$ ; définie négative ssi $(-1)^k\Delta_k > 0$ pour tout $k$ (signes alternés, $\Delta_1 < 0$).
- **Matrice $A^TA$** : pour toute matrice $A$, $A^TA$ est semi-définie positive, car $\mathbf{x}^TA^TA\mathbf{x} = \|A\mathbf{x}\|^2 \ge 0$ ; elle est définie positive ssi les colonnes de $A$ sont indépendantes (alors $A\mathbf{x} \ne \mathbf{0}$ pour $\mathbf{x} \ne \mathbf{0}$). C'est ce qui justifie les [[Moindres carrés|équations normales]] et les valeurs singulières $\sigma_i = \sqrt{\lambda_i}$ ([[Décomposition en valeurs singulières]]).
- **Décomposition de Cholesky** : toute matrice symétrique définie positive s'écrit de façon unique $A = R^TR$, avec $R$ [[Matrice triangulaire|triangulaire]] supérieure à diagonale strictement positive. Réciproquement, une telle écriture rend $A$ définie positive.
- **Usage en analyse** : en un point critique d'une fonction de plusieurs variables, la matrice hessienne (dérivées secondes, symétrique) décide de la nature du point : définie positive, minimum local ; définie négative, maximum local ; indéfinie, point selle. En dimension 2, c'est le critère $f_{xx}f_{yy} - f_{xy}^2 > 0$ et $f_{xx} > 0$ utilisé dans [[10 - linear regression]] ([[Moindres carrés]]).

Notion parente : [[Forme quadratique]]. Voir aussi : [[Valeur propre]], [[Matrice symétrique]], [[Matrice triangulaire]], [[Moindres carrés]], [[Décomposition en valeurs singulières]], [[Optimisation sous contrainte]].
Résumés : [[2 - Symmetric matrices and quadratic forms]]
