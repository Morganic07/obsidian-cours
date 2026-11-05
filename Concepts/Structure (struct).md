---
type: concept
aliases: [struct, structures en C, typedef struct, typedef]
matieres: [C++]
sources: ["[[Chp3 - pointeurs , tableaux, listes chainées, structures]]"]
maj: 2026-11-05
---

Une structure (`struct`) regroupe sous un même nom plusieurs variables de **types différents**, alors qu'un tableau ne contient que des valeurs du même type. Exemple : un étudiant, avec un `int age` et un `float note`.

- Sans `typedef` : `struct Etudiant { int age; float note; };` puis `struct Etudiant eleve1;`.
- Avec `typedef` (un alias) : `typedef struct Etudiant { ... } Etudiant;` puis `Etudiant eleve1;`.
- Accès à un champ : `eleve1.age = 20;`. Via un pointeur : `p->age`.

Une structure peut contenir un pointeur vers une structure du même type : c'est ainsi qu'on construit le chaînon d'une [[Liste chaînée]] (`struct Chainon *suivant`).

Liens : [[Liste chaînée]], [[Pointeur et adresse mémoire]]

Résumé : [[Chp3 - pointeurs , tableaux, listes chainées, structures (résumé)]]
