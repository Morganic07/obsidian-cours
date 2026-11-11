---
type: concept
tags: [year4]
aliases: [linker, éditeur de liens, linking, link, ld, undefined reference]
sources: ["[[Raw/Year 4/C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[5 - Compilation séparée]]) : l'édition de liens assemble les [[Fichier objet|fichiers objets]] `.o` en un [[Exécutable|exécutable]] : `g++ Point.o Segment.o main.o -o programme`.

## Compléments (hors du cours)

- C'est la dernière étape de la [[Chaîne de compilation|chaîne de compilation]]. Sous [[Linux]], `g++` y appelle l'éditeur de liens `ld`. Il relie chaque appel à une fonction définie dans un autre fichier objet au code de cette fonction (résolution des [[Symbole (édition de liens)|symboles]]), et ajoute la [[Bibliothèque standard du C++|bibliothèque standard]].
- Erreurs typiques :
  - `undefined reference to 'Point::Point(int, int)'` : une fonction déclarée n'est définie dans aucun fichier objet (`.o` oublié dans la commande, méthode jamais écrite, faute de frappe) ;
  - `multiple definition of …` : une fonction définie deux fois, souvent parce qu'elle est écrite dans un `.h` inclus par plusieurs `.cpp` ([[Règle de la définition unique]]).
  Les deux finissent par `ld returned 1 exit status`. Ce ne sont pas des [[Erreur de compilation|erreurs de compilation]] : chaque fichier, pris seul, était correct.
- Liaison **statique** (le code d'une [[Bibliothèque statique|bibliothèque statique]] est copié dans l'exécutable) ou **dynamique** (une [[Bibliothèque partagée|bibliothèque partagée]] est chargée au lancement ; option `-l` : `-lm` pour la bibliothèque mathématique du C).

Voir aussi : [[Compilation séparée]], [[GCC]].

## Dans [[4 - Cours complet]]

L'éditeur de liens (*linker*, `ld`, appelé par gcc/g++) lie les parties distinctes (le code écrit et la bibliothèque standard) en un exécutable, en résolvant les références aux symboles. Les erreurs de liaison sont plus difficiles à corriger que les erreurs de compilation, plus faciles que les erreurs d'exécution.

Résumés : [[5 - Compilation séparée]], [[4 - Cours complet]]
