---
type: concept
tags: [year4]
aliases: [array decay, array-to-pointer decay, décroissance en pointeur, conversion tableau-pointeur]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp7/7.1.c|7.1.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : en [[Langage C|C]] et en [[Langage C++|C++]], une expression de type tableau est convertie implicitement en [[Pointeur et adresse mémoire|pointeur]] vers son premier élément : dans la plupart des expressions, `tab` vaut `&tab[0]`. On parle de « décroissance » (*decay*) parce que le type perd une information, la taille du tableau. La norme C17 (§ 6.3.2.1, al. 3) prévoit trois exceptions : `tab` opérande de l'[[Opérateur sizeof|opérateur `sizeof`]], opérande de l'[[Opérateur d'adresse|opérateur `&`]], ou chaîne littérale qui initialise un tableau.

Conséquences pour les fonctions :

- un tableau n'est **jamais copié** lors d'un appel : la fonction reçoit l'adresse de la première case, et peut donc modifier le tableau d'origine (contrairement au [[Passage par valeur|passage par valeur]] d'un `int`) ;
- un paramètre déclaré `int t[]` ou même `int t[10]` est en réalité un `int *t` : les trois écritures sont équivalentes ;
- la fonction ne connaît pas la taille du tableau. `sizeof(t)` y donne la taille d'un pointeur (8 octets en 64 bits), pas celle du tableau ; il faut passer la taille en paramètre supplémentaire.

```c
void affiche(int t[], int n) {       // t est un int*
    for (int i = 0; i < n; i++)
        printf("%d ", t[i]);         // t[i] équivaut à *(t + i)
}
int tab[5] = {1, 2, 3, 4, 5};
affiche(tab, 5);                     // tab décroît en &tab[0]
// sizeof(tab) vaut 20 ici, mais sizeof(t) vaut 8 dans affiche
```

C'est aussi ce qui fonde l'[[Arithmétique des pointeurs|arithmétique des pointeurs]] : `tab[i]` est défini comme `*(tab + i)`. Une taille transmise plus grande que le tableau fait écrire au-delà de sa fin, sans contrôle ([[Dépassement de tampon]]). En C++, `std::vector` ([[Classe vector (C++)]]) et `std::array` ne décroissent pas et connaissent leur taille.

## Dans le cours

- [[tp7]] : `print_tab(tab)` s'écrit sans crochets ni `&` ; la fonction reçoit l'adresse de la première case et la taille en paramètre.
- [[tableaux]] : `init_tab(tab)` remplit le tableau d'origine, parce que la fonction reçoit `&tab[0]`.
- [[3 - pointeurs , tableaux, listes chainées, structures]] : le § 7 (fonctions et tableaux) emploie déjà la notion dans ses commentaires.
- [[2 - structures code]] : `sizeof(tab) / sizeof(tab[0])` ne donne le nombre de cases que là où le tableau est déclaré, pas dans une fonction qui le reçoit.

Voir aussi : [[Tableau (programmation)]], [[Arithmétique des pointeurs]], [[Passage de paramètres]].
