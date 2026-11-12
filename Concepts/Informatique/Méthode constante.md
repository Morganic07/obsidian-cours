---
type: concept
tags: [year4]
aliases: [méthode const, const member function, fonction membre constante]
matieres: [C／C++]
sources: ["[[Raw/Year 4/C／C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : en [[Langage C++|C++]], une méthode déclarée avec `const` après ses parenthèses s'engage à ne pas modifier l'objet sur lequel elle est appelée. Le compilateur refuse toute modification d'un attribut dans son corps. Seules les méthodes constantes peuvent être appelées sur un objet constant ou sur une [[Référence (C++)|référence]] `const`, d'où l'habitude de marquer `const` tous les [[Accesseur et mutateur|accesseurs]] et les méthodes d'affichage.

```cpp
class Point {
    int x, y;
public:
    int getX() const { return x; }      // ne modifie pas l'objet
    void setX(int v) { x = v; }         // modifie : pas const
    void affiche() const;
};
void Point::affiche() const { std::cout << x << ", " << y; }   // const répété dans la définition
```

`const` fait partie de la signature : il se répète dans la définition hors classe ([[Opérateur de résolution de portée]]).

## Dans le cours

Pas nommé : la version corrigée du code de [[5 - Compilation séparée]] déclare `void affiche() const;` dans `Point` et `Segment`.

- [[formation C++]] : les accesseurs comme `getVolume` de `Television` et l'opérateur unaire `operator-` de `Point` ne modifient pas l'objet et gagneraient à être déclarés `const`, pour être appelables sur un `const Point&`.
- [[exo-prof]] : `int getX() const` dans `classeSegment.cpp` ; les accesseurs de `classePoint.cpp` ne sont pas `const`, si bien qu'on ne peut pas les appeler sur un `const Point&`.
- [[compilation séparée (C++)]] : `getX()` et `getY()` de `Point.h` ne sont pas déclarés `const` ; il faudrait l'ajouter dans la déclaration et dans la définition.

Voir aussi : [[Constante (programmation)]], [[Classe et objet]].

Résumés : [[5 - Compilation séparée]]
