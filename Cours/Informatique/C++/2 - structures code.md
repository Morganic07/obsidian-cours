---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/C／C++/chp2 - structures code .docx|chp2 - structures code]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 4/C／C++/chp2 - structures code .docx|chp2 - structures code]], dans [[Cours/Informatique/C++/_index|C++]]. Le code est du [[Langage C|C]].
## Idée générale

Les structures de contrôle (conditions et boucles), les fonctions, la structure d'un programme, le passage des arguments et les tableaux.

## 1. Opérateurs

Les conditions s'écrivent avec des [[Opérateur de comparaison|opérateurs de comparaison]] et des [[Opérateur logique|opérateurs logiques]] :

| Opérateur | Signification |
|---|---|
| `==` | test d'équivalence |
| `!=` | différent (non-équivalence) |
| `>` | supérieur |
| `>=` | supérieur ou égal |
| `<` | inférieur |
| `<=` | inférieur ou égal |
| `&&` | ET logique |
| `\|\|` | OU logique |
| `!` | NON logique |
| `^` | OU exclusif (XOR) **bit à bit** : le C n'a pas d'opérateur XOR logique [[Erreurs du cours#^e-2-structures-code\|✎]] |

Les opérateurs **bit à bit** travaillent sur chaque bit des entiers et non sur des valeurs vrai/faux : `&` (ET), `|` (OU), `^` (OU exclusif), `~` (NON), `<<` et `>>` (décalages). Par exemple `6 & 3` vaut `2` (`110` ET `011` donne `010`) alors que `6 && 3` vaut `1`. Pour un vrai XOR logique, on écrit `(a != 0) != (b != 0)`, ou plus court `!a != !b`. [[Complément hors du cours|ⓘ]]

Le résultat de toutes ces opérations est un `int` : `1` pour vrai, `0` pour faux. En condition, toute valeur non nulle est vraie, d'où l'écriture courante `if (n)` pour `if (n != 0)`. Côté priorités, `!` passe avant les comparaisons, qui passent avant `&&`, lui-même avant `||` : `a || b && c` se lit `a || (b && c)`. Dans le doute, des parenthèses. [[Complément hors du cours|ⓘ]]

## 2. `if ... else`

Voir [[Structure conditionnelle]].

```c
if (condition1) {
    instruction1;
}
else if (condition2) {
    instruction2;
}
else if (condition3) {
    instruction3;
}
else {
    instruction_par_defaut;
}
```

Les conditions sont testées dans l'ordre et seule la première vraie est exécutée : les suivantes ne sont même pas évaluées. Un `else` se rattache toujours au `if` sans `else` le plus proche, ce qui piège quand on imbrique des `if` sans accolades. [[Complément hors du cours|ⓘ]]

Pour choisir entre deux valeurs, le C a aussi l'[[Opérateur conditionnel|opérateur ternaire]] `condition ? valeur_si_vrai : valeur_si_faux`, qui est une expression : `max = (a > b) ? a : b;` remplace un `if ... else` de quatre lignes. [[Complément hors du cours|ⓘ]]

## 3. `switch ... case`

Pour éviter les imbrications de `if`, le C possède une instruction qui explore plusieurs cas à la fois : `switch`.

```c
switch (variable) {
    case valeur1 :
        instruction10;
        instruction11;
        break;

    case valeur2 :
        instruction12;
        instruction13;
        break;

    ...

    default :
        instruction_par_defaut;
}
```

**Attention** : une fois l'exécution commencée à partir d'un `case`, les instructions suivantes sont exécutées séquentiellement, y compris celles des `case` suivants, jusqu'à rencontrer un `break`, qu'il ne faut donc surtout pas oublier.

Limites du `switch` : la variable testée doit être de type entier (`int`, `char`, type énuméré `enum`), et chaque `case` une constante connue à la compilation. On ne peut donc pas y comparer des `float`, des chaînes de caractères ni des intervalles (`case x > 10` n'existe pas) : il faut alors des `if ... else`. Le `default` est facultatif ; s'il manque et qu'aucun cas ne correspond, rien n'est exécuté. [[Complément hors du cours|ⓘ]]

Le passage d'un `case` au suivant sans `break` (*fall-through*) sert parfois exprès, pour traiter plusieurs valeurs de la même façon : [[Complément hors du cours|ⓘ]]

```c
switch (c) {
    case 'a': case 'e': case 'i': case 'o': case 'u': case 'y':
        printf("voyelle");
        break;
    default:
        printf("consonne ou autre");
}
```

## 4. Boucle `for`

Voir [[Boucle (programmation)]]. Trois éléments, séparés par des `;` :

1. un élément d'**initialisation**, exécuté **avant toutes** les itérations ;
2. une **condition** de boucle, vérifiée **avant chaque** itération ;
3. une instruction de **fin de boucle** (souvent une incrémentation ou une décrémentation), exécutée **après chaque** itération.

```c
for (initialisation ; condition ; incrémentation) {
    instructions à répéter
}
```

### Exemple `for (i = 0 ; i < 10 ; i = i + 1)`

1. `i = 0` initialise `i` à 0 ; la variable doit avoir été déclarée avant.
2. `i < 10` est la condition qui autorise l'exécution du bloc.
3. `i = i + 1` est l'incrémentation (souvent écrite `i++`, voir [[Opérateur d'incrémentation]]).

Remarques :

- La boucle s'exécute **10 fois**. Dans la boucle, `i` prend toutes les valeurs de 0 à 9 inclus. À la dernière itération, `i` est incrémenté pour atteindre 10, ce qui est la condition de sortie : **après la boucle, `i` vaut 10**.
- Ces trois éléments devraient être systématiquement présents dans les cas usuels du module, même s'il est possible de faire autrement.
- Si le bloc ne contient qu'une instruction, les accolades sont facultatives.
- Depuis la norme C99, la variable peut être déclarée dans la boucle elle-même : `for (int i = 0 ; i < 10 ; i++)`. Elle n'existe alors que dans la boucle ([[Portée d'une variable]]) et on ne peut plus lire sa valeur après. [[Complément hors du cours|ⓘ]]
- Le `for` n'est qu'une écriture compacte du `while` : `for (init ; cond ; incr) { corps }` équivaut à `init; while (cond) { corps incr; }` (sauf si le corps contient un `continue`, qui sauterait `incr` dans la version `while`). On choisit `for` quand le nombre d'itérations est connu d'avance (parcourir un tableau), `while` quand il dépend de ce qui se passe dans la boucle. [[Complément hors du cours|ⓘ]]

Deux instructions modifient le déroulement de n'importe quelle boucle : `break` en sort immédiatement (comme dans le `switch`), et `continue` saute la fin de l'itération en cours pour passer à la suivante (dans un `for`, l'incrémentation est quand même exécutée). Par exemple, `for (i = 0 ; i < 10 ; i++) { if (i % 2 == 0) continue; printf("%d ", i); }` n'affiche que les nombres impairs. [[Complément hors du cours|ⓘ]]

## 5. Boucle `do ... while`

La condition de rebouclage est vérifiée **à la fin** : le bloc est exécuté **au moins une fois**.

```c
do {
    bloc d'instructions à répéter
} while (condition de rebouclage);
```

N.B. : attention au point-virgule après le `while`.

Usage typique : redemander une saisie tant qu'elle n'est pas valide, puisqu'il faut de toute façon la demander une première fois. [[Complément hors du cours|ⓘ]]

```c
int note;
do {
    printf("Note entre 0 et 20 : ");
    scanf("%d", &note);
} while (note < 0 || note > 20);
```

## 6. Boucle `while`

Très proche de la précédente, sauf que la condition est vérifiée **avant** le bloc : comme pour le `for`, le bloc peut n'être jamais exécuté.

```c
while (condition de boucle) {
    bloc d'instructions à répéter
}
```

Le bloc doit faire évoluer quelque chose dont dépend la condition, sinon la boucle ne s'arrête jamais (voir la boucle infinie de [[1 - basiques]]). Pour démontrer qu'une boucle s'arrête et calcule ce qu'on attend, on utilise un variant (une quantité entière qui décroît à chaque tour) et un invariant (une propriété vraie à chaque tour) : voir [[Terminaison d'un algorithme]] et [[Correction d'un algorithme]]. [[Complément hors du cours|ⓘ]]

## 7. Fonctions

### Déclaration

![[chp2 - structures code - image2.png]]

*Figure : anatomie de la déclaration `float moyenne (int a, int b);` : type de retour, nom de la fonction, paramètres (type et nom de chacun).*

```c
float moyenne (int a, int b);
```

Cette déclaration indique au compilateur qu'il existe un symbole `moyenne`, fonction à deux paramètres entiers qui renvoie un réel. Une fois déclarée, la fonction peut être appelée n'importe où dans le programme : le compilateur vérifie à chaque appel que le nombre et le type des paramètres, ainsi que la valeur de retour, sont cohérents avec le profil déclaré. Voir [[Fonction et procédure]].

Vocabulaire : cette déclaration sans corps s'appelle un **prototype** ; l'implémentation, avec son bloc `{ }`, est la **définition**. Les noms écrits dans la déclaration (`a`, `b`) sont les **paramètres** (formels) ; les valeurs données à l'appel, comme dans `moyenne(12, 15)`, sont les **arguments** (ou paramètres effectifs). Dans un prototype, les noms des paramètres sont facultatifs : `float moyenne (int, int);` est valide. [[Complément hors du cours|ⓘ]]

Les fichiers d'en-tête inclus en tête de programme ne contiennent justement que des prototypes : `stdio.h` déclare `printf` et `scanf`, `math.h` déclare `sqrt` ou `pow`, et leur code est fourni à l'édition de liens par la bibliothèque standard (sous Linux, les fonctions de `math.h` demandent souvent l'option `-lm` : `gcc prog.c -o prog -lm`). C'est le même principe que pour découper un programme en plusieurs fichiers : prototypes dans un `.h`, définitions dans un `.c` (voir [[Programmation modulaire]]). [[Complément hors du cours|ⓘ]]

### Règles pour que la compilation se passe bien

1. Les fonctions doivent être déclarées **avant** d'être appelées.
2. Toutes les fonctions doivent être implémentées.
3. La signature doit être identique dans la déclaration et dans l'implémentation.
4. Le type de la valeur de retour et le type des arguments doivent être respectés à l'appel.

### Structurer le code

Un programme se découpe en quatre blocs : inclusion des fichiers d'en-tête, déclaration des fonctions et procédures, fonction principale ([[Fonction main (C et C++)|`main`]]), implémentation des fonctions et procédures.

Les prototypes ne sont nécessaires que parce que les fonctions sont implémentées **après** `main` : le compilateur lit le fichier de haut en bas. Une autre organisation, aussi valide, définit chaque fonction avant son premier appel, sans prototype. Le `return 0;` final de `main` renvoie au système un **code de sortie** : `0` signifie que tout s'est bien passé, une autre valeur signale une erreur (constantes `EXIT_SUCCESS` et `EXIT_FAILURE` de `stdlib.h`) ; en shell, `echo $?` affiche ce code après l'exécution. [[Complément hors du cours|ⓘ]]

![[chp2 - structures code - image13.png]]

*Figure : programme C découpé en blocs annotés ; les cadres verts signalent les appels de fonctions et de procédures dans `main` et dans `carre`.*

Code de la figure ; `affiche_points` doit déclarer ses compteurs `i` et `j` (`int i, j;`), sans quoi il ne compile pas : [[Erreurs du cours#^e-2-structures-code|✎]]

```c
#include <stdio.h>                       /* inclusion des fichiers d'en-tête */

int produit (int a, int b);              /* déclaration des fonctions */
int carre (int a);                       /* et des procédures */
void affiche_points (int a, int b);

int main () {                            /* fonction principale */
    int x = 3;
    int y = 5;

    printf ("Le rectangle ");
    affiche_points (x, y);
    printf (" a %d points\n", produit (x, y));

    printf ("Le carre \n");
    affiche_points (x, x);
    printf (" a %d points\n", carre (x));

    return 0;
}

int produit (int a, int b) {             /* implémentation */
    int val;
    val = a * b;
    return val;
}

int carre (int a) {
    int v;
    v = produit (a, a);
    return v;
}

void affiche_points (int a, int b) {
    int i, j;
    for (i = 0 ; i < a ; i ++) {
        for (j = 0 ; j < b ; j ++) {
            printf (". ");
        }
        printf ("\n");
    }
}
```

### Procédure

Une **procédure** est une fonction qui ne renvoie rien (elle affiche, par exemple, mais ne fait pas de `return` de valeur) : elle est de type `void`. Selon le cours, toutes les procédures sont des `void`, mais tous les `void` ne sont pas forcément des procédures.

La dernière phrase s'explique par les autres usages du mot `void` : dans `int lire(void)`, il indique que la fonction ne prend **aucun paramètre** (elle renvoie pourtant un `int`) ; dans `void *`, il désigne un pointeur générique, vers une donnée de type quelconque (c'est ce que renvoie `malloc`). Une procédure peut quitter avant la fin par un `return;` sans valeur. [[Complément hors du cours|ⓘ]]

Les variables déclarées dans une fonction (comme `val` dans `produit`) sont **locales** : elles n'existent que pendant l'appel et sont invisibles depuis `main` ou les autres fonctions. Deux fonctions peuvent donc utiliser le même nom sans conflit. Une variable déclarée hors de toute fonction est **globale**, visible partout dans le fichier ; pratique, elle rend le programme plus difficile à suivre et s'utilise avec parcimonie (voir [[Portée d'une variable]]). [[Complément hors du cours|ⓘ]]

Une fonction peut s'appeler elle-même : c'est la [[Récursivité|récursivité]]. Exemple classique, la [[Factorielle|factorielle]] : `int fact(int n) { if (n <= 1) return 1; return n * fact(n - 1); }`. Il faut un cas d'arrêt (`n <= 1`), sinon les appels s'empilent jusqu'à faire déborder la pile. [[Complément hors du cours|ⓘ]]

### Passage des arguments

En C, par défaut, le passage des arguments se fait **par copie** ([[Passage par valeur]], [[Passage de paramètres]]).

1. **Variables simples** (`int`, `float`, `char`…) : la fonction reçoit une **copie** de la valeur, dans une nouvelle zone mémoire. Toute modification du paramètre dans la fonction est sans effet sur la variable d'origine dans `main`. Pour modifier une variable de `main`, on passe donc un [[Pointeur et adresse mémoire|pointeur]] sur cette variable, afin d'agir sur la case mémoire d'origine.
2. **Tableaux et pointeurs** : pour des raisons de performance, le C ne recopie jamais un tableau entier. Le nom du tableau est converti en l'adresse de son premier élément (un pointeur).

Syntaxes **équivalentes** (`init_tab` reçoit l'adresse du tableau `t`) :

```c
void init_tab(float *t)      /* OK : syntaxe pointeur */
void init_tab(float t[])     /* OK : syntaxe tableau sans taille */
void init_tab(float t[100])  /* OK : la taille 100 est ignorée par le C */
```

Syntaxe **non équivalente** :

```c
void init_tab(float t)       /* NON : ne fonctionne pas pour un tableau */
```

Exemple type du point 1 : une fonction `echange(int a, int b)` qui permute ses paramètres ne change rien dans `main` ; il faut écrire `echange(int *a, int *b)` et l'appeler avec `echange(&x, &y)`. Le programme complet est au chapitre 3, [[3 - pointeurs , tableaux, listes chainées, structures]] (voir aussi [[Échange de deux variables]]). [[Complément hors du cours|ⓘ]]

Deux conséquences du point 2. D'abord, la fonction travaille sur le tableau d'origine, pas sur une copie : `init_tab` peut remplir directement le tableau de `main`. Pour s'interdire de le modifier, on écrit `const float *t`. Ensuite, la fonction ne connaît pas la taille du tableau (c'est pour cela que le `100` de `t[100]` est ignoré) : on la passe en paramètre supplémentaire, `void init_tab(float t[], int n)`. Dans la fonction, `sizeof(t)` donne la taille d'un pointeur (8 octets sur un système 64 bits), pas celle du tableau. [[Complément hors du cours|ⓘ]]

## 8. Tableaux

Un [[Tableau (programmation)|tableau en C]] se déclare avec trois informations : le type des éléments, le nom du tableau, sa taille (nombre d'éléments).

![[chp2 - structures code - image3.png]]

*Figure : tableau de 10 cases numérotées de 0 à 9, chaque case désignée par `tab[0]` à `tab[9]`.*

```c
int tab [10];     /* tableau de 10 entiers */
```

- La taille est en général une expression constante ; depuis la norme C99, elle peut aussi être une variable qui a déjà une valeur au moment de la déclaration (tableau de taille variable, voir plus bas). Les indices vont obligatoirement de $0$ à $taille - 1$. [[Erreurs du cours#^e-2-structures-code|✎]]
- **Note** : les éléments ne sont **pas initialisés** ; croire qu'ils valent tous zéro après la création est une erreur.
- Accès à la case d'indice $i$ : `tab[i]`.
- Un tableau peut être initialisé dès sa déclaration avec des accolades : `int tab[5] = {4, 8, 15, 16, 23};`. Si la liste est plus courte que le tableau, les cases restantes valent 0 : `int tab[10] = {0};` met donc tout le tableau à zéro. Avec une liste, la taille peut être omise et le compilateur la compte : `int tab[] = {1, 2, 3};` crée 3 cases. [[Complément hors du cours|ⓘ]]
- Le C ne vérifie jamais les indices : écrire `tab[10]` dans un tableau de 10 cases (le **débordement d'indice**, *out of bounds*) compile sans erreur et lit ou écrase la mémoire voisine. C'est un [[Comportement indéfini|comportement indéfini]], cause fréquente d'[[Erreur de segmentation|erreurs de segmentation]] et de failles de sécurité (*buffer overflow*). L'erreur la plus courante est la boucle `for (i = 0 ; i <= 10 ; i++)`, qui fait un tour de trop. [[Complément hors du cours|ⓘ]]
- Le nombre de cases se retrouve par `sizeof(tab) / sizeof(tab[0])` (taille totale divisée par la taille d'une case), mais seulement là où le tableau est déclaré, pas dans une fonction qui le reçoit en paramètre. Un tableau ne s'affecte pas en bloc : `t1 = t2;` est refusé, il faut copier case par case. [[Complément hors du cours|ⓘ]]
- Une [[Chaîne de caractères|chaîne de caractères]] en C n'est qu'un tableau de `char` terminé par le caractère nul `'\0'` : `char mot[] = "chat";` réserve 5 cases. Les tableaux à deux dimensions se déclarent `int m[3][4];` (3 lignes de 4 colonnes) et se parcourent avec deux boucles `for` imbriquées, `m[i][j]` désignant la case de la ligne `i` et de la colonne `j`. [[Complément hors du cours|ⓘ]]

Exemples :

```c
tab [3] = 12;              /* met 12 dans la case n° 3, donc la 4e case (on numérote à partir de 0) */
printf ("%d", tab [3]);    /* affiche la valeur de la case n° 3 */
tab [3] = tab [3] + 2;     /* la case passe de 12 à 14 */
```

Compléments de la note :

- Pour définir un tableau, il faut toujours connaître sa taille au moment de la déclaration. Une taille donnée par une variable est permise depuis C99 (tableau de taille variable, *VLA*, devenu facultatif pour les compilateurs en C11 mais accepté par `gcc`), à condition que la variable ait déjà une valeur ; l'exemple suivant est faux parce que `n` n'est pas initialisé : [[Erreurs du cours#^e-2-structures-code|✎]]

```c
int n;
int tab[n];   /* faux : n n'a pas de valeur ; correct avec int n = 10; */
```

- Tous les éléments d'un tableau ont **le même type** :

```c
int tab[5];    /* 5 éléments int */
char tab[5];   /* 5 éléments char */
```

L'image des tableaux finit sur « L'exemple suivant : » sans l'exemple annoncé (vérifié sur l'image).
