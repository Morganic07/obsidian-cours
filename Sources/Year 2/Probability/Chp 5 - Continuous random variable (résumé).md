---
type: source
sources: ["[[Chp 5 - Continuous random variable]]"]
maj: 2026-11-05
---

Résumé de [[Chp 5 - Continuous random variable]], dans [[Year 2 - Probability]]. En cas d'écart, le cours et ses images font foi. Les images n'ont pas été ouvertes : seules leurs transcriptions ont été lues.

## Idée générale

Reprendre le chapitre 4 pour les variables continues : les sommes deviennent des [[Intégrale|intégrales]] et la loi est une densité. Le chapitre présente aussi les lois uniforme, normale et exponentielle, la fonction génératrice des moments et le changement de variable.

## Contenu, dans l'ordre du cours

- **Densité** (pdf, à ne pas confondre avec la pmf) : $f$ telle que $P(a \le X \le b) = \int_a^b f(x)\,dx$. Conditions : $f \ge 0$ et $\int_{-\infty}^{\infty} f = 1$.
- **Loi uniforme** sur $[A, B]$ : $f = 1/(B-A)$ sur $[A, B]$, 0 ailleurs. Notation $X \sim \mathrm{Unif}[A, B]$.
- **Un point a probabilité nulle** : $P(X = c) = \int_c^c f = 0$. Inclure ou exclure les bornes ne change rien : $P(a \le X \le b) = P(a < X < b) = \dots$
- **[[Fonction de répartition]]** : $F(x) = \int_{-\infty}^x f(y)\,dy$, donc $F$ est une [[Primitive|primitive]] de $f$. $P(X > a) = 1 - F(a)$, $P(a \le X \le b) = F(b) - F(a)$, et $F'(x) = f(x)$ en tout point où la dérivée existe.
- **[[Espérance et variance]]** : $E(X) = \int x f(x)\,dx$, $E[h(X)] = \int h f$, $\mathrm{Var}(X) = \int (x-\mu)^2 f = E[(X-\mu)^2]$. Propriétés : formule raccourcie $E(X^2) - \mu^2$, **inégalité de Tchebychev** $P(|X - \mu| \ge k\sigma) \le 1/k^2$ pour $k \ge 1$, linéarité, $E(aX+b) = a\mu + b$, $\mathrm{Var}(aX+b) = a^2\sigma^2$, $\sigma_{aX+b} = |a|\sigma$.
- **[[Fonction génératrice des moments]]** : $M_X(t) = E(e^{tX}) = \int e^{tx}f(x)\,dx$. Elle existe si elle est définie sur un intervalle contenant 0 avec des $t$ positifs et négatifs. $M_X(0) = 1$, $E(X^r) = M_X^{(r)}(0)$. Elle détermine la loi.
- **[[Loi normale]]** : $f(x; \mu, \sigma) = \frac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/(2\sigma^2)}$, notée $N(\mu, \sigma)$. Règle 68-95-99,7 : $P(|X - \mu| < k\sigma) \approx 68\,\%$, $95\,\%$, $99{,}73\,\%$ pour $k = 1, 2, 3$.
- **Loi normale centrée réduite** : $Z \sim N(0, 1)$, de fonction de répartition $\Phi$. Si $X \sim N(\mu, \sigma)$, alors $Z = (X - \mu)/\sigma$ est centrée réduite et $P(a \le X \le b) = \Phi\!\left(\frac{b-\mu}{\sigma}\right) - \Phi\!\left(\frac{a-\mu}{\sigma}\right)$. Réciproquement $X = \mu + \sigma Z$. On lit alors $\Phi$ dans la table.
- **[[Loi exponentielle]]** : $f(x; \lambda) = \lambda e^{-\lambda x}$ pour $x > 0$. $F(x) = 1 - e^{-\lambda x}$ pour $x > 0$ ; moyenne et écart-type valent tous deux $1/\lambda$.
- **Médiane et percentiles** : le $(100p)$-ième percentile $\eta_p$ vérifie $p = F(\eta_p)$, soit $\eta_p = F^{-1}(p)$ si l'inverse existe. La médiane est $\eta_{0{,}5}$. Pour une densité symétrique, la médiane est le centre de symétrie.
- **Théorème de transformation** : si $Y = g(X)$ avec $g$ strictement monotone d'inverse $h$ dérivable, $f_Y(y) = f_X(h(y))\,|h'(y)|$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Notation de la loi normale** : le cours écrit $N(\mu, \sigma)$ (écart-type) pour la définition, puis $\mathcal{N}(\mu, \sigma^2)$ (variance) dans la règle 68-95-99,7. Il s'agit de la même loi, la seconde notation compte la variance. À ne pas confondre dans un exercice (complément).
2. **Tableau récapitulatif de la fonction génératrice** : il écrit $M_X^{(2)}(0) = E[X^2]$ puis « ... ». C'est cohérent avec $E(X^r) = M^{(r)}_X(0)$. Le chapitre précédent n'ayant pas de section sur la fonction génératrice, la phrase « as in the discrete case » renvoie à un cas absent des notes (complément).
3. **Deux alertes de lecture seulement** : le coin coupé de la proposition $F' = f$ et le « (A) » de la dernière image ne gênent pas le sens. Fausses alertes sur le fond.
4. **Percentile** : le $p$ lu sur le graphique de $F(x)$ (entre 0,2 et 0,4) est illisible. Aucun chiffre n'est repris dans le wiki.
