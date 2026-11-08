---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Analyse dans Rn/Chp 5 : Calcul différentiel d'ordre supérieur.docx|Chp 5 - Calcul différentiel d'ordre supérieur]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Analyse dans Rn/Chp 5 : Calcul différentiel d'ordre supérieur.docx|Chp 5 - Calcul différentiel d'ordre supérieur]], dans [[Cours/Mathématiques/Analyse dans Rn/_index|Analyse dans Rn]].
## 1. Différentiation d'ordre supérieur ou égal à 2

Pour $f$ de deux variables, les dérivées partielles d'ordre 2 sont
$$f''(x, y) = \left(\frac{\partial^2 f}{\partial x^2}\ ;\ \frac{\partial^2 f}{\partial y^2}\ ;\ \frac{\partial^2 f}{\partial x\partial y}\ ;\ \frac{\partial^2 f}{\partial y\partial x}\right),$$
avec par exemple
$$\frac{\partial^2 f}{\partial x^2} = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial x}\right), \qquad \frac{\partial^2 f}{\partial y\partial x} = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right).$$
La dérivée croisée s'écrit comme limite : [[Erreurs du cours#^e-5-calcul-differentiel-d-ordre-superieur|✎]]
$$\frac{\partial^2 f}{\partial y\partial x} = \lim_{t \to 0}\frac1t\left[\left.\frac{\partial f}{\partial x}\right|_{x,\,y+t} - \left.\frac{\partial f}{\partial x}\right|_{x,\,y}\right].$$
Voir [[Dérivée partielle]].

Exemple : $f(x, y) = x^3y^2$. Alors $\frac{\partial f}{\partial x} = 3x^2y^2$ et $\frac{\partial f}{\partial y} = 2x^3y$, puis $\frac{\partial^2 f}{\partial x^2} = 6xy^2$, $\frac{\partial^2 f}{\partial y^2} = 2x^3$, et $\frac{\partial^2 f}{\partial y\partial x} = \frac{\partial}{\partial y}(3x^2y^2) = 6x^2y = \frac{\partial}{\partial x}(2x^3y) = \frac{\partial^2 f}{\partial x\partial y}$ : les deux dérivées croisées coïncident, comme le prévoit le théorème de Schwarz ci-dessous. [[Complément hors du cours|ⓘ]]

Notations courantes, dites de Monge : $p = \frac{\partial f}{\partial x}$, $q = \frac{\partial f}{\partial y}$, $r = \frac{\partial^2 f}{\partial x^2}$, $s = \frac{\partial^2 f}{\partial x\partial y}$, $t = \frac{\partial^2 f}{\partial y^2}$ ; on écrit aussi $f_x$, $f_{xx}$, $f_{yy}$. [[Complément hors du cours|ⓘ]]

> **Définition 2 (classe $\mathcal C^k$, $\mathcal C^\infty$)** : soit $U$ un [[Ouvert et fermé|ouvert]] de $\mathbb R^p$ et $f : U \to \mathbb R^n$. $f$ est de classe $\mathcal C^k$ sur $U$ si et seulement si toutes ses dérivées partielles d'ordre $k$ existent et sont continues sur $U$. $f$ est de classe $\mathcal C^\infty$ si et seulement si elle est $\mathcal C^k$ pour tout $k \in \mathbb N$ ([[Fonction de classe Ck]]).

> **Propriété 1** : si $f$ est $\mathcal C^k$ sur $U$, toutes ses dérivées partielles d'ordre **inférieur ou égal** à $k$ sont définies et continues.

Notes de cours :
- $f$ de classe $\mathcal C^k$ $\iff$ les composantes de $f$ sont $\mathcal C^k$ ;
- $f$ de classe $\mathcal C^k$ $\Rightarrow$ les dérivées partielles de $f$ sont continues jusqu'à l'ordre $k$ inclus.

> **Théorème 1 (stabilité de $\mathcal C^k$ par composition)** : soit $f$ de classe $\mathcal C^k$ de $U$ (ouvert de $\mathbb R^p$) dans $\mathbb R^q$, et $g$ de classe $\mathcal C^k$ de $V$ (ouvert de $\mathbb R^q$) dans $\mathbb R^n$. Si $f(U) \subset V$, alors $g \circ f$ est $\mathcal C^k$ sur $U$.

> **Théorème 2** : soit $f : U \to \mathbb R^n$ une application. Sont équivalents : [[Erreurs du cours#^e-5-calcul-differentiel-d-ordre-superieur|✎]]
> 1. $f$ est de classe $\mathcal C^k$ ;
> 2. les fonctions coordonnées de $f$ dans la base de $\mathbb R^n$ sont de classe $\mathcal C^k$.

> **Théorème 3 ([[Théorème de Schwarz]])** : soit $f$ de classe $\mathcal C^1$ de $U$ (ouvert de $\mathbb R^p$) dans $\mathbb R^q$, $a \in U$ et $(i, j) \in [\![1, p]\!]^2$. Si $\frac{\partial^2 f}{\partial x_j\partial x_i}$ et $\frac{\partial^2 f}{\partial x_i\partial x_j}$ sont définies et continues en $a$, alors
> $$\left.\frac{\partial^2 f}{\partial x_j\partial x_i}\right|_a = \left.\frac{\partial^2 f}{\partial x_i\partial x_j}\right|_a.$$

Remarques du cours :
- si $f$ est $\mathcal C^2$, les dérivées croisées sont continues, donc Schwarz s'applique : être $\mathcal C^2$ est une [[Condition nécessaire et suffisante|condition suffisante]] mais non nécessaire ;
- si $f$ n'est pas $\mathcal C^2$, cela ne veut pas dire que les dérivées croisées ne sont pas égales ;
- la condition « être $\mathcal C^2$ » est trop forte pour Schwarz : seule la [[Limite et continuité|continuité]] des dérivées croisées est requise.

Sans continuité des dérivées croisées, elles peuvent différer. Contre-exemple classique : $f(x, y) = \dfrac{xy(x^2 - y^2)}{x^2 + y^2}$, $f(0, 0) = 0$, de classe $\mathcal C^1$ sur $\mathbb R^2$. On calcule $\left.\frac{\partial f}{\partial x}\right|_{0,y} = -y$ et $\left.\frac{\partial f}{\partial y}\right|_{x,0} = x$, d'où $\left.\frac{\partial^2 f}{\partial y\partial x}\right|_{0,0} = -1$ mais $\left.\frac{\partial^2 f}{\partial x\partial y}\right|_{0,0} = 1$. [[Complément hors du cours|ⓘ]]

Conséquence pratique : pour $f$ de classe $\mathcal C^k$, l'ordre des dérivations n'importe pas jusqu'à l'ordre $k$. Pour deux variables, une fonction $\mathcal C^2$ n'a donc que **trois** dérivées secondes distinctes ($\frac{\partial^2 f}{\partial x^2}$, $\frac{\partial^2 f}{\partial x\partial y}$, $\frac{\partial^2 f}{\partial y^2}$), et non quatre. [[Complément hors du cours|ⓘ]]

## Matrice hessienne, formule de Taylor et extrema

Cette section n'est pas dans la note ; elle prolonge naturellement le chapitre et sert en optimisation (et dans [[Extremum local d'une fonction de deux variables|la régression linéaire]] vue en year 3). [[Complément hors du cours|ⓘ]]

**[[Matrice hessienne]].** Pour $f : U \subset \mathbb R^p \to \mathbb R$ de classe $\mathcal C^2$, la hessienne en $a$ est la matrice $p \times p$ des dérivées secondes :
$$H_f(a) = \left(\left.\frac{\partial^2 f}{\partial x_i\partial x_j}\right|_a\right)_{1 \le i, j \le p}, \qquad \text{pour } p = 2 :\ H_f(a) = \begin{pmatrix} r & s \\ s & t \end{pmatrix}.$$
Par le théorème de Schwarz, elle est [[Matrice symétrique|symétrique]], donc diagonalisable en base orthonormée ([[Théorème spectral]]). C'est la jacobienne du gradient. [[Complément hors du cours|ⓘ]]

**Formule de Taylor-Young à l'ordre 2.** Si $f$ est $\mathcal C^2$ sur $U$ et $a \in U$ :
$$f(a + h) = f(a) + \vec\nabla_af \cdot h + \frac12\,{}^th\,H_f(a)\,h + o(\|h\|^2).$$
Pour $p = 2$ et $h = (h_1, h_2)$ : $\frac12\,{}^thH_f(a)h = \frac12(r h_1^2 + 2s h_1h_2 + t h_2^2)$, une [[Forme quadratique|forme quadratique]] en $h$. C'est la généralisation du [[Développement limité|développement limité]] à l'ordre 2 en une variable. [[Complément hors du cours|ⓘ]]

**Points critiques.** Si $f$ (différentiable sur l'ouvert $U$) admet un [[Extremum local|extremum local]] en $a$, alors $\vec\nabla_af = 0$ : $a$ est un **point critique**. La réciproque est fausse : $f(x, y) = x^2 - y^2$ a un point critique en $(0, 0)$, qui n'est ni un minimum ni un maximum (un **point col**, ou point selle). [[Complément hors du cours|ⓘ]]

**Nature d'un point critique** (condition suffisante, $f$ de classe $\mathcal C^2$, $\vec\nabla_af = 0$) : [[Complément hors du cours|ⓘ]]

| Hessienne $H_f(a)$ | Cas $p = 2$ | Conclusion |
|---|---|---|
| [[Forme quadratique définie positive\|définie positive]] (valeurs propres $> 0$) | $rt - s^2 > 0$ et $r > 0$ | minimum local strict |
| définie négative (valeurs propres $< 0$) | $rt - s^2 > 0$ et $r < 0$ | maximum local strict |
| valeurs propres non nulles de signes opposés | $rt - s^2 < 0$ | point col (pas d'extremum) |
| une valeur propre nulle | $rt - s^2 = 0$ | on ne peut pas conclure à l'ordre 2 |

Exemple : $f(x, y) = x^2 + xy + y^2 - 3x$. $\vec\nabla f = (2x + y - 3,\ x + 2y) = 0$ donne $(x, y) = (2, -1)$. Puis $r = 2$, $s = 1$, $t = 2$ : $rt - s^2 = 3 > 0$ et $r > 0$, c'est un minimum local (ici global, $f$ étant une fonction quadratique convexe), de valeur $f(2, -1) = -3$. [[Complément hors du cours|ⓘ]]

## 2. Systèmes d'EDP d'ordre 1

On résout un système d'[[Équation aux dérivées partielles|équations aux dérivées partielles]]
$$\left.\frac{\partial f}{\partial x}\right|_{x,y} = g(x, y), \qquad \left.\frac{\partial f}{\partial y}\right|_{x,y} = h(x, y),$$
avec $g$, $h$ de classe $\mathcal C^1$.

**Étape 1 : condition de compatibilité.** Vérifier que
$$\left.\frac{\partial g}{\partial y}\right|_{x,y} = \left.\frac{\partial h}{\partial x}\right|_{x,y}.$$
Justification : si $g$ et $h$ sont $\mathcal C^1$, leurs dérivées partielles sont continues, donc $\frac{\partial^2 f}{\partial x^2} = \frac{\partial g}{\partial x}$, $\frac{\partial^2 f}{\partial y^2} = \frac{\partial h}{\partial y}$, $\frac{\partial^2 f}{\partial x\partial y} = \frac{\partial h}{\partial x}$ et $\frac{\partial^2 f}{\partial y\partial x} = \frac{\partial g}{\partial y}$ sont continues : $f$ est $\mathcal C^2$ et vérifie Schwarz, $\frac{\partial^2 f}{\partial x\partial y} = \frac{\partial^2 f}{\partial y\partial x}$, d'où $\frac{\partial g}{\partial y} = \frac{\partial h}{\partial x}$.

Interprétation : résoudre le système, c'est chercher une fonction $f$ dont le [[Gradient|gradient]] est le champ de vecteurs $(g, h)$ ; une telle $f$ s'appelle un **potentiel** du champ (en physique, le champ électrostatique dérive d'un potentiel). La condition de compatibilité est nécessaire ; elle est aussi suffisante quand l'ouvert est $\mathbb R^2$, un pavé ou plus généralement un ouvert [[Partie convexe|convexe]] (théorème de Poincaré). Sur un ouvert « troué », elle ne suffit pas : $g = \frac{-y}{x^2+y^2}$, $h = \frac{x}{x^2+y^2}$ la vérifient sur $\mathbb R^2 \setminus \{(0,0)\}$, mais il n'existe pas de $f$ sur tout cet ouvert (le candidat naturel, l'angle polaire $\theta$, ne peut pas y être défini continûment). [[Complément hors du cours|ⓘ]]

**Étape 2** : résoudre l'une des deux EDP, par exemple la première : $f(x, y) = G(x, y) + K_1(y)$, où $G$ est une [[Primitive|primitive]] de $g$ selon $x$ et $K_1$ une fonction quelconque $\mathcal C^2$.

**Étape 3** : dériver cette solution par rapport à l'autre variable (ici $y$) et l'injecter dans l'EDP non encore utilisée : on obtient une équation sur $K_1$.

**Étape 4** : résoudre l'équation de l'étape 3.

**Étape 5** : écrire la solution en combinant les étapes 2 et 4.

### Exemple complet

Résoudre sur $\mathbb R^2$ :
$$\begin{cases}
\left.\dfrac{\partial f}{\partial x}\right|_{x,y} = (x + 1)\cos(x + y) + \sin(x + y) - \sin x = g(x, y) \\[2mm]
\left.\dfrac{\partial f}{\partial y}\right|_{x,y} = (x + 1)\cos(x + y) = h(x, y)
\end{cases}$$

1. **Compatibilité** : $\dfrac{\partial g}{\partial y} = -(x + 1)\sin(x + y) + \cos(x + y) = \dfrac{\partial h}{\partial x}$ : le système admet des solutions.
2. **Intégrer la seconde EDP par rapport à $y$** (plus simple) : $f(x, y) = (x + 1)\sin(x + y) + K_1(x)$, avec $K_1$ de classe $\mathcal C^2$ sur $\mathbb R$.
3. **Dériver par rapport à $x$** : $\dfrac{\partial f}{\partial x} = \sin(x + y) + (x + 1)\cos(x + y) + K_1'(x)$. On injecte dans la première EDP :
$$\sin(x + y) + (x + 1)\cos(x + y) + K_1'(x) = (x + 1)\cos(x + y) + \sin(x + y) - \sin x,$$
d'où $K_1'(x) = -\sin x$. [[Erreurs du cours#^e-5-calcul-differentiel-d-ordre-superieur|✎]]
4. **Intégrer** : $K_1(x) = \cos x + C$, $C \in \mathbb R$.
5. **Solution** :
$$f(x, y) = (x + 1)\sin(x + y) + \cos x + C, \qquad C \in \mathbb R.$$

## 3. EDP d'ordre 2

La démarche est la même qu'à l'ordre 1 : utiliser des changements de variables pour se ramener à une EDP dont on connaît la solution.

> **Théorème 4** : soit $U$ un ouvert [[Partie convexe|convexe]] de $\mathbb R^2$ (par exemple $\mathbb R^2$, un pavé, un disque). [[Erreurs du cours#^e-5-calcul-differentiel-d-ordre-superieur|✎]] Les solutions de classe $\mathcal C^2$ de $\dfrac{\partial^2 f}{\partial x^2} = 0$ sont de la forme
> $$f(x, y) = xG(y) + H(y),$$
> où $G$ et $H$ sont $\mathcal C^2$ sur la projection de $U$ sur l'axe $Oy$.

Démonstration : on applique deux fois le théorème 8 du [[4 - Calcul différentiel du premier ordre|chapitre 4]]. $\frac{\partial}{\partial x}\left(\frac{\partial f}{\partial x}\right) = 0$ donne $\frac{\partial f}{\partial x} = G(y)$ ; en intégrant encore par rapport à $x$, $f(x, y) = xG(y) + H(y)$. La convexité de $U$ garantit que, pour chaque $y$, les $x$ tels que $(x, y) \in U$ forment un intervalle, hypothèse du théorème 8 ; sans elle, $G$ et $H$ pourraient changer d'un morceau à l'autre. [[Complément hors du cours|ⓘ]]

> **Théorème 5** : soit $U$ un ouvert convexe de $\mathbb R^2$. [[Erreurs du cours#^e-5-calcul-differentiel-d-ordre-superieur|✎]] Les solutions de classe $\mathcal C^2$ de $\dfrac{\partial^2 f}{\partial x\partial y} = 0$ sont de la forme
> $$f(x, y) = G(x) + H(y),$$
> où $G$ et $H$ sont $\mathcal C^2$ sur les projections de $U$ sur les axes $Ox$ et $Oy$ respectivement.

Démonstration du théorème 5 : $\frac{\partial^2 f}{\partial x\partial y} = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right) = 0$ donne $\frac{\partial f}{\partial y} = \varphi(y)$ ; en intégrant par rapport à $y$, $f(x, y) = H(y) + G(x)$, où $H$ est une primitive de $\varphi$. [[Complément hors du cours|ⓘ]]

Le cours ne donne pas d'exemple d'EDP d'ordre 2 dans cette note.

**Exemple classique : l'[[Équation des ondes|équation des ondes]]** (ou des cordes vibrantes), $\dfrac{\partial^2 f}{\partial t^2} = c^2\dfrac{\partial^2 f}{\partial x^2}$, $c > 0$, pour $f$ de classe $\mathcal C^2$ sur $\mathbb R^2$. [[Complément hors du cours|ⓘ]]
1. Changement de variables $u = x + ct$, $v = x - ct$ : linéaire, de déterminant $\begin{vmatrix} 1 & c \\ 1 & -c \end{vmatrix} = -2c \neq 0$, donc un $\mathcal C^1$-difféomorphisme (et même $\mathcal C^\infty$) de $\mathbb R^2$ sur $\mathbb R^2$. On pose $f(x, t) = g(x + ct, x - ct)$. [[Complément hors du cours|ⓘ]]
2. Dérivation en chaîne : $\frac{\partial f}{\partial x} = \frac{\partial g}{\partial u} + \frac{\partial g}{\partial v}$, $\frac{\partial f}{\partial t} = c\frac{\partial g}{\partial u} - c\frac{\partial g}{\partial v}$, puis, avec Schwarz pour $g$ : $\frac{\partial^2 f}{\partial x^2} = \frac{\partial^2 g}{\partial u^2} + 2\frac{\partial^2 g}{\partial u\partial v} + \frac{\partial^2 g}{\partial v^2}$ et $\frac{\partial^2 f}{\partial t^2} = c^2\left(\frac{\partial^2 g}{\partial u^2} - 2\frac{\partial^2 g}{\partial u\partial v} + \frac{\partial^2 g}{\partial v^2}\right)$. [[Complément hors du cours|ⓘ]]
3. L'équation devient $-4c^2\frac{\partial^2 g}{\partial u\partial v} = 0$, soit $\frac{\partial^2 g}{\partial u\partial v} = 0$ : par le théorème 5, $g(u, v) = G(u) + H(v)$. [[Complément hors du cours|ⓘ]]
4. Solution (formule de d'Alembert) : $f(x, t) = G(x + ct) + H(x - ct)$, avec $G$, $H$ de classe $\mathcal C^2$ : la somme de deux ondes qui se déplacent à la vitesse $c$, l'une vers la gauche, l'autre vers la droite. [[Complément hors du cours|ⓘ]]

Les autres grandes EDP d'ordre 2 de la physique sont l'**équation de Laplace** $\Delta f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} = 0$ (ses solutions sont les fonctions **harmoniques** ; $\Delta$ est le **laplacien**) et l'**équation de la chaleur** $\frac{\partial f}{\partial t} = D\frac{\partial^2 f}{\partial x^2}$ (diffusion). Elles ne se résolvent pas, en général, par un simple changement de variables. [[Complément hors du cours|ⓘ]]
