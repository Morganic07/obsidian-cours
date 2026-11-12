---
type: concept
tags: [year4]
aliases: [étapes de la compilation, compilation toolchain]
sources: ["[[Raw/Year 4/C／C++/Chp1 - basiques.docx|Chp1 - basiques]]", "[[Raw/Year 4/C／C++/chp4 prise de note.pdf|chp4 prise de note.pdf]]", "[[Raw/Year 4/C／C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : la chaîne de compilation est la suite d'étapes qui transforme un fichier source C ou C++ en exécutable. `gcc` (ou `g++` pour le C++, voir [[GCC]]) les enchaîne toutes en une seule commande, mais chacune peut être lancée seule.

| Étape | Rôle | Option | Produit | Erreur typique |
|---|---|---|---|---|
| 1. Préprocesseur | traite les directives `#` : `#include` recopie le fichier d'en-tête, `#define` remplace les macros ; retire les commentaires | `gcc -E` | source « pur » (`.i`) | `fatal error: x.h: Aucun fichier ou dossier de ce type` |
| 2. Compilation | vérifie la syntaxe et les types, traduit en assembleur | `gcc -S` | `.s` | `expected ';'`, `'x' undeclared` |
| 3. Assemblage | traduit l'assembleur en code machine | `gcc -c` | fichier objet `.o` | rare |
| 4. Édition de liens (*linker*, programme `ld`) | réunit les fichiers objets et les bibliothèques (bibliothèque standard du C ou du C++, `-lm` pour `math.h`) en un exécutable | (par défaut) | exécutable (`a.out` sans `-o`) | `undefined reference to 'f'` puis `ld returned 1 exit status` |

L'erreur d'édition de liens survient quand une fonction est déclarée (son prototype est connu, la compilation passe) mais jamais définie, ou que son nom est mal orthographié : `ld` ne trouve son code dans aucun fichier objet ni aucune bibliothèque.

Commande usuelle : `gcc -Wall -Wextra prog.c -o prog`. Pour un programme en plusieurs fichiers ([[Programmation modulaire]]), on compile chaque fichier séparément puis on lie :

```bash
g++ -c point.cpp          # produit point.o
g++ -c main.cpp           # produit main.o
g++ main.o point.o -o prog
```

Seul le fichier modifié est alors à recompiler. Les bibliothèques peuvent être liées statiquement (leur code est copié dans l'exécutable) ou dynamiquement ([[Bibliothèque partagée]], chargée à l'exécution).

Le cas de Java est différent : `javac` produit du bytecode exécuté par une machine virtuelle, sans édition de liens préalable (voir [[Compilation et bytecode]]).

## Dans le cours

[[1 - basiques]] donne une table de messages d'[[Erreur de compilation|erreurs de compilation]] qui viennent en fait d'étapes différentes ; [[4 - Prise de note]] compile avec `g++ monprog.cpp -o monprog -Wall`. Les étapes y sont détaillées dans les compléments.

[[5 - Compilation séparée]] en nomme trois : le [[Préprocesseur|préprocesseur]], qui remplace chaque `#include` par le contenu du fichier « avant la compilation » ; la compilation de chaque `.cpp` en [[Fichier objet|fichier objet]] `.o` (`g++ -c`) ; l'[[Édition de liens|édition de liens]], qui assemble les `.o` en [[Exécutable|exécutable]].

Voir aussi : [[GCC]], [[Compilation séparée]], [[Option de compilation]], [[Make (logiciel)]], [[Erreur de compilation]], [[Programmation modulaire]], [[Bibliothèque partagée]], [[Compilation et bytecode]], [[Langage C]], [[Langage C++]].

[[4 - Cours complet]] décrit la fabrication en deux commandes : `g++ -Wall -c helloWorld.cpp` (préprocesseur, compilation et assemblage vers `helloWorld.o`), puis `g++ -Wall -o helloWorld helloWorld.o` (édition des liens), avec un schéma source → compilateur → code objet → éditeur de liens → exécutable.

Résumés : [[1 - basiques]], [[4 - Prise de note]], [[5 - Compilation séparée]], [[4 - Cours complet]]
