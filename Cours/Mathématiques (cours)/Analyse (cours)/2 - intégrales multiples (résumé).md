---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Analyse/Chp9-intégrales multiples.pdf|Chp9-intégrales multiples.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé de Chp9-intégrales multiples ([[Raw/Year 2/Analyse/Chp9-intégrales multiples.pdf|Chp9-intégrales multiples.pdf]]) (3 pages manuscrites, scannées), dans [[Analyse (index)]]. Ce sont des notes de cours à la main : pas de preuves, seulement les définitions et les méthodes. Lu en image. Les passages surlignés dans les notes sont les formules à retenir.

## 1. Domaines d'intégration

Voir [[Intégrale multiple]].

### Compacts élémentaires

**[[Compact élémentaire]] de 1er type** (bords du type $y = f(x)$) : $D \subset \mathbb{R}^2$,
$$D = \{(x,y) \in \mathbb{R}^2 \mid a \le x \le b \ \text{et}\ y_1(x) \le y \le y_2(x)\}.$$

**Compact élémentaire de 2e type** (bords du type $x = f(y)$) :
$$D = \{(x,y) \in \mathbb{R}^2 \mid a \le y \le b \ \text{et}\ x_1(y) \le x \le x_2(y)\}.$$

### Pavé

$P \subset \mathbb{R}^n$ est un **[[Pavé|pavé]]** si et seulement s'il existe $a = (a_1, \dots, a_n)$ et $b = (b_1, \dots, b_n)$ tels que
$$P = \prod_{i=1}^{n} [a_i, b_i] \quad \text{(produit de segments).}$$
En gros, un pavé de $\mathbb{R}^1$ est un segment, de $\mathbb{R}^2$ un rectangle, de $\mathbb{R}^3$ un parallélépipède rectangle.

### Théorème de Fubini

Soit $f$ à valeurs réelles, continue et définie sur $P = \{(x,y) \in \mathbb{R}^2 \mid a \le x \le b,\ c \le y \le d\}$. Alors
$$\iint_P f(x,y)\,dx\,dy = \int_c^d \left(\int_a^b f(x,y)\,dx\right) dy = \int_a^b \left(\int_c^d f(x,y)\,dy\right) dx.$$
Sur un pavé, on peut donc commencer par intégrer en $dx$ ou en $dy$, selon ce qui arrange.

### Aire d'une figure

$$\mathcal{A}(D) = \iint_D 1\,dx\,dy.$$

![[Chp9 intégrales multiples - p1.jpg]]
*Figure : un domaine $D$ quelconque du plan, dont l'aire est l'intégrale double de $1$.*

## 2. Techniques d'intégration

**Sur un compact élémentaire de 1er type** $D = \{a \le x \le b,\ f_1(x) \le y \le f_2(x)\}$ :
$$\iint_D f(x,y)\,dx\,dy = \int_a^b \left(\int_{f_1(x)}^{f_2(x)} f(x,y)\,dy\right) dx.$$
Importance de l'ordre : on intègre d'abord en $y$, puis en $x$ (les bornes intérieures dépendent de $x$).

**Sur un compact élémentaire de 2e type** $D = \{a \le y \le b,\ f_1(y) \le x \le f_2(y)\}$ :
$$\iint_D f(x,y)\,dx\,dy = \int_a^b \left(\int_{f_1(y)}^{f_2(y)} f(x,y)\,dx\right) dy.$$
Importance de l'ordre : on intègre d'abord en $x$, puis en $y$.

**Autre domaine.** Si $D$ n'est ni un pavé ni un compact élémentaire, il faut le transformer (le découper, ou changer de variables) pour se ramener à l'un de ces deux cas.

## 3. Changement de variable (coordonnées)

### Choisir les coordonnées selon la forme de $D$

| Forme de $D$ | Coordonnées |
|---|---|
| quelconque | cartésiennes |
| cercle / disque | [[Coordonnées polaires\|polaires]] |
| [[Ellipse\|ellipse]] | [[Coordonnées elliptiques\|elliptiques]] |

### Rappels : cercle, disque, ellipse

- Cercle de centre $O$ et de rayon $r$ : $x^2 + y^2 = r^2$ ($\le$ pour le disque).
- Cercle de centre $(a;b)$ : $(x-a)^2 + (y-b)^2 = r^2$ ($\le$ pour le disque).
- Aire du disque $\pi r^2$, périmètre du cercle $2\pi r$. Le cercle correspond au périmètre (« $=$ »), le disque à l'aire (« $\le$ »).
- Ellipse centrée en $O$, de demi-axes $a$ et $b$ : $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$.
- Ellipse de centre $(c;d)$ : $\dfrac{(x-c)^2}{a^2} + \dfrac{(y-d)^2}{b^2} = 1$.

![[Chp9 intégrales multiples - p3.jpg]]
*Figure : cercle de rayon $r$ centré à l'origine, cercle centré en $(a;b)$, ellipse de demi-axes $a$ et $b$ (sommets $\pm a$, $\pm b$), ellipse centrée en $(c;d)$, avec leurs équations.*

### Formule du changement de variables

Soit $D$ un domaine et $\varphi : (u,v) \mapsto (x(u,v),\, y(u,v))$ une bijection d'un domaine $\Delta$ sur $D$. Le **jacobien** de $\varphi$ ([[Matrice jacobienne]]) est
$$J_\varphi = \begin{vmatrix} \dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v} \\[2mm] \dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v} \end{vmatrix}.$$
Alors
$$\iint_D f(x,y)\,dx\,dy = \iint_\Delta f\big(x(u,v),\, y(u,v)\big)\,|J_\varphi|\,du\,dv.$$
La valeur absolue du jacobien est marquée en rouge dans les notes : ne pas l'oublier.

### Coordonnées usuelles

- **Polaires** : $x = r\cos\theta$, $y = r\sin\theta$.
- **Elliptiques** : $x = a\,r\cos\theta$, $y = b\,r\sin\theta$, avec $J_\varphi = a\,b\,r$.

## Points à vérifier

- Le jacobien des coordonnées polaires n'est pas écrit dans ces notes. Il vaut $r$ (complément) : c'est le cas $a = b = 1$ du jacobien elliptique $abr$.
- Les notes s'arrêtent là : pas d'intégrales triples, ni de coordonnées cylindriques ou sphériques (complément : le titre du chapitre est « intégrales multiples », mais seules les intégrales doubles figurent dans ce PDF).
- Page 2, le second encadré est intitulé « compact élémentaire de 1er type » alors qu'il décrit le **2e type** ($a \le y \le b$, $f_1(y) \le x \le f_2(y)$) : erreur de copie dans les notes.
- Les notes ne précisent pas les hypothèses du changement de variables (bijection de classe $\mathcal{C}^1$, d'inverse $\mathcal{C}^1$ : voir [[Difféomorphisme]]), ni les domaines de $r$ et $\theta$ (complément : $r \ge 0$, $\theta \in [0, 2\pi[$).
- Fubini : les notes écrivent « Soit $f \in \mathbb{R}$ », à lire « $f$ à valeurs réelles ».

## Liens

[[Intégrale multiple]], [[Intégrale]] (cas à une variable, Chap 7 : [[1 - Integration (résumé)]]), [[Matrice jacobienne]] et [[Difféomorphisme]] (le changement de variable demande une bijection régulière), [[Dérivée partielle]] pour les dérivées du jacobien. Exercices associés : voir [[Analyse (index)]].
