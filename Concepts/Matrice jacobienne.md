---
type: concept
aliases: [matrice de Jacobi, matrices jacobiennes, jacobien, Jacobian, "jacobien d'un changement de variable", J_φ]
matieres: [Analyse dans Rn, Analyse]
sources: ["[[Chp 4 - Calcul différentiel du premier ordre]]", "[[raw/Year 2/Analyse/Chp9-intégrales multiples.pdf|Chp9-intégrales multiples]]"]
maj: 2026-11-06
---

Pour $f : U \subset \mathbb{R}^p \to \mathbb{R}^n$ différentiable en $a$, $J_f(a)$ est la matrice à $n$ lignes et $p$ colonnes de la [[Différentielle]] $D_af$ dans les bases canoniques : son coefficient en ligne $i$ et colonne $j$ est $\left.\frac{\partial f_i}{\partial x_j}\right|_a$.

Si $n = p$, son [[Déterminant]] est le **jacobien**. Un jacobien non nul en $a$ rend $D_a\phi$ bijective.

Le jacobien intervient aussi dans le changement de variable des intégrales doubles, comme $\rho$ en polaires : voir [[Intégrale multiple]]. Pour $\varphi : (u, v) \mapsto (x, y)$, le cours d'Analyse ([[Chp9-intégrales multiples (résumé)]]) pose $J_\varphi = \det\begin{pmatrix}\partial x/\partial u & \partial x/\partial v\\ \partial y/\partial u & \partial y/\partial v\end{pmatrix}$, et l'on intègre avec $|J_\varphi|$.

Notion parente : [[Différentielle]]. Voir aussi : [[Dérivée partielle]], [[Gradient]], [[Difféomorphisme]], [[Transformation linéaire]], [[Déterminant]], [[Intégrale multiple]].

Résumés : [[Chp 4 - Calcul différentiel du premier ordre (résumé)]], [[Chp9-intégrales multiples (résumé)]]
