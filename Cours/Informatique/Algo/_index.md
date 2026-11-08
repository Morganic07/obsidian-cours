---
type: matiere
tags:
  - year1
  - year2
sources:
  - "[[0 - Algo Maths|Cours 1 (Algo Maths)]]"
  - "[[0 - diapo prof|AlgoID1]]"
  - "[[0 - Python|Python (Algo Maths)]]"
  - "[[1 - récursivité et complexité|Chp1 - récursivité et complexité]]"
  - "[[2 - piles listes file|chp2 - piles listes file]]"
  - "[[Raw/Year 2/Algo/DM/AVL momo.docx|AVL momo]]"
  - "[[Raw/Year 2/Algo/DM/qui dit quoi AVL.docx|qui dit quoi AVL]]"
  - "[[Raw/Year 2/Algo/DM/TD_Algo.docx|TD_Algo]]"
maj: 2026-11-08
---

Algorithmique et programmation en Python : récursivité, complexité, structures de données linéaires, puis arbres AVL. En Year 2, deux notes de cours (chapitres 1 et 2) et quatre PDF ; la partie Year 1 (ancienne matière Algo Maths) est en fin de page.

## Parcours

| Note | Sujet | Résumé |
|---|---|---|
| [[1 - récursivité et complexité\|Chp1 - récursivité et complexité]] | Récursivité, pile de récursion, complexité, dichotomie | [[1 - récursivité et complexité\|Résumé]] |
| [[2 - piles listes file\|chp2 - piles listes file]] | Listes, piles, files | [[2 - piles listes file\|Résumé]] |

## Documents PDF

Quatre PDF complètent les notes : trois chapitres de cours sur les arbres (ils font suite aux chapitres 1 et 2 ; les « chapitres 3 à 5 » de l'enseignante) et une fiche de cours sur l'AVL.

| Document | Contenu | Résumé |
|---|---|---|
| Chapitre3-Arbres ([[Raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf\|Chapitre3-Arbres.pdf]]) | Rappel sur les graphes, définition et vocabulaire des arbres | [[3 - Arbres\|Résumé]] |
| Chapitre4-Preing2ID ([[Raw/Year 2/Algo/Cours/Chapitre4-Preing2ID.pdf\|Chapitre4-Preing2ID.pdf]]) | Arbres binaires : propriétés, parcours, code Python | [[4 - Arbres binaires\|Résumé]] |
| Chapitre5-ABR ([[Raw/Year 2/Algo/Cours/Chapitre5-ABR.pdf\|Chapitre5-ABR.pdf]]) | Arbres binaires de recherche : insertion, recherche, suppression | [[5 - ABR\|Résumé]] |
| ARBRE AVL ([[Raw/Year 2/Algo/DM/ARBRE AVL.pdf\|ARBRE AVL.pdf]]) | Fiche AVL : rotations, insertion, suppression, pseudo-code | [[6 - AVL\|Résumé]] |

## Concepts

- **Récursivité** : [[Récursivité]], [[Récurrence]], [[Factorielle]], [[Pile d'exécution]], [[Diviser pour régner]]
- **Complexité** : [[Complexité algorithmique]], [[Calcul de complexité et théorème de résolution]], [[Classe de complexité]], [[Recherche dichotomique]], [[Partie entière]]
- **Structures de données linéaires** : [[Liste chaînée]], [[Pile et file]]
- **Rappels sur les graphes** : [[Graphe non orienté]], [[Graphe orienté]], [[Chemin (graphe)]], [[Cycle (graphe)]], [[Circuit (graphe)]], [[Sous-graphe]]
- **Arbres** : [[Arbre (théorie des graphes)]], [[Arborescence (graphe)]], [[Vocabulaire des arbres]], [[Hauteur d'un arbre]], [[Arbre m-aire]], [[B-arbre]], [[Arbre binaire]], [[Arbre binaire de recherche]], [[Méthode spéciale Python]], [[Arbre AVL]]
- **Ajoutés par l'enrichissement** : [[Machine de Turing]], [[Invariant de boucle]], [[Tri fusion]], [[Tas binaire]], [[Notation polonaise]], [[Arbre rouge-noir]]

Les fiches sont enrichies de compléments hors du cours (passages marqués ⓘ).

## À revoir en priorité avant un examen

- [[1 - récursivité et complexité]] : la méthode de substitution se déroule jusqu'au cas de base $T(0)$, d'où $T(n) = nb + c$.

## Liens avec les autres matières

- **[[Cours/Mathématiques/Analyse/_index|Analyse]]** : la notation $O$ rejoint la [[Comparaison asymptotique]] des fonctions et des suites.
- **C++** (Year 4) : la [[Liste chaînée]] est reprise avec des pointeurs dans [[3 - pointeurs , tableaux, listes chainées, structures|le chapitre 3 de C++]]. La pile d'exécution est celle de la gestion mémoire en [[1 - basiques|C++ chapitre 1]].
- **Graph theory** (Year 4) : le cours de théorie des graphes a sa propre page de [[Complexité algorithmique]]. Les rappels du chapitre 3 ([[Graphe non orienté]], [[Graphe orienté]], [[Chemin (graphe)]], [[Cycle (graphe)]], [[Sous-graphe]], [[Arbre (théorie des graphes)]]) y sont repris en détail : [[Cours/Informatique/Graph theory/_index|Graph theory]].
- **Year 1** (section ci-dessous) : [[Récursivité]], [[Récurrence]] et [[Factorielle]] y sont introduites ; la [[Récurrence]] l'est aussi en [[Cours/Mathématiques/Outil Maths/_index|Outil Maths]].

## Year 1

Ancienne matière Algo Maths, rattachée à Algo. Premiers pas en algorithmique : récurrence, récursivité, pseudo-code, Python. Trois documents sont intégrés.

| Note | Sujet | Résumé |
|---|---|---|
| [[0 - Algo Maths\|Cours 1 (Algo Maths)]] | Notions, Hanoï, crayons, carré magique | [[0 - Algo Maths\|Résumé]] |
| [[0 - Python\|Python (Algo Maths)]] | `range`, boucle sans variable, `print(..., end="")` | [[0 - Python\|Résumé]] |
| AlgoID1 (PDF, 163 pages) | Introduction, pseudo-code, fonctions et procédures, Python, enregistrements, récursivité, avec TD | [[0 - diapo prof\|Résumé]] |

### Concepts

- **Notions de départ (Cours 1)** : [[Algorithme]], [[Modélisation d'un problème]], [[Problème du passeur]], [[Correction d'un algorithme]], [[Récurrence]], [[Problème des crayons]], [[Somme des premiers entiers]], [[Carré magique]], [[Fractale]], [[Nombre premier]], [[Bit]], [[Transistor]], [[Numération binaire]], [[Nombre à virgule flottante]], [[Loi de Parkinson]]
- **Pseudo-code et types** : [[Pseudo-code]], [[Affectation]], [[Échange de deux variables]], [[Type primitif]], [[Chaîne de caractères]], [[Division euclidienne]], [[Structure conditionnelle]], [[Boucle (programmation)]], [[Équation du second degré]], [[Palindrome]]
- **Fonctions et enregistrements** : [[Fonction et procédure]], [[Passage de paramètres]], [[Portée d'une variable]], [[Programmation modulaire]], [[Structure (struct)]], [[Pile et file]] (voir [[0 - diapo prof]])
- **Python** : [[Langage Python]], [[Langage interprété]], [[Typage dynamique]], [[Fonction range (Python)]], [[Dataclass (Python)]]
- **Récursivité** : [[Récursivité]], [[Récursivité terminale]], [[Terminaison d'un algorithme]], [[Conjecture de Syracuse]], [[Problème indécidable]], [[Factorielle]], [[Suite de Fibonacci]], [[Algorithme d'Euclide]], [[Exponentiation rapide]], [[Recherche dichotomique]], [[Tours de Hanoï]]
- **Problèmes difficiles et sac à dos** : [[Complexité algorithmique]] (cours de graphes), [[Problème du voyageur de commerce]], [[Algorithme d'approximation]], [[Problème du sac à dos]], [[Recherche exhaustive]], [[Code de Gray]], [[Algorithme glouton]], [[Algorithme stochastique]], [[Programmation dynamique]]

### À revoir en priorité avant un examen

- [[0 - Algo Maths|Cours 1]] : dans le faux raisonnement des crayons, l'hérédité échoue de $k = 1$ à $k = 2$ ; un flottant n'est pas un réel : en Python, `0.1 + 0.2 == 0.3` vaut `False`.
- [[0 - Python|Python]] : `range(début, fin, pas)` ajoute le pas à chaque tour : `range(2, 10, 5)` donne 2, 7.

### Liens avec les autres matières

- **[[Cours/Mathématiques/Outil Maths/_index|Outil Maths]]** : [[Récurrence]] et [[Logique propositionnelle]].
- **[[Cours/Informatique/Graph theory/_index|Graph theory]]** : la complexité des [[Tours de Hanoï]] ; l'[[Algorithme glouton]] de Kruskal ([[Arbre couvrant minimal]]).
- **[[Cours/Informatique/Java/_index|Java]]** et **[[Cours/Informatique/C++/_index|C++]]** : [[Type primitif]], [[Structure conditionnelle]] et [[Boucle (programmation)]] dans d'autres langages.
- **[[Cours/Mathématiques/Analyse Maths/_index|Analyse Maths]]** : [[Factorielle]], [[Suite de Fibonacci]] et [[Équation du second degré]].
