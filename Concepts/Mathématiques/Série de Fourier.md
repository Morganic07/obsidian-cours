---
type: concept
tags: [year3]
aliases: [séries de Fourier, Fourier series, coefficients de Fourier, phénomène de Gibbs, Gibbs phenomenon, égalité de Parseval, Parseval's identity, square wave, fonction créneau]
matieres: [Séries]
sources: ["[[Chp6 - Fourier Series (résumé)|Chp6 - Fourier Series]]"]
maj: 2026-11-06
---

À une fonction $f$ $2\pi$-périodique et continue par morceaux, on associe $FS(f)(x) = a_0 + \sum_{n \ge 1}(a_n\cos nx + b_n\sin nx)$ avec $a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} f$, $a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f\cos nx$, $b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f\sin nx$. Cette série n'est pas toujours égale à $f$.

- **Parité** : $f$ paire donne $b_n = 0$ ; $f$ impaire donne $a_n = 0$ ; les intégrales se font sur $[0, \pi]$.
- **Convergence simple** : si $f$ et $f'$ sont continues par morceaux, la somme vaut $f(x)$ en un point de continuité et $\frac{1}{2}(f(x^+) + f(x^-))$ en un saut.
- **Convergence normale** : $f$ continue et $f'$ continue par morceaux.
- **Gibbs** : les sommes partielles dépassent près des sauts. Exemple du cours : la fonction créneau (square wave) valant 0 sur $[-\pi, 0)$ et 1 sur $(0, \pi]$, approchée par $S_1, S_3, \dots, S_{15}$.
- **Parseval** : $a_0^2 + \frac{1}{2}\sum(a_n^2 + b_n^2) = \frac{1}{2\pi}\int_{-\pi}^{\pi} f^2$.

Convention du cours : la série commence par $a_0$ (la moyenne), non par $a_0/2$.

Liens : [[Intégrale]], [[Convergence uniforme]], [[Fonction continue par morceaux]], [[Fonction périodique]], [[Fonction paire et impaire]]

Résumé : [[Chp6 - Fourier Series (résumé)]]
