---
type: concept
tags:
  - year1
  - year4
aliases:
  - struct
  - structures en C
  - typedef struct
  - enregistrement
  - enregistrements
  - type structuré
  - types structurés
matieres:
  - C／C++
  - Algo Maths
sources:
  - "[[3 - pointeurs , tableaux, listes chainées, structures|Chp3 - pointeurs , tableaux, listes chainées, structures]]"
  - "[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"
  - "[[Raw/Year 4/C／C++/chp4 prise de note.pdf|chp4 prise de note.pdf]]"
  - "[[Raw/Year 4/C／C++/Chp3 - pointeurs , tableaux, listes chainées, structures.docx|Chp3 - pointeurs , tableaux, listes chainées, structures]]"
maj: 2026-11-12
---

Une structure (`struct`) regroupe sous un même nom plusieurs variables de **types différents**, alors qu'un tableau ne contient que des valeurs du même type. Exemple : un étudiant, avec un `int age` et un `float note`.

- Sans `typedef` : `struct Etudiant { int age; float note; };` puis `struct Etudiant eleve1;`.
- Avec `typedef` (un alias) : `typedef struct Etudiant { ... } Etudiant;` puis `Etudiant eleve1;`.
- Accès à un champ : `eleve1.age = 20;`. Via un pointeur : `p->age`.

**Compléments (hors du cours)** :

- **Initialisation groupée** : `Etudiant e = {20, 15.5};` remplit les champs dans l'ordre de leur déclaration.
- **Copie** : une structure est copiée champ par champ lors d'une affectation (`e2 = e1;`) ou d'un passage à une fonction par valeur ; la fonction travaille alors sur une copie. Pour éviter la copie ou modifier l'original, on passe un pointeur `Etudiant *p` et on accède aux champs par `p->age` (voir [[Opérateur flèche]], [[Passage par valeur]]).
- **Alignement** : le compilateur ajoute des octets de remplissage (*padding*) pour aligner les champs en mémoire, si bien que `sizeof` d'une structure peut dépasser la somme des tailles de ses champs. `struct { char c; int i; }` fait en général 8 octets, et non 5 (1 octet pour `c`, 3 de remplissage, 4 pour `i`).
- **En C++**, une `struct` est une classe dont les membres sont publics par défaut (privés dans une `class`) ; elle peut avoir des méthodes et des constructeurs, et le mot `struct` n'est plus requis devant le nom : `Etudiant e;` suffit, sans `typedef`.

Une structure peut contenir un pointeur vers une structure du même type : c'est ainsi qu'on construit le chaînon d'une [[Liste chaînée]] (`struct Chainon *suivant`).

**En pseudo-code (Algo Maths, 1re année)**, on parle d'**enregistrement** ou de type structuré : il regroupe des champs de types différents. On définit d'abord le type (`Structure ... FinStruct`), puis des variables ; l'accès se fait par `variable.champ`, et un champ peut lui-même être un enregistrement (`pers1.ddn.année`). Exercices : fraction, complexe, date, âge d'une personne ; l'examen de janvier 2023 porte sur joueur, équipe et classement.

**En C++** (chapitre 4) : la prise de note rapproche la `class` du C++ de la `struct` du C : toutes deux permettent de créer un type de variable ([[4 - Prise de note]]). La classe y ajoute des fonctions membres et des droits d'accès `public` / `private` (voir [[Classe et objet]]).

Notion parente : [[Langage C]]. Liens : [[Liste chaînée]], [[Pointeur et adresse mémoire]], [[Opérateur flèche]], [[Classe et objet]]

## Dans le cours

- [[td listes chaînées]] : structure autoréférente `typedef struct Chainon { int valeur; struct Chainon *suivant; } Chainon;` ([[Alias de type (typedef)]]), allouée par `malloc(sizeof(Chainon))` ([[Opérateur sizeof]]) ; un prototype placé avant ce `typedef` empêchait ex1.c de compiler.
- [[formation C++]] : en C++, `class` et `struct` ne diffèrent que par l'accès par défaut des membres (privé pour `class`, public pour `struct`).

Résumés : [[3 - pointeurs , tableaux, listes chainées, structures]], [[0 - diapo prof]], [[4 - Prise de note]]
