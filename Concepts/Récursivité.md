---
type: concept
aliases: [fonction récursive, fonctions récursives, algorithme récursif, algorithmes récursifs, pile de récursion, appel récursif, appels récursifs]
matieres: [Algo, Algo Maths]
sources: ["[[Chp1 - récursivité et complexité]]"]
maj: 2026-11-05
---

Une fonction est récursive si elle est définie, directement ou indirectement, en fonction d'elle-même. Directe : elle s'appelle. Indirecte : B appelle C, C appelle D, D rappelle B.

**Deux parties à coder** : une condition d'arrêt (un `if`) et l'appel récursif, avec des `return`. L'exécution a deux phases : la descente, qui enchaîne les appels jusqu'à la condition d'arrêt, puis la montée, où chaque appel rend sa valeur à celui d'en dessous.

**Exemple** : `fact(n)` renvoie 1 si `n == 0`, sinon `n * fact(n-1)`. Pour `fact(4)`, la descente va jusqu'à `fact(0)`, puis la montée calcule $1, 2, 6, 24$.

**Pile de récursion** : les appels en cours sont empilés dans la pile d'exécution, qui gère tous les appels de fonctions. Chaque bloc stocke les paramètres, l'adresse de retour et les variables locales. En Python, elle est limitée à environ 1000 appels. Voir [[Pile et file]].

**Coût** : se met en équation $T(n) = a\,T(n/b) + f(n)$ et se résout par substitution ou par le théorème de résolution, voir [[Calcul de complexité et théorème de résolution]]. Exemple : [[Recherche dichotomique]].

Le polycopié de 1re année distingue la récursivité terminale, où l'appel récursif est la dernière opération, de la non terminale. Il note aussi que la terminaison d'un programme est indécidable en général. Hauteur et parcours d'un [[Arbre binaire]] sont des exemples classiques.

Liens : [[Calcul de complexité et théorème de résolution]], [[Pile et file]], [[Recherche dichotomique]], [[Tours de Hanoï]], [[Récurrence]], [[Arbre binaire]]

Résumés : [[Chp1 - récursivité et complexité (résumé)]], [[AlgoID1 (résumé)]], [[Chapitre4-Preing2ID (résumé)]]
