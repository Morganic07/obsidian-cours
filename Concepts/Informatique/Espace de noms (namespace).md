---
type: concept
tags: [year4]
aliases: [namespace, espace de noms, "std::"]
sources: ["[[Raw/Year 4/C／C++/chp4 C++.pdf|chp4 C++.pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[4 - C++]]) : en C++, `std::` est le namespace (espace de noms) de la bibliothèque standard (*Standard Library*). `std::cout`, `std::endl` et `std::string` en font partie.

**Complément, hors du cours** : un espace de noms regroupe des noms (fonctions, classes, variables) sous un préfixe, pour éviter les conflits entre bibliothèques. On y accède par l'opérateur `::`, le même qui rattache une méthode à sa classe (`Point::affiche`, voir [[Classe et objet]]). La directive `using namespace std;` permet d'écrire `cout` sans préfixe, comme le fait l'aide `ifstream f(...)` de l'exercice `Maze`.

Notion parente : [[Langage C++]]. Voir aussi : [[Flux d'entrée-sortie (C++)]].

## Dans le cours

[[4 - Cours complet]] explique `using namespace std;` : `cout` et `cin` existent dans l'espace de noms `std` mais pourraient exister ailleurs ; leur nom complet est `std::cout`, l'opérateur `::` réalisant la résolution de portée « un peu comme le `/` dans un chemin ». La directive évite d'écrire le nom complet ; la fiche ajoute qu'elle est à proscrire dans un en-tête.

Résumés : [[4 - C++]], [[4 - Cours complet]]
