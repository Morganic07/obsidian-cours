---
type: concept
tags: [year3]
aliases: [séries entières, power series, rayon de convergence, radius of convergence, intervalle de convergence, série de Taylor, série de Maclaurin, Taylor series, Maclaurin series, série binomiale, polynôme de Taylor, Taylor polynomial, formule de Hadamard, Cauchy-Hadamard formula, théorème d'Abel radial, Abel's theorem]
matieres: [Séries]
sources: ["[[5 - power series|Chp5 - power series]]"]
maj: 2026-11-08
---

**Définition** (d'après [[5 - power series]]) : série de fonctions $\sum a_n(x - \alpha)^n$. Trois cas : convergence en $\alpha$ seulement ($R = 0$), partout ($R = +\infty$), ou rayon $0 < R < +\infty$ avec convergence absolue pour $|x - \alpha| < R$ et divergence pour $|x - \alpha| > R$. Le rayon est unique. Aux bords, tout peut arriver, y compris une [[Convergence conditionnelle|convergence conditionnelle]] (série binomiale en 1 pour $-1 < a < 0$). Le rayon se calcule avec $\lim \frac{|a_{n+1}|}{|a_n|}$ ou $\lim \sqrt[n]{|a_n|}$ égale à $\ell$ : $R = 1/\ell$ ([[Critère de d'Alembert et de Cauchy]]).

**Formule de Hadamard** : $\frac{1}{R} = \limsup_{n \to +\infty} \sqrt[n]{|a_n|}$ (avec $1/0 = +\infty$ et $1/(+\infty) = 0$). Elle donne le rayon dans tous les cas, même quand les limites des critères du rapport et de la racine n'existent pas (par exemple quand la moitié des coefficients est nulle, comme pour $\sum x^{2n}$). Le rayon se définit aussi par $R = \sup\{r \ge 0 : (a_n r^n) \text{ bornée}\}$, ce qui découle du [[Lemme d'Abel]]. [[Complément hors du cours|ⓘ]]

**Propriétés** : convergence normale sur tout $[\alpha - r, \alpha + r]$ avec $r < R$, somme continue et indéfiniment dérivable sur $]\alpha - R, \alpha + R[$, dérivation et intégration terme à terme avec le même rayon (voir [[Interversion de limites]]).

**Opérations** : pour $\lambda \neq 0$, $\sum \lambda a_n x^n$ a le même rayon $R_a$ (pour $\lambda = 0$, la série nulle est de rayon $+\infty$) [[Erreurs du cours#^e-serie-entiere|✎]] ; la somme a un rayon $\ge \min(R_a, R_b)$ ; le produit se fait par le [[Produit de Cauchy]], $c_n = \sum_{k=0}^{n} a_k b_{n-k}$, de rayon $\ge \min(R_a, R_b)$, avec $S_c = S_a S_b$ sur $|x| < \min(R_a, R_b)$. Exemple : $\left(\sum x^n\right)^2 = \sum (n+1)x^n = \frac{1}{(1-x)^2}$ pour $|x| < 1$. [[Complément hors du cours|ⓘ]]

**Théorème d'Abel radial** : si $\sum a_n R^n$ converge, la somme $S$ est continue en $R$ à gauche, c'est-à-dire $\lim_{x \to R^-} S(x) = \sum a_n R^n$ (et de même en $-R$ si $\sum a_n (-R)^n$ converge ; la série est centrée en 0 ici). Il permet d'étendre une formule valable sur $]-R, R[$ à une borne où la série converge : de $\ln(1+x) = \sum_{n \ge 1} (-1)^{n-1}\frac{x^n}{n}$ sur $]-1, 1[$, on tire $\ln 2 = \sum_{n \ge 1} \frac{(-1)^{n-1}}{n}$ ; de même, $\frac{\pi}{4} = \sum_{n \ge 0} \frac{(-1)^n}{2n+1}$ avec $\arctan$. [[Complément hors du cours|ⓘ]]

**Taylor** : si $f = \sum a_n(x - \alpha)^n$, alors $a_n = \frac{f^{(n)}(\alpha)}{n!}$ (série de Maclaurin en $\alpha = 0$). Le polynôme de Taylor d'ordre $n$ est $T_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(\alpha)}{k!}(x-\alpha)^k$. [[Reste de Taylor]] sous forme intégrale, de Lagrange, ou par inégalité de Taylor. Séries usuelles : $e^x$, $\sin$, $\cos$, $\sinh$, $\cosh$ ([[Fonctions hyperboliques]]) sur $\mathbb{R}$ ; $\frac{1}{1-x}$, $\ln(1+x)$, $\arctan$, $(1+x)^a$ sur $]-1, 1[$. Applications : somme d'une série numérique ($\ln(3/2)$), approximation de $\pi$ (la série $\sum \frac{(-1)^n}{2n+1}$ vaut $\pi/4$ avec $|R_n(1)| \le \frac{1}{2n+3}$ : $n \ge 49$ pour $10^{-2}$ sur $\pi/4$, $n \ge 199$ pour $10^{-2}$ sur $\pi$) [[Erreurs du cours#^e-serie-entiere|✎]] et de $e$.

**Unicité du développement** : les coefficients étant déterminés par $a_n = \frac{f^{(n)}(\alpha)}{n!}$, deux séries entières de même somme au voisinage de $\alpha$ ont les mêmes coefficients ; on peut donc identifier les coefficients, et une fonction paire n'a que des coefficients d'indice pair. [[Complément hors du cours|ⓘ]]

**Une fonction $\mathcal{C}^\infty$ n'est pas toujours développable en série entière** : $f(x) = e^{-1/x^2}$ pour $x \neq 0$, $f(0) = 0$, est de [[Fonction de classe Ck|classe $\mathcal{C}^\infty$]] sur $\mathbb{R}$ avec $f^{(n)}(0) = 0$ pour tout $n$ ; sa série de Maclaurin est nulle (rayon $+\infty$), alors que $f(x) > 0$ pour $x \neq 0$. Il faut donc que le [[Reste de Taylor]] tende vers 0. [[Complément hors du cours|ⓘ]]

Voir aussi : [[Lemme d'Abel]], [[Produit de Cauchy]], [[Fonction de classe Ck]], [[Développement limité]], [[Convergence uniforme]], [[Série numérique]], [[Reste de Taylor]], [[Critère de d'Alembert et de Cauchy]], [[Interversion de limites]], [[Fonctions hyperboliques]], [[Convergence conditionnelle]]

Résumé : [[5 - power series]]
