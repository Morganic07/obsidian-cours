---
type: concept
tags: [year4]
aliases: [inline, fonction en ligne, inline function, mot-clé inline]
matieres: [C++]
sources: ["[[Raw/Year 4/C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition (complément, hors du cours)** : en [[Langage C++|C++]], une fonction déclarée `inline` peut être **définie dans plusieurs unités de compilation**, à condition que toutes les définitions soient identiques : c'est l'exception à la [[Règle de la définition unique|règle de la définition unique]] qui permet d'écrire une fonction entière dans un [[Fichier d'en-tête|fichier d'en-tête]]. Les méthodes définies dans le corps de la classe sont implicitement `inline`.

```cpp
// Point.h
class Point {
    int x;
public:
    int getX() const { return x; }   // implicitement inline
};
inline int carre(int n) { return n * n; }   // fonction libre dans un .h
```

Le mot évoque à l'origine une demande d'**intégration** : remplacer l'appel par le corps de la fonction pour éviter le coût de l'[[Appel de fonction|appel]]. Les compilateurs actuels décident seuls de cette optimisation ; `inline` sert aujourd'hui surtout à autoriser la définition multiple.

## Dans le cours

Pas nommé : la notion apparaît dans les compléments de [[5 - Compilation séparée]], qui explique pourquoi un `.h` ne contient que des déclarations.

Voir aussi : [[Accesseur et mutateur]], [[Classe et objet]].

Résumés : [[5 - Compilation séparée]]
