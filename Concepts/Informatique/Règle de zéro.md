---
type: concept
tags: [year4]
aliases: [rule of zero, règle du zéro, règle de cinq, rule of five]
sources: ["[[Raw/Year 4/C／C++/programmes C++/exo-prof/classeSegment.cpp|classeSegment.cpp]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : la règle de zéro est un principe de conception en [[Langage C++|C++]], formulé sous ce nom par R. Martinho Fernandes en 2012 : une classe qui ne gère pas directement une ressource (mémoire allouée par `new`, fichier, verrou) ne déclare **aucune** des opérations spéciales de copie, de déplacement et de destruction. Elle laisse le compilateur les générer, et elles font alors la bonne chose membre par membre.

Elle s'inscrit dans une suite de règles :

- **règle de trois** (C++98) : si une classe doit écrire son [[Destructeur (programmation)|destructeur]], son [[Constructeur (programmation)|constructeur par copie]] ou son [[Opérateur d'affectation par copie|opérateur d'affectation par copie]], elle doit en général écrire les trois ([[Copie superficielle et copie profonde]]) ;
- **règle de cinq** (C++11) : on y ajoute le constructeur par déplacement et l'affectation par déplacement ;
- **règle de zéro** : mieux vaut n'en écrire aucun, en confiant chaque ressource à une classe dédiée qui sait la copier et la libérer, la classe métier se contentant de la contenir ([[Composition (programmation)]]).

```cpp
// Au lieu de gérer un int* avec new/delete et cinq fonctions spéciales :
class Releve {
    std::string lieu;            // se copie et se libère tout seul
    std::vector<double> mesures; // idem
};                               // aucune fonction spéciale à écrire
```

Les classes dédiées de la [[Bibliothèque standard du C++|bibliothèque standard]] sont `std::string` ([[Classe string (C++)]]), `std::vector` ([[Classe vector (C++)]]) et les autres conteneurs, et les pointeurs intelligents `std::unique_ptr` et `std::shared_ptr`. Le principe sous-jacent, l'acquisition de ressource lors de l'initialisation (RAII), lie la vie d'une ressource à celle d'un objet. Écrire une fonction spéciale identique à celle que générerait le compilateur est au mieux inutile, au pire nuisible : déclarer un constructeur par copie rend dépréciée la génération de l'opérateur d'affectation (avertissement `-Wdeprecated-copy` de [[GCC]]) et supprime celle des opérations de déplacement. Si l'on tient à les rendre visibles, on écrit `= default`.

## Dans le cours

- [[exo-prof]] : le constructeur par copie de `Point`, identique à celui que génère le compilateur, peut être supprimé ; l'avertissement `-Wdeprecated-copy` disparaît alors.
- [[formation C++]] : la fiche conseille `std::vector` ou `std::string` plutôt qu'une copie profonde écrite à la main.

Voir aussi : [[Destructeur (programmation)]], [[Copie superficielle et copie profonde]], [[Opérateur d'affectation par copie]], [[Allocation dynamique]].
