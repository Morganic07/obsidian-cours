---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/C++/chp4 prise de note.pdf|chp4 prise de note.pdf]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 4/C++/chp4 prise de note.pdf|chp4 prise de note.pdf]] (9 pages manuscrites, avec des captures d'écran de code et de terminal), dans [[Cours/Informatique/C++/_index|C++]]. C'est la prise de note du cours résumé dans [[4 - C++]] : elle suit le même plan et ajoute la compilation, les exercices faits en séance et leur sortie. Le code des captures est recopié en texte ; l'invite du terminal, qui porte un nom, n'est pas reprise.

## Compiler un programme C++

```bash
g++ monprog.cpp -o monprog -Wall
./monprog
```

- `g++` compile aussi des fichiers `.c` (voir [[GCC]]).
- Le [[Langage C++|C++]] ajoute au [[Langage C|C]] la programmation orientée objet.
- Les options : `-o monprog` donne le nom de l'exécutable (sans elle, il s'appelle `a.out`) ; `-Wall` active la plupart des **avertissements** (variable non initialisée, variable inutilisée…), qui signalent un code suspect sans bloquer la compilation ; `-std=c++17` (ou `c++20`) choisit la version de la norme. `./` lance l'exécutable du répertoire courant. [[Complément hors du cours|ⓘ]]
- `g++` traite un fichier `.c` **comme du C++** et ajoute la bibliothèque standard C++ à l'édition de liens ; `gcc` compile un `.c` comme du C. Un programme C qui utilise un mot réservé du C++ (`class`, `new`) comme nom de variable ne passe donc pas avec `g++`. [[Complément hors du cours|ⓘ]]
- La commande enchaîne quatre étapes (voir [[Chaîne de compilation]]) : le **préprocesseur** traite les `#include` ; la **compilation** traduit le code en assembleur ; l'**assemblage** produit un fichier objet `.o` ; l'**édition de liens** réunit les fichiers objets et les bibliothèques en un exécutable. Une faute de syntaxe est signalée à la compilation, une fonction déclarée mais jamais définie à l'édition de liens (`undefined reference`). [[Complément hors du cours|ⓘ]]

Les deux variables doivent être initialisées, sinon le résultat est indéterminé : [[Erreurs du cours#^e-4-prise-de-note|✎]]

```cpp
int x = 10;
int y = 20;
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

Avec une nuance : `std::endl` vide aussi le [[Tampon (buffer)|tampon]] de sortie, ce qui force l'affichage immédiat ; `"\n"` passe seulement à la ligne. `std` est plus précisément l'[[Espace de noms (namespace)|espace de noms]] de la bibliothèque standard, et `std::` le préfixe qui y désigne un nom ; `using namespace std;` permet de l'omettre. [[Complément hors du cours|ⓘ]]

## Types de base et affichage

Types de base : `int`, `double`, `char` (un seul caractère), `bool`, `std::string` (chaîne de caractères). Voir [[Type primitif]].

- Les opérateurs restent les mêmes qu'en C.
- `if`, `for`, `while` et `switch case` ont la même syntaxe en C et en C++ (voir [[Structure conditionnelle]], [[Boucle (programmation)]]).
- Le C++ (depuis C++11) ajoute une boucle qui parcourt tous les éléments d'un tableau ou d'une collection : `for (int v : tab) { std::cout << v << " "; }`. Il permet aussi de déclarer le compteur dans le `for` (`for (int i = 0; …)`), ce que le C n'autorise que depuis C99. [[Complément hors du cours|ⓘ]]

```cpp
std::cout << "Score :" << score << std::endl;   // affiche la valeur de la variable score
```

```cpp
int a = 12;
float f = 13.3;
std::cout << a << " " << f << std::endl;
```

Affiche `12 13.3`, avec une espace entre les deux valeurs : en C++, le séparateur décimal est le point (`13,3` ne compile pas dans une déclaration). [[Erreurs du cours#^e-4-prise-de-note|✎]]

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

En C++, l'équivalence est même presque exacte : une `struct` peut aussi avoir des méthodes et des constructeurs, et la seule différence est l'accès par défaut, public dans une `struct`, privé dans une `class`. Ce qu'une classe ajoute à la `struct` du C, ce sont les **fonctions membres** et le contrôle d'accès. [[Complément hors du cours|ⓘ]]

**Données `public` et `private`** (voir [[Encapsulation (programmation)]]) :
- `public` : accessible depuis l'extérieur de la classe, n'importe quel code peut lire ou modifier ;
- `private` : accessible seulement dans la classe.

Dans le constructeur, on écrit `x = 0;` sans `int` : `int x = 0;` déclarerait une nouvelle variable locale qui masquerait l'attribut, laissé alors non initialisé. [[Erreurs du cours#^e-4-prise-de-note|✎]]

```cpp
class Point {
private:
    int x, y;
public:
    Point();               // on déclare la fonction
    affiche-coordonné();
};

Point::Point() {
    x = 0;
}
```

**Portée** : `Point::` signifie « s'applique à la classe `Point` ».

```cpp
Point::affiche-coordonné(Point p) {
    std::cout << p.x << endl;
}
```

Selon la note, cela ne fonctionne pas tel quel : il faut déclarer la fonction dans la classe, et on rajoute `Point::` devant son nom pour la définir.

Un nom de fonction ne peut pas contenir de tiret, et il manque le type de retour, `void` ; la version du PDF s'appelle `affiche`. [[Complément hors du cours|ⓘ]]

`::` est l'**opérateur de résolution de portée** : `Point::affiche` signifie « la fonction `affiche` qui appartient à la classe `Point` », comme `std::cout` signifie « le `cout` de l'espace de noms `std` ». Sans le préfixe, `void affiche() { … }` définirait une fonction ordinaire, sans lien avec la classe et sans accès à `x` et `y`. Une méthode n'a pas besoin de recevoir l'objet en paramètre (`affiche-coordonné(Point p)`) : appelée par `p.affiche()`, elle travaille directement sur les attributs de `p`. [[Complément hors du cours|ⓘ]]

Si on écrit `Point p;` dans le programme, cela crée une variable `p` de type `Point`, et deux variables `int` `x` et `y`. La note dit que `x` est initialisé à 0 parce qu'on l'a défini dans le constructeur (le **constructeur par défaut**), et que `y` prend probablement une valeur aléatoire parce qu'il n'est pas initialisé dans ce constructeur (voir [[Variable non initialisée]]).

**Exercice demandé par l'enseignant** (sans résultat attendu, pour s'entraîner à écrire des classes ; même règle, les attributs s'affectent sans `int` dans le constructeur) : [[Erreurs du cours#^e-4-prise-de-note|✎]]

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
        x = 1;
        y = 1;
}

int main() {

Cercle c;
Cercle();

return 0;
}
```

Dans ce `main`, `Cercle c;` crée un objet nommé `c` en appelant le constructeur par défaut. La ligne `Cercle();` appelle elle aussi le constructeur, mais crée un objet **temporaire** sans nom, détruit dès la fin de l'instruction : elle ne sert à rien ici. Et `Cercle c();`, avec des parenthèses vides, ne créerait pas d'objet du tout : le compilateur y lit la déclaration d'une fonction `c` qui renvoie un `Cercle`. [[Complément hors du cours|ⓘ]]

**Important** : la fonction qu'on crée pour réaliser un constructeur doit avoir **le même nom que la classe** (voir [[Constructeur (programmation)]]).

Le constructeur n'a **aucun type de retour**, pas même `void`. On ne l'appelle jamais comme une méthode (`c.Cercle()` est interdit) : il s'exécute une seule fois, à la création de l'objet. [[Complément hors du cours|ⓘ]]

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
    int getX() const { return x; }
};

Point p1(3, 4);
Point p2(5, 6);
std::cout << p1.getX();
```

Comme `x` est `private` dans cette classe, on le lit hors de la classe par un accesseur (voir « Get et set » plus bas) : `std::cout << p1.x;` serait refusé par le compilateur. [[Erreurs du cours#^e-4-prise-de-note|✎]]

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

Sur `const Point& autre`, la note dit : on récupère l'adresse (un pointeur) ; on ne modifie pas `autre`, on lit sa valeur.

En toute rigueur, `Point&` est une **référence**, pas un pointeur (voir [[Référence (C++)]]) : un autre nom pour l'objet passé, qui s'utilise sans `*` (`autre.x` et non `autre->x`). Le compilateur la réalise souvent avec une adresse, d'où l'intuition de la note. Elle est même obligatoire ici : passé par valeur, `autre` serait une copie, dont la création appellerait le constructeur par copie lui-même, sans fin. [[Complément hors du cours|ⓘ]]

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

Le point-virgule après l'accolade fermante d'une **définition de fonction** (`Cercle:: Cercle() { … };`) est inutile mais accepté : c'est une [[Instruction vide|déclaration vide]], que `-Wall -Wpedantic` peut signaler. Il n'est obligatoire qu'après la définition de la classe elle-même (`class Cercle { … };`). [[Complément hors du cours|ⓘ]]

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

Deux détails de cette capture : `getX()` renvoie un `float` alors que `x` est un `int` (la valeur est convertie, mais le type de retour devrait être `int`) ; et `c1.getX();` seul ne sert à rien, la valeur renvoyée n'étant ni affichée ni rangée (`std::cout << c1.getX();`). Un accesseur se déclare en général `const` : `int getX() const;`. [[Complément hors du cours|ⓘ]]

Une correction possible de l'exercice du rayon : le mutateur n'accepte la valeur que si elle est positive ou nulle, et le constructeur par paramètres passe par lui pour que la règle vaille dès la création. [[Complément hors du cours|ⓘ]]

```cpp
class Cercle {
private:
    int x, y;
    float rayon;
public:
    Cercle(int a, int b, float r) {
        x = a;
        y = b;
        rayon = 0;
        setRayon(r);
    }
    float getRayon() const { return rayon; }
    void setRayon(float r) {
        if (r >= 0) {
            rayon = r;
        } else {
            std::cerr << "Rayon négatif refusé" << std::endl;
        }
    }
};
```

La note s'arrête là : la surcharge d'opérateurs et l'exercice type ne sont que dans le PDF ([[4 - C++]]).
