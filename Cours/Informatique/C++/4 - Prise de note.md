---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/C++/chp4 prise de note.pdf|chp4 prise de note.pdf]]"]
maj: 2026-11-08
complet: true
---

Résumé de [[Raw/Year 4/C++/chp4 prise de note.pdf|chp4 prise de note.pdf]] (9 pages manuscrites, avec des captures d'écran de code et de terminal), dans [[Cours/Informatique/C++/_index|C++]]. C'est la prise de note du cours résumé dans [[4 - C++]] : elle suit le même plan et ajoute la compilation, les exercices faits en séance et leur sortie. Le code des captures est recopié en texte ; l'invite du terminal, qui porte un nom, n'est pas reprise.

## Compiler un programme C++

```bash
g++ monprog.cpp -o monprog -Wall
./monprog
```

- `g++` compile aussi des fichiers `.c` (voir [[GCC]]).
- Le [[Langage C++|C++]] ajoute au [[Langage C|C]] la programmation orientée objet.

```cpp
int x;
int y;
std::cout << x + y;   // affiche : 30   (équivaut à printf("%d", x+y))
```

`std` désigne la bibliothèque (*library*), `cout` se lit « c out » (voir [[Flux d'entrée-sortie (C++)]], [[Fonctions printf et scanf]]).

```cpp
#include <iostream>

int main() {
    std::cout << "Bonjour, C++ !" << std::endl;
    return 0;
}
```

`std::endl` = `\n`, fin de ligne.

## Types de base et affichage

Types de base : `int`, `double`, `char` (un seul caractère), `bool`, `std::string` (chaîne de caractères). Voir [[Type primitif]].

- Les opérateurs restent les mêmes qu'en C.
- `if`, `for`, `while` et `switch case` ont la même syntaxe en C et en C++ (voir [[Structure conditionnelle]], [[Boucle (programmation)]]).

```cpp
std::cout << "Score :" << score << std::endl;   // affiche la valeur de la variable score
```

```cpp
int a = 12;
float f = 13,3;
std::cout << a << " " << f << std::endl;
```

Affiche `12 13,3`, avec une espace entre les deux valeurs (voir « Erreurs du cours » : en C++ le séparateur décimal est le point).

## La notion d'objet : classe et instance

```cpp
class Voiture {
public:
    std::string marque;
};

Voiture voiture1;
Voiture voiture2;

voiture1.marque = "Peugot";
```

Une `class` est l'équivalent approximatif d'une `struct` en C (voir [[Structure (struct)]]) : elle permet de créer un type de variable. Voir [[Classe et objet]].

**Données `public` et `private`** (voir [[Encapsulation (programmation)]]) :
- `public` : accessible depuis l'extérieur de la classe, n'importe quel code peut lire ou modifier ;
- `private` : accessible seulement dans la classe.

```cpp
class Point {
private:
    int x, y;
public:
    Point();               // on déclare la fonction
    affiche-coordonné();
};

Point::Point() {
    int x = 0;
}
```

**Portée** : `Point::` signifie « s'applique à la classe `Point` ».

```cpp
Point::affiche-coordonné(Point p) {
    std::cout << p.x << endl;
}
```

Selon la note, cela ne fonctionne pas tel quel : il faut déclarer la fonction dans la classe, et on rajoute `Point::` devant son nom pour la définir. (Complément, hors du cours : un nom de fonction ne peut pas contenir de tiret, et il manque le type de retour, `void` ; la version du PDF s'appelle `affiche`.)

Si on écrit `Point p;` dans le programme, cela crée une variable `p` de type `Point`, et deux variables `int` `x` et `y`. La note dit que `x` est initialisé à 0 parce qu'on l'a défini dans le constructeur (le **constructeur par défaut**), et que `y` prend probablement une valeur aléatoire parce qu'il n'est pas initialisé dans ce constructeur (voir [[Variable non initialisée]] ; voir « Erreurs du cours » pour `x`).

**Exercice demandé par l'enseignant** (sans résultat attendu, pour s'entraîner à écrire des classes) :

```cpp
#include <iostream>

class Cercle {
private :
        int x,y ;
        float rayon;
public :
        Cercle();
};

Cercle:: Cercle() {
        int x = 1;
        int y = 1;
}

int main() {

Cercle c;
Cercle();

return 0;
}
```

**Important** : la fonction qu'on crée pour réaliser un constructeur doit avoir **le même nom que la classe** (voir [[Constructeur (programmation)]]).

## Constructeur par paramètres (2e type)

```cpp
class Point {
private:
    int x, y;
public:
    Point(int a, int b) {
        x = a;
        y = b;
    }
};

Point p1(3, 4);
Point p2(5, 6);
std::cout << p1.x;
```

Version faite en séance :

```cpp
class Cercle {
private :
        int x,y;

public:
        Cercle(int a, int b) {

                x=a;
                y=b;
        }
};

int main() {

Cercle c1(1,2);
Cercle c2(3,4);


return 0;
}
```

## Constructeur par copie (3e type)

```cpp
class Point {
public:
    int x, y;

    Point(int a, int b) { x = a; y = b; }

    Point(const Point& autre) {
        x = autre.x;
        y = autre.y;
    }
};
```

Sur `const Point& autre`, la note dit : on récupère l'adresse (un pointeur) ; on ne modifie pas `autre`, on lit sa valeur. En toute rigueur, `Point&` est une **référence**, pas un pointeur (voir [[Référence (C++)]] ; complément, hors du cours).

```cpp
//constructeur par copie
class Cercle {
private :
        int x,y;

public:

        Cercle(int a, int b) {
                x=a;
                y=b;
        }

        Cercle(const Cercle& autre) {
                x=autre.x;
                y=autre.y;
        }
};

int main() {

Cercle c1(1,2);
Cercle c2(c1);
```

Consigne notée : avoir **toujours les 3 constructeurs en même temps** dans une classe ; ils sont séparés ici seulement pour mieux visualiser. C'est la consigne des exercices (voir l'exercice type de [[4 - C++]]), pas une règle du langage.

Avec un constructeur par copie, on peut écrire :

```cpp
Point p1(3, 4);
Point p2 = p1;
```

Classe complète faite en séance, avec une fonction d'affichage :

```cpp
class Cercle {
private :
        int x,y;

public:
        Cercle();
        Cercle(int a, int b) {
                x=a;
                y=b;
        }

        Cercle(const Cercle& autre) {
                x=autre.x;
                y=autre.y;
        }
        void affiche();

};

Cercle:: Cercle() {
        x = 1;
        y = 1;
};

void Cercle::affiche() {
        std::cout <<"x : "<< x << std::endl;
        std::cout <<"y : "<< y << std::endl;
};


int main() {

Cercle c1(1,2);
c1.affiche();
Cercle c2;
c2.affiche();

return 0;
}
```

Sortie de `./cercle` :

```text
x : 1
y : 2
x : 1
y : 1
```

Ici le constructeur par défaut affecte les attributs (`x = 1;`, sans `int`) : `c2` vaut bien (1, 1).

## Get et set

Ils permettent d'accéder aux variables privées pour les lire (*get*) et pour les modifier (*set*). Voir [[Accesseur et mutateur]].

```cpp
class CompteBancaire {
private:
    double solde;

public:
    double getSolde() {        // « getteur »
        return solde;
    }

    void setSolde(double s) {  // « setteur »
        solde = s;
    }
};
```

**Exercice** : créer un `getrayon` et un `setrayon` qui empêche d'entrer un rayon négatif. La note ne donne pas de correction ; la capture suivante applique get et set à `x` :

```cpp
class Cercle {
private :
        int x,y;
        //float rayon;

public:
        Cercle();
        Cercle(int a, int b) {
                x=a;
                y=b;

        }


        Cercle(const Cercle& autre) {
                x=autre.x;
                y=autre.y;
        }
        void affiche();
        float getX();
        void setX(int w);

};

Cercle:: Cercle() {
        x = 1;
        y = 1;
};

void Cercle::affiche() {
        std::cout <<"x : "<< x << std::endl;
        std::cout <<"y : "<< y << std::endl;
};

float Cercle::getX() {
        return x;
};

void Cercle::setX(int w) {
        x = w;
};

int main() {

Cercle c1(1,2);
c1.affiche();

c1.getX();
c1.setX(5);
c1.affiche();

return 0;
}
```

Sortie :

```text
x : 1
y : 2
x : 5
y : 2
```

La note s'arrête là : la surcharge d'opérateurs et l'exercice type ne sont que dans le PDF ([[4 - C++]]).

## Erreurs du cours

- **Constructeur `Point::Point() { int x = 0; }`** (page 3) : `int x = 0;` déclare une **nouvelle variable locale** `x`, qui masque l'attribut ; l'attribut `x` de l'objet n'est donc pas initialisé, pas plus que `y`. La note dit pourtant que `x` vaut 0. Il faut écrire `x = 0;` sans `int`, comme dans le PDF ([[4 - C++]]). Même faute dans le premier exercice `Cercle` (page 4, `int x = 1; int y = 1;`) ; les captures suivantes (pages 7 et 9) l'ont corrigée.
- **`float f = 13,3;`** (page 2) : en C++, le séparateur décimal est le point. `13,3` ne compile pas dans une déclaration ; il faut `float f = 13.3;`, et l'affichage est `12 13.3`.
- **`int x; int y; std::cout << x + y; // affiche : 30`** (page 1) : sans initialisation, le résultat est indéterminé ; le PDF écrit `int x = 10; int y = 20;`.

Source : [[Raw/Year 4/C++/chp4 prise de note.pdf|chp4 prise de note.pdf]].
