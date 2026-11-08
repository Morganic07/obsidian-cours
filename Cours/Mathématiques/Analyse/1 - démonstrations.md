---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Analyse/chp7/démonstrations - integration .docx|démonstrations - integration]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Analyse/chp7/démonstrations - integration .docx|démonstrations - integration]], dans [[Cours/Mathématiques/Analyse/_index|Analyse]]. Cette note donne les preuves des énoncés de [[1 - Integration|Chap7-Integration]] (voir [[1 - Integration]]), dans le même ordre, et deux exemples de calcul de primitives trigonométriques.
Notations : $\mathcal{E}([a,b],\mathbb{R})$ désigne les fonctions en escalier ; $\mathcal{E}^-_{[a,b]}(f)$ celles qui sont $\le f$, $\mathcal{E}^+_{[a,b]}(f)$ celles qui sont $\ge f$ ; $A^\pm_{[a,b]}(f)$ l'ensemble de leurs intégrales.

## 1. Propriétés de l'intégrale d'une fonction en escalier

**Énoncé** (linéarité, [[Inégalité triangulaire]], [[Relation de Chasles]], parties réelle et imaginaire) : voir [[1 - Integration]].

**Préalable non démontré dans la note : l'intégrale ne dépend pas de la subdivision adaptée.** Ajouter un point $c$ dans $]x_i, x_{i+1}[$ coupe le terme $y_i(x_{i+1} - x_i)$ en $y_i(c - x_i) + y_i(x_{i+1} - c)$, de même somme ; par récurrence, raffiner une subdivision adaptée ne change pas la somme. Deux subdivisions adaptées ont un raffinement commun, leur réunion, qui donne donc la même somme que chacune. C'est aussi ce qui permet ci-dessus de prendre une subdivision adaptée à $f$ et à $g$ à la fois. [[Complément hors du cours|ⓘ]]

**Démonstration.** Soient $\lambda, \mu \in \mathbb{C}$, $c \in [a,b]$ et une [[Subdivision|subdivision]] $(x_0, \dots, x_n)$ adaptée à $f$ **et** à $g$, donc aussi à $\lambda f + \mu g$, $|f|$, $\mathrm{Re}(f)$, $\mathrm{Im}(f)$. Idée : la valeur de la fonction sur $]x_i, x_{i+1}[$ est sa valeur au milieu $\frac{x_i + x_{i+1}}{2}$.

(i) Linéarité :
$$\int_{[a,b]} (\lambda f + \mu g) = \sum_{i=0}^{n-1} (\lambda f + \mu g)\!\left(\tfrac{x_i + x_{i+1}}{2}\right)(x_{i+1} - x_i) = \lambda \sum_{i=0}^{n-1} f\!\left(\tfrac{x_i + x_{i+1}}{2}\right)(x_{i+1} - x_i) + \mu \sum_{i=0}^{n-1} g\!\left(\tfrac{x_i + x_{i+1}}{2}\right)(x_{i+1} - x_i) = \lambda \int_{[a,b]} f + \mu \int_{[a,b]} g.$$

(ii) Par l'inégalité triangulaire dans $\mathbb{C}$ :
$$\left| \int_{[a,b]} f \right| = \left| \sum_{i=0}^{n-1} f\!\left(\tfrac{x_i + x_{i+1}}{2}\right)(x_{i+1} - x_i) \right| \le \sum_{i=0}^{n-1} \left| f\!\left(\tfrac{x_i + x_{i+1}}{2}\right) \right|(x_{i+1} - x_i) = \int_{[a,b]} |f|.$$

(iii) Quitte à ajouter $c$ à la subdivision, on suppose $x_k = c$ pour un $k \in [\![0, n]\!]$. Alors $f_{|[a,c]}$ est en escalier de subdivision adaptée $(x_0, \dots, x_k)$, $f_{|[c,b]}$ de subdivision adaptée $(x_k, \dots, x_n)$, et on coupe la somme en $\sum_{i=0}^{k-1} + \sum_{i=k}^{n-1}$, ce qui donne $\int_{[a,c]} f + \int_{[c,b]} f$.

(iv) On sépare $f = \mathrm{Re}(f) + i\,\mathrm{Im}(f)$ dans la somme : $\int_{[a,b]} f = \int_{[a,b]} \mathrm{Re}(f) + i \int_{[a,b]} \mathrm{Im}(f)$. $\blacksquare$

## 2. Encadrement d'une fonction continue

**Énoncé.** Soit $f : [a,b] \to \mathbb{R}$ continue. Pour tout $\varepsilon > 0$, il existe $\varphi, \psi \in \mathcal{E}([a,b],\mathbb{R})$ telles que $\varphi \le f \le \psi$ et $0 \le \psi - \varphi \le \varepsilon$.

**Preuve.** Par le théorème d'approximation, il existe $\theta$ en escalier telle que $\forall x$, $|f(x) - \theta(x)| \le \frac{\varepsilon}{2}$, soit $\theta(x) - \frac{\varepsilon}{2} \le f(x) \le \theta(x) + \frac{\varepsilon}{2}$. On pose $\varphi = \theta - \frac{\varepsilon}{2}$ et $\psi = \theta + \frac{\varepsilon}{2}$.

Le théorème d'approximation lui-même n'est pas prouvé dans la note. Preuve : par le théorème de Heine, $f$ continue sur le segment $[a,b]$ y est [[Continuité uniforme|uniformément continue]] ; il existe $\delta > 0$ tel que $|x - y| \le \delta \Rightarrow |f(x) - f(y)| \le \varepsilon$. On prend une subdivision $(x_0, \dots, x_n)$ de pas $\le \delta$ et $\theta = f(x_i)$ sur $[x_i, x_{i+1}[$, $\theta(b) = f(b)$ : pour $x \in [x_i, x_{i+1}[$, $|x - x_i| \le \delta$, donc $|f(x) - \theta(x)| \le \varepsilon$. [[Complément hors du cours|ⓘ]]

![[démonstrations - integration - image6.png]]
*Figure : une fonction continue encadrée par une fonction en escalier inférieure (vert) et une supérieure (orange), à $\varepsilon$ près ; en bas, les rectangles des fonctions en escalier $\phi \le f$ et $\phi \ge f$.*

Le document définit au passage, pour $f : [a,b] \to \mathbb{R}$ **bornée quelconque** :
$$I^-(f) = \sup\left\{ \int_a^b \phi \;\middle|\; \phi \text{ en escalier},\ \phi \le f \right\}, \qquad I^+(f) = \inf\left\{ \int_a^b \phi \;\middle|\; \phi \text{ en escalier},\ \phi \ge f \right\}.$$

## 3. Existence de l'intégrale d'une fonction continue

**Énoncé.** Si $f : [a,b] \to \mathbb{R}$ est continue, $A^-_{[a,b]}(f)$ admet une borne supérieure, $A^+_{[a,b]}(f)$ une borne inférieure, et elles sont égales.

**Preuve.** $f$ continue sur un segment est bornée ; on pose $m = \inf f$ et $M = \sup f$.
1. $\mathcal{E}^-_{[a,b]}(f)$ contient la constante $m$, donc $A^-_{[a,b]}(f)$ est non vide. [[Erreurs du cours#^e-1-demonstrations|✎]] Pour tout $\varphi \in \mathcal{E}^-$, $\varphi \le f \le M$, donc $\int \varphi \le M(b-a)$ : $A^-$ est majorée, elle a une [[Borne supérieure|borne supérieure]] $\alpha$.
2. De même $A^+_{[a,b]}(f)$ est non vide et minorée par $m(b-a)$ : elle a une borne inférieure $\beta$.
3. Pour tout $(\varphi, \psi) \in \mathcal{E}^- \times \mathcal{E}^+$, $\varphi \le \psi$, donc $\int \varphi \le \int \psi$. Chaque $\int \psi$ majore $A^-$, donc $\alpha \le \int \psi$ ; $\alpha$ minore $A^+$, et $\beta$ est le plus grand minorant : $\alpha \le \beta$.
4. Soit $\varepsilon > 0$ : il existe $\varphi \in \mathcal{E}^-$, $\psi \in \mathcal{E}^+$ avec $\psi - \varphi \le \varepsilon$, d'où $\int \psi - \int \varphi \le \varepsilon(b-a)$. Comme $\int \varphi \le \alpha \le \beta \le \int \psi$ :
$$0 \le \beta - \alpha \le \varepsilon(b-a) \quad \text{pour tout } \varepsilon > 0,$$
donc $\alpha = \beta$. $\square$

## 4. Linéarité de l'intégrale

**Lemme.** Soit $\varepsilon > 0$. Si $f$ est continue et $\theta \in \mathcal{E}([a,b],\mathbb{R})$ vérifie $|f - \theta| \le \varepsilon$, alors $\left|\int_{[a,b]} f - \int_{[a,b]} \theta\right| \le (b-a)\varepsilon$.

**Preuve du lemme.** $\theta - \varepsilon \le f \le \theta + \varepsilon$, donc par définition de l'intégrale $\int (\theta - \varepsilon) \le \int f \le \int (\theta + \varepsilon)$, et par linéarité pour les fonctions en escalier on conclut.

**Preuve de la linéarité.** Soient $\theta_1, \theta_2$ en escalier avec $|f - \theta_1| \le \varepsilon$ et $|g - \theta_2| \le \varepsilon$. Par le lemme :
$$(*)\quad \left| \int f - \int \theta_1 \right| \le (b-a)\varepsilon, \qquad \left| \int g - \int \theta_2 \right| \le (b-a)\varepsilon.$$
On pose $h = \lambda f + \mu g$ et $\theta = \lambda\theta_1 + \mu\theta_2$ : $|h - \theta| \le (|\lambda| + |\mu|)\varepsilon$, donc par le lemme $\left| \int h - \int \theta \right| \le (b-a)(|\lambda| + |\mu|)\varepsilon$.
Avec $I = \int \theta = \lambda \int \theta_1 + \mu \int \theta_2$ et $(*)$ : $\left| \lambda \int f + \mu \int g - I \right| \le (b-a)(|\lambda| + |\mu|)\varepsilon$. Alors
$$\Delta = \left| \int h - \Big(\lambda \int f + \mu \int g\Big) \right| = \left| \int h - I + \Big(I - \lambda \int f - \mu \int g\Big) \right| \le \left| \int h - I \right| + \left| I - \lambda \int f - \mu \int g \right| \le 2(b-a)(|\lambda| + |\mu|)\varepsilon.$$
Vrai pour tout $\varepsilon > 0$, donc $\Delta = 0$. $\square$ (Le premier « ≤ » est l'inégalité triangulaire.) [[Erreurs du cours#^e-1-demonstrations|✎]]

## 5. Relation de Chasles

**Preuve.** Soit $\varphi \in \mathcal{E}^-_{[a,b]}(f)$. Alors $\varphi_{|[a,c]} \in \mathcal{E}^-_{[a,c]}(f)$ et $\varphi_{|[c,b]} \in \mathcal{E}^-_{[c,b]}(f)$, donc [[Erreurs du cours#^e-1-demonstrations|✎]]
$$\int_{[a,b]} \varphi = \int_{[a,c]} \varphi + \int_{[c,b]} \varphi \le \int_{[a,c]} f + \int_{[c,b]} f.$$
Ce membre de droite majore $A^-_{[a,b]}(f)$, d'où $\int_{[a,b]} f \le \int_{[a,c]} f + \int_{[c,b]} f$. En appliquant ce résultat à $-f$ (linéarité), on obtient l'inégalité inverse, donc l'égalité. $\square$

## 6. Positivité, croissance, majorations

1. $f \ge 0$ : $\varphi = 0$ est en escalier et $\varphi \le f$, donc $\int_a^b f \ge \int_a^b \varphi = 0$.
2. On applique (1) à $h = g - f \ge 0$ : $\int h \ge 0 \Rightarrow \int g \ge \int f$ par linéarité.
3. $-|f| \le f \le |f|$, donc par croissance $-\int |f| \le \int f \le \int |f|$, soit $\left|\int f\right| \le \int |f|$.
4. Il suffit d'intégrer $m \le f \le M$.

## 7. Fonction positive d'intégrale nulle

**Énoncé.** $f : [a,b] \to \mathbb{R}$ continue et positive : $\int_{[a,b]} f = 0 \iff f$ est nulle sur $[a,b]$.

**Preuve.** $\Leftarrow$ : évident. $\Rightarrow$ : par [[Preuve par contraposition|contraposition]], supposons $f(c) > 0$ pour un $c \in [a,b]$. La continuité en $c$ avec $\varepsilon = \frac{f(c)}{2}$ donne $a \le \alpha < \beta \le b$ tels que $\forall x \in [\alpha, \beta]$, $|f(x) - f(c)| \le \varepsilon$. Ainsi $f(x) \ge \frac{f(c)}{2}$ sur $[\alpha, \beta]$, et [[Erreurs du cours#^e-1-demonstrations|✎]]
$$\int_a^b f \ge \int_\alpha^\beta f \ge \int_\alpha^\beta \varepsilon\,dx = (\beta - \alpha)\varepsilon > 0.$$

## 8. Primitives et théorème fondamental

**Deux [[Primitive|primitives]] diffèrent d'une constante.** Si $F_1$ et $F_2$ sont deux primitives de $f$ sur $I$, $(F_1 - F_2)' = f - f = 0$, donc $F_1 - F_2$ est constante sur l'intervalle $I$. $\square$ [[Erreurs du cours#^e-1-demonstrations|✎]]

Le passage « dérivée nulle donc constante » vient de l'[[Inégalité des accroissements finis|inégalité des accroissements finis]] : $|h(x) - h(y)| \le \sup|h'|\cdot|x - y| = 0$ pour tous $x, y$ de l'intervalle. Il exige un intervalle : sur $\mathbb{R}^*$, la fonction égale à $0$ sur $]-\infty,0[$ et à $1$ sur $]0,+\infty[$ a une dérivée nulle sans être constante ; ainsi $\ln|x| + c_1$ (pour $x < 0$) et $\ln|x| + c_2$ (pour $x > 0$), avec $c_1 \ne c_2$, est encore une primitive de $\frac{1}{x}$ sur $\mathbb{R}^*$. [[Complément hors du cours|ⓘ]]

**Théorème fondamental de l'analyse, preuve.**
(1) $F(x) = \int_a^x f(t)\,dt$ est définie pour tout $x \in I$ car $f$ est continue sur $[a,x]$ ou $[x,a]$. Soit $x_0 \in I$ ; on montre que $F$ est [[Dérivabilité|dérivable]] en $x_0$ avec $F'(x_0) = f(x_0)$ :
$$\frac{F(x) - F(x_0)}{x - x_0} - f(x_0) = \frac{1}{x - x_0}\int_{x_0}^{x} \big(f(t) - f(x_0)\big)\,dt.$$
Par l'[[Inégalité de la moyenne|inégalité de la moyenne]] (valable aussi si $x < x_0$, d'où les valeurs absolues) : [[Erreurs du cours#^e-1-demonstrations|✎]]
$$\left|\frac{F(x) - F(x_0)}{x - x_0} - f(x_0)\right| \le \frac{1}{|x - x_0|}\left|\int_{x_0}^{x} |f(t) - f(x_0)|\,dt\right|.$$
$f$ continue en $x_0$ : $\forall \varepsilon > 0,\ \exists \alpha > 0,\ |t - x_0| \le \alpha \Rightarrow |f(t) - f(x_0)| \le \varepsilon$. Pour $|x - x_0| \le \alpha$, tout $t$ entre $x_0$ et $x$ vérifie cette inégalité, et le quotient est $\le \varepsilon$. Donc $\lim_{x \to x_0} \frac{F(x) - F(x_0)}{x - x_0} = f(x_0)$. Vrai pour tout $x_0$, et $f$ continue : $F$ est $\mathcal{C}^1$ et $F' = f$.
Unicité : si $G$ est une autre primitive nulle en $a$, $F = G + C$, et en $x = a$, $C = 0$.
(2) $h : x \mapsto F(x) - F(a)$ est dérivable, $h' = f$, $h(a) = 0$ : par unicité, $h(x) = \int_a^x f(t)\,dt$. $\square$

## 9. Dérivation d'une intégrale à bornes variables

**Énoncé** ([[Dérivation d'une intégrale à bornes variables]]) : $g(x) = \int_{u(x)}^{v(x)} f(t)\,dt$ vérifie $g'(x) = f(v(x))\,v'(x) - f(u(x))\,u'(x)$.

**Preuve.** Pour $x \in I$, $u(x), v(x) \in J$ et $J$ est un intervalle, donc $[u(x), v(x)] \subset J$ et $g(x)$ existe. $f$ continue sur $J$ a une primitive $F$ de classe $\mathcal{C}^1$, et $g(x) = F(v(x)) - F(u(x))$ : $g$ est $\mathcal{C}^1$ (différence de composées), et $g'(x) = v'(x) f(v(x)) - u'(x) f(u(x))$.

## 10. Intégration par parties et changement de variable

**[[Intégration par parties]], preuve.** $fg$ est $\mathcal{C}^1$, donc
$$\int_a^b f'g + \int_a^b fg' = \int_a^b (fg)' = \big[f(t)g(t)\big]_a^b.$$

**[[Changement de variable dans une intégrale|Changement de variable]], preuve.** Si $F$ est une primitive de $f$, $F \circ \varphi$ est une primitive de $(f \circ \varphi)\,\varphi'$, et
$$\int_{\varphi(a)}^{\varphi(b)} f(x)\,dx = F(\varphi(b)) - F(\varphi(a)) = \big[F \circ \varphi\big]_a^b = \int_a^b f(\varphi(t))\,\varphi'(t)\,dt.$$

Les deux étapes sous-entendues : $F$ existe parce que $f$ est continue sur l'intervalle $I$ (théorème fondamental), et $(F \circ \varphi)' = (F' \circ \varphi)\,\varphi' = (f \circ \varphi)\,\varphi'$ par [[Dérivation en chaîne|dérivation des fonctions composées]] ; cette dernière est continue, ce qui autorise à appliquer le théorème fondamental à droite. [[Complément hors du cours|ⓘ]]

## 11. Exemples : primitives trigonométriques

**Exemple 15 ([[Règles de Bioche]]).** Calcul de $\int \frac{\cos x\,dx}{2 - \cos^2 x}$. Avec $\omega(x) = \frac{\cos x\,dx}{2-\cos^2 x}$ :
$$\omega(\pi - x) = \frac{\cos(\pi-x)\,d(\pi-x)}{2-\cos^2(\pi-x)} = \frac{(-\cos x)(-dx)}{2-\cos^2 x} = \omega(x),$$
donc on pose $u = \sin x$, $du = \cos x\,dx$ :
$$\int \frac{\cos x\,dx}{2-\cos^2 x} = \int \frac{\cos x\,dx}{2-(1-\sin^2 x)} = \int \frac{du}{1+u^2} = \arctan(\sin x) + c.$$

**Changement de variable $t = \tan\frac{x}{2}$** (formules de la tangente de l'arc moitié) :
$$\cos x = \frac{1-t^2}{1+t^2}, \qquad \sin x = \frac{2t}{1+t^2}, \qquad \tan x = \frac{2t}{1-t^2}, \qquad dx = \frac{2\,dt}{1+t^2}.$$

D'où viennent ces formules : avec $\theta = \frac{x}{2}$, $\cos x = \cos^2\theta - \sin^2\theta$ et $\sin x = 2\sin\theta\cos\theta$ ; en divisant par $\cos^2\theta + \sin^2\theta = 1$ puis numérateur et dénominateur par $\cos^2\theta$, on obtient les expressions en $t = \tan\theta$. Pour $dx$ : sur $]-\pi, \pi[$, $x = 2\arctan t$, donc $dx = \frac{2\,dt}{1+t^2}$. Le changement n'est valable que sur un intervalle où $\frac{x}{2}$ évite $\frac{\pi}{2} + k\pi$. [[Complément hors du cours|ⓘ]]

**Exemple 16.** Calcul de $\int_{-\pi/2}^{0} \frac{dx}{1-\sin x}$. $t = \tan\frac{x}{2}$ est une bijection de $[-\frac{\pi}{2}, 0]$ sur $[-1, 0]$ :
$$\int_{-\pi/2}^{0} \frac{dx}{1-\sin x} = \int_{-1}^{0} \frac{\frac{2\,dt}{1+t^2}}{1-\frac{2t}{1+t^2}} = 2\int_{-1}^{0} \frac{dt}{1+t^2-2t} = 2\int_{-1}^{0} \frac{dt}{(1-t)^2} = 2\left[\frac{1}{1-t}\right]_{-1}^{0} = 2\left(1-\frac{1}{2}\right) = 1.$$

## 12. Sommes de Riemann

**Preuve** (cas $f$ [[Application lipschitzienne|lipschitzienne]], en particulier $f$ de classe $\mathcal{C}^1$ ; constante $K$), avec $a_k = a + k\frac{b-a}{n}$ et $R_n = \frac{b-a}{n}\sum_{k=0}^{n-1} f(a_k)$ :
$$\begin{aligned}
\left|\int_a^b f - R_n\right| &= \left|\sum_{k=0}^{n-1}\int_{a_k}^{a_{k+1}} \big(f(x) - f(a_k)\big)\,dx\right| \\
&\le \sum_{k=0}^{n-1}\int_{a_k}^{a_{k+1}} |f(x) - f(a_k)|\,dx \quad \text{(inégalité triangulaire)} \\
&\le \sum_{k=0}^{n-1}\int_{a_k}^{a_{k+1}} K|x-a_k|\,dx \le \sum_{k=0}^{n-1}\int_{a_k}^{a_{k+1}} K(a_{k+1}-a_k)\,dx \\
&= K\sum_{k=0}^{n-1}(a_{k+1}-a_k)^2 = K\frac{(b-a)^2}{n}.
\end{aligned}$$
Comme $K\frac{(b-a)^2}{n} \to 0$, par encadrement $R_n \to \int_a^b f$. $\square$ La note ne traite pas le cas continu général.

La majoration se resserre en gardant $|x - a_k|$ au lieu de le majorer par $a_{k+1} - a_k$ : $\int_{a_k}^{a_{k+1}} K(x - a_k)\,dx = \frac{K}{2}(a_{k+1} - a_k)^2$, d'où $\left|\int_a^b f - R_n\right| \le K\frac{(b-a)^2}{2n}$. [[Complément hors du cours|ⓘ]]

**Cas $f$ seulement continue.** Par le théorème de Heine, $f$ est [[Continuité uniforme|uniformément continue]] sur $[a,b]$ : pour $\varepsilon > 0$, il existe $\delta > 0$ tel que $|x - y| \le \delta \Rightarrow |f(x) - f(y)| \le \varepsilon$. Dès que $\frac{b-a}{n} \le \delta$, chaque $x \in [a_k, a_{k+1}]$ vérifie $|f(x) - f(a_k)| \le \varepsilon$, et le même calcul donne $\left|\int_a^b f - R_n\right| \le \sum_{k=0}^{n-1} \varepsilon\,(a_{k+1} - a_k) = (b-a)\,\varepsilon$. Donc $R_n \to \int_a^b f$. $\square$ [[Complément hors du cours|ⓘ]]
