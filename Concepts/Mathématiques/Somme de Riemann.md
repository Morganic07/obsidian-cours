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
  - "[[Raw/Year 2/Analyse/chp7/démonstrations - integration .docx|démonstrations - integration]]"
maj: 2026-11-08
---

Somme de Riemann d'ordre $n$ associée à $f:[a,b]\to\mathbb{R}$ :
$$\frac{b-a}{n}\sum_{k=0}^{n-1} f(a_k),\qquad a_k=a+k\frac{b-a}{n}$$
(rectangles « à gauche »). [[Erreurs du cours#^e-somme-de-riemann|✎]] On a le même résultat avec $R'_n = \frac{b-a}{n}\sum_{k=1}^{n} f(a_k)$, méthode des rectangles « à droite ».

C'est l'intégrale d'une fonction en escalier (méthode des rectangles). Elle converge vers $\int_a^b f$, avec une erreur en $1/n$. La preuve est faite pour $f$ $K$-lipschitzienne, avec une erreur majorée par $K(b-a)^2/n$.

Le TD7 (ex. 13-14) fait reconnaître des sommes de la forme $\frac1n\sum f(k/n)$.

## Compléments (hors du cours)

**Borne plus fine.** Pour $f$ $K$-lipschitzienne, en majorant sur chaque intervalle $[a_k, a_{k+1}]$ de longueur $h = \frac{b-a}{n}$ :
$$\left|\int_{a_k}^{a_{k+1}} f - h f(a_k)\right| \le \int_{a_k}^{a_{k+1}} K(t-a_k)\,dt = \frac{K h^2}{2},$$
d'où, en sommant les $n$ intervalles, $\left|\int_a^b f - R_n\right| \le \dfrac{K(b-a)^2}{2n}$. Pour $f$ de classe $C^1$, on prend $K = M_1 = \sup_{[a,b]}|f'|$ ([[Inégalité des accroissements finis]]) : erreur $\le \dfrac{M_1(b-a)^2}{2n}$.

**Cas d'une fonction seulement continue.** La convergence $R_n \to \int_a^b f$ reste vraie : par le théorème de Heine, $f$ est uniformément continue sur le segment ([[Continuité uniforme]]), donc pour tout $\varepsilon > 0$ il existe $n_0$ tel que $|f(t) - f(a_k)| \le \varepsilon$ sur chaque intervalle dès que $n \ge n_0$, et l'erreur est majorée par $\varepsilon(b-a)$. On n'obtient en revanche aucune vitesse de convergence.

**Calcul de limites.** Le cas $[a,b] = [0,1]$ donne
$$\frac1n\sum_{k=1}^{n} f\!\left(\frac kn\right) \xrightarrow[n\to+\infty]{} \int_0^1 f(t)\,dt.$$
Exemple : $\displaystyle\sum_{k=1}^{n} \frac{1}{n+k} = \frac1n\sum_{k=1}^{n}\frac{1}{1+k/n} \to \int_0^1 \frac{dt}{1+t} = \ln 2$.

**Autres méthodes d'intégration numérique** (avec $M_p = \sup_{[a,b]}|f^{(p)}|$) :

| Méthode | Approximation sur $[a_k, a_{k+1}]$ | Erreur globale |
|---|---|---|
| Rectangles (gauche ou droite) | $h\,f(a_k)$ | $\le \dfrac{M_1(b-a)^2}{2n}$ |
| Point milieu | $h\,f\!\left(\frac{a_k+a_{k+1}}{2}\right)$ | $\le \dfrac{M_2(b-a)^3}{24n^2}$ |
| [[Méthode des trapèzes\|Trapèzes]] | $\frac h2\big(f(a_k)+f(a_{k+1})\big)$ | $\le \dfrac{M_2(b-a)^3}{12n^2}$ |
| Simpson | $\frac h6\big(f(a_k)+4f(m_k)+f(a_{k+1})\big)$, $m_k$ milieu | $\le \dfrac{M_4(b-a)^5}{2880\,n^4}$ |

La méthode de Simpson est exacte pour les polynômes de degré $\le 3$.

Notion parente : [[Intégrale]]. Voir aussi : [[Subdivision]], [[Application lipschitzienne]], [[Méthode des trapèzes]].

Résumés : [[1 - Integration]], [[1 - démonstrations]], [[0 - Intégration UTILITAIRE]]
