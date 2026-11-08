---
type: concept
tags:
  - year2
aliases:
  - valeur moyenne d'une fonction
  - valeur moyenne
matieres:
  - Analyse
sources:
  - "[[1 - Integration|Chap7-Integration]]"
  - "[[0 - Intégration UTILITAIRE|Intégration UTILITAIRE]]"
  - "[[Raw/Year 2/Analyse/chp7/Chap7-Integration.docx|Chap7-Integration]]"
maj: 2026-11-08
---

La valeur moyenne d'une fonction continue $f:[a,b]\to\mathbb{R}$ est $\frac{1}{b-a}\int_a^b f$ : c'est la constante $\mu$ telle que $\int_{[a,b]} f = \int_{[a,b]} \mu$.

Le TD7 (ex. 4) étudie le cas d'égalité $\int_a^b f=(b-a)\sup|f|$.

## Formule de la moyenne (complément, hors du cours)

Si $f$ est continue sur $[a,b]$ ($a<b$), il existe $c \in [a,b]$ tel que
$$\int_a^b f(t)\,dt = (b-a)\,f(c), \qquad\text{autrement dit}\quad f(c) = \mu = \frac{1}{b-a}\int_a^b f.$$

**Preuve.** $f$ continue sur le segment $[a,b]$ est bornée et atteint ses bornes ([[Théorème des bornes atteintes]]) : $m = \min f$ et $M = \max f$. De $m \le f \le M$ et de la croissance de l'intégrale, on tire
$$m(b-a) \le \int_a^b f \le M(b-a), \qquad\text{donc}\quad m \le \mu \le M.$$
La valeur $\mu$ est comprise entre deux valeurs prises par $f$ ; le [[Théorème des valeurs intermédiaires]] donne $c$ tel que $f(c) = \mu$.

**Lecture géométrique.** Pour $f \ge 0$, l'aire sous la courbe entre $a$ et $b$ est égale à celle du rectangle de base $[a,b]$ et de hauteur $f(c)$.

La continuité est nécessaire : une fonction en escalier valant $0$ puis $1$ sur $[0,2]$ a pour moyenne $\frac12$, valeur qu'elle ne prend jamais.

Notion parente : [[Intégrale]].

Résumés : [[1 - Integration]], [[0 - Intégration UTILITAIRE]]
