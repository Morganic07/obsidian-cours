---
type: concept
tags: [year2]
aliases: [équations aux dérivées partielles, EDP, EDPs, partial differential equation, système d'EDP, EDP d'ordre 1, EDP d'ordre 2]
matieres: [Analyse dans Rn, Analyse Maths, Analyse]
sources: ["[[4 - Calcul différentiel du premier ordre|Chp 4 - Calcul différentiel du premier ordre]]", "[[5 - Calcul différentiel d'ordre supérieur|Chp 5 - Calcul différentiel d'ordre supérieur]]"]
maj: 2026-11-06
---

Équation qui lie une fonction de plusieurs variables à ses dérivées partielles. La méthode vue cette année ramène l'équation à une forme connue par [[Difféomorphisme|changement de variables]].

**Solutions connues**, sur un ouvert de $\mathbb{R}^2$ :

- $\frac{\partial f}{\partial x} = g(x, y)$ donne $f = K(y) + \int g\,dx$, avec $K$ quelconque de classe $\mathcal{C}^1$ (théorème 8 du chapitre 4).
- $\frac{\partial^2 f}{\partial x^2} = 0$ donne $f = xG(y) + H(y)$.
- $\frac{\partial^2 f}{\partial x \partial y} = 0$ donne $f = G(x) + H(y)$.

**Système $\frac{\partial f}{\partial x} = g$ et $\frac{\partial f}{\partial y} = h$** :

1. Vérifier $\frac{\partial g}{\partial y} = \frac{\partial h}{\partial x}$, ce qui vient du théorème de Schwarz.
2. Intégrer une des équations, ce qui fait apparaître une fonction $K$ de l'autre variable.
3. Dériver selon l'autre variable, et injecter le résultat dans l'équation restante.
4. Résoudre l'équation obtenue sur $K$.
5. Écrire la solution.

Notion parente : [[Dérivée partielle]]. Voir aussi : [[Difféomorphisme]], [[Fonction de classe Ck]]

Résumés : [[4 - Calcul différentiel du premier ordre]], [[5 - Calcul différentiel d'ordre supérieur]]
