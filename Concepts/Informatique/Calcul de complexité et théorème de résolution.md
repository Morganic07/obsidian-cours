---
type: concept
tags:
  - year2
  - year4
aliases:
  - Master Theorem
  - master theorem
  - théorème de résolution de la récurrence
  - méthode de substitution
  - complexité au meilleur
  - complexité en moyenne
  - règles de la notation O
  - complexité d'un algorithme récursif
matieres:
  - Algo
  - graph theory
sources:
  - "[[1 - récursivité et complexité|Chp1 - récursivité et complexité]]"
  - "[[Raw/Year 2/Algo/DM/AVL momo.docx|AVL momo]]"
  - "[[Raw/Year 2/Algo/DM/qui dit quoi AVL.docx|qui dit quoi AVL]]"
  - "[[3 - complexité|chp3 - complexité]]"
maj: 2026-11-08
---

Page du cours d'Algo de deuxième année sur le calcul de la complexité. La notion générale est dans [[Complexité algorithmique]] (cours de théorie des graphes), la comparaison des ordres de grandeur dans [[Comparaison asymptotique]].

**Définition du cours** : quantité de ressources (le temps) nécessaire pour résoudre un problème de taille $n$, indépendamment de la machine. On distingue le meilleur cas, le pire cas (la garantie) et le cas moyen. On retient l'ordre de grandeur : $n^2 + 2n - 5$ opérations donnent $O(n^2)$.

**Règles de calcul** : une instruction de base coûte $O(1)$. Une boucle de $m$ itérations coûte $m \times$ (condition + corps). Un `if/else` coûte la condition plus les deux branches. Un appel ajoute le coût de la fonction.

**Règles de la notation $O$** : on oublie les constantes, on garde le terme dominant. $O(T_1) + O(T_2) = \max$ et $O(T_1)\,O(T_2) = O(T_1 T_2)$.

**Classes** : constante, logarithmique, linéaire, quadratique, polynomiale $O(n^p)$, exponentielle $O(a^n)$.

**Fonction récursive** : le coût est celui des appels, plus celui qui sépare les données et reconstruit le résultat.
- Substitution : $T(n) = T(n-1) + b$, avec $T(0) = c$, donne $T(n) = ib + T(n-i) = nb + T(0) = nb + c$, soit $O(n)$. [[Erreurs du cours#^e-calcul-de-complexite-et-theoreme-de-resolution|✎]]
- Forme [[Diviser pour régner|diviser pour régner]] (Master Theorem) : $T(n) = a\,T(n/b) + f(n)$ avec $f(n) = c\,n^k$. On a $O(n^{\log_b a})$ si $a > b^k$, $O(n^k \log_b n)$ si $a = b^k$, $O(n^k)$ si $a < b^k$.

**En théorie des graphes** (quatrième année) : la complexité d'un algorithme récursif est une suite définie par récurrence. Factorielle récursive : $T(n) = T(n-1) + 3$, donc $3n + 1$, en $\Theta(n)$. [[Tours de Hanoï]] : $T(n) = 2T(n-1) + 1$, $T(1) = 1$, donc $\sum_{k=0}^{n-1} 2^k$, en $\Theta(2^n)$.

**Arbres AVL** : `ajouter` coûte $O(h)$, et la hauteur $h$ est en $O(\log n)$ si l'arbre est équilibré.

Notion parente : [[Complexité algorithmique]]. Voir aussi : [[Récursivité]], [[Recherche dichotomique]], [[Diviser pour régner]], [[Tours de Hanoï]], [[Arbre AVL]]

Résumés : [[1 - récursivité et complexité]], [[3 - complexité]]
