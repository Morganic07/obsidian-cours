---
type: concept
tags: [year2]
aliases: [dérivées partielles, partial derivative, partial derivatives, Schwarz, dérivées croisées, dérivée seconde partielle, "dérivées d'ordre 2"]
matieres: [Analyse dans Rn, Analyse Maths, Analyse]
sources: ["[[Chp 4 - Calcul différentiel du premier ordre]]", "[[Chp 5 - Calcul différentiel d'ordre supérieur]]"]
maj: 2026-11-06
---

Dérivée de $f$ selon une seule variable, les autres étant fixées :

$$\left.\frac{\partial f}{\partial x_j}\right|_a = \lim_{t \to 0} \frac{f(a + te_j) - f(a)}{t}$$

Pour une application vectorielle, elle se calcule composante par composante. Avoir toutes ses dérivées partielles en un point n'implique pas d'y être continue, car elles ne regardent que les directions des axes.

**Dérivation en chaîne** : $g(t) = f(u_1(t), \dots, u_n(t))$ a pour dérivée $g'(t) = \sum_i u_i'(t)\frac{\partial f}{\partial x_i}$. De même, pour $h(u, v) = f(g_1(u, v), g_2(u, v))$ : $\frac{\partial h}{\partial u} = \frac{\partial f}{\partial x}\frac{\partial g_1}{\partial u} + \frac{\partial f}{\partial y}\frac{\partial g_2}{\partial u}$.

**Ordre 2** : $\frac{\partial^2 f}{\partial x^2}$, $\frac{\partial^2 f}{\partial y^2}$ et les deux dérivées croisées, avec $\frac{\partial^2 f}{\partial y \partial x} = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)$.

**[[Théorème de Schwarz]]** : si les dérivées croisées sont définies et continues en $a$, alors $\frac{\partial^2 f}{\partial x_j \partial x_i} = \frac{\partial^2 f}{\partial x_i \partial x_j}$ en $a$. Être $\mathcal{C}^2$ suffit, mais n'est pas nécessaire.

Notion parente : [[Différentielle]]. Voir aussi : [[Théorème de Schwarz]], [[Gradient]], [[Fonction de classe Ck]], [[Matrice jacobienne]], [[Équation aux dérivées partielles]]

## À vérifier

- Définition 1 du Chp 4 : $a \in \mathbb{R}^p$ au lieu de $a \in U$ (résumé Chp 4, point 5).

Résumés : [[Chp 4 - Calcul différentiel du premier ordre (résumé)]], [[Chp 5 - Calcul différentiel d'ordre supérieur (résumé)]], [[Chp9-intégrales multiples (résumé)]]
