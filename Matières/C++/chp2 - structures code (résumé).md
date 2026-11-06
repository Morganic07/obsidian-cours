---
type: source
tags: [year4]
sources: ["[[chp2 - structures code]]"]
maj: 2026-11-05
---

Résumé de [[chp2 - structures code]], dans [[C++ (matière)]]. Le code est du C. En cas d'écart, le cours et ses images font foi.

## Idée générale

Les structures de contrôle, les fonctions et les tableaux.

## Contenu, dans l'ordre du cours

- **Opérateurs** : `==`, `!=`, `>`, `>=`, `<`, `<=`, `&&`, `||`, `!` et `^` (donné comme XOR logique).
- **`if ... else if ... else`** et **`switch ... case`** : une fois un `case` atteint, les suivants s'exécutent aussi jusqu'à un `break`, qu'il ne faut donc pas oublier.
- **`for (initialisation ; condition ; incrémentation)`** : l'initialisation a lieu une fois avant la boucle, la condition avant chaque tour, l'incrémentation après chaque tour. Avec `i = 0`, `i < 10`, `i = i + 1`, la boucle fait 10 tours, `i` prend les valeurs de 0 à 9 et vaut 10 en sortie. Les accolades sont facultatives pour une seule instruction.
- **`do ... while (condition);`** : le bloc s'exécute au moins une fois, le `;` final est obligatoire. **`while`** : le bloc peut ne jamais s'exécuter.
- **Fonctions** : déclaration `float moyenne (int a, int b);` (type de retour, nom, paramètres). Règles : déclarer avant d'appeler, implémenter toutes les fonctions, signatures identiques à la déclaration et à l'implémentation, types respectés à l'appel.
- **Structure d'un programme** : `#include`, déclarations, `main`, implémentations. Une procédure est une fonction qui ne renvoie rien (type `void`) ; toute procédure est de type `void`, mais le cours précise que tout `void` n'est pas forcément une procédure.
- **Passage des arguments** : par copie. Une variable simple passée à une fonction n'est pas modifiée dans `main`. Pour la modifier, on passe un pointeur (voir [[Pointeur et adresse mémoire]]). Un tableau est converti en l'adresse de son premier élément : `float *t`, `float t[]` et `float t[100]` sont équivalents, la taille 100 est ignorée ; `float t` n'est pas équivalent.
- **Tableaux** : type, nom, taille : `int tab[10];`. Les indices vont de 0 à taille − 1, les éléments ne sont pas initialisés à zéro. Tous les éléments ont le même type.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Images lues par leur transcription, aucune ouverte.

1. **`^` « XOR logique »** (complément) : en C, `^` est un OU exclusif bit à bit, il n'existe pas de XOR logique.
2. **Taille du tableau « écrite en dur »** (complément) : le cours interdit `int n; int tab[n];`. En C99, un tableau de taille variable est permis si `n` a une valeur. L'exemple du cours est de toute façon incorrect, `n` n'étant pas initialisé.
3. **Fonction `affiche_points`** : `i` et `j` ne sont pas déclarés dans le code de l'image. Alerte des transcriptions confirmée par le texte.
4. **Haut de plusieurs images coupé** (tableau des opérateurs, `if/else`) : une ligne de texte n'est pas lisible, sans conséquence sur le contenu.
5. **Remarque sur le `for`** : le passage surligné dans l'image dit que `i` vaut 10 après la boucle. Cette remarque est juste.
