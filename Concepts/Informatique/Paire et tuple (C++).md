---
type: concept
tags: [year4]
aliases: ["std::pair", "std::tuple", tuple (C++), liaison structurée, structured binding]
sources: ["[[Raw/Year 4/C／C++/programmes C++/formation/10-SurchargeOpérateurs1.cpp|10-SurchargeOpérateurs1.cpp]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : la [[Bibliothèque standard du C++|bibliothèque standard du C++]] fournit deux types génériques pour regrouper des valeurs, éventuellement de types différents, sans écrire de [[Structure (struct)|structure]] :

- `std::pair<T1, T2>` (en-tête `<utility>`) regroupe **deux** valeurs, accessibles par les attributs `.first` et `.second` ;
- `std::tuple<T1, T2, …>` (en-tête `<tuple>`, depuis C++11) en regroupe un nombre quelconque, accessibles par `std::get<i>(t)`, où l'indice `i` doit être connu à la compilation.

Leur usage le plus courant est de **renvoyer plusieurs valeurs** d'une fonction, qui ne peut en renvoyer qu'une ([[Instruction return]]). Depuis C++17, une **liaison structurée** décompose le résultat en variables nommées :

```cpp
#include <utility>
std::pair<int, int> getCoord() { return {x, y}; }

auto [a, b] = p.getCoord();            // a = x, b = y (C++17)
std::pair<int, int> c = p.getCoord();
std::cout << c.first << ", " << c.second;

std::tuple<std::string, int, double> t = {"Alice", 20, 15.5};
std::cout << std::get<1>(t);           // 20
```

`std::make_pair` et `std::make_tuple` les construisent en déduisant les types ; les comparaisons `==` et `<` sont définies (ordre lexicographique). `std::pair` est aussi le type des éléments de `std::map` (clé et valeur, voir [[Tableau associatif]]).

Ils sont pratiques pour des regroupements ponctuels, mais `.first`, `.second` ou `std::get<2>` ne disent rien du sens des valeurs : dès qu'un regroupement revient souvent, une structure ou une [[Classe et objet|classe]] aux attributs nommés (`Point` avec `x` et `y`) est plus lisible ([[Maintenabilité]]). Le tuple de [[Langage Python|Python]] joue le même rôle (`return x, y`), mais en C++ cette écriture invoque l'[[Opérateur virgule|opérateur virgule]].

## Dans le cours

- [[formation C++]] : alternative à `return x, y;` pour renvoyer les deux coordonnées d'un `Point` (programme 10), avec `std::pair<int,int>` et une liaison structurée.

Voir aussi : [[Opérateur virgule]], [[Instruction return]], [[Mot-clé auto]], [[Classe vector (C++)]].
