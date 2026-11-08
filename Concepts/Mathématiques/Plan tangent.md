---
type: concept
tags: [year2]
aliases: [plans tangents, plan tangent à une surface, tangent plane]
sources: ["[[Raw/Year 2/Analyse dans Rn/Chp 4 : Calcul différentiel du premier ordre.docx|Chp 4 - Calcul différentiel du premier ordre]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : si $f : U \subset \mathbb{R}^2 \to \mathbb{R}$ est [[Différentielle|différentiable]] en $(x_0, y_0)$, la surface d'équation $z = f(x, y)$ admet au point $(x_0, y_0, f(x_0, y_0))$ le plan tangent
$$z = f(x_0, y_0) + \frac{\partial f}{\partial x}(x_0, y_0)\,(x - x_0) + \frac{\partial f}{\partial y}(x_0, y_0)\,(y - y_0).$$

- C'est l'analogue, en deux variables, de la [[Tangente à une courbe|tangente]] $y = f(a) + f'(a)(x - a)$.
- La différentiabilité dit exactement que la surface est approchée par ce plan à $o(\|h\|)$ près : $f(x_0 + h_1, y_0 + h_2) = f(x_0, y_0) + D_{(x_0, y_0)} f(h) + o(\|h\|)$, et le plan est le graphe de cette approximation affine.
- Un vecteur normal au plan est $\left(\dfrac{\partial f}{\partial x}(x_0, y_0),\ \dfrac{\partial f}{\partial y}(x_0, y_0),\ -1\right)$ ; sa projection sur le plan $(x, y)$ est le [[Gradient|gradient]].

**Exemple** : $f(x, y) = x^2 y$ en $(1, 2)$. $f(1, 2) = 2$, $\partial f/\partial x = 2xy = 4$, $\partial f/\partial y = x^2 = 1$, d'où le plan tangent $z = 2 + 4(x - 1) + (y - 2)$, soit $z = 4x + y - 4$.

## Dans le cours

Le cours ne le nomme pas. Il apparaît dans les compléments de [[4 - Calcul différentiel du premier ordre]], comme interprétation géométrique de la différentielle.

Voir aussi : [[Différentielle]], [[Tangente à une courbe]], [[Gradient]], [[Dérivée partielle]].

Résumés : [[4 - Calcul différentiel du premier ordre]]
