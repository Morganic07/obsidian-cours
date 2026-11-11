---
type: concept
tags: [year4]
aliases: [member initializer list, initializer list (constructeur), liste d'initialisation des membres]
matieres: [C++]
sources: ["[[Raw/Year 4/C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : la liste d'initialisation d'un [[Constructeur (programmation)|constructeur]] C++ initialise les attributs **avant** l'entrée dans le corps du constructeur. Elle s'écrit après la parenthèse des paramètres, introduite par `:`, sous la forme `attribut(valeur)` séparés par des virgules. Les attributs sont construits dans l'ordre de leur déclaration dans la classe, quel que soit l'ordre de la liste.

```cpp
Segment::Segment(Point a, Point b)
    : p1(a), p2(b) {          // p1 et p2 construits par copie de a et b
    ...
}
```

Elle est **obligatoire** pour initialiser :
- un attribut objet dont la classe n'a pas de constructeur par défaut ;
- un attribut constant (`const`) ou une [[Référence (C++)|référence]], qui ne peuvent pas être affectés après coup ;
- la classe de base, en cas d'[[Héritage (programmation)|héritage]].

Pour les autres attributs, elle évite une construction par défaut suivie d'une [[Affectation|affectation]]. Écrire `int x = 0;` dans le corps du constructeur déclare au contraire une variable locale, sans toucher l'attribut (erreur relevée dans [[4 - Prise de note]]).

## Dans le cours

[[5 - Compilation séparée]] l'emploie sans la nommer dans `Segment.cpp` : `: p1(a), p2(b)`. Elle y est indispensable, car `Point` n'a que le constructeur `Point(int, int)` : sans elle, `g++` signale `no matching function for call to 'Point::Point()'`.

Voir aussi : [[Classe et objet]], [[Langage C++]].

Résumés : [[5 - Compilation séparée]]
