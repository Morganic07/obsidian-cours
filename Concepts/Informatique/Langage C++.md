---
type: concept
tags: [year4]
aliases: [C++, cpp, C plus plus]
sources: ["[[Raw/Year 4/C／C++/chp4 C++.pdf|chp4 C++.pdf]]", "[[Raw/Year 4/C／C++/chp4 prise de note.pdf|chp4 prise de note.pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[4 - C++]]) : le C++ est un langage de programmation **compilé** (traduit en binaire avant exécution, pour la rapidité), créé au début des années 1980 comme une **extension du [[Langage C|C]]**. Il ajoute au C la [[Programmation orientée objet|programmation orientée objet]] (classes, objets, héritage…) tout en restant proche de la machine. Usages cités : jeux vidéo (moteurs 3D, temps réel), systèmes embarqués (automobile, aéronautique, robotique), logiciels lourds et systèmes d'exploitation.

## Ce qui change par rapport au C

- **Mêmes bases** : types (`int`, `double`, `char`), opérateurs, et même syntaxe pour `if`, `for`, `while` et `switch` ([[4 - Prise de note]]). S'y ajoutent `bool` et `std::string` (voir [[Type primitif]]).
- **Entrées-sorties** par flux : `std::cout << x;` au lieu de `printf` (voir [[Flux d'entrée-sortie (C++)]], [[Fonctions printf et scanf]]), avec `#include <iostream>`.
- **Espace de noms** `std::` pour la bibliothèque standard (voir [[Espace de noms (namespace)]]).
- **Classes** : une `class` ressemble à une `struct` du C, mais regroupe données et fonctions membres, avec des droits d'accès (voir [[Classe et objet]], [[Encapsulation (programmation)]], [[Constructeur (programmation)]], [[Accesseur et mutateur]], [[Surcharge d'opérateurs]], [[Fonction amie (friend)]]).
- **Références** : `const Point& p` passe un objet sans le copier (voir [[Référence (C++)]]).

## Compilation

D'après [[4 - Prise de note]] : `g++ monprog.cpp -o monprog -Wall`, puis `./monprog`. `g++` compile aussi des fichiers `.c` (voir [[GCC]]).

```cpp
#include <iostream>

int main() {
    std::cout << "Bonjour, C++ !" << std::endl;
    return 0;
}
```

Notion parente : [[Langage C]]. Voir aussi : [[Langage Java]], [[Typage statique]].

## Dans le cours

[[4 - Cours complet]] (polycopié de TP de 2012, écrit en C++98) présente le C++ comme un [[Langage compilé|langage compilé]] et en enseigne les bases sans la programmation objet : chaîne de fabrication avec g++, types usuels (`int`, `double`, `string`, `char`, `bool`), `cin` et `cout`, `if`, `switch`, `while`, `for`, constantes, pointeurs et références (« en C++, pas en C »), fonctions et programmation modulaire. Il s'appuie sur le livre de Stroustrup ([[Principes et pratique avec C++ (livre)]]).

Résumés : [[4 - C++]], [[4 - Prise de note]], [[4 - Cours complet]]
