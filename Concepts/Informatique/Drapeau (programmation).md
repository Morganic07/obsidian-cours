---
type: concept
tags: [year4]
aliases: [variable drapeau, drapeau booléen, flag (variable), indicateur booléen]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp5/5.4.c|5.4.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : un drapeau (*flag*) est une [[Variable (programmation)|variable]], le plus souvent [[Booléen|booléenne]], qui mémorise qu'un événement s'est produit au cours d'un traitement : « un diviseur a été trouvé », « le tableau est trié », « la saisie est valide ». Son emploi suit toujours trois temps :

1. l'[[Initialisation (programmation)|initialiser]] à la valeur « pas encore arrivé » ;
2. le **basculer** quand l'événement survient, en général dans une [[Boucle (programmation)|boucle]] ;
3. le **tester** ensuite, ou dans la condition de la boucle pour l'arrêter plus tôt.

```c
#include <stdbool.h>
bool est_premier = true;                 // 1. hypothèse de départ
for (int i = 2; i * i <= n && est_premier; i++)
    if (n % i == 0)
        est_premier = false;             // 2. un diviseur : on baisse le drapeau
if (est_premier && n >= 2)               // 3. test final
    printf("%d est premier\n", n);
```

En [[Langage C|C]] avant C99, un drapeau est un `int` qui vaut 0 ou 1 ; depuis C99, on dispose du type `bool` de `<stdbool.h>` (mot-clé natif en C23 et en [[Langage C++|C++]]).

Le drapeau complète l'[[Accumulateur (programmation)|accumulateur]] et le [[Compteur (programmation)|compteur]] : il ne garde qu'un oui ou non. Dans des [[Boucle imbriquée|boucles imbriquées]], un drapeau propre à la boucle interne doit être remis à sa valeur initiale à chaque tour de la boucle externe ; le plus sûr est de le déclarer dans le corps de la boucle externe ([[Portée d'une variable]]). Il sert aussi à savoir après coup pourquoi une boucle s'est arrêtée quand on en sort par `break` ([[Instructions break et continue]]).

Le mot a un autre sens, voisin : un « drapeau » est aussi un bit d'un [[Registre du processeur|registre d'état]] du [[Processeur|processeur]] (retenue, zéro, signe) ou d'un masque d'options manipulé par les [[Opérateur bit à bit|opérateurs bit à bit]].

## Dans le cours

- [[tp5]] : `est_premier` (programmes 5.4 et 5.6) passe à 0 au premier diviseur trouvé ; en 5.6, il doit être remis à 1 pour chaque nouveau nombre testé.
- [[tp4]] : la fiche conseille de garder un drapeau pour savoir, après un `break`, si le nombre secret a été trouvé.

Voir aussi : [[Booléen]], [[Valeur sentinelle]], [[Structure conditionnelle]].
