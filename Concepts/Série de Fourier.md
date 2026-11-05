---
type: concept
aliases: [séries de Fourier, Fourier series, coefficients de Fourier, phénomène de Gibbs, Gibbs phenomenon, égalité de Parseval, Parseval's identity]
matieres: [Séries]
sources: ["[[Chp6 - Fourier Series]]"]
maj: 2026-11-05
---

À une fonction $f$ $2\pi$-périodique et continue par morceaux, on associe $FS(f)(x) = a_0 + \sum_{n \ge 1}(a_n\cos nx + b_n\sin nx)$ avec $a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} f$, $a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f\cos nx$, $b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f\sin nx$. Cette série n'est pas toujours égale à $f$.

- **Parité** : $f$ paire donne $b_n = 0$ ; $f$ impaire donne $a_n = 0$ ; les intégrales se font sur $[0, \pi]$.
- **Convergence simple** : si $f$ et $f'$ sont continues par morceaux, la somme vaut $f(x)$ en un point de continuité et $\frac{1}{2}(f(x^+) + f(x^-))$ en un saut.
- **Convergence normale** : $f$ continue et $f'$ continue par morceaux.
- **Gibbs** : les sommes partielles dépassent près des sauts.
- **Parseval** : $a_0^2 + \frac{1}{2}\sum(a_n^2 + b_n^2) = \frac{1}{2\pi}\int_{-\pi}^{\pi} f^2$.

Convention du cours : la série commence par $a_0$ (la moyenne), non par $a_0/2$.

Liens : [[Intégrale]], [[Convergence uniforme]]

Résumé : [[Chp6 - Fourier Series (résumé)]]
