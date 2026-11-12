---
type: concept
tags: [year4]
aliases: [friend, fonction friend, fonction amie]
sources: ["[[Raw/Year 4/C／C++/chp4 C++.pdf|chp4 C++.pdf]]"]
maj: 2026-11-12
---

**Définition** (d'après [[4 - C++]]) : le mot-clé `friend`, placé devant une fonction déclarée dans une classe, permet à cette fonction, qui **n'est pas une méthode de la classe**, d'**accéder à ses membres privés**.

Cas du cours, l'opérateur d'affichage `operator<<` de la classe `Point` (voir [[Surcharge d'opérateurs]]) :
1. `std::cout` est externe à `Point` : l'opérateur est appelé sur le flux, qui n'appartient pas à la classe ;
2. on ne peut pas ajouter de méthode à `std::ostream` : `operator<<` est donc écrit en dehors des classes.

| Sans `friend` | Avec `friend` |
|---|---|
| `operator<<` ne peut pas accéder à `x` et `y`, car ils sont privés | `operator<<` accède aux membres privés de `Point` |

Notion parente : [[Encapsulation (programmation)]]. Voir aussi : [[Classe et objet]], [[Flux d'entrée-sortie (C++)]].

## Dans le cours

- [[formation C++]] : `friend std::ostream& operator<<(std::ostream&, const Point&)`, défini dans la classe, lit les attributs privés `x` et `y` pour afficher un `Point` (programme 12).
- [[exo-prof]] : même `operator<<` déclaré `friend` dans `classePoint.cpp` ; il renvoie le flux par [[Référence (C++)|référence]] pour enchaîner `std::cout << p1 << std::endl`.

Résumés : [[4 - C++]]
