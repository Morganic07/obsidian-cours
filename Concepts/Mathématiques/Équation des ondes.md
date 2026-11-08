---
type: concept
tags: [year2]
aliases: [équation des cordes vibrantes, formule de d'Alembert, wave equation]
sources: ["[[Raw/Year 2/Analyse dans Rn/Chp 5 : Calcul différentiel d'ordre supérieur.docx|Chp 5 - Calcul différentiel d'ordre supérieur]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : l'équation des ondes à une dimension d'espace est l'[[Équation aux dérivées partielles|EDP]] d'ordre 2
$$\frac{\partial^2 f}{\partial t^2} = c^2\,\frac{\partial^2 f}{\partial x^2}, \qquad c > 0,$$
d'inconnue $f(x, t)$ de classe $\mathcal{C}^2$ sur $\mathbb{R}^2$. Elle décrit la propagation d'une onde à la vitesse $c$ : corde vibrante, son, ondes électromagnétiques.

**Résolution par changement de variables** :

1. Poser $u = x + ct$, $v = x - ct$. L'application $(x, t) \mapsto (u, v)$ est linéaire, de déterminant $\begin{vmatrix} 1 & c \\ 1 & -c \end{vmatrix} = -2c \ne 0$ : c'est un $\mathcal{C}^1$-[[Difféomorphisme|difféomorphisme]] de $\mathbb{R}^2$ sur $\mathbb{R}^2$.
2. Écrire $f(x, t) = g(u, v)$. La règle de la chaîne donne $\dfrac{\partial^2 f}{\partial x^2} = g_{uu} + 2g_{uv} + g_{vv}$ et $\dfrac{\partial^2 f}{\partial t^2} = c^2(g_{uu} - 2g_{uv} + g_{vv})$, en utilisant le [[Théorème de Schwarz]] ($g_{uv} = g_{vu}$).
3. L'équation devient $-4c^2\,\dfrac{\partial^2 g}{\partial u \partial v} = 0$, soit $\dfrac{\partial^2 g}{\partial u \partial v} = 0$, d'où $g(u, v) = G(u) + H(v)$ (théorème 5 du chapitre 5).
4. **Formule de d'Alembert** : les solutions $\mathcal{C}^2$ sont
$$f(x, t) = G(x + ct) + H(x - ct),$$
avec $G$, $H$ de classe $\mathcal{C}^2$ sur $\mathbb{R}$ : la somme de deux ondes qui se déplacent à la vitesse $c$, $G(x + ct)$ vers la gauche et $H(x - ct)$ vers la droite, sans se déformer.

## Dans le cours

Le cours ne la nomme pas. Elle apparaît dans les compléments de [[5 - Calcul différentiel d'ordre supérieur]], comme exemple type de la méthode de résolution d'une EDP d'ordre 2 par changement de variables.

Voir aussi : [[Équation aux dérivées partielles]], [[Difféomorphisme]], [[Théorème de Schwarz]], [[Dérivée partielle]].

Résumés : [[5 - Calcul différentiel d'ordre supérieur]]
