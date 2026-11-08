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

## Compléments (hors du cours)

- **Un opérateur surchargé est un appel de fonction** : `-p1` devient `p1.operator-()`, et `p1 + p2` devient `p1.operator+(p2)` : c'est l'objet de gauche qui porte la méthode.
- **Règles** : on ne peut pas inventer d'opérateur (`**` n'existe pas en C++), ni changer son nombre d'opérandes, sa priorité ou son associativité, ni redéfinir un opérateur entre types de base (`int + int`) ; au moins un opérande doit être d'un type défini par l'utilisateur. `::`, `.`, `?:` et `sizeof` ne se surchargent pas.
- **Forme usuelle de l'addition** : `Point operator+(const Point& autre) const;` : la [[Référence (C++)|référence constante]] évite une copie, et le `const` final indique que l'objet de gauche n'est pas modifié.
- **`operator+=`** modifie l'objet de gauche et renvoie une référence sur lui :

```cpp
Point& operator+=(const Point& autre) {
    x += autre.x;
    y += autre.y;
    return *this;
}
```

- **`operator<<` renvoie `std::ostream&`** parce qu'un flux ne se copie pas, et pour permettre l'enchaînement : `std::cout << p1 << p2` se lit `(std::cout << p1) << p2`, le premier appel renvoyant `std::cout` lui-même.
- **`operator=`** (affectation) est généré par le compilateur s'il n'est pas écrit ; il faut l'écrire soi-même dans une classe qui gère de la mémoire dynamique (règle de trois, voir [[Destructeur (programmation)]]).

En Python, le même mécanisme passe par les [[Méthode spéciale Python|méthodes spéciales]] (`__add__` pour `+`).

Notion parente : [[Classe et objet]]. Voir aussi : [[Programmation orientée objet]].

Résumés : [[4 - C++]]
