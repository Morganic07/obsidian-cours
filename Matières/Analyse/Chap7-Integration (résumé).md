---
type: source
tags: [year2]
sources: ["[[Chap7-Integration]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Chap7-Integration]], dans [[Analyse (matière)]]. Le chapitre construit l'[[Intégrale]] (fonctions en escalier, puis continues), la relie aux [[Primitive|primitives]], donne les techniques de calcul et les méthodes d'approximation. En cas d'écart, le cours et ses images font foi.

## Idée générale

L'intégrale se construit d'abord pour les fonctions en escalier, puis pour les fonctions continues, en les encadrant. Le théorème fondamental la relie ensuite aux primitives, qui permettent de la calculer.

## 1. Intégrale d'une fonction en escalier

### Subdivision

**Définition.** On appelle [[Subdivision|subdivision]] $s$ d'un segment $[a,b]$ toute suite finie $s = (x_0, x_1, \dots, x_n)$ de réels tels que
$$a = x_0 < x_1 < \dots < x_n = b.$$

### Fonction en escalier

**Définition (fonction en escalier, subdivision adaptée).** Une fonction $f : [a,b] \to \mathbb{C}$ est *en escalier* s'il existe une subdivision $(x_0, \dots, x_n)$ de $[a,b]$, dite *adaptée à $f$*, telle que $f$ est constante sur $]x_i, x_{i+1}[$ pour tout $i \in [\![0, n-1]\!]$. Les valeurs aux points $x_i$ sont quelconques.

![[Chap7-Integration - image3.png]]
*Figure : fonction en escalier sur $[a,b]$, constante par paliers sur chaque $]x_i, x_{i+1}[$ ; les valeurs aux points $x_i$ (points pleins) peuvent différer des paliers.*

**Théorème (propriétés élémentaires).** Soient $f, g : [a,b] \to \mathbb{C}$ en escalier.
- Ajouter un nombre fini de points à une subdivision adaptée à $f$ donne encore une subdivision adaptée à $f$. A fortiori, la réunion d'une subdivision adaptée à $f$ et d'une subdivision adaptée à $g$ est adaptée à $f$ **et** à $g$.
- Pour tous $\lambda, \mu \in \mathbb{C}$, $\lambda f + \mu g$ est en escalier, de même que $|f|$, $\mathrm{Re}(f)$, $\mathrm{Im}(f)$ et $fg$.

### Intégrale d'une fonction en escalier

**Définition-théorème.** Soit $f : [a,b] \to \mathbb{C}$ en escalier et $(x_0, \dots, x_n)$ une subdivision adaptée. Si $y_i$ est la valeur de $f$ sur $]x_i, x_{i+1}[$, le nombre
$$\sum_{i=0}^{n-1} y_i\,(x_{i+1} - x_i)$$
ne dépend pas de la subdivision adaptée choisie. C'est l'*intégrale de $f$ sur $[a,b]$*, notée $\int_{[a,b]} f$ ou $\int_{[a,b]} f(t)\,\mathrm{d}t$.

![[Chap7-Integration - image12.png]]
*Figure : le rectangle sous le palier $y_i$ entre $x_i$ et $x_{i+1}$ a pour aire algébrique $y_i(x_{i+1} - x_i)$ (cas $f$ réelle).*

**Propriétés.** Soient $f, g : [a,b] \to \mathbb{C}$ en escalier.
1. **Linéarité** : pour tous $\lambda, \mu \in \mathbb{C}$, $\int_{[a,b]} (\lambda f + \mu g) = \lambda \int_{[a,b]} f + \mu \int_{[a,b]} g$.
2. **[[Inégalité triangulaire]]** : $\left|\int_{[a,b]} f\right| \le \int_{[a,b]} |f|$.
3. **[[Relation de Chasles]]** : pour tout $c \in [a,b]$, $\int_{[a,b]} f = \int_{[a,c]} f + \int_{[c,b]} f$.
4. **Parties réelle et imaginaire** : $\int_{[a,b]} f = \int_{[a,b]} \mathrm{Re}(f) + \mathrm{i} \int_{[a,b]} \mathrm{Im}(f)$.

## 2. Intégrale d'une fonction continue (par morceaux)

### Approximation par des fonctions en escalier

**Théorème.** Soit $f : [a,b] \to \mathbb{R}$ continue et $\varepsilon > 0$. Il existe $\theta : [a,b] \to \mathbb{R}$ en escalier telle que $\forall x \in [a,b],\ |f(x) - \theta(x)| \le \varepsilon$.

**Propriété (encadrement).** Soit $f : [a,b] \to \mathbb{R}$ continue. Pour tout $\varepsilon > 0$, il existe $\varphi, \psi \in \mathcal{E}([a,b], \mathbb{R})$ (fonctions en escalier) telles que
$$\varphi \le f \le \psi \quad \text{et} \quad 0 \le \psi - \varphi \le \varepsilon.$$

**Théorème.** Si $f : [a,b] \to \mathbb{R}$ est continue, alors
- $A^-_{[a,b]}(f) = \left\{ \int_{[a,b]} \varphi \mid \varphi \in \mathcal{E}^-_{[a,b]}(f) \right\}$ admet une [[Borne supérieure|borne supérieure]] ;
- $A^+_{[a,b]}(f) = \left\{ \int_{[a,b]} \psi \mid \psi \in \mathcal{E}^+_{[a,b]}(f) \right\}$ admet une borne inférieure ;

et ces deux bornes sont égales. ($\mathcal{E}^-$ : fonctions en escalier inférieures à $f$ ; $\mathcal{E}^+$ : supérieures à $f$.)

### Définition de l'intégrale

**Définition.** Soit $f : [a,b] \to \mathbb{R}$ [[Limite et continuité|continue]]. L'*intégrale de $f$ sur $[a,b]$* est le réel
$$\int_{[a,b]} f = \sup\left\{ \int_{[a,b]} \varphi \mid \varphi \in \mathcal{E}^{-}_{[a,b]}(f) \right\} = \inf\left\{ \int_{[a,b]} \psi \mid \psi \in \mathcal{E}^{+}_{[a,b]}(f) \right\}.$$

### Propriétés

**Linéarité.** Pour $f, g : [a,b] \to \mathbb{R}$ continues et $(\lambda, \mu) \in \mathbb{R}^2$ : $\int_{[a,b]} (\lambda f + \mu g) = \lambda \int_{[a,b]} f + \mu \int_{[a,b]} g$.

**Lemme.** Soit $\varepsilon > 0$. Si $f : [a,b] \to \mathbb{R}$ est continue et $\theta \in \mathcal{E}([a,b],\mathbb{R})$ vérifie $|f - \theta| \le \varepsilon$, alors
$$\left| \int_{[a,b]} f - \int_{[a,b]} \theta \right| \le (b-a)\,\varepsilon.$$

**Relation de Chasles.** Pour $f : [a,b] \to \mathbb{R}$ continue et $c \in [a,b]$ : $\int_{[a,b]} f = \int_{[a,c]} f + \int_{[c,b]} f$.

**Notation $\int_a^b$.** Pour $a, b$ réels quelconques (pas forcément $a < b$) et $f$ continue entre $a$ et $b$ :
- si $a < b$, $\int_a^b f(x)\,dx = \int_{[a,b]} f(x)\,dx$ ;
- si $a = b$, $\int_a^b f(x)\,dx = 0$ ;
- si $b < a$, $\int_a^b f(x)\,dx = -\int_{[b,a]} f(x)\,dx$.

Chasles et la linéarité restent alors vraies pour $a, b, c$ quelconques.

**Propriétés (positivité, croissance, majorations).** Soient $f, g : I \to \mathbb{R}$ continues sur un intervalle $I$ et $a, b \in I$.
1. $f \ge 0$ et $a \le b \Rightarrow \int_a^b f(x)\,dx \ge 0$ (positivité) ;
2. $f \le g$ et $a \le b \Rightarrow \int_a^b f \le \int_a^b g$ (croissance) ;
3. $a \le b \Rightarrow \left|\int_a^b f\right| \le \int_a^b |f|$ ;
4. si $a \le b$ et $m \le f \le M$ entre $a$ et $b$, alors $m(b-a) \le \int_a^b f(x)\,dx \le M(b-a)$.

**Remarque.** Vraie aussi si $b < a$ : $\left|\int_a^b f(x)\,dx\right| \le \left|\int_a^b |f(x)|\,dx\right|$.

### Valeur moyenne

**Définition.** La [[Inégalité de la moyenne|valeur moyenne]] d'une fonction continue $f : [a,b] \to \mathbb{R}$ est
$$\mu = \frac{1}{b-a} \int_{[a,b]} f.$$
C'est la constante $\mu$ qui vérifie $\int_{[a,b]} f = \int_{[a,b]} \mu$.

### Fonction positive d'intégrale nulle

**Propriété.** Soit $f : [a,b] \to \mathbb{R}$ continue et positive. Alors $\int_{[a,b]} f = 0$ si et seulement si $f$ est nulle sur $[a,b]$.

**Remarque (contre-exemple sans continuité).** $f(x) = 0$ sur $]0,1[$ et $f(0) = f(1) = 1$ : $f$ est positive, non nulle, mais $\int_0^1 f = 0$.

## 3. Calcul intégral

### Primitives

**Définition.** Soient $I$ un intervalle et $f : I \to \mathbb{K}$ continue. Une [[Primitive|primitive]] de $f$ est une fonction $F$ de classe $\mathcal{C}^1$ sur $I$ dont la dérivée est $f$.

**Propriété.** Deux primitives d'une même fonction sur un intervalle diffèrent d'une constante.

**Théorème fondamental de l'analyse.** Soient $I$ un intervalle de $\mathbb{R}$, $f : I \to \mathbb{K}$ continue et $a \in I$.
1. La fonction $F : x \mapsto \int_a^x f(t)\,dt$ est l'unique primitive de $f$ qui s'annule en $a$.
2. Pour toute primitive $F$ de $f$ sur $I$ : $\int_a^x f(t)\,dt = F(x) - F(a)$.

**Notations.**
- $\int f(x)\,\mathrm{d}x$ (notation de Leibniz) désigne une primitive *quelconque* de $f$, définie à une constante additive près.
- $x \mapsto \int_a^x f(t)\,\mathrm{d}t$ est la primitive de $f$ qui s'annule en $a$.

### Dérivation d'une intégrale à bornes variables

**Propriété** ([[Dérivation d'une intégrale à bornes variables]]). Soient $I, J$ deux intervalles, $u, v : I \to \mathbb{R}$ de classe $\mathcal{C}^1$ avec $u(I), v(I) \subset J$, et $f : J \to \mathbb{K}$ continue. Alors $g : x \mapsto \int_{u(x)}^{v(x)} f(t)\,dt$ est définie et de classe $\mathcal{C}^1$ sur $I$, et
$$\forall x \in I,\quad g'(x) = f(v(x))\,v'(x) - f(u(x))\,u'(x).$$

### Intégration par parties

**Propriété** ([[Intégration par parties]]). Si $f$ et $g$ sont de classe $\mathcal{C}^1$ sur $[a,b]$ à valeurs dans $\mathbb{K}$ :
$$\int_a^b f'(t)\,g(t)\,dt = \big[f(t)\,g(t)\big]_a^b - \int_a^b f(t)\,g'(t)\,dt.$$

### Changement de variable

**Propriété** ([[Changement de variable dans une intégrale]]). Soient $I$ un intervalle, $f : I \to \mathbb{K}$ continue et $\varphi : [a,b] \to I$ de classe $\mathcal{C}^1$. Alors
$$\int_{\varphi(a)}^{\varphi(b)} f(x)\,\mathrm{d}x = \int_a^b f(\varphi(t))\,\varphi'(t)\,\mathrm{d}t.$$
On a effectué le changement de variable $x = \varphi(t)$.

**Méthode.** En pratique, modifier les trois éléments :
1. la variable : $x = \varphi(t)$ ;
2. l'élément différentiel : $dx = \varphi'(t)\,dt$ ;
3. les bornes : si $t$ varie entre $a$ et $b$, $x$ varie entre $\varphi(a)$ et $\varphi(b)$.

### Parité et périodicité

**Propriété** ([[Parité et périodicité d'une intégrale]]). Soit $f : \mathbb{R} \to \mathbb{K}$ continue.
1. Si $f$ est [[Fonction périodique|périodique]] de période $T$, pour tous $a, b$ :
$$\int_a^b f(t)\,dt = \int_{a+T}^{b+T} f(t)\,dt, \qquad \int_a^{a+T} f(t)\,dt = \int_b^{b+T} f(t)\,dt.$$
2. Si $f$ est [[Fonction paire et impaire|paire]] : $\int_{-a}^{a} f = 2\int_0^a f$.
3. Si $f$ est impaire : $\int_{-a}^{a} f = 0$.

## 4. Recherche de primitives

### Tableaux de primitives usuelles

| Fonction | Primitive |
|---|---|
| $e^x$ | $e^x$ |
| $\ln x$ | $x \ln x - x$ |
| $\frac{1}{x}$ | $\ln\lvert x\rvert$ |
| $x^{\alpha}$ $(\alpha \neq -1)$ | $\frac{x^{\alpha+1}}{\alpha+1}$ |
| $\sin x$ | $-\cos x$ |
| $\cos x$ | $\sin x$ |
| $\tan x$ | $-\ln\lvert\cos x\rvert$ |

Et : $\displaystyle\int \frac{du}{u^2 + a^2} = \frac{1}{a}\arctan\left(\frac{u}{a}\right) + C$.

Fonctions trigonométriques réciproques ([[Fonctions trigonométriques réciproques]]) :

| Primitive de $f(x)$ | Fonction $f(x)$ | Dérivée de $f(x)$ |
|---|---|---|
| $x \arcsin(x) + \sqrt{1-x^2}$ | $\arcsin(x)$ | $\frac{1}{\sqrt{1-x^2}}$ |
| $x \arccos(x) - \sqrt{1-x^2}$ | $\arccos(x)$ | $-\frac{1}{\sqrt{1-x^2}}$ |
| $x \arctan(x) - \frac{1}{2}\ln(1+x^2)$ | $\arctan(x)$ | $\frac{1}{1+x^2}$ |

Formes composées ($u$ dérivable) :

| Fonction $f$ | Primitive $F$ |
|---|---|
| $k \in \mathbb{R}$ | $kx + C$ |
| $x^n,\ n \in \mathbb{N}$ | $\frac{x^{n+1}}{n+1} + C$ |
| $\frac{1}{\sqrt{x}}$ | $2\sqrt{x} + C$ |
| $\frac{1}{x^n},\ n \in \mathbb{N}^* \setminus \{1\}$ | $\frac{-1}{(n-1)x^{n-1}} + C$ |
| $u'(x)\,u^n(x),\ n \in \mathbb{N}^*$ | $\frac{u^{n+1}(x)}{n+1} + C$ |
| $\frac{u'(x)}{\sqrt{u(x)}}$ | $2\sqrt{u(x)} + C$ |
| $\frac{u'(x)}{u^n(x)},\ n \in \mathbb{N}^* \setminus \{1\}$ | $\frac{-1}{(n-1)u^{n-1}(x)} + C$ |
| $\frac{u'(x)}{u(x)}$ | $\ln\lvert u(x)\rvert + C$ |
| $e^x$ | $e^x + C$ |
| $u'(x)\,e^{u(x)}$ | $e^{u(x)} + C$ |
| $\cos x$ | $\sin x + C$ |
| $u'(x)\cos(u(x))$ | $\sin(u(x)) + C$ |
| $\sin x$ | $-\cos x + C$ |
| $u'(x)\sin(u(x))$ | $-\cos(u(x)) + C$ |

### Intégration des éléments simples

**Théorème ([[Décomposition en éléments simples]]).** Soit $\frac{P(x)}{Q(x)}$ une fraction rationnelle à coefficients réels. Elle s'écrit comme somme d'un polynôme $E(x) \in \mathbb{R}[x]$ (la *partie entière*) et d'éléments simples de la forme
$$\frac{\gamma}{(x-x_0)^k} \quad \text{ou} \quad \frac{\alpha x + \beta}{(ax^2+bx+c)^k} \text{ avec } b^2 - 4ac < 0,$$
où $\alpha, \beta, \gamma, a, b, c \in \mathbb{R}$ et $k \in \mathbb{N}\setminus\{0\}$.

**Méthode.**
1. On sait intégrer le polynôme $E(x)$.
2. Élément $\frac{\gamma}{(x-x_0)^k}$ (sur $]-\infty, x_0[$ ou $]x_0, +\infty[$) :
   - $k = 1$ : $\int \frac{\gamma\,dx}{x - x_0} = \gamma \ln|x - x_0| + c_0$ ;
   - $k \ge 2$ : $\int \frac{\gamma\,dx}{(x-x_0)^k} = \frac{\gamma}{-k+1}(x-x_0)^{-k+1} + c_0$.
3. Élément $\frac{\alpha x + \beta}{(ax^2+bx+c)^k}$ : on l'écrit
$$\frac{\alpha x + \beta}{(ax^2+bx+c)^k} = \gamma \frac{2ax+b}{(ax^2+bx+c)^k} + \delta \frac{1}{(ax^2+bx+c)^k}.$$
   - (a) $k = 1$ : $\int \frac{2ax+b}{ax^2+bx+c}\,dx = \int \frac{u'}{u} = \ln|ax^2+bx+c| + c_0$ ;
   - (b) $k \ge 2$ : $\int \frac{2ax+b}{(ax^2+bx+c)^k}\,dx = \frac{1}{-k+1}(ax^2+bx+c)^{-k+1} + c_0$ ;
   - (c) $k = 1$ : pour $\int \frac{dx}{ax^2+bx+c}$, le changement de variable $u = px+q$ ramène à $\int \frac{du}{u^2+1} = \arctan u + c_0$ ;
   - (d) $k \ge 2$ : $u = px+q$ ramène à $I_k = \int \frac{du}{(u^2+1)^k}$ ; une intégration par parties fait passer de $I_k$ à $I_{k-1}$.

**Exemple : calcul de $I_2$.** Dans $I_1 = \int \frac{du}{u^2+1}$, on pose $f = \frac{1}{u^2+1}$, $g' = 1$, donc $f' = \frac{-2u}{(u^2+1)^2}$, $g = u$ :
$$I_1 = \left[\frac{u}{u^2+1}\right] + \int \frac{2u^2\,du}{(u^2+1)^2} = \left[\frac{u}{u^2+1}\right] + 2\int \frac{u^2+1-1}{(u^2+1)^2}\,du = \left[\frac{u}{u^2+1}\right] + 2I_1 - 2I_2.$$
D'où $I_2 = \frac{1}{2} I_1 + \frac{1}{2}\frac{u}{u^2+1} + c_0$, et comme $I_1 = \arctan u$ :
$$I_2 = \int \frac{du}{(u^2+1)^2} = \frac{1}{2}\arctan u + \frac{1}{2}\frac{u}{u^2+1} + c_0.$$

### Intégration des fonctions trigonométriques

Les primitives $\int P(\cos x, \sin x)\,dx$ ou $\int \frac{P(\cos x, \sin x)}{Q(\cos x, \sin x)}\,dx$ ($P$, $Q$ polynômes) se ramènent à l'intégration d'une fraction rationnelle. Deux méthodes :
- les [[Règles de Bioche]], assez efficaces mais pas toujours applicables ;
- le changement de variable $t = \tan\frac{x}{2}$, qui marche toujours mais demande plus de calculs.

**Règles de Bioche.** On note $\omega(x) = f(x)\,dx$. Alors $\omega(-x) = -f(-x)\,dx$ et $\omega(\pi - x) = -f(\pi - x)\,dx$.
- Si $\omega(-x) = \omega(x)$ : poser $u = \cos x$.
- Si $\omega(\pi - x) = \omega(x)$ : poser $u = \sin x$.
- Si $\omega(\pi + x) = \omega(x)$ : poser $u = \tan x$.

## 5. Approximation d'intégrales, sommes de Riemann

**[[Somme de Riemann]]** d'ordre $n$ associée à $f : [a,b] \to \mathbb{R}$ (continue) :
$$\lim_{n\to+\infty} \frac{b-a}{n} \sum_{k=1}^{n} f\left(a + k\frac{b-a}{n}\right) = \int_a^b f(t)\,dt.$$

**Remarque.** Cette somme est l'intégrale de la fonction en escalier $\varphi$ qui vaut $f(a_k)$ sur $]a_k, a_{k+1}[$ pour $0 \le k \le n-1$ (avec $a_k = a + k\frac{b-a}{n}$) : c'est l'aire en bleu ci-dessous (voir point à vérifier 1).

![[Chap7-Integration - image10.png]]
*Figure : rectangles bleus de hauteur $f(a_k)$ à l'extrémité gauche de chaque intervalle.*

**Remarque.** On reconnaît la méthode des rectangles : une somme de Riemann approche bien l'intégrale pourvu que le pas soit petit. Même résultat avec
$$R'_n = \frac{b-a}{n}\sum_{k=1}^{n} f\left(a + k\frac{b-a}{n}\right) \quad \text{(rectangles « à droite »)}.$$

![[Chap7-Integration - image9.png]]
*Figure : méthode des rectangles « à droite », la hauteur de chaque rectangle est la valeur de $f$ à son extrémité droite.*

**[[Méthode des trapèzes]].** La somme de Riemann converge vers l'intégrale en $\frac{1}{n}$. Pour plus de précision, on approche $\int_{[a,b]} f$ par
$$T_n(f) = \frac{b-a}{n} \sum_{k=0}^{n-1} \frac{f(a_k) + f(a_{k+1})}{2}.$$
Si $f$ est de classe $\mathcal{C}^2$ sur $[a,b]$, l'erreur est en $\frac{1}{n^2}$ :
$$\left| \int_a^b f(x)\,dx - T_n(f) \right| \le M_2 \frac{(b-a)^3}{12n^2}, \qquad M_2 = \sup_{x \in [a,b]} |f''(x)|.$$

![[Chap7-Integration - image31.png]]
*Figure : l'aire sous la courbe découpée en trapèzes dont les sommets sont sur la courbe.*

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Somme de Riemann** : image lue directement, la formule porte sur $k = 1, \dots, n$, ce qui correspond aux rectangles à droite. La remarque suivante décrit pourtant $f(a_k)$ pour $0 \le k \le n - 1$, soit les rectangles à gauche. Les deux convergent vers l'intégrale, mais ce ne sont pas les mêmes sommes. La remarque sur $R'_n$ donne d'ailleurs exactement la même formule ($k = 1$ à $n$) que la définition, ce qui suggère que la définition devait porter sur $k = 0, \dots, n-1$.
2. **Primitive** : « La primitive de $f$ est toute fonction » devrait dire « Une primitive », puisqu'il y en a une infinité.
3. **Transcriptions** (mentions « À vérifier » reprises) : la définition de subdivision écrit « x0, x1, xn » sans indices ; le théorème d'approximation emploie $\varepsilon$ puis $\epsilon$ ; l'en-tête du tableau des fonctions trigonométriques réciproques est coupé sur l'image et a été reconstitué ; dans le tableau des formes composées, « $\mathbb{N}* - 1\}$ » a une accolade manquante, lue ici comme $\mathbb{N}^* \setminus \{1\}$.
4. Le tableau des formes composées est présent deux fois dans la note (image dupliquée).
