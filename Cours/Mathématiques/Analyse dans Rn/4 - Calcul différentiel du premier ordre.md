---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Analyse dans Rn/Chp 4 : Calcul différentiel du premier ordre.docx|Chp 4 - Calcul différentiel du premier ordre]]"]
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 2/Analyse dans Rn/Chp 4 : Calcul différentiel du premier ordre.docx|Chp 4 - Calcul différentiel du premier ordre]] (« Chapitre 4 : Calcul différentiel du premier ordre »), dans [[Cours/Mathématiques/Analyse dans Rn/_index|Analyse dans Rn]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Une fonction de plusieurs variables se dérive d'abord direction par direction. La différentielle en donne une approximation linéaire complète, et sert ensuite à résoudre des équations aux dérivées partielles par changement de variables.

## 1. Dérivée partielle

> **Définition 1 ([[Dérivée partielle]])** : soit $U$ un [[Ouvert et fermé|ouvert]] de $\mathbb R^p$, $a \in U$ (le cours écrit $a \in \mathbb R^p$) et $f : U \to F$ ($F$ un EVN). Soit $(e_1, \ldots, e_p)$ la base canonique de $\mathbb R^p$. $f$ admet une dérivée partielle première en $a$ par rapport à la $j$-ème variable si et seulement si l'application
> $$\phi_j : D_j \to F,\quad t \mapsto f(a + te_j), \qquad D_j = \{t \in \mathbb R \mid a + te_j \in U\}$$
> est [[Dérivabilité|dérivable]] en 0. On a alors
> $$\left.\frac{\partial f}{\partial x_j}\right|_a = \phi_j'(0) = \lim_{t \to 0} \frac{f(a + te_j) - f(a)}{t}.$$
> La notation $\left.\frac{\partial f}{\partial x_j}\right|_a$ signifie qu'on dérive par rapport à la $j$-ème variable et qu'on évalue au point $a$.

![[Chp 4 - Calcul différentiel du premier ordre - image23.png]]
*Figure : la surface $z = f(x,y)$ coupée par le plan vertical $y = y_0$ ; la coupe donne la courbe $x \mapsto f(x, y_0)$, dont la pente en $x_0$ est $\partial f/\partial x$ en $(x_0, y_0)$.*

> **Remarque importante** : une application dont toutes les dérivées partielles sont définies en $a$ n'est **pas nécessairement continue** en $a$. Les dérivées partielles ne regardent que les directions des vecteurs de la base canonique, alors qu'on peut s'approcher de $a$ par d'autres directions.

> **Propriété 1** : $f : U \to \mathbb R^n$ admet une dérivée première par rapport à la $j$-ème variable ($j \in [\![1, p]\!]$) si et seulement si, pour tout $i \in [\![1, n]\!]$, $\left.\frac{\partial f_i}{\partial x_j}\right|_a$ est définie. Alors
> $$\left.\frac{\partial f}{\partial x_j}\right|_a = \left(\left.\frac{\partial f_1}{\partial x_j}\right|_a ; \ldots ; \left.\frac{\partial f_n}{\partial x_j}\right|_a\right).$$

## 2. Fonctions différentiables sur un ouvert

> **Définition 2 (fonction [[Différentielle|différentiable]])** : soit $U$ un ouvert de $(\mathbb R^p, \|\cdot\|_p)$, $a \in U$, $f : U \to (F, \|\cdot\|_F)$ et $U_0 = \{h \in \mathbb R^p \mid a + h \in U\}$. $f$ est différentiable en $a$ si et seulement s'il existe une [[Transformation linéaire|application linéaire]] $l : \mathbb R^p \to F$ et une application $\epsilon : U_0 \to F$ telles que
> 1. $\lim_{h \to 0_{\mathbb R^p}} \epsilon(h) = 0_F$ ;
> 2. $\forall h \in U_0,\ f(a + h) = f(a) + l(h) + \|h\|_p\,\epsilon(h)$.
>
> Le second point est le [[Développement limité|développement limité]] à l'ordre 1 de $f$ en $a$. $f$ est différentiable sur $U$ si elle l'est en tout point de $U$.

> **Théorème 1 (différentielle)** : si $f$ est différentiable en $a$, l'application $l$ est **unique**. On l'appelle **différentielle** de $f$ en $a$, notée $D_af$.

- **Propriété 2** : toute application linéaire $\phi : \mathbb R^p \to F$ est différentiable, et $D_a\phi = \phi$ pour tout $a$.
- **Propriété 3** : si $f$ est différentiable en $a$, ses dérivées partielles premières par rapport à toutes ses variables sont définies en $a$ et
$$D_af : \mathbb R^p \to F,\quad h = (h_1, \ldots, h_p) \mapsto D_af(h) = \sum_{j=1}^p h_j \left.\frac{\partial f}{\partial x_j}\right|_a$$
(le cours mélange les indices $i$ et $j$, voir Erreurs du cours).
- **Propriété 4** : si $f$ est différentiable en $a$, elle est continue en $a$.

> **Théorème 2 (différentiabilité sur $\mathbb R^2$)** : soit $U$ un ouvert de $\mathbb R^2$, $(x, y) \in U$, $f : U \to F$. $f$ est différentiable en $(x, y)$ si et seulement si
> $$\lim_{(h_1,h_2) \to (0,0)} \frac{1}{\|(h_1,h_2)\|}\left(f(x + h_1, y + h_2) - f(x,y) - h_1\left.\frac{\partial f}{\partial x}\right|_{x,y} - h_2\left.\frac{\partial f}{\partial y}\right|_{x,y}\right) = 0_F,$$
> la norme utilisée n'ayant pas d'influence sur le résultat.

## 3. Fonctions de classe $\mathcal C^1$

> **Définition 3 (classe $\mathcal C^1$)** : $f : U \to F$ est de classe $\mathcal C^1$ sur $U$ ([[Fonction de classe Ck]]) si et seulement si toutes ses dérivées partielles premières sont **définies et continues** en tout point de $U$. On note $\mathcal C^1(U, F)$ l'ensemble de ces applications.

- **Propriété 5** : toute application linéaire $\phi : \mathbb R^p \to F$ est $\mathcal C^1$ sur $\mathbb R^p$.

> **Théorème 3** : si $f$ est $\mathcal C^1$ sur $U$, alors (1) $f$ est différentiable sur $U$ et (2) $f$ est continue sur $U$.

**Schéma des implications** :
$$f \in \mathcal C^1(U; F) \Rightarrow f \text{ différentiable en } a \in U \Rightarrow \begin{cases} f \text{ continue en } a \\ f \text{ admet toutes ses dérivées partielles en } a \end{cases}$$

![[Chp 4 - Calcul différentiel du premier ordre - image41.png]]
*Figure : schéma des implications entre classe $\mathcal C^1$, différentiabilité, continuité et existence des dérivées partielles.*

Attention :
1. si $f$ est $\mathcal C^1$ en $a$, ses dérivées premières en $a$ sont, par définition, définies et continues ;
2. si $f$ n'est que différentiable en $a$, ses dérivées premières sont définies mais « pas continues » selon le cours (lire « pas forcément continues », voir Erreurs du cours).

> **Théorème 4** : $\mathcal C^1(U, F)$ est un sous-[[Espace vectoriel|espace vectoriel]] de l'espace $\mathcal C(U, F)$ des fonctions continues de $U$ dans $F$.

> **Théorème 5** : pour tous $f, g \in \mathcal C^1(U, F)$, $f \times g \in \mathcal C^1(U, F)$ (voir Erreurs du cours).

> **Théorème 6 (composition)** : soit $f$ de classe $\mathcal C^1$ de $U$ (ouvert de $\mathbb R^p$) dans $\mathbb R^q$, et $g$ de classe $\mathcal C^1$ de $V$ (ouvert de $\mathbb R^q$) dans $\mathbb R^n$. Si $f(U) \subset V$, alors $g \circ f$ est $\mathcal C^1$ sur $U$.

## 4. Composition et changement de variables

> **Propriété 6 ([[Dérivation en chaîne]])** : soit $f : \mathbb R^n \to \mathbb R$ de classe $\mathcal C^1$ sur un ouvert $U$, et $u_1, \ldots, u_n$ de classe $\mathcal C^1$ sur un intervalle $I$, avec $(u_1(t), \ldots, u_n(t)) \in U$ pour tout $t \in I$. Alors $g(t) = f(u_1(t), \ldots, u_n(t))$ est $\mathcal C^1$ sur $I$ et
> $$g'(t) = u_1'(t)\left.\frac{\partial f}{\partial x_1}\right|_{u_1(t), \ldots, u_n(t)} + \cdots + u_n'(t)\left.\frac{\partial f}{\partial x_n}\right|_{u_1(t), \ldots, u_n(t)}.$$
> C'est l'analogue de $(g \circ f)' = (g' \circ f) \times f'$.

> **Propriété 7** : soit $U$, $V$ deux ouverts de $\mathbb R^2$, $f : U \to \mathbb R$, $g_1, g_2 : V \to \mathbb R$, toutes $\mathcal C^1$, avec $(g_1(u,v), g_2(u,v)) \in U$ pour tout $(u,v) \in V$. Alors $h(u, v) = f(g_1(u,v), g_2(u,v))$ est $\mathcal C^1$ sur $V$ et
> $$\begin{cases}
> \dfrac{\partial h}{\partial u}\Big|_{u,v} = \dfrac{\partial f}{\partial x}\Big|_{g_1, g_2}\dfrac{\partial g_1}{\partial u}\Big|_{u,v} + \dfrac{\partial f}{\partial y}\Big|_{g_1, g_2}\dfrac{\partial g_2}{\partial u}\Big|_{u,v} \\[2ex]
> \dfrac{\partial h}{\partial v}\Big|_{u,v} = \dfrac{\partial f}{\partial x}\Big|_{g_1, g_2}\dfrac{\partial g_1}{\partial v}\Big|_{u,v} + \dfrac{\partial f}{\partial y}\Big|_{g_1, g_2}\dfrac{\partial g_2}{\partial v}\Big|_{u,v}
> \end{cases}$$

**Remarque** : avec $g(u,v) = (g_1(u,v), g_2(u,v))$, $h = f \circ g$. La propriété 7 donne les dérivées partielles de $h$ par rapport à ses variables naturelles $u$, $v$ à partir de celles de $f$ par rapport à $x$, $y$. Elle sert à résoudre les [[Équation aux dérivées partielles|équations aux dérivées partielles]] par changement de variables, seule méthode vue cette année. L'exemple explicite renvoie au poly (pages 78-79), non recopié dans la note.

## 5. Matrice de Jacobi et gradient

> **Définition 4 ([[Matrice jacobienne|matrice de Jacobi]])** : soit $f : U \to \mathbb R^n$ différentiable en $a \in U$ ($U$ ouvert de $\mathbb R^p$). La matrice jacobienne $J_f(a)$ est la matrice à $n$ lignes et $p$ colonnes de $D_af$ dans les bases canoniques :
> $$J_f(a) = \left(\left.\frac{\partial f_i}{\partial x_j}\right|_a\right) = \begin{bmatrix} \left.\frac{\partial f_1}{\partial x_1}\right|_a & \cdots & \left.\frac{\partial f_1}{\partial x_p}\right|_a \\ \vdots & & \vdots \\ \left.\frac{\partial f_n}{\partial x_1}\right|_a & \cdots & \left.\frac{\partial f_n}{\partial x_p}\right|_a \end{bmatrix}$$
> Si $n = p$, le **jacobien** de $f$ en $a$ est le [[Déterminant|déterminant]] de $J_f(a)$.

> **Définition 5 ([[Gradient]])** : pour $f : U \to \mathbb R$ différentiable en $a$, le gradient de $f$ en $a$, noté $\overrightarrow{\text{grad}}(f)(a)$ ou $\vec\nabla_af$, est
> $$\vec\nabla_af = {}^tJ_f(a) = \begin{pmatrix} \left.\frac{\partial f}{\partial x_1}\right|_a \\ \vdots \\ \left.\frac{\partial f}{\partial x_p}\right|_a \end{pmatrix}.$$

> **Propriété 8 (gradient et différentielle)** : $D_af(h) = \vec\nabla_af \cdot h$ ([[Produit scalaire|produit scalaire]]) ; le cours écrit $\forall (a, h) \in U^2$ (voir Erreurs du cours).

> **Propriété 9 (interprétation du gradient)** : le gradient d'une fonction $f : \mathbb R^n \to \mathbb R$ est perpendiculaire aux directions où $f$ est constante et pointe dans la direction où la variation de $f$ est maximale (plus grande pente). Sa norme est d'autant plus grande que la variation de $f$ au point considéré est grande.

### Inégalité des accroissements finis

On généralise le théorème des accroissements finis de $\mathbb R \to \mathbb R$ (note de cours : « accroissements finis pas vu en cours, voir si le prof va revenir dessus »).

> **Théorème 7 ([[Inégalité des accroissements finis]])** : soit $U$ un ouvert de $\mathbb R^p$, $f : U \to \mathbb R$ de classe $\mathcal C^1$, et $a, b \in U$ tels que $[a, b] = \{(1 - \lambda)a + \lambda b \mid \lambda \in [0, 1]\} \subset U$. S'il existe $M$ tel que
> $$\forall x \in [a, b],\quad \|\vec\nabla_xf\|_1 = \sum_{j=1}^p \left|\left.\frac{\partial f}{\partial x_j}\right|_x\right| \le M,$$
> alors $|f(b) - f(a)| \le M\,\|b - a\|_1$.

> **Définition 6 ([[Partie convexe]])** : $C \subset E$ est convexe si et seulement si
> $$\forall (x, y) \in C^2,\ \forall \lambda \in [0, 1],\ (1 - \lambda)x + \lambda y \in C,$$
> c'est-à-dire si tout segment joignant deux points de $C$ est contenu dans $C$.

![[Chp 4 - Calcul différentiel du premier ordre - image38.png]]
*Figure : une ellipse, convexe (le segment $[x, y]$ reste dedans), et une « cacahuète », non convexe (une partie du segment, en rouge, sort de l'ensemble).*

> **Propriété 10** : soit $U$ un ouvert **convexe** de $\mathbb R^p$ et $f : U \to \mathbb R$ de classe $\mathcal C^1$. S'il existe $M$ tel que $\|\vec\nabla_xf\|_1 \le M$ en tout point de $U$, alors $f$ est $M$-lipschitzienne sur $U$ ([[Application lipschitzienne]]).

> **Propriété 11 (fonction constante)** : soit $U$ un ouvert convexe et $f : U \to \mathbb R$ de classe $\mathcal C^1$. $f$ est constante sur $U$ si et seulement si $\vec\nabla_af = 0$ pour tout $a \in U$ :
> $$\forall j \in [\![1, p]\!],\ \forall a \in U,\ \left.\frac{\partial f}{\partial x_j}\right|_a = 0.$$
> Démonstration : $f$ constante $\iff$ $f$ 0-lipschitzienne.

## 6. Équations aux dérivées partielles du premier ordre et $\mathcal C^1$-difféomorphismes

Une [[Équation aux dérivées partielles]] généralise les équations différentielles :

| Type | Définition | Inconnue |
|---|---|---|
| Équation différentielle | lie une fonction à ses dérivées | fonction d'une seule variable |
| Équation aux dérivées partielles | lie une fonction à ses dérivées partielles | fonction de plusieurs variables |

On considère des EDP de la forme
$$F\left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, f, x, y\right) = 0,$$
où $f : \mathbb R^2 \to \mathbb R$ est inconnue.

> **Théorème 8** : soit $g : \mathbb R^2 \to \mathbb R$ continue sur un ouvert $U$. Les solutions de classe $\mathcal C^1$ sur $U$ de l'EDP
> $$\left.\frac{\partial f}{\partial x}\right|_{x,y} = g(x, y) \quad (4.4)$$
> sont de la forme
> $$f(x, y) = K(y) + \int g(x, y)\,dx,$$
> où $\int g(x,y)\,dx$ est une [[Primitive|primitive]] quelconque de $g$ par rapport à $x$, et $K$ une fonction quelconque de $\mathbb R$ dans $\mathbb R$, de classe $\mathcal C^1$ sur un ouvert de $\mathbb R$ correspondant à la projection de $U$ sur l'axe $Oy$.

> **Définition 7 ($\mathcal C^1$-difféomorphisme)** : soit $U$ un ouvert de $\mathbb R^p$ et $V$ un ouvert de $\mathbb R^n$. $\phi : U \to V$ est un $\mathcal C^1$-[[Difféomorphisme|difféomorphisme]] de $U$ dans $V$ si et seulement si :
> 1. $\phi$ est de classe $\mathcal C^1$ sur $U$ ;
> 2. $\phi$ réalise une [[Bijection|bijection]] de $U$ dans $V$ ;
> 3. $\phi^{-1}$ est de classe $\mathcal C^1$ sur $V$.

- **Propriété 12** : si $\phi$ est une application linéaire bijective de $\mathbb R^p$ dans $\mathbb R^n$, alors $p = n$ et $\phi$ est un $\mathcal C^1$-difféomorphisme.
- **Propriété 13 (caractérisation rapide)** : si $\phi : U \to V$ (1) est $\mathcal C^1$ sur $U$, (2) réalise une bijection de $U$ dans $V$, (3) a, en tout point $a$ de $U$, une différentielle $D_a\phi$ linéaire bijective de $\mathbb R^p$ dans $\mathbb R^n$, alors $p = n$ et $\phi$ est un $\mathcal C^1$-difféomorphisme de $U$ sur $V$.
- **Propriété 14** : si le jacobien de $\phi$ en $a$ est non nul, alors $D_a\phi$ est une application linéaire bijective.

### Méthode : résoudre une EDP $(E)$ par changement de variables

| Étape | Cas direct | Cas indirect |
|---|---|---|
| Changement de variables | $(x; y) = \varphi(u, v)$, $\varphi : V \to U$, $(u; v) \mapsto (x(u,v); y(u,v))$ | $(u; v) = \varphi(x, y)$, $\varphi : U \to V$, $(x; y) \mapsto (u(x,y); v(x,y))$ |
| Hypothèse | $\varphi$ est un $\mathcal C^1$-difféomorphisme (le cours écrit « de $U$ sur $V$ » pour les deux colonnes) | idem |
| Nouvelle fonction | $g = f \circ \varphi$, avec $f \in \mathcal C^1(U; \mathbb R)$, donc $g \in \mathcal C^1(V; \mathbb R)$ | $g = f \circ \varphi^{-1}$, c'est-à-dire $f = g \circ \varphi$, donc $g \in \mathcal C^1(V; \mathbb R)$ |
| Dérivation en chaîne | $\dfrac{\partial g}{\partial u} = \dfrac{\partial f}{\partial x}\dfrac{\partial x}{\partial u} + \dfrac{\partial f}{\partial y}\dfrac{\partial y}{\partial u}$ et $\dfrac{\partial g}{\partial v} = \dfrac{\partial f}{\partial x}\dfrac{\partial x}{\partial v} + \dfrac{\partial f}{\partial y}\dfrac{\partial y}{\partial v}$ | $\dfrac{\partial f}{\partial x} = \dfrac{\partial g}{\partial u}\dfrac{\partial u}{\partial x} + \dfrac{\partial g}{\partial v}\dfrac{\partial v}{\partial x}$ et $\dfrac{\partial f}{\partial y} = \dfrac{\partial g}{\partial u}\dfrac{\partial u}{\partial y} + \dfrac{\partial g}{\partial v}\dfrac{\partial v}{\partial y}$ |
| Réécrire $(E)$ | exprimer $\partial f/\partial x$ et $\partial f/\partial y$ en fonction de $\partial g/\partial u$ et $\partial g/\partial v$, puis reporter dans $(E)$. Si le changement est simple, mieux vaut souvent l'inverser et passer au cas indirect. | injecter directement $\partial f/\partial x$ et $\partial f/\partial y$ dans $(E)$ |
| Résoudre | $(E') : F\left(\dfrac{\partial g}{\partial u}; \dfrac{\partial g}{\partial v}; g; u; v\right) = 0$ | idem |
| Revenir à $x$, $y$ | avec $(u; v) = \varphi^{-1}(x, y)$, si le changement est simple à inverser | avec $(u; v) = \varphi(x, y)$ |

## 7. Changement de variables en coordonnées polaires

Les [[Coordonnées polaires]] définissent un $\mathcal C^1$-difféomorphisme sur chacun des trois demi-plans suivants.

**Demi-plan $x > 0$**, $\theta \in\, ]-\frac\pi2, \frac\pi2[$ :
$$\phi : \mathbb R_+^* \times \left]-\tfrac\pi2, \tfrac\pi2\right[ \to \mathbb R_+^* \times \mathbb R,\quad (\rho, \theta) \mapsto (\rho\cos\theta, \rho\sin\theta)$$
$$\phi^{-1}(x, y) = \left(\sqrt{x^2 + y^2},\ \arctan\tfrac yx\right)$$

![[Chp 4 - Calcul différentiel du premier ordre - image22.png]]
*Figure : demi-plan $x > 0$ hachuré, $\theta \in\, ]-\pi/2, \pi/2[$.*

**Demi-plan $x < 0$**, $\theta \in\, ]\frac\pi2, \frac{3\pi}2[$ :
$$\phi : \mathbb R_+^* \times \left]\tfrac\pi2, \tfrac{3\pi}2\right[ \to \mathbb R_-^* \times \mathbb R,\quad (\rho, \theta) \mapsto (\rho\cos\theta, \rho\sin\theta)$$
$$\phi^{-1}(x, y) = \left(\sqrt{x^2 + y^2},\ \pi + \arctan\tfrac yx\right)$$

![[Chp 4 - Calcul différentiel du premier ordre - image35.png]]
*Figure : demi-plan $x < 0$ hachuré, $\theta \in\, ]\pi/2, 3\pi/2[$.*

**Demi-plan $y > 0$**, $\theta \in\, ]0, \pi[$ :
$$\phi : \mathbb R_+^* \times\, ]0, \pi[ \to \mathbb R \times \mathbb R_+^*,\quad (\rho, \theta) \mapsto (\rho\cos\theta, \rho\sin\theta)$$
$$\phi^{-1}(x, y) = \left(\sqrt{x^2 + y^2},\ \arccos\frac{x}{\sqrt{x^2 + y^2}}\right)$$

![[Chp 4 - Calcul différentiel du premier ordre - image2.png]]
*Figure : demi-plan $y > 0$ hachuré, $\theta \in\, ]0, \pi[$.*

(Voir [[Fonctions trigonométriques réciproques]].)

## Erreurs du cours

- [[Raw/Year 2/Analyse dans Rn/Chp 4 : Calcul différentiel du premier ordre.docx|Chp 4 - Calcul différentiel du premier ordre]] écrit « si $f$ n'est que différentiable en $a$ alors les dérivées premières sont définies mais pas continues » ; il faut « pas forcément continues ».
- Théorème 5 : le cours écrit, pour $F$ un EVN quelconque, « $f, g \in \mathcal C^1(U, F) \Rightarrow f \times g \in \mathcal C^1(U, F)$ » ; il faut un espace $F$ muni d'un produit, par exemple $F = \mathbb{R}$ : sinon $f \times g$ n'a pas de sens.
- Propriété 3 : le cours écrit $D_af(h) = \sum_{i=1}^{p} h_i \left.\frac{\partial f}{\partial x_j}\right|_a$ ; il faut le même indice, $\sum_{j=1}^{p} h_j \left.\frac{\partial f}{\partial x_j}\right|_a$ (forme reprise dans cette fiche).
- Propriété 8 : le cours écrit $\forall (a, h) \in U^2$ ; il faut $a \in U$ et $h \in \mathbb{R}^p$. De même, la définition 1 écrit « Soit $a \in \mathbb{R}^p$ » ; il faut $a \in U$. La propriété 10 dit « pour tout point $a \in U$ » mais écrit sa formule en $x$.
- Propriété 11 (fonction constante) : l'énoncé se termine par « alors $f$ est $M$-lipschitzienne sur $U$ », phrase reprise de la propriété 10 ; il faut la supprimer.
- Tableau du changement de variables : le cas direct définit $\varphi : V \to U$ mais écrit « $\varphi$ est un $\mathcal C^1$-difféomorphisme de $U$ sur $V$ » ; pour ce cas, il faut « de $V$ sur $U$ ».
