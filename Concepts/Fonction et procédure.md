---
type: concept
aliases: [procédure, procédures, valeur de retour, programme principal, Fonction en C, déclaration de fonction, signature d'une fonction, type de retour, procédure en C]
matieres: [Algo Maths, C++]
sources: ["[[raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1]]", "[[chp2 - structures code]]"]
maj: 2026-11-06
---

Une fonction reçoit des paramètres en entrée et retourne une valeur ; une procédure est une suite d'instructions nommée, sans valeur retournée.

**Algo Maths** : le programme est le point d'entrée, il appelle mais n'est jamais appelé. L'appel suspend l'appelant ; la fin de l'appelé ramène à l'endroit de l'appel, où le résultat doit être stocké. Fonctions prédéfinies : `ent`, `aléa`, `sqrt`, `longueur`… En Python : fonctions avec ou sans arguments et `return`, modules (`from math import *`).

**C** (C++) : déclaration `float moyenne (int a, int b);` (type de retour, nom, paramètres typés). Règles : déclarer avant d'appeler, implémenter toutes les fonctions, signatures identiques à la déclaration et à l'implémentation, types respectés à l'appel. Un programme se compose des `#include`, des déclarations, de `main` et des implémentations. Une procédure est une fonction qui ne renvoie rien (type `void`) ; selon le cours, tout `void` n'est pas forcément une procédure.

Notion parente : [[Programmation modulaire]]. Voir aussi : [[Passage de paramètres]], [[Passage par valeur]], [[Portée d'une variable]], [[Récursivité]], [[Pointeur et adresse mémoire]], [[Erreur de compilation]].

## À vérifier

- C : dans la fonction `affiche_points` de l'image, `i` et `j` ne sont pas déclarés (relevé du résumé).

Résumés : [[AlgoID1 (résumé)]], [[Contrôles (résumé)]], [[chp2 - structures code (résumé)]]
