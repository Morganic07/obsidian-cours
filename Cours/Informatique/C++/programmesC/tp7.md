---
type: source
tags: [year4]
sources:
  - "[[Raw/Year 4/C／C++/programmes C/tp7/7.1.c|7.1.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp7/7.2.c|7.2.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp7/7.3.c|7.3.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp7/7.4.c|7.4.c]]"
  - "[[Raw/Year 4/C／C++/programmes C/tp7/7.5.c|7.5.c]]"
maj: 2026-11-12
complet: true
enrichi: 2026-11-12
---

Programmes du TP 7 de [[Langage C|C]] (dossier `programmes C/tp7`, cinq fichiers dont un vide), dans [[Cours/Informatique/C++/_index|C++]]. Ils portent sur les [[Tableau (programmation)|tableaux]] : les remplir avec `scanf`, les parcourir avec une [[Boucle (programmation)|boucle]] `for`, et surtout les passer à une [[Fonction et procédure|fonction]]. Ils appliquent le § 8 de [[2 - structures code]] et annoncent le § 7 de [[3 - pointeurs , tableaux, listes chainées, structures]], où l'on voit qu'une fonction reçoit en fait l'**adresse** du tableau (voir aussi [[tableaux]]). Deux programmes contenaient une erreur, et un commentaire une affirmation fausse, corrigés ci-dessous (✎). Compilation avec [[GCC|`gcc`]] `-std=c17 -Wall -Wextra`.

## 7.1

D'après le code, l'exercice demande de faire remplir un tableau de 10 entiers par l'utilisateur, puis de l'afficher dans une [[Fonction et procédure|procédure]] `print_tab` ; telle qu'elle est écrite, `print_tab` affiche le **double** de chaque valeur.

```c
#include <stdio.h>

void print_tab(int tab[10]);

int main(){
    int tab [10] ;   /* tableau de 10 entiers, déclaré mais pas initialisé */
    int i ;

    for (i = 0 ; i < 10 ; i = i + 1) {
        printf ("Quelle valeur pour la case %d ?\n", i) ;
        scanf ("%d", &tab [i]) ;
    }

    print_tab(tab);

    return 0 ;
}

void print_tab(int tab[10]){
    printf ("Voici le tableau que vous avez rempli :\n") ;
    int i;
    for (i = 0 ; i < 10 ; i = i + 1) {
        printf ("%d ", tab[i]*2) ;
    }
}
```

Sortie pour les saisies 1 à 10 : `Voici le tableau que vous avez rempli :` puis `2 4 6 8 10 12 14 16 18 20`.

Les commentaires du fichier découpent `main` en deux temps : **on demande à l'utilisateur de remplir les 10 cases du tableau**, case par case, avec `scanf("%d", &tab[i])` ([[Fonctions printf et scanf|`scanf`]] ; l'[[Opérateur d'adresse|opérateur `&`]] donne l'adresse de la case `i`, où `scanf` écrit la valeur lue) ; puis **on affiche le tableau complet**, ici en le confiant à `print_tab`.

Le premier commentaire disait « un tableau de 10 entiers est initialisé » : `int tab[10];` **déclare** le tableau sans l'**initialiser** ([[Initialisation (programmation)|initialisation]]), ses cases contiennent des valeurs indéterminées jusqu'à la boucle de saisie (le cours le dit au § 8 de [[2 - structures code]]). Le commentaire est corrigé dans le code ci-dessus. [[Erreurs du cours#^e-tp7|✎]]

Explications :

- **Indices** : les cases d'un tableau de 10 éléments vont de `tab[0]` à `tab[9]` ; la boucle `for (i = 0 ; i < 10 ; i = i + 1)` les parcourt exactement.
- **Passage à une fonction** : on écrit `print_tab(tab)`, sans crochets ni `&`. Le nom du tableau est converti en l'adresse de sa première case ([[Décroissance d'un tableau en pointeur|décroissance en pointeur]]) : `print_tab` lit le tableau de `main`, sans copie. Le `10` de `int tab[10]` dans le [[Argument et paramètre|paramètre]] est ignoré par le [[Compilateur|compilateur]], qui comprend `int *tab`, un [[Pointeur et adresse mémoire|pointeur]] (voir [[3 - pointeurs , tableaux, listes chainées, structures]], § 7).
- **`tab[i]*2`** : le double est calculé à l'affichage, le tableau lui-même n'est pas modifié ; le message « le tableau que vous avez rempli » est donc trompeur.

Le dernier `printf` n'a pas de `\n` : la sortie se termine sur la même ligne que l'invite du [[Interface en ligne de commande|terminal]]. Ajouter `printf("\n");` après la boucle. La [[Variable (programmation)|variable]] `i` de `print_tab` est distincte de celle de `main` : chaque fonction a ses [[Portée d'une variable|variables locales]]. [[Complément hors du cours|ⓘ]]

## 7.2

D'après le code, l'exercice demande de saisir 5 entiers dans un tableau, puis d'afficher la plus petite et la plus grande valeur avec leurs indices.

`indice_min` et `indice_max` n'étaient pas initialisés : si le minimum (ou le maximum) est la première case, la boucle ne leur affecte jamais de valeur, et le `printf` lit une [[Variable non initialisée|variable non initialisée]]. Ils sont initialisés à 0, l'indice de `tab[0]` qui sert de valeur de départ. [[Erreurs du cours#^e-tp7|✎]]

```c
#include <stdio.h>

int main(){
    int tab[5];

    for (int i=0; i<5;i++){
        printf("rentrez une valeur case %d: \n", i);
        scanf("%d", &tab[i]);
    }

    int valeur_min = tab[0];
    int indice_min = 0;
    int valeur_max = tab[0];
    int indice_max = 0;

    for (int j=0; j<5; j++){
        if (valeur_min > tab[j]){
            valeur_min = tab[j];
            indice_min = j;
        }
        else if (valeur_max < tab[j]){
            valeur_max = tab[j];
            indice_max = j;
        }
    }

    printf("valeur min : %d | indice : %d \n", valeur_min, indice_min);
    printf("valeur max : %d | indice : %d \n", valeur_max, indice_max);

    return 0;
}
```

Sortie pour `5 1 3 4 2` : `valeur min : 1 | indice : 1` et `valeur max : 5 | indice : 0`.

C'est l'algorithme de [[Recherche du minimum et du maximum|recherche du minimum et du maximum]] : on part de la première case comme candidat, puis on compare chaque case au candidat courant ([[Opérateur de comparaison|opérateurs de comparaison]] dans une [[Structure conditionnelle|structure conditionnelle]] `if … else if`), en un seul parcours ([[Recherche séquentielle|parcours séquentiel]], $n - 1$ comparaisons utiles pour chaque extremum, soit une [[Complexité algorithmique|complexité]] linéaire $O(n)$). Partir de `tab[0]` plutôt que d'une valeur arbitraire (0, ou 1000) garantit un résultat juste quelles que soient les valeurs saisies, négatives comprises. Les comparaisons strictes (`>` et `<`) retiennent la **première** occurrence en cas d'égalité. Le `else if` est sûr : une valeur ne peut pas être à la fois plus petite que le minimum courant et plus grande que le maximum courant, puisque le minimum est toujours inférieur ou égal au maximum.

Pourquoi l'oubli d'initialisation passait inaperçu : avec la saisie `1 5 3 4 2`, le programme d'origine affichait bien `indice : 0`, parce que la case mémoire contenait 0 par hasard. Lire une variable non initialisée est un [[Comportement indéfini|comportement indéfini]] : un autre compilateur, une autre option (`-O2`) ou un autre contexte peuvent donner n'importe quelle valeur. `gcc -Wall -O2` le signale par un [[Avertissement de compilation|avertissement]] : `'indice_min' may be used uninitialized`. [[Complément hors du cours|ⓘ]]

La boucle peut commencer à `j = 1`, la case 0 étant déjà le candidat de départ. La taille 5, écrite en dur à quatre endroits, gagnerait à être une [[Constante (programmation)|constante]] (`#define N 5`, voir [[Macro (préprocesseur)]]) pour éviter les [[Nombre magique (programmation)|nombres magiques]]. [[Complément hors du cours|ⓘ]]

## 7.3

D'après le code, l'exercice demande de saisir 5 entiers, puis d'afficher dans une procédure `amplitude` le maximum, le minimum et leur différence, et dans une procédure `moyenne` la moyenne des valeurs.

Dans `moyenne`, `float moyenne = compteur/5;` faisait une division **entière** ([[Opérateurs arithmétiques|opérateur `/`]] entre deux `int`, voir [[Type entier]]) : pour `1 2 3 4 6`, le programme affichait `3.000000` au lieu de `3.200000`. Corrigé en `compteur/5.0f`. [[Erreurs du cours#^e-tp7|✎]]

```c
#include <stdio.h>

void amplitude(int tab[5]);
void moyenne(int tab[5]);

int main(){
    int tab[5];

    for (int i = 0; i < 5; i++){
        printf("rentrez valeurs  : \n");
        scanf("%d", &tab[i]);
    }

    amplitude(tab);
    moyenne(tab);

    return 0;
}

void amplitude(int tab[5]){
    int max = tab[0];
    int min = tab[0];

    for (int i = 0; i < 5; i++ ){
        if (max < tab[i]) max = tab[i];
    }

    for (int j = 0; j < 5; j++ ){
        if (min > tab[j]) min = tab[j];
    }

    printf("Max : %d | min : %d \n", max, min);
    printf("amplitude : %d \n", max-min);
}

void moyenne(int tab[5]){
    int compteur = 0;

    for (int i = 0; i<5; i++){
        compteur += tab[i];
    }

    float moyenne = compteur/5.0f;

    printf("moyenne : %f\n", moyenne);
}
```

Sortie pour `1 2 3 4 6` : `Max : 6 | min : 1`, `amplitude : 5`, `moyenne : 3.200000`.

Explications :

- **Amplitude** : l'« amplitude » du programme est l'[[Étendue (statistique)|étendue]] de la série, $\max - \min$, un indicateur de dispersion de la [[Statistique descriptive|statistique descriptive]].
- **Moyenne** : `compteur` est un [[Accumulateur (programmation)|accumulateur]] qui reçoit la somme des cases, divisée ensuite par l'effectif : c'est la [[Moyenne empirique|moyenne arithmétique]] $\bar{x} = \frac{1}{n}\sum x_i$, la plus courante des [[Mesures de tendance centrale|mesures de tendance centrale]].
- **Division entière** : quand les deux opérandes de `/` sont des entiers, le C calcule le quotient de la [[Division euclidienne|division euclidienne]] (16 / 5 = 3), **avant** toute conversion ; ranger le résultat dans un `float` ne rattrape rien. Il faut qu'un opérande soit réel : `5.0f` ([[Valeur littérale|littéral]] `float`), `5.0` (`double`), ou une conversion explicite `(float)compteur / 5` ([[Transtypage]]).
- **`%f`** affiche un [[Nombre à virgule flottante|nombre à virgule flottante]] avec 6 décimales par défaut ; `%.2f` en garde 2 (voir [[Fonctions printf et scanf]]).

Dans la procédure `moyenne`, la variable locale s'appelle aussi `moyenne` : elle **masque** le nom de la fonction à l'intérieur du [[Bloc d'instructions|bloc]] ([[Masquage de nom|masquage de nom]]). C'est permis, mais ambigu à la lecture, et empêcherait par exemple un appel [[Récursivité|récursif]] ; l'[[Option de compilation|option]] `gcc -Wshadow` le signale. Un nom comme `resultat` évite la confusion. [[Complément hors du cours|ⓘ]]

Les deux boucles d'`amplitude` peuvent n'en faire qu'une, qui met à jour `max` et `min` dans le même parcours, comme en 7.2. Les deux procédures affichent leur résultat au lieu de le renvoyer : des fonctions `int etendue(int tab[], int n)` et `float moyenne(int tab[], int n)`, qui renvoient une valeur sans rien afficher, seraient réutilisables, et la taille en paramètre les rendrait valables pour tout tableau (voir 7.4). [[Complément hors du cours|ⓘ]]

## 7.4

D'après le code, l'exercice demande une procédure `doubleLesImpaires(tab, taille)` qui double, **dans le tableau lui-même**, les valeurs impaires, puis l'affiche.

```c
#include <stdio.h>

void doubleLesImpaires(int tab[], int taille_tab );

int main(){
    int tableau[5] = {0,1,2,3,4};
    int taille = 5;

    doubleLesImpaires(tableau, taille);

    return 0;
}

void doubleLesImpaires(int tab[], int taille_tab){
    for (int i = 0; i < taille_tab; i++){
        if (tab[i]%2 != 0) tab[i]*=2;
    }

    for (int j = 0; j < taille_tab; j++)printf("%d ", tab[j]);
}
```

Sortie : `0 2 2 6 4`.

Explications :

- **Initialisation par liste** : `int tableau[5] = {0,1,2,3,4};` donne une valeur à chaque case dès la déclaration ([[Initialisation (programmation)]]).
- **Taille en paramètre** : `int tab[]` (sans taille) et `int taille_tab` forment le couple habituel en C, puisque la fonction ne reçoit que l'adresse du tableau et ne peut pas connaître sa taille ([[3 - pointeurs , tableaux, listes chainées, structures]], § 7). La procédure marche ainsi pour n'importe quel tableau d'entiers, contrairement à 7.1 et 7.3, figées sur 10 et 5 cases.
- **Modification en place** : `tab[i]*=2` ([[Opérateur d'affectation composée|affectation composée]]) écrit dans le tableau de `main`, puisque `tab` contient son adresse : c'est un [[Effet de bord|effet de bord]] voulu, visible après l'appel. Les entiers simples sont copiés ([[Passage par valeur]]), les tableaux non : c'est la différence entre 7.1, qui ne modifie rien, et 7.4.
- **Impair** : `tab[i]%2 != 0` teste la [[Parité d'un entier|parité]] avec l'opérateur modulo ([[Opérateurs arithmétiques]]).

Écrire `!= 0` plutôt que `== 1` est le bon réflexe : en C, le reste de la division d'un nombre négatif est négatif (`-3 % 2` vaut `-1`, la division tronquant vers zéro depuis la [[Norme du C|norme]] C99, voir [[Division euclidienne]]), donc `tab[i] % 2 == 1` raterait les impairs négatifs. [[Complément hors du cours|ⓘ]]

Le nom `doubleLesImpaires` suit la [[Casse chameau|casse chameau]], comme `volumeCube` au TP 6 ([[tp6]]). Pour signaler qu'une fonction ne doit **pas** modifier un tableau, on déclare le paramètre `const int tab[]` : le compilateur refuse alors toute écriture dans `tab`. Écrire `tab[i]` avec `i >= taille_tab` serait un [[Dépassement de tampon|dépassement de tampon]], que le C ne détecte pas. En [[Langage C++|C++]], la [[Classe vector (C++)|classe `std::vector`]] connaît sa propre taille (`v.size()`) et dispense de ce paramètre. [[Complément hors du cours|ⓘ]]

## 7.5

Fichier vide.

## À retenir

- `int tab[10];` **déclare** un tableau sans l'initialiser : ses cases sont indéterminées jusqu'à la première écriture ; `int tab[5] = {0};` met tout à zéro.
- Un [[Tableau (programmation)|tableau]] se passe à une fonction par son nom seul : `f(tab)`. La fonction reçoit son adresse, peut le modifier, et ne connaît pas sa taille : la passer en paramètre.
- Toute [[Variable non initialisée|variable]] lue après une boucle (indice du minimum…) doit avoir une valeur de départ, même si la boucle « devrait » l'affecter.
- [[Recherche du minimum et du maximum|Minimum et maximum]] : partir de `tab[0]`, jamais d'une valeur arbitraire.
- `somme / 5` entre entiers est une division entière : écrire `somme / 5.0f` ou `(float)somme / 5`.
- Tester l'imparité par `x % 2 != 0`, qui reste juste pour les négatifs. [[Complément hors du cours|ⓘ]]
- Une fonction qui calcule renvoie son résultat ; l'affichage reste dans `main`. [[Complément hors du cours|ⓘ]]
