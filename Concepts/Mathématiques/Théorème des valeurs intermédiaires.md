---
type: concept
tags: [year1]
aliases: [TVI, valeurs intermédiaires]
matieres: [Analyse Maths]
sources: ["[[Raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1.pdf]]", "[[Raw/Year 1/Contrôles.pdf|Contrôles.pdf]]"]
maj: 2026-11-07
---

Si $f$ est continue sur $[a, b]$ et $f(a)f(b) \le 0$, alors $f$ s'annule entre $a$ et $b$.

La preuve procède par dichotomie avec deux [[Suites adjacentes]], ce qui approche le zéro à $(b-a)/2^n$ près. Conséquence : l'image d'un intervalle par une fonction continue est un intervalle. Le DS4 associe le TVI à la stricte monotonie pour prouver l'unicité d'une racine.

Notion parente : [[Limite et continuité]]. Voir aussi : [[Recherche dichotomique]], [[Suites adjacentes]], [[Borne supérieure]], [[Intervalle réel]].

## Erreurs du cours

- [[Raw/Year 1/Analyse Maths/Cours/AnalyseID1.pdf|AnalyseID1.pdf]] (preuve du théorème 21, p. 54) pose l'invariant « $f(a_n)f(b_n) < 0$ » ; il faut « $f(a_n)f(b_n) \le 0$ », comme l'hypothèse $f(a)f(b) \le 0$ et comme ce que la construction garantit ensuite ($f(a_{n+1})f(b_{n+1}) \le 0$). L'énoncé du théorème est juste.

Résumés : [[0 - rappels pdf]]
