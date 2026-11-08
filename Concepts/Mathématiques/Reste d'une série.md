---
type: concept
tags: [year3]
aliases: [remainder of a series, reste d'ordre n, nth remainder]
matieres: [Séries]
sources: ["[[1 - Convergent, divergent and positive terms SERIES|Chp1 - Convergent, divergent and positive terms SERIES]]", "[[4 - Series of functions|Chp4 - Series of functions]]"]
maj: 2026-11-08
---

Pour une série convergente de somme $S$ et de sommes partielles $S_n$ : $R_n = S - S_n = \sum_{k \ge n+1} a_k$, qui tend vers 0 ([[1 - Convergent, divergent and positive terms SERIES|Chp1 - Convergent, divergent and positive terms SERIES]]).

**Majorations** : par [[Comparaison série-intégrale|comparaison avec une intégrale]], $\int_{n+1}^{+\infty} f \le R_n \le \int_n^{+\infty} f$ (pour $\sum 1/n^3$ avec $n = 20$ : $S_{20} = 1.20087$ et $1.20200 \le S \le 1.20212$ [[Erreurs du cours#^e-reste-d-une-serie|✎]]) ; pour une série alternée, $|R_n| \le b_{n+1}$ ([[Critère des séries alternées]]).

**Séries de fonctions** : $R_n$ converge simplement vers 0, et la série converge uniformément si et seulement si $(R_n)$ converge uniformément vers 0 ([[4 - Series of functions|Chp4 - Series of functions]]).

À distinguer du [[Reste de Taylor]].

Notion parente : [[Série numérique]]. Voir aussi : [[Comparaison série-intégrale]], [[Critère des séries alternées]], [[Convergence uniforme]].
Résumés : [[1 - Convergent, divergent and positive terms SERIES]], [[2 - Alternating and absolutly convergent series]], [[4 - Series of functions]]
