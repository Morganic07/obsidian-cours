---
type: matiere
tags:
  - year4
sources:
  - "[[1 - basiques|Chp1 - basiques]]"
  - "[[2 - structures code|chp2 - structures code]]"
  - "[[3 - pointeurs , tableaux, listes chainées, structures|Chp3 - pointeurs , tableaux, listes chainées, structures]]"
  - "[[4 - C++|chp4 C++]]"
  - "[[4 - Prise de note|chp4 prise de note]]"
  - "[[4 - Cours complet|chp4 C++ - cours super complet]]"
  - "[[5 - Compilation séparée|chp5 compilation séparée]]"
  - "[[tp2|programmes C/tp2]]"
  - "[[tp3|programmes C/tp3]]"
  - "[[tp4|programmes C/tp4]]"
  - "[[tp5|programmes C/tp5]]"
  - "[[tp6|programmes C/tp6]]"
  - "[[tp7|programmes C/tp7]]"
  - "[[tableaux|programmes C/tableaux]]"
  - "[[pointeurs|programmes C/pointeurs]]"
  - "[[td listes chaînées|programmes C/td_liste_chainees]]"
  - "[[formation C++|programmes C++/formation]]"
  - "[[exo-prof|programmes C++/exo-prof]]"
  - "[[compilation séparée (C++)|programmes C++/compilation separée]]"
maj: 2026-11-12
---

Programmation bas niveau, puis objet. Les trois premières notes portent sur le [[Langage C|langage C]] (`printf`, `malloc`, `struct`), d'où le nom du dossier de Drive, `C／C++` (renommé le 2026-11-12, autrefois `C++`) ; le chapitre 4 passe au [[Langage C++|C++]] et à la [[Programmation orientée objet|programmation orientée objet]], avec un polycopié de TP complet ; le chapitre 5 découpe le code en plusieurs fichiers ([[Compilation séparée|compilation séparée]], [[Make (logiciel)|Makefile]]). Les 7 documents sont intégrés, ainsi que les programmes de l'utilisatrice (78 fichiers `.c`, `.cpp`, `.h` et Makefile, une fiche par dossier), dont les commentaires reprennent le cours.

## Parcours

| Note | Sujet | Résumé |
|---|---|---|
| [[1 - basiques\|Chp1 - basiques]] | Syntaxe, types, mémoire, erreurs, questions pièges | [[1 - basiques\|Résumé]] |
| [[2 - structures code\|chp2 - structures code]] | Boucles, `switch`, fonctions, tableaux | [[2 - structures code\|Résumé]] |
| [[3 - pointeurs , tableaux, listes chainées, structures\|Chp3 - pointeurs , tableaux, listes chainées, structures]] | Adresses, pointeurs, passage par adresse, `struct`, listes chaînées | [[3 - pointeurs , tableaux, listes chainées, structures\|Résumé]] |
| [[4 - C++\|chp4 C++]] | Diaporama : bases du C++, `std::cout`, classes, public/privé, constructeurs, get/set, surcharge d'opérateurs, exercices `Point`, `Segment` et `Maze` | [[4 - C++\|Résumé]] |
| [[4 - Prise de note\|chp4 prise de note]] | Notes manuscrites du chapitre 4 : compilation avec `g++`, exercices `Cercle` faits en séance et leur sortie | [[4 - Prise de note\|Résumé]] |
| [[4 - Cours complet\|chp4 C++ - cours super complet]] | Polycopié de TP (2012) : fabrication avec `g++` (compilation, édition de liens), types, `cin`/`cout`, règles de codage, affectation et initialisation, `if`/`switch`/`while`/`for`, constantes, pointeurs et références, fonctions, programmation modulaire avec make ; 56 questions de révision et 6 exercices, avec leurs solutions | [[4 - Cours complet\|Résumé]] |
| [[5 - Compilation séparée\|chp5 compilation séparée]] | Diaporama : fichiers `.h` et `.cpp`, `#include` et garde d'inclusion, compilation séparée en `.o`, édition de liens, Makefile (classes `Point` et `Segment`) | [[5 - Compilation séparée\|Résumé]] |

## Programmes

Les programmes du Drive (dossiers `programmes C` et `programmes C++`), un dossier par fiche, dans l'ordre du cours ; les fiches portent le nom de leur dossier et sont rangées dans les sous-dossiers `programmesC/` (de tp2 à td listes chaînées) et `programmesCPP/` (formation C++, exo-prof, compilation séparée). Chaque programme y est donné en bloc de code, compilé et exécuté, ses commentaires remis en explications ; les erreurs trouvées sont corrigées (✎).

| Fiche | Dossier | Chapitre illustré | Contenu |
|---|---|---|---|
| [[tp2]] | `programmes C/tp2` (10) | [[1 - basiques]] | Types, variables, `printf` et `scanf`, opérateurs arithmétiques, division entière |
| [[tp3]] | `programmes C/tp3` (12) | [[2 - structures code]] | Conditions, opérateurs de comparaison et logiques, `if … else if`, `switch` |
| [[tp4]] | `programmes C/tp4` (9) | [[2 - structures code]] | Boucle `for`, `break`, compteurs et accumulateurs, suites, boucles imbriquées |
| [[tp5]] | `programmes C/tp5` (8) | [[2 - structures code]] | `while` et `do … while` : nombres premiers et parfaits, suite de Syracuse, drapeau |
| [[tp6]] | `programmes C/tp6` (3) | [[2 - structures code]] | Fonctions, prototypes, `return` (puissance, ordre, volumes) |
| [[tp7]] | `programmes C/tp7` (5) | [[2 - structures code]], [[3 - pointeurs , tableaux, listes chainées, structures\|Chp3]] | Tableaux remplis, parcourus et passés à une fonction ; minimum, maximum, moyenne |
| [[tableaux]] | `programmes C/tableaux` (2) | [[3 - pointeurs , tableaux, listes chainées, structures\|Chp3]] | `init_tab` et `affiche_tab` en syntaxe pointeur et en syntaxe tableau |
| [[pointeurs]] | `programmes C/pointeurs` (1) | [[3 - pointeurs , tableaux, listes chainées, structures\|Chp3]] | `echange` par adresse |
| [[td listes chaînées]] | `programmes C/td_liste_chainees` (6) | [[3 - pointeurs , tableaux, listes chainées, structures\|Chp3]] | `struct Chainon`, double pointeur, ajout, comptage, suppression, recherche, libération |
| [[formation C++]] | `programmes C++/formation` (13) | [[4 - C++]], [[4 - Cours complet]] | Progression commentée : variables, `cout`, conditions, boucles, classe, constructeurs, méthodes, surcharge d'opérateurs, `operator<<` |
| [[exo-prof]] | `programmes C++/exo-prof` (3) | [[4 - C++]] | Classes `Point` et `Segment` : constructeurs, accesseurs, affichage |
| [[compilation séparée (C++)]] | `programmes C++/compilation separée` (6) | [[5 - Compilation séparée]] | `Point` et `Segment` en `.h` et `.cpp`, `main.cpp`, Makefile |

## Concepts

- **Langage et compilation (Chp1)** : [[Langage C]], [[Typage statique]], [[Mot réservé]], [[Type primitif]], [[Transtypage]], [[Variable non initialisée]], [[Fonctions printf et scanf]], [[Erreur de compilation]], [[Erreur de segmentation]], [[Pile d'exécution]]
- **Représentation des données (Chp1)** : [[Numération binaire]], [[Notation hexadécimale]], [[Complément à deux]], [[Norme IEEE 754]], [[Code ASCII]]
- **Structures de contrôle (Chp1 et chp2)** : [[Opérateur de comparaison]], [[Évaluation en court-circuit]], [[Structure conditionnelle]], [[Boucle (programmation)]], [[Instruction vide]], [[Fonction et procédure]], [[Passage par valeur]]
- **Mémoire et pointeurs (chp2 et Chp3)** : [[Tableau (programmation)]], [[Pointeur et adresse mémoire]], [[Arithmétique des pointeurs]], [[Pointeur NULL]], [[Allocation dynamique]], [[Structure (struct)]], [[Opérateur flèche]], [[Liste chaînée]]
- **Le C++ (chp4)** : [[Langage C++]], [[GCC]] (`g++`), [[Espace de noms (namespace)]], [[Flux d'entrée-sortie (C++)]], [[Référence (C++)]]
- **Programmation objet (chp4)** : [[Programmation orientée objet]], [[Classe et objet]], [[Encapsulation (programmation)]], [[Constructeur (programmation)]], [[Accesseur et mutateur]], [[Surcharge d'opérateurs]], [[Fonction amie (friend)]], [[Distance]] (exercice `Maze`)
- **Polycopié de TP (chp4, cours complet)** : [[Compilateur]], [[Langage compilé]], [[Code machine]], [[Langage d'assemblage]], [[Environnement de développement intégré]], [[Débogueur]], [[Commentaire (programmation)]], [[Fonction main (C et C++)]], [[Instruction (programmation)]], [[Expression (programmation)]], [[Bloc d'instructions]], [[Lvalue et rvalue]], [[Initialisation (programmation)]], [[Valeur littérale]], [[Type entier]], [[Type char]], [[Booléen]], [[Classe string (C++)]], [[Fonction getline]], [[Opérateurs arithmétiques]], [[Opérateur d'affectation composée]], [[Règle de codage]], [[Macro (préprocesseur)]], [[Déréférencement]], [[Opérateur d'adresse]], [[Argument et paramètre]], [[Appel de fonction]], [[Accumulateur (programmation)]], [[Valeur sentinelle]], [[Dépassement d'entier]], [[Portabilité (informatique)]], [[Norme du C]]
- **Compilation séparée (chp5)** : [[Compilation séparée]], [[Programmation modulaire]], [[Fichier d'en-tête]], [[Fichier source]], [[Interface et implémentation]], [[Déclaration et définition]], [[Préprocesseur]], [[Directive include]], [[Garde d'inclusion]], [[Compilation conditionnelle]], [[Unité de compilation]], [[Fichier objet]], [[Édition de liens]], [[Symbole (édition de liens)]], [[Exécutable]], [[Option de compilation]], [[Make (logiciel)]], [[Liste d'initialisation]], [[Opérateur de résolution de portée]], [[Bibliothèque standard du C++]], [[Norme du C++]]
- **Ajoutés par l'enrichissement** : [[Règle de la définition unique]], [[Fonction inline]], [[Méthode constante]], [[Avertissement de compilation]], [[Bibliothèque statique]], [[CMake]], [[Clang]], [[Comportement indéfini]], [[Chaîne de compilation]], [[Fichier d'en-tête]], [[Pointeur pendant]], [[Fuite mémoire]], [[Destructeur (programmation)]], [[Héritage (programmation)]]
- **Programmes C (`programmesC/`)** : [[Identificateur (programmation)]], [[Opérateur sizeof]], [[Opérateur bit à bit]], [[Opérateur virgule]], [[Comparaison de nombres flottants]], [[Instructions break et continue]], [[Instruction return]], [[Table de sauts]], [[Boucle imbriquée]], [[Drapeau (programmation)]], [[Erreur de décalage d'une unité]], [[Masquage de nom]], [[Décroissance d'un tableau en pointeur]], [[Dépassement de tampon]], [[Double pointeur]], [[Alias de type (typedef)]], [[Bibliothèque standard du C]], [[POSIX]], [[AddressSanitizer]], [[Valgrind]], [[Crible d'Ératosthène]], [[Art ASCII]], [[Norme ISO 8601]], [[Pavé numérique]]
- **Programmes C++ (`programmesCPP/`)** : [[Surcharge de fonctions]], [[Pointeur this]], [[Opérateur unaire et opérateur binaire]], [[Opérateur d'affectation par copie]], [[Copie superficielle et copie profonde]], [[Règle de zéro]], [[Invariant de classe]], [[Composition (programmation)]], [[Paire et tuple (C++)]], [[Classe list (C++)]], [[Compilation incrémentale]]
- **Notions mathématiques et autres des exercices** : [[Puissance (mathématiques)]], [[Exponentiation]], [[Fonction affine]], [[Équation du premier degré]], [[Aire (géométrie)]], [[Volume (géométrie)]], [[Nombre pi]], [[Nombre de Mersenne]], [[Nombres de Lucas]], [[Échelle logarithmique]], [[Échelle de Richter]], [[Magnitude de moment]], [[Séisme]], [[Année bissextile]], [[Calendrier grégorien]], [[Mention (diplôme)]], [[Droit de vote]]

Les fiches sont enrichies de compléments hors du cours (passages marqués ⓘ).

## À revoir en priorité avant un examen

- [[1 - basiques]] : `if (a = 3)` est une affectation, toujours vraie, et non une comparaison ; `a == b == c` ne teste pas l'égalité des trois valeurs (écrire `a == b && b == c`).
- [[3 - pointeurs , tableaux, listes chainées, structures]] : un `int` fait en général 4 octets, y compris sur un système 64 bits ; une adresse s'affiche avec `%p` ; dans le programme `malloc`, `free` libère le bloc sans effacer son contenu.
- [[4 - C++]] : un attribut privé n'est pas accessible hors de la classe (passer par un accesseur).
- [[4 - Prise de note]] : dans un constructeur, `int x = 0;` déclare une variable locale ; l'attribut s'initialise par `x = 0;` ou par la liste d'initialisation ; le séparateur décimal est le point (`13.3`).
- [[4 - Cours complet]] : `string` demande `#include <string>` et `std::` (ou `using namespace std;`) ; appeler une fonction avant de l'avoir déclarée est une erreur en C++, pas un avertissement.
- [[5 - Compilation séparée]] : le `main` du cours appelle une méthode `affiche()` que les classes ne déclarent pas ; un `.h` ne contient que des déclarations ; dans un Makefile, la commande commence par une tabulation.

## Liens avec les autres matières

- **[[Cours/Informatique/Algo/_index|Algo]]** : la [[Liste chaînée]] y est vue sans pointeurs, avec la pile d'exécution et la récursivité ; les arbres binaires de recherche y sont programmés en objet en Python (classe `Node`, [[Méthode spéciale Python|méthodes spéciales]] `__init__` et `__str__`), à comparer aux [[Constructeur (programmation)|constructeurs]] du chapitre 4.
- **[[Cours/Informatique/Java/_index|Java]]** : les mêmes structures de contrôle, avec le [[Transtypage]] et l'[[Évaluation en court-circuit]] ; Java est aussi un langage à classes (voir [[Programmation orientée objet]]).
- **[[Cours/Informatique/OS/_index|Operating System]]** : en Bash, la [[Structure conditionnelle]], la [[Boucle (programmation)]], le [[Tableau (programmation)]], l'[[Opérateur de comparaison]] et le [[Code ASCII]] ont leur équivalent shell ; les programmes C y sont compilés avec [[GCC]].
- **[[Cours/Informatique/Algo/_index|Algo]]** : le [[Type primitif]], la [[Fonction et procédure]] et la [[Structure (struct)]] y sont introduits en pseudo-code.
- **[[Cours/Informatique/Data mining/_index|data mining]]** : les distances euclidienne et de Manhattan demandées dans l'exercice `Maze` y servent au clustering (voir [[Distance]]).
