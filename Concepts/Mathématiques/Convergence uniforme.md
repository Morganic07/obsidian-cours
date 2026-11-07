---
type: concept
tags: [year3]
aliases: [uniform convergence, convergence simple, pointwise convergence, convergence normale, normal convergence, norme uniforme, suite de fonctions, séries de fonctions, critère de Weierstrass, Weierstrass M-test]
matieres: [Séries]
sources: ["[[Chp3 - Sequence of function (résumé)|Chp3 - Sequence of function]]", "[[Chp4 - Series of functions (résumé)|Chp4 - Series of functions]]"]
maj: 2026-11-06
---

Pour une suite de fonctions $(f_n)$ sur $X$ :
- **convergence simple** : $(f_n(x))$ converge pour chaque $x$ ; le rang $N$ dépend de $x$ ;
- **convergence uniforme** vers $f$ : $\forall \epsilon, \exists N, n \ge N \Rightarrow \forall x, |f_n(x) - f(x)| < \epsilon$. Équivalent à $\|f_n - f\|_\infty \to 0$, avec $\|f\|_\infty = \sup_X |f|$. Elle implique la convergence simple, pas l'inverse.

**Ce que l'uniformité permet** : limite de fonctions continues continue ; échange limite et intégrale sur $[a, b]$ ; échange limite et dérivée si $(f_n')$ converge uniformément et $(f_n(x_0))$ converge ; échange de deux limites. La convergence simple seule ne suffit pas à ces échanges.

**Séries de fonctions** $\sum f_n$ : mêmes notions appliquées aux sommes partielles. **Convergence normale** : $\sum \|f_n\|_\infty$ converge (critère de Weierstrass : $\|f_n\|_\infty \le a_n$, $\sum a_n$ convergente). Normale implique uniforme, absolue et simple.

Contre-exemple du cours : $f_n$ triangulaire de hauteur $n$ en $1/n$ converge simplement vers 0, mais chaque intégrale vaut 1.

Liens : [[Série numérique]], [[Série entière]], [[Limite et continuité]], [[Application lipschitzienne]] (l'autre usage de « uniformément continue »), [[Interversion de limites]], [[Point limite]], [[Reste d'une série]]

Résumés : [[Chp3 - Sequence of function (résumé)]], [[Chp4 - Series of functions (résumé)]], [[Chp5 - power series (résumé)]]
