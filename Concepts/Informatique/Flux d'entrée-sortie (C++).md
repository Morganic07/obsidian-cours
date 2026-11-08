---
type: concept
tags: [year4]
aliases: [std::cout, cout, std::endl, endl, iostream, ifstream, fstream, ostream, std::ostream, flux de sortie, flux d'entrée]
sources: ["[[Raw/Year 4/C++/chp4 C++.pdf|chp4 C++.pdf]]", "[[Raw/Year 4/C++/chp4 prise de note.pdf|chp4 prise de note.pdf]]"]
maj: 2026-11-08
---

**Définition** (d'après [[4 - C++]]) : `std::cout` (« *console output* ») envoie du texte ou des valeurs vers la **sortie standard**, en général le terminal. L'opérateur `<<` y « insère » plusieurs éléments à la suite ; `std::endl` insère un retour à la ligne (comme `"\n"`). Il faut `#include <iostream>`.

```cpp
int score = 42;
std::cout << "Score : " << score << std::endl;   // Score : 42
```

- Équivalent C : `std::cout << x + y;` fait ce que fait `printf("%d", x + y)` ([[4 - Prise de note]] ; voir [[Fonctions printf et scanf]]). Pas de format à donner : le type de la valeur suffit.
- Pour afficher ses propres objets, on surcharge `<<` : `std::ostream& operator<<(std::ostream& os, const Point& p)` (voir [[Surcharge d'opérateurs]]).

## Lire un fichier

Aide donnée pour l'exercice `Maze` de [[4 - C++]] :

```cpp
#include <fstream>                 // gestion des flux

ifstream f("toto.txt");            // flux d'entrée lié au fichier ; ou ifstream f(maze_name)
f >> _map[i];                      // lit une valeur et la range à l'indice i
f.close();                         // ferme le flux
```

`>>` lit dans un flux d'entrée comme `<<` écrit dans un flux de sortie.

Notion parente : [[Langage C++]]. Voir aussi : [[Espace de noms (namespace)]], [[Opération d'entrée-sortie]], [[Redirection et tube]].

Résumés : [[4 - C++]], [[4 - Prise de note]]
