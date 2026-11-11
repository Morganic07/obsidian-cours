---
type: concept
tags:
  - year1
  - year4
aliases:
  - procédure
  - procédures
  - valeur de retour
  - programme principal
  - Fonction en C
  - déclaration de fonction
  - signature d'une fonction
  - type de retour
  - procédure en C
matieres:
  - Algo Maths
  - C++
sources:
  - "[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"
  - "[[2 - structures code|chp2 - structures code]]"
maj: 2026-11-11
---

Une fonction reçoit des paramètres en entrée et retourne une valeur ; une procédure est une suite d'instructions nommée, sans valeur retournée.

**Algo Maths** : le programme est le point d'entrée, il appelle mais n'est jamais appelé. L'appel suspend l'appelant ; la fin de l'appelé ramène à l'endroit de l'appel, où le résultat doit être stocké. Fonctions prédéfinies : `ent`, `aléa`, `sqrt`, `longueur`… En Python : fonctions avec ou sans arguments et `return`, modules (`from math import *`).

**C** (C++) : déclaration `float moyenne (int a, int b);` (type de retour, nom, paramètres typés). Règles : déclarer avant d'appeler, implémenter toutes les fonctions, signatures identiques à la déclaration et à l'implémentation, types respectés à l'appel. Un programme se compose des `#include`, des déclarations, de `main` et des implémentations. Une procédure est une fonction qui ne renvoie rien (type `void`) ; selon le cours, tout `void` n'est pas forcément une procédure.

Notion parente : [[Programmation modulaire]]. Voir aussi : [[Passage de paramètres]], [[Passage par valeur]], [[Portée d'une variable]], [[Récursivité]], [[Pointeur et adresse mémoire]], [[Erreur de compilation]].

## Dans le cours

**C++** ([[4 - Cours complet]]) : une fonction a un type de retour, un nom, une liste de paramètres et un corps. On définit une fonction pour un traitement distinct et nommé : plus clair, réutilisable, plus facile à tester ; chaque fonction réalise une seule action logique, sans saisie ni affichage, en 10 à 15 lignes au plus, et son nom est un verbe. Une fonction `void` est une procédure.

Résumés : [[0 - diapo prof]], [[2 - structures code]], [[4 - Cours complet]]
