---
type: concept
tags: [year4]
aliases: [opérateur unaire, opérateur binaire, opérateurs unaires, opérateurs binaires, unary operator, binary operator, arité d'un opérateur]
sources: ["[[Raw/Year 4/C／C++/programmes C++/formation/10-SurchargeOpérateurs1.cpp|10-SurchargeOpérateurs1.cpp]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : l'**arité** d'un opérateur est son nombre d'opérandes. En [[Langage C|C]] et en [[Langage C++|C++]] :

- un opérateur **unaire** n'a qu'un opérande : `-a` (opposé), `!a` (NON logique), `~a` (NON bit à bit), `++a` et `a++` ([[Opérateur d'incrémentation]]), `*p` ([[Déréférencement]]), `&x` ([[Opérateur d'adresse]]), `sizeof x` ([[Opérateur sizeof]]) ;
- un opérateur **binaire** en a deux : `a + b` ([[Opérateurs arithmétiques]]), `a == b` ([[Opérateur de comparaison]]), `a && b` ([[Opérateur logique]]), `a = b` ([[Affectation]]), `a & b` ([[Opérateur bit à bit]]), `a, b` ([[Opérateur virgule]]) ;
- un seul opérateur est **ternaire**, à trois opérandes : `c ? a : b` ([[Opérateur conditionnel]]).

Un même symbole peut avoir plusieurs arités, que le compilateur distingue par le contexte : `-a` (unaire) et `a - b` (binaire), `*p` (déréférencement) et `a * b` (produit), `&x` (adresse) et `a & b` (ET bit à bit). Les opérateurs unaires sont plus prioritaires que les binaires : `-a * b` se lit `(-a) * b` ([[Associativité et ordre d'évaluation]]).

**En surcharge d'opérateurs** ([[Surcharge d'opérateurs]]), l'arité fixe le nombre de paramètres. Écrit comme méthode, un opérateur unaire ne prend **aucun** paramètre (l'opérande est l'objet lui-même) et un opérateur binaire en prend **un**, l'opérande de droite ; écrit comme fonction libre, il prend un ou deux paramètres. On ne peut pas changer l'arité d'un opérateur existant.

```cpp
class Point {
    int x, y;
public:
    Point(int x, int y) : x(x), y(y) {}
    Point operator-() const { return Point(-x, -y); }               // unaire : -p
    Point operator+(const Point& p) const { return Point(x + p.x, y + p.y); } // binaire : p + q
};
```

Le compilateur traduit `-p` en `p.operator-()` et `p + q` en `p.operator+(q)`.

## Dans le cours

- [[formation C++]] : `Point operator-()` surcharge l'opérateur unaire `-` (programme 10) et `Point operator+(Point)` l'opérateur binaire `+` (programme 11) ; l'opérateur d'affichage `<<` est une fonction libre `friend` (programme 12).
- [[4 - C++]] : la section sur la surcharge d'opérateurs présente l'opérateur unaire `-` et la traduction de `p1 + p2` en `p1.operator+(p2)`.

Voir aussi : [[Surcharge d'opérateurs]], [[Expression (programmation)]], [[Notation polonaise]].
