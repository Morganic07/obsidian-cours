---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
complet: true
enrichi: 2026-11-11
---

Résumé de [[Raw/Year 4/C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]] (5 diapositives), dans [[Cours/Informatique/C++/_index|C++]]. Le chapitre reprend les classes `Point` et `Segment` de [[4 - C++]] et les répartit en plusieurs fichiers : [[Fichier d'en-tête|fichiers d'en-tête]] `.h` et [[Fichier source|fichiers source]] `.cpp`, [[Directive include|directives `#include`]] traitées par le [[Préprocesseur|préprocesseur]], [[Compilation séparée|compilation séparée]] de chaque `.cpp` en [[Fichier objet|fichier objet]] `.o`, [[Édition de liens|édition de liens]], puis automatisation avec un [[Make (logiciel)|Makefile]].

## Plan

1. Découper le code : `.h` et `.cpp`.
2. L'exemple : les classes `Point` et `Segment`.
3. Les `#include` et le préprocesseur.
4. Compilation séparée : de `.cpp` à `.o`, puis à l'[[Exécutable|exécutable]].
5. Le Makefile.

## 1. Découper le code : `.h` et `.cpp`

Un programme en [[Langage C++|C++]], [[Langage compilé|langage compilé]], d'une certaine taille ne tient pas dans un seul fichier de [[Code source|code source]] : on le découpe, en général un couple de fichiers par [[Classe et objet|classe]]. C'est la [[Programmation modulaire|programmation modulaire]] appliquée au C++.

| Fichier | Rôle |
|---|---|
| **[[Fichier d'en-tête\|Fichier d'en-tête]]** `.h` | **déclare** ce qui existe : classes, [[Classe et objet\|attributs]], prototypes des méthodes. C'est l'**interface**, ce que les autres fichiers ont besoin de connaître. |
| **[[Fichier source\|Fichier source]]** `.cpp` | **définit** le code des méthodes. C'est l'**implémentation** : chaque `.cpp` est [[Compilation séparée\|compilé séparément]] des autres. |

Cette séparation entre [[Interface et implémentation|interface et implémentation]] repose sur la distinction entre [[Déclaration et définition|déclaration et définition]] : une déclaration annonce un nom et son type (« la méthode `Point(int, int)` existe »), une définition fournit le code ou réserve la mémoire. Un fichier qui utilise une classe n'a besoin que de sa déclaration, qu'il obtient en incluant l'en-tête ; le code des méthodes n'est fourni qu'une fois, au moment de l'[[Édition de liens|édition de liens]]. [[Complément hors du cours|ⓘ]]

Organisation du projet de l'exemple :

```text
mon_projet/
├── Point.h       déclaration de la classe Point
├── Point.cpp     définition de ses méthodes
├── Segment.h     déclaration de la classe Segment
├── Segment.cpp   définition de ses méthodes
└── main.cpp      programme principal : main()
```

Programme principal, tel que le donne le cours ; la [[Fonction main (C et C++)|fonction `main`]] est le point d'entrée du programme, et elle seule ne se range dans aucune classe. Il n'inclut que `Segment.h` (qui inclut lui-même `Point.h`) et `<iostream>`, la partie de la [[Bibliothèque standard du C++|bibliothèque standard]] qui fournit les [[Flux d'entrée-sortie (C++)|flux d'entrée-sortie]].

```cpp
#include "Segment.h"
#include <iostream>

int main() {
    Point a(0, 0), b(3, 4);
    Segment s(a, b);
    a.affiche();
    s.affiche();     // 5
    return 0;
}
```

Les classes `Point` et `Segment` des diapositives suivantes ne déclarent pas de méthode `affiche()` : ce `main` ne compile pas (`error: 'class Point' has no member named 'affiche'`). Il faut déclarer `void affiche() const;` dans `Point.h` et dans `Segment.h`, et la définir dans `Point.cpp` et `Segment.cpp` (voir la version complète au § 2). [[Erreurs du cours#^e-5-compilation-separee|✎]]

Le commentaire `// 5` donne la longueur attendue : le segment de $(0, 0)$ à $(3, 4)$ mesure $\sqrt{3^2 + 4^2} = \sqrt{25} = 5$ par le [[Théorème de Pythagore|théorème de Pythagore]] ([[Distance|distance euclidienne]]). [[Complément hors du cours|ⓘ]]

## 2. L'exemple : les classes `Point` et `Segment`

**Point.h** : la [[Classe et objet|classe]] déclare ses attributs (deux `int`, [[Type primitif|type primitif]] entier) et le [[Déclaration et définition|prototype]] de son [[Constructeur (programmation)|constructeur]] ; le fichier est protégé par une [[Garde d'inclusion|garde d'inclusion]] (`#ifndef` … `#endif`, voir § 3).

```cpp
#ifndef POINT_H
#define POINT_H
class Point {
public:
    int x, y;
    Point(int a, int b);   // déclaration
};
#endif //POINT_H
```

**Point.cpp** : inclut son propre en-tête, puis définit le constructeur. Le nom complet `Point::Point` utilise l'[[Opérateur de résolution de portée|opérateur de résolution de portée]] `::`, qui rattache la définition à la classe `Point`.

```cpp
#include "Point.h"

Point::Point(int a, int b) {   // définition
    x = a;
    y = b;
}
```

**Segment.h** : un `Segment` contient deux `Point` ; l'en-tête doit donc inclure `Point.h`, sans quoi le type `Point` serait inconnu à la compilation.

```cpp
#ifndef SEGMENT_H
#define SEGMENT_H

#include "Point.h"

class Segment {
public:
    Point p1, p2;
    double longueur;
    Segment(Point a, Point b);
};

#endif //SEGMENT_H
```

**Segment.cpp** : le constructeur initialise `p1` et `p2` par une [[Liste d'initialisation|liste d'initialisation]] (`: p1(a), p2(b)`), puis calcule la longueur avec `std::sqrt` ([[Racine carrée|racine carrée]], déclarée dans l'en-tête standard [[Bibliothèque cmath|`<cmath>`]]). `dx` et `dy` sont des `double` ([[Nombre à virgule flottante|nombres à virgule flottante]]) : la différence de deux `int` y est convertie.

```cpp
#include "Segment.h"
#include <cmath>

Segment::Segment(Point a, Point b)
    : p1(a), p2(b) {
    double dx = p2.x - p1.x;
    double dy = p2.y - p1.y;
    longueur = std::sqrt(dx*dx + dy*dy);
}
```

La liste d'initialisation n'est pas ici une affaire de style : `Point` n'a pas de constructeur par défaut (sans paramètre). Sans liste, le compilateur devrait construire `p1` et `p2` par défaut avant d'entrer dans le corps du constructeur, et refuse : `error: no matching function for call to 'Point::Point()'`. Les attributs sont toujours construits avant le corps du constructeur, dans l'ordre de leur déclaration dans la classe. [[Complément hors du cours|ⓘ]]

Les deux `Point` sont passés **par valeur** ([[Passage par valeur|passage par valeur]]) : chaque appel en fait une copie. Pour un objet plus gros, on écrirait `Segment(const Point& a, const Point& b)`, une [[Référence (C++)|référence]] constante qui évite la copie. [[Complément hors du cours|ⓘ]]

Les attributs sont ici `public` pour simplifier ; avec des attributs privés ([[Encapsulation (programmation)|encapsulation]]), `Segment` passerait par des [[Accesseur et mutateur|accesseurs]] `getX()` et `getY()`, comme dans [[4 - C++]]. [[Complément hors du cours|ⓘ]]

Version qui compile avec le `main` du § 1 : on ajoute la méthode `affiche()`, déclarée [[Méthode constante|constante]] (`const` : elle ne modifie pas l'objet). `main.cpp` peut alors inclure aussi `Point.h`, sans dommage grâce aux gardes. [[Erreurs du cours#^e-5-compilation-separee|✎]]

```cpp
// Point.h
#ifndef POINT_H
#define POINT_H
class Point {
public:
    int x, y;
    Point(int a, int b);
    void affiche() const;
};
#endif

// Point.cpp
#include "Point.h"
#include <iostream>
Point::Point(int a, int b) { x = a; y = b; }
void Point::affiche() const {
    std::cout << "(" << x << ", " << y << ")" << std::endl;
}

// Segment.h : comme plus haut, avec en plus
//     void affiche() const;

// Segment.cpp : comme plus haut, avec en plus #include <iostream> et
void Segment::affiche() const { std::cout << longueur << std::endl; }
```

Sortie : `(0, 0)` puis `5`.

## 3. Les `#include` et le préprocesseur

Le **[[Préprocesseur|préprocesseur]]** remplace chaque `#include` par le contenu du fichier désigné, **avant** la compilation.

| Forme | Usage |
|---|---|
| [[Directive include\|`#include`]] `"Point.h"` | **guillemets** : fichier du projet, cherché d'abord dans le dossier du fichier qui contient le `#include`, puis comme les chevrons. [[Erreurs du cours#^e-5-compilation-separee\|✎]] |
| `#include <iostream>` | **chevrons** : [[Bibliothèque standard du C++\|bibliothèque standard]] ou système (`iostream`, `cmath`…). |

Le dossier de recherche des guillemets est celui du fichier qui fait l'inclusion, pas le [[Chemin de fichier|répertoire courant]] depuis lequel on lance `g++` : les deux coïncident dans un projet à plat comme celui-ci, mais pas quand les sources sont rangées dans des sous-dossiers. Les autres dossiers s'ajoutent avec l'option `-I` (`g++ -Iinclude -c main.cpp`). [[Complément hors du cours|ⓘ]]

Les en-têtes de la bibliothèque standard du C++ n'ont pas d'[[Extension de nom de fichier|extension]] (`<iostream>`, [[Bibliothèque cmath|`<cmath>`]], `<string>` pour la [[Classe string (C++)|classe `string`]]) ; ceux hérités du [[Langage C|C]] existent sous deux noms, `<math.h>` et `<cmath>`, la seconde forme rangeant ses noms dans l'[[Espace de noms (namespace)|espace de noms]] `std` (`std::sqrt`). [[Complément hors du cours|ⓘ]]

**[[Garde d'inclusion|Garde d'inclusion]]** : deux écritures, dans `Point.h`.

```cpp
// garde d'inclusion, version courte
#pragma once

// ou, version classique :
#ifndef POINT_H
#define POINT_H
// ... déclarations ...
#endif
```

**Chaîne d'inclusion** : `main.cpp` → `Segment.h` → `Point.h`. La garde évite que `Point.h` soit lu deux fois, ce qui définirait la classe `Point` en double.

Avec la seule chaîne du cours, `Point.h` n'est inclus qu'une fois ; le cas se produit dès que `main.cpp` inclut à la fois `Segment.h` et `Point.h`. Sans garde, [[GCC|`g++`]] s'arrête alors sur une [[Erreur de compilation|erreur de compilation]] sur `error: redefinition of 'class Point'`. La version classique repose sur la [[Compilation conditionnelle|compilation conditionnelle]] : à la première inclusion, la [[Macro (préprocesseur)|macro]] `POINT_H` n'est pas définie, le contenu est gardé et `#define POINT_H` la définit ; à la seconde, `#ifndef POINT_H` est faux et tout jusqu'à `#endif` est sauté. Le nom de la macro doit être propre à chaque fichier. `#pragma once` n'appartient pas à la [[Norme du C++|norme du C++]] (sa [[Portabilité (informatique)|portabilité]] n'est donc garantie qu'en pratique), mais les [[Compilateur|compilateurs]] [[GCC]], [[Clang]] et [[Visual Studio|MSVC]] l'acceptent tous. [[Complément hors du cours|ⓘ]]

La garde ne protège qu'à l'intérieur d'**une** [[Unité de compilation|unité de compilation]] (un `.cpp` et tout ce qu'il inclut). Chaque `.cpp` reprend l'inclusion à zéro : `Point.h` est bien lu une fois par `main.cpp`, une fois par `Point.cpp`, une fois par `Segment.cpp`. C'est pourquoi un en-tête ne contient que des déclarations, et pas le code des fonctions : une fonction définie dans un `.h` inclus par trois `.cpp` serait définie trois fois, et l'[[Édition de liens|éditeur de liens]] refuserait (`multiple definition of …`). C'est la [[Règle de la définition unique|règle de la définition unique]] (*one definition rule*). Les méthodes écrites dans le corps de la classe y échappent, car elles sont implicitement [[Fonction inline|inline]]. [[Complément hors du cours|ⓘ]]

`g++ -E main.cpp` montre le résultat du préprocesseur : avec `<iostream>`, ce petit `main` devient un texte de plus de 37 000 lignes (g++ 14). [[Complément hors du cours|ⓘ]]

## 4. Compilation séparée : de `.cpp` à `.o`, puis à l'exécutable

![[5 - Compilation séparée - image1.png]]
*Figure : chaque source est compilée séparément par `g++ -c` en fichier objet ; l'édition de liens assemble les trois `.o` en un exécutable, `programme`.*

```bash
g++ -c Point.cpp               # produit Point.o
g++ -c Segment.cpp             # produit Segment.o
g++ -c main.cpp                # produit main.o
g++ Point.o Segment.o main.o -o programme      # édition de liens
```

- `-c` (*compile only*) s'arrête avant l'[[Édition de liens|édition de liens]] et produit le **[[Fichier objet|fichier objet]]** `.o` ([[Code machine|code machine]] encore incomplet, avec la liste des noms qu'il définit et de ceux qu'il utilise sans les définir).
- La dernière commande ne compile rien : [[GCC|`g++`]] y appelle l'**éditeur de liens** (`ld`), qui réunit les `.o` et la [[Bibliothèque standard du C++|bibliothèque standard]] en un seul [[Exécutable|exécutable]], nommé par `-o`.

Les [[Option de compilation|options de compilation]] `-c` et `-o` sont celles de [[4 - Prise de note]], où tout tenait en une commande : `g++ monprog.cpp -o monprog -Wall`. Cette commande unique enchaîne en réalité toutes les étapes de la [[Chaîne de compilation|chaîne de compilation]] : préprocesseur, [[Compilateur|compilation]] en [[Langage d'assemblage|assembleur]], assemblage en fichier objet, édition de liens. [[Complément hors du cours|ⓘ]]

L'intérêt de la séparation, outre la [[Maintenabilité|maintenabilité]] d'un code rangé par classe : quand on modifie `Point.cpp`, seul `Point.o` est à refaire, puis l'édition de liens ; les autres `.o` resservent tels quels. Le gain croît avec la taille du projet. En revanche, modifier `Point.h` oblige à recompiler tous les `.cpp` qui l'incluent, directement ou non : ici les trois. [[Complément hors du cours|ⓘ]]

Deux familles d'erreurs, selon l'étape (dans les deux cas, `g++` se termine avec un [[Code de retour|code de retour]] non nul) : [[Erreur de compilation|erreur de compilation]] quand un `.cpp` est incorrect ou utilise un nom non déclaré (en-tête oublié) ; erreur d'édition de liens quand un nom est déclaré mais défini nulle part, par exemple si l'on oublie `Point.o` dans la dernière commande : `undefined reference to 'Point::Point(int, int)'` puis `ld returned 1 exit status`. Le message cite le [[Symbole (édition de liens)|symbole]] introuvable. [[Complément hors du cours|ⓘ]]

Le code de la [[Bibliothèque standard du C++|bibliothèque standard]] est lié **dynamiquement** par défaut : l'exécutable appelle `libstdc++` sous forme de [[Bibliothèque partagée|bibliothèque partagée]], chargée au lancement. On peut aussi regrouper ses propres `.o` en [[Bibliothèque statique|bibliothèque statique]] (`ar rcs libgeom.a Point.o Segment.o`) dont le code est copié dans l'exécutable. [[Complément hors du cours|ⓘ]]

## 5. Automatiser avec un Makefile

Taper ces commandes à chaque modification devient vite pénible : l'outil **[[Make (logiciel)|make]]** les lance à partir d'un fichier nommé `Makefile`, et ne refait que ce qui a changé.

```makefile
CXX      = g++
CXXFLAGS = -Wall -std=c++17

programme: main.o Point.o Segment.o
	$(CXX) $^ -o $@

main.o: main.cpp Segment.h Point.h
	$(CXX) $(CXXFLAGS) -c $<

Point.o: Point.cpp Point.h
	$(CXX) $(CXXFLAGS) -c $<

Segment.o: Segment.cpp Segment.h Point.h
	$(CXX) $(CXXFLAGS) -c $<

clean:
	rm -f *.o programme
```

- **Règle** : `cible: dépendances`. La **cible** est le fichier à produire ; les **dépendances** sont les fichiers dont elle dépend.
- **Commande** : la ligne commence **obligatoirement par une tabulation**, pas par des espaces.
- **Variables** : `CXX` (le [[Compilateur|compilateur]]) et `CXXFLAGS` (ses [[Option de compilation|options]]) se définissent en tête et s'emploient avec `$(…)`.
- **Variables automatiques** :

| Variable | Sens |
|---|---|
| `$@` | la cible |
| `$<` | la 1re dépendance |
| `$^` | toutes les dépendances |

Lecture des options : `-Wall` active la plupart des [[Avertissement de compilation|avertissements]] ; `-std=c++17` choisit la version C++17 de la [[Norme du C++|norme du langage]]. [[Complément hors du cours|ⓘ]]

Utilisation, depuis l'[[Interface en ligne de commande|interface en ligne de commande]] d'un [[Émulateur de terminal|terminal]], sous [[Linux]] : `make` construit la première cible du fichier (`programme`) ; `make clean` lance la règle `clean`, qui efface les `.o` et l'exécutable avec la [[Commande rm|commande `rm`]] (`-f` : sans erreur si le fichier n'existe pas). [[Complément hors du cours|ⓘ]]

Fonctionnement : make compare les dates de modification des fichiers ([[Fichier objet|`.o`]], [[Fichier source|sources]], [[Fichier d'en-tête|en-têtes]]). Une cible est refaite si elle n'existe pas ou si l'une de ses dépendances est plus récente qu'elle ; les dépendances sont d'abord mises à jour elles-mêmes, récursivement. Après `touch Point.h` (la [[Commande touch|commande `touch`]] met la date du fichier à l'heure courante), `make` refait les trois `.o` (tous dépendent de `Point.h`) puis `programme` ; après une modification de `main.cpp` seul, il ne refait que `main.o` et `programme`. D'où l'importance de lister les `.h` dans les dépendances : un en-tête oublié et le programme est lié avec des `.o` périmés, d'où des erreurs incompréhensibles. [[Complément hors du cours|ⓘ]]

Une ligne de commande commencée par des espaces au lieu d'une [[Caractère de tabulation|tabulation]] donne l'erreur `Makefile:4: *** missing separator.  Stop.` (le numéro est celui de la ligne fautive). [[Complément hors du cours|ⓘ]]

`clean` n'est pas un fichier : on la déclare d'habitude « cible factice » par `.PHONY: clean`, pour que la règle s'exécute même si un fichier nommé `clean` existe dans le dossier. [[Complément hors du cours|ⓘ]]

Sur les projets plus importants, on n'écrit plus le Makefile à la main : un générateur comme [[CMake]] le produit (ou un fichier pour un autre outil, comme [[Ninja (logiciel)|Ninja]]), et les [[Environnement de développement intégré|environnements de développement]] s'en servent pour compiler, à partir d'une description du projet, et les options `-MMD -MP` de `g++` peuvent calculer automatiquement les dépendances aux `.h`. [[Complément hors du cours|ⓘ]]

## À retenir

- [[Fichier d'en-tête|`.h`]] = [[Déclaration et définition|déclarations]] ([[Interface et implémentation|interface]]), protégées par une [[Garde d'inclusion|garde d'inclusion]] ; [[Fichier source|`.cpp`]] = définitions (implémentation), une par classe en général.
- [[Directive include|`#include "…"`]] pour les fichiers du projet, `#include <…>` pour la [[Bibliothèque standard du C++|bibliothèque standard]].
- `g++ -c f.cpp` → [[Fichier objet|`f.o`]] ; `g++ a.o b.o -o prog` → [[Édition de liens|édition de liens]].
- [[Make (logiciel)|Makefile]] : `cible: dépendances`, puis la commande après une tabulation ; `$@`, `$<`, `$^`.
- Ne jamais définir de fonction hors classe dans un `.h` inclus par plusieurs `.cpp` ([[Règle de la définition unique|règle de la définition unique]]). [[Complément hors du cours|ⓘ]]
