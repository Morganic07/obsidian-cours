---
type: source
tags: [year4]
sources:
  - "[[Raw/Year 4/C／C++/programmes C/pointeurs/test_parametre_par_ref.c|test_parametre_par_ref.c]]"
maj: 2026-11-12
complet: true
enrichi: 2026-11-12
---

Un programme de [[Langage C|C]] (dossier `programmes C/pointeurs`), dans [[Cours/Informatique/C++/_index|C++]] : la version « par adresse » de la fonction `echange` du § 6 de [[3 - pointeurs , tableaux, listes chainées, structures]] (« Fonctions : paramètres par valeur, puis par adresse »), qui répond au problème posé au § 7 de [[2 - structures code]] : une fonction ne peut pas modifier une variable de `main` qu'elle reçoit par copie ([[Passage par valeur|passage par valeur]]). Le fichier compile sans avertissement avec [[GCC|`gcc`]] `-std=c17 -Wall -Wextra`.

## test_parametre_par_ref.c

D'après le code, l'exercice demande d'écrire une fonction `echange` qui permute les valeurs de deux variables de `main`, en lui passant leurs adresses, et d'afficher les valeurs avant, pendant et après l'appel.

```c
#include <stdio.h>

void echange(int *a, int *b);

int main(){
    int var1 = 10;
    int var2=20;
    printf("var1 : %d, var2 : %d \n", var1, var2);
    echange(&var1, &var2);
    printf("var 1 : %d , var2 : %d \n",var1, var2 );

    return 0;
}

void echange(int *a, int *b){
    int temp;

    printf("a : %d , b : %d\n", *a, *b);
    temp = *a;
    *a=*b;
    *b=temp;
    printf("a : %d, b : %d \n", *a, *b);
}
```

Sortie :

```text
var1 : 10, var2 : 20
a : 10 , b : 20
a : 20, b : 10
var 1 : 20 , var2 : 10
```

Explications :

- **Paramètres `int *a, int *b`** : `echange` reçoit deux [[Pointeur et adresse mémoire|pointeurs]] sur `int`, c'est-à-dire deux adresses.
- **Appel `echange(&var1, &var2)`** : l'[[Opérateur d'adresse|opérateur d'adresse]] `&` fournit l'adresse de `var1` et celle de `var2`.
- **`*a`, `*b`** : le [[Déréférencement|déréférencement]] accède à la valeur rangée à l'adresse ; `*a` **est** `var1` pendant l'appel. Écrire dans `*a` écrit donc dans `var1`.
- **Trois affectations** : `temp = *a; *a = *b; *b = temp;` est l'[[Échange de deux variables|échange de deux variables]] classique, avec une variable temporaire qui garde l'ancienne valeur de `*a` avant qu'elle soit écrasée.
- **Effet visible dans `main`** : la dernière ligne affiche `20` et `10`. Avec la version par valeur `echange(int a, int b)`, les deux `printf` de `echange` seraient les mêmes, mais `main` afficherait encore `10` et `20` : seules les copies auraient été échangées, dans le cadre de `echange` sur la [[Pile d'exécution|pile d'exécution]].

Le nom du fichier parle de passage « par référence » : en C, il n'existe que le [[Passage de paramètres|passage]] par valeur, et ce sont ici les adresses qui sont copiées dans `a` et `b`. On parle de passage par adresse (ou par pointeur). Le vrai passage par référence est celui du [[Langage C++|C++]] : `void echange(int &a, int &b)`, appelé `echange(var1, var2)`, sans `&` ni `*` (voir [[Référence (C++)]]) ; la [[Bibliothèque standard du C++|bibliothèque standard]] fournit `std::swap`. [[Complément hors du cours|ⓘ]]

Appeler `echange(NULL, &var2)` déréférencerait le [[Pointeur NULL|pointeur nul]] : [[Comportement indéfini|comportement indéfini]], en pratique une [[Erreur de segmentation|erreur de segmentation]]. Une fonction qui reçoit des pointeurs suppose qu'ils désignent des variables valides ; c'est à l'appelant de le garantir, ou à la fonction de le tester (`if (a == NULL || b == NULL) return;`). Le même mécanisme sert à toute fonction qui doit « renvoyer » plusieurs résultats : `scanf("%d", &x)` reçoit l'adresse de `x` pour la même raison ([[Fonctions printf et scanf]]). [[Complément hors du cours|ⓘ]]

## À retenir

- Pour qu'une fonction modifie une variable de l'appelant, on lui passe l'**adresse** (`&x`) et elle travaille sur `*p`.
- `int *a` dans la signature déclare un pointeur ; `*a` dans le corps désigne la valeur pointée.
- Un échange demande une variable temporaire : `temp = *a; *a = *b; *b = temp;`.
- En C, tout est passé par valeur : « par adresse » signifie qu'on copie une adresse ; la référence est une notion du C++. [[Complément hors du cours|ⓘ]]
