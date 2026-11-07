---
type: concept
tags:
  - year2
  - year3
aliases:
  - combinatorics
  - combinatoire
  - binomial coefficient
  - principe fondamental du dénombrement
  - permutations et combinaisons
  - Fundamental counting principle
  - product rule
  - k-tuple
  - k-uplet
  - arbre de décision du dénombrement
matieres:
  - Probability
  - Statistics
sources:
  - "[[3 - Combinatorics|Chp 3 - Combinatorics]]"
  - "[[0 - proba&stats utilitaire|probabilité statistiques utilitaire]]"
maj: 2026-11-07
---

Compter les issues sert à calculer $P(A) = |A|/|S|$ quand elles sont [[Équiprobabilité|équiprobables]] ([[Espace probabilisé]]).

- **Principe du produit** (*fundamental counting principle*) : $k$ choix successifs de $m_1, \dots, m_k$ possibilités donnent $m_1 \cdots m_k$ $k$-uplets (suites ordonnées).
- **Avec remise** : $k$ choix parmi $n$ objets donnent $n^k$ issues.
- **Sans remise, ordonné** ([[Permutation (dénombrement)|permutation]] de taille $k$) : $n!/(n-k)!$.
- **Sans remise, non ordonné** ([[Combinaison (dénombrement)|combinaison]]) : [[Coefficient binomial]] $\binom{n}{k} = \dfrac{n!}{k!(n-k)!}$, car chaque combinaison donne $k!$ permutations. $\binom{n}{0} = \binom{n}{n} = 1$, $\binom{n}{1} = n$.
- **Permutation de $n$ objets** : $n!$, ou $n!/(n_1!\cdots n_i!)$ si certains sont identiques.
- **Combinaison non distincte** : $\binom{n+k-1}{k}$ (donnée par l'arbre du cours, sans démonstration).

Le cours range ces cas dans un « arbre de décision » : sans sélection, des permutations ($n!$ ou $n!/(n_1!\cdots n_i!)$) ; avec sélection, un échantillon ordonné ($n!/(n-k)!$ ou $n^k$) ou non ordonné ($\binom{n}{k}$ ou $\binom{n+k-1}{k}$). Ce schéma n'a rien à voir avec l'[[Arbre de décision]] du data mining.

L'aide-mémoire de Statistics (troisième année) note $_nP_r = n!/(n-r)!$ et $_nC_r = n!/(r!(n-r)!)$.

Sert aux lois [[Loi binomiale]] et hypergéométrique.

Voir aussi : [[Permutation (dénombrement)]], [[Combinaison (dénombrement)]], [[Coefficient binomial]], [[Factorielle]], [[Équiprobabilité]], [[Probabilité conditionnelle]]

## Erreurs du cours

- [[3 - Combinatorics|Chp 3 - Combinatorics]] (texte du document vérifié) écrit que $k$ choix avec remise parmi $n$ objets donnent « $n_k$ » issues ($k$ en indice) ; il faut « $n^k$ », comme dans l'arbre de décision du même chapitre.

Résumés : [[3 - Combinatorics]], [[0 - proba&stats utilitaire]]
