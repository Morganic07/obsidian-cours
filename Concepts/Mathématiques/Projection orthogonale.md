---
type: concept
tags: [year2, year3]
aliases: [orthogonal projection, orthogonal projections, projections orthogonales, projeté orthogonal, projeté orthogonalement, Orthogonal Decomposition Theorem, théorème de décomposition orthogonale, best approximation, meilleure approximation]
sources: ["[[1 - Orthogonality|chp 1 - Orthogonality]]", "[[2 - Symmetric matrices and quadratic forms|Chp2 - Symmetric matrices and quadratic forms]]", "[[13 - Principal Components Analysis|Cours 13 - Principal Components Analysis]]"]
maj: 2026-11-08
---

Tout $\mathbf{y}$ de $\mathbb{R}^n$ s'écrit de façon unique $\mathbf{y} = \hat{\mathbf{y}} + \mathbf{z}$, avec $\hat{\mathbf{y}}$ dans le sous-espace $W$ et $\mathbf{z}$ dans $W^\perp$. On note $\hat{\mathbf{y}} = \text{proj}_W\,\mathbf{y}$. C'est le **théorème de décomposition orthogonale** (Orthogonal Decomposition Theorem) ; $\hat{\mathbf{y}}$ ne dépend que de $W$.

- **Sur un vecteur** $\mathbf{u} \neq \mathbf{0}$ : $\hat{\mathbf{y}} = \frac{\mathbf{y} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}}\mathbf{u}$. Le résultat ne change pas si l'on remplace $\mathbf{u}$ par $c\mathbf{u}$, car il ne dépend que de la droite engendrée.
- **Sur un sous-espace** de base orthogonale $\{\mathbf{u}_1, \dots, \mathbf{u}_p\}$ : $\hat{\mathbf{y}} = \frac{\mathbf{y} \cdot \mathbf{u}_1}{\mathbf{u}_1 \cdot \mathbf{u}_1}\mathbf{u}_1 + \dots + \frac{\mathbf{y} \cdot \mathbf{u}_p}{\mathbf{u}_p \cdot \mathbf{u}_p}\mathbf{u}_p$. Le résultat ne dépend que de $W$, pas de la base choisie.
- **Sur un sous-espace de base orthonormale** : $\text{proj}_W\,\mathbf{y} = (\mathbf{y} \cdot \mathbf{u}_1)\mathbf{u}_1 + \dots + (\mathbf{y} \cdot \mathbf{u}_p)\mathbf{u}_p = UU^T\mathbf{y}$, avec $U = [\mathbf{u}_1 \cdots \mathbf{u}_p]$.
- **Meilleure approximation** (théorème de meilleure approximation, best approximation) : $\hat{\mathbf{y}}$ est le point de $W$ le plus proche de $\mathbf{y}$, soit $\|\mathbf{y} - \hat{\mathbf{y}}\| < \|\mathbf{y} - \mathbf{v}\|$ pour tout $\mathbf{v}$ de $W$ différent de $\hat{\mathbf{y}}$.
- **Si $\mathbf{y}$ est déjà dans $W$** : $\text{proj}_W\,\mathbf{y} = \mathbf{y}$.
- **Matrice de projection** : pour un $\mathbf{u}_j$ d'une décomposition spectrale, $(\mathbf{u}_j\mathbf{u}_j^T)\mathbf{x}$ est la projection de $\mathbf{x}$ sur la droite engendrée par $\mathbf{u}_j$.

**En ACP** (Data analysis) : chaque point est projeté orthogonalement sur la composante, d'où $\|a_i\|^2 = \|w_ic\|^2 + \|a_i - w_ic\|^2$ (variance initiale = variance restante + variance perdue).

## Compléments (hors du cours)

**D'où vient le coefficient** : on cherche $\hat{\mathbf{y}} = \alpha\mathbf{u}$ tel que $\mathbf{z} = \mathbf{y} - \alpha\mathbf{u}$ soit orthogonal à $\mathbf{u}$. La condition $(\mathbf{y} - \alpha\mathbf{u})\cdot\mathbf{u} = 0$ donne $\mathbf{y}\cdot\mathbf{u} - \alpha\,\mathbf{u}\cdot\mathbf{u} = 0$, d'où $\alpha = \dfrac{\mathbf{y}\cdot\mathbf{u}}{\mathbf{u}\cdot\mathbf{u}}$.

Exemple : $\mathbf{y} = (7,6)$, $\mathbf{u} = (4,2)$. On a $\mathbf{y}\cdot\mathbf{u} = 40$ et $\mathbf{u}\cdot\mathbf{u} = 20$, donc $\hat{\mathbf{y}} = 2\mathbf{u} = (8,4)$ et $\mathbf{z} = (-1,2)$, avec bien $\mathbf{z}\cdot\mathbf{u} = -4 + 4 = 0$. La distance de $\mathbf{y}$ à la droite engendrée par $\mathbf{u}$ vaut $\|\mathbf{z}\| = \sqrt{5}$.

**Matrice de projection** $P = UU^T$ ($U$ à colonnes orthonormées engendrant $W$) : elle vérifie $P^2 = P$ (projeter deux fois revient à projeter une fois, car $U^TU = I$) et $P^T = P$. Réciproquement, toute matrice symétrique telle que $P^2 = P$ est la matrice d'une projection orthogonale (sur son espace des colonnes). $I - P$ est la projection orthogonale sur $W^\perp$ : $\mathbf{z} = (I - P)\mathbf{y}$.

**Preuve de la meilleure approximation** : pour $\mathbf{v} \in W$, on écrit $\mathbf{y} - \mathbf{v} = (\mathbf{y} - \hat{\mathbf{y}}) + (\hat{\mathbf{y}} - \mathbf{v})$. Le premier terme est dans $W^\perp$, le second dans $W$ ; ils sont orthogonaux, donc par le [[Théorème de Pythagore]] :
$$\|\mathbf{y} - \mathbf{v}\|^2 = \|\mathbf{y} - \hat{\mathbf{y}}\|^2 + \|\hat{\mathbf{y}} - \mathbf{v}\|^2,$$
qui est strictement supérieur à $\|\mathbf{y} - \hat{\mathbf{y}}\|^2$ dès que $\mathbf{v} \neq \hat{\mathbf{y}}$. La distance de $\mathbf{y}$ à $W$ vaut donc $\|\mathbf{z}\| = \|\mathbf{y} - \hat{\mathbf{y}}\|$.

Notion parente : [[Complément orthogonal]]. Liens : [[Orthogonalité]], [[Théorème de Pythagore]], [[Matrice orthogonale]], [[Famille orthogonale]], [[Procédé de Gram-Schmidt]], [[Moindres carrés]], [[Matrice symétrique]], [[Décomposition spectrale]], [[Analyse en composantes principales]] (projection des données sur les composantes)

Résumés : [[1 - Orthogonality]], [[2 - Symmetric matrices and quadratic forms]], [[13 - Principal Components Analysis]]
