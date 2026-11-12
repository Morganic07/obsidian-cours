---
type: source
tags: [year4]
sources:
  - "[[Raw/Year 4/C／C++/programmes C++/compilation separée/Makefile|Makefile]]"
  - "[[Raw/Year 4/C／C++/programmes C++/compilation separée/main.cpp|main.cpp]]"
  - "[[Raw/Year 4/C／C++/programmes C++/compilation separée/Point.h|Point.h]]"
  - "[[Raw/Year 4/C／C++/programmes C++/compilation separée/Point.cpp|Point.cpp]]"
  - "[[Raw/Year 4/C／C++/programmes C++/compilation separée/Segment.h|Segment.h]]"
  - "[[Raw/Year 4/C／C++/programmes C++/compilation separée/Segment.cpp|Segment.cpp]]"
maj: 2026-11-12
complet: true
enrichi: 2026-11-12
---

Programme du dossier `compilation separée` (six fichiers), dans [[Cours/Informatique/C++/_index|C++]] : les classes `Point` et `Segment` de [[exo-prof]], réparties en plusieurs fichiers et compilées par un [[Make (logiciel)|Makefile]], comme le demande [[5 - Compilation séparée]]. Chaque [[Classe et objet|classe]] [[Langage C++|C++]] a son [[Fichier d'en-tête|fichier d'en-tête]] `.h`, qui la déclare, et son [[Fichier source|fichier source]] `.cpp`, qui définit ses méthodes ; `main.cpp` contient le programme principal. Chaque `.cpp` est [[Compilation séparée|compilé séparément]] en [[Fichier objet|fichier objet]] `.o`, puis l'[[Édition de liens|édition de liens]] assemble les trois `.o` en un [[Exécutable|exécutable]]. C'est la [[Programmation modulaire|programmation modulaire]] du chapitre 5 appliquée à l'exercice du chapitre 4 ([[4 - C++]]).

Organisation du dossier :

```text
compilation separée/
├── Makefile      règles de compilation
├── main.cpp      programme principal
├── Point.h       déclaration de la classe Point
├── Point.cpp     définition de ses méthodes
├── Segment.h     déclaration de la classe Segment
└── Segment.cpp   définition de ses méthodes
```

## Point.h

D'après le code, ce fichier déclare la classe `Point` : deux coordonnées entières privées ([[Encapsulation (programmation)|encapsulation]]), trois constructeurs, `set`, `getX`, `getY` et `afficherPoint`.

```cpp
#ifndef POINT_H // ou #pragma once
#define POINT_H

class Point{
    private :
        int x, y;

    public :
        Point();
        Point(int a , int b);
        Point(const Point& autrePoint);

        void set(int x, int y);
        int getX();
        int getY();

        void afficherPoint();
};

#endif
```

**Explications.**

- **Un en-tête ne fait que déclarer.** On y déclare tout (attributs, constructeurs, méthodes) sans décrire le détail des fonctions : ce sont des prototypes, terminés par `;`. Le détail, c'est-à-dire la [[Déclaration et définition|définition]] des méthodes, se fera dans `Point.cpp`. L'en-tête est l'**interface** de la classe, ce que les autres fichiers ont besoin de connaître ; le `.cpp` est son **implémentation** ([[Interface et implémentation|interface et implémentation]]).
- **`#ifndef POINT_H` / `#define POINT_H` / `#endif`** forment une [[Garde d'inclusion|garde d'inclusion]] : à la première inclusion, la [[Macro (préprocesseur)|macro]] `POINT_H` n'est pas définie, le [[Préprocesseur|préprocesseur]] garde le contenu et définit `POINT_H` ; à une inclusion suivante dans le même fichier compilé, `POINT_H` est définie et tout le contenu est sauté ([[Compilation conditionnelle|compilation conditionnelle]]). Le commentaire le rappelle : `#pragma once`, en une ligne, a le même effet.
- La garde est indispensable ici : `main.cpp` inclut `Point.h` puis `Segment.h`, qui inclut à nouveau `Point.h`. Sans garde, la classe `Point` serait définie deux fois dans la même [[Unité de compilation|unité de compilation]], et le compilateur refuserait (`error: redefinition of 'class Point'`), conformément à la [[Règle de la définition unique|règle de la définition unique]]. [[Complément hors du cours|ⓘ]]

Dans un prototype, le nom des paramètres est facultatif et ne lie pas la définition : `Point.h` déclare `set(int x, int y)` et `Point.cpp` la définit avec `set(int a, int b)`, ce qui est permis. Le choix de `a` et `b` dans la définition est d'ailleurs le bon : avec des paramètres nommés `x` et `y`, ils masqueraient les attributs ([[Portée d'une variable|portée]]) et `x = x;` ne modifierait rien ; il faudrait écrire `this->x = x;`. [[Complément hors du cours|ⓘ]]

`getX()` et `getY()` ne modifient pas l'objet et gagneraient à être déclarés [[Méthode constante|constants]] (`int getX() const;`, et de même dans la définition), comme dans `classeSegment.cpp`. [[Complément hors du cours|ⓘ]]

## Point.cpp

D'après le code, ce fichier définit les constructeurs et les méthodes déclarés dans `Point.h`.

```cpp
#include <iostream>
#include "Point.h"

// les 3 constructeurs
Point::Point(){
    x = 0;
    y = 0;
}
Point::Point(int a, int b){
    x = a;
    y = b;
}
Point::Point(const Point& autrePoint){
    x = autrePoint.x;
    y = autrePoint.y;
}

// les méthodes get, set, affiche
int Point::getX(){return x;}

int Point::getY(){return y;}

void Point::set(int a, int b){
    x = a;
    y = b;
}

void Point::afficherPoint(){
    std::cout << x << ";" << y << std::endl;
}
```

**Explications.**

- **`#include "Point.h"`** : on inclut l'en-tête de la classe, entre guillemets `""` parce que c'est un fichier du projet ; les en-têtes de la [[Bibliothèque standard du C++|bibliothèque standard]] s'incluent entre chevrons, `#include <iostream>` ([[Directive include|directive `#include`]]).
- **On y définit toutes les fonctions** déclarées dans l'en-tête, chacune sous son nom complet `Point::…`, avec l'[[Opérateur de résolution de portée|opérateur de résolution de portée]] `::` qui la rattache à la classe.
- Les trois [[Constructeur (programmation)|constructeurs]] (par défaut, par paramètres, par copie) et les [[Accesseur et mutateur|accesseurs et le mutateur]] sont ceux de [[exo-prof]] ; `afficherPoint` écrit `x;y` sur le [[Flux d'entrée-sortie (C++)|flux]] `std::cout`.

Avec `#include "…"`, le préprocesseur cherche d'abord dans le dossier du fichier qui inclut, puis dans les dossiers système ; avec `<…>`, seulement dans les dossiers système et ceux donnés par l'[[Option de compilation|option]] `-I`. Sous Linux, le nom est [[Sensibilité à la casse|sensible à la casse]] : `#include "point.h"` ne trouverait pas `Point.h`. [[Complément hors du cours|ⓘ]]

Un `.cpp` inclut toujours son propre en-tête, en premier de préférence : le compilateur vérifie ainsi que les définitions correspondent aux déclarations, et que l'en-tête se suffit à lui-même (il inclut tout ce dont il a besoin). [[Complément hors du cours|ⓘ]]

## Segment.h

D'après le code, ce fichier déclare la classe `Segment` : deux `Point` `A` et `B`, une longueur, trois constructeurs, deux accesseurs, `getLongueur` et `afficherSegment`.

```cpp
#pragma once
#include "Point.h"

class Segment{
    private :
        Point A;
        Point B;
        float longueur;

    public :
        Segment();
        Segment(Point p1, Point p2);
        Segment(const Segment& autreSegment);

        Point getA();
        Point getB();
        float getLongueur();
        void afficherSegment();
};
```

**Explications.**

- **`#pragma once`** remplace ici la garde `#ifndef … #define … #endif` : les deux marchent, comme le note le commentaire du fichier. `#pragma once` est plus court et évite le risque de deux gardes de même nom, mais ce n'est pas une directive de la [[Norme du C++|norme]] ; [[GCC]], [[Clang]] et MSVC la reconnaissent tous. [[Complément hors du cours|ⓘ]]
- **`#include "Point.h"`** : un `Segment` contient deux `Point` ([[Composition (programmation)|composition]]) ; pour connaître la taille et les constructeurs de `Point`, le compilateur a besoin de sa déclaration complète, d'où l'inclusion dans l'en-tête même.

Quand une classe ne fait que **mentionner** une autre par pointeur ou référence (`Point*`, `const Point&` en paramètre), une déclaration anticipée `class Point;` suffit dans l'en-tête, sans `#include` : moins d'inclusions, donc moins de recompilations quand `Point.h` change. Elle ne suffit pas ici, puisque `Segment` contient des `Point` par valeur. [[Complément hors du cours|ⓘ]]

## Segment.cpp

D'après le code, ce fichier définit les constructeurs et les méthodes de `Segment`.

```cpp
#include <iostream>
#include <cmath>
#include "Segment.h"

Segment::Segment(){
    A.set(0,0);
    B.set(0,0);
    longueur = 0;
}

Segment::Segment(Point p1, Point p2){
    A = p1;
    B = p2;
    longueur = getLongueur();
}

Segment::Segment(const Segment& autreSegment){
    A = autreSegment.A;
    B = autreSegment.B;
    longueur = autreSegment.longueur;
}

Point Segment::getA(){
    return A;
}

Point Segment::getB(){
    return B;
}

float Segment::getLongueur(){
    longueur = std::sqrt((B.getX()-A.getX())*(B.getX()-A.getX())+(B.getY()-A.getY())*(B.getY()-A.getY()));
    return longueur;
}

void Segment::afficherSegment(){
    A.afficherPoint();
    B.afficherPoint();
    std::cout << "longueur : " << getLongueur() << std::endl;
}
```

**Explications.**

- `Segment.cpp` n'inclut que `Segment.h`, qui inclut lui-même `Point.h` : il connaît donc les deux classes. Il inclut `<cmath>` pour `std::sqrt` ([[Bibliothèque cmath|`<cmath>`]], [[Racine carrée|racine carrée]]) et `<iostream>` pour `std::cout`.
- **`getLongueur`** calcule la [[Distance|distance euclidienne]] $\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$ ([[Théorème de Pythagore|théorème de Pythagore]]), la range dans l'attribut `longueur` et la renvoie. Pour $(2, 3)$ et $(0, 1)$ : $\sqrt{4 + 4} = \sqrt 8 \approx 2{,}82843$.
- **Constructeur par paramètres** : `A = p1;` affecte une copie du point reçu ; la longueur est calculée aussitôt.
- **Constructeur par défaut** : `A` et `B` ont déjà été construits à (0, 0) par le constructeur par défaut de `Point` avant le corps du constructeur ; `A.set(0,0)` ne change rien, sans conséquence.

Différences avec `classeSegment.cpp` ([[exo-prof]]) : le constructeur par paramètres affecte directement `A = p1;` au lieu de recopier les coordonnées par `set` ; la longueur se calcule dans `getLongueur` et non dans une méthode `calculerLongueur` ; l'affichage écrit `x;y` et « longueur : ». Avec `-Wall -Wextra`, `A = p1;` et les affectations du constructeur par copie déclenchent le même [[Avertissement de compilation|avertissement]] `-Wdeprecated-copy` (opérateur d'affectation implicite d'une classe dont le constructeur par copie est écrit à la main) ; le remède est le même : supprimer le constructeur par copie de `Point`, ou initialiser par la [[Liste d'initialisation|liste d'initialisation]] `Segment::Segment(Point p1, Point p2) : A(p1), B(p2) { … }`. [[Complément hors du cours|ⓘ]]

`getLongueur()` modifie l'attribut `longueur` à chaque lecture ([[Effet de bord|effet de bord]] d'un accesseur), et l'attribut n'est jamais lu ailleurs que dans le constructeur par copie : il pourrait disparaître, la méthode calculant la longueur à la demande, déclarée `float getLongueur() const`. [[Complément hors du cours|ⓘ]]

## main.cpp

D'après le code, le programme principal crée un segment par défaut puis le segment de $(2, 3)$ à $(0, 1)$, et les affiche.

```cpp
#include <iostream>
#include "Point.h"
#include "Segment.h"

int main(){
    std::cout << "s1 : "<< std::endl;
    Segment s1;
    s1.afficherSegment();

    std::cout << "s2 : "<< std::endl;

    Point p1(2,3);
    Point p2(0,1);

    Segment s2(p1, p2);
    s2.afficherSegment();

    return 0;
}
```

Sortie de `./programmeEntier` :

```text
s1 : 
0;0
0;0
longueur : 0
s2 : 
2;3
0;1
longueur : 2.82843
```

**Explications.**

- `main.cpp` inclut `Point.h` et `Segment.h` : il n'a besoin que des **déclarations** pour compiler les appels (`Segment s1;`, `s2.afficherSegment()`), sans voir le code des méthodes, qui ne le rejoindra qu'à l'édition de liens. Dans `main.o`, les appels à `Segment::afficherSegment` restent des [[Symbole (édition de liens)|symboles]] non résolus, que l'éditeur de liens trouve dans `Segment.o` ; si un `.o` manque à la commande, il échoue avec `undefined reference to …`. [[Complément hors du cours|ⓘ]]
- `Point.h` est inclus deux fois (directement, puis par `Segment.h`) : la garde d'inclusion en écarte la seconde copie.

Seule la [[Fonction main (C et C++)|fonction `main`]] n'appartient à aucune classe ; dans un projet, elle est seule dans son fichier, et l'on peut écrire d'autres `main` de test qui réutilisent `Point.o` et `Segment.o` sans les recompiler. [[Complément hors du cours|ⓘ]]

## Makefile

D'après le code, le Makefile décrit comment fabriquer l'exécutable `programmeEntier` à partir des trois `.cpp`.

```makefile
CXX      = g++

OBJETS = main.o Point.o Segment.o

# Édition de liens : assemble les .o en exécutable
programmeEntier: $(OBJETS)
	$(CXX) $(OBJETS) -o $@

# Chaque .o dépend de son .cpp et des .h qu'il inclut
main.o: main.cpp Point.h Segment.h
	$(CXX) -c main.cpp

Point.o: Point.cpp Point.h
	$(CXX) -c Point.cpp

Segment.o: Segment.cpp Segment.h Point.h
	$(CXX) -c Segment.cpp

clean:
	rm -f $(OBJETS) programmeEntier
```

**Explications** (les commentaires du fichier, remis au propre).

- **Variables** : `CXX = g++` nomme le [[Compilateur|compilateur]] C++ de [[GCC]], `OBJETS` la liste des fichiers objets ; `$(CXX)` et `$(OBJETS)` sont remplacés par leur valeur.
- **Structure d'une règle** : `cible: dépendances`, puis, à la ligne suivante, la commande, qui commence obligatoirement par une [[Caractère de tabulation|tabulation]]. Dans la première règle, `programmeEntier` est la cible et les dépendances sont les `OBJETS`, ici `main.o`, `Point.o` et `Segment.o`.
- **La commande d'édition de liens** `$(CXX) $(OBJETS) -o $@` se traduit, sans les variables, par `g++ main.o Point.o Segment.o -o programmeEntier` : elle assemble les `.o` en exécutable.
- **`$@` est une variable automatique** : elle vaut la cible de la règle, ici `programmeEntier`. Si l'on change le nom de la cible, on n'a pas à réécrire la commande, puisque le nom n'y est pas codé en dur.
- **Chaque `.o` dépend de son `.cpp` et des `.h` qu'il inclut** : `g++ -c main.cpp` compile sans lier (option `-c`) et produit `main.o`. `Segment.o` dépend aussi de `Point.h`, puisque `Segment.h` l'inclut.
- **`clean`** efface les `.o` et l'exécutable ([[Commande rm|`rm -f`]] : sans erreur si un fichier manque).

Exécution de `make` dans le dossier (vérifiée ; la première règle du fichier est la cible par défaut) : [[Complément hors du cours|ⓘ]]

```text
g++ -c main.cpp
g++ -c Point.cpp
g++ -c Segment.cpp
g++ main.o Point.o Segment.o -o programmeEntier
```

`make` automatise ainsi la [[Chaîne de compilation|chaîne de compilation]] ([[Préprocesseur|préprocesseur]], compilation, édition de liens), lancée depuis l'[[Interface en ligne de commande|interface en ligne de commande]]. Il compare les dates de modification : une cible n'est refaite que si l'une de ses dépendances est plus récente qu'elle. C'est la [[Compilation incrémentale|compilation incrémentale]]. Vérifié avec la [[Commande touch|commande `touch`]], qui met à jour la date d'un fichier : un second `make` répond `'programmeEntier' is up to date` ; après `touch Segment.cpp`, seuls `Segment.o` et l'édition de liens sont refaits ; après `touch Point.h`, les trois `.o`, puisque les trois en dépendent. Les dépendances forment un [[Graphe orienté|graphe orienté]] sans cycle, que `make` parcourt dans l'ordre d'un [[Tri topologique|tri topologique]]. [[Complément hors du cours|ⓘ]]

Les dépendances aux `.h` écrites à la main sont le point fragile : un `#include` ajouté sans mise à jour du Makefile, et une modification de l'en-tête ne déclenche plus la recompilation, d'où des `.o` incohérents. `g++ -MMD` produit ces dépendances automatiquement (fichiers `.d` que le Makefile inclut par `-include $(OBJETS:.o=.d)`). [[Complément hors du cours|ⓘ]]

Améliorations usuelles de ce Makefile : [[Complément hors du cours|ⓘ]]

```makefile
CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g
OBJETS   = main.o Point.o Segment.o

programmeEntier: $(OBJETS)
	$(CXX) $(OBJETS) -o $@

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

main.o: Point.h Segment.h
Point.o: Point.h
Segment.o: Segment.h Point.h

.PHONY: clean
clean:
	rm -f $(OBJETS) programmeEntier
```

- `CXXFLAGS` regroupe les [[Option de compilation|options de compilation]] : version de la norme, avertissements, informations pour le [[Débogueur|débogueur]] (`-g`) ; le Makefile d'origine n'en passe aucune, si bien que les avertissements `-Wdeprecated-copy` n'apparaissent pas. [[Complément hors du cours|ⓘ]]
- La **règle générique** `%.o: %.cpp` remplace les trois commandes identiques ; `$<` est la variable automatique qui vaut la première dépendance (le `.cpp`). Les lignes sans commande ajoutent seulement les dépendances aux en-têtes. [[Complément hors du cours|ⓘ]]
- `.PHONY: clean` déclare que `clean` n'est pas un fichier : sans cette ligne, s'il existe un fichier nommé `clean` dans le dossier, `make clean` répond `'clean' is up to date` et n'efface rien (vérifié). [[Complément hors du cours|ⓘ]]

Au-delà de quelques fichiers, on génère le Makefile plutôt que de l'écrire : [[CMake]] décrit le projet (`add_executable(programmeEntier main.cpp Point.cpp Segment.cpp)`) et produit un Makefile ou un fichier pour [[Ninja (logiciel)|Ninja]], en calculant lui-même les dépendances aux en-têtes. [[Complément hors du cours|ⓘ]]

## À retenir

- Un `.h` **déclare** (classe, prototypes), un `.cpp` **définit** ; chaque `.cpp` inclut son propre `.h`.
- Tout en-tête est protégé par une garde d'inclusion, `#ifndef NOM_H / #define NOM_H / #endif` ou `#pragma once` ; sans elle, un en-tête inclus deux fois provoque une redéfinition.
- `#include "Point.h"` pour un fichier du projet, `#include <iostream>` pour la bibliothèque standard.
- `g++ -c fichier.cpp` compile sans lier et produit `fichier.o` ; `g++ a.o b.o -o prog` fait l'édition de liens.
- Dans un Makefile : `cible: dépendances`, puis la commande après une **tabulation** ; `$@` vaut la cible.
- Un `.o` dépend de son `.cpp` **et de tous les `.h` qu'il inclut**, directement ou non : un `.h` modifié doit faire recompiler tous les fichiers qui l'incluent.
- `make` ne refait que ce qui est plus ancien que ses dépendances ; `make clean` repart de zéro. [[Complément hors du cours|ⓘ]]
- Déclarer `.PHONY` les cibles qui ne sont pas des fichiers, et passer `-Wall -Wextra` par `CXXFLAGS`. [[Complément hors du cours|ⓘ]]
