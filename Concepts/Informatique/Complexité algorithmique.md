---
type: concept
tags:
  - year2
  - year4
aliases:
  - complexité temporelle
  - complexité spatiale
  - complexité d'un algorithme
  - complexité en temps
  - pire des cas
  - notation Θ
  - notation Ω
  - opération élémentaire
  - complexité au pire
matieres:
  - graph theory
  - Algo Maths
  - Algo
sources:
  - "[[3 - complexité|chp3 - complexité]]"
  - "[[1 - récursivité et complexité|Chp1 - récursivité et complexité]]"
maj: 2026-11-07
---

La **complexité temporelle** est le nombre d'opérations élémentaires (affectation, addition, multiplication, comparaison, toutes de coût égal) en fonction de la taille $n$ du problème ; la **complexité spatiale** est la mémoire utilisée. Elle ne dépend ni de la machine ni du langage. On distingue pire cas, meilleur cas (plus petit nombre d'opérations) et cas moyen : moyenne des complexités sur les jeux de données de taille $n$, pondérée par la probabilité $P(d)$ des données.

**Règles de calcul** (cours d'Algo de Year 2) : une instruction de base coûte une unité, une boucle additionne ses itérations, un appel ajoute le coût de la fonction. Dans la notation $O$, on oublie les constantes et on garde le terme dominant.

**Notations** (graph theory) : $O(g)$ borne supérieure, $\Omega(g)$ borne inférieure, $\Theta(g)$ borne serrée. Classes : constant, logarithmique, linéaire, quasi-linéaire, quadratique, cubique, exponentiel, factoriel.

Exemples du cours de graphes : fonction `f` à un `if/else` (une comparaison, puis 2 ou 3 opérations selon la branche), avec $T(n) = 4$ au pire, $3$ au meilleur et $3{,}5$ en moyenne, soit la moyenne des deux branches supposées également probables (hypothèse que le cours ne formule pas) ; recherche séquentielle $O(n)$, dichotomique $O(\log n)$, tri de sélection $O(n^2)$, factorielle récursive $\Theta(n)$, [[Tours de Hanoï]] $\Theta(2^n)$. Pour un algorithme récursif, la complexité est une suite définie par récurrence ([[Récursivité]], [[Récurrence]]). Parcours de graphes en $O(|V| + |E|)$ : [[Graphe orienté]].

Dans le cours d'Algo, le calcul pas à pas, la méthode de substitution et le théorème de résolution sont dans [[Calcul de complexité et théorème de résolution]].

Liens : [[Comparaison asymptotique]] (le $O$ des suites et des fonctions), [[Classe de complexité]], [[Recherche séquentielle]], [[Recherche dichotomique]], [[Tri par sélection]], [[Arbre couvrant minimal]], [[Calcul de complexité et théorème de résolution]]

Résumés : [[3 - complexité]], [[1 - récursivité et complexité]]
