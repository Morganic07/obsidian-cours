---
type: concept
tags: [year1, year4]
aliases: [struct, structures en C, typedef struct, typedef, enregistrement, enregistrements, type structuré, types structurés]
matieres: [C++, Algo Maths]
sources: ["[[Chp3 - pointeurs , tableaux, listes chainées, structures]]", ".raw/Year 1/Algo Maths/AlgoID1.pdf"]
maj: 2026-11-06
---

Une structure (`struct`) regroupe sous un même nom plusieurs variables de **types différents**, alors qu'un tableau ne contient que des valeurs du même type. Exemple : un étudiant, avec un `int age` et un `float note`.

- Sans `typedef` : `struct Etudiant { int age; float note; };` puis `struct Etudiant eleve1;`.
- Avec `typedef` (un alias) : `typedef struct Etudiant { ... } Etudiant;` puis `Etudiant eleve1;`.
- Accès à un champ : `eleve1.age = 20;`. Via un pointeur : `p->age`.

Une structure peut contenir un pointeur vers une structure du même type : c'est ainsi qu'on construit le chaînon d'une [[Liste chaînée]] (`struct Chainon *suivant`).

**En pseudo-code (Algo Maths, 1re année)**, on parle d'**enregistrement** ou de type structuré : il regroupe des champs de types différents. On définit d'abord le type (`Structure ... FinStruct`), puis des variables ; l'accès se fait par `variable.champ`, et un champ peut lui-même être un enregistrement (`pers1.ddn.année`). Exercices : fraction, complexe, date, âge d'une personne ; l'examen de janvier 2023 porte sur joueur, équipe et classement.

Notion parente : [[Langage C]]. Liens : [[Liste chaînée]], [[Pointeur et adresse mémoire]], [[Opérateur flèche]]

Résumés : [[Chp3 - pointeurs , tableaux, listes chainées, structures (résumé)]], [[AlgoID1 (résumé)]], [[Contrôles (résumé)|Contrôles (résumé)]]
