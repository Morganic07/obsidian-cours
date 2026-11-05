---
type: concept
aliases: [complexité temporelle, complexité spatiale, complexité d'un algorithme, complexité en temps, pire des cas, notation Θ, notation Ω, opération élémentaire]
matieres: [graph theory, Algo Maths, Algo]
sources: ["[[chp3 - complexité]]", "[[Chp1 - récursivité et complexité]]"]
maj: 2026-11-05
---

La **complexité temporelle** est le nombre d'opérations élémentaires (affectation, addition, multiplication, comparaison, toutes de coût égal) en fonction de la taille $n$ du problème ; la **complexité spatiale** est la mémoire utilisée. Elle ne dépend ni de la machine ni du langage. On distingue pire cas, meilleur cas et cas moyen.

**Règles de calcul** (cours d'Algo de Year 2) : une instruction de base coûte une unité, une boucle additionne ses itérations, un appel ajoute le coût de la fonction. Dans la notation $O$, on oublie les constantes et on garde le terme dominant.

**Notations** (graph theory) : $O(g)$ borne supérieure, $\Omega(g)$ borne inférieure, $\Theta(g)$ borne serrée. Classes : constant, logarithmique, linéaire, quasi-linéaire, quadratique, cubique, exponentiel, factoriel.

Exemples du cours de graphes : recherche séquentielle $O(n)$, dichotomique $O(\log n)$, tri de sélection $O(n^2)$, factorielle récursive $\Theta(n)$, [[Tours de Hanoï]] $\Theta(2^n)$. Pour un algorithme récursif, la complexité est une suite définie par récurrence ([[Récursivité]], [[Récurrence]]). Parcours de graphes en $O(|V| + |E|)$ : [[Graphe orienté]].

Dans le cours d'Algo, le calcul pas à pas, la méthode de substitution et le théorème de résolution sont dans [[Calcul de complexité et théorème de résolution]].

Liens : [[Comparaison asymptotique]] (le $O$ des suites et des fonctions), [[Recherche dichotomique]], [[Arbre couvrant minimal]], [[Calcul de complexité et théorème de résolution]]

Résumés : [[chp3 - complexité (résumé)]], [[Chp1 - récursivité et complexité (résumé)]]
