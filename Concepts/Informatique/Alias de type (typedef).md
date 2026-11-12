---
type: concept
tags: [year4]
aliases: [typedef, mot-clé typedef, type alias, déclaration using (alias de type)]
sources: ["[[Raw/Year 4/C／C++/programmes C/td_liste_chainees/ex1.c|ex1.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : en [[Langage C|C]] et en [[Langage C++|C++]], le [[Mot réservé|mot réservé]] `typedef` donne un nouveau nom, un **alias**, à un type existant. Il ne crée pas de type distinct : l'alias et le type d'origine sont interchangeables partout.

```c
typedef unsigned int uint;           // uint est un autre nom de unsigned int
typedef struct Chainon {
    int valeur;
    struct Chainon *suivant;         // l'alias n'existe pas encore ici
} Chainon;                           // Chainon = struct Chainon
```

Sans l'alias, il faut écrire `struct Chainon` à chaque usage, le nom d'une [[Structure (struct)|structure]] C vivant dans un espace de noms séparé des autres identificateurs. L'alias n'est connu qu'**après** la fin de la déclaration : dans une structure autoréférente comme celle d'une [[Liste chaînée|liste chaînée]], le champ `suivant` s'écrit donc encore `struct Chainon *`. Pour la même raison, une fonction dont le prototype emploie `Chainon` doit être déclarée après le `typedef` ([[Déclaration et définition]]).

Usages courants : raccourcir un type long ou un [[Pointeur et adresse mémoire|pointeur]] de fonction, masquer un détail de représentation (`size_t`, `uint32_t` de `<stdint.h>` sont des `typedef` de la [[Bibliothèque standard du C|bibliothèque standard du C]]), faciliter un changement de type ultérieur (`typedef double reel;`).

En C++, le nom d'une `struct` ou d'une `class` s'emploie directement sans le mot `struct`, ce qui rend ce `typedef` inutile. Depuis la [[Norme du C++|norme]] C++11, la déclaration `using` est la forme moderne de l'alias, plus lisible et utilisable avec les modèles (*templates*) :

```cpp
using Entier = int;               // équivaut à typedef int Entier;
using Liste = std::vector<int>;
```

## Dans le cours

- [[td listes chaînées]] : `typedef struct Chainon {…} Chainon;` définit le type des chaînons ; dans `ex1.c`, le prototype `void creerListe(Chainon **ptrpremier);` placé avant ce `typedef` empêchait le programme de compiler (`unknown type name 'Chainon'`).
- [[1 - basiques]] : `typedef` figure dans la liste des mots réservés du C, parmi les « constructeurs vus plus tard ».

Voir aussi : [[Structure (struct)]], [[Mot réservé]], [[Type primitif]].
