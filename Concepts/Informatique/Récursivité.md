---
type: concept
tags:
  - year1
  - year2
aliases:
  - fonction récursive
  - fonctions récursives
  - algorithme récursif
  - algorithmes récursifs
  - appel récursif
  - appels récursifs
  - récursion simple
  - récursion multiple
  - condition d'arrêt
  - récursivité directe
  - récursivité indirecte
  - phase de descente
  - phase de montée
matieres:
  - Algo
  - Algo Maths
sources:
  - "[[Chp1 - récursivité et complexité]]"
  - ".raw/Year 2/Algo/Cours/Chapitre4-Preing2ID.pdf"
  - ".raw/Year 1/Algo Maths/AlgoID1.pdf"
  - "[[Cours/Year 1/Algo Maths/Cours 1|Cours 1 (Algo Maths)]]"
maj: 2026-11-06
---

Une fonction est récursive si elle est définie, directement ou indirectement, en fonction d'elle-même. Directe : elle s'appelle. Indirecte : B appelle C, C appelle D, D rappelle B.

**Deux parties à coder** : une condition d'arrêt (un `if`) et l'appel récursif, avec des `return`. L'exécution a deux phases : la descente, qui enchaîne les appels jusqu'à la condition d'arrêt, puis la montée, où chaque appel rend sa valeur à celui d'en dessous.

**Exemple** : `fact(n)` renvoie 1 si `n == 0`, sinon `n * fact(n-1)`. Pour `fact(4)`, la descente va jusqu'à `fact(0)`, puis la montée calcule $1, 2, 6, 24$.

**Pile de récursion** : les appels en cours sont empilés dans la [[Pile d'exécution|pile d'exécution]], qui gère tous les appels de fonctions. Chaque bloc stocke les paramètres, l'adresse de retour et les variables locales. En Python, elle est limitée à environ 1000 appels. Voir [[Pile et file]].

**Coût** : se met en équation $T(n) = a\,T(n/b) + f(n)$ et se résout par substitution ou par le théorème de résolution, voir [[Calcul de complexité et théorème de résolution]]. Exemple : [[Recherche dichotomique]].

Le polycopié de 1re année distingue la récursivité terminale, où l'appel récursif est la dernière opération, de la non terminale. Il note aussi que la terminaison d'un programme est indécidable en général. Hauteur et parcours d'un [[Arbre binaire]] sont des exemples classiques.

**Algo Maths (1re année)** : un algorithme est récursif s'il s'appelle lui-même, en correspondance avec la [[Récurrence|récurrence]]. Forme générale : une condition d'arrêt $c(x)$, un cas trivial $g(x)$, un appel sur le successeur $s(x)$. La récursion est **simple** (un appel) ou **multiple**. Avantages : code court, proche des mathématiques, adapté aux structures récursives ; coût : la pile d'appels. Tout algorithme récursif a une version itérative. Exemples : [[Factorielle|factorielle]], PGCD d'Euclide, [[Tours de Hanoï|Hanoï]], Fibonacci ; le TD3 traite division entière, palindrome, miroir et puissance.

**Algo (2e année)** compare les versions itérative et récursive de la factorielle et de la somme des $n$ premiers entiers.

Liens : [[Calcul de complexité et théorème de résolution]], [[Pile et file]], [[Pile d'exécution]], [[Recherche dichotomique]], [[Tours de Hanoï]], [[Récurrence]], [[Récursivité terminale]], [[Terminaison d'un algorithme]], [[Factorielle]], [[Arbre binaire]]

Résumés : [[Chp1 - récursivité et complexité (résumé)]], [[AlgoID1 (résumé)]], [[Chapitre4-Preing2ID (résumé)]], [[Séance 1 - Algo Maths (résumé)|Cours 1 (résumé)]], [[Contrôles (résumé)|Contrôles (résumé)]], [[Projet-Arbre-AVL-ID2 (résumé)]]
