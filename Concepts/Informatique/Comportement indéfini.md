---
type: concept
tags: [year4]
aliases: [comportements indéfinis, comportement non défini, undefined behavior, undefined behaviour, UB, comportement défini par l'implémentation, implementation-defined behavior]
sources: ["[[Raw/Year 4/C++/Chp1 - basiques.docx|Chp1 - basiques]]", "[[Raw/Year 4/C++/chp2 - structures code .docx|chp2 - structures code]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : en [[Langage C|C]] (et en C++), un **comportement indéfini** (*undefined behavior*) est une situation pour laquelle la norme du langage n'impose aucun résultat. Le programme peut sembler fonctionner, afficher n'importe quoi, planter, ou changer de comportement selon le compilateur, la machine et les options d'optimisation. Le compilateur n'est pas tenu de le signaler, ni à la compilation ni à l'exécution, et il a le droit de supposer qu'il n'arrive jamais pour optimiser le code.

## Exemples classiques

- lire une [[Variable non initialisée|variable locale non initialisée]] ;
- accéder hors des bornes d'un [[Tableau (programmation)|tableau]] : `tab[10]` pour un tableau de 10 cases ;
- déréférencer un [[Pointeur NULL|pointeur NULL]], ou un pointeur vers une variable locale disparue (adresse renvoyée par `return &a;`) ;
- dépasser la capacité d'un `int` **signé** (débordement, par exemple `INT_MAX + 1`) ; pour un entier non signé au contraire, le calcul se fait modulo $2^n$ et le résultat est défini ;
- utiliser un format de `printf` qui ne correspond pas au type, comme afficher une adresse avec `%d` au lieu de `%p` ;
- modifier deux fois la même variable sans point de séquence entre les deux, comme `i = i++ + 1;`.

Un accès mémoire invalide se traduit souvent par une [[Erreur de segmentation]], mais pas toujours : un débordement peut aussi écraser silencieusement une autre variable, ce qui en fait une source de failles de sécurité (*buffer overflow*).

## À distinguer

- **Comportement défini par l'implémentation** : la norme laisse le choix, mais chaque compilateur doit le documenter et s'y tenir. Exemples : le signe d'un `char` sans qualificatif, la taille d'un `int`.
- **Comportement non spécifié** : plusieurs résultats sont permis, sans obligation de documenter, par exemple l'ordre d'évaluation des arguments d'une fonction.

## Parades

Compiler avec les avertissements (`gcc -Wall -Wextra`, voir [[GCC]]), initialiser toutes ses variables, vérifier les indices avant d'accéder à un tableau, tester les pointeurs avant de les déréférencer. Les options `-fsanitize=address,undefined` de GCC et Clang, ou l'outil Valgrind, détectent beaucoup de ces erreurs à l'exécution.

## Dans le cours

Le cours ne nomme pas la notion. [[1 - basiques]] montre qu'une variable non initialisée affiche une valeur « aléatoire », et [[2 - structures code]] que le C ne vérifie pas les indices des tableaux ; leurs compléments rattachent ces deux cas au comportement indéfini.

Voir aussi : [[Variable non initialisée]], [[Tableau (programmation)]], [[Erreur de segmentation]], [[Pointeur NULL]], [[Pointeur et adresse mémoire]], [[Pile d'exécution]], [[Fonctions printf et scanf]], [[Langage C]], [[GCC]].

Résumés : [[1 - basiques]], [[2 - structures code]]
