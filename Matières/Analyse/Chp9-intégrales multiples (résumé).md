---
type: source
tags: [year2]
sources: ["[[raw/Year 2/Analyse/Chp9-intégrales multiples.pdf|Chp9-intégrales multiples]]"]
maj: 2026-11-06
---

Résumé de [[raw/Year 2/Analyse/Chp9-intégrales multiples.pdf|Chp9-intégrales multiples]] (3 pages manuscrites, scannées), dans [[Analyse (matière)]]. Ce sont des notes de cours à la main : pas de preuves, seulement les définitions et les méthodes. Lu en image.

## Contenu, dans l'ordre

**Domaines d'intégration** (voir [[Intégrale multiple]])
- Compact élémentaire de 1er type : $D = \{(x,y) : a \le x \le b,\ y_1(x) \le y \le y_2(x)\}$.
- Compact élémentaire de 2e type : $D = \{(x,y) : a \le y \le b,\ x_1(y) \le x \le x_2(y)\}$.
- Un pavé de $\mathbb{R}^n$ est un produit de segments $\prod [a_i, b_i]$ : segment dans $\mathbb{R}^1$, rectangle dans $\mathbb{R}^2$, parallélépipède rectangle dans $\mathbb{R}^3$.
- **Théorème de Fubini** : $f$ continue sur le pavé $[a,b] \times [c,d]$. Alors $\iint_P f\,dx\,dy = \int_c^d \left(\int_a^b f\,dx\right) dy = \int_a^b \left(\int_c^d f\,dy\right) dx$. On choisit l'ordre qui arrange.
- Aire d'une figure : $A(D) = \iint_D 1\,dx\,dy$.

**Techniques d'intégration**
- Sur un compact de 1er type : $\int_a^b \left(\int_{f_1(x)}^{f_2(x)} f(x,y)\,dy\right) dx$. On intègre d'abord en $y$, puis en $x$. L'ordre compte : les bornes intérieures dépendent de la variable extérieure.
- Sur un compact de 2e type : on intègre d'abord en $x$, puis en $y$.
- Si $D$ n'est ni un pavé ni un compact élémentaire, on le découpe ou on le transforme pour se ramener à l'un des deux cas.

**Changement de variable**
- Adapter les coordonnées à la forme de $D$ : forme quelconque, coordonnées cartésiennes ; disque ou cercle, polaires ; ellipse, elliptiques.
- Rappels : cercle $(x-a)^2 + (y-b)^2 = r^2$ (disque avec $\le$), aire $\pi r^2$, périmètre $2\pi r$ ; ellipse $\frac{(x-c)^2}{a^2} + \frac{(y-d)^2}{b^2} = 1$.
- Formule : $\varphi : (u,v) \mapsto (x(u,v), y(u,v))$ bijection d'un domaine $\Delta$ sur $D$, de jacobien $J_\varphi = \det \begin{pmatrix} \partial x/\partial u & \partial x/\partial v \\ \partial y/\partial u & \partial y/\partial v \end{pmatrix}$. Alors $\iint_D f\,dx\,dy = \iint_\Delta f(x(u,v), y(u,v))\,|J_\varphi|\,du\,dv$. La valeur absolue du jacobien est marquée en rouge dans le cours.
- Polaires : $x = r\cos\theta,\ y = r\sin\theta$.
- Elliptiques : $x = a r\cos\theta,\ y = b r\sin\theta$, avec $J_\varphi = a b r$.

## Points à vérifier

- Le jacobien des coordonnées polaires n'est pas écrit dans ces notes. Il vaut $r$ (complément) : c'est le cas $a = b = 1$ du jacobien elliptique $abr$.
- Les notes s'arrêtent là : pas d'intégrales triples, ni de coordonnées cylindriques ou sphériques (complément : le titre du chapitre est « intégrales multiples », mais seules les intégrales doubles figurent dans ce PDF).

## Liens

[[Intégrale multiple]], [[Intégrale]] (cas à une variable, Chap 7 : [[Chap7-Integration (résumé)]]), [[Matrice jacobienne]] et [[Difféomorphisme]] (le changement de variable demande une bijection régulière), [[Dérivée partielle]] pour les dérivées du jacobien. Exercices associés : voir [[Analyse (matière)]].
