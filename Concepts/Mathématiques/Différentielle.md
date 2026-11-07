---
type: concept
tags: [year2]
aliases: [différentiable, différentiables, différentiabilité, application différentiable, différentiabilité sur R2]
matieres: [Analyse dans Rn]
sources: ["[[Chp 4 - Calcul différentiel du premier ordre (résumé)|Chp 4 - Calcul différentiel du premier ordre]]"]
maj: 2026-11-06
---

$f$ est différentiable en $a$ s'il existe une [[Transformation linéaire|application linéaire]] $l$ et une application $\epsilon$ de limite nulle en 0 telles que :

$$f(a + h) = f(a) + l(h) + \|h\|\,\epsilon(h)$$

C'est le développement limité à l'ordre 1. $l$ est unique : c'est la différentielle de $f$ en $a$, notée $D_af$. Elle vaut $D_af(h) = \sum_j h_j \left.\frac{\partial f}{\partial x_j}\right|_a$.

- Une application linéaire $\phi$ est différentiable, et $D_a\phi = \phi$.
- Différentiable en $a$ implique continue en $a$, et dérivées partielles définies en $a$. Réciproquement, $\mathcal{C}^1$ implique différentiable.
- Dans $\mathbb{R}^2$ (théorème 2), $f$ est différentiable en $(x, y)$ si et seulement si $\frac{1}{\|h\|}\left(f(x + h_1, y + h_2) - f(x, y) - h_1\frac{\partial f}{\partial x} - h_2\frac{\partial f}{\partial y}\right)$ tend vers 0, quelle que soit la norme choisie.

> [!warning] Écart dans le cours
> [[Chp 4 - Calcul différentiel du premier ordre (résumé)|Chp 4 - Calcul différentiel du premier ordre]] dit qu'une fonction seulement différentiable a des dérivées « définies mais pas continues ». Il faut lire « pas forcément continues » (complément).

Liens : [[Dérivée partielle]], [[Fonction de classe Ck]], [[Matrice jacobienne]], [[Gradient]], [[Limite et continuité]], [[Développement limité]], [[Dérivabilité]]

Résumé : [[Chp 4 - Calcul différentiel du premier ordre (résumé)]]
