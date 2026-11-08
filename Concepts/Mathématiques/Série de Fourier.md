---
type: concept
tags: [year3]
aliases: [séries de Fourier, Fourier series, coefficients de Fourier, phénomène de Gibbs, Gibbs phenomenon, égalité de Parseval, Parseval's identity, square wave, fonction créneau, inégalité de Bessel, Bessel's inequality, forme complexe de Fourier, complex Fourier series, problème de Bâle, Basel problem]
matieres: [Séries]
sources: ["[[6 - Fourier Series|Chp6 - Fourier Series]]"]
maj: 2026-11-08
---

**Définition** (d'après [[6 - Fourier Series]]) : à une fonction $f$ $2\pi$-périodique et continue par morceaux, on associe $FS(f)(x) = a_0 + \sum_{n \ge 1}(a_n\cos nx + b_n\sin nx)$ avec $a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} f$, $a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f\cos nx$, $b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f\sin nx$. Cette série n'est pas toujours égale à $f$.

- **Parité** : $f$ paire donne $b_n = 0$ ; $f$ impaire donne $a_n = 0$ ; les intégrales se font sur $[0, \pi]$.
- **Convergence simple** : si $f$ et $f'$ sont continues par morceaux, la somme vaut $f(x)$ en un point de continuité et $\frac{1}{2}(f(x^+) + f(x^-))$ en un saut.
- **Convergence normale** : $f$ continue et $f'$ continue par morceaux.
- **Gibbs** : les sommes partielles dépassent près des sauts. Exemple du cours : la fonction créneau (square wave) valant 0 sur $[-\pi, 0)$ et 1 sur $(0, \pi]$, approchée par $S_1, S_3, \dots, S_{15}$.
- **Parseval** : $a_0^2 + \frac{1}{2}\sum(a_n^2 + b_n^2) = \frac{1}{2\pi}\int_{-\pi}^{\pi} f^2$.

Convention du cours : la série commence par $a_0$ (la moyenne), non par $a_0/2$.

## Compléments

- **Orthogonalité**, d'où viennent les formules des coefficients : pour le [[Produit scalaire]] $\langle f, g\rangle = \int_{-\pi}^{\pi} f g$, les fonctions $1, \cos nx, \sin nx$ sont deux à deux orthogonales. Pour $m, n \ge 1$, $\int_{-\pi}^{\pi} \cos mx \cos nx\,dx = \int_{-\pi}^{\pi} \sin mx \sin nx\,dx = \pi$ si $m = n$, $0$ sinon ; $\int_{-\pi}^{\pi} \cos mx \sin nx\,dx = 0$ pour tous $m, n$ ; $\int_{-\pi}^{\pi} 1 = 2\pi$. En multipliant la série par $\cos nx$ (ou $\sin nx$) et en intégrant, un seul terme survit, ce qui donne $a_n$ (ou $b_n$). $a_0$ est la valeur moyenne de $f$ sur une période. Voir [[Famille orthogonale]]. [[Complément hors du cours|ⓘ]]
- **Période $T$ quelconque** : avec $\omega = \frac{2\pi}{T}$, $FS(f)(x) = a_0 + \sum_{n \ge 1}(a_n \cos n\omega x + b_n \sin n\omega x)$, où $a_0 = \frac{1}{T}\int_0^T f$, $a_n = \frac{2}{T}\int_0^T f(x)\cos n\omega x\,dx$, $b_n = \frac{2}{T}\int_0^T f(x)\sin n\omega x\,dx$ (toute période d'intégration de longueur $T$ convient). [[Complément hors du cours|ⓘ]]
- **Forme complexe** : $FS(f)(x) = \sum_{n \in \mathbb{Z}} c_n e^{inx}$ avec $c_n = \frac{1}{2\pi}\int_{-\pi}^{\pi} f(x) e^{-inx}\,dx$. Avec la convention du cours, $c_0 = a_0$, et pour $n \ge 1$, $c_n = \frac{a_n - i b_n}{2}$, $c_{-n} = \frac{a_n + i b_n}{2}$. Voir [[Forme trigonométrique et exponentielle]]. [[Complément hors du cours|ⓘ]]
- **Créneau du cours** : $a_0 = \frac{1}{2}$, $a_n = 0$, $b_n = \frac{1 - (-1)^n}{n\pi}$, donc $FS(f)(x) = \frac{1}{2} + \frac{2}{\pi}\sum_{k \ge 0} \frac{\sin((2k+1)x)}{2k+1}$. Le dépassement de Gibbs vaut environ 9 % du saut et ne diminue pas quand on ajoute des termes : il se rapproche du saut sans disparaître, signe que la convergence n'est pas uniforme au voisinage d'une discontinuité (une limite uniforme de fonctions continues serait continue, voir [[Convergence uniforme]]). [[Complément hors du cours|ⓘ]]
- **Inégalité de Bessel** : pour tout $N$, $a_0^2 + \frac{1}{2}\sum_{n=1}^{N}(a_n^2 + b_n^2) \le \frac{1}{2\pi}\int_{-\pi}^{\pi} f^2$ ; la série des $a_n^2 + b_n^2$ converge donc, et $a_n \to 0$, $b_n \to 0$ (lemme de Riemann-Lebesgue). Parseval en est le cas d'égalité. [[Complément hors du cours|ⓘ]]
- **Sommes de séries numériques** : le théorème de Dirichlet en $x = \frac{\pi}{2}$ sur le créneau (où $f = 1$) donne $1 - \frac{1}{3} + \frac{1}{5} - \dots = \frac{\pi}{4}$. Parseval sur le même créneau donne $\frac{1}{4} + \frac{2}{\pi^2}\sum_{k \ge 0}\frac{1}{(2k+1)^2} = \frac{1}{2}$, soit $\sum_{k \ge 0} \frac{1}{(2k+1)^2} = \frac{\pi^2}{8}$ ; en séparant pairs et impairs, $S = \sum_{n \ge 1}\frac{1}{n^2}$ vérifie $S = \frac{\pi^2}{8} + \frac{S}{4}$, d'où $S = \frac{\pi^2}{6}$ (problème de Bâle, résolu par Euler). [[Complément hors du cours|ⓘ]]
- **Coefficients de la dérivée** : si $f$ est continue, $2\pi$-périodique et $f'$ continue par morceaux, une [[Intégration par parties]] donne $a_n(f') = n\,b_n(f)$ et $b_n(f') = -n\,a_n(f)$. Avec Bessel appliqué à $f'$ et l'[[Inégalité de Cauchy-Schwarz]], $\sum(|a_n| + |b_n|)$ converge : c'est l'idée de la preuve de la convergence normale. [[Complément hors du cours|ⓘ]]

Liens : [[Série numérique]], [[Produit scalaire]], [[Famille orthogonale]], [[Intégrale]], [[Convergence uniforme]], [[Fonction continue par morceaux]], [[Fonction périodique]], [[Fonction paire et impaire]]

Résumé : [[6 - Fourier Series]]
