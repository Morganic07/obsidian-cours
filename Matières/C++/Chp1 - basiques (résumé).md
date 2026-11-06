---
type: source
tags: [year4]
sources: ["[[Chp1 - basiques]]"]
maj: 2026-11-05
---

Résumé de [[Chp1 - basiques]], dans [[C++ (matière)]]. Le contenu est du langage C (mots réservés du C, `printf`, `scanf`, `malloc`), pas du C++. En cas d'écart, le cours et ses images font foi.

## Idée générale

Syntaxe de base du C, types, mémoire (pile), erreurs de compilation, puis une série de « questions pièges » sur des pièges classiques du langage.

## Contenu, dans l'ordre du cours

- **Syntaxe** : instructions finies par `;`, blocs entre `{}`, indentation, pas d'espace ni de `-` dans un nom, pas de chiffre en première position. Liste des mots réservés par catégorie (types, boucles, sélections, ruptures de séquence, classes d'allocation, constructeurs, divers).
- **Types de base** : `void`, `int` (qualificatifs `short`, `long`, `signed`, `unsigned`), `char` (code ASCII, aussi un entier sur 8 bits), `float`, `double`, `long double`.
- **`printf` et `scanf`** : séquences `%d` ou `%i`, `%u`, `%o`, `%x` ou `%X`, `%f`, `%c`, `%s`. Modificateurs de largeur comme `%3d` et `%03d`.
- **Gestion mémoire** : le type fixe la place à réserver (`char` 1 octet, `int` en général 4, `double` en général 8), la façon d'interpréter les bits (complément à deux, IEEE 754, ASCII) et permet des vérifications à la compilation (typage statique).
- **Variables en pile** : une variable locale va dans la pile (stack), organisée en LIFO. Un appel empile un cadre (variables locales, paramètres, adresse de retour), la fin de la fonction le libère.
- **Erreurs du compilateur** : point-virgule oublié, accolade oubliée, variable non déclarée, `undefined reference` (fonction inconnue), fichier d'en-tête introuvable.
- **`char` est un entier** : `c = 65` et `c = 'A'` sont identiques. `%d` affiche 66, `%c` affiche B pour `char lettre = 66`.
- **Questions pièges** : `a == b == c` ; accolades facultatives pour une seule instruction ; `if (a = 3)` ; `if (x == 5);` ; `||` paresseux, voir [[Évaluation en court-circuit]] ; variable non initialisée ; `while (x < 10);` boucle infinie.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Seules les transcriptions ont été lues (aucune image ouverte).

1. **`if (a=3)`** (complément). **À corriger avant un examen.** Le cours explique que le test « regarde si `a` peut prendre la valeur 3 ». C'est faux : l'affectation met 3 dans `a`, et la valeur de l'expression est 3, donc non nulle et vraie. La condition est donc toujours vraie, et c'est pour cela que « bonjour » s'affiche.
2. **Remplacement de `a == b == c`** (complément). **À corriger avant un examen.** Le cours propose `if (a == b && b == c)` (juste) puis `if (((a==b) == 1) == (b==c))`. La seconde n'est pas équivalente : elle est aussi vraie quand `a != b` et `b != c`, puisque `0 == 0`.
3. **`int resultat = total + texte;`** (complément) : le cours dit que l'addition d'un entier et d'une adresse n'a pas de sens. En C, c'est de l'arithmétique de pointeurs, valide. Le compilateur ne se plaint que de l'affectation d'un pointeur à un `int`. Le cours écrit prudemment « erreur ou avertissement ».
4. **`if (x == 5);` puis `{ printf("A"); }`** : le cours écrit que « le if ne s'exécute pas ». La phrase est ambiguë : le `;` forme une instruction vide, donc le bloc suivant s'exécute toujours. Le résultat annoncé, « AB », est juste.
5. **`while (x < 10); x++;`** : l'explication est juste (la boucle n'a que l'instruction vide).
6. **`char` signé ou non** : le cours écrit que `char` peut être déclaré en signé (`char`) ou non (`unsigned char`). Le signe d'un `char` seul dépend de l'implémentation (complément).
7. **Variable non initialisée** : « valeur aléatoire » dans le cours ; en toute rigueur, valeur indéterminée.
8. **Sections vides** : le document contient quelques titres sans contenu, et une section « 2. Le type char » qui reprend un passage numéroté sans la partie 1.
