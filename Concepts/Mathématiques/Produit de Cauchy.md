---
type: concept
tags: [year3]
aliases: [Cauchy product, produit de Cauchy de deux séries, convolution discrète]
sources: ["[[Raw/Year 3/Séries/Chp5 : power series.docx|Chp5 - power series]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : le produit de Cauchy de deux séries $\sum_{n \ge 0} a_n$ et $\sum_{n \ge 0} b_n$ est la série $\sum_{n \ge 0} c_n$ de terme général
$$c_n = \sum_{k=0}^{n} a_k\, b_{n-k} = a_0 b_n + a_1 b_{n-1} + \dots + a_n b_0.$$
On regroupe tous les produits $a_k b_l$ dont les indices ont la même somme $k + l = n$, comme on regroupe les termes de même degré en multipliant deux polynômes.

**Séries numériques.** Si $\sum a_n$ et $\sum b_n$ convergent absolument, alors $\sum c_n$ converge absolument et
$$\sum_{n=0}^{+\infty} c_n = \left(\sum_{n=0}^{+\infty} a_n\right)\left(\sum_{n=0}^{+\infty} b_n\right).$$
Il suffit même que l'une des deux converge absolument et l'autre converge (théorème de Mertens). Sans convergence absolue, le résultat tombe : le produit de Cauchy de la série alternée $\sum \frac{(-1)^n}{\sqrt{n+1}}$, convergente, par elle-même diverge, car $|c_n| \ge 1$ pour tout $n$.

**Séries entières.** Pour $\sum a_n x^n$ et $\sum b_n x^n$ de rayons $R_a$ et $R_b$, de sommes $S_a$ et $S_b$, la série produit $\sum c_n x^n$ a un rayon $R_c \ge \min(R_a, R_b)$, et
$$\forall x,\ |x| < \min(R_a, R_b) \Rightarrow S_c(x) = S_a(x)\, S_b(x).$$
Le rayon peut être strictement plus grand : $(1 - x)$ et $\sum x^n$ ont pour produit la série $1$, de rayon $+\infty$.

**Exemples.**
- $\left(\sum x^n\right)^2 = \sum_{n \ge 0} (n+1)x^n = \dfrac{1}{(1-x)^2}$ pour $|x| < 1$ : ici $a_k = b_k = 1$, donc $c_n = n + 1$.
- $e^x e^y = e^{x+y}$ : avec $a_k = \frac{x^k}{k!}$ et $b_k = \frac{y^k}{k!}$, $c_n = \sum_{k=0}^{n} \frac{x^k y^{n-k}}{k!(n-k)!} = \frac{(x+y)^n}{n!}$ par la [[Formule du binôme de Newton]].

## Dans le cours

Le cours ne la nomme pas. [[5 - power series]] traite la somme de deux séries entières et la multiplication par un scalaire ; le produit apparaît dans les compléments de la fiche, section « Opérations ».

Voir aussi : [[Série entière]], [[Série numérique]], [[Convergence conditionnelle]], [[Suite géométrique]], [[Formule du binôme de Newton]]

Résumés : [[5 - power series]]
