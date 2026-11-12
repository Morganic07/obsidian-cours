---
type: concept
tags: [year4]
aliases: [copie superficielle, copie profonde, shallow copy, deep copy, copie membre à membre]
sources: ["[[Raw/Year 4/C／C++/programmes C++/formation/7-constructeurCopie.cpp|7-constructeurCopie.cpp]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : copier un objet peut se faire de deux façons.

- Une **copie superficielle** (*shallow copy*) recopie les attributs un par un, tels quels. Si l'un d'eux est un [[Pointeur et adresse mémoire|pointeur]], la copie reçoit la même adresse que l'original : les deux objets désignent alors **la même** zone mémoire.
- Une **copie profonde** (*deep copy*) alloue une nouvelle zone pour la copie et y recopie le contenu pointé : les deux objets sont indépendants, modifier l'un ne touche pas l'autre.

Pour des attributs simples (`int`, `double`) ou des objets qui se copient eux-mêmes correctement, les deux coïncident. La différence n'apparaît qu'avec des pointeurs vers de la mémoire obtenue par [[Allocation dynamique|allocation dynamique]].

En [[Langage C++|C++]], le [[Constructeur (programmation)|constructeur par copie]] et l'[[Opérateur d'affectation par copie|opérateur d'affectation par copie]] que génère le compilateur copient **membre à membre**, donc superficiellement pour un pointeur brut. Pour une classe qui possède un bloc alloué par `new`, c'est une erreur :

```cpp
class Tableau {
    int* donnees; int n;
public:
    Tableau(int n) : donnees(new int[n]), n(n) {}
    ~Tableau() { delete[] donnees; }
    // copie profonde : nouvelle zone, contenu recopié
    Tableau(const Tableau& autre) : donnees(new int[autre.n]), n(autre.n) {
        for (int i = 0; i < n; i++) donnees[i] = autre.donnees[i];
    }
};
```

Sans ce constructeur par copie, `Tableau b = a;` ferait pointer `a` et `b` sur le même bloc : une écriture dans `b` modifierait `a`, et les deux [[Destructeur (programmation)|destructeurs]] libéreraient le bloc deux fois (double libération, [[Comportement indéfini|comportement indéfini]], voir [[Pointeur pendant]]). C'est l'origine de la **règle de trois** : une classe qui doit écrire son destructeur, son constructeur par copie ou son opérateur d'affectation doit en général écrire les trois.

La solution moderne est de ne pas gérer la mémoire à la main : des membres `std::vector` ([[Classe vector (C++)]]) ou `std::string` ([[Classe string (C++)]]) font eux-mêmes une copie profonde, et la copie générée par le compilateur devient juste ([[Règle de zéro]]).

En [[Langage Python|Python]], la même distinction existe entre `copy.copy` (superficielle) et `copy.deepcopy` (profonde), et l'affectation `b = a` ne copie rien du tout. En [[Langage C|C]], affecter une [[Structure (struct)|structure]] (`s2 = s1;`) fait une copie superficielle.

## Dans le cours

- [[formation C++]] : `Point p2(p1);` (programme 7) utilise le constructeur de copie implicite, qui copie membre à membre les deux `int` de `Point` ; la fiche explique pourquoi cela ne suffirait plus avec de la mémoire allouée par `new`.
- [[exo-prof]] : le constructeur par copie écrit à la main pour `Point` fait la même copie superficielle que la version générée, suffisante pour des `int`.
- [[4 - C++]] : la section « Copie : fonctionnement et usages » présente le constructeur par copie fourni par le compilateur.

Voir aussi : [[Constructeur (programmation)]], [[Destructeur (programmation)]], [[Opérateur d'affectation par copie]], [[Règle de zéro]].
