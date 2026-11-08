---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Séries/Chp5 : power series.docx|Chp5 - power series]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Séries/Chp5 : power series.docx|Chp5 - power series]], dans [[Cours/Mathématiques/Séries/_index|Séries]]. Cours en anglais. Toutes les images de la note sont des énoncés (texte et formules) : leur contenu est recopié ci-dessous, aucune n'est une figure.

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

**D'où vient ce théorème : le [[Lemme d'Abel]].** S'il existe $r > 0$ tel que la suite $(a_n r^n)$ soit bornée, alors $\sum a_n x^n$ converge absolument pour tout $|x| < r$. En effet, si $|a_n r^n| \le M$, alors $|a_n x^n| \le M \left|\frac{x}{r}\right|^n$, terme d'une série géométrique convergente. On en déduit la définition générale du rayon : $R = \sup\{r \ge 0 : (a_n r^n) \text{ est bornée}\}$, et les trois cas du théorème. [[Complément hors du cours|ⓘ]]

Le nom de « rayon » vient des séries entières à variable complexe : la série converge sur un **disque** ouvert $|z - \alpha| < R$ du plan complexe, dont l'intervalle réel n'est qu'un diamètre. Cela explique, par exemple, que $\frac{1}{1+x^2} = \sum (-1)^n x^{2n}$ ait un rayon 1 alors que la fonction est définie sur tout $\mathbb{R}$ : elle n'est pas définie en $z = \pm i$, à distance 1 de 0. [[Complément hors du cours|ⓘ]]

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

Exemples de chaque cas (centrés en 0) : [[Complément hors du cours|ⓘ]]

| Série | $R$ | Intervalle de convergence |
|---|---|---|
| $\sum n!\,x^n$ | 0 | $\{0\}$ |
| $\sum \frac{x^n}{n!}$ | $+\infty$ | $\mathbb{R}$ |
| $\sum x^n$ | 1 | $]-1, 1[$ (le terme ne tend pas vers 0 en $\pm 1$) |
| $\sum_{n\ge1} \frac{x^n}{n}$ | 1 | $[-1, 1[$ (série harmonique alternée en $-1$, harmonique en $1$) |
| $\sum_{n\ge1} \frac{(-1)^n x^n}{n}$ | 1 | $]-1, 1]$ |
| $\sum_{n\ge1} \frac{x^n}{n^2}$ | 1 | $[-1, 1]$ (convergence absolue en $\pm 1$) |

## Critères du rapport et de la racine

Voir [[Critère de d'Alembert et de Cauchy]].

**Proposition (rapport).** Si $R$ est le rayon de $\sum a_n(x-\alpha)^n$ et si $a_n \ne 0$ pour $n$ assez grand :
$$\lim_{n\to+\infty} \frac{|a_{n+1}|}{|a_n|} = \ell \in [0,+\infty] \ \Rightarrow\ R = \frac{1}{\ell}.$$

**Proposition (racine).** Sous les mêmes hypothèses :
$$\lim_{n\to+\infty} \sqrt[n]{|a_n|} = \ell \in [0,+\infty] \ \Rightarrow\ R = \frac{1}{\ell}.$$

Conventions : $\frac{1}{0} = +\infty$ et $\frac{1}{+\infty} = 0$.

Ces deux critères ne s'appliquent que si la limite existe. La **formule de Hadamard** donne le rayon dans tous les cas : $\frac{1}{R} = \limsup_{n\to+\infty} \sqrt[n]{|a_n|}$, avec les mêmes conventions. [[Complément hors du cours|ⓘ]]

**Remarque (coefficients lacunaires).** Quand des coefficients sont nuls (*gaps*), appliquer les critères aux termes complets de rangs $n$ et $n+1$ de la série, c'est-à-dire à $a_n(x-\alpha)^n$, et non aux seuls coefficients.

Exemple : $\sum_{n\ge0} \frac{x^{2n}}{4^n}$ n'a que des puissances paires. Le rapport de deux termes consécutifs non nuls vaut $\frac{x^{2n+2}/4^{n+1}}{x^{2n}/4^n} = \frac{x^2}{4}$ ; la série converge si $\frac{x^2}{4} < 1$ et diverge si $\frac{x^2}{4} > 1$, d'où $R = 2$. [[Complément hors du cours|ⓘ]]

## Opérations sur les séries entières

**Proposition (multiplication par un scalaire).** Soit $\lambda \in \mathbb{R}$ et $\sum a_n x^n$ de rayon $R_a$ et de somme $S_a$. Le rayon $R_{\lambda a}$ et la somme $S_{\lambda a}$ de $\sum \lambda a_n x^n$ vérifient
$$R_{\lambda a} = R_a \ (\lambda \ne 0) \quad\text{et}\quad \forall x,\ |x| < R_a \Rightarrow S_{\lambda a}(x) = \lambda S_a(x).$$
L'inégalité est stricte, car la série peut diverger au bord, et $\lambda = 0$ est exclu (série nulle, de rayon $+\infty$). [[Erreurs du cours#^e-5-power-series|✎]]

**Définition (somme).** La somme de $\sum a_n x^n$ et $\sum b_n x^n$ est $\sum (a_n + b_n)x^n$.

**Proposition.** Avec $R_a$, $R_b$ les rayons et $S_a$, $S_b$ les sommes, le rayon $R_{a+b}$ de la série somme vérifie $R_{a+b} \ge \min(R_a, R_b)$, et
$$\forall x,\ |x| < \min(R_a, R_b) \Rightarrow S_{a+b}(x) = S_a(x) + S_b(x).$$
Ici aussi l'inégalité est stricte. [[Erreurs du cours#^e-5-power-series|✎]]
De plus, si $R_a \ne R_b$, alors $R_{a+b} = \min(R_a, R_b)$.

Si $R_a = R_b$, le rayon de la somme peut être strictement plus grand : $\sum x^n$ et $\sum (-x^n)$ ont un rayon 1, leur somme est la série nulle, de rayon $+\infty$. [[Complément hors du cours|ⓘ]]

**Produit (de Cauchy).** Le [[Produit de Cauchy]] de $\sum a_n x^n$ et $\sum b_n x^n$ est $\sum c_n x^n$ avec $c_n = \sum_{k=0}^{n} a_k b_{n-k}$ : on développe le produit et on regroupe les termes de même degré, comme pour des polynômes. Son rayon vérifie $R_c \ge \min(R_a, R_b)$, et pour $|x| < \min(R_a, R_b)$, $S_c(x) = S_a(x)\,S_b(x)$. Exemple : $\frac{1}{(1-x)^2} = \left(\sum x^n\right)^2 = \sum (n+1)x^n$ pour $|x| < 1$. [[Complément hors du cours|ⓘ]]

Le cours annonce ensuite l'étude de la continuité de la somme, puis la **dérivation et l'intégration terme à terme** (*term-by-term differentiation and integration*).

## Continuité

**Théorème.** Soit $\sum a_n(x-\alpha)^n$ de rayon $R > 0$. La série converge normalement sur tout intervalle $[\alpha - r, \alpha + r]$ avec $0 < r < R$, donc la somme $S$ est continue sur $]\alpha - R, \alpha + R[$.
De plus, si $\sum a_n(-R)^n$ converge, $S$ est continue en $\alpha - R$ ; si $\sum a_n R^n$ converge, $S$ est continue en $\alpha + R$.

**Corollaire.** Dans ces conditions, si $\sum a_n(-R)^n$ converge, alors $S(\alpha - R) = \sum a_n(-R)^n$ ; si $\sum a_n R^n$ converge, alors $S(\alpha + R) = \sum a_n R^n$.

Ce résultat de continuité au bord porte le nom de **théorème d'Abel radial**. Il permet d'étendre une formule valable sur $]-R, R[$ à une borne où la série converge. Exemple : $\ln(1+x) = \sum_{n\ge1} (-1)^{n-1}\frac{x^n}{n}$ sur $]-1, 1[$ ; en $x = 1$, la série converge (série alternée) et $\ln(1+x)$ est continue en 1, d'où $\ln 2 = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \dots$ C'est le même argument qui justifie, plus bas, la formule de $\pi$ en $x = 1$ pour $\arctan$. [[Complément hors du cours|ⓘ]]

## Dérivation et intégration terme à terme

**Théorème (dérivation).** Si $R > 0$, la somme $S$ est dérivable sur $]\alpha - R, \alpha + R[$ et
$$\forall x \in\, ]\alpha - R, \alpha + R[,\quad S'(x) = \sum_{n=1}^{+\infty} n a_n (x-\alpha)^{n-1}.$$

**Théorème (intégration).** Si $R > 0$, la somme $S$ est intégrable sur $]\alpha - R, \alpha + R[$ et
$$\int S(x)\,dx = C + \sum_{n=0}^{+\infty} a_n \frac{(x-\alpha)^{n+1}}{n+1}.$$

La primitive qui s'annule en $\alpha$ correspond à $C = 0$ : $\int_\alpha^x S(t)\,dt = \sum_{n=0}^{+\infty} a_n \frac{(x-\alpha)^{n+1}}{n+1}$. C'est ainsi qu'on obtient de nouvelles séries usuelles à partir de la série géométrique. Exemple : pour $|t| < 1$, $\frac{1}{1+t^2} = \sum_{n\ge0} (-1)^n t^{2n}$ ; en intégrant de 0 à $x$, $\arctan x = \sum_{n\ge0} (-1)^n \frac{x^{2n+1}}{2n+1}$. De même, $\frac{1}{1+t} = \sum (-1)^n t^n$ donne $\ln(1+x)$, et la dérivation de $\frac{1}{1-x}$ donne $\frac{1}{(1-x)^2}$. [[Complément hors du cours|ⓘ]]

**Remarques.**
1. Le rayon de convergence reste le même après dérivation ou intégration, mais pas forcément l'intervalle de convergence : le comportement aux bornes peut changer. Une série peut converger en une borne alors que sa série dérivée y diverge.
2. Faits de base (série centrée en 0) : toute série entière a un rayon $0 \le R \le +\infty$ ; elle converge absolument pour $|x| < R$ et diverge pour $|x| > R$ ; la convergence est normale, donc uniforme, sur tout intervalle $|x| < r$ avec $0 \le r < R$ ; si $R > 0$, la somme est indéfiniment dérivable sur $|x| < R$, et ses dérivées s'obtiennent en dérivant terme à terme.

## Séries de Taylor et de Maclaurin

**Théorème (valeur des coefficients).** Si $f$ est développable en série entière en $\alpha$, $f(x) = \sum a_n (x-\alpha)^n$, alors
$$a_n = \frac{f^{(n)}(\alpha)}{n!}, \qquad \forall x \in\, ]\alpha - R, \alpha + R[,\ f(x) = \sum_{n=0}^{+\infty} \frac{f^{(n)}(\alpha)}{n!}(x-\alpha)^n.$$

**Définitions.**
- Cette série est la **série de Taylor** de $f$ en $\alpha$.
- En $\alpha = 0$, $\sum \frac{f^{(n)}(0)}{n!}x^n$ est la **série de Maclaurin** de $f$.

**Conséquence : unicité du développement.** Les coefficients étant déterminés par les dérivées de $f$ en $\alpha$, deux séries entières qui ont la même somme au voisinage de $\alpha$ ont les mêmes coefficients. On peut donc identifier les coefficients, comme pour des polynômes ; par exemple, si $f$ est paire, ses coefficients d'indice impair sont nuls. [[Complément hors du cours|ⓘ]]

### Polynômes de Taylor

**Définition.** Pour $f$ indéfiniment dérivable, le $n$-ième polynôme de Taylor de $f$ en $\alpha$ est
$$T_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(\alpha)}{k!}(x-\alpha)^k,$$
et le reste est $R_n(x) = f(x) - T_n(x)$. Voir [[Reste de Taylor]] et [[Développement limité]].

**Théorème (condition suffisante).** Si $\lim_{n\to+\infty} R_n(x) = 0$ pour $|x-\alpha| < R$, alors $f$ est la somme de sa série de Taylor sur $|x-\alpha| < R$.

Cette condition n'est pas automatique : une fonction indéfiniment dérivable n'est pas toujours égale à sa série de Taylor. Contre-exemple classique : $f(x) = e^{-1/x^2}$ pour $x \ne 0$ et $f(0) = 0$. Elle est de [[Fonction de classe Ck|classe $\mathcal{C}^\infty$]] sur $\mathbb{R}$ et toutes ses dérivées en 0 sont nulles : sa série de Maclaurin est la série nulle, de rayon $+\infty$, alors que $f(x) > 0$ pour $x \ne 0$. [[Complément hors du cours|ⓘ]]

### Inégalité de Taylor

**Théorème.** S'il existe $M > 0$ et $d > 0$ tels que, pour tout $x$ avec $|x-\alpha| \le d$ et pour tout $n$, $|f^{(n+1)}(x)| \le M$, alors
$$\forall x \in [\alpha - d, \alpha + d],\quad |R_n(x)| \le \frac{M}{(n+1)!}|x - \alpha|^{n+1}.$$
L'intervalle $[\alpha - d, \alpha + d]$ est celui des $x$ tels que $|x - \alpha| \le d$. [[Erreurs du cours#^e-5-power-series|✎]]

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

D'où [[Erreurs du cours#^e-5-power-series|✎]]
$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \ldots = \sum_{n=0}^{+\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!}.$$

**Étude du reste.** Pour tout $x$ et tout $n$, $|f^{(n)}(x)| \le 1$.
- Si $x > 0$ :
$$|R_n(x)| = \frac{1}{n!}\left|\int_0^x (x-t)^n f^{(n+1)}(t)\,dt\right| \le \frac{1}{n!}\int_0^x (x-t)^n\,dt = \frac{x^{n+1}}{(n+1)!}.$$
- Si $x < 0$ : $R_n(x) = -\frac{1}{n!}\int_x^0 (x-t)^n f^{(n+1)}(t)\,dt$, donc [[Erreurs du cours#^e-5-power-series|✎]]
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
2. $-1 < a < 0$ : [[Convergence conditionnelle|conditionnellement convergente]] en $x = 1$, divergente en $x = -1$ (pour $a = 0$, la série se réduit à 1). [[Erreurs du cours#^e-5-power-series|✎]]
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

Avec le théorème d'Abel radial (section « Continuité »), les formules de $\ln(1+x)$ et de $\arctan x$ restent vraies en $x = 1$, et celle de $\arctan x$ aussi en $x = -1$ : les intervalles de convergence exacts sont $]-1, 1]$ et $[-1, 1]$. [[Complément hors du cours|ⓘ]]

**Formule d'Euler.** En remplaçant $x$ par $ix$ dans la série de $e^x$ (qui a encore un sens pour une variable complexe) et en séparant les termes pairs et impairs, on retrouve les séries de $\cos$ et de $\sin$ : $e^{ix} = \cos x + i \sin x$. Voir [[Forme trigonométrique et exponentielle]]. [[Complément hors du cours|ⓘ]]

## Applications

### Calcul de la somme d'une série numérique

On cherche $\frac{1}{1\cdot 2} - \frac{1}{2\cdot 2^2} + \frac{1}{3\cdot 2^3} - \frac{1}{4\cdot 2^4} + \dots$ On l'écrit
$$\sum_{n=1}^{+\infty} (-1)^{n-1}\frac{1}{n\cdot 2^n} = \sum_{n=1}^{+\infty} (-1)^{n-1}\frac{\left(\frac{1}{2}\right)^n}{n},$$
et la série de $\ln(1+x)$ en $x = \frac12$ donne
$$\sum_{n=1}^{+\infty} (-1)^{n-1}\frac{1}{n\cdot 2^n} = \ln\left(1+\frac{1}{2}\right) = \ln\frac{3}{2}.$$

### Approximation de $\pi$

On part de $\arctan x = \sum (-1)^n \frac{x^{2n+1}}{2n+1}$. En $x = 1$, la série est alternée et convergente, d'où
$$\pi = 4\sum_{n=0}^{+\infty} \frac{(-1)^n}{2n+1}.$$
Comme la série est alternée ([[Critère des séries alternées]]), $|R_n(1)| \le |a_{n+1}| = \frac{1}{2n+3}$. Cette majoration porte sur la somme de la série, qui vaut $\pi/4$ : pour une précision de $10^{-2}$ sur $\pi/4$, il faut $n \ge 49$ ; pour $10^{-2}$ sur $\pi$, il faut $\frac{4}{2n+3} \le 10^{-2}$, soit $n \ge 199$. [[Erreurs du cours#^e-5-power-series|✎]]

Cette série (dite de Leibniz) converge donc très lentement. Les calculs effectifs de $\pi$ utilisent des valeurs de $x$ plus petites, où les termes décroissent vite : la **formule de Machin** (1706), $\frac{\pi}{4} = 4\arctan\frac{1}{5} - \arctan\frac{1}{239}$, fait gagner environ 1,4 décimale par terme avec $\arctan\frac15$ (les termes sont divisés par $25$ à chaque rang). [[Complément hors du cours|ⓘ]]

### Approximation de $e$

$e^x = \sum \frac{x^n}{n!}$, donc en $x = 1$ : $e = \sum_{n=0}^{+\infty} \frac{1}{n!}$. Avec la forme de Lagrange, il existe $c$ entre 0 et 1 tel que $R_n(1) = \frac{f^{(n+1)}(c)}{(n+1)!}$. Toutes les dérivées de l'exponentielle sont égales à l'exponentielle, donc [[Erreurs du cours#^e-5-power-series|✎]]
$$0 \le R_n(1) = \frac{e^c}{(n+1)!} \le \frac{e}{(n+1)!} \le \frac{3}{(n+1)!}.$$
Pour une précision de $10^{-5}$, $n = 8$ suffit ($9! = 362\,880$). L'approximation est bien plus efficace que pour $\pi$.
