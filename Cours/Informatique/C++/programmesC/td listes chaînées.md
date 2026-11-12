---
type: source
tags: [year4]
sources:
  - "[[Raw/Year 4/C／C++/programmes C/td_liste_chainees/ex1.c|ex1.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/td_liste_chainees/ex2.c|ex2.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/td_liste_chainees/ex3.c|ex3.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/td_liste_chainees/ex4.c|ex4.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/td_liste_chainees/ex5.c|ex5.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/td_liste_chainees/tous_les_exo.c|tous_les_exo.c]]"
maj: 2026-11-12
complet: true
enrichi: 2026-11-12
---

Programmes du TD sur les [[Liste chaînée|listes chaînées]], écrits en [[Langage C|C]] dans le dossier `td_liste_chainees` (six fichiers), dans [[Cours/Informatique/C++/_index|C++]]. Ils mettent en œuvre la fin de [[3 - pointeurs , tableaux, listes chainées, structures]] (§ 8 à 10) : une [[Structure (struct)|structure]] `Chainon` à deux champs, des [[Pointeur et adresse mémoire|pointeurs]] et des [[Double pointeur|doubles pointeurs]], l'[[Allocation dynamique|allocation dynamique]] avec `malloc` et `free`. Chaque exercice reprend le précédent et ajoute une [[Fonction et procédure|fonction]] : créer la liste (ex1), ajouter en tête (ex2), compter (ex3), supprimer une valeur (ex4) ; `tous_les_exo.c` rassemble le tout, avec la recherche et la libération de la liste. Les commentaires du code, qui expliquent le cours, sont remis au propre dans le texte.

## ex1.c

D'après le code, l'exercice demande de déclarer le type `Chainon` et d'écrire `creerListe`, qui initialise une liste vide.

Le fichier d'origine déclare le prototype `void creerListe(Chainon **ptrpremier);` **avant** le `typedef` qui définit `Chainon` : à cette ligne le type est inconnu et le programme ne compile pas (`error: unknown type name 'Chainon'`, suivi d'une [[Déclaration implicite de fonction|déclaration implicite]] de `creerListe` dans `main`). Le prototype est donc déplacé après le `typedef` : [[Erreurs du cours#^e-td-listes-chainees|✎]]

```c
#include <stdio.h>

typedef struct Chainon{
    int valeur;
    struct Chainon *suivant;
} Chainon;

void creerListe(Chainon **ptrpremier);   // après le typedef

int main(){
    Chainon *premier;
    creerListe(&premier);
    return 0;
}

void creerListe(Chainon **ptrpremier){
    *ptrpremier = NULL;
}
```

**Explications.**

- **Le type `Chainon`.** `struct Chainon` contient une valeur entière et un pointeur `suivant` vers le chaînon suivant : la structure est **autoréférente**, d'où l'écriture `struct Chainon *suivant` à l'intérieur (l'[[Alias de type (typedef)|alias]] `Chainon` n'existe qu'après l'accolade fermante). `typedef struct Chainon {…} Chainon;` crée l'alias `Chainon`, qui évite de répéter `struct` partout. [[Complément hors du cours|ⓘ]]
- **`Chainon *premier;`** : `premier` est un pointeur sur `Chainon`. Il occupe lui-même une case mémoire (disons à l'adresse `0x100`, sur la [[Pile d'exécution|pile]] de `main`) et sa valeur, tant qu'on ne l'a pas affectée, est **indéterminée** ([[Variable non initialisée|variable non initialisée]]).
- **`creerListe(&premier)`** : l'[[Opérateur d'adresse|opérateur `&`]] fournit l'adresse de `premier`, soit `0x100`. Le paramètre `ptrpremier` reçoit cette adresse ; son type est `Chainon **`, « pointeur vers un pointeur vers `Chainon` ».
- **`*ptrpremier = NULL;`** : le [[Déréférencement|déréférencement]] `*ptrpremier` va à l'adresse contenue dans `ptrpremier` (donc `0x100`, la case de `premier`) et y écrit [[Pointeur NULL|`NULL`]]. Au retour, `premier` occupe toujours `0x100` et vaut `NULL` : la liste est vide. [[Erreurs du cours#^e-td-listes-chainees|✎]]
- Pourquoi un double pointeur : en C tout argument est transmis par [[Passage par valeur|valeur]]. Avec un paramètre `Chainon *p`, la fonction recevrait une copie de `premier` et `p = NULL;` ne modifierait que cette copie. Pour qu'une fonction modifie une variable de l'appelant, il faut lui passer l'adresse de cette variable ; la variable étant ici un pointeur, son adresse est un `Chainon **`. Cette modification d'une variable extérieure à la fonction est un [[Effet de bord|effet de bord]] voulu.

Le programme ne produit aucune sortie. En C, l'ordre compte : un nom (type, fonction) doit être [[Déclaration et définition|déclaré]] avant sa première utilisation dans le fichier, car le [[Compilateur|compilateur]] lit le [[Code source|code source]] de haut en bas en une passe. [[Complément hors du cours|ⓘ]]

Plus simple pour une liste vide : `Chainon *premier = NULL;` directement dans `main`, ce que fait le cours ; `creerListe` sert surtout à s'exercer au double pointeur. Une fonction qui renvoie la liste (`Chainon *creerListe(void) { return NULL; }`, appelée par `premier = creerListe();`) éviterait aussi le double pointeur. [[Complément hors du cours|ⓘ]]

## ex2.c

D'après le code, l'exercice demande d'écrire `ajouterElement`, qui ajoute une valeur **en tête** de liste.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Chainon{
    int valeur;
    struct Chainon *suivant;
}Chainon;

void creerListe(Chainon **premier);
void ajouterElement(Chainon **premier, int user_valeur);

int main(){
    Chainon *premier;   // adresse du premier élément de la liste
    creerListe(&premier);
    ajouterElement(&premier, 7);

    free(premier);

    return 0;
}

void creerListe(Chainon **premier){
    *premier = NULL;
}

void ajouterElement(Chainon **premier, int user_valeur){
    Chainon *nouveau = malloc(sizeof(Chainon));

    nouveau -> valeur = user_valeur;
    nouveau -> suivant = *premier;
    *premier = nouveau;
}
```

**Explications.**

- **`malloc(sizeof(Chainon))`** réserve sur le [[Espace mémoire d'un processus|tas]] un bloc de la taille d'un chaînon (l'[[Opérateur sizeof|opérateur `sizeof`]] donne cette taille en octets) et renvoie son adresse, rangée dans `nouveau`. `malloc` est déclarée dans `<stdlib.h>`, de la [[Bibliothèque standard du C|bibliothèque standard du C]]. [[Complément hors du cours|ⓘ]]
- **`nouveau->valeur = user_valeur;`** : l'[[Opérateur flèche|opérateur flèche]] `->` revient à écrire `(*nouveau).valeur` ; on va dans la case `valeur` du nouveau chaînon pour y mettre 7.
- **`nouveau->suivant = *premier;`** : `*premier` (la variable `premier` du `main`) valait `NULL` ; le champ `suivant` du nouveau chaînon reçoit donc `NULL`, ce qui indique qu'il n'y a rien après lui : c'est le dernier élément.
- **`*premier = nouveau;`** : cette [[Affectation|affectation]] met à jour la [[Variable (programmation)|variable]] `premier` du `main` : elle ne vaut plus `NULL` mais l'adresse du chaînon qui vient d'être créé.
- **L'ordre des deux dernières instructions est imposé.** Si l'on écrivait `*premier = nouveau;` d'abord, on écraserait l'adresse de l'ancien premier chaînon avant de l'avoir sauvegardée dans `nouveau->suivant`, et l'on perdrait l'accès à tout le reste de la liste.
- **`free(premier);`** rend au système le seul chaînon alloué. Ce `free` suffit ici parce que la liste n'a qu'un élément ; avec plusieurs, il faut parcourir la liste (voir `supprimerListe` dans `tous_les_exo.c`). [[Complément hors du cours|ⓘ]]

L'ajout en tête coûte un temps constant, $O(1)$ en [[Complexité algorithmique|complexité]], quelle que soit la longueur de la liste ; l'ajout en queue demande de parcourir toute la liste, $O(n)$, sauf à tenir aussi un pointeur sur le dernier chaînon. Les éléments ajoutés en tête ressortent dans l'ordre inverse de leur ajout, comme dans une [[Pile et file|pile]] (dernier entré, premier sorti). [[Complément hors du cours|ⓘ]]

`malloc` renvoie `NULL` quand la mémoire manque ; un programme [[Robustesse (informatique)|robuste]] le teste avant d'écrire dans le bloc (`if (nouveau == NULL) { … }`), sans quoi `nouveau->valeur` déréférence un pointeur nul, un [[Comportement indéfini|comportement indéfini]] qui se traduit en pratique par une [[Erreur de segmentation|erreur de segmentation]]. En C, le `void *` renvoyé par `malloc` se convertit implicitement en `Chainon *` : le [[Transtypage|transtypage]] `(Chainon *)` est inutile (il est obligatoire en [[Langage C++|C++]]). [[Complément hors du cours|ⓘ]]

## ex3.c

D'après le code, l'exercice demande d'écrire `nombreElements`, qui compte les chaînons, et de l'appeler avant et après trois ajouts.

`ex3.c` alloue trois chaînons sans jamais les libérer : [[Fuite mémoire|fuite mémoire]] de 48 octets en 3 blocs, signalée par [[AddressSanitizer]] (`gcc -fsanitize=address`). Une boucle de libération est ajoutée à la fin de `main` : [[Erreurs du cours#^e-td-listes-chainees|✎]]

```c
int main(){
    Chainon *premier;
    creerListe(&premier);

    printf("taille de la liste : %d", nombreElements(premier));

    ajouterElement(&premier, 7);
    ajouterElement(&premier, 5);
    ajouterElement(&premier, 3);

    printf("taille de la liste : %d", nombreElements(premier));

    while (premier != NULL){             // libération ajoutée
        Chainon *suivant = premier->suivant;
        free(premier);
        premier = suivant;
    }

    return 0;
}

int nombreElements(Chainon *premier){
    int compteur;
    compteur = 0;

    Chainon *actuel = premier;   // pointeur temporaire de parcours

    while (actuel != NULL){
        compteur++;
        actuel = (*actuel).suivant;
    }

    return compteur;
}
```

`creerListe` et `ajouterElement` sont celles d'ex2.c. Sortie : `taille de la liste : 0taille de la liste : 3` ; les deux messages se collent, faute de `\n` à la fin du premier [[Fonctions printf et scanf|`printf`]].

**Explications.**

- **Parcours d'une liste.** On crée un pointeur temporaire `actuel` qui va parcourir la liste dans la [[Boucle (programmation)|boucle]] `while` ; tant qu'il désigne un chaînon (`actuel != NULL`), on incrémente le [[Compteur (programmation)|compteur]] et on passe au suivant par `actuel = (*actuel).suivant;` (équivalent de `actuel->suivant`). Le `NULL` final joue le rôle de [[Valeur sentinelle|sentinelle]] : il arrête la boucle.
- **Passage par `Chainon *` et non `Chainon **`** : `nombreElements` lit la liste sans la modifier ; une copie du pointeur de tête lui suffit. C'est la règle du cours : `Chainon **` pour modifier `premier`, `Chainon *` pour lire.
- **Pourquoi un pointeur temporaire** : avancer directement avec le paramètre `premier` serait correct ici (c'est une copie locale), mais `actuel` rend l'intention claire et laisse `premier` intact pour la suite de la fonction. [[Complément hors du cours|ⓘ]]

Le comptage coûte $O(n)$ : il faut visiter chaque chaînon, alors qu'un [[Tableau (programmation)|tableau]] connaît sa taille. Une implémentation qui compte souvent range la longueur dans une structure `Liste` (tête et taille) mise à jour à chaque ajout ou suppression. Une version [[Récursivité|récursive]] s'écrit `return premier == NULL ? 0 : 1 + nombreElements(premier->suivant);`, mais elle empile un cadre par chaînon sur la pile d'exécution. [[Complément hors du cours|ⓘ]]

## ex4.c

D'après le code, l'exercice demande d'écrire `supprimerElement`, qui retire de la liste le premier chaînon portant une valeur donnée, et renvoie 1 s'il l'a trouvé, 0 sinon.

Le test de la boucle était inversé (mauvais [[Opérateur de comparaison|opérateur de comparaison]]) : `if (actuel->suivant->valeur != user_valeur)` supprime le premier chaînon dont la valeur **diffère** de celle cherchée. Sur la liste 3 → 5 → 7, `supprimerElement(&premier, 5)` retirait 7 et laissait 3 → 5 (vérifié à l'exécution). La condition devient `==`, comme dans `tous_les_exo.c` ; une boucle de libération est aussi ajoutée à la fin de `main`, car le programme laissait 32 octets non libérés (fuite mémoire) : [[Erreurs du cours#^e-td-listes-chainees|✎]]

```c
int main(){
    Chainon *premier;
    creerListe(&premier);

    ajouterElement(&premier, 7);
    ajouterElement(&premier, 5);
    ajouterElement(&premier, 3);

    nombreElements(premier);

    supprimerElement(&premier, 5);

    while (premier != NULL){             // libération ajoutée
        Chainon *suivant = premier->suivant;
        free(premier);
        premier = suivant;
    }

    return 0;
}

int supprimerElement(Chainon **adr_premier, int user_valeur){

    if (*adr_premier==NULL) return 0;   // liste vide

    else if ((*adr_premier)->valeur== user_valeur ){   // c'est le premier
        Chainon *chainon_delete = *adr_premier;

        *adr_premier = (*adr_premier)->suivant;
        free(chainon_delete);

        return 1;
    }

    Chainon *actuel = *adr_premier;

    while (actuel->suivant !=NULL){

        if (actuel->suivant->valeur == user_valeur){
            Chainon *chainon_delete = actuel->suivant;
            actuel->suivant = chainon_delete->suivant;
            free(chainon_delete);
            return 1;
        }

        actuel = actuel->suivant;
    }

    return 0;
}
```

Les autres fonctions sont celles d'ex3.c (avec `actuel->suivant` au lieu de `(*actuel).suivant`). Le programme n'affiche rien : la valeur renvoyée par `nombreElements(premier);` est calculée puis ignorée.

**Explications.**

- **Trois cas.** Liste vide : rien à faire, on renvoie 0. Valeur dans le premier chaînon : il faut modifier `premier` lui-même, d'où le paramètre `Chainon **adr_premier`. Valeur plus loin : on modifie le champ `suivant` du chaînon **précédent**.
- **`actuel->suivant->valeur`** est la valeur contenue dans le chaînon suivant : `actuel->suivant` est l'adresse de ce chaînon, et `->valeur` va lire sa case `valeur`. On s'arrête donc **un cran avant** le chaînon à supprimer, parce qu'une liste simplement chaînée ne permet pas de revenir en arrière : arrivé sur le chaînon à supprimer, on ne pourrait plus raccrocher son prédécesseur.
- **Variable temporaire `chainon_delete`** : elle garde l'adresse du chaînon à libérer pendant qu'on le décroche (`actuel->suivant = chainon_delete->suivant;`), puis `free(chainon_delete)` le rend au système. Sans elle, on perdrait l'adresse du bloc à libérer.
- **Valeur de retour** 1 ou 0 : une [[Booléen|valeur booléenne]] codée en `int`, à la manière du C d'avant `<stdbool.h>`. [[Complément hors du cours|ⓘ]]
- Le `else` après un `return` est superflu (le code qui suit ne s'exécute que si les deux premiers tests échouent), sans conséquence. [[Complément hors du cours|ⓘ]]

Le bogue de la condition inversée est typique : le programme compile, s'exécute sans erreur et donne un résultat faux. Seul un test qui affiche la liste après la suppression le révèle ; d'où l'intérêt d'une fonction d'affichage et de [[Test unitaire|tests unitaires]] sur les cas limites (liste vide, valeur en tête, au milieu, en queue, absente). [[Complément hors du cours|ⓘ]]

Le double pointeur permet de traiter les trois cas d'un seul geste : en parcourant la liste avec un `Chainon **p` qui désigne successivement `premier`, puis chaque champ `suivant`, la suppression s'écrit `Chainon *del = *p; *p = del->suivant; free(del);` quel que soit l'endroit du chaînon. [[Complément hors du cours|ⓘ]]

```c
int supprimerElement(Chainon **adr_premier, int user_valeur){
    for (Chainon **p = adr_premier; *p != NULL; p = &(*p)->suivant){
        if ((*p)->valeur == user_valeur){
            Chainon *del = *p;
            *p = del->suivant;
            free(del);
            return 1;
        }
    }
    return 0;
}
```

## ex5.c

Fichier vide : une [[Fonction main (C et C++)|fonction `main`]] qui renvoie 0, sans exercice.

## tous_les_exo.c

D'après le code, le fichier rassemble les exercices précédents et en ajoute deux : `rechercherElement`, qui renvoie l'adresse du premier chaînon portant une valeur (ou `NULL`), et `supprimerListe`, qui libère toute la liste.

La ligne `Chainon *resultat = rechercherElement(premier, 5);x` se termine par un `x`, faute de frappe, qui empêche la compilation (`error: unknown type name 'x'`) ; le `x` est retiré. [[Erreurs du cours#^e-td-listes-chainees|✎]]

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Chainon{
    int valeur;
    struct Chainon *suivant;
}Chainon;

void creerListe(Chainon **premier);
void ajouterElement(Chainon **premier, int user_valeur);
int nombreElements(Chainon *premier);
int supprimerElement(Chainon **premier, int user_valeur);
Chainon *rechercherElement(Chainon *premier, int user_valeur);
void supprimerListe(Chainon **premier);

int main(){
    Chainon *premier;

    creerListe(&premier);

    printf("taille de la liste : %d", nombreElements(premier));

    ajouterElement(&premier, 7);
    ajouterElement(&premier, 5);
    ajouterElement(&premier, 3);

    printf("taille de la liste : %d\n", nombreElements(premier));

    Chainon *resultat = rechercherElement(premier, 5);
    printf("Valeur %d trouvee, adresse %p\n", resultat->valeur, (void*)resultat);

    supprimerListe(&premier);
    printf("taille de la liste : %d", nombreElements(premier));

    return 0;
}

Chainon *rechercherElement(Chainon *premier, int user_valeur){
    Chainon *actuel = premier;

    while (actuel !=NULL){
        if (actuel->valeur == user_valeur) return actuel;
        actuel = actuel->suivant;
    }

    return NULL;
}

void supprimerListe(Chainon **adr_premier){
    Chainon *actuel = *adr_premier;
    Chainon *suivant;

    while (actuel != NULL){
        suivant = actuel->suivant;   // sauvegarde avant le free
        free(actuel);
        actuel = suivant;
    }

    *adr_premier = NULL;
}
```

`creerListe`, `ajouterElement`, `nombreElements` et `supprimerElement` sont celles des exercices précédents (avec la condition `==`). Sortie (l'adresse change à chaque exécution) :

```text
taille de la liste : 0taille de la liste : 3
Valeur 5 trouvee, adresse 0x55e48cdd32d0
taille de la liste : 0
```

**Explications** (les commentaires du fichier, remis au propre).

- **`typedef`** permet de définir un alias : `Chainon` désigne désormais `struct Chainon`. C'est un [[Mot réservé|mot réservé]] du C.
- **`nombreElements`** : un pointeur temporaire parcourt la liste ; si la cellule est occupée (pointeur non `NULL`), le compteur s'incrémente et le pointeur passe à l'élément suivant.
- **`supprimerElement`** : si le premier chaînon est `NULL`, la liste est vide et la fonction renvoie 0. Si le premier chaînon porte la valeur cherchée, la variable temporaire `chainon_delete` garde son adresse, l'affectation `*adr_premier = (*adr_premier)->suivant;` fait de son successeur le nouveau premier, puis `free(chainon_delete)` libère l'ancien premier, et la fonction renvoie 1. Sinon, le pointeur `actuel` parcourt la liste tant qu'il reste des chaînons après lui, compare la valeur du chaînon suivant, et en cas d'égalité le décroche et le libère de la même manière ; s'il n'a rien trouvé, la fonction renvoie 0. [[Erreurs du cours#^e-td-listes-chainees|✎]]
- **`rechercherElement`** : `actuel` va de chaînon en chaînon tant qu'il reste des éléments ; dès que sa case `valeur` correspond à la valeur cherchée, la fonction renvoie l'adresse du chaînon, et `NULL` si elle atteint la fin de la liste.
- C'est une [[Recherche séquentielle|recherche séquentielle]], en $O(n)$. Elle renvoie un `Chainon *` et non un `int` : l'appelant peut ensuite lire ou modifier le chaînon trouvé. [[Complément hors du cours|ⓘ]]
- **`%p` et `(void*)resultat`** : `%p` affiche une adresse en [[Notation hexadécimale|hexadécimal]] et attend un `void *`, d'où la conversion explicite. [[Complément hors du cours|ⓘ]]
- **`supprimerListe`** : on commence par le premier chaînon ; tant qu'il en reste, on range l'adresse du chaînon suivant dans `suivant`, on libère le chaînon actuel, puis on passe au suivant. L'ordre est impératif : après `free(actuel)`, lire `actuel->suivant` serait lire de la mémoire rendue ([[Pointeur pendant|pointeur pendant]]). Enfin `*adr_premier = NULL;` remet la liste à vide, d'où la taille 0 affichée ensuite, sans pointeur pendant dans `main`.

`resultat->valeur` suppose que la valeur a été trouvée : si `rechercherElement` renvoie `NULL` (valeur absente), ce déréférencement est un comportement indéfini, en pratique une erreur de segmentation. Il faut tester le résultat : `if (resultat != NULL) printf(…); else printf("Valeur absente\n");`. [[Complément hors du cours|ⓘ]]

Pour vérifier qu'aucun bloc n'est oublié, on compile avec `gcc -g -fsanitize=address`, ou l'on exécute le programme sous [[Valgrind]] (`valgrind --leak-check=full ./prog`) : les deux signalent les [[Fuite mémoire|fuites]], les lectures après `free` et les dépassements de bloc, avec la ligne fautive. Sur ce dossier, AddressSanitizer ne signale rien pour ex2 et `tous_les_exo`, et des fuites pour ex3 et ex4 avant correction. [[Complément hors du cours|ⓘ]]

En [[Langage C++|C++]], on n'écrit plus de liste chaînée à la main hors exercice : la [[Bibliothèque standard du C++|bibliothèque standard]] fournit `std::forward_list` (simplement chaînée) et `std::list` (doublement chaînée), voir [[Classe list (C++)]], qui libèrent leurs nœuds d'elles-mêmes dans leur [[Destructeur (programmation)|destructeur]]. Pour la plupart des usages, [[Classe vector (C++)|`std::vector`]] reste plus rapide, car ses éléments contigus profitent de la [[Mémoire cache|mémoire cache]] du processeur. [[Complément hors du cours|ⓘ]]

## Compilation et vérification

Commandes utilisées (hors cours) : `gcc -std=c17 -Wall -Wextra exN.c -o exN`, puis `./exN`. L'option `-Wall -Wextra` active les [[Avertissement de compilation|avertissements]] courants de [[GCC]] ; `-std=c17` fixe la version de la [[Norme du C|norme du C]] ([[Option de compilation|options de compilation]]). Bilan : ex1.c et tous_les_exo.c ne compilaient pas ([[Erreur de compilation|erreurs de compilation]]) ; ex3.c et ex4.c compilaient sans avertissement mais fuyaient, et ex4.c supprimait le mauvais chaînon. [[Complément hors du cours|ⓘ]]

## À retenir

- Un type se déclare avant tout prototype qui l'utilise : le `typedef` d'abord, les prototypes ensuite.
- Pour qu'une fonction modifie `premier`, on lui passe `&premier`, de type `Chainon **` ; pour seulement lire la liste, `Chainon *` suffit.
- Ajout en tête : `nouveau->suivant = *premier;` **avant** `*premier = nouveau;`, sinon on perd le reste de la liste.
- Pour supprimer un chaînon, on s'arrête sur son **prédécesseur** (`actuel->suivant->valeur`) et on garde l'adresse du chaînon dans une variable temporaire avant le `free`.
- Libérer une liste : sauvegarder `suivant` **avant** `free(actuel)`, puis remettre la tête à `NULL`.
- Un `malloc` = un `free` : chaque chaînon alloué doit être libéré, sinon [[Fuite mémoire|fuite mémoire]] ; le C n'a pas de [[Ramasse-miettes|ramasse-miettes]] comme Java ou Python, et `-fsanitize=address` détecte la fuite. [[Complément hors du cours|ⓘ]]
- Un programme qui compile et tourne peut être faux : afficher la liste après chaque opération, et tester les cas limites (vide, tête, milieu, queue, absent). [[Complément hors du cours|ⓘ]]
- Tester un pointeur renvoyé (`malloc`, recherche) avant de le déréférencer. [[Complément hors du cours|ⓘ]]
