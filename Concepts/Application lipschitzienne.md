---
type: concept
aliases: [lipschitzienne, lipschitziennes, lipschitzien, k-lipschitzien, k-lipschitzienne, M-lipschitzienne, uniformément continue, continuité uniforme]
matieres: [Analyse dans Rn, Analyse Maths, Analyse]
sources: ["[[Chp 3 - Limite et continuité d’applications]]", "[[Chp 4 - Calcul différentiel du premier ordre]]"]
maj: 2026-11-05
---

$f$ est $k$-lipschitzienne sur $A$ si $\forall x, y \in A, \|f(x) - f(y)\|_F \le k\|x - y\|_E$.

**Continuité uniforme** : $\forall \epsilon > 0, \exists \delta > 0, \forall x, y, d_E(x, y) < \delta \Rightarrow d_F(f(x), f(y)) < \epsilon$. Le $\delta$ est le même partout, alors qu'en continuité classique il peut dépendre du point.

**Avec le gradient** : sur un ouvert convexe, si $f$ est $\mathcal{C}^1$ et si $\|\vec{\nabla}_xf\|_1 \le M$, alors $f$ est $M$-lipschitzienne. $f$ est constante si et seulement si elle est 0-lipschitzienne.

> [!warning] Écart dans le cours
> Une note de [[Chp 3 - Limite et continuité d’applications]] écrit « $k$-lipschitzien ⇔ uniformément continue ». Seule l'implication ⇒ est vraie : $\sqrt{x}$ sur $[0, 1]$ est uniformément continue, sans être lipschitzienne (complément).

Liens : [[Limite et continuité]], [[Gradient]], [[Norme]]

Résumés : [[Chp 3 - Limite et continuité d’applications (résumé)]], [[Chp 4 - Calcul différentiel du premier ordre (résumé)]]
