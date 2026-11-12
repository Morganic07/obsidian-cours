---
type: source
tags: [year4]
sources:
  - "[[Raw/Year 4/C／C++/programmes C/tableaux/tab1.c|tab1.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tableaux/tab2.c|tab2.c]]"
maj: 2026-11-12
complet: true
enrichi: 2026-11-12
---

Deux programmes de [[Langage C|C]] (dossier `programmes C/tableaux`), dans [[Cours/Informatique/C++/_index|C++]]. Ce sont les deux versions du programme du § 7 de [[3 - pointeurs , tableaux, listes chainées, structures]] (« Fonctions et tableaux : deux manières de faire ») : la même paire de [[Fonction et procédure|procédures]], `init_tab` et `affiche_tab`, écrite une fois en syntaxe [[Pointeur et adresse mémoire|pointeur]] (`tab1.c`), une fois en syntaxe [[Tableau (programmation)|tableau]] (`tab2.c`). Le passage des tableaux aux fonctions est introduit au § 7 de [[2 - structures code]] et mis en pratique au TP 7 ([[tp7]]). Les deux fichiers compilent sans avertissement avec [[GCC|`gcc`]] `-std=c17 -Wall -Wextra` et affichent 100 lignes `1.000000`.

## tab1.c

D'après le code, l'exercice demande de remplir un tableau de 100 `float` avec la valeur 1.0 dans une fonction, puis de l'afficher dans une autre, en manipulant le tableau par un pointeur.

```c
#include <stdio.h>

void init_tab(float *t){
    for (int i=0; i<100;i++){
        *(t+i) = 1.0;
    }
}

void affiche_tab(float *t){
    for (int i=0; i<100;i++){
        printf("%f\n", *(t+i));
    }
}

int main(){
    float tab[100];
    init_tab(tab);
    affiche_tab(tab);
}
```

Explications :

- **Paramètre `float *t`** : la fonction reçoit l'**adresse** de la première case du tableau, rangée dans un pointeur sur `float`.
- **Appel `init_tab(tab)`** : le nom du tableau, employé sans crochets, est converti en `&tab[0]` ([[Décroissance d'un tableau en pointeur|décroissance en pointeur]]) ; c'est pourquoi on n'écrit ni `init_tab(&tab)` ni `init_tab(tab[100])`.
- **`*(t+i)`** : `t+i` est l'adresse de la case `i`, obtenue par [[Arithmétique des pointeurs|arithmétique des pointeurs]] (le décalage est de `i` cases, soit `i * sizeof(float)` [[Octet|octets]], pas de `i` octets) ; l'étoile ([[Déréférencement|déréférencement]]) accède à la valeur rangée à cette adresse, en écriture dans `init_tab`, en lecture dans `affiche_tab`.
- **Pas de copie** : `init_tab` écrit directement dans le `tab` de `main`, sur la [[Pile d'exécution|pile]] (100 `float` de 4 octets, soit 400 octets).

`main` se termine sans `return 0;` : c'est permis pour `main` seule, qui renvoie alors 0 depuis la [[Norme du C|norme]] C99 ([[Code de retour|code de retour]] de succès). Toute autre fonction non `void` doit, elle, exécuter un `return` (voir [[tp6]]). `1.0` est un [[Valeur littérale|littéral]] `double`, converti en `float` à l'affectation ; `1.0f` est le littéral `float` correspondant. [[Complément hors du cours|ⓘ]]

## tab2.c

D'après le code, l'exercice demande la même chose qu'en `tab1.c`, avec la notation à crochets.

```c
#include <stdio.h>

void init_tab(float t[]){
    for (int i = 0; i<100; i++){
        t[i]=1.0;
    }
}

void affiche_tab(float t[]){
    for (int i=0; i<100;i++){
        printf("%f\n", t[i]);
    }
}

int main(){
    float tab[100];
    init_tab(tab);
    affiche_tab(tab);
    return 0;
}
```

Les deux fichiers sont équivalents : dans une liste de paramètres, `float t[]` (et même `float t[100]`) est **réécrit** par le compilateur en `float *t`, et `t[i]` est défini comme `*(t + i)`. Le choix de la notation est une affaire de lisibilité : les crochets disent « tableau », l'étoile dit « adresse ». `%f` affiche un [[Nombre à virgule flottante|réel]] avec 6 décimales ([[Fonctions printf et scanf]]).

L'équivalence `t[i]` ⇔ `*(t + i)` est si littérale que `i[t]` est aussi valide (addition commutative), curiosité à ne jamais écrire. La taille 100, écrite en dur dans les deux fonctions, est un [[Nombre magique (programmation)|nombre magique]] : avec `void init_tab(float t[], int n)` et l'appel `init_tab(tab, 100)`, la fonction sert pour tout tableau ; une valeur de `n` trop grande ferait écrire hors du tableau ([[Dépassement de tampon|dépassement de tampon]], [[Comportement indéfini|comportement indéfini]]). `affiche_tab` ne modifie rien : `const float t[]` le garantit. [[Complément hors du cours|ⓘ]]

## À retenir

- `float *t`, `float t[]` et `float t[100]` sont trois écritures du **même** paramètre : un pointeur.
- `t[i]` ⇔ `*(t + i)` ; `t + i` avance de `i` cases, pas de `i` octets.
- Passer `tab`, pas `&tab` ni `tab[100]`.
- La fonction travaille sur le tableau d'origine et ignore sa taille : passer la taille en paramètre. [[Complément hors du cours|ⓘ]]
- `main` sans `return` renvoie 0 ; les autres fonctions non `void`, jamais. [[Complément hors du cours|ⓘ]]
