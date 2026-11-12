---
type: concept
tags: [year4]
aliases: [scope resolution operator, opérateur ::, opérateur de portée]
matieres: [C／C++]
sources: ["[[Raw/Year 4/C／C++/chp4 C++.pdf|chp4 C++.pdf]]", "[[Raw/Year 4/C／C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : en [[Langage C++|C++]], l'opérateur `::` qualifie un nom par la portée à laquelle il appartient : une classe (`Point::affiche`), un [[Espace de noms (namespace)|espace de noms]] (`std::cout`, `std::sqrt`) ou, sans rien à gauche, la portée globale (`::x`). Il lève l'ambiguïté quand un même nom existe dans plusieurs portées (voir [[Portée d'une variable]]).

Son usage le plus courant est la définition d'une méthode **hors de la classe**, dans le [[Fichier source|fichier source]] : sans `Point::`, `affiche` serait une fonction libre, sans accès aux attributs de `Point`.

```cpp
void Point::affiche() const {   // méthode affiche de la classe Point
    std::cout << x << ", " << y << std::endl;
}
```

`Point::Point(int a, int b)` se lit « le constructeur `Point` de la classe `Point` ».

## Dans le cours

- [[4 - C++]] définit les méthodes hors de la classe avec `Point::`, et écrit `std::cout`.
- [[5 - Compilation séparée]] : `Point::Point` et `Segment::Segment` dans les fichiers `.cpp` ; `std::sqrt` de `<cmath>`.

Voir aussi : [[Classe et objet]], [[Déclaration et définition]].

- [[4 - Cours complet]] : `::` permet la résolution de portée en C++, « un peu comme le `/` dans un chemin », comme dans `std::cout`.

Résumés : [[4 - C++]], [[5 - Compilation séparée]], [[4 - Cours complet]]
