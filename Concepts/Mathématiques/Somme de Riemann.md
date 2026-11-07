---
type: concept
tags:
  - year2
aliases:
  - sommes de Riemann
  - somme de Riemann d'ordre n
  - méthode des rectangles à gauche
  - méthode des rectangles à droite
sources:
  - "[[1 - Integration|Chap7-Integration]]"
  - "[[1 - démonstrations|démonstrations - integration]]"
maj: 2026-11-07
---

Somme de Riemann d'ordre $n$ associée à $f:[a,b]\to\mathbb{R}$ :
$$\frac{b-a}{n}\sum_{k=0}^{n-1} f(a_k),\qquad a_k=a+k\frac{b-a}{n}$$
(rectangles « à gauche »). On a le même résultat avec $R'_n = \frac{b-a}{n}\sum_{k=1}^{n} f(a_k)$, méthode des rectangles « à droite ».

C'est l'intégrale d'une fonction en escalier (méthode des rectangles). Elle converge vers $\int_a^b f$, avec une erreur en $1/n$. La preuve est faite pour $f$ $K$-lipschitzienne, avec une erreur majorée par $K(b-a)^2/n$.

Le TD7 (ex. 13-14) fait reconnaître des sommes de la forme $\frac1n\sum f(k/n)$.

Notion parente : [[Intégrale]]. Voir aussi : [[Subdivision]], [[Application lipschitzienne]], [[Méthode des trapèzes]].

## Erreurs du cours

- [[1 - Integration|Chap7-Integration]] (image vérifiée) écrit la somme de Riemann avec « $\sum_{k=1}^{n}$ », puis la décrit comme la fonction en escalier valant $f(a_k)$ pour $0 \le k \le n-1$ et donne « le même résultat avec $R'_n$ » écrit lui aussi avec $\sum_{k=1}^{n}$ ; la première somme doit porter sur $k = 0, \dots, n-1$ (rectangles à gauche).

Résumés : [[1 - Integration]], [[1 - démonstrations]], [[0 - Intégration UTILITAIRE]]
