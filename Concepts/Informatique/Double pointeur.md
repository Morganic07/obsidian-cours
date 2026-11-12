---
type: concept
tags: [year4]
aliases: [pointeur de pointeur, pointer to pointer, double pointer, pointeur double]
sources: ["[[Raw/Year 4/C／C++/Chp3 - pointeurs , tableaux, listes chainées, structures.docx|Chp3 - pointeurs , tableaux, listes chainées, structures]]"]
maj: 2026-11-12
---

**Définition** (d'après [[3 - pointeurs , tableaux, listes chainées, structures]]) : un double pointeur (pointeur de pointeur) est une variable qui contient l'adresse d'un [[Pointeur et adresse mémoire|pointeur]]. Il se déclare avec deux étoiles, `type **nom;` : `int **doublePtr;` est un « pointeur vers un pointeur vers un `int` ». Il sert quand on veut pointer vers une variable qui est déjà un pointeur, et surtout quand on doit **modifier l'adresse contenue dans un pointeur depuis une fonction**. On accède à la valeur finale par `**`. Précautions données par le cours : initialiser pointeurs et doubles pointeurs avant usage, un `free` pour chaque `malloc`, vérifier `NULL` avant d'accéder à un double pointeur.

```c
int x = 10;
int *ptr = &x;        // ptr contient l'adresse de x
int **dptr = &ptr;    // dptr contient l'adresse de ptr
// *dptr vaut ptr, **dptr vaut x (10) ; **dptr = 20; modifie x
```

**Pourquoi il en faut un pour modifier un pointeur dans une fonction (complément, hors du cours).** Le [[Langage C|C]] passe tous ses arguments par valeur ([[Passage par valeur]]) : une fonction qui reçoit un `Chainon *premier` travaille sur une copie de l'adresse, et `premier = nouveau;` dans la fonction ne change pas le pointeur de l'appelant. Pour le modifier, on transmet **son adresse**, de type `Chainon **`, et la fonction écrit à travers elle avec un [[Déréférencement|déréférencement]] : [[Complément hors du cours|ⓘ]]

```c
void ajouterEnTete(Chainon **ptrpremier, int v) {
    Chainon *nouveau = malloc(sizeof(Chainon));
    nouveau->valeur = v;
    nouveau->suivant = *ptrpremier;   // ancien premier
    *ptrpremier = nouveau;            // modifie le pointeur de l'appelant
}
// appel : ajouterEnTete(&premier, 5);
```

`*ptrpremier` est le pointeur de l'appelant (la tête de la [[Liste chaînée|liste chaînée]]), `**ptrpremier` le premier chaînon lui-même. Autre usage courant : `int main(int argc, char **argv)`, où `argv` est un tableau de [[Chaîne de caractères|chaînes]], donc un tableau de `char *`, qui [[Décroissance d'un tableau en pointeur|décroît]] en `char **`. Un tableau à deux dimensions alloué dynamiquement (un tableau de lignes, chacune obtenue par `malloc`) se manipule aussi par un `int **`. En [[Langage C++|C++]], une [[Référence (C++)|référence]] sur pointeur (`Chainon *&premier`) rend le même service avec une syntaxe plus légère. [[Complément hors du cours|ⓘ]]

## Dans le cours

- [[3 - pointeurs , tableaux, listes chainées, structures]] : le § 10 définit le double pointeur, le compare au pointeur simple et l'illustre par `x`, `ptr`, `dptr` et même un triple pointeur `tptr`.
- [[td listes chaînées]] : `creerListe`, `ajouterElement`, `supprimerElement` et `supprimerListe` reçoivent un `Chainon **` pour modifier la tête de liste `premier` ; un commentaire d'`ex1.c` confondait `*ptrpremier` et `**ptrpremier`.

Voir aussi : [[Pointeur et adresse mémoire]], [[Déréférencement]], [[Opérateur d'adresse]], [[Pointeur NULL]], [[Allocation dynamique]].
