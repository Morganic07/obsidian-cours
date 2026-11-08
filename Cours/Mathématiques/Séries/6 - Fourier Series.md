---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Séries/Chp6 : Fourier Series.docx|Chp6 - Fourier Series]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Séries/Chp6 : Fourier Series.docx|Chp6 - Fourier Series]], dans [[Cours/Mathématiques/Séries/_index|Séries]]. Cours en anglais. Les énoncés en image sont recopiés en texte ; seule la figure du phénomène de Gibbs est intégrée.

## Idée générale

Associer à une fonction $2\pi$-périodique une série trigonométrique, puis dire quand elle converge vers la fonction. Voir [[Série de Fourier]].

L'idée revient à Joseph Fourier, qui l'introduit pour résoudre l'équation de la chaleur (*Théorie analytique de la chaleur*, 1822) : un signal périodique se décompose en une somme d'oscillations pures, la **fondamentale** ($n = 1$, même période que $f$) et les **harmoniques** ($n \ge 2$, fréquences multiples). La suite $(a_n, b_n)$ est le **spectre** du signal ; c'est la base du traitement du signal, de l'acoustique (le timbre d'un instrument tient à ses harmoniques) et de la compression d'images et de sons. [[Complément hors du cours|ⓘ]]

## Définition

**Définition.** Une série de Fourier (ou série trigonométrique) est
$$a_0 + \sum_{n=1}^{+\infty} (a_n \cos nx + b_n \sin nx),$$
où $(a_n)_{n\ge0}$ et $(b_n)_{n\ge1}$ sont des réels, les **coefficients de Fourier** de la série.

On calcule des séries de Fourier pour une classe de fonctions précise, les fonctions [[Fonction continue par morceaux|continues par morceaux]].

**Définition.** Une fonction est continue par morceaux (*piece-wise continuous*) sur un intervalle si l'intervalle peut être découpé en un nombre fini d'intervalles sur chacun desquels la fonction est continue et admet des limites finies à droite et à gauche. Une telle fonction n'a qu'un nombre fini de discontinuités.

## Séries de Fourier de période $2\pi$

**Définition.** Soit $f$ continue par morceaux sur $\mathbb{R}$. $f$ est [[Fonction périodique|périodique]] de période $2\pi$ ($2\pi$-périodique) si
$$\forall x \in \mathbb{R},\ f(x+2\pi) = f(x).$$

**Remarque.** Si une fonction continue par morceaux est définie sur $[-\pi, \pi[$ ou sur $[0, 2\pi[$, et prolongée hors de cet intervalle par $f(x+2\pi) = f(x)$, alors elle est $2\pi$-périodique.

**Proposition.** Si $f$ est $2\pi$-périodique :
$$\forall a, b \in \mathbb{R},\quad \int_a^{a+2\pi} f(t)\,dt = \int_b^{b+2\pi} f(t)\,dt.$$
En particulier $\int_{-\pi}^{\pi} f = \int_0^{2\pi} f$. Voir [[Parité et périodicité d'une intégrale]].

## Série de Fourier d'une fonction $2\pi$-périodique continue par morceaux

**Définition.** Soit $f$ continue par morceaux et $2\pi$-périodique. Sa série de Fourier est
$$FS(f)(x) = a_0 + \sum_{n=1}^{+\infty} (a_n \cos nx + b_n \sin nx),$$
avec
$$a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} f(x)\,dx,$$
$$\forall n \ge 1,\quad a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\cos nx\,dx, \qquad b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\sin nx\,dx.$$
Ce sont les coefficients de Fourier de $f$.

**D'où viennent ces formules : l'orthogonalité.** Pour $m, n \ge 1$ entiers, en linéarisant les produits ([[Linéarisation trigonométrique]]) :
$$\int_{-\pi}^{\pi} \cos mx \cos nx\,dx = \int_{-\pi}^{\pi} \sin mx \sin nx\,dx = \begin{cases} \pi & \text{si } m = n \\ 0 & \text{si } m \ne n \end{cases}, \qquad \int_{-\pi}^{\pi} \cos mx \sin nx\,dx = 0,$$
et $\int_{-\pi}^{\pi} \cos nx\,dx = \int_{-\pi}^{\pi} \sin nx\,dx = 0$. Les fonctions $1, \cos x, \sin x, \cos 2x, \dots$ sont donc deux à deux [[Orthogonalité|orthogonales]] pour le [[Produit scalaire|produit scalaire]] $\langle f, g \rangle = \int_{-\pi}^{\pi} f g$. Si $f = a_0 + \sum (a_k \cos kx + b_k \sin kx)$, multiplier par $\cos nx$ et intégrer sur $[-\pi, \pi]$ (en supposant l'échange somme-intégrale permis) annule tous les termes sauf $a_n \pi$ : d'où $a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\cos nx\,dx$. Intégrer $f$ seule laisse $2\pi a_0$, d'où le facteur $\frac{1}{2\pi}$ : $a_0$ est la **valeur moyenne** de $f$ sur une période. [[Complément hors du cours|ⓘ]]

**Somme partielle.** On note $S_N(x) = a_0 + \sum_{n=1}^{N} (a_n \cos nx + b_n \sin nx)$ la somme partielle d'ordre $N$ ; dire que la série de Fourier converge en $x$, c'est dire que $S_N(x)$ a une limite quand $N \to +\infty$. C'est la notation $S_n$ utilisée dans la figure du phénomène de Gibbs. [[Complément hors du cours|ⓘ]]

**Fonction de période $T$ quelconque.** Si $f$ est $T$-périodique, on pose $\omega = \frac{2\pi}{T}$ (pulsation) et
$$FS(f)(x) = a_0 + \sum_{n=1}^{+\infty} (a_n \cos n\omega x + b_n \sin n\omega x), \quad a_0 = \frac{1}{T}\int_{0}^{T} f, \quad a_n = \frac{2}{T}\int_{0}^{T} f(x)\cos n\omega x\,dx, \quad b_n = \frac{2}{T}\int_{0}^{T} f(x)\sin n\omega x\,dx.$$
Pour $T = 2\pi$, on retrouve les formules du cours ; les théorèmes de convergence et Parseval s'adaptent de la même façon. [[Complément hors du cours|ⓘ]]

**Forme complexe.** Avec $e^{inx} = \cos nx + i \sin nx$ ([[Forme trigonométrique et exponentielle]]), on écrit aussi $FS(f)(x) = \sum_{n=-\infty}^{+\infty} c_n e^{inx}$, où $c_n = \frac{1}{2\pi}\int_{-\pi}^{\pi} f(x) e^{-inx}\,dx$. Le lien avec les coefficients réels : $c_0 = a_0$, et pour $n \ge 1$, $c_n = \frac{a_n - i b_n}{2}$, $c_{-n} = \frac{a_n + i b_n}{2}$. Cette forme est la plus courante en physique et en traitement du signal. [[Complément hors du cours|ⓘ]]

**Remarque.** Cette définition ne dit pas que $f$ est la somme de sa série de Fourier : elle associe seulement à chaque fonction continue par morceaux et $2\pi$-périodique une série $FS(f)$. Les conditions pour que $f$ en soit la somme viennent plus loin.

## Phénomène de Gibbs

Premières sommes partielles de la série de Fourier d'une fonction créneau (*square wave*) :

![[Chp6 - Fourier Series - image9.png]]

*Figure : sommes partielles $S_1$, $S_3$, $S_5$, $S_7$, $S_{11}$ et $S_{15}$ (en bleu) d'une fonction créneau valant 0 sur $[-\pi, 0[$ et 1 sur $]0, \pi]$ (en rouge).*

Quand $n$ augmente, $S_n$ approche de mieux en mieux la fonction créneau, mais les sommes partielles dépassent (*overshoot*) près des sauts : c'est le **phénomène de Gibbs**. On dirait que $f$ est la somme de sa série de Fourier, sauf aux points où $f$ est discontinue.

**Calcul de la série de ce créneau.** $a_0 = \frac{1}{2\pi}\int_0^{\pi} 1\,dx = \frac{1}{2}$ ; pour $n \ge 1$, $a_n = \frac{1}{\pi}\int_0^{\pi} \cos nx\,dx = \frac{1}{\pi}\left[\frac{\sin nx}{n}\right]_0^{\pi} = 0$ et $b_n = \frac{1}{\pi}\int_0^{\pi} \sin nx\,dx = \frac{1 - (-1)^n}{n\pi}$, soit $\frac{2}{n\pi}$ pour $n$ impair et $0$ pour $n$ pair. Donc
$$FS(f)(x) = \frac{1}{2} + \frac{2}{\pi}\sum_{k=0}^{+\infty} \frac{\sin\big((2k+1)x\big)}{2k+1}.$$
Seules les harmoniques impaires apparaissent, ce qui explique que la figure ne montre que $S_1, S_3, S_5, \dots$ (les sommes paires répètent la précédente). Les $a_n$ sont nuls parce que $f - \frac{1}{2}$ est impaire. [[Complément hors du cours|ⓘ]]

**Taille du dépassement.** Le dépassement ne disparaît pas quand $n$ grandit : il se resserre contre le saut mais sa hauteur tend vers environ $9\,\%$ de la hauteur du saut (ici les sommes partielles montent jusqu'à environ $1{,}09$). La convergence n'est donc pas [[Convergence uniforme|uniforme]] près d'une discontinuité ; c'est forcé, car une limite uniforme de fonctions continues (les $S_n$) est continue, ce que le créneau n'est pas. [[Complément hors du cours|ⓘ]]

## Séries de Fourier des fonctions paires

**Définition.** Soit $I$ un intervalle symétrique par rapport à l'origine. $f$ est [[Fonction paire et impaire|paire]] si $\forall x \in I,\ f(-x) = f(x)$.

**Proposition.** Si $f$ est $2\pi$-périodique, continue par morceaux et paire :
$$a_0 = \frac{1}{\pi}\int_0^{\pi} f(x)\,dx, \qquad \forall n \ge 1,\ a_n = \frac{2}{\pi}\int_0^{\pi} f(x)\cos nx\,dx, \qquad b_n = 0,$$
donc
$$FS(f)(x) = a_0 + \sum_{n=1}^{+\infty} a_n \cos nx.$$

Justification : si $f$ est paire, $x \mapsto f(x)\sin nx$ est impaire, donc son intégrale sur $[-\pi, \pi]$ est nulle ($b_n = 0$), tandis que $f(x)\cos nx$ est paire, d'où $\int_{-\pi}^{\pi} = 2\int_0^{\pi}$ ([[Parité et périodicité d'une intégrale]]). Le même argument, inversé, donne le cas impair ci-dessous. [[Complément hors du cours|ⓘ]]

## Séries de Fourier des fonctions impaires

**Définition.** $f$ est impaire si $\forall x \in I,\ f(-x) = -f(x)$.

**Proposition.** Si $f$ est $2\pi$-périodique, continue par morceaux et impaire :
$$\forall n \ge 0,\ a_n = 0, \qquad \forall n \ge 1,\ b_n = \frac{2}{\pi}\int_0^{\pi} f(x)\sin nx\,dx,$$
donc
$$FS(f)(x) = \sum_{n=1}^{+\infty} b_n \sin nx.$$

## Convergence des séries de Fourier

### Convergence simple (théorème de Dirichlet)

**Théorème.** Si $f$ est $2\pi$-périodique et si $f$ et $f'$ sont continues par morceaux sur $[-\pi, \pi]$, la série de Fourier de $f$ converge simplement. Sa somme vaut $f(x)$ en tout point où $f$ est continue. En un point $x$ de discontinuité, elle vaut la moyenne des limites à droite et à gauche :
$$\frac{1}{2}\left(f(x^+) + f(x^-)\right), \qquad f(x^+) = \lim_{t \to x^+} f(t),\quad f(x^-) = \lim_{t \to x^-} f(t).$$
(Le nom « théorème de Dirichlet » n'est pas dans le cours.)

**Exemple : la série de Leibniz.** Appliqué au créneau ci-dessus en $x = \frac{\pi}{2}$ (point de continuité, $f = 1$) : $\sin\big((2k+1)\frac{\pi}{2}\big) = (-1)^k$, donc $1 = \frac{1}{2} + \frac{2}{\pi}\sum_{k \ge 0} \frac{(-1)^k}{2k+1}$, soit
$$\sum_{k=0}^{+\infty} \frac{(-1)^k}{2k+1} = 1 - \frac{1}{3} + \frac{1}{5} - \dots = \frac{\pi}{4}.$$
En $x = 0$ (saut de 0 à 1), tous les sinus sont nuls et la série vaut $\frac{1}{2}$, la moyenne des limites à gauche et à droite, comme l'annonce le théorème. Les séries de Fourier servent ainsi à calculer des sommes de [[Série numérique|séries numériques]]. [[Complément hors du cours|ⓘ]]

### Convergence normale

**Théorème.** Si $f$ est $2\pi$-périodique, continue, et si $f'$ est continue par morceaux sur $[-\pi, \pi]$, la série de Fourier de $f$ converge normalement vers $f$ (voir [[4 - Series of functions|convergence normale]]).

Idée de la preuve : une intégration par parties donne les coefficients de $f'$ en fonction de ceux de $f$, $a_n(f') = n\,b_n(f)$ et $b_n(f') = -n\,a_n(f)$. Alors $|a_n(f)| + |b_n(f)| = \frac{1}{n}\big(|b_n(f')| + |a_n(f')|\big)$, et l'[[Inégalité de Cauchy-Schwarz]] jointe à Parseval appliquée à $f'$ montre que $\sum (|a_n| + |b_n|)$ converge : c'est la convergence normale, puisque $|a_n \cos nx + b_n \sin nx| \le |a_n| + |b_n|$. La continuité de $f$ est indispensable (voir le phénomène de Gibbs). Plus $f$ est régulière, plus ses coefficients décroissent vite. [[Complément hors du cours|ⓘ]]

## Égalité de Parseval

**Théorème.** Si $f$ est $2\pi$-périodique et continue par morceaux sur $[-\pi, \pi]$ :
$$a_0^2 + \frac{1}{2}\sum_{n=1}^{+\infty}\left(a_n^2 + b_n^2\right) = \frac{1}{2\pi}\int_{-\pi}^{\pi} f(x)^2\,dx.$$

**Interprétation.** Le membre de droite est la valeur moyenne de $f^2$, l'**énergie** (ou puissance moyenne) du signal ; Parseval dit qu'elle se répartit entre les harmoniques, chacune comptant pour $\frac{1}{2}(a_n^2 + b_n^2)$. C'est l'analogue du [[Théorème de Pythagore]] dans la base orthogonale des $\cos nx$, $\sin nx$. Il n'est pas nécessaire que la série converge vers $f$ pour l'appliquer. [[Complément hors du cours|ⓘ]]

**Conséquence : les coefficients tendent vers 0.** La série $\sum (a_n^2 + b_n^2)$ étant convergente, son terme général tend vers 0, donc $a_n \to 0$ et $b_n \to 0$ (cas particulier du lemme de Riemann-Lebesgue). L'inégalité $a_0^2 + \frac{1}{2}\sum_{n=1}^{N}(a_n^2 + b_n^2) \le \frac{1}{2\pi}\int_{-\pi}^{\pi} f^2$, vraie pour tout $N$, s'appelle l'**inégalité de Bessel**. [[Complément hors du cours|ⓘ]]

**Exemple : le problème de Bâle.** Pour le créneau ci-dessus : $a_0^2 = \frac{1}{4}$, $\frac{1}{2}\sum b_n^2 = \frac{1}{2}\sum_{k \ge 0}\frac{4}{\pi^2(2k+1)^2}$ et $\frac{1}{2\pi}\int_{-\pi}^{\pi} f^2 = \frac{1}{2\pi}\cdot\pi = \frac{1}{2}$. Parseval donne $\sum_{k \ge 0} \frac{1}{(2k+1)^2} = \frac{\pi^2}{8}$. Comme $\sum_{n \ge 1}\frac{1}{n^2}$ se sépare en termes impairs et termes pairs, et que les pairs valent $\sum \frac{1}{(2k)^2} = \frac{1}{4}\sum_{n \ge 1}\frac{1}{n^2}$, on obtient $\frac{3}{4}\sum_{n \ge 1}\frac{1}{n^2} = \frac{\pi^2}{8}$, soit
$$\sum_{n=1}^{+\infty} \frac{1}{n^2} = \frac{\pi^2}{6},$$
la somme de la [[Série numérique|série de Riemann]] d'exposant 2, trouvée par Euler au XVIII<sup>e</sup> siècle par une autre méthode. [[Complément hors du cours|ⓘ]]
