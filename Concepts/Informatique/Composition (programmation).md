---
type: concept
tags: [year4]
aliases: [composition d'objets, object composition, relation « a un », has-a]
sources: ["[[Raw/Year 4/C／C++/programmes C++/exo-prof/classeSegment.cpp|classeSegment.cpp]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : en [[Programmation orientée objet|programmation orientée objet]], la composition est la relation dans laquelle un objet est formé d'autres objets, qu'il contient comme attributs : c'est la relation « **a un** » (*has-a*). Un `Segment` a deux `Point`, une voiture a un moteur. Les objets contenus font partie du contenant : ils sont créés avec lui et détruits avec lui.

```cpp
class Segment {
    Point A, B;                     // composition : un Segment a deux Point
public:
    Segment(const Point& a, const Point& b) : A(a), B(b) {}
};
```

Elle s'oppose à l'[[Héritage (programmation)|héritage]], relation « **est un** » (*is-a*) : un segment n'est pas un point, donc `Segment` ne doit pas hériter de `Point`. La maxime « préférer la composition à l'héritage » (*Design Patterns*, Gamma, Helm, Johnson et Vlissides, 1994) rappelle que la composition couple moins les classes : le contenant n'utilise que l'interface publique de ses composants, ce qui respecte l'[[Encapsulation (programmation)|encapsulation]].

En [[Langage C++|C++]] :

- les objets membres sont construits **avant** le corps du [[Constructeur (programmation)|constructeur]] du contenant, dans l'ordre de leur déclaration ; on leur passe leurs valeurs par la [[Liste d'initialisation|liste d'initialisation]], sinon ils sont d'abord construits par défaut puis modifiés ;
- ils sont détruits automatiquement après le corps du [[Destructeur (programmation)|destructeur]] du contenant, dans l'ordre inverse ;
- pour connaître la taille du contenant, le compilateur a besoin de la définition complète de la classe composante, d'où le `#include "Point.h"` dans `Segment.h` ([[Directive include]]).

En [[UML]], la composition se dessine par un losange plein du côté du contenant ; l'agrégation, forme plus faible où les parties peuvent exister sans le tout, par un losange vide.

## Dans le cours

- [[exo-prof]] : `Segment` contient deux `Point` ; la fiche conseille de les initialiser par la liste d'initialisation plutôt que de les construire à (0, 0) puis de les modifier.
- [[compilation séparée (C++)]] : la même composition, répartie sur plusieurs fichiers, explique pourquoi `Segment.h` inclut `Point.h`.
- [[4 - C++]] : l'exercice type fait construire un segment à partir de deux points.

Voir aussi : [[Classe et objet]], [[Héritage (programmation)]], [[Programmation orientée objet]].
