---
type: concept
tags: [year2, year3]
aliases: [moment generating function, mgf, MGF]
matieres: [Probability, Statistics]
sources: ["[[5 - Continuous random variable|Chp 5 - Continuous random variable]]", "[[3 - More on probability|Chp3 - More on probability]]"]
maj: 2026-11-07
---

$M_X(t) = E(e^{tX})$, définie par $\int e^{tx}f(x)\,dx$ pour une variable continue. Elle existe si elle est définie sur un intervalle contenant 0, avec des $t$ positifs et négatifs. $M_X(0) = 1$ et $E(X^r) = M_X^{(r)}(0)$.

Elle détermine la loi : deux lois ayant la même fonction génératrice (si elle existe) sont égales.

Pour des variables indépendantes, $M_{X+Y}(t) = M_X(t)M_Y(t)$, et pour $Y = \sum a_iX_i + b$, $M_Y(t) = e^{bt}\prod M_{X_i}(a_it)$.

Notion parente : [[Espérance et variance]]. Voir aussi : [[Variable aléatoire]], [[Loi normale]].

## Erreurs du cours

- [[3 - More on probability|Chp3 - More on probability]] écrit « dⁿ/dtⁿ M_X(t) = E(Xⁿ) » ; il faut évaluer la dérivée en 0 : $M_X^{(n)}(0) = E(X^n)$.
- [[3 - More on probability|Chp3 - More on probability]] écrit « M_{aX+bY+x}(t) = M_X(at) x M_y(bt) x e^{tc} » ; il faut $M_{aX+bY+c}(t) = M_X(at)\,M_Y(bt)\,e^{ct}$, pour $X$ et $Y$ indépendantes.

Résumés : [[5 - Continuous random variable]], [[3 - More on probability]]
