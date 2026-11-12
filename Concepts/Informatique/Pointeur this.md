---
type: concept
tags: [year4]
aliases: [this, this pointer, mot-clé this, "*this"]
sources: ["[[Raw/Year 4/C／C++/programmes C++/formation/6-constructeurParametre.cpp|6-constructeurParametre.cpp]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : dans une méthode non statique d'une [[Classe et objet|classe]] [[Langage C++|C++]], `this` est un [[Pointeur et adresse mémoire|pointeur]] vers l'objet sur lequel la méthode est appelée. Lors de l'appel `p1.affiche()`, `this` vaut `&p1`. Le compilateur le passe comme un paramètre caché : une méthode est en fait une fonction qui reçoit l'adresse de son objet.

Dans le corps d'une méthode, un attribut `x` est un raccourci de `this->x` ([[Opérateur flèche]]). On écrit `this` explicitement dans trois cas :

- **lever un [[Masquage de nom|masquage]]** : quand un paramètre porte le nom d'un attribut, `x` désigne le paramètre, et `x = x;` l'affecte à lui-même ; `this->x = x;` vise l'attribut. La [[Liste d'initialisation|liste d'initialisation]] `: x(x)` évite le problème dans un [[Constructeur (programmation)|constructeur]] ;
- **renvoyer l'objet lui-même**, par `return *this;` ([[Déréférencement]]), pour enchaîner les appels ou dans les opérateurs d'affectation (`operator=`, `operator+=`, voir [[Opérateur d'affectation par copie]]) ;
- **passer l'objet courant** à une autre fonction, ou tester l'auto-affectation : `if (this != &autre)`.

```cpp
class Point {
    int x, y;
public:
    Point(int x, int y) { this->x = x; this->y = y; }   // paramètres masquant les attributs
    Point& deplacer(int dx, int dy) { x += dx; y += dy; return *this; }
};
Point p(0, 0);
p.deplacer(1, 2).deplacer(3, 4);                       // chaînage grâce à *this
```

Dans une [[Méthode constante|méthode constante]], `this` est un pointeur vers un objet constant (`const Point*`), ce qui interdit de modifier les attributs. Une méthode `static` n'a pas de `this`, n'étant liée à aucun objet. En [[Langage Java|Java]], `this` est une référence et s'écrit `this.x` ; en [[Langage Python|Python]], c'est le paramètre explicite `self`.

## Dans le cours

- [[4 - C++]] : un complément présente `this`, avec `x` raccourci de `this->x` et `void setX(int x) { this->x = x; }`.
- [[formation C++]] : complément sur le constructeur `Point(int x, int y)` (programme 6), où `x = x;` n'affecterait pas l'attribut.

Voir aussi : [[Classe et objet]], [[Masquage de nom]], [[Opérateur flèche]], [[Méthode constante]].
