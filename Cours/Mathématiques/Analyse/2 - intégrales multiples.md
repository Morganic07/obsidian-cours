---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Analyse/Chp9-intégrales multiples.pdf|Chp9-intégrales multiples.pdf]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de Chp9-intégrales multiples ([[Raw/Year 2/Analyse/Chp9-intégrales multiples.pdf|Chp9-intégrales multiples.pdf]]) (3 pages manuscrites, scannées), dans [[Cours/Mathématiques/Analyse/_index|Analyse]]. Ce sont des notes de cours à la main : pas de preuves, seulement les définitions et les méthodes. Lu en image. Les passages surlignés dans les notes sont les formules à retenir.

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

Concrètement, l'intégrale entre parenthèses se calcule en traitant l'autre variable comme une constante : dans $\int_a^b f(x,y)\,dx$, $y$ est fixé et le résultat est une fonction de $y$ seul, que l'on intègre ensuite sur $[c,d]$. [[Complément hors du cours|ⓘ]]

**Cas d'une fonction à variables séparées.** Si $f(x,y) = g(x)\,h(y)$ sur le pavé $[a,b]\times[c,d]$, l'intégrale double est le produit de deux intégrales simples : $\displaystyle\iint_P g(x)\,h(y)\,dx\,dy = \left(\int_a^b g(x)\,dx\right)\left(\int_c^d h(y)\,dy\right)$. Exemple : $\displaystyle\iint_{[0,1]\times[0,2]} x\,y^2\,dx\,dy = \frac12 \times \frac83 = \frac43$. [[Complément hors du cours|ⓘ]]

### Aire d'une figure

$$\mathcal{A}(D) = \iint_D 1\,dx\,dy.$$

![[Chp9 intégrales multiples - p1.jpg]]
*Figure : un domaine $D$ quelconque du plan, dont l'aire est l'intégrale double de $1$.*

**Interprétation géométrique.** Pour $f \ge 0$ continue sur $D$, $\iint_D f(x,y)\,dx\,dy$ est le **volume** du solide compris entre le domaine $D$ (dans le plan $z = 0$) et la surface $z = f(x,y)$, comme l'intégrale simple d'une fonction positive est une aire sous une courbe. Avec $f = 1$, ce volume est celui d'un cylindre de base $D$ et de hauteur 1, d'où la formule de l'aire. De même, $\dfrac{1}{\mathcal{A}(D)}\iint_D f\,dx\,dy$ est la **valeur moyenne** de $f$ sur $D$. [[Complément hors du cours|ⓘ]]

**Propriétés de calcul.** Comme l'intégrale simple, l'intégrale double est **linéaire** ($\iint_D (\lambda f + \mu g) = \lambda\iint_D f + \mu\iint_D g$), **positive** ($f \ge 0 \Rightarrow \iint_D f \ge 0$, donc $f \le g \Rightarrow \iint_D f \le \iint_D g$) et **additive par rapport au domaine** (analogue de la [[Relation de Chasles]]) : si $D = D_1 \cup D_2$ avec $D_1$ et $D_2$ qui ne se chevauchent que sur un bord, $\iint_D f = \iint_{D_1} f + \iint_{D_2} f$. C'est cette dernière propriété qui justifie le découpage d'un domaine compliqué en morceaux simples (section 2). [[Complément hors du cours|ⓘ]]

## 2. Techniques d'intégration

**Sur un compact élémentaire de 1er type** $D = \{a \le x \le b,\ f_1(x) \le y \le f_2(x)\}$ :
$$\iint_D f(x,y)\,dx\,dy = \int_a^b \left(\int_{f_1(x)}^{f_2(x)} f(x,y)\,dy\right) dx.$$
Importance de l'ordre : on intègre d'abord en $y$, puis en $x$ (les bornes intérieures dépendent de $x$).

**Sur un compact élémentaire de 2e type** $D = \{a \le y \le b,\ f_1(y) \le x \le f_2(y)\}$ : [[Erreurs du cours#^e-2-integrales-multiples|✎]]
$$\iint_D f(x,y)\,dx\,dy = \int_a^b \left(\int_{f_1(y)}^{f_2(y)} f(x,y)\,dx\right) dy.$$
Importance de l'ordre : on intègre d'abord en $x$, puis en $y$.

**Méthode pour poser les bornes.** Dessiner $D$. Pour un type 1, lire l'intervalle $[a,b]$ parcouru par $x$ (projection de $D$ sur l'axe des $x$), puis, pour un $x$ fixé, tracer la verticale : elle entre dans $D$ en $y = f_1(x)$ (courbe du bas) et en sort en $y = f_2(x)$ (courbe du haut). Pour un type 2, même chose avec une horizontale, de la courbe de gauche $x = f_1(y)$ à celle de droite $x = f_2(y)$. Les bornes extérieures sont toujours des **constantes**. [[Complément hors du cours|ⓘ]]

**Exemple sur un triangle.** Le triangle $T$ de sommets $(0,0)$, $(1,0)$, $(1,1)$ est à la fois de 1er type ($0 \le x \le 1$, $0 \le y \le x$) et de 2e type ($0 \le y \le 1$, $y \le x \le 1$). Les deux calculs donnent le même résultat : [[Complément hors du cours|ⓘ]]
$$\iint_T xy\,dx\,dy = \int_0^1 x\left(\int_0^x y\,dy\right)dx = \int_0^1 \frac{x^3}{2}\,dx = \frac18, \qquad \int_0^1 y\left(\int_y^1 x\,dx\right)dy = \int_0^1 \frac{y - y^3}{2}\,dy = \frac18.$$

**Intervertir l'ordre d'intégration.** Quand un domaine est des deux types, on peut réécrire l'intégrale dans l'autre ordre en redécrivant $D$, ce qui débloque parfois un calcul impossible autrement. Exemple : $\int_0^1\left(\int_y^1 e^{x^2}\,dx\right)dy$ ne se calcule pas directement ($e^{x^2}$ n'a pas de primitive exprimable avec les fonctions usuelles) ; le domaine est le triangle $T$ ci-dessus, donc l'intégrale vaut $\int_0^1\left(\int_0^x e^{x^2}\,dy\right)dx = \int_0^1 x\,e^{x^2}\,dx = \dfrac{e - 1}{2}$. [[Complément hors du cours|ⓘ]]

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

**Pourquoi le jacobien.** $|J_\varphi(u,v)|$ est le facteur par lequel $\varphi$ multiplie les aires au voisinage de $(u,v)$ : un petit rectangle de côtés $du$, $dv$ du domaine $\Delta$ est envoyé sur un petit parallélogramme d'aire environ $|J_\varphi|\,du\,dv$ dans $D$. On écrit en abrégé $dx\,dy = |J_\varphi|\,du\,dv$. C'est l'analogue en dimension 2 du facteur $\varphi'(t)$ du [[Changement de variable dans une intégrale|changement de variable à une variable]], $\int f(x)\,dx = \int f(\varphi(t))\,\varphi'(t)\,dt$ ; la valeur absolue remplace ici l'orientation des bornes. [[Complément hors du cours|ⓘ]]

**Hypothèses précises.** Le théorème demande que $\varphi$ soit un [[Difféomorphisme|difféomorphisme]] de classe $C^1$ (bijection $C^1$ de réciproque $C^1$, ce qui revient à $J_\varphi \ne 0$ partout) entre l'intérieur de $\Delta$ et l'intérieur de $D$. Les bords comptent pour une aire nulle : on peut donc ignorer les points où la bijectivité est perdue, comme l'origine en coordonnées polaires (tous les $(0,\theta)$ ont la même image). [[Complément hors du cours|ⓘ]]

### Coordonnées usuelles

- **Polaires** : $x = r\cos\theta$, $y = r\sin\theta$.
- **Elliptiques** : $x = a\,r\cos\theta$, $y = b\,r\sin\theta$, avec $J_\varphi = a\,b\,r$.

**Jacobien des coordonnées polaires.** Les notes ne l'écrivent pas ; il se calcule avec la formule ci-dessus : [[Complément hors du cours|ⓘ]]
$$J_\varphi = \begin{vmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{vmatrix} = r\cos^2\theta + r\sin^2\theta = r, \qquad \text{d'où } dx\,dy = r\,dr\,d\theta.$$
Le disque de centre $O$ et de rayon $R$ correspond au rectangle $\Delta = [0,R]\times[0,2\pi]$ : le changement de variable transforme un disque en pavé, où [[Intégrale multiple|Fubini]] s'applique. Une couronne $R_1 \le \sqrt{x^2+y^2} \le R_2$ donne $[R_1,R_2]\times[0,2\pi]$, un quart de disque dans le quadrant $x, y \ge 0$ donne $[0,R]\times[0,\pi/2]$. Pour un disque de centre $(a;b)$, on pose $x = a + r\cos\theta$, $y = b + r\sin\theta$ (même jacobien $r$). [[Complément hors du cours|ⓘ]]

**Le jacobien elliptique** se calcule de même : $J_\varphi = \begin{vmatrix} a\cos\theta & -ar\sin\theta \\ b\sin\theta & br\cos\theta \end{vmatrix} = abr$. L'intérieur de l'ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} \le 1$ correspond à $0 \le r \le 1$, $0 \le \theta \le 2\pi$ (on remplace et on trouve $r^2 \le 1$). [[Complément hors du cours|ⓘ]]

**Exemples d'aires.** Aire du disque : $\displaystyle\iint_D dx\,dy = \int_0^{2\pi}\!\!\int_0^R r\,dr\,d\theta = 2\pi \cdot \frac{R^2}{2} = \pi R^2$, ce qui retrouve la formule rappelée plus haut. Aire de l'ellipse de demi-axes $a$ et $b$ : $\displaystyle\int_0^{2\pi}\!\!\int_0^1 abr\,dr\,d\theta = \pi ab$ (on retrouve $\pi R^2$ pour $a = b = R$). [[Complément hors du cours|ⓘ]]

**L'intégrale de Gauss, application classique des polaires.** L'[[Intégrale de Gauss]] $I = \int_{-\infty}^{+\infty} e^{-x^2}\,dx$ ne se calcule pas par primitive. On calcule son carré comme une intégrale double sur tout le plan, que l'on passe en polaires : $I^2 = \iint_{\mathbb{R}^2} e^{-(x^2+y^2)}\,dx\,dy = \int_0^{2\pi}\!\!\int_0^{+\infty} e^{-r^2}\,r\,dr\,d\theta = 2\pi \cdot \frac12 = \pi$, donc $I = \sqrt{\pi}$. C'est ce résultat qui donne la constante $\frac{1}{\sigma\sqrt{2\pi}}$ de la densité de la [[Loi normale]]. (Le calcul sur un domaine non borné demande de passer à la limite sur des disques de rayon $R \to +\infty$, ce que le cours ne traite pas.) [[Complément hors du cours|ⓘ]]

### Intégrales triples

Le cours s'arrête à la dimension 2, mais tout se transpose à $\mathbb{R}^3$ : Fubini s'écrit avec trois intégrales emboîtées, le **volume** d'un domaine $V$ est $\iiint_V 1\,dx\,dy\,dz$, et le changement de variables utilise un jacobien $3\times 3$. [[Complément hors du cours|ⓘ]]

- **[[Coordonnées cylindriques]]** (domaines de révolution autour de l'axe $Oz$, cylindres, cônes) : $x = r\cos\theta$, $y = r\sin\theta$, $z = z$ ; jacobien $r$, donc $dx\,dy\,dz = r\,dr\,d\theta\,dz$. [[Complément hors du cours|ⓘ]]
- **[[Coordonnées sphériques]]** (boules, sphères) : $x = r\sin\varphi\cos\theta$, $y = r\sin\varphi\sin\theta$, $z = r\cos\varphi$, avec $r \ge 0$, $\varphi \in [0,\pi]$ (angle avec l'axe $Oz$), $\theta \in [0, 2\pi]$ ; jacobien $r^2\sin\varphi$, donc $dx\,dy\,dz = r^2\sin\varphi\,dr\,d\varphi\,d\theta$. Exemple : volume de la boule de rayon $R$, $\int_0^{2\pi}\!\!\int_0^{\pi}\!\!\int_0^R r^2\sin\varphi\,dr\,d\varphi\,d\theta = 2\pi \cdot 2 \cdot \frac{R^3}{3} = \frac43\pi R^3$. [[Complément hors du cours|ⓘ]]

## Liens

[[Intégrale multiple]], [[Intégrale]] (cas à une variable, Chap 7 : [[1 - Integration]]), [[Matrice jacobienne]] et [[Difféomorphisme]] (le changement de variable demande une bijection régulière), [[Dérivée partielle]] pour les dérivées du jacobien. Exercices associés : voir [[Cours/Mathématiques/Analyse/_index|Analyse]].
