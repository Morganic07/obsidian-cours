---
type: concept
tags: [year2]
aliases: [norm, norms, normes, espace vectoriel normé, espaces vectoriels normés, EVN, norme euclidienne, normes équivalentes, norme 1, norme infinie, norme de Manhattan, absolue homogénéité, équivalence des normes, length of a vector, longueur d'un vecteur]
matieres: [Bilinear Algebra, Algèbre Linéaire, Analyse dans Rn]
sources: ["[[1 - Orthogonality|chp 1 - Orthogonality]]", "[[2 - éléments de topologie dans Rn|Chp 2 - éléments de topologie dans Rn]]"]
maj: 2026-11-08
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

**Constantes explicites sur $\mathbb{R}^n$ (complément, hors du cours)** :
$$\|x\|_\infty \le \|x\|_2 \le \|x\|_1 \le \sqrt{n}\,\|x\|_2 \le n\,\|x\|_\infty.$$
L'inégalité $\|x\|_1 \le \sqrt{n}\,\|x\|_2$ vient de l'[[Inégalité de Cauchy-Schwarz]] appliquée à $(|x_i|)$ et $(1, \dots, 1)$. Pour les boules unité de $\mathbb{R}^2$, cela se lit sur le dessin : la boule de $\|\cdot\|_1$ (un losange) est inscrite dans celle de $\|\cdot\|_2$ (le disque), elle-même inscrite dans celle de $\|\cdot\|_\infty$ (le carré).

**Inégalité triangulaire de $\|\cdot\|_2$ (inégalité de Minkowski, complément)** : elle découle de Cauchy-Schwarz,
$$\|x + y\|_2^2 = \|x\|_2^2 + 2\,x \cdot y + \|y\|_2^2 \le \|x\|_2^2 + 2\|x\|_2\|y\|_2 + \|y\|_2^2 = (\|x\|_2 + \|y\|_2)^2.$$

**En dimension infinie (complément)**, les normes ne sont plus toutes équivalentes. Sur $\mathcal{C}([0, 1])$, avec $\|f\|_\infty = \sup |f|$ et $\|f\|_1 = \int_0^1 |f|$, la suite $f_n(x) = x^n$ vérifie $\|f_n\|_\infty = 1$ et $\|f_n\|_1 = \frac{1}{n+1} \to 0$ : aucune constante $\beta$ ne donne $\|f\|_\infty \le \beta\|f\|_1$.

**Continuité de la norme (complément)** : la seconde inégalité triangulaire $|\,\|x\| - \|y\|\,| \le \|x - y\|$ dit que la norme est 1-[[Application lipschitzienne|lipschitzienne]], donc continue.

**[[Distance]]** : une norme donne une distance $d(X, Y) = \|X - Y\|$. Une distance en général est symétrique, nulle seulement entre points égaux, et vérifie l'inégalité triangulaire.

Toute distance ne vient pas d'une norme (complément) : une distance issue d'une norme vérifie $d(\lambda X, \lambda Y) = |\lambda|\,d(X, Y)$. La distance discrète ($d(X, Y) = 1$ si $X \ne Y$, $0$ sinon) donne $d(2X, 2Y) = 1 \ne 2 = 2\,d(X, Y)$ pour $X \ne Y$ : elle ne vient d'aucune norme.

**Cas d'égalité** ([[2 - éléments de topologie dans Rn|Chp 2]]) : pour la norme euclidienne, $\|x + y\| = \|x\| + \|y\| \iff y = 0$ ou $x = \lambda y$ avec $\lambda \ge 0$ ; pour $y = -x$ non nul, $\|x + y\| = 0 \neq 2\|x\|$. [[Erreurs du cours#^e-norme|✎]]

Liens : [[Produit scalaire]], [[Orthogonalité]], [[Boule et voisinage]], [[Limite et continuité]], [[Espace vectoriel]], [[Distance]], [[Inégalité triangulaire]], [[Vecteur unitaire]], [[Inégalité de Cauchy-Schwarz]], [[Application lipschitzienne]]

Résumés : [[1 - Orthogonality]], [[2 - éléments de topologie dans Rn]]
