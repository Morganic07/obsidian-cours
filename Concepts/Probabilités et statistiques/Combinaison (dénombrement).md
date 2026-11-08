---
type: concept
tags: [year2]
aliases: [Combinaison, combination, combinations, combinaisons, nCk, combinaison avec répétition, étoiles et barres, stars and bars]
matieres: [Probability]
sources: ["[[3 - Combinatorics|Chp 3 - Combinatorics]]", "[[Raw/Year 2/Probability/Chp 3 : Combinatorics.docx|Chp 3 - Combinatorics]]"]
maj: 2026-11-08
---

Une combinaison est un sous-ensemble non ordonné de taille $k$. Chaque combinaison correspond à $k!$ [[Permutation (dénombrement)|permutations]], donc

$${}_nC_k=\frac{{}_nP_k}{k!}=\binom nk=\frac{n!}{k!(n-k)!}\quad\text{(coefficient binomial)}.$$

Exemple : choisir 3 éléments parmi $\{a,b,c,d,e\}$ donne $60/6=10$ combinaisons. On a $\binom nn=\binom n0=1$ et $\binom n1=n$.

## Compléments (hors du cours)

- **Notations françaises** : $\binom nk$ se lit « $k$ parmi $n$ » ; l'ancienne notation est $C_n^k$ (attention à l'ordre des indices, inverse de ${}_nC_k$).
- **Propriétés** :
  - symétrie $\binom nk = \binom n{n-k}$ (choisir les $k$ éléments pris revient à choisir les $n-k$ laissés) ;
  - [[Formule de Pascal]] $\binom nk = \binom{n-1}{k-1} + \binom{n-1}{k}$ ;
  - $\sum_{k=0}^{n} \binom nk = 2^n$, le nombre de parties d'un ensemble à $n$ éléments.
- **Combinaison avec répétition** : le nombre de choix non ordonnés de $k$ objets parmi $n$ types, chaque type pouvant être pris plusieurs fois, est
  $$\binom{n+k-1}{k}.$$
  Preuve par **étoiles et barres** : on code un choix par $k$ étoiles (les objets) séparées par $n-1$ barres (les frontières entre types), soit $n+k-1$ places dont on choisit les $k$ occupées par des étoiles. Exemple : 3 boules de glace parmi 5 parfums, $\binom{7}{3} = 35$ coupes possibles.
- **Exemple d'urne** : 4 boules rouges et 6 noires, on en tire 3 sans remise. $P(\text{2 rouges}) = \dfrac{\binom42\binom61}{\binom{10}3} = \dfrac{6 \times 6}{120} = \dfrac{3}{10}$ ; c'est la [[Loi hypergéométrique]].

Notion parente : [[Dénombrement]]. Voir aussi : [[Loi binomiale]], [[Loi hypergéométrique]], [[Coefficient binomial]], [[Formule de Pascal]].

Résumés : [[3 - Combinatorics]]
