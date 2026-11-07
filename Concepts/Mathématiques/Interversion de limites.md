---
type: concept
tags: [year3]
aliases: [limit switching, échange de limites, intégration terme à terme, dérivation terme à terme, interversion limite-intégrale]
sources: ["[[Chp3 - Sequence of function (résumé)|Chp3 - Sequence of function]]", "[[Chp4 - Series of functions (résumé)|Chp4 - Series of functions]]"]
maj: 2026-11-06
---

Résultats valables sous [[Convergence uniforme|convergence uniforme]] d'une suite de fonctions $(f_n)$ vers $f$ ([[Chp3 - Sequence of function (résumé)|Chp3 - Sequence of function]]) :

- **échange de limites** : si $a$ est un [[Point limite|point limite]] et $\ell_n = \lim_{x \to a} f_n(x)$, alors $(\ell_n)$ converge vers $\lim_{x \to a} f(x)$ ;
- **continuité** : la limite d'une suite de fonctions continues est continue ;
- **intégration** : pour des fonctions continues, $\lim \int_a^b f_n = \int_a^b f$ ;
- **dérivation** : si $(f_n(x_0))$ converge et si $(f_n')$ converge uniformément vers $g$, alors $f' = g$.

Les mêmes énoncés valent pour les séries de fonctions, qu'on intègre ou dérive alors terme à terme ([[Chp4 - Series of functions (résumé)|Chp4 - Series of functions]]), et servent pour les [[Série entière|séries entières]] ([[Chp5 - power series (résumé)]]).

Contre-exemple du cours : des fonctions « triangles » d'intégrale 1 qui convergent simplement vers 0, sans que les intégrales tendent vers 0.

Notion parente : [[Convergence uniforme]]. Voir aussi : [[Point limite]], [[Série entière]].

## À vérifier

- Le contre-exemple est déclaré à valeurs dans $[0, 1]$, alors que $f_n(1/n) = n$.

Résumés : [[Chp3 - Sequence of function (résumé)]], [[Chp4 - Series of functions (résumé)]], [[Chp5 - power series (résumé)]]
