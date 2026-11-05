---
type: concept
aliases: [boule ouverte, boules ouvertes, boule fermée, boules fermées, voisinage, voisinages]
matieres: [Analyse dans Rn, Analyse Maths, Analyse]
sources: ["[[Chp 2 - éléments de topologie dans Rn]]"]
maj: 2026-11-05
---

Dans un EVN :

- **Boule ouverte** : $B(a, r) = \{x \mid \|x - a\| < r\}$.
- **Boule fermée** : $\overline{B}(a, r) = \{x \mid \|x - a\| \le r\}$.
- **Sphère** : $S(a, r) = \{x \mid \|x - a\| = r\}$, et $\overline{B}(a, r) = B(a, r) \cup S(a, r)$.

La forme dépend de la norme. Dans $\mathbb{R}^2$, la boule fermée de rayon 1 est un losange pour $\|\cdot\|_1$, un disque pour $\|\cdot\|_2$ et un carré pour $\|\cdot\|_\infty$. Dans $\mathbb{R}$, c'est un intervalle centré en $a$.

**Voisinage** : $V$ est un voisinage de $a$ si $\exists r > 0$ tel que $B(a, r) \subset V$. Alors $a \in V$. Toute réunion, et toute intersection **finie**, de voisinages de $a$ est un voisinage de $a$. Une intersection infinie peut ne pas en être un : $\bigcap_n \,]-\frac{1}{n}, \frac{1}{n}[\, = \{0\}$. En dimension finie, être un voisinage ne dépend pas de la norme. Tout EVN est séparé : deux points distincts ont des voisinages disjoints.

Liens : [[Norme]], [[Ouvert et fermé]], [[Intérieur et adhérence]], [[Limite et continuité]]

Résumé : [[Chp 2 - éléments de topologie dans Rn (résumé)]]
