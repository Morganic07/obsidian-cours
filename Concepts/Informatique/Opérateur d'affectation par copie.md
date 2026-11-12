---
type: concept
tags: [year4]
aliases: ["operator=", copy assignment operator, affectation par copie, opérateur d'affectation (C++)]
sources: ["[[Raw/Year 4/C／C++/programmes C++/exo-prof/classeSegment.cpp|classeSegment.cpp]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : en [[Langage C++|C++]], l'opérateur d'affectation par copie est la méthode `T& operator=(const T& autre)` d'une classe `T`. Il est appelé par `a = b;` quand `a` **existe déjà**, et remplace le contenu de `a` par une copie de celui de `b`. Il se distingue du [[Constructeur (programmation)|constructeur par copie]], appelé quand un objet **naît** à partir d'un autre :

```cpp
Point p1(1, 2);
Point p2 = p1;     // constructeur par copie (p2 naît) malgré le signe =
Point p3;
p3 = p1;           // opérateur d'affectation par copie (p3 existait)
```

Si la classe ne le déclare pas, le compilateur en génère un qui affecte les attributs un par un, dans leur ordre de déclaration : c'est une [[Copie superficielle et copie profonde|copie superficielle]]. Il renvoie `*this` par [[Référence (C++)|référence]] ([[Pointeur this]]), ce qui permet d'enchaîner `a = b = c;` comme pour les types de base ([[Affectation]]).

Quand l'écrire soi-même : quand la classe gère une ressource (mémoire allouée par `new`, fichier). Il doit alors libérer l'ancienne ressource de `a`, copier en profondeur celle de `b`, et rester juste pour l'auto-affectation `a = a;` :

```cpp
Tableau& operator=(const Tableau& autre) {
    if (this != &autre) {                 // auto-affectation
        int* copie = new int[autre.n];
        std::copy(autre.donnees, autre.donnees + autre.n, copie);
        delete[] donnees;                 // libère l'ancien bloc
        donnees = copie; n = autre.n;
    }
    return *this;
}
```

**Règle de trois** : destructeur, constructeur par copie et opérateur d'affectation par copie vont ensemble ; si l'un a besoin d'un code particulier, les deux autres aussi (voir [[Destructeur (programmation)]]). Depuis C++11, la génération implicite de l'opérateur d'affectation est **dépréciée** quand la classe déclare elle-même un constructeur par copie ou un destructeur ; [[GCC]] le signale par `-Wdeprecated-copy`, activé par `-Wextra` ([[Avertissement de compilation]]). Avec C++11 s'ajoute l'affectation par déplacement `operator=(T&&)`, d'où la « règle de cinq ». Quand rien de tout cela n'est nécessaire, mieux vaut n'en écrire aucun ([[Règle de zéro]]).

C'est un cas particulier de [[Surcharge d'opérateurs|surcharge d'opérateurs]] ; il doit être une méthode de la classe, jamais une fonction libre.

## Dans le cours

- [[exo-prof]] : `A = autreSegment.A;` dans le constructeur par copie de `Segment` appelle l'opérateur d'affectation généré de `Point`, alors que `Point` déclare son propre constructeur par copie : GCC signale deux fois `-Wdeprecated-copy`. La fiche conseille la règle de zéro.
- [[compilation séparée (C++)]] : le même avertissement réapparaît dans la version en plusieurs fichiers.

Voir aussi : [[Constructeur (programmation)]], [[Copie superficielle et copie profonde]], [[Règle de zéro]], [[Surcharge d'opérateurs]].
