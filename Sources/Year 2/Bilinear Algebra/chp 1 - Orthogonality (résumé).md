---
type: source
sources: ["[[chp 1 - Orthogonality]]"]
maj: 2026-11-05
---

Résumé de [[chp 1 - Orthogonality]], dans [[Year 2 - Bilinear Algebra]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Le chapitre part du [[Produit scalaire]] pour mesurer longueurs, distances et angles droits. Il en tire un outil central, la [[Projection orthogonale]], puis trois applications : le [[Procédé de Gram-Schmidt]], la [[Factorisation QR]] et les [[Moindres carrés]], qui mènent à la [[Régression linéaire]].

## Contenu, dans l'ordre du cours

- **[[Produit scalaire]]** : $\mathbf{x} \cdot \mathbf{y} = x_1y_1 + \dots + x_ny_n = \mathbf{x}^T\mathbf{y} = \|\mathbf{x}\|\,\|\mathbf{y}\|\cos\theta$. Un dot product est un inner product, mais la réciproque est fausse.
- **[[Norme]] et distance** : $\|\mathbf{v}\| = \sqrt{\mathbf{v} \cdot \mathbf{v}}$, $\|c\mathbf{v}\| = |c|\,\|\mathbf{v}\|$ et $\text{dist}(\mathbf{u}, \mathbf{v}) = \|\mathbf{u} - \mathbf{v}\|$. Un vecteur de norme 1 est un unit vector.
- **[[Orthogonalité]]** : $\mathbf{u} \cdot \mathbf{v} = 0$, équivalent à Pythagore (Theorem 2).
- **[[Complément orthogonal]]** : $W^\perp$ est un sous-espace. Theorem 3 : $(\text{Row } A)^\perp = \text{Nul } A$ et $(\text{Col } A)^\perp = \text{Nul } A^T$. Le cours l'illustre avec $A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$ : Nul $A$ est la droite de $(1, -2, 1)$, perpendiculaire au plan Row $A$, et Nul $A^T = \{\mathbf{0}\}$.
- **[[Famille orthogonale]]** : des vecteurs non nuls deux à deux orthogonaux sont indépendants. Dans une base orthogonale, les coefficients se calculent directement : $c_j = \frac{\mathbf{y} \cdot \mathbf{u}_j}{\mathbf{u}_j \cdot \mathbf{u}_j}$. Une matrice $U$ a des colonnes orthonormales si et seulement si $U^TU = I$, et elle préserve alors longueurs et orthogonalité.
- **[[Projection orthogonale]]** : $\mathbf{y} = \hat{\mathbf{y}} + \mathbf{z}$, décomposition unique avec $\hat{\mathbf{y}}$ dans $W$ et $\mathbf{z}$ dans $W^\perp$. $\hat{\mathbf{y}}$ ne dépend que de $W$, et c'est le point de $W$ le plus proche de $\mathbf{y}$. Avec une base orthonormale, $\text{proj}_W\,\mathbf{y} = UU^T\mathbf{y}$.
- **[[Matrice orthogonale]]** : carrée, à colonnes orthonormales, avec $U^{-1} = U^T$.
- **[[Procédé de Gram-Schmidt]]** : une base devient une base orthogonale, en retirant à chaque vecteur ses projections sur les précédents.
- **[[Factorisation QR]]** : Gram-Schmidt avec normalisation revient à écrire $A = QR$.
- **[[Moindres carrés]]** : quand $A\mathbf{x} = \mathbf{b}$ n'a pas de solution, on minimise $\|\mathbf{b} - A\mathbf{x}\|$, ce qui mène aux équations normales $A^TA\mathbf{x} = A^T\mathbf{b}$.
- **[[Régression linéaire]]** : $X\boldsymbol{\beta} = \mathbf{y}$ est le même problème avec d'autres notations.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Ces remarques comparent son texte à ses images, ou à son propre raisonnement.

1. **Projeté de $\mathbf{b}$** : le texte dit que $\hat{\mathbf{x}}$ est le projeté orthogonal de $\mathbf{b}$ sur Col $A$. La figure du cours montre que c'est $A\hat{\mathbf{x}}$. D'ailleurs, $\hat{\mathbf{x}}$ est dans $\mathbb{R}^n$, alors que Col $A$ est dans $\mathbb{R}^m$. Le wiki suit la figure.
2. **Normalisation** : l'image donne $\frac{1}{\|\mathbf{v}\|}\|\mathbf{v}\|$ et le texte écrit $\mathbf{u} = x\mathbf{v}$. Telle quelle, cette expression vaut 1, donc $\mathbf{u} = \mathbf{v}$. Le coefficient attendu est $\frac{1}{\|\mathbf{v}\|}$ (complément, le cours ne le dit pas sous cette forme). Le texte exact de l'image reste à interpréter.
3. **Application to linear models** : « determine β1 and β1 » doit se lire β0 et β1.
4. **Distance minimale** : « the smallest distance is $\|\mathbf{b} - A\mathbf{x}\|$ » ne vaut que pour $\mathbf{x} = \hat{\mathbf{x}}$, comme le dit plus loin le cours avec la least-square error.
5. **Figure QR** : sa légende dit « upper diagonal matrix », alors que le théorème et le contenu de la figure indiquent une matrice triangulaire supérieure.
