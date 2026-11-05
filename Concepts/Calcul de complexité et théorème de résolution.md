---
type: concept
aliases: [Master Theorem, master theorem, théorème de résolution de la récurrence, méthode de substitution, diviser pour régner, complexité au meilleur, complexité en moyenne, règles de la notation O, complexité d'un algorithme récursif]
matieres: [Algo]
sources: ["[[Chp1 - récursivité et complexité]]", "[[AVL momo]]", "[[qui dit quoi AVL]]"]
maj: 2026-11-05
---

Page du cours d'Algo de deuxième année sur le calcul de la complexité. La notion générale est dans [[Complexité algorithmique]] (cours de théorie des graphes), la comparaison des ordres de grandeur dans [[Comparaison asymptotique]].

**Définition du cours** : quantité de ressources (le temps) nécessaire pour résoudre un problème de taille $n$, indépendamment de la machine. On distingue le meilleur cas, le pire cas (la garantie) et le cas moyen. On retient l'ordre de grandeur : $n^2 + 2n - 5$ opérations donnent $O(n^2)$.

**Règles de calcul** : une instruction de base coûte $O(1)$. Une boucle de $m$ itérations coûte $m \times$ (condition + corps). Un `if/else` coûte la condition plus les deux branches. Un appel ajoute le coût de la fonction.

**Règles de la notation $O$** : on oublie les constantes, on garde le terme dominant. $O(T_1) + O(T_2) = \max$ et $O(T_1)\,O(T_2) = O(T_1 T_2)$.

**Classes** : constante, logarithmique, linéaire, quadratique, polynomiale $O(n^p)$, exponentielle $O(a^n)$.

**Fonction récursive** : le coût est celui des appels, plus celui qui sépare les données et reconstruit le résultat.
- Substitution : $T(n) = T(n-1) + b$ donne $O(n)$.
- Forme diviser pour régner : $T(n) = a\,T(n/b) + f(n)$ avec $f(n) = c\,n^k$. On a $O(n^{\log_b a})$ si $a > b^k$, $O(n^k \log_b n)$ si $a = b^k$, $O(n^k)$ si $a < b^k$.

**Arbres AVL** : `ajouter` coûte $O(h)$, et la hauteur $h$ est en $O(\log n)$ si l'arbre est équilibré.

Liens : [[Récursivité]], [[Recherche dichotomique]], [[Arbre AVL]], [[Complexité algorithmique]]

Résumés : [[Chp1 - récursivité et complexité (résumé)]], [[AVL momo (résumé)]]
