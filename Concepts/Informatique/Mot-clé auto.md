---
type: concept
tags: [year4]
aliases: [auto (C++), inférence de type, type inference, déduction de type]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : depuis C++11, `auto` à la place d'un type demande au compilateur de **déduire** le type de la variable de son initialisation : `auto n = 25;` déclare un `int`, `auto x = 2.5;` un `double`. Le [[Typage statique|typage]] reste statique : le type est fixé une fois pour toutes à la compilation. On le réserve aux cas où le type est évident ou très long (itérateurs). En C et en C++98, `auto` désignait une classe de stockage (variable locale automatique), inutile en pratique (voir [[Mot réservé]]).

## Dans le cours

Absent de [[4 - Cours complet]] (C++98) ; ajouté au récapitulatif des évolutions du C++ moderne. Le diaporama [[4 - C++]] le mentionne aussi en complément.

Résumés : [[4 - Cours complet]]
