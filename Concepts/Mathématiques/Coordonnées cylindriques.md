---
type: concept
tags: [year2]
aliases: [cylindrical coordinates, coords cylindriques, passage en cylindriques]
sources: ["[[Raw/Year 2/Analyse/Chp9-intégrales multiples.pdf|Chp9-intégrales multiples.pdf]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : coordonnées de $\mathbb{R}^3$ qui reprennent les [[Coordonnées polaires]] dans le plan $(x,y)$ et gardent la hauteur :
$$x = r\cos\theta,\qquad y = r\sin\theta,\qquad z = z,\qquad r \ge 0,\ \theta \in [0,2\pi].$$

**Jacobien.**
$$J = \begin{vmatrix}\cos\theta & -r\sin\theta & 0\\ \sin\theta & r\cos\theta & 0\\ 0 & 0 & 1\end{vmatrix} = r, \qquad\text{donc}\quad dx\,dy\,dz = r\,dr\,d\theta\,dz.$$

**Usage.** Adaptées aux domaines de révolution autour de l'axe $Oz$ (cylindres, cônes, paraboloïdes) et aux fonctions qui dépendent de $x^2 + y^2$.

**Exemple.** Volume du cylindre de rayon $R$ et de hauteur $h$ :
$$\int_0^h\!\!\int_0^{2\pi}\!\!\int_0^R r\,dr\,d\theta\,dz = h\cdot 2\pi\cdot\frac{R^2}{2} = \pi R^2 h.$$

## Dans le cours

Le cours ne la nomme pas : il s'arrête à la dimension 2. Elle apparaît dans les compléments de [[2 - intégrales multiples]].

Notion parente : [[Coordonnées polaires]]. Voir aussi : [[Intégrale multiple]], [[Coordonnées sphériques]], [[Matrice jacobienne]].

Résumés : [[2 - intégrales multiples]]
