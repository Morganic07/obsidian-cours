---
type: concept
tags:
  - year2
aliases:
  - changement de variables x = φ(t)
  - intégration par changement de variable
matieres:
  - Analyse
sources:
  - "[[1 - Integration (résumé)|Chap7-Integration]]"
  - "[[Raw/Year 2/Analyse/Chp9-intégrales multiples.pdf|Chp9-intégrales multiples.pdf]]"
maj: 2026-11-06
---

Soient $I$ un intervalle de $\mathbb{R}$, $f : I \to \mathbb{K}$ continue sur $I$ et $\varphi : [a,b] \to I$ de classe $\mathcal{C}^1$ sur $[a,b]$. Alors

$$\int_{\varphi(a)}^{\varphi(b)} f(x)\,\mathrm{d}x = \int_a^b f(\varphi(t))\,\varphi'(t)\,\mathrm{d}t.$$

On dit qu'on a effectué le changement de variables $x=\varphi(t)$. En pratique, il faut modifier les trois éléments : la variable $x=\varphi(t)$, l'élément différentiel $\mathrm{d}x=\varphi'(t)\,\mathrm{d}t$ et les bornes. La preuve consiste à dériver $F\circ\varphi$, où $F$ est une primitive de $f$.

Le chapitre 9 étend le changement de variables aux intégrales doubles, avec la valeur absolue du jacobien ([[Théorème de transformation]]).

Notion parente : [[Primitive]]. Voir aussi : [[Règles de Bioche]], [[Intégrale multiple]], [[Matrice jacobienne]].

Résumés : [[1 - Integration (résumé)]], [[1 - démonstrations (résumé)]], [[TD7-integration (1) (résumé)]], [[2 - intégrales multiples (résumé)]]
