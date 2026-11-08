---
type: concept
tags:
  - year2
aliases:
  - intégrales
  - fonction en escalier
  - fonctions en escalier
  - méthode des rectangles
  - intégrale d'une fonction en escalier
  - intégrale d'une fonction continue
  - fonction en escalier adaptée
matieres:
  - Analyse
  - Analyse Maths
  - Analyse dans Rn
  - Probability
  - Séries
sources:
  - "[[1 - Integration|Chap7-Integration]]"
  - "[[1 - démonstrations|démonstrations - integration]]"
  - "[[0 - Intégration UTILITAIRE|Intégration UTILITAIRE]]"
maj: 2026-11-08
---

**Construction** : une fonction en escalier est constante sur chaque intervalle d'une [[Subdivision|subdivision]] adaptée ; son intégrale est $\sum y_i(x_{i+1} - x_i)$, qui ne dépend pas de la subdivision. Une fonction continue sur $[a, b]$ s'encadre par des fonctions en escalier $\varphi \le f \le \psi$ avec $\psi - \varphi \le \varepsilon$. Son intégrale est le sup des $\int\varphi$, égal à l'inf des $\int\psi$ ([[Borne supérieure]]).

**Propriétés**, pour $f$ et $g$ continues :

- Linéarité et [[Relation de Chasles|relation de Chasles]], aussi pour $a$, $b$, $c$ quelconques, avec $\int_a^b = -\int_b^a$.
- Si $a \le b$ : positivité, croissance, $\left|\int_a^b f\right| \le \int_a^b |f|$, et $m(b - a) \le \int_a^b f \le M(b - a)$ si $m \le f \le M$ ([[Inégalité de la moyenne]]).
- Valeur moyenne : $\mu = \frac{1}{b - a}\int_{[a,b]} f$.
- Une fonction continue, positive, d'intégrale nulle est nulle. Sans continuité, c'est faux.
- Période $T$ : $\int_a^{a+T} f$ ne dépend pas de $a$. Fonction paire : $\int_{-a}^a f = 2\int_0^a f$. Fonction impaire : $\int_{-a}^a f = 0$.

**Calcul approché** :

- **[[Somme de Riemann]]** : $\frac{b - a}{n}\sum_{k=1}^{n} f\left(a + k\frac{b - a}{n}\right) \to \int_a^b f$. C'est la méthode des rectangles, avec une erreur en $1/n$.
- **[[Méthode des trapèzes]]** : $T_n(f) = \frac{b - a}{n}\sum_{k=0}^{n-1} \frac{f(a_k) + f(a_{k+1})}{2}$, avec une erreur au plus $M_2\frac{(b - a)^3}{12n^2}$ si $f$ est $\mathcal{C}^2$.

Le calcul exact passe par une [[Primitive]].

En plusieurs variables : [[Intégrale multiple]]. Une série à termes positifs se compare à une intégrale : voir [[Série numérique]].

Liens : [[Primitive]], [[Limite et continuité]], [[Application lipschitzienne]], [[Intégrale multiple]]

Résumés : [[1 - Integration]], [[1 - démonstrations]], [[0 - Intégration UTILITAIRE]], [[5 - Continuous random variable]]
