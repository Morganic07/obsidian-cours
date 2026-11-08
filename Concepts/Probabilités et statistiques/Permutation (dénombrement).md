---
type: concept
tags: [year2]
aliases: [Permutation, permutations, nPk, arrangement, arrangements, permutation de taille k, coefficient multinomial, anagramme, A_n^k]
matieres: [Probability]
sources: ["[[3 - Combinatorics|Chp 3 - Combinatorics]]", "[[Raw/Year 2/Probability/Chp 3 : Combinatorics.docx|Chp 3 - Combinatorics]]"]
maj: 2026-11-08
---

Une suite **ordonnée** de $k$ objets distincts pris sans remise parmi $n$ est une permutation de taille $k$. Il y en a
$${}_nP_k=n(n-1)\cdots(n-k+1)=\frac{n!}{(n-k)!}.$$

Sans sélection, $n$ objets distincts ont $n!$ permutations, et $\frac{n!}{n_1!\cdots n_i!}$ s'ils ne sont pas tous distincts (groupes de $n_1,\dots,n_i$ objets identiques).

Le schéma du cours appelle « arrangement » l'échantillon ordonné.

## Compléments (hors du cours)

- **Notation française des arrangements** : $A_n^k = \dfrac{n!}{(n-k)!}$, le ${}_nP_k$ du cours. Exemple : un podium (or, argent, bronze) parmi 8 coureurs, $A_8^3 = 8 \times 7 \times 6 = 336$.
- **Arrangement avec répétition** : suite ordonnée de $k$ éléments pris parmi $n$, chacun pouvant revenir : $n^k$ possibilités. Exemple : un code à 4 chiffres, $10^4 = 10\,000$.
- **Permutation d'objets non distincts** : $\dfrac{n!}{n_1!\cdots n_i!}$ avec $n_1 + \dots + n_i = n$ s'appelle le **coefficient multinomial**, noté $\binom{n}{n_1, \dots, n_i}$ ; on divise par les $n_j!$ façons d'échanger des objets identiques sans changer la suite. Exemple : les anagrammes d'ANANAS (3 A, 2 N, 1 S), $\dfrac{6!}{3!\,2!\,1!} = 60$.
- **Convention** $0! = 1$ : elle rend les formules valables pour $k = 0$ ou $k = n$ (une seule façon de ne rien ranger).
- **Formule de Stirling** : $n! \sim \sqrt{2\pi n}\left(\dfrac{n}{e}\right)^n$ quand $n \to \infty$ ; elle donne l'ordre de grandeur de $n!$ quand le calcul exact est impraticable.

Notion parente : [[Dénombrement]]. Voir aussi : [[Factorielle]], [[Combinaison (dénombrement)]].

Résumés : [[3 - Combinatorics]]
