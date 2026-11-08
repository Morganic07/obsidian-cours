---
type: concept
tags: [year2]
aliases: [intégrale gaussienne, Gaussian integral, intégrale d'Euler-Poisson]
sources: ["[[Raw/Year 2/Analyse/Chp9-intégrales multiples.pdf|Chp9-intégrales multiples.pdf]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** :
$$I = \int_{-\infty}^{+\infty} e^{-x^2}\,dx = \sqrt{\pi}.$$
L'intégrale converge (pour $|x| \ge 1$, $e^{-x^2} \le e^{-|x|}$), mais $x \mapsto e^{-x^2}$ n'a pas de [[Primitive]] exprimable avec les fonctions usuelles : on ne peut pas la calculer par une primitive, d'où le détour par une intégrale double.

**Calcul classique.** Par [[Intégrale multiple|Fubini]], $I^2 = \left(\int_{\mathbb{R}} e^{-x^2}dx\right)\left(\int_{\mathbb{R}} e^{-y^2}dy\right) = \iint_{\mathbb{R}^2} e^{-(x^2+y^2)}\,dx\,dy$. En [[Coordonnées polaires]] ($dx\,dy = r\,dr\,d\theta$) :
$$I^2 = \int_0^{2\pi}\!\!\int_0^{+\infty} e^{-r^2}\, r\,dr\,d\theta = 2\pi \left[-\tfrac12 e^{-r^2}\right]_0^{+\infty} = 2\pi\cdot\frac12 = \pi.$$
Le passage à $\mathbb{R}^2$ tout entier se justifie par une limite sur les disques $D_R$ de rayon $R \to +\infty$ : $\iint_{D_R} e^{-(x^2+y^2)}\,dx\,dy = \pi\left(1 - e^{-R^2}\right) \to \pi$, et les carrés $[-R,R]^2$ sont encadrés par les disques $D_R$ et $D_{R\sqrt2}$. Comme $I > 0$, $I = \sqrt{\pi}$.

**Conséquences.**
- Par le changement de variable $x = t/\sqrt2$ : $\displaystyle\int_{-\infty}^{+\infty} e^{-t^2/2}\,dt = \sqrt{2\pi}$.
- Plus généralement, pour $\sigma > 0$ : $\displaystyle\int_{-\infty}^{+\infty} e^{-\frac{(x-\mu)^2}{2\sigma^2}}\,dx = \sigma\sqrt{2\pi}$, d'où la constante $\frac{1}{\sigma\sqrt{2\pi}}$ qui fait de la densité de la [[Loi normale]] une densité de probabilité (intégrale égale à 1).
- Par parité ([[Parité et périodicité d'une intégrale]]) : $\displaystyle\int_0^{+\infty} e^{-x^2}\,dx = \frac{\sqrt\pi}{2}$.

## Dans le cours

Le cours ne la nomme pas. Elle apparaît dans les compléments de [[2 - intégrales multiples]], comme application du passage en coordonnées polaires.

Voir aussi : [[Intégrale multiple]], [[Coordonnées polaires]], [[Loi normale]], [[Changement de variable dans une intégrale]].

Résumés : [[2 - intégrales multiples]]
