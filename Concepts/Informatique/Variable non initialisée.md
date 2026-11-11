---
type: concept
tags:
  - year4
aliases:
  - variable non définie
sources:
  - "[[1 - basiques|Chp1 - basiques]]"
  - "[[Raw/Year 4/C++/Chp1 - basiques.docx|Chp1 - basiques]]"
  - "[[Raw/Year 4/C++/chp4 C++.pdf|chp4 C++.pdf]]"
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : une variable non initialisée est une variable déclarée sans recevoir de valeur. En C, une variable locale (sur la [[Pile d'exécution|pile]]) contient alors ce qui restait dans sa case mémoire, laissé par un appel de fonction précédent : la « valeur aléatoire » n'est pas tirée au hasard, c'est un résidu. La norme range la lecture d'une telle variable parmi les comportements indéfinis : la valeur peut changer d'une exécution ou d'une compilation à l'autre (selon les options d'optimisation), et le compilateur peut en tirer des conclusions inattendues. Les variables globales et `static`, elles, sont initialisées à zéro automatiquement. `gcc -Wall` signale souvent l'oubli (`'y' is used uninitialized`, voir [[Erreur de compilation]]).

## Dans le cours

En C, `int y; printf("y = %d", y);` affiche selon le cours une « valeur aléatoire ». De même, les éléments d'un tableau ne sont pas initialisés à zéro.

**En C++** ([[4 - C++]]) : sans constructeur, les attributs `x` et `y` d'un objet ne sont pas initialisés et contiennent « une valeur indéterminée (n'importe quoi) ». Le [[Constructeur (programmation)|constructeur par défaut]] sert à créer chaque objet dans un état connu. Piège relevé dans [[4 - Prise de note]] : `int x = 0;` écrit dans le constructeur déclare une variable locale, et l'attribut reste non initialisé.

[[4 - Cours complet]] fait de l'initialisation systématique une [[Règle de codage|règle de codage]], « trop de programmes ont connu des bugs dus à des oublis d'initialisation », et montre qu'une variable de boucle non initialisée fausse une boucle `while`.

Notion parente : [[Langage C]]. Voir aussi : [[Tableau (programmation)]], [[Pile d'exécution]], [[Erreur de compilation]], [[Variable (programmation)]], [[Initialisation (programmation)]].

Résumés : [[1 - basiques]], [[2 - structures code]], [[4 - C++]], [[4 - Prise de note]], [[4 - Cours complet]]
