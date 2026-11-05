---
type: source
sources: ["[[chp3 - complexité]]"]
maj: 2026-11-05
---

Résumé de [[chp3 - complexité]], dans [[Year 4 - graph theory]]. Cours en français. En cas d'écart, le cours et ses images font foi. Images non ouvertes. Voir [[Complexité algorithmique]].

## Idée générale

Mesurer le coût d'un algorithme en nombre d'opérations élémentaires et en mémoire, selon la taille $n$ du problème et indépendamment de la machine et du langage.

## Contenu, dans l'ordre du cours

- **Complexité temporelle** : nombre d'opérations élémentaires (affectation, addition, multiplication, comparaison, toutes de coût égal). **Complexité spatiale** : mémoire utilisée. Pire cas, meilleur cas, cas moyen (avec la probabilité $P(d)$ des données).
- **Exemple de fonction `f(x, y)`** : pire cas 4, meilleur 3, moyen 3,5.
- **`somme_1`** (boucle, $O(n)$) et **`somme_2`** (formule, $O(1)$).
- **Notations** $O$, $\Omega$, $\Theta$ : bornes supérieure, inférieure, serrée. Classes : constant, logarithmique, linéaire, quasi-linéaire, quadratique, cubique, exponentiel, factoriel.
- **Boucles `while`** : A, $O(\min(m, n))$ ; B, $O(\max(m, n))$ ; C, $O(m + n)$ ; D, $O(m \cdot n)$ (l'étudiant écrit « linéaire » pour chacune).
- **Recherche séquentielle** : pire cas $O(n)$, meilleur $O(1)$, moyen $\frac{n+1}{2}$.
- **Recherche dichotomique** dans un tableau trié de $n = 2^k$ éléments : $v_{2^k} \le 1 + v_{2^{k-1}}$, donc $O(\log n)$ ; sinon encadrer $n$ entre deux puissances de 2.
- **Tri de sélection** : pire cas $T(n) = n^2 + 4n - 5$, soit $O(n^2)$. **Tri d'insertion** : exercice posé, non traité.
- **Produit matriciel** : $A$ de taille $(m, n)$, $B$ de taille $(n, p)$, $C_{i,j} = \sum_k A_{i,k}B_{k,j}$.
- **Algorithmes récursifs** : la complexité est une suite définie par récurrence. Factorielle récursive : $T(n) = T(n-1) + 3$, donc $3n + 1$, $\Theta(n)$. [[Tours de Hanoï]] : $T(n) = 2T(n-1) + 1$, $T(1) = 1$, donc $\sum_{k=0}^{n-1} 2^k$, $\Theta(2^n)$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Algorithme D en $O(m \cdot n)$, noté « linéaire »** : $m \cdot n$ n'est pas linéaire (quadratique si $m = n$). Le cours écrit « → linéaire » après chaque algorithme, ce qui est juste pour A, B, C et faux pour D (complément). **À corriger avant un examen.**
2. **`somme_1` et `somme_2`** : le texte dit qu'ils font la même chose. `range(n)` somme $0 + \ldots + (n-1) = \frac{n(n-1)}{2}$, alors que `n * (n + 1) // 2` vaut la somme jusqu'à $n$. Les deux ne coïncident pas (complément). Les complexités $O(n)$ et $O(1)$ restent justes.
3. **Dimension du produit matriciel** : le texte dit que $C$ est de dimension $(m, n)$, alors qu'elle est $(m, p)$ ; « une matrice $C$ de matrice » est à lire « de dimension » (alerte confirmée, complément).
4. **Code des algorithmes** : indentation incertaine sur l'image (`return S`, bloc `else` de l'algorithme D, indentation de `print`). Alertes à vérifier sur l'image, non ouverte.
5. **Hanoï** : l'équation $T(n) = 2T(n-1) + 1$ est introduite pour « $n > 0$ » alors que la base est $T(1) = 1$ ; la fin de la résolution est coupée sur l'image. Le résultat $\sum_0^{n-1} 2^k = 2^n - 1$ est juste.
6. **`recherche_dic` renvoie 0** quand la valeur est trouvée et $-1$ sinon, et non sa position (complément, sans effet sur l'analyse).
7. **Cas moyen de la fonction `f`** : 3,5 suppose les deux branches équiprobables, ce que le texte ne précise pas.
