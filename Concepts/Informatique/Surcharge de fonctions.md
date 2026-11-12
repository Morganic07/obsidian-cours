---
type: concept
tags: [year4]
aliases: [function overloading, surcharge de fonction, surcharge de méthodes, surcharge de constructeur, résolution de surcharge]
sources: ["[[Raw/Year 4/C／C++/programmes C++/formation/6-constructeurParametre.cpp|6-constructeurParametre.cpp]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : en [[Langage C++|C++]], plusieurs fonctions d'une même portée peuvent porter le même nom si leurs listes de paramètres diffèrent, par le **nombre** ou par le **type** des paramètres. On parle de surcharge (*overloading*). À chaque [[Appel de fonction|appel]], le compilateur choisit la version dont les paramètres correspondent le mieux aux arguments : c'est la **résolution de surcharge**, faite à la compilation.

```cpp
int    aire(int cote)               { return cote * cote; }
int    aire(int l, int L)           { return l * L; }
double aire(double rayon)           { return 3.14159 * rayon * rayon; }

aire(3);        // version 1 : 9
aire(3, 4);     // version 2 : 12
aire(2.0);      // version 3 : 12.566…
```

Règles :

- le **type de retour seul** ne suffit pas à distinguer deux surcharges : `int f(int)` et `double f(int)` sont refusés ;
- les conversions comptent : une correspondance exacte l'emporte sur une promotion (`char` vers `int`), elle-même préférée à une conversion (`int` vers `double`) ; si deux versions conviennent aussi bien, l'appel est **ambigu** et ne compile pas (`f(1)` avec `f(long)` et `f(double)`) ;
- les méthodes se surchargent de la même façon, y compris les [[Constructeur (programmation)|constructeurs]] : par défaut, par paramètres, par copie. Une [[Méthode constante|méthode constante]] et sa version non constante sont aussi deux surcharges ;
- les paramètres par défaut (`Point(int x = 0, int y = 0)`) remplacent souvent plusieurs surcharges.

Pour distinguer les versions à l'[[Édition de liens|édition de liens]], le compilateur encode les types des paramètres dans le nom du [[Symbole (édition de liens)|symbole]] (*name mangling*) : `aire(int)` devient par exemple `_Z4airei` avec [[GCC]]. Le [[Langage C|C]] ne permet pas la surcharge : deux fonctions ne peuvent pas y porter le même nom, d'où des familles comme `abs`, `labs`, `fabs`. La [[Surcharge d'opérateurs|surcharge d'opérateurs]] applique le même mécanisme aux opérateurs. [[Langage Java|Java]] admet aussi la surcharge ; [[Langage Python|Python]] non, une seconde définition remplaçant la première.

## Dans le cours

- [[formation C++]] : la classe `Point` a deux constructeurs, `Point()` et `Point(int, int)` (programme 6), surcharge de constructeur qui permet de créer un point avec ou sans coordonnées.

Voir aussi : [[Surcharge d'opérateurs]], [[Constructeur (programmation)]], [[Typage statique]].
