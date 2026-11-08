---
type: concept
tags: [year3]
aliases: [limit switching, échange de limites, intégration terme à terme, dérivation terme à terme, interversion limite-intégrale]
sources: ["[[3 - Sequence of function|Chp3 - Sequence of function]]", "[[4 - Series of functions|Chp4 - Series of functions]]"]
maj: 2026-11-08
---

Résultats valables sous [[Convergence uniforme|convergence uniforme]] d'une suite de fonctions $(f_n)$ vers $f$ ([[3 - Sequence of function|Chp3 - Sequence of function]]) :

- **échange de limites** : si $a$ est un [[Point limite|point limite]] et $\ell_n = \lim_{x \to a} f_n(x)$, alors $(\ell_n)$ converge vers $\lim_{x \to a} f(x)$ ;
- **continuité** : la limite d'une suite de fonctions continues est continue ;
- **intégration** : pour des fonctions continues, $\lim \int_a^b f_n = \int_a^b f$ ;
- **dérivation** : si $(f_n(x_0))$ converge et si $(f_n')$ converge uniformément vers $g$, alors $f' = g$.

Les mêmes énoncés valent pour les séries de fonctions, qu'on intègre ou dérive alors terme à terme ([[4 - Series of functions|Chp4 - Series of functions]]), et servent pour les [[Série entière|séries entières]] ([[5 - power series]]).

Contre-exemple du cours : des fonctions « triangles » $f_n : [0, 1] \to \mathbb{R}_+$ (à valeurs jusqu'à $f_n(\frac1n) = n$) [[Erreurs du cours#^e-interversion-de-limites|✎]], $f_n(x) = n^2x$ sur $[0, \frac1n]$, $-n^2x + 2n$ sur $[\frac1n, \frac2n]$, $0$ sur $[\frac2n, 1]$, d'intégrale 1, qui convergent simplement vers 0 sans que les intégrales tendent vers 0 : la convergence n'est donc pas uniforme. Le théorème ne donne qu'une condition suffisante pour échanger limite et intégrale.

Notion parente : [[Convergence uniforme]]. Voir aussi : [[Point limite]], [[Série entière]].
Résumés : [[3 - Sequence of function]], [[4 - Series of functions]], [[5 - power series]]
