---
type: concept
tags: [year4]
aliases: ["std::list", "std::forward_list", forward_list, liste chaînée de la STL]
sources: ["[[Raw/Year 4/C／C++/programmes C/td_liste_chainees/tous_les_exo.c|tous_les_exo.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : la [[Bibliothèque standard du C++|bibliothèque standard du C++]] fournit deux [[Conteneur (informatique)|conteneurs]] qui réalisent des [[Liste chaînée|listes chaînées]] :

- `std::list<T>` (en-tête `<list>`) : liste **doublement** chaînée, chaque nœud connaissant son précédent et son suivant ; on la parcourt dans les deux sens ;
- `std::forward_list<T>` (en-tête `<forward_list>`, depuis C++11) : liste **simplement** chaînée, plus économe en mémoire, comme celles qu'on écrit à la main en [[Langage C|C]].

```cpp
#include <list>
#include <iostream>

std::list<int> l = {3, 5, 7};
l.push_front(1);              // ajout en tête : 1 3 5 7
l.push_back(9);               // ajout en queue : 1 3 5 7 9
l.remove(5);                  // supprime toutes les valeurs 5
for (int v : l) std::cout << v << ' ';
```

Comme toute liste chaînée, elles offrent l'insertion et la suppression en $O(1)$ à une position déjà atteinte, mais l'accès au $i$-ième élément coûte $O(n)$ : il n'y a pas d'opérateur `[]`. Les nœuds sont alloués et libérés par le conteneur lui-même (son [[Destructeur (programmation)|destructeur]] libère tout), ce qui supprime les [[Fuite mémoire|fuites mémoire]] et les [[Pointeur pendant|pointeurs pendants]] des listes écrites à la main.

En pratique, la [[Classe vector (C++)|classe `std::vector`]] est presque toujours plus rapide, même pour des insertions, parce que ses éléments sont contigus en mémoire et profitent de la [[Mémoire cache|mémoire cache]] du processeur ; `std::list` se justifie quand on insère ou retire souvent au milieu d'une longue séquence en gardant des itérateurs valides.

## Dans le cours

- [[td listes chaînées]] : alternative standard aux listes écrites à la main en C avec `malloc`, `free` et des [[Double pointeur|doubles pointeurs]] ; hors exercice, on ne programme plus de liste chaînée soi-même en C++.

Voir aussi : [[Liste chaînée]], [[Classe vector (C++)]], [[Structure de données]], [[Pile et file]].
