---
type: concept
tags: [year4]
aliases: [en-tête (C++), header, header file, fichier .h, fichier .hpp]
matieres: [C／C++]
sources: ["[[Raw/Year 4/C／C++/chp4 C++.pdf|chp4 C++.pdf]]", "[[Raw/Year 4/C／C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : un fichier d'en-tête (*header*, extension `.h`, ou `.hpp` en C++) contient des **déclarations** (classes, prototypes de fonctions, constantes) destinées à être partagées entre plusieurs fichiers source.

- **Inclusion** : la directive du préprocesseur `#include` recopie le contenu du fichier à la place de la directive, avant la compilation proprement dite.
  - chevrons pour un en-tête de la bibliothèque standard : `#include <iostream>` (sans extension en C++) ;
  - guillemets pour un fichier du projet : `#include "point.h"`.
- **Organisation usuelle d'une classe** : la définition de la classe dans `point.h`, les définitions des méthodes dans `point.cpp`, l'utilisation dans `main.cpp`.

```cpp
// point.h
#pragma once
class Point {
    int x, y;
public:
    Point(int a, int b);
    void affiche() const;
};

// point.cpp
#include <iostream>
#include "point.h"
Point::Point(int a, int b) : x(a), y(b) {}
void Point::affiche() const { std::cout << x << ", " << y << std::endl; }

// main.cpp
#include "point.h"
int main() { Point p(3, 4); p.affiche(); }
```

On compile ensuite tous les fichiers source ensemble : `g++ main.cpp point.cpp -o prog`. Les en-têtes ne se donnent pas au compilateur : ils sont inclus.

- **Double inclusion** : si un en-tête est inclus deux fois dans le même fichier (directement ou par un autre en-tête), la classe serait définie deux fois, ce qui est une erreur. On le protège par `#pragma once` en première ligne, ou par une garde d'inclusion :

```cpp
#ifndef POINT_H
#define POINT_H
// ... contenu ...
#endif
```

- On évite d'écrire `using namespace std;` dans un en-tête : tout fichier qui l'inclut en hériterait (voir [[Espace de noms (namespace)]]).

## Dans le cours

- [[4 - C++]] utilise `#include <iostream>` et définit les méthodes hors de la classe avec `Point::`, sans séparer le code en plusieurs fichiers. La notion apparaît dans ses compléments.
- [[5 - Compilation séparée]] la définit : le fichier d'en-tête `.h` « déclare ce qui existe (classes, attributs, prototypes des méthodes). C'est l'interface, ce que les autres fichiers ont besoin de connaître » ; le [[Fichier source|fichier source]] `.cpp` en définit le code. Exemple : `Point.h` et `Segment.h`, protégés par une [[Garde d'inclusion|garde d'inclusion]], inclus par la [[Directive include|directive `#include`]].
- [[tp2]] : `#include <stdio.h>` insère l'en-tête qui déclare `printf` dans le premier programme (« Hello world »).
- [[formation C++]] : `std::string` est déclaré dans `<string>`, que `<iostream>` n'inclut pas forcément selon la norme ; et `using namespace std;` est à éviter dans un en-tête.
- [[exo-prof]] : une méthode définie dans le corps de la classe est implicitement `inline`, donc plaçable dans un en-tête inclus par plusieurs fichiers.
- [[compilation séparée (C++)]] : `Point.h` et `Segment.h` ne contiennent que les déclarations des classes ; les définitions des méthodes sont dans `Point.cpp` et `Segment.cpp`.

Voir aussi : [[Classe et objet]], [[Programmation modulaire]], [[Compilation séparée]], [[Déclaration et définition]], [[Interface et implémentation]], [[Préprocesseur]], [[Langage C++]], [[Erreur de compilation]].

- [[4 - Cours complet]] le présente comme le fichier inclus par `#include`, d'extension `.h`, qui contient les déclarations donnant accès au code d'une bibliothèque ; il note que le débutant confond bibliothèque et fichier d'en-tête, et que les en-têtes standard du C++ n'ont pas d'extension. Son exercice 4 déclare `somme1aN()` dans `somme.h`.

Résumés : [[4 - C++]], [[5 - Compilation séparée]], [[4 - Cours complet]]
