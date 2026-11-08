---
type: concept
tags: [year2]
aliases: [__init__, __str__, méthodes spéciales]
matieres: [Algo]
sources: ["[[Raw/Year 2/Algo/Cours/Chapitre5-ABR.pdf|Chapitre5-ABR.pdf]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : en [[Langage Python|Python]], une méthode spéciale (ou « méthode magique », *dunder method*) est une méthode dont le nom commence et finit par deux tirets bas, et que Python appelle implicitement lors d'une opération du langage. `__init__` est appelée à la création d'un objet pour initialiser ses attributs, `__str__` par `print()` ou `str()` pour obtenir sa représentation textuelle ; d'autres définissent le comportement des opérateurs (`__add__` pour `+`, `__eq__` pour `==`) ou de `len()` (`__len__`). On ne les appelle en général pas directement.

## Dans le cours

Nommé dans Chapitre5-ABR ([[Raw/Year 2/Algo/Cours/Chapitre5-ABR.pdf|Chapitre5-ABR.pdf]]) sans définition : le cours crée la classe `Node` (attributs `data`, `left`, `right`, `parent`) avec les méthodes spéciales `__init__` et `__str__`.

Voir aussi : [[Arbre binaire de recherche]], [[Programmation orientée objet]]. En C++, `__init__` correspond au [[Constructeur (programmation)|constructeur]] et `__add__` à la [[Surcharge d'opérateurs|surcharge]] de `operator+` (complément, hors du cours).

Résumés : [[5 - ABR]]
