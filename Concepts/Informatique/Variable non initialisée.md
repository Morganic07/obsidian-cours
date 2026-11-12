---
type: concept
tags:
  - year4
aliases:
  - variable non définie
sources:
  - "[[1 - basiques|Chp1 - basiques]]"
  - "[[Raw/Year 4/C／C++/Chp1 - basiques.docx|Chp1 - basiques]]"
  - "[[Raw/Year 4/C／C++/chp4 C++.pdf|chp4 C++.pdf]]"
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : une variable non initialisée est une variable déclarée sans recevoir de valeur. En C, une variable locale (sur la [[Pile d'exécution|pile]]) contient alors ce qui restait dans sa case mémoire, laissé par un appel de fonction précédent : la « valeur aléatoire » n'est pas tirée au hasard, c'est un résidu. La norme range la lecture d'une telle variable parmi les comportements indéfinis : la valeur peut changer d'une exécution ou d'une compilation à l'autre (selon les options d'optimisation), et le compilateur peut en tirer des conclusions inattendues. Les variables globales et `static`, elles, sont initialisées à zéro automatiquement. `gcc -Wall` signale souvent l'oubli (`'y' is used uninitialized`) : c'est un [[Avertissement de compilation|avertissement]], pas une [[Erreur de compilation|erreur]], et le programme compile quand même.

## Dans le cours

En C, `int y; printf("y = %d", y);` affiche selon le cours une « valeur aléatoire ». De même, les éléments d'un tableau ne sont pas initialisés à zéro.

**En C++** ([[4 - C++]]) : sans constructeur, les attributs `x` et `y` d'un objet ne sont pas initialisés et contiennent « une valeur indéterminée (n'importe quoi) ». Le [[Constructeur (programmation)|constructeur par défaut]] sert à créer chaque objet dans un état connu. Piège relevé dans [[4 - Prise de note]] : `int x = 0;` écrit dans le constructeur déclare une variable locale, et l'attribut reste non initialisé.

[[4 - Cours complet]] fait de l'initialisation systématique une [[Règle de codage|règle de codage]], « trop de programmes ont connu des bugs dus à des oublis d'initialisation », et montre qu'une variable de boucle non initialisée fausse une boucle `while`.

- [[tp2]] : si `scanf` échoue, `nb1` garde sa valeur indéterminée ; tester la valeur de retour de `scanf` l'évite ([[Validation des entrées]]).
- [[tp3]] : en 3.3, `a`, `b` et `c` étaient comparés avant toute saisie (corrigé par un `scanf`).
- [[tp4]] : si la saisie n'est pas un nombre, `algo` reste non initialisée.
- [[tp5]] : `guess` testé dans le `while` avant la première saisie (5.3), signalé par `gcc -Wall -O2` ; corrigé en `int guess = 0;`.
- [[tp7]] : `indice_min` et `indice_max` jamais affectés quand l'extremum est en case 0 (7.2) ; initialisés à 0.
- [[td listes chaînées]] : `Chainon *premier;` a une valeur indéterminée tant que `creerListe` ne l'a pas mis à `NULL`.
- [[formation C++]] : `Television` sans constructeur laisse `volume` et `canal` non initialisés.

Notion parente : [[Langage C]]. Voir aussi : [[Tableau (programmation)]], [[Pile d'exécution]], [[Erreur de compilation]], [[Variable (programmation)]], [[Initialisation (programmation)]].

Résumés : [[1 - basiques]], [[2 - structures code]], [[4 - C++]], [[4 - Prise de note]], [[4 - Cours complet]]
