---
type: concept
tags: [year4]
aliases: [surcharge d'opérateur, operator overloading, operator+, operator-, "operator<<", surcharge de l'opérateur d'affichage]
sources: ["[[Raw/Year 4/C++/chp4 C++.pdf|chp4 C++.pdf]]"]
maj: 2026-11-08
---

**Définition** (d'après [[4 - C++]]) : en C++, on peut **redéfinir le comportement d'un opérateur** (`-`, `+`, `<<`…) pour ses propres classes. La fonction s'appelle `operator` suivi du symbole ; elle est appelée automatiquement quand on écrit l'opérateur.

| Type | Exemple | Définition |
|---|---|---|
| **unaire** (un seul objet, `-x`) | `Point p2 = -p1;` donne (-3, -4) | `Point operator-() { return Point{-x, -y}; }` |
| **binaire** (deux objets, `a + b`) | `Point p3 = p1 + p2;` | `Point operator+(Point autre) { return Point{x + autre.x, y + autre.y}; }` |
| **affichage** | `std::cout << p;` affiche `(3, 4)` | voir ci-dessous |

Le `return Point(...)` appelle le [[Constructeur (programmation)|constructeur par paramètres]] avec les nouvelles coordonnées.

**Opérateur d'affichage** `<<` :

```cpp
friend std::ostream& operator<<(std::ostream& os, const Point& p) {
    os << "(" << p.x << ", " << p.y << ")";
    return os;
}
```

- `std::ostream& os` : référence au flux de sortie (par exemple `std::cout`), non `const` puisqu'on écrit dedans (voir [[Flux d'entrée-sortie (C++)]]).
- `const Point& p` : référence constante à l'objet affiché, qu'on ne fait que lire (voir [[Référence (C++)]]).
- `friend` : l'opérateur est appelé sur `std::cout`, extérieur à `Point`, et on ne peut pas ajouter de méthode à `std::ostream` ; il est donc écrit hors des classes, et `friend` lui donne accès aux attributs privés (voir [[Fonction amie (friend)]]).
- `return os;` permet d'enchaîner les `<<` (complément, hors du cours).

En Python, le même mécanisme passe par les [[Méthode spéciale Python|méthodes spéciales]] (`__add__` pour `+`).

Notion parente : [[Classe et objet]]. Voir aussi : [[Programmation orientée objet]].

Résumés : [[4 - C++]]
