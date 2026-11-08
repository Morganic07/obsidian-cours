---
type: concept
tags: [year4]
aliases: [en-tête (C++), header, header file, fichier .h, fichier .hpp, "#include", include guard, "#pragma once"]
matieres: [C++]
sources: ["[[Raw/Year 4/C++/chp4 C++.pdf|chp4 C++.pdf]]"]
maj: 2026-11-08
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

Le cours ne le nomme pas : [[4 - C++]] utilise `#include <iostream>` et définit les méthodes hors de la classe avec `Point::`, sans séparer le code en plusieurs fichiers. La notion apparaît dans les compléments de [[4 - C++]].

Voir aussi : [[Classe et objet]], [[Programmation modulaire]], [[Langage C++]], [[Erreur de compilation]].

Résumés : [[4 - C++]]
