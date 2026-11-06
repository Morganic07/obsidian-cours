---
type: source
sources: ["[[raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1 (PDF)]]"]
maj: 2026-11-06
---

Résumé du recueil [[raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1 (PDF)]] (163 pages, CY Tech, pré-ING 1re année), dans [[Year 1 - Algo Maths]]. Plusieurs supports sont collés bout à bout : cours d'introduction, éléments de base en pseudo-code, fonctions et procédures, Python, types structurés, récursivité, avec leurs TD. Notions déjà dans le wiki : [[Récursivité]], [[Tours de Hanoï]], [[Structure (struct)]], [[Portée d'une variable]], [[Pile et file]], [[Récurrence]], et le résumé [[Python (résumé)]].

Limite de lecture : le texte est extrait en entier, mais certaines diapositives sont des images (code Python, figures, schémas) que le texte ne rend pas. Elles ne sont pas résumées.

## 1. Introduction à l'algorithmique

- Objectifs : initiation à l'algorithmique procédurale et à la programmation en C ; évaluation par DS et projets.
- **Algorithme** : procédure de calcul bien définie qui transforme une ou plusieurs valeurs d'entrée en sortie (définition de Cormen et al., source principale du cours). Un problème spécifie la relation entrée / sortie.
- Spécifier un algorithme : langage humain, pseudo-code, langage informatique.
- Exemples : gâteau aux pommes, passeur (loup, chèvre, chou), tri d'une suite de nombres (instance, entrée, sortie).
- **Correction** : un algorithme est correct s'il se termine, pour toute entrée, avec la bonne sortie. Un algorithme incorrect peut servir si son taux d'erreur est contrôlé.
- **Problèmes difficiles** : voyageur de commerce, sans algorithme exact efficace connu, mais avec des algorithmes d'approximation.
- **Modélisation** : formaliser objets et opérations d'un problème réel (cartes routières et graphes, gestion de ressources d'une compagnie aérienne, commerce électronique et cryptographie).
- **Décomposition** en sous-problèmes (citation de Descartes), modularité.
- Les erreurs coûtent cher : explosion d'Ariane 5 en 1996 (programme d'Ariane 4 non reconfiguré). L'algorithmique reste nécessaire malgré la puissance des machines (loi de Parkinson).

## 2. Éléments de base en pseudo-code

- Structure d'un `PROGRAMME ... DEBUT ... FIN`, commentaires, `ECRIRE`, `LIRE`.
- **Variables et types** : `ENTIER` (opérateurs `+ - * DIV MOD`), `REEL`, `BOOLEEN` (`ET OU NON`), `CARACTERE`, `CHAINE` (concaténation `&`). Déclaration avant le programme.
- **Affectation** `←` : initialisation, expression de même type que la variable.
- **Conditionnelle** : opérateurs de comparaison, `SI ... ALORS ... SINON ... FINSI`, `SELON ... CAS ... DEFAUT ... FINSELON`. Exercices : température de l'eau, année bissextile.
- **Boucles** : `TANTQUE` (test avant), `REPETER ... JUSQUACEQUE` (test après), `POUR i DE ... A ...` (compteur, ne pas modifier `i`). Exemple : somme $1 + 2 + \dots + n$ ; exercice : produit $1 \times \dots \times N$ en trois versions. `SI` n'est pas une boucle.
- **TD** : valeur de variables après une suite d'affectations ; **permutation** avec une variable temporaire ; saisie et affichage (carré, moyenne, total TTC, pouces en cm, décomposition en billets et pièces avec DIV et MOD, secondes en heures, minutes, secondes).

## 3. Fonctions et procédures

- **Fonction** : paramètres en entrée, une valeur retournée. **Procédure** : tâche nommée, sans valeur retournée. **Programme** : point d'entrée, appelle mais n'est jamais appelé. Exemples : `calculeCarre`, résolution de $ax + b = 0$, `puissance`, équation du second degré (disjonction de cas sur $\Delta$).
- **Appel** : suspension de l'appelant, retour à l'endroit de l'appel, résultat à stocker.
- **Variables locales et globales** : trois exemples où il faut prévoir l'affichage (la modification d'un paramètre n'affecte pas l'argument, celle d'une globale si).
- **Plusieurs résultats** : retourner une structure, ou utiliser des paramètres de sortie. Modes `E` (entrée), `S` (sortie), `ES` (entrée-sortie). Exemple : `divisionEntiere` par soustractions. `permuter` sans `ES` ne change rien aux variables de l'appelant ; `permuter2` avec `ES` marche.
- Fonctions prédéfinies (`ent`, `aléa`, `sqrt`, `longueur`, `extrait`, `trouve`, `ascii`, `carac`) ; **présentation modulaire** (modules courts, testables, peu de variables globales).

## 4. Python

- **Fonctions en Python** : avantages (pas de ré-écriture, approche modulaire, réutilisation), fonctions avec ou sans arguments et avec ou sans `return`. Passage par valeur de la référence : un argument mutable peut être modifié hors de la fonction (effets de bord). Modules (`from math import *`). Exercices : nombre de premiers inférieurs à $n$, aire d'un triangle, maximum de trois nombres, inversion d'une chaîne.
- **Introduction** (cours en anglais, 2018-2019) : langage interprété, typé dynamiquement, indentation significative ; types de base, affectation simple, simultanée, concurrente ; opérateurs arithmétiques (dont `//` et `**`), logiques, relationnels ; `x += 1` ; `print`, `input` ; `if / elif / else`, `while`, `for ... in`, `break`, `continue`.

## 5. Types structurés (enregistrements)

- Un enregistrement regroupe des champs de types différents ; on définit d'abord le type (`Structure ... FinStruct`) puis des variables. Accès `variable.champ`. Un champ peut être lui-même un enregistrement (`pers1.ddn.année`).
- Exemples : complexe, date, stage, personne, produit et fournisseur. Exercices : fraction (affichage, addition), complexe, âge d'une personne à une date donnée (0 si la date est antérieure à la naissance).

## 6. Récursivité

- Définition : un algorithme est récursif s'il s'appelle lui-même, en correspondance avec la [[Récurrence]]. Exemples : factorielle, PGCD d'Euclide, [[Tours de Hanoï]] (`Déplacer(n, de, à, par)`), Fibonacci.
- **Forme générale** d'une fonction récursive : condition d'arrêt $c(x)$, cas trivial $g(x)$, appel sur le successeur $s(x)$ ; idem pour une procédure.
- **Types** : simple ou multiple ; terminale (l'appel est la dernière instruction) ou non terminale.
- **Terminaison** : la condition d'arrêt doit être atteinte. Exemples à discuter : `exemple1` à `exemple4` (le dernier est la suite de Syracuse, dont on ne sait pas démontrer la terminaison). La terminaison d'un programme est **indécidable**.
- **Avantages et coûts** : code court et proche des mathématiques, mais pile d'appels coûteuse ([[Pile et file]]) ; la récursivité terminale avec accumulateur y remédie ; tout algorithme récursif a une version itérative.
- Factorielle terminale `factRT(n, acc)`, Fibonacci naïf (sous-calculs répétés : `Fibo(3)` deux fois, `Fibo(2)` trois fois) et terminal `fiboRT(n, fn-2, fn-1)`.
- **TD3** : quotient et reste de la division entière, palindrome, miroir d'une chaîne (récursif et itératif), puissance $n^k$ naïve, terminale, par dichotomie ($n^k = (n \cdot n)^{k/2}$ si $k$ pair), dichotomie terminale.

## Points à vérifier

- **Factorielle récursive** : le cas d'arrêt est `n = 1`, donc `fact(0)` ne se termine pas. L'énoncé suppose $n \geq 1$ ; avec le cas `n = 0` la fonction vaudrait aussi pour 0 (complément).
- **Noms incohérents** : `calculeCarre` défini, `calculCarre` appelé ; `rep : INTEGER` dans un programme où le type s'écrit `ENTIER` ; `FINTANQUE` dans la syntaxe et `FINTANTQUE` dans l'exemple. Sans conséquence pour le fond.
- **Python** : `print i` dans l'exemple de boucle sur une chaîne est la syntaxe de Python 2 ; en Python 3 il faut `print(i)` (complément).
