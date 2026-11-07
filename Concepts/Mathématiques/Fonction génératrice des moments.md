---
type: concept
tags: [year2, year3]
aliases: [moment generating function, mgf, MGF]
matieres: [Probability, Statistics]
sources: ["[[Chp 5 - Continuous random variable (résumé)|Chp 5 - Continuous random variable]]", "[[Chp3 - More on probability (résumé)|Chp3 - More on probability]]"]
maj: 2026-11-06
---

$M_X(t) = E(e^{tX})$, définie par $\int e^{tx}f(x)\,dx$ pour une variable continue. Elle existe si elle est définie sur un intervalle contenant 0, avec des $t$ positifs et négatifs. $M_X(0) = 1$ et $E(X^r) = M_X^{(r)}(0)$.

Elle détermine la loi : deux lois ayant la même fonction génératrice (si elle existe) sont égales.

Pour des variables indépendantes, $M_{X+Y}(t) = M_X(t)M_Y(t)$, et pour $Y = \sum a_iX_i + b$, $M_Y(t) = e^{bt}\prod M_{X_i}(a_it)$.

Notion parente : [[Espérance et variance]]. Voir aussi : [[Variable aléatoire]], [[Loi normale]].

## À vérifier

- [[Chp 5 - Continuous random variable (résumé)|Chp 5 - Continuous random variable]] : « as in the discrete case » renvoie à un cas absent des notes.
- [[Chp3 - More on probability (résumé)|Chp3 - More on probability]] écrit $\frac{d^n}{dt^n}M_X(t) = E(X^n)$ sans évaluer en 0, et $M_{aX+bY+x}$ pour $+c$.

Résumés : [[Chp 5 - Continuous random variable (résumé)]], [[Chp3 - More on probability (résumé)]]
