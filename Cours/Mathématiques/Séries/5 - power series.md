---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Séries/Chp5 : power series.docx|Chp5 - power series]]"]
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 3/Séries/Chp5 : power series.docx|Chp5 - power series]], dans [[Cours/Mathématiques/Séries/_index|Séries]]. Cours en anglais. En cas d'écart, le cours et ses images font foi. Toutes les images de la note sont des énoncés (texte et formules) : leur contenu est recopié ci-dessous, aucune n'est une figure.

## Idée générale

Les séries entières $\sum a_n(x - \alpha)^n$ : domaine de convergence, régularité de la somme, développement de Taylor et séries usuelles, puis applications au calcul de sommes et à l'approximation de $\pi$ et de $e$. Voir [[Série entière]].

## Définition

**Définition.** Une série entière (*power series*) centrée en 0 est une série de fonctions de la forme
$$\sum_{n\in\mathbb{N}} a_n x^n = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + \ldots$$
Les constantes $a_n$ sont les **coefficients**. Pour $\alpha \in \mathbb{R}$, une série entière centrée en $\alpha$ est
$$\sum_{n\in\mathbb{N}} a_n (x-\alpha)^n = a_0 + a_1 (x-\alpha) + a_2 (x-\alpha)^2 + \ldots$$

## Convergence d'une série entière

**Théorème.** Pour une série entière $\sum a_n(x-\alpha)^n$, il n'y a que trois possibilités :
1. elle ne converge que pour $x = \alpha$ ;
2. elle converge pour tout $x \in \mathbb{R}$ ;
3. il existe $R$ avec $0 < R < +\infty$ tel que la série converge absolument si $|x-\alpha| < R$ et diverge si $|x-\alpha| > R$. Pour $x - \alpha = \pm R$, tout peut arriver.

**Définition.** Ce nombre $R$ est le **rayon de convergence** (*radius of convergence*). Par convention, $R = 0$ dans le cas 1 et $R = +\infty$ dans le cas 2.

**Proposition.** Le rayon de convergence est unique.

## Intervalle de convergence

**Proposition.** L'intervalle de convergence de $\sum a_n(x-\alpha)^n$ est l'ensemble des $x$ pour lesquels la série converge.

Centrée en 0 :
- $R = 0$ : intervalle $\{0\}$ ;
- $R = +\infty$ : intervalle $]-\infty, +\infty[$ ;
- $R \in\, ]0, +\infty[$ : en $x = \pm R$, la série peut converger en une borne, aux deux, ou à aucune. Quatre possibilités : $[-R, R]$, $]-R, R]$, $[-R, R[$, $]-R, R[$.

Centrée en $\alpha$ (généralisation) :
- $R = 0$ : $\{\alpha\}$ ;
- $R = +\infty$ : $]-\infty, +\infty[$ ;
- $R \in\, ]0, +\infty[$ : $[\alpha - R, \alpha + R]$, $]\alpha - R, \alpha + R]$, $[\alpha - R, \alpha + R[$ ou $]\alpha - R, \alpha + R[$.

## Critères du rapport et de la racine

Voir [[Critère de d'Alembert et de Cauchy]].

**Proposition (rapport).** Si $R$ est le rayon de $\sum a_n(x-\alpha)^n$ et si $a_n \ne 0$ pour $n$ assez grand :
$$\lim_{n\to+\infty} \frac{|a_{n+1}|}{|a_n|} = \ell \in [0,+\infty] \ \Rightarrow\ R = \frac{1}{\ell}.$$

**Proposition (racine).** Sous les mêmes hypothèses :
$$\lim_{n\to+\infty} \sqrt[n]{|a_n|} = \ell \in [0,+\infty] \ \Rightarrow\ R = \frac{1}{\ell}.$$

Conventions : $\frac{1}{0} = +\infty$ et $\frac{1}{+\infty} = 0$.

**Remarque (coefficients lacunaires).** Quand des coefficients sont nuls (*gaps*), appliquer les critères aux termes complets de rangs $n$ et $n+1$ de la série, c'est-à-dire à $a_n(x-\alpha)^n$, et non aux seuls coefficients.

## Opérations sur les séries entières

**Proposition (multiplication par un scalaire).** Soit $\lambda \in \mathbb{R}$ et $\sum a_n x^n$ de rayon $R_a$ et de somme $S_a$. Le rayon $R_{\lambda a}$ et la somme $S_{\lambda a}$ de $\sum \lambda a_n x^n$ vérifient
$$R_{\lambda a} = R_a \ (\lambda \ne 0) \quad\text{et}\quad \forall x,\ |x| < R_a \Rightarrow S_{\lambda a}(x) = \lambda S_a(x).$$
(Le cours écrit $|x| \le R_a$ et n'exclut pas $\lambda = 0$, voir « Erreurs du cours ».)

**Définition (somme).** La somme de $\sum a_n x^n$ et $\sum b_n x^n$ est $\sum (a_n + b_n)x^n$.

**Proposition.** Avec $R_a$, $R_b$ les rayons et $S_a$, $S_b$ les sommes, le rayon $R_{a+b}$ de la série somme vérifie $R_{a+b} \ge \min(R_a, R_b)$, et
$$\forall x,\ |x| < \min(R_a, R_b) \Rightarrow S_{a+b}(x) = S_a(x) + S_b(x).$$
(Le cours écrit $|x| \le \min(R_a, R_b)$, voir « Erreurs du cours ».)
De plus, si $R_a \ne R_b$, alors $R_{a+b} = \min(R_a, R_b)$.

Le cours annonce ensuite l'étude de la continuité de la somme, puis la **dérivation et l'intégration terme à terme** (*term-by-term differentiation and integration*).

## Continuité

**Théorème.** Soit $\sum a_n(x-\alpha)^n$ de rayon $R > 0$. La série converge normalement sur tout intervalle $[\alpha - r, \alpha + r]$ avec $0 < r < R$, donc la somme $S$ est continue sur $]\alpha - R, \alpha + R[$.
De plus, si $\sum a_n(-R)^n$ converge, $S$ est continue en $\alpha - R$ ; si $\sum a_n R^n$ converge, $S$ est continue en $\alpha + R$.

**Corollaire.** Dans ces conditions, si $\sum a_n(-R)^n$ converge, alors $S(\alpha - R) = \sum a_n(-R)^n$ ; si $\sum a_n R^n$ converge, alors $S(\alpha + R) = \sum a_n R^n$.

## Dérivation et intégration terme à terme

**Théorème (dérivation).** Si $R > 0$, la somme $S$ est dérivable sur $]\alpha - R, \alpha + R[$ et
$$\forall x \in\, ]\alpha - R, \alpha + R[,\quad S'(x) = \sum_{n=1}^{+\infty} n a_n (x-\alpha)^{n-1}.$$

**Théorème (intégration).** Si $R > 0$, la somme $S$ est intégrable sur $]\alpha - R, \alpha + R[$ et
$$\int S(x)\,dx = C + \sum_{n=0}^{+\infty} a_n \frac{(x-\alpha)^{n+1}}{n+1}.$$

**Remarques.**
1. Le rayon de convergence reste le même après dérivation ou intégration, mais pas forcément l'intervalle de convergence : le comportement aux bornes peut changer. Une série peut converger en une borne alors que sa série dérivée y diverge.
2. Faits de base (série centrée en 0) : toute série entière a un rayon $0 \le R \le +\infty$ ; elle converge absolument pour $|x| < R$ et diverge pour $|x| > R$ ; la convergence est normale, donc uniforme, sur tout intervalle $|x| < r$ avec $0 \le r < R$ ; si $R > 0$, la somme est indéfiniment dérivable sur $|x| < R$, et ses dérivées s'obtiennent en dérivant terme à terme.

## Séries de Taylor et de Maclaurin

**Théorème (valeur des coefficients).** Si $f$ est développable en série entière en $\alpha$, $f(x) = \sum a_n (x-\alpha)^n$, alors
$$a_n = \frac{f^{(n)}(\alpha)}{n!}, \qquad \forall x \in\, ]\alpha - R, \alpha + R[,\ f(x) = \sum_{n=0}^{+\infty} \frac{f^{(n)}(\alpha)}{n!}(x-\alpha)^n.$$

**Définitions.**
- Cette série est la **série de Taylor** de $f$ en $\alpha$.
- En $\alpha = 0$, $\sum \frac{f^{(n)}(0)}{n!}x^n$ est la **série de Maclaurin** de $f$.

### Polynômes de Taylor

**Définition.** Pour $f$ indéfiniment dérivable, le $n$-ième polynôme de Taylor de $f$ en $\alpha$ est
$$T_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(\alpha)}{k!}(x-\alpha)^k,$$
et le reste est $R_n(x) = f(x) - T_n(x)$. Voir [[Reste de Taylor]] et [[Développement limité]].

**Théorème (condition suffisante).** Si $\lim_{n\to+\infty} R_n(x) = 0$ pour $|x-\alpha| < R$, alors $f$ est la somme de sa série de Taylor sur $|x-\alpha| < R$.

### Inégalité de Taylor

**Théorème.** S'il existe $M > 0$ et $d > 0$ tels que, pour tout $x$ avec $|x-\alpha| \le d$ et pour tout $n$, $|f^{(n+1)}(x)| \le M$, alors
$$\forall x \in [\alpha - d, \alpha + d],\quad |R_n(x)| \le \frac{M}{(n+1)!}|x - \alpha|^{n+1}.$$
(Le cours écrit l'intervalle $[d - \alpha, d + \alpha]$, voir « Erreurs du cours ».)

### Forme intégrale du reste

**Théorème.** Si $f^{(n+1)}$ est continue sur un intervalle ouvert $I$ contenant $\alpha$ et $x$ :
$$R_n(x) = \frac{1}{n!}\int_{\alpha}^{x} (x-t)^n f^{(n+1)}(t)\,dt.$$

### Exemple : série de Maclaurin de $\sin$

Dérivées successives :

| Ordre | $f^{(k)}(x)$ | $f^{(k)}(0)$ |
|---|---|---|
| $4n$ | $\sin x$ | 0 |
| $4n+1$ | $\cos x$ | 1 |
| $4n+2$ | $-\sin x$ | 0 |
| $4n+3$ | $-\cos x$ | $-1$ |

D'où
$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \ldots = \sum_{n=0}^{+\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!}.$$

**Étude du reste.** Pour tout $x$ et tout $n$, $|f^{(n)}(x)| \le 1$.
- Si $x > 0$ :
$$|R_n(x)| = \frac{1}{n!}\left|\int_0^x (x-t)^n f^{(n+1)}(t)\,dt\right| \le \frac{1}{n!}\int_0^x (x-t)^n\,dt = \frac{x^{n+1}}{(n+1)!}.$$
- Si $x < 0$ : $R_n(x) = -\frac{1}{n!}\int_x^0 (x-t)^n f^{(n+1)}(t)\,dt$, donc
$$|R_n(x)| \le \frac{1}{n!}\int_x^0 |x - t|^n\,dt = \frac{1}{n!}\int_x^0 (t-x)^n\,dt = \frac{(-x)^{n+1}}{(n+1)!}.$$

Comme $\frac{|x|^{n+1}}{(n+1)!} \to 0$, $R_n(x) \to 0$ : $\sin x$ est la somme de sa série de Maclaurin.

### Forme de Lagrange du reste

**Théorème.** Si $f^{(n+1)}$ est continue sur un intervalle ouvert $I$ contenant $\alpha$ et $x$, il existe $c$ entre $\alpha$ et $x$ tel que
$$R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-\alpha)^{n+1}.$$

## La fonction $(1+x)^a$ et la série binomiale

**Théorème.** Pour $a \in \mathbb{R}$ et $|x| < 1$ :
$$(1+x)^a = 1 + \sum_{n=1}^{+\infty} \frac{a(a-1)\cdots(a-n+1)}{n!} x^n = \sum_{n=0}^{+\infty} \binom{a}{n} x^n.$$
Voir [[Coefficient binomial]].

**Remarques.**
1. Si $a$ est un entier positif, les termes finissent par être nuls : la série est finie (formule du [[Formule du binôme de Newton|binôme]]).
2. Le rayon vaut 1 ; la convergence en $\pm 1$ dépend de $a$.

**Proposition (bords).**
1. $a > 0$ : absolument convergente en $x = 1$ et $x = -1$.
2. $-1 < a < 0$ : [[Convergence conditionnelle|conditionnellement convergente]] en $x = 1$, divergente en $x = -1$ (le cours écrit $-1 < a \le 0$, voir « Erreurs du cours »).
3. $a \le -1$ : divergente en $x = 1$ et $x = -1$.

**Deux cas particuliers.**
1. Pour $x \in [-1, 1]$ :
$$\sqrt{1+x} = 1 + \frac{x}{2} + \sum_{n=2}^{+\infty} (-1)^{n+1} \frac{1\cdot 3\cdot 5 \cdots (2n-3)}{n!\,2^n} x^n = \sum_{n=0}^{+\infty} (-1)^{n+1} \frac{\binom{2n}{n}}{(2n-1)2^{2n}} x^n.$$
2. Pour $x \in\, ]-1, 1]$ :
$$\frac{1}{\sqrt{1+x}} = 1 + \sum_{n=1}^{+\infty} (-1)^{n} \frac{1\cdot 3\cdot 5 \cdots (2n-1)}{n!\,2^n} x^n = \sum_{n=0}^{+\infty} (-1)^{n} \frac{\binom{2n}{n}}{2^{2n}} x^n.$$

## Séries de Maclaurin usuelles

| Fonction | Série | Domaine (cours) |
|---|---|---|
| $e^x$ | $\sum_{n\ge0} \frac{x^n}{n!}$ | $\mathbb{R}$ |
| $\sinh x$ | $\sum_{n\ge0} \frac{x^{2n+1}}{(2n+1)!}$ | $\mathbb{R}$ |
| $\cosh x$ | $\sum_{n\ge0} \frac{x^{2n}}{(2n)!}$ | $\mathbb{R}$ |
| $\sin x$ | $\sum_{n\ge0} (-1)^n \frac{x^{2n+1}}{(2n+1)!}$ | $\mathbb{R}$ |
| $\cos x$ | $\sum_{n\ge0} (-1)^n \frac{x^{2n}}{(2n)!}$ | $\mathbb{R}$ |
| $\arctan x$ | $\sum_{n\ge0} (-1)^n \frac{x^{2n+1}}{2n+1}$ | $]-1, 1[$ |
| $\frac{1}{1-x}$ | $\sum_{n\ge0} x^n$ | $]-1, 1[$ |
| $\frac{1}{(1-x)^2}$ | $\sum_{n\ge1} n x^{n-1}$ | $]-1, 1[$ |
| $\frac{1}{1+x}$ | $\sum_{n\ge0} (-1)^n x^n$ | $]-1, 1[$ |
| $\ln(1+x)$ | $\sum_{n\ge1} (-1)^{n-1} \frac{x^n}{n}$ | $]-1, 1[$ |
| $(1+x)^a$, $a \in \mathbb{R}$ | $\sum_{n\ge0} \frac{a(a-1)\cdots(a-n+1)}{n!} x^n$ | $]-1, 1[$ |

Voir aussi [[Fonctions hyperboliques]] et [[Fonctions trigonométriques réciproques]].

## Applications

### Calcul de la somme d'une série numérique

On cherche $\frac{1}{1\cdot 2} - \frac{1}{2\cdot 2^2} + \frac{1}{3\cdot 2^3} - \frac{1}{4\cdot 2^4} + \dots$ On l'écrit
$$\sum_{n=1}^{+\infty} (-1)^{n-1}\frac{1}{n\cdot 2^n} = \sum_{n=1}^{+\infty} (-1)^{n-1}\frac{\left(\frac{1}{2}\right)^n}{n},$$
et la série de $\ln(1+x)$ en $x = \frac12$ donne
$$\sum_{n=1}^{+\infty} (-1)^{n-1}\frac{1}{n\cdot 2^n} = \ln\left(1+\frac{1}{2}\right) = \ln\frac{3}{2}.$$

### Approximation de $\pi$

On part de $\arctan x = \sum (-1)^n \frac{x^{2n+1}}{2n+1}$. En $x = 1$, la série est alternée et convergente, d'où
$$\pi = 4\sum_{n=0}^{+\infty} \frac{(-1)^n}{2n+1}.$$
Comme la série est alternée ([[Critère des séries alternées]]), $|R_n(1)| \le |a_{n+1}| = \frac{1}{2n+3}$. Selon le cours, pour une précision de $10^{-2}$, il faut $n \ge 49$ : cela vaut pour $\pi/4$ ; pour $\pi$, il faut $n \ge 199$ (voir « Erreurs du cours »).

### Approximation de $e$

$e^x = \sum \frac{x^n}{n!}$, donc en $x = 1$ : $e = \sum_{n=0}^{+\infty} \frac{1}{n!}$. Avec la forme de Lagrange, il existe $c$ entre 0 et 1 tel que $R_n(1) = \frac{f^{(n+1)}(c)}{(n+1)!}$. Toutes les dérivées de l'exponentielle sont égales à l'exponentielle, donc
$$0 \le R_n(1) = \frac{e^c}{(n+1)!} \le \frac{e}{(n+1)!} \le \frac{3}{(n+1)!}.$$
Pour une précision de $10^{-5}$, $n = 8$ suffit ($9! = 362\,880$). L'approximation est bien plus efficace que pour $\pi$.

## Erreurs du cours

- [[Raw/Year 3/Séries/Chp5 : power series.docx|Chp5 - power series]] écrit, dans l'inégalité de Taylor, « $\forall x \in [d - \alpha, d + \alpha]$ » (vérifié sur l'image) ; il faut « $[\alpha - d, \alpha + d]$ », cohérent avec $|x - \alpha| \le d$.
- [[Raw/Year 3/Séries/Chp5 : power series.docx|Chp5 - power series]] écrit que pour approcher $\pi$ à $10^{-2}$ « we need to take $n \geq 49$ » ; $|R_n(1)| \le \frac{1}{2n+3}$ porte sur la série $\sum \frac{(-1)^n}{2n+1}$, qui vaut $\pi/4$. Pour $10^{-2}$ sur $\pi$, il faut $\frac{4}{2n+3} \le 10^{-2}$, soit $n \ge 199$ ; $n \ge 49$ donne $10^{-2}$ sur $\pi/4$.
- [[Raw/Year 3/Séries/Chp5 : power series.docx|Chp5 - power series]] écrit la série de $\sin x$ avec « $-\frac{x^7}{7}$ » (vérifié sur l'image) ; il faut « $-\frac{x^7}{7!}$ ». Dans la majoration du reste, il écrit « $|x_t|^n$ » ; il faut « $|x - t|^n$ ».
- [[Raw/Year 3/Séries/Chp5 : power series.docx|Chp5 - power series]] écrit « $0 \le R_n(1) = \frac{e}{(n+1)!} \le \frac{3}{(n+1)!}$ » (vérifié sur l'image) ; il faut « $R_n(1) = \frac{e^c}{(n+1)!} \le \frac{e}{(n+1)!}$ ». La conclusion ($n = 8$ pour $10^{-5}$) reste juste.
- [[Raw/Year 3/Séries/Chp5 : power series.docx|Chp5 - power series]] écrit « $R_{\lambda a} = R_a$ and $\forall x \in \mathbb{R}, |x| \leq R_a \Rightarrow S_{\lambda a}(x) = \lambda S_a(x)$ » ; c'est faux pour $\lambda = 0$ (série nulle, $R = +\infty$), et il faut $|x| < R_a$, car la série peut diverger au bord. Même remarque pour « $|x| \leq \min(R_a, R_b)$ » dans la somme de deux séries.
- [[Raw/Year 3/Séries/Chp5 : power series.docx|Chp5 - power series]] écrit, pour la série du binôme, « If $-1 < a \leq 0$, then the series is conditionally convergent for $x = 1$ » ; il faut $-1 < a < 0$ : pour $a = 0$, la série se réduit à 1.
