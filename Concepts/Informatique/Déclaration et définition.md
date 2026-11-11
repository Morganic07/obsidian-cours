---
type: concept
tags: [year4]
aliases: [prototype de fonction, function prototype, déclaration anticipée, forward declaration]
matieres: [C++]
sources: ["[[Raw/Year 4/C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[5 - Compilation séparée]]) : en C++, le [[Fichier d'en-tête|fichier d'en-tête]] `.h` **déclare** ce qui existe (classes, attributs, prototypes des méthodes) ; le [[Fichier source|fichier source]] `.cpp` **définit** le code des méthodes.

```cpp
// Point.h
Point(int a, int b);            // déclaration (prototype)

// Point.cpp
Point::Point(int a, int b) {    // définition
    x = a;
    y = b;
}
```

## Compléments (hors du cours)

- Une **déclaration** annonce un nom et son type, pour que le compilateur puisse vérifier les appels ; une **définition** fournit le corps de la fonction, ou réserve la mémoire d'une variable. Toute définition est aussi une déclaration.
- Un **prototype** est la déclaration d'une fonction sans son corps : type de retour, nom, types des paramètres, suivi de `;`. Les noms des paramètres y sont facultatifs (`int max(int, int);`).
- On peut déclarer autant de fois qu'on veut, mais définir **une seule fois** dans tout le programme : c'est la [[Règle de la définition unique|règle de la définition unique]]. Une fonction déclarée mais jamais définie passe la compilation et échoue à l'[[Édition de liens|édition de liens]] (`undefined reference`).
- La **déclaration anticipée** `class Point;` suffit quand un fichier ne manipule que des pointeurs ou des références vers `Point` : elle évite d'inclure tout l'en-tête.
- En [[Langage C|C]], une fonction appelée avant sa déclaration est une erreur depuis C99 ; d'où l'habitude de placer les prototypes en tête de fichier ou dans un `.h`.

Voir aussi : [[Interface et implémentation]], [[Fonction et procédure]], [[Compilation séparée]].

## Dans [[4 - Cours complet]]

La déclaration d'une fonction est l'instruction qui l'annonce au compilateur ; la forme recommandée est le prototype (type de retour et signature, noms des paramètres facultatifs), et la définition y ajoute le corps. Une instruction qui définit une variable est une définition : elle réserve la mémoire.

Résumés : [[5 - Compilation séparée]], [[4 - Cours complet]]
