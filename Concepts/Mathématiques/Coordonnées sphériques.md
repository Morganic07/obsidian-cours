---
type: concept
tags: [year2]
aliases: [spherical coordinates, coords sphériques, passage en sphériques]
sources: ["[[Raw/Year 2/Analyse/Chp9-intégrales multiples.pdf|Chp9-intégrales multiples.pdf]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : coordonnées de $\mathbb{R}^3$ qui repèrent un point par sa distance à l'origine et deux angles :
$$x = r\sin\varphi\cos\theta,\qquad y = r\sin\varphi\sin\theta,\qquad z = r\cos\varphi,$$
avec $r \ge 0$ (distance à l'origine), $\varphi \in [0,\pi]$ (angle avec l'axe $Oz$, ou colatitude) et $\theta \in [0,2\pi]$ (angle dans le plan $(x,y)$, ou longitude).

**Jacobien.** La valeur absolue du déterminant de la [[Matrice jacobienne]] de $(r,\varphi,\theta) \mapsto (x,y,z)$ vaut $r^2\sin\varphi$ (positif sur $[0,\pi]$), donc
$$dx\,dy\,dz = r^2\sin\varphi\,dr\,d\varphi\,d\theta.$$

**Usage.** Adaptées aux boules, aux sphères et aux fonctions qui ne dépendent que de $x^2 + y^2 + z^2$.

**Exemple.** Volume de la boule de rayon $R$ :
$$\int_0^{2\pi}\!\!\int_0^{\pi}\!\!\int_0^R r^2\sin\varphi\,dr\,d\varphi\,d\theta = 2\pi\cdot 2\cdot\frac{R^3}{3} = \frac43\pi R^3.$$

**Attention aux conventions.** En physique, on note souvent $\theta$ l'angle avec l'axe $Oz$ et $\varphi$ l'angle dans le plan $(x,y)$ : les rôles des deux lettres sont échangés. Le jacobien reste $r^2 \sin(\text{angle avec } Oz)$.

## Dans le cours

Le cours ne la nomme pas : il s'arrête à la dimension 2. Elle apparaît dans les compléments de [[2 - intégrales multiples]].

Voir aussi : [[Intégrale multiple]], [[Coordonnées cylindriques]], [[Coordonnées polaires]].

Résumés : [[2 - intégrales multiples]]
