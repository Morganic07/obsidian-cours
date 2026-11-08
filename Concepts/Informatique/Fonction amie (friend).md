---
type: concept
tags: [year4]
aliases: [friend, fonction friend, fonction amie]
sources: ["[[Raw/Year 4/C++/chp4 C++.pdf|chp4 C++.pdf]]"]
maj: 2026-11-08
---

**Définition** (d'après [[4 - C++]]) : le mot-clé `friend`, placé devant une fonction déclarée dans une classe, permet à cette fonction, qui **n'est pas une méthode de la classe**, d'**accéder à ses membres privés**.

Cas du cours, l'opérateur d'affichage `operator<<` de la classe `Point` (voir [[Surcharge d'opérateurs]]) :
1. `std::cout` est externe à `Point` : l'opérateur est appelé sur le flux, qui n'appartient pas à la classe ;
2. on ne peut pas ajouter de méthode à `std::ostream` : `operator<<` est donc écrit en dehors des classes.

| Sans `friend` | Avec `friend` |
|---|---|
| `operator<<` ne peut pas accéder à `x` et `y`, car ils sont privés | `operator<<` accède aux membres privés de `Point` |

Notion parente : [[Encapsulation (programmation)]]. Voir aussi : [[Classe et objet]], [[Flux d'entrée-sortie (C++)]].

Résumés : [[4 - C++]]
