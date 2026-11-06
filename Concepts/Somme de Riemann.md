---
type: concept
aliases: [sommes de Riemann, somme de Riemann d'ordre n, méthode des rectangles à gauche, méthode des rectangles à droite]
sources: ["[[Chap7-Integration]]", "[[démonstrations - integration]]"]
maj: 2026-11-06
---

Somme de Riemann d'ordre $n$ associée à $f:[a,b]\to\mathbb{R}$ :
$$\frac{b-a}{n}\sum f(a_k),\qquad a_k=a+k\frac{b-a}{n}.$$

C'est l'intégrale d'une fonction en escalier (méthode des rectangles). Elle converge vers $\int_a^b f$, avec une erreur en $1/n$. La preuve est faite pour $f$ $K$-lipschitzienne, avec une erreur majorée par $K(b-a)^2/n$.

Le TD7 (ex. 13-14) fait reconnaître des sommes de la forme $\frac1n\sum f(k/n)$.

Notion parente : [[Intégrale]]. Voir aussi : [[Subdivision]], [[Application lipschitzienne]], [[Méthode des trapèzes]].

## À vérifier

La formule du cours porte sur $k=1,\dots,n$ (rectangles à droite), mais la remarque qui suit décrit $f(a_k)$ pour $0\le k\le n-1$ (rectangles à gauche) ([[Chap7-Integration (résumé)]], point 1).

Résumés : [[Chap7-Integration (résumé)]], [[démonstrations - integration (résumé)]], [[Intégration UTILITAIRE (résumé)]], [[TD7-integration (1) (résumé)]]
