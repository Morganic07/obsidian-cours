---
type: concept
aliases: [combinatorics, combinatoire, coefficient binomial, binomial coefficient, principe fondamental du dénombrement, permutations et combinaisons]
matieres: [Probability]
sources: ["[[Chp 3 - Combinatorics]]"]
maj: 2026-11-05
---

Compter les issues sert à calculer $P(A) = |A|/|S|$ quand elles sont équiprobables ([[Espace probabilisé]]).

- **Principe du produit** : $k$ choix successifs de $m_1, \dots, m_k$ possibilités donnent $m_1 \cdots m_k$ $k$-uplets.
- **Avec remise** : $k$ choix parmi $n$ objets donnent $n^k$ issues.
- **Sans remise, ordonné** (permutation de taille $k$) : $n!/(n-k)!$.
- **Sans remise, non ordonné** (combinaison) : $\binom{n}{k} = \dfrac{n!}{k!(n-k)!}$, car chaque combinaison donne $k!$ permutations. $\binom{n}{0} = \binom{n}{n} = 1$, $\binom{n}{1} = n$.
- **Permutation de $n$ objets** : $n!$, ou $n!/(n_1!\cdots n_i!)$ si certains sont identiques.
- **Combinaison non distincte** : $\binom{n+k-1}{k}$ (donnée par l'arbre du cours, sans démonstration).

Sert aux lois [[Loi binomiale]] et hypergéométrique.

Résumé : [[Chp 3 - Combinatorics (résumé)]]
