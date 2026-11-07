---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/C++/chp2 - structures code .docx|chp2 - structures code]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 4/C++/chp2 - structures code .docx|chp2 - structures code]], dans [[C++ (index)]]. Le code est du [[Langage C|C]]. En cas d'écart, le cours et ses images font foi.

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
| `^` | « XOR logique » selon le cours (voir le point 1 à vérifier) |

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

## 5. Boucle `do ... while`

La condition de rebouclage est vérifiée **à la fin** : le bloc est exécuté **au moins une fois**.

```c
do {
    bloc d'instructions à répéter
} while (condition de rebouclage);
```

N.B. : attention au point-virgule après le `while`.

## 6. Boucle `while`

Très proche de la précédente, sauf que la condition est vérifiée **avant** le bloc : comme pour le `for`, le bloc peut n'être jamais exécuté.

```c
while (condition de boucle) {
    bloc d'instructions à répéter
}
```

## 7. Fonctions

### Déclaration

![[chp2 - structures code - image2.png]]

*Figure : anatomie de la déclaration `float moyenne (int a, int b);` : type de retour, nom de la fonction, paramètres (type et nom de chacun).*

```c
float moyenne (int a, int b);
```

Cette déclaration indique au compilateur qu'il existe un symbole `moyenne`, fonction à deux paramètres entiers qui renvoie un réel. Une fois déclarée, la fonction peut être appelée n'importe où dans le programme : le compilateur vérifie à chaque appel que le nombre et le type des paramètres, ainsi que la valeur de retour, sont cohérents avec le profil déclaré. Voir [[Fonction et procédure]].

### Règles pour que la compilation se passe bien

1. Les fonctions doivent être déclarées **avant** d'être appelées.
2. Toutes les fonctions doivent être implémentées.
3. La signature doit être identique dans la déclaration et dans l'implémentation.
4. Le type de la valeur de retour et le type des arguments doivent être respectés à l'appel.

### Structurer le code

Un programme se découpe en quatre blocs : inclusion des fichiers d'en-tête, déclaration des fonctions et procédures, fonction principale ([[Méthode main|`main`]]), implémentation des fonctions et procédures.

![[chp2 - structures code - image13.png]]

*Figure : programme C découpé en blocs annotés ; les cadres verts signalent les appels de fonctions et de procédures dans `main` et dans `carre`.*

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
    for (i = 0 ; i < a ; i ++) {         /* i et j non déclarés : voir point 3 */
        for (j = 0 ; j < b ; j ++) {
            printf (". ");
        }
        printf ("\n");
    }
}
```

### Procédure

Une **procédure** est une fonction qui ne renvoie rien (elle affiche, par exemple, mais ne fait pas de `return` de valeur) : elle est de type `void`. Selon le cours, toutes les procédures sont des `void`, mais tous les `void` ne sont pas forcément des procédures.

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

## 8. Tableaux

Un [[Tableau (programmation)|tableau en C]] se déclare avec trois informations : le type des éléments, le nom du tableau, sa taille (nombre d'éléments).

![[chp2 - structures code - image3.png]]

*Figure : tableau de 10 cases numérotées de 0 à 9, chaque case désignée par `tab[0]` à `tab[9]`.*

```c
int tab [10];     /* tableau de 10 entiers */
```

- La taille doit être une expression constante (pas une variable du programme). Les indices vont obligatoirement de $0$ à $taille - 1$.
- **Note** : les éléments ne sont **pas initialisés** ; croire qu'ils valent tous zéro après la création est une erreur.
- Accès à la case d'indice $i$ : `tab[i]`.

Exemples :

```c
tab [3] = 12;              /* met 12 dans la case n° 3, donc la 4e case (on numérote à partir de 0) */
printf ("%d", tab [3]);    /* affiche la valeur de la case n° 3 */
tab [3] = tab [3] + 2;     /* la case passe de 12 à 14 */
```

Compléments de la note :

- Pour définir un tableau, il faut toujours connaître sa taille. Le cours interdit d'écrire la taille avec une variable, « la taille doit être écrite en dur » :

```c
int n;
int tab[n];   /* interdit selon le cours : voir point 2 */
```

- Tous les éléments d'un tableau ont **le même type** :

```c
int tab[5];    /* 5 éléments int */
char tab[5];   /* 5 éléments char */
```

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Images lues par leur transcription ; les images 2 et 3 ont été ouvertes et confirment la transcription.

1. **`^` « XOR logique »** (complément) : en C, `^` est un OU exclusif bit à bit, il n'existe pas de XOR logique.
2. **Taille du tableau « écrite en dur »** (complément) : le cours interdit `int n; int tab[n];`. En C99, un tableau de taille variable est permis si `n` a une valeur. L'exemple du cours est de toute façon incorrect, `n` n'étant pas initialisé.
3. **Fonction `affiche_points`** : `i` et `j` ne sont pas déclarés dans le code de l'image. Alerte des transcriptions confirmée par le texte.
4. **Haut de plusieurs images coupé** (tableau des opérateurs, `if/else`) : une ligne de texte n'est pas lisible, sans conséquence sur le contenu.
5. **Remarque sur le `for`** : le passage surligné dans l'image dit que `i` vaut 10 après la boucle. Cette remarque est juste.
6. **Coquilles de l'image du `for`** : « ouvent » (pour « souvent ») et « optionnelle » au singulier ; corrigées ici, sans effet sur le sens.
7. **Image des tableaux coupée** : elle finit sur « L'exemple suivant : » sans l'exemple annoncé.
