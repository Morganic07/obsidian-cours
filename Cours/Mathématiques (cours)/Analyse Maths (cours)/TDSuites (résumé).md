---
type: source
tags: [year1]
sources: ["[[Raw/Year 1/Analyse Maths/Exos/TDSuites.pdf|TDSuites.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé de TDSuites ([[Raw/Year 1/Analyse Maths/Exos/TDSuites.pdf|TDSuites.pdf]]) (122 diapositives, texte, « Analyse, premier semestre 2023-2024 »), dans [[Analyse Maths (index)]]. Ce sont les diapositives corrigées du TD sur les suites numériques. La numérotation compte deux exercices 15 (l'un sur les suites adjacentes, l'autre sur Cesàro). Lu par sections ; les énoncés des exercices 4, 6, 7 et 11 et deux pages de corrigé (4 f-h, 4 m) ont été relus en image. Le document ne contient aucune figure : rien n'est intégré. Notion centrale : [[Suite numérique]].

## Récapitulatif des exercices

| Ex. | Sujet | Méthode du corrigé |
|---|---|---|
| 1, 2 | Exemples de suites (croissante majorée, ni croissante ni décroissante, ni majorée ni minorée) ; propriétés « à partir d'un certain rang » en quantificateurs | $u_n = 1 - \frac1{n+1}$ (croissante, majorée par 1) ; $\exists N, \forall n \ge N, \dots$ |
| 3 | Limites par la définition ($\frac{n+1}{n+2}$, $\frac{n^2+1}{n+1}$, $-3\cdot 2^{n+1}$) | Écrire $\lvert u_n - \ell\rvert < \varepsilon$ (ou $> M$, ou $< m$), isoler $n$, puis prendre $N = E(\cdot) + 1$ |
| 4 à 7 | Calculs de limites : racines à conjuguer, $\frac{\sin n}{n}$, $(-1)^n$, sommes de fractions, $(1 + x/n)^n$, $\sqrt[n]{n^2}$, $n e^{-n}$, $E(nx)/n$, $n!/n^n$ | Quantité conjuguée, factorisation du terme dominant, encadrement et gendarmes, passage au logarithme pour $(1+x/n)^n$ (indication $\ln(1+t)/t \to 1$), croissances comparées. Pour $a^n - b^n \over a^n + b^n$ : trois cas $a = b$, $a > b$, $a < b$ |
| 8 | $\frac{E(x) + E(2x) + \dots + E(nx)}{n^2}$ ; $\mathbb{Q}$ dense dans $\mathbb{R}$ | Encadrement $kx - 1 < E(kx) \le kx$, somme, gendarmes : la limite est $x/2$ ; la densité s'en déduit |
| 9 | Vrai ou faux (limites, sommes, produits) | Contre-exemples : $(-1)^n$ pour la somme et le produit de suites divergentes ; $x_n = (1 + (-1)^n)/2$, $y_n = (1 - (-1)^n)/2$ pour $x_n y_n \to 0$ sans que l'un des deux tende vers 0 |
| 11 | Divergence de $n\sin(n\pi/2)$, etc. | Deux sous-suites de limites différentes |
| 12 | $(u_{2n})$, $(u_{3n})$, $(u_{2n+1})$ convergent, donc $(u_n)$ converge | $(u_{6n})$ est extraite de $(u_{2n})$ et de $(u_{3n})$ : les limites coïncident ; $(u_{6n+3})$ relie $u_{2n+1}$ et $u_{3n}$ ; les indices pairs et impairs recouvrent $\mathbb{N}$ |
| 13 | Critère $u_{n+1}/u_n \to l$ : $l < 1$ donne limite 0, $l > 1$ donne $+\infty$, $l = 1$ indéterminé | Comparer à une suite géométrique ; applications à $a^n/n!$ etc. Voir [[Critère de d'Alembert et de Cauchy]] |
| 14, 15 | Suites adjacentes : $\sum 1/\sqrt k - 2\sqrt{n+1}$ et $\sum 1/\sqrt k - 2\sqrt n$ ; série alternée $\sum (-1)^{k-1}/k$ | Montrer $(u_n)$ croissante, $(v_n)$ décroissante, $v_n - u_n \to 0$ ; pour l'alternée, les suites paire et impaire sont adjacentes. Voir [[Série numérique]] |
| 16 | Deux suites imbriquées ($\frac{u + 2v}{3}$, $\frac{u + 3v}{4}$) | $w_n = v_n - u_n$ géométrique ; $t_n = 3u_n + 8v_n$ est constante, ce qui donne la limite commune |
| 17 | Si $u_n \to l$ et $a < l$, alors $u_n > a$ à partir d'un rang | Prendre $\varepsilon < l - a$ |
| 18 à 21 | Suites récurrentes $u_{n+1} = f(u_n)$ ($\sqrt{u_n + 1}$, $\frac1{u_n} + 1$, $3 - \sqrt{u_n/2}$, $1 + 2/u_n$, $\frac12 u(u^2 - 3u + 4)$) | Intervalle stable par $f$, monotonie de $f$, points fixes ; $f$ croissante donne une suite monotone ; $f$ décroissante donne deux suites extraites (paire et impaire) monotones de sens contraires ; signe de $f(x) - x$ et cas selon $u_0$ |
| 22 à 24 | Suites complexes (module, partie réelle et imaginaire), $z_{n+1} = \frac13(2z_n - \bar z_n)$, relation de récurrence entre $z_n$ et $z_{n+1}$ | Passer au module ou séparer $\mathrm{Re}$ et $\mathrm{Im}$. Voir [[Nombre complexe]] |
| 25 (Cesàro) | Si $u_n \to l$, la moyenne $\frac1n\sum u_k \to l$ ; réciproque fausse ; cas $+\infty$ | Découper la somme à un rang $N$ fixé |
| 26 | Constante d'Euler : $\frac1{n+1} \le \ln(n+1) - \ln n \le \frac1n$, $\ln(n+1) \le H_n \le 1 + \ln n$, $H_n - \ln n$ décroissante positive donc convergente | Comparaison série-intégrale pour la fonction $1/x$ décroissante. La limite $\gamma \approx 0{,}5772$ : on ignore si elle est rationnelle |
| 27 | $z_n = a^n$ avec $a \in \mathbb{C}$ | $\lvert a\rvert < 1$ : limite nulle ; $\lvert a\rvert > 1$ : module infini, divergence ; $\lvert a\rvert = 1$ : cas selon $\theta/2\pi$ |

## Théorèmes utilisés dans le corrigé

Le TD cite ou rappelle ces résultats (énoncés tels que les diapositives les donnent) :

- **Théorème d'encadrement** ([[Théorème des gendarmes]]) : si $a_n \le u_n \le b_n$ et $a_n, b_n \to \ell$, alors $u_n \to \ell$.
- **Théorème de composition à gauche par une fonction** : si $u_n \to a$ et $f(t) \to b$ quand $t \to a$, alors $f(u_n) \to b$ ([[Composition de fonctions]], [[Caractérisation séquentielle de la limite]]).
- **Produit d'une suite bornée et d'une suite de limite nulle** : si $(u_n)$ est bornée et $v_n \to 0$, alors $u_n v_n \to 0$.
- **Caractérisation séquentielle de la densité** : $A \subset \mathbb{R}$ est dense dans $\mathbb{R}$ si et seulement si tout réel est limite d'une suite d'éléments de $A$.
- **Suites extraites** ([[Suite extraite]]) : toute suite extraite d'une suite convergente de limite $L$ converge vers $L$. Si $(v_{2n})$ et $(v_{2n+1})$ convergent vers la même limite $\ell$, alors $v_n \to \ell$.
- **[[Suites adjacentes]]** : une suite croissante et une suite décroissante dont la différence tend vers 0 convergent vers la même limite.
- **Théorème sur les suites récurrentes** $u_{n+1} = f(u_n)$, $f$ définie sur un [[Intervalle stable|intervalle stable]] : si $f$ est croissante, $(u_n)$ est monotone ; si $f$ est décroissante, $(u_{2n})$ et $(u_{2n+1})$ sont monotones de sens contraires ; si $(u_n)$ converge et $f$ est continue, la limite est un [[Point fixe|point fixe]] de $f$.
- **[[Théorème de la limite monotone]]** : une suite monotone a une limite (finie si elle est bornée).
- **Suites complexes** ([[Suite complexe]]) : $(u_n)$ converge si et seulement si $(\mathrm{Re}(u_n))$ et $(\mathrm{Im}(u_n))$ convergent, et alors $\lim u_n = \lim \mathrm{Re}(u_n) + i \lim \mathrm{Im}(u_n)$. De plus $u_n \to \ell \iff |u_n - \ell| \to 0$ ; en particulier $u_n \to 0 \iff |u_n| \to 0$.

## Exercice 1 — exemples de suites

Donner un exemple de suite (1) croissante et majorée ; (2) ni croissante ni décroissante ; (3) ni majorée ni minorée. Le corrigé précise que ces exemples ne sont pas les seuls.

1. $u_n = 1 - \frac{1}{n+1}$. Alors $u_{n+1} - u_n = \frac{1}{n+1} - \frac{1}{n+2} = \frac{1}{(n+1)(n+2)} > 0$ : croissante. Et $-\frac1{n+1} < 0 \Rightarrow u_n < 1$ : majorée.
2. $u_n = \sin\left(\frac{n\pi}{2}\right)$, qui vaut $1$ si $n = 1 + 4k$, $0$ si $n = 2k$, $-1$ si $n = 3 + 4k$ : ni croissante ni décroissante.
3. $u_n = n$ si $n$ pair, $-n$ si $n$ impair : $u_{2k} \to +\infty$ et $u_{2k+1} \to -\infty$, ni majorée ni minorée ([[Majorant et minorant]]).

## Exercice 2 — quantificateurs

Écrire avec des [[Quantificateur|quantificateurs]] :
1. $(u_n)$ positive à partir d'un certain rang : $\exists N \in \mathbb{N}, \forall n \ge N, u_n \ge 0$.
2. $(u_n)$ constante à partir d'un certain rang : $\exists N \in \mathbb{N}, \forall n \ge N, u_n = u_N$.
3. $(u_n)$ croissante à partir d'un certain rang : $\exists N \in \mathbb{N}, \forall n \ge N, u_{n+1} \ge u_n$.

## Exercice 3 — limites par la définition

Déterminer les limites en revenant à la définition ([[Convergence d'une suite]]).

**(a) $u_n = \frac{n+1}{n+2}$.** Calcul : $\frac{n(1 + 1/n)}{n(1 + 2/n)} \to 1$. Définition : $\forall \varepsilon > 0, \exists N, \forall n \ge N, |u_n - 1| < \varepsilon$. On a
$$|u_n - 1| < \varepsilon \iff \frac{1}{n+2} < \varepsilon \iff \frac1\varepsilon - 2 < n.$$
On pose $N = E\left(\frac1\varepsilon - 2\right) + 1$ ([[Partie entière]]) : pour $n \ge N$, $|u_n - 1| < \varepsilon$, donc $u_n \to 1$.

**(b) $v_n = \frac{n^2+1}{n+1}$.** Calcul : $\frac{n + 1/n}{1 + 1/n} \to +\infty$. Définition : $\forall M > 0, \exists N, \forall n \ge N, v_n > M$. Comme $n^2 + 1 > n^2 - 1$, $\frac{n^2+1}{n+1} > \frac{(n-1)(n+1)}{n+1} = n - 1$ ; il suffit donc que $n - 1 > M$, soit $n > M + 1$. On pose $N = E(M + 1) + 1$.

**(c) $w_n = -3 \cdot 2^{n+1}$.** Calcul : $-6 \lim 2^n = -\infty$. Définition : $\forall m < 0, \exists N, \forall n \ge N, w_n < m$.
$$-3 \cdot 2^{n+1} < m \iff 2^{n+1} > -\frac m3 \iff (n+1)\ln 2 > \ln\left(-\frac m3\right) \iff n > \frac{\ln(-m/3)}{\ln 2} - 1.$$
On pose $N = E\left(\frac{\ln(-m/3)}{\ln 2} - 1\right) + 1$.

## Exercice 4 — calculs de limites

Énoncé : déterminer, si elles existent, les limites de

| | Suite | Limite (corrigé) | Méthode |
|---|---|---|---|
| a) | $\dfrac{10^{92} n^2}{n + n^3}$ | $0$ | Factoriser $n^3$ : $10^{92}\,\frac{1/n}{1/n^2 + 1}$ |
| b) | $\sqrt{n+2} - \sqrt n$ | $0$ | [[Quantité conjuguée]] : $\frac{2}{\sqrt{n+2} + \sqrt n}$ |
| c) | $\dfrac{\sqrt n \sin n}{n + \sqrt n}$ | $0$ | $= \frac{\frac{1}{\sqrt n}\sin n}{1 + \frac1{\sqrt n}}$ |
| d) | $\sqrt{n + \sqrt n} - \sqrt n$ | $\frac12$ | Conjuguée : $\frac{\sqrt n}{\sqrt{n + \sqrt n} + \sqrt n} = \frac{1}{\sqrt{1 + 1/\sqrt n} + 1}$ |
| e) | $\sqrt{n^2 + n + 1} - \sqrt{n^2 + 1}$ | $\frac12$ | Conjuguée : $\frac{n}{\sqrt{n^2+n+1} + \sqrt{n^2+1}}$, puis factoriser $n$ |
| f) | $\dfrac{(-1)^n + n}{n + 7\sqrt n}$ | $1$ | $= \frac{(-1)^n/n + 1}{1 + 7/\sqrt n}$ |
| g) | $\dfrac{(-3)^n + 7^n}{2^n + 5^n}$ | $+\infty$ | $= \left(\frac75\right)^n \cdot \frac{(-3/7)^n + 1}{(2/5)^n + 1} \to (+\infty)\cdot 1$ |
| h) | $\dfrac{n^2 + \cos n}{\sin(n) - 3n^2}$ | $-\frac13$ | $= \frac{1 + \cos n / n^2}{\sin n / n^2 - 3}$ |
| i) | $\dfrac{1}{n^2} + \dfrac{2}{n^2} + \dots + \dfrac{n}{n^2}$ | $\frac12$ | $= \frac{1 + \dots + n}{n^2} = \frac{n(n+1)}{2n^2} = \frac{n+1}{2n}$ |
| j) (à faire chez soi) | $\sqrt{n+1} - \sqrt n$ | $0$ | Conjuguée : $\frac{1}{\sqrt{n+1} + \sqrt n}$ |
| k) (chez soi) | $\dfrac{\sqrt n - 1}{\sqrt n + 1}$ | $1$ | $= 1 - \frac{2}{\sqrt n + 1}$ |
| l) (chez soi) | $\dfrac{2^n - 3^{n+1}}{5^{2n}}$ | $0$ | $= \left(\frac{2}{25}\right)^n - 3\left(\frac{3}{25}\right)^n$ |
| m) (chez soi) | $\sqrt{n^2 + 2n + 3} - \sqrt{n^2 + n + 1}$ | $\frac12$ | Conjuguée : $\frac{n+2}{\sqrt{n^2+2n+3} + \sqrt{n^2+n+1}} = \frac{1 + 2/n}{\sqrt{1 + 2/n + 3/n^2} + \sqrt{1 + 1/n + 1/n^2}}$ |

## Exercice 5 — deux suites à paramètres

**(1) $u_n = \frac{a^n - b^n}{a^n + b^n}$, $a, b > 0$.** Trois cas :
- $a = b$ : $u_n = 0$ pour tout $n$, limite $0$ ;
- $a > b$ : $u_n = \frac{1 - (b/a)^n}{1 + (b/a)^n}$ avec $0 < b/a < 1$, donc $(b/a)^n \to 0$ et $u_n \to 1$ ;
- $b > a$ : $u_n = \frac{(a/b)^n - 1}{(a/b)^n + 1} \to -1$.

**(2) $u_n = 1 + a + a^2 + \dots + a^n$, $a > 0$** ([[Suite géométrique]]) :
$$u_n = \begin{cases} n + 1 & a = 1 \\ \dfrac{a^{n+1} - 1}{a - 1} & a \ne 1 \end{cases} \qquad \lim a^n = \begin{cases} +\infty & a > 1 \\ 0 & 0 \le a < 1 \end{cases}$$
d'où $\lim u_n = +\infty$ si $a \ge 1$, et $\lim u_n = \frac{1}{1-a}$ si $0 \le a < 1$.

## Exercice 6 — limites par composition

Énoncé : (1) $\lim \left(1 + \frac xn\right)^n$, $x \in \mathbb{R}$, avec l'indication $\lim_{t \to 0} \frac{\ln(1+t)}{t} = 1$ ; (2) $\lim \sqrt[n]{n^2}$ ; (3) $\lim \sin\left(\frac{n^2 + 2n + 3}{n+1}\pi\right)$. À faire chez soi : (a) $n^{1/n}$ ; (b) $\ln\left(\frac{1+n}{n^2}\right)$.

**(1)** Si $x = 0$, la suite vaut 1. Si $x \ne 0$ :
$$\left(1 + \frac xn\right)^n = \exp\left(n \ln\left(1 + \frac xn\right)\right) = \exp\left(x \cdot \frac{\ln(1 + x/n)}{x/n}\right).$$
Comme $x/n \to 0$ et $\frac{\ln(1+t)}{t} \to 1$, la composition à gauche donne $x \cdot \frac{\ln(1 + x/n)}{x/n} \to x$, puis, par continuité de $\exp$ :
$$\lim_{n \to +\infty} \left(1 + \frac xn\right)^n = e^x.$$

**(2)** $\sqrt[n]{n^2} = \exp\left(\frac2n \ln n\right)$. Il suffit de montrer $\frac{\ln n}{n} \to 0$ :
- pour $x > 0$, $x < e^x$, donc $\ln x < x$ ;
- $\ln n = 2\ln\sqrt n < 2\sqrt n$, d'où $0 \le \frac{\ln n}{n} < \frac{2}{\sqrt n}$ ;
- par encadrement, $\frac{\ln n}{n} \to 0$, et par composition $\sqrt[n]{n^2} \to e^0 = 1$.

**(3)** $\frac{n^2 + 2n + 3}{n+1} = (n+1) + \frac{2}{n+1}$, donc
$$\sin\left(\frac{n^2+2n+3}{n+1}\pi\right) = \sin\left((n+1)\pi + \frac{2\pi}{n+1}\right) = \cos((n+1)\pi)\,\sin\left(\frac{2\pi}{n+1}\right).$$
Or $\sin\frac{2\pi}{n+1} \to 0$ et $-1 \le \cos((n+1)\pi) \le 1$ : par encadrement, la limite est $0$.

**(a, chez soi)** $n^{1/n} = \exp\left(\frac{\ln n}{n}\right) \to 1$.
**(b, chez soi)** $\frac{1+n}{n^2} \to 0^+$ et $\ln x \to -\infty$ quand $x \to 0^+$, donc $\ln\frac{1+n}{n^2} \to -\infty$.

## Exercice 7 — encadrements

Énoncé : (a) $n e^{-n}$ ; (b) $\frac1n + \frac{1}{n + \sqrt1} + \dots + \frac{1}{n + \sqrt n}$ ; (c) $\frac{E(nx)}{n}$ ; (d) $(\sqrt{n+1} - \sqrt n)\cos(e^n)$ ; (e) $\frac{n!}{n^n}$.

**(a)** De $x < e^x$ avec $x = n/2$ : $\frac n2 < e^{n/2}$, donc $\frac{n^2}{4} < e^n$, et $0 < \frac{n}{e^n} < \frac4n$. Par encadrement, $n e^{-n} \to 0$ ([[Croissances comparées]]).

**(b)** Pour $0 \le k \le n$ : $\frac{1}{n + \sqrt n} \le \frac{1}{n + \sqrt k} \le \frac1n$. En sommant les $n + 1$ termes :
$$\frac{n+1}{n + \sqrt n} \le u_n \le \frac{n+1}{n},$$
et les deux bornes tendent vers 1 : $u_n \to 1$.

**(c)** $nx - 1 < E(nx) \le nx$, donc $x - \frac1n < \frac{E(nx)}{n} \le x$ : la limite est $x$.

**(d)** Méthode 1 : $-(\sqrt{n+1} - \sqrt n) \le u_n \le \sqrt{n+1} - \sqrt n$, et $\sqrt{n+1} - \sqrt n \to 0$, donc $u_n \to 0$. Méthode 2 : $(\cos(e^n))$ est bornée et $\sqrt{n+1} - \sqrt n \to 0$ : produit d'une suite bornée et d'une suite de limite nulle.

**(e)** Pour $n > 2$ : $n! = 1 \times 2 \times 3 \times \dots \times n < 1 \times 2 \times \underbrace{n \times \dots \times n}_{n-2 \text{ fois}} = 2n^{n-2}$, donc $0 < \frac{n!}{n^n} < \frac{2}{n^2} \to 0$.

## Exercice 8 — sommes de parties entières, densité de $\mathbb{Q}$

Soit $x \in \mathbb{R}$. (1) Limite de $u_n = \frac{E(x) + E(2x) + \dots + E(nx)}{n^2}$. (2) En déduire que $\mathbb{Q}$ est dense dans $\mathbb{R}$.

**(1)** Pour tout $k$, $kx - 1 < E(kx) \le kx$. En sommant pour $k = 1, \dots, n$ :
$$x\frac{n(n+1)}{2n^2} - \frac1n < u_n \le x\frac{n(n+1)}{2n^2},$$
et les deux bornes tendent vers $\frac x2$ : $u_n \to \frac x2$.

**(2)** Posons $v_n = 2u_n$. Pour tout $n$, $v_n \in \mathbb{Q}$ (somme d'entiers divisée par $n^2$), et $v_n \to x$. Tout réel est donc limite d'une suite de rationnels : par la caractérisation séquentielle, $\mathbb{Q}$ est dense dans $\mathbb{R}$ ([[Densité de ℚ dans ℝ]]).

## Exercice 9 — vrai ou faux

Démontrer la propriété si elle est vraie, donner un [[Preuve par contre-exemple|contre-exemple]] sinon.

| # | Propriété | Réponse | Justification du corrigé |
|---|---|---|---|
| 1 | Si $u_n < v_n$ et $v_n \to 0$, alors $u_n \to 0$ | Faux | $u_n = -2 + \frac1n$, $v_n = \frac1n$ : $u_n < v_n$ mais $u_n \to -2$ |
| 2 | Une suite non majorée tend vers $+\infty$ | Faux | $u_n = n$ si $n$ pair, $-n$ si $n$ impair |
| 3 | Si $u_n \to l$, alors $\forall p$, $u_{n+p} - u_n \to 0$ | Vrai | Pour $n > N$ (rang associé à $\varepsilon/2$) : $\lvert u_{n+p} - u_n\rvert \le \lvert u_{n+p} - l\rvert + \lvert l - u_n\rvert < \varepsilon$ ([[Inégalité triangulaire]]) |
| 4 | $(x_n)$, $(y_n)$ divergentes $\Rightarrow$ $(x_n + y_n)$ diverge | Faux | $y_n = -x_n$ ; par exemple $n$ et $-n$, de somme nulle |
| 5 | $(x_n)$, $(y_n)$ divergentes $\Rightarrow$ $(x_n y_n)$ diverge | Faux | $x_n = 1$ si $n$ pair, $-1$ sinon ; $y_n = -1$ si $n$ pair, $1$ sinon : $x_n y_n = -1$ |
| 6 | Pour toute $(y_n)$, si $x_n \to 0$ alors $x_n y_n \to 0$ | Faux | $x_n = \frac1n$, $y_n = n^a$ avec $a > 1$ : $x_n y_n = n^{a-1} \to +\infty$ |
| 7 | Si $x_n y_n \to 0$, alors $x_n \to 0$ ou $y_n \to 0$ | Faux | $x_n = \frac{1 + (-1)^n}{2}$, $y_n = \frac{1 - (-1)^n}{2}$ : $x_n y_n = \frac{1 - (-1)^{2n}}{4} = 0$, mais ni $x_n$ ni $y_n$ n'ont de limite |
| 8 | $(u_n)$ convergente à termes $> 0$ $\Rightarrow$ limite $> 0$ | Faux | $u_n = \frac1n \to 0$ |
| 9 | $(u_n)$ croissante et $u_n \le 7$ $\Rightarrow$ $u_n \to 7$ | Faux | $u_n = m - \frac1n$ avec $m < 7$ : limite $m < 7$ |

## Exercice 11 — divergence par sous-suites

Méthode : exhiber deux suites extraites de limites différentes.

1. $a_n = n\sin\left(\frac{n\pi}{2}\right)$ : avec $\varphi_1(n) = 2n$, $a_{2n} = 2n\sin(n\pi) = 0 \to 0$ ; avec $\varphi_2(n) = 1 + 4n$, $a_{1+4n} = (1+4n)\sin\left(\frac\pi2 + 2n\pi\right) = 1 + 4n \to +\infty$.
2. $b_n = \frac{(-1)^n n^3 + 3n^2 + 5}{2 - 5n^3}$ : $b_{2n} = \frac{(2n)^3 + 3(2n)^2 + 5}{2 - 5(2n)^3} \to -\frac15$ ; $b_{2n+1} = \frac{-(2n+1)^3 + 3(2n+1)^2 + 5}{2 - 5(2n+1)^3} \to \frac15$.
3. $c_n = (-1)^n \frac{n}{1+n}\cos\left(\frac{n\pi}{7}\right)$ : $c_{7n} = (-1)^{7n}\frac{7n}{1+7n}\cos(n\pi) = (-1)^{8n}\frac{7n}{1+7n} \to 1$ ; $c_{14n+1} = -\frac{14n+1}{2+14n}\cos\left(\frac\pi7 + 2n\pi\right) \to -\cos\frac\pi7$.

(L'exercice 10 n'apparaît pas dans le document.)

## Exercice 12 — trois suites extraites

On suppose que $(u_{2n})$, $(u_{3n})$ et $(u_{2n+1})$ convergent, de limites $\ell$, $\ell''$ et $\ell'$. Montrer que $(u_n)$ converge.

1. $(u_{6n})$ est extraite de $(u_{2n})$ et de $(u_{3n})$ : $\ell = \ell''$.
2. $(u_{6n+3})$ est extraite de $(u_{2n+1})$ et de $(u_{3n})$ : $\ell' = \ell''$.
3. Donc $\lim u_{2n} = \lim u_{2n+1}$, et par le théorème des suites paire et impaire, $(u_n)$ converge.

## Exercice 13 — critère du rapport

Soit $(u_n)$ à termes strictement positifs, avec $\frac{u_{n+1}}{u_n} \to \ell \in [0, +\infty]$. Voir [[Critère de d'Alembert et de Cauchy]].

**1. Si $\ell < 1$, alors $u_n \to 0$.** Posons $\varepsilon = \frac{1 - \ell}{2}$. Il existe $N$ tel que, pour $n \ge N$, $\left|\frac{u_{n+1}}{u_n} - \ell\right| \le \frac{1 - \ell}{2}$, donc $\frac{u_{n+1}}{u_n} \le \frac{1 + \ell}{2} < 1$. En écrivant $u_n = u_N \prod_{k=N}^{n-1} \frac{u_{k+1}}{u_k}$ :
$$|u_n| \le |u_N|\left(\frac{1+\ell}{2}\right)^{n-N} \to 0,$$
et par encadrement $u_n \to 0$.

**2. Si $\ell > 1$, alors $u_n \to +\infty$.** Avec $\varepsilon = \frac{\ell - 1}{2}$, pour $n > N$ : $1 < \frac{1 + \ell}{2} \le \frac{u_{n+1}}{u_n} \le \frac{3\ell - 1}{2}$. Donc $u_n \ge |u_N|\left(\frac{1+\ell}{2}\right)^{n-N} \to +\infty$.

**3. Si $\ell = 1$, on ne peut pas conclure.** $u_n = n$ : rapport $\to 1$, suite divergente. $v_n = \frac{1}{n+1}$ : rapport $\frac{n+1}{n+2} \to 1$ (le corrigé écrit $\frac{n}{n+1}$), suite convergente vers 0.

**4. Applications.**

| Suite | Rapport $\frac{u_{n+1}}{u_n}$ | Conclusion |
|---|---|---|
| $u_n = \frac{a^n}{n!}$, $a > 0$ | $\frac{a}{n+1} \to 0 < 1$ | $u_n \to 0$ |
| $v_n = \frac{n^n}{n!}$ | $\left(\frac{n+1}{n}\right)^n = \left(1 + \frac1n\right)^n \to e > 1$ | $v_n \to +\infty$ |
| $w_n = \frac{a^n}{n^p}$, $a > 1$, $p \in \mathbb{N}$ | $a\left(\frac{n}{n+1}\right)^p \to a > 1$ | $w_n \to +\infty$ |
| $z_n = \sqrt[n]{a}$, $a > 0$ | $a^{\frac{1}{n+1} - \frac1n} = a^{\frac{-1}{n(n+1)}} \to 1$ | Critère inopérant ; $z_n = \exp\left(\frac{\ln a}{n}\right) \to 1$ |

## Exercice 14 — suites adjacentes avec racines

$u_n = \sum_{k=1}^n \frac{1}{\sqrt k} - 2\sqrt{n+1}$ et $v_n = \sum_{k=1}^n \frac{1}{\sqrt k} - 2\sqrt n$. Montrer qu'elles convergent vers la même limite.

Méthode : montrer qu'elles sont adjacentes.
- $u_{n+1} - u_n = \frac{1}{\sqrt{n+1}} - 2\sqrt{n+2} + 2\sqrt{n+1} = \frac{2n + 3 - 2\sqrt{(n+2)(n+1)}}{\sqrt{n+1}} > 0$, car $(2n+3)^2 = 4n^2 + 12n + 9 > 4n^2 + 12n + 8 = 4(n+2)(n+1)$ : $(u_n)$ croissante.
- $v_{n+1} - v_n = \frac{1}{\sqrt{n+1}} - 2\sqrt{n+1} + 2\sqrt n = \frac{-1 - 2n + 2\sqrt{n(n+1)}}{\sqrt{n+1}} < 0$, car $4n^2 + 4n < 4n^2 + 4n + 1$ : $(v_n)$ décroissante.
- $v_n - u_n = 2(\sqrt{n+1} - \sqrt n) \to 0$.

Les deux suites sont adjacentes, donc convergent vers la même limite.

## Exercice 15 — série harmonique alternée

$u_n = \sum_{k=1}^n \frac{(-1)^{k-1}}{k}$. Montrer que $(u_{2n})$ et $(u_{2n+1})$ sont adjacentes ; en déduire que $(u_n)$ converge ([[Série numérique]], [[Critère des séries alternées]]).

- $u_{2n+2} - u_{2n} = \frac{1}{2n+1} - \frac{1}{2n+2} > 0$ : $(u_{2n})$ croissante.
- $u_{2n+3} - u_{2n+1} = \frac{1}{2n+3} - \frac{1}{2n+2} < 0$ : $(u_{2n+1})$ décroissante.
- $u_{2n+1} - u_{2n} = \frac{1}{2n+1} \to 0$.

Les suites paire et impaire sont adjacentes, de même limite : $(u_n)$ converge.

## Exercice 16 — deux suites imbriquées

$u_0 = 1$, $v_0 = 12$, $u_{n+1} = \frac{u_n + 2v_n}{3}$, $v_{n+1} = \frac{u_n + 3v_n}{4}$.

1. $w_n = v_n - u_n$ : $w_{n+1} = \frac{u_n + 3v_n}{4} - \frac{u_n + 2v_n}{3} = \frac{v_n - u_n}{12} = \frac{1}{12}w_n$. Suite géométrique de raison $\frac1{12}$ : $w_n = \frac{11}{12^n} \to 0$.
2. $u_{n+1} = u_n + \frac{2w_n}{3} = u_n + \frac{22}{3 \cdot 12^n}$, donc $(u_n)$ croissante ; de même $v_{n+1} - v_n = -\frac{11}{4 \cdot 12^n} < 0$, $(v_n)$ décroissante ; et $v_n - u_n = w_n \ge 0$.
3. $(u_n)$ et $(v_n)$ sont adjacentes : elles convergent vers une même limite $\ell$.
4. $t_n = 3u_n + 8v_n$ : avec $u_n = u_{n+1} - \frac{22}{3\cdot 12^n}$ et $v_n = v_{n+1} + \frac{11}{4 \cdot 12^n}$, on obtient $t_n = 3u_{n+1} + 8v_{n+1} = t_{n+1}$. $(t_n)$ est constante : $t_n = 3 + 8 \cdot 12 = 99$.
5. $99 = \lim t_n = 3\ell + 8\ell = 11\ell$, donc $\ell = 9$ : $\lim u_n = \lim v_n = 9$.

## Exercice 17 — minoration à partir d'un rang

Si $u_n \to l$ et $a < l$, il existe $N$ tel que $n \ge N \Rightarrow u_n > a$.

Choisir $\varepsilon > 0$ avec $\varepsilon < l - a$, c'est-à-dire $a < l - \varepsilon$. Par définition de la limite, il existe $N$ tel que pour $n > N$, $|u_n - l| \le \varepsilon$, donc $l - \varepsilon \le u_n$. D'où $a < l - \varepsilon \le u_n$.

## Exercices 18 à 21 — suites récurrentes $u_{n+1} = f(u_n)$

### Méthode générale (d'après les corrigés)

1. Étudier $f$ : sens de variation (signe de $f'$).
2. Trouver un intervalle stable $I$ ($f(I) \subset I$) contenant $u_0$ ; alors tous les $u_n$ sont dans $I$ (par récurrence, [[Récurrence]]).
3. Chercher les points fixes de $f$ (ou de $f \circ f$) dans $I$.
4. Si $f$ est croissante : $(u_n)$ est monotone, de sens donné par le signe de $u_1 - u_0 = f(u_0) - u_0$ ; la comparer au point fixe (bornée), conclure par le théorème de la limite monotone, et identifier la limite à un point fixe.
5. Si $f$ est décroissante : $(u_{2n})$ et $(u_{2n+1})$ sont récurrentes pour $f \circ f$ (croissante), monotones de sens contraires ; le signe de $u_2 - u_0$ donne leur sens ; leurs limites sont des points fixes de $f \circ f$ ; si elles coïncident, $(u_n)$ converge.

### Exercice 18 (1) — $u_{n+1} = \sqrt{u_n + 1}$, sur $I = [0, +\infty[$

- $f(x) = \sqrt{x+1}$, $f'(x) = \frac{1}{2\sqrt{x+1}} > 0$ : croissante ; $I$ est stable.
- Point fixe : $\sqrt{x+1} = x \iff x^2 - x - 1 = 0$, d'où (avec $x \ge 0$) $x = \frac{1 + \sqrt5}{2}$.
- **$u_0 = 0$** : $f(0) - 0 = 1 > 0$, donc $(u_n)$ croissante ; $u_0 < \frac{1+\sqrt5}{2}$ et $f$ croissante donnent $u_n < \frac{1+\sqrt5}{2}$ pour tout $n$. Croissante majorée : $u_n \to \frac{1+\sqrt5}{2}$.
- **$u_0 = 2$** : $f(2) - 2 = \sqrt3 - 2 < 0$, donc $(u_n)$ décroissante, minorée par $\frac{1+\sqrt5}{2}$ : $u_n \to \frac{1+\sqrt5}{2}$.

### Exercice 18 (2) — $u_{n+1} = \frac{1}{u_n} + 1$, sur $I = ]0, +\infty[$

- $f(x) = \frac1x + 1$, $f'(x) = -\frac1{x^2} < 0$ : décroissante ; $I$ stable. $(u_{2n})$ et $(u_{2n+1})$ sont récurrentes pour $f \circ f$.
- $(f \circ f)(x) = \frac{1}{\frac1x + 1} + 1 = \frac{x}{x+1} + 1 = \frac{2x + 1}{x + 1}$, croissante.
- Points fixes de $f \circ f$ : $\frac{2x+1}{x+1} = x \iff x^2 - x - 1 = 0$, d'où l'unique point fixe positif $\frac{1+\sqrt5}{2}$.
- **$u_0 = 1$** : $u_1 = 2$, $u_2 = \frac32$, $u_2 - u_0 > 0$ : $(u_{2n})$ croissante, $(u_{2n+1})$ décroissante, avec $u_{2n} \le \frac{1+\sqrt5}{2} \le u_{2n+1}$. Les deux convergent vers $\frac{1+\sqrt5}{2}$, donc $u_n \to \frac{1+\sqrt5}{2}$.
- **$u_0 = 2$** : $u_1 = \frac32$, $u_2 = \frac53$, $u_2 - u_0 < 0$ : $(u_{2n})$ décroissante, $(u_{2n+1})$ croissante, avec $u_{2n+1} \le \frac{1+\sqrt5}{2} \le u_{2n}$ ; même limite $\frac{1+\sqrt5}{2}$.

### Exercice 19 — $u_0 = 0$, $u_{n+1} = 3 - \sqrt{\frac{u_n}{2}}$

Énoncé : (1) montrer $u_n \in [0, 3]$ ; (2) points fixes de $f(x) = 3 - \sqrt{x/2}$ dans cet intervalle ; (3) $(u_{2n})$ croissante, $(u_{2n+1})$ décroissante ; (4) on admet que $f \circ f$ a les mêmes points fixes que $f$ dans $[0, 3]$ : conclure.

- $f$ est décroissante ($f'(x) = -\frac{1}{4\sqrt{x/2}} < 0$). Pour $x \in [0, 3]$ : $0 < 3 - \sqrt{3/2} = f(3) \le f(x) \le f(0) = 3$, donc $[0, 3]$ est stable et $u_n \in [0, 3]$ pour tout $n$.
- Points fixes : $3 - \sqrt{x/2} = x \iff x^2 - \frac{13}{2}x + 9 = 0$ (après élévation au carré), d'où l'unique solution $x = 2$ dans $[0, 3]$.
- $f$ décroissante : $(u_{2n})$, $(u_{2n+1})$ monotones de sens contraires ; $u_2 - u_0 = 3 - \sqrt{3/2} - 0 > 0$ : $(u_{2n})$ croissante, $(u_{2n+1})$ décroissante. Bornées, elles convergent vers $\ell$ et $\ell'$, points fixes de $f \circ f$ dans $[0, 3]$, donc égaux à 2 (admis). Conclusion : $u_n \to 2$.

### Exercice 20 — $u_0 = 1$, $u_{n+1} = 1 + \frac{2}{u_n}$

Énoncé : (1) $[1, 3]$ est stable par $f$, conséquence sur $u_n$, sens de variation de $f$ ; $v_n = u_{2n}$, $w_n = u_{2n+1}$ ; (2) $(v_n)$ croissante, $(w_n)$ décroissante ; (3) convergence et limites ; (4) nature de $(u_n)$.

- $f(x) = 1 + \frac2x$, $f'(x) = -\frac{2}{x^2} < 0$ : décroissante. Pour $x \in [1, 3]$ : $1 + \frac23 = f(3) \le f(x) \le f(1) = 3$, donc $[1, 3]$ est stable et $1 \le u_n \le 3$.
- $u_2 - u_0 = \frac53 - 1 > 0$ : $(v_n)$ croissante, $(w_n)$ décroissante ; bornées, elles convergent vers $L$ et $L'$.
- $(f \circ f)(x) = \frac{2}{1 + 2/x} + 1 = \frac{2x}{x+2} + 1 = \frac{3x + 2}{x + 2}$ ; sur $[1, 3]$ : $\frac{3x+2}{x+2} = x \iff x^2 - x - 2 = 0 \iff x = 2$.
- Donc $L = L' = 2$ et $u_n \to 2$.

### Exercice 21 — $u_{n+1} = \frac12 u_n(u_n^2 - 3u_n + 4)$

Indication de l'énoncé : étudier les variations de $f$, ses points fixes, le signe de $f(x) - x$, puis distinguer selon $u_0$.

- $f(x) = \frac12 x(x^2 - 3x + 4)$ ; $f'(x) = \frac32 x^2 - 3x + 2$, de discriminant négatif, donc $f' > 0$ : $f$ croissante sur $\mathbb{R}$.
- $f(x) - x = x\left(\frac12 x^2 - \frac32 x + 1\right)$ : points fixes $0$, $1$, $2$.
- Signe : $f(x) - x \le 0$ sur $]-\infty, 0] \cup [1, 2]$ ; $f(x) - x \ge 0$ sur $[0, 1] \cup [2, +\infty[$.
- Intervalles stables (car $f$ croissante) : $]-\infty, 0]$, $[0, 1]$, $[1, 2]$, $[2, +\infty[$ ; et aussi $]-\infty, 0[$, $\{0\}$, $]0, 1]$, $[1, 2[$, $\{2\}$, $]2, +\infty[$.

| $u_0$ | Sens de $(u_n)$ | Limite |
|---|---|---|
| $]-\infty, 0[$ | décroissante | $-\infty$ (pas de point fixe dans l'intervalle) |
| $0$ | constante | $0$ |
| $]0, 1]$ | croissante, bornée par 1 | $1$ |
| $[1, 2[$ | décroissante, bornée | $1$ |
| $2$ | constante | $2$ |
| $]2, +\infty[$ | croissante | $+\infty$ |

## Suites complexes (exercices 22 à 24)

### Exercice 22

1. $u_n = \frac{n^2 i^n}{n^3 + 1}$ : $|u_n| = \frac{n^2}{n^3+1} \to 0$, donc $u_n \to 0$.
2. $u_n = \frac1n + (-1)^n i$ : $\mathrm{Re}(u_n) \to 0$ mais $\mathrm{Im}(u_n) = (-1)^n$ ne converge pas : $(u_n)$ diverge.
3. $u_n = \frac{n}{n + 3i} - \frac{in}{n+1}$ : $\frac{n}{n+3i} = \frac{n(n - 3i)}{n^2 + 9}$, d'où $u_n = \frac{n^2}{n^2+9} - i\left(\frac{3n}{n^2+9} + \frac{n}{n+1}\right) \to 1 - i$.
4. $u_n = \frac{n^2 i - in + 1 - 3i}{(2n + 4i - 3)(n - i)}$ : le dénominateur vaut $2n^2 - 3n + 4 + (2n+3)i$ ; en multipliant par le conjugué,
$$u_n = \frac{2n^3 - 12n - 5 + i(2n^4 - 5n^3 + n^2 + 3n - 15)}{(2n^2 - 3n + 4)^2 + (2n+3)^2} \to 0 + \frac i2 = \frac i2.$$

### Exercice 23 — $z_{n+1} = \frac13(2z_n - \bar z_n)$, $z_0 \in \mathbb{C}$

Avec $z_n = x_n + iy_n$ : $2z_n - \bar z_n = z_n + (z_n - \bar z_n) = x_n + 3iy_n$, donc $x_{n+1} = \frac13 x_n$ et $y_{n+1} = y_n$. Ainsi $x_n = \left(\frac13\right)^n x_0 \to 0$, $y_n = y_0$, et
$$\lim z_n = i y_0 = i\,\mathrm{Im}(z_0).$$

### Exercice 24

$x_{n+1} = \frac{x_n - y_n}{2}$, $y_{n+1} = \frac{x_n + y_n}{2}$, $z_n = x_n + iy_n$.

1. $z_{n+1} = \frac12(x_n + iy_n) + \frac12(-y_n + ix_n) = \frac12 z_n + \frac i2 z_n = \frac{1+i}{2} z_n$, donc $z_n = \frac{(1+i)^n}{2^n} z_0$.
2. $|z_n| = \left(\frac{\sqrt2}{2}\right)^n |z_0| = \left(\frac{1}{\sqrt2}\right)^n |z_0| \to 0$, donc $z_n \to 0$ : $x_n \to 0$ et $y_n \to 0$.

## Exercice 25 — théorème de Cesàro

Énoncé (diapositive intitulée « Exercice 15 - Théorème de Cesàro ») : $v_n = \frac{u_1 + \dots + u_n}{n}$, moyenne arithmétique des $n$ premiers termes. (1) Si $u_n \to l \in \mathbb{R}$, montrer $v_n \to l$ ; étudier la réciproque. (2) Que dire si $u_n \to +\infty$ ? Voir [[Théorème de Cesàro]].

**(1) Démonstration.** Soit $\varepsilon > 0$ et $N_0$ tel que $n > N_0 \Rightarrow |u_n - l| \le \frac\varepsilon2$. Pour $n > N_0$ :
$$|v_n - l| = \left|\frac1n\sum_{k=1}^n (u_k - l)\right| \le \frac1n\sum_{k=1}^{N_0 - 1}|u_k - l| + \frac1n\sum_{k=N_0}^{n}|u_k - l| \le \frac1n\sum_{k=1}^{N_0-1}|u_k - l| + \frac{n - N_0 + 1}{n}\cdot\frac\varepsilon2.$$
Comme $\frac{n - N_0 + 1}{n} < 1$, le second terme est $\le \frac\varepsilon2$. Le premier est une constante divisée par $n$ : il existe $N_1$ tel qu'il soit $\le \frac\varepsilon2$ pour $n > N_1$. Avec $N = \max(N_0, N_1)$ : $n > N \Rightarrow |v_n - l| \le \varepsilon$.

**Réciproque fausse.** $u_n = (-1)^{n+1}$ diverge, mais $0 \le v_n \le \frac1n$, donc $v_n \to 0$.

**(2) Si $u_n \to +\infty$, alors $v_n \to +\infty$.** Soit $A > 0$ et $N_0$ tel que $n > N_0 \Rightarrow u_n > 4A$. Pour $n > N_0$ :
$$v_n \ge \frac{u_1 + \dots + u_{N_0 - 1}}{n} + 4A\,\frac{n - N_0 + 1}{n}.$$
Il existe $N_1$ tel que $\frac{n - N_0 + 1}{n} > \frac12$ pour $n > N_1$, et $N_2$ tel que $\frac{u_1 + \dots + u_{N_0-1}}{n} > -A$ pour $n > N_2$. Avec $N = \max(N_0, N_1, N_2)$ : $v_n > -A + 4A \cdot \frac12 = A$.

## Exercice 26 — constante d'Euler

$H_n = 1 + \frac12 + \dots + \frac1n$ ([[Constante d'Euler]]).

1. **Montrer $\frac{1}{n+1} \le \ln(n+1) - \ln n \le \frac1n$.** $f(x) = \frac1x$ est continue décroissante sur $]0, +\infty[$, donc
$$\frac{1}{n+1} = (n + 1 - n) f(n+1) \le \int_n^{n+1} \frac{dx}{x} = \ln(n+1) - \ln n \le (n+1-n) f(n) = \frac1n.$$
2. **En déduire $\ln(n+1) \le H_n \le 1 + \ln n$** ([[Comparaison série-intégrale]]). Pour $k \ge 1$, $\frac1k \ge \int_k^{k+1}\frac{dx}{x}$, donc $H_n \ge \int_1^{n+1}\frac{dx}{x} = \ln(n+1)$. Pour $k \ge 2$, $\frac1k \le \int_{k-1}^k \frac{dx}{x}$, donc $H_n \le 1 + \int_1^n \frac{dx}{x} = 1 + \ln n$ (vrai aussi pour $n = 1$).
3. **Limite de $H_n$** : par le théorème des gendarmes (minoration par $\ln(n+1)$), $H_n \to +\infty$.
4. **$u_n = H_n - \ln n$ est décroissante et positive.** $u_{n+1} - u_n = \frac{1}{n+1} - (\ln(n+1) - \ln n) \le 0$ d'après 1. Positivité par récurrence : $u_1 = 1 > 0$, et $u_{n+1} = H_n + \frac{1}{n+1} - \ln(n+1) > 0$ car $H_n \ge \ln(n+1)$.
5. **Conclusion** : $(u_n)$ est décroissante et minorée par 0, donc converge vers $\gamma \ge 0$, la constante d'Euler (Leonhard Euler, 1707-1783), $\gamma \approx 0{,}5772156649\ldots$ ; on ne sait toujours pas si elle est rationnelle ou irrationnelle.

## Exercice 27 — suite géométrique complexe $z_n = a^n$, $a \in \mathbb{C}$

1. **$|a| < 1$** : $|z_n| = |a|^n \to 0$, donc $z_n \to 0$. **$|a| > 1$** : $|z_n| \to +\infty$, $(z_n)$ diverge.
2. **$|a| = 1$, $a = e^{i\theta}$, $\frac{\theta}{2\pi} \in \mathbb{Z}$** : $\theta = 2k\pi$, $a = 1$, $(z_n)$ constante égale à 1, limite 1.
3. **$\frac{\theta}{2\pi} \in \mathbb{Q} \setminus \mathbb{Z}$** : $\frac{\theta}{2\pi} = \frac pq$ avec $p, q$ premiers entre eux, $q \ne 0$. Alors $z_n = e^{2ip n\pi/q}$ et $z_{n+q} = z_n e^{2ip\pi} = z_n$ : la suite est périodique, et prend les valeurs $1, e^{2ip\pi/q}, e^{4ip\pi/q}, \dots, e^{2ip(q-1)\pi/q}$ selon le reste de $n$ modulo $q$. Le corrigé conclut : « périodique et donc divergente » (voir Points à vérifier).
4. **$\frac{\theta}{2\pi} \notin \mathbb{Q}$** : les $z_n$ sont deux à deux distincts (si $z_n = z_m$ avec $n \ne m$, alors $\theta(n - m) = 2k\pi$, donc $\frac{\theta}{2\pi} = \frac{k}{n-m} \in \mathbb{Q}$, contradiction). Proposition admise : l'ensemble $\{e^{in\theta} : n \in \mathbb{N}\}$ est dense dans le cercle unité $\mathbb{U}$. Pour tout $u \in \mathbb{U}$, une suite extraite de $(z_n)$ tend vers $u$ : $(z_n)$ a des suites extraites de limites différentes, donc diverge.

## À retenir

- Pour une suite récurrente : stabilité de l'intervalle, monotonie de $f$, points fixes, puis monotonie de la suite et limite. Si $f$ est décroissante, étudier $f \circ f$ ou les suites paire et impaire.
- Pour montrer la convergence d'une suite alternée ou encadrée : suites adjacentes.
- Une démonstration par la définition suit toujours le schéma : fixer $\varepsilon$ (ou $M$), isoler $n$, choisir $N$.
- Pour une forme $\sqrt{A} - \sqrt{B}$ : quantité conjuguée. Pour une puissance $u_n^{v_n}$ : écrire $\exp(v_n \ln u_n)$ et composer.
- Pour montrer une divergence : deux suites extraites de limites différentes.

## Points à vérifier

- **Exercice 27, question 3** : le corrigé écrit que si $\theta/2\pi \in \mathbb{Q} \setminus \mathbb{Z}$, la suite est « périodique et donc divergente ». Une suite périodique peut converger (une suite constante est périodique). Ici la divergence vient du fait que la suite prend plusieurs valeurs distinctes, répétées indéfiniment ($q \ge 2$ valeurs $e^{2ip\pi n/q}$), donc deux sous-suites ont des limites différentes (complément).
- **Exercice 13, question 3** : le corrigé écrit $\frac{v_{n+1}}{v_n} = \frac{n}{n+1}$ pour $v_n = \frac{1}{n+1}$ ; le rapport exact est $\frac{n+1}{n+2}$. La conclusion (rapport $\to 1$) n'est pas changée.
- **Exercice 13, question 4** : l'énoncé donne $z_n = \sqrt[n]{a}$ avec $a \in \mathbb{R}$, le corrigé avec $a \in \mathbb{R}^*_+$ ; seule la seconde hypothèse a un sens ici.
- **Exercice 19** : le corrigé définit $f$ sur $]0, +\infty[$, puis raisonne sur $[0, 3]$ et utilise $f(0) = 3$ ; $f$ est en fait définie sur $[0, +\infty[$ (complément). L'unicité du point fixe de $f \circ f$ est admise par l'énoncé.
- **Exercice 21** : le corrigé écrit $[2, +\infty]$ (crochet fermé en $+\infty$) dans l'étude du signe de $f(x) - x$ ; coquille.
- **Numérotation** : l'exercice 10 est absent ; l'énoncé de Cesàro est titré « Exercice 15 », son corrigé « Exercice 25 » ; une diapositive de la constante d'Euler est titrée « Exercice 21 ».
- **Exercice 7 (b)** : l'énoncé commence la somme par $\frac1n = \frac{1}{n + \sqrt0}$ ; le corrigé compte donc $n + 1$ termes ($k = 0, \dots, n$), d'où les bornes $\frac{n+1}{n+\sqrt n}$ et $\frac{n+1}{n}$.

## Liens

[[Suite numérique]], [[Limite et continuité]], [[Série numérique]], [[Critère de d'Alembert et de Cauchy]], [[Récurrence]], [[Borne supérieure]].
