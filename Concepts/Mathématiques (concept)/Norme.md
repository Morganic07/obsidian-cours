---
type: concept
tags: [year2]
aliases: [norm, norms, normes, espace vectoriel normé, espaces vectoriels normés, EVN, norme euclidienne, normes équivalentes, norme 1, norme infinie, norme de Manhattan, absolue homogénéité, équivalence des normes, length of a vector, longueur d'un vecteur]
matieres: [Bilinear Algebra, Algèbre Linéaire, Analyse dans Rn]
sources: ["[[1 - Orthogonality (résumé)|chp 1 - Orthogonality]]", "[[2 - éléments de topologie dans Rn (résumé)|Chp 2 - éléments de topologie dans Rn]]"]
maj: 2026-11-06
---

Application qui mesure la taille d'un vecteur. Un espace vectoriel muni d'une norme est un espace vectoriel normé (EVN). Elle vérifie trois propriétés :

- **Séparation** : $\|x\| = 0 \Rightarrow x = 0_E$.
- **Absolue homogénéité** : $\|\lambda x\| = |\lambda|\,\|x\|$.
- **Inégalité triangulaire** : $\|x + y\| \le \|x\| + \|y\|$, et aussi $\|x - y\| \ge |\,\|x\| - \|y\|\,|$.

Une norme est toujours positive. Sur $\mathbb{R}^n$, le cours en donne trois :

- $\|x\|_1 = \sum |x_i|$, dite de Manhattan : la longueur en suivant un quadrillage.
- $\|x\|_2 = \sqrt{\sum x_i^2}$, dite euclidienne : la longueur à vol d'oiseau. C'est celle du [[Produit scalaire]], $\|\mathbf{v}\| = \sqrt{\mathbf{v} \cdot \mathbf{v}}$.
- $\|x\|_\infty = \max |x_i|$.

Sur $\mathbb{R}$, ces trois normes valent $|x|$. Un vecteur de norme 1 est un unit vector ([[Vecteur unitaire]]). En Bilinear Algebra, la norme (length) vérifie $\|c\mathbf{v}\| = |c|\,\|\mathbf{v}\|$.

**Normes équivalentes** : il existe $\alpha, \beta > 0$ tels que $\alpha\|x\|_a \le \|x\|_b \le \beta\|x\|_a$. En dimension finie, toutes les normes sont équivalentes. Voisinages, ouverts et limites n'y dépendent donc pas de la norme.

**[[Distance]]** : une norme donne une distance $d(X, Y) = \|X - Y\|$. Une distance en général est symétrique, nulle seulement entre points égaux, et vérifie l'inégalité triangulaire.

> [!warning] Écart dans le cours
> [[2 - éléments de topologie dans Rn (résumé)|Chp 2 - éléments de topologie dans Rn]] donne le cas d'égalité $\|x + y\| = \|x\| + \|y\| \iff x = \lambda y$ avec $\lambda \in \mathbb{R}$. Il faut $\lambda \ge 0$ (complément).

Liens : [[Produit scalaire]], [[Orthogonalité]], [[Boule et voisinage]], [[Limite et continuité]], [[Espace vectoriel]], [[Distance]], [[Inégalité triangulaire]], [[Vecteur unitaire]]

Résumés : [[1 - Orthogonality (résumé)]], [[2 - éléments de topologie dans Rn (résumé)]]
