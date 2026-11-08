---
type: concept
tags: [year2]
aliases: [équations aux dérivées partielles, EDP, EDPs, partial differential equation, système d'EDP, EDP d'ordre 1, EDP d'ordre 2, équation de transport, équation de Laplace, équation de la chaleur, fonction harmonique]
matieres: [Analyse dans Rn, Analyse Maths, Analyse]
sources: ["[[4 - Calcul différentiel du premier ordre|Chp 4 - Calcul différentiel du premier ordre]]", "[[5 - Calcul différentiel d'ordre supérieur|Chp 5 - Calcul différentiel d'ordre supérieur]]", "[[Raw/Year 2/Analyse dans Rn/Chp 5 : Calcul différentiel d'ordre supérieur.docx|Chp 5 - Calcul différentiel d'ordre supérieur]]"]
maj: 2026-11-08
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

## Compléments (complément, hors du cours)

**Un exemple d'ordre 1 : l'équation de transport** $\frac{\partial f}{\partial x} + \frac{\partial f}{\partial y} = 0$ sur $\mathbb{R}^2$. On pose $(u, v) = (x, x - y)$ et $f(x, y) = F(u, v)$. Par la règle de dérivation des composées, $\frac{\partial f}{\partial x} = \frac{\partial F}{\partial u} + \frac{\partial F}{\partial v}$ et $\frac{\partial f}{\partial y} = -\frac{\partial F}{\partial v}$, donc l'équation devient $\frac{\partial F}{\partial u} = 0$, d'où $F(u, v) = K(v)$ et $f(x, y) = K(x - y)$, avec $K$ de classe $\mathcal{C}^1$. La solution est constante le long des droites $x - y = $ constante.

**Le système $\frac{\partial f}{\partial x} = g$, $\frac{\partial f}{\partial y} = h$** revient à chercher un **potentiel** du champ de vecteurs $(g, h)$, c'est-à-dire une fonction dont il est le [[Gradient]]. La condition de compatibilité $\frac{\partial g}{\partial y} = \frac{\partial h}{\partial x}$ est nécessaire ([[Théorème de Schwarz]]). Elle est suffisante sur un ouvert convexe (plus généralement étoilé) : c'est le théorème de Poincaré. Elle ne l'est pas sur $\mathbb{R}^2 \setminus \{0\}$ : le champ $(g, h) = \left(\frac{-y}{x^2 + y^2}, \frac{x}{x^2 + y^2}\right)$ vérifie la condition, mais n'a pas de potentiel sur cet ouvert (sa circulation le long du cercle unité vaut $2\pi$, alors que celle d'un gradient le long d'une courbe fermée est nulle).

**Trois exemples classiques d'ordre 2** :

- l'[[Équation des ondes]] $\frac{\partial^2 f}{\partial t^2} = c^2 \frac{\partial^2 f}{\partial x^2}$, dont les solutions sont $f(x, t) = G(x + ct) + H(x - ct)$ (formule de d'Alembert) ;
- l'équation de Laplace $\Delta f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} = 0$, dont les solutions sont les **fonctions harmoniques** (par exemple $x^2 - y^2$, ou les parties réelles des fonctions holomorphes) ;
- l'équation de la chaleur $\frac{\partial f}{\partial t} = D\,\frac{\partial^2 f}{\partial x^2}$, $D > 0$, qui décrit la diffusion de la température ou d'une concentration.

Notion parente : [[Dérivée partielle]]. Voir aussi : [[Difféomorphisme]], [[Fonction de classe Ck]], [[Théorème de Schwarz]], [[Gradient]], [[Équation des ondes]]

Résumés : [[4 - Calcul différentiel du premier ordre]], [[5 - Calcul différentiel d'ordre supérieur]]
