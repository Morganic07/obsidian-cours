---
type: concept
tags: [year4]
aliases: [cmath, "<cmath>", math.h, pow, std::pow, fonction pow]
sources: ["[[Raw/Year 4/C／C++/chp4 C++ - cours super complet.pdf|chp4 C++ - cours super complet.pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : en-tête de la [[Bibliothèque standard du C++|bibliothèque standard]] qui déclare les fonctions mathématiques héritées du C (`math.h`) : `pow(x, y)` (puissance), `sqrt` ([[Racine carrée|racine carrée]]), `fabs`, `exp`, `log`, `sin`, `cos`, `floor`, `ceil`, `round`. Elles travaillent sur des [[Nombre à virgule flottante|nombres à virgule flottante]] (`double`). Sous Linux, leur code est dans `libm` ; en C il faut parfois lier avec `-lm`, g++ le fait seul.

## Dans le cours

[[4 - Cours complet]] utilise `pow(i, 2)` pour la table des carrés et décrit l'[[Appel de fonction|appel]] : déclaration `double pow(double x, double y);` dans un [[Fichier d'en-tête|en-tête]], définition dans la bibliothèque `libm.so`, documentation par `man pow`.

Résumés : [[4 - Cours complet]]
