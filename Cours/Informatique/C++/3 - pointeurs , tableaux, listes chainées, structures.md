---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/C++/Chp3 - pointeurs , tableaux, listes chainées, structures.docx|Chp3 - pointeurs , tableaux, listes chainées, structures]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 4/C++/Chp3 - pointeurs , tableaux, listes chainées, structures.docx|Chp3 - pointeurs , tableaux, listes chainées, structures]], dans [[Cours/Informatique/C++/_index|C++]]. Le code est du [[Langage C|C]].
## Idée générale

Comment la mémoire se représente (adresses, tableaux contigus), comment les pointeurs la manipulent, puis ce qu'on en tire : passage par adresse, tableaux en paramètre, `struct`, listes chaînées, doubles pointeurs.

Le cours suit un même schéma mémoire sur plusieurs diapositives : une colonne d'adresses, une colonne d'indices, une colonne de valeurs. Les figures sont reprises ci-dessous dans l'ordre.

## 1. Création d'un tableau

La création d'un tableau alloue chaque élément de façon **contiguë en mémoire**.

```c
int effectifs[6];   // allocation de la mémoire : 6 fois la taille d'un entier
```

![[Chp3 - pointeurs , tableaux, listes chainées, structures - image13.png]]

*Figure : les 6 cases de `effectifs`, chacune avec son adresse (0x16fdab76 à 0x16fdab8a), son indice (0 à 5) et 4 sous-cases pour les 4 octets d'un entier.*

Ce que dit la diapositive :

- Une adresse est souvent affichée en [[Notation hexadécimale|notation hexadécimale]] et commence par **0x**. Un [[Octet|octet]] se code sur 2 chiffres hexadécimaux ; 32 bits = 4 octets = 8 chiffres hexadécimaux.
- **Adresse** : entier désignant l'emplacement où est stockée la donnée. Sa taille dépend de l'architecture : 4 octets (32 bits) sur système 32 bits, 8 octets (64 bits) sur système 64 bits.
- **Taille d'un entier** : un `int` fait en général 4 octets, sur les systèmes 32 bits comme sur les systèmes 64 bits courants (modèles LP64 de Linux et macOS, LLP64 de Windows) ; ce sont les pointeurs, et le `long` en LP64, qui passent à 8 octets en 64 bits. [[Erreurs du cours#^e-3-pointeurs-tableaux-listes-chainees-structures|✎]]

![[Chp3 - pointeurs , tableaux, listes chainées, structures - image4.png]]

*Figure : les adresses des 6 cases se suivent, de 4 en 4.*

- L'allocation est **contiguë** : les adresses se suivent, de 4 en 4 car un entier fait 4 octets.
- C'est **efficace** (rapide) lors de traitements répétés.
- Pourquoi c'est rapide : l'adresse de la case `i` se calcule directement, $\text{adresse}(t[i]) = \text{adresse}(t[0]) + i \times \text{taille du type}$, donc l'accès à n'importe quelle case prend un temps constant ; et des cases voisines sont chargées ensemble dans la [[Mémoire cache|mémoire cache]] du processeur, ce qui accélère les parcours. [[Complément hors du cours|ⓘ]]

## 2. Variables typées

```c
int capacite;        // allocation de la mémoire : 1 fois la taille d'un entier
int effectifs[6];    // allocation de la mémoire : 6 fois la taille d'un entier
```

![[Chp3 - pointeurs , tableaux, listes chainées, structures - image1.png]]

*Figure : `capacite` occupe la case 0x16fdab72, juste avant les 6 cases de `effectifs`.*

- Toute allocation en mémoire est référencée par une **adresse**.
- Le C demande de connaître le **type** (pour prévoir la place à allouer) et la **taille** (nombre de cases du tableau, pour prévoir une place contiguë) dès le début d'un bloc.
- L'opérateur `sizeof` donne la taille en octets d'un type ou d'une variable : `sizeof(char)` vaut 1 par définition, `sizeof(int)` vaut en général 4, et, dans la fonction où le tableau est déclaré, `sizeof(effectifs)` vaut $6 \times 4 = 24$. D'où l'idiome `sizeof(effectifs) / sizeof(effectifs[0])` pour obtenir le nombre de cases. [[Complément hors du cours|ⓘ]]

## 3. Adresses

```c
effectifs[1] = 38;
capacite = effectifs[1];
```

![[Chp3 - pointeurs , tableaux, listes chainées, structures - image8.png]]

*Figure : après ces deux lignes, `capacite` et `effectifs[1]` contiennent 38 ; la colonne des adresses est « ce qu'utilise la machine ».*

Dans certaines situations, il est préférable, voire obligatoire, d'utiliser directement les adresses :

- le passage de référence à des fonctions ;
- la manipulation de données complexes ou volumineuses ;
- l'allocation de mémoire.

**On utilise les pointeurs pour stocker et utiliser les adresses.**

### Obtenir et afficher une adresse

```c
printf("l'adresse de capacite est %p", &capacite);
// l'adresse de capacite est 0x16fdab72
```

![[Chp3 - pointeurs , tableaux, listes chainées, structures - image5.png]]

*Figure : `&capacite` désigne la case 0x16fdab72.*

- `&` donne l'**adresse** d'une variable.
- Le code de format `%p` affiche une adresse.

### Le nom d'un tableau est l'adresse de sa première case

```c
for(i=0;i<6;i++) printf("l'adresse de effectifs[%d] est %p \n", i, &effectifs[i]);
```

![[Chp3 - pointeurs , tableaux, listes chainées, structures - image9.png]]

*Figure : schéma mémoire et sortie du terminal ; les adresses affichées avancent de 4 en 4 (0x16d383610, …614, …618, …61c, …620, …624).*

```c
for(i=0;i<6;i++) printf("l'adresse de effectifs[%d] est %p \n", i, effectifs+i);
```

![[Chp3 - pointeurs , tableaux, listes chainées, structures - image3.png]]

*Figure : le nom `effectifs` pointe sur la case d'indice 0.*

- Le nom du tableau est aussi l'adresse de son premier élément.
- Une adresse est un nombre entier : on peut lui ajouter ou retrancher une valeur, un indice (essentiellement additions et soustractions). Voir [[Arithmétique des pointeurs]].
- **Ajouter ou soustraire un entier à une adresse revient à se décaler en mémoire de la taille du type concerné.** Avec des `int`, ajouter 1 décale de 4 octets (en 32 comme en 64 bits). [[Erreurs du cours#^e-3-pointeurs-tableaux-listes-chainees-structures|✎]]
- La différence de deux pointeurs sur un même tableau donne le **nombre d'éléments** qui les séparent, pas le nombre d'octets : `&effectifs[5] - &effectifs[1]` vaut 4. Additionner deux pointeurs, en revanche, n'a pas de sens et ne compile pas. [[Complément hors du cours|ⓘ]]

## 4. Manipuler les adresses : les pointeurs

Voir [[Pointeur et adresse mémoire]].

```c
int *ptr;   // ici l'opérateur * indique que ptr est un pointeur sur entier
```

Un pointeur est une **variable** destinée à contenir une **adresse**. On peut :

- l'initialiser ;
- l'afficher ;
- lui affecter des valeurs (des adresses) ;
- lui ajouter ou soustraire des entiers (décalage) ;
- accéder à son contenu.

![[Chp3 - pointeurs , tableaux, listes chainées, structures - image21.png]]

*Figure : `ptr` est une case mémoire de plus (0x16fdab8e), encore vide.*

### L'initialiser

```c
int *ptr;
ptr = &capacite;   // ptr est destiné à recopier des adresses d'entiers
```

![[Chp3 - pointeurs , tableaux, listes chainées, structures - image14.png]]

*Figure : l'adresse de `capacite` (0x16fdab72) est recopiée dans la case de `ptr`.*

### L'afficher

```c
printf("%p \n", ptr);
```

![[Chp3 - pointeurs , tableaux, listes chainées, structures - image16.png]]

*Figure : `ptr` contient 0x16fdab72, l'adresse de `capacite`.*

### Lui affecter une adresse, la décaler

```c
int *ptr;
ptr = effectifs+3;
```

![[Chp3 - pointeurs , tableaux, listes chainées, structures - image7.png]]

*Figure : `effectifs+3` désigne la case d'indice 3 (0x16fdab82), adresse rangée dans `ptr`.*

### Accéder à son contenu (déréférencement)

```c
ptr = &capacite;
printf("valeur pointée par ptr : %d", *ptr);   // valeur pointée par ptr : 38
int calc = *ptr;                                // calc = 38
```

![[Chp3 - pointeurs , tableaux, listes chainées, structures - image27.png]]

*Figure : `ptr` contient l'adresse de `capacite` ; la flèche rouge va de `ptr` vers `capacite`.*

L'opérateur `*` accolé au nom du pointeur donne accès à la valeur rangée à l'adresse que contient le pointeur.

Le symbole `*` a donc deux rôles : dans une **déclaration** (`int *ptr;`), il dit que `ptr` est un pointeur ; dans une **expression** (`*ptr`), il déréférence. Piège classique : `int *p, q;` déclare un pointeur `p` et un entier `q`, l'étoile ne s'applique qu'au nom qui la suit. [[Complément hors du cours|ⓘ]]

Déréférencer un pointeur qui n'a pas été initialisé ([[Variable non initialisée]]) lit ou écrit à une adresse quelconque : c'est un comportement indéfini, qui se termine souvent par une [[Erreur de segmentation]]. D'où la règle : initialiser tout pointeur, au besoin à `NULL`. [[Complément hors du cours|ⓘ]]

## 5. Résumé des opérations sur les pointeurs

- Pour afficher une adresse : `%p` ; `%d` ne convient pas, car une adresse de 64 bits ne tient pas dans un `int` et s'affiche tronquée ou fausse. [[Erreurs du cours#^e-3-pointeurs-tableaux-listes-chainees-structures|✎]]
- `&X` : « adresse de X ».
- `*X` : « contenu de l'adresse pointée par X ».

### Programme complet commenté

Code du cours, avec ses commentaires résumés ; le pointeur du bloc alloué s'appelle `buffer` d'un bout à l'autre, et `free` libère le bloc sans effacer son contenu : [[Erreurs du cours#^e-3-pointeurs-tableaux-listes-chainees-structures|✎]]

```c
int main() {
    int i;
    i = 1;
    int *p;   // p doit contenir une adresse : int *p = adresse d'un int,
              // float *p = adresse d'un float... L'étoile « devrait aller »
              // avec le int (int* p) : c'est elle qui déclare un pointeur sur int.
    printf("1) adresse de i: %p\n", &i);
    p = &i;   // & donne l'adresse mémoire de la variable
    printf("2) adresse dans p: %p\n", p);
    printf("3) valeur pointée par p: %d\n", *p);  // p contient l'adresse de i, i vaut 1, donc *p = 1
    *p = 2;   // modifie la valeur rangée à l'adresse contenue dans p, donc i
    printf("4) valeur pointée par p: %d\n", *p);  // 2
    printf("4bis) valeur de i: %d\n", i);         // 2

    unsigned char c;
    unsigned char *buffer;   // pointeur vers un unsigned char
    buffer = malloc(sizeof(unsigned char) * 10);
        // malloc (memory allocation) : 10 octets réservés dans le tas (heap).
        // buffer ne contient PAS les 10 octets, mais l'ADRESSE du bloc.
    printf("5) adresse dans buffer: %p\n", buffer);
    unsigned char *pb = buffer;         // pb contient la même adresse
    printf("6) adresse dans pb: %p\n", pb);
    pb++;                               // avance d'un octet (taille d'un unsigned char)
    printf("7) adresse dans pb: %p\n", pb);
    free(buffer);   // rend le bloc, sans effacer son contenu ; après chaque malloc, TOUJOURS free
    printf("8) adresse dans buffer: %p\n", buffer);
    printf("9) adresse dans pb: %p\n", pb);
        // 8 et 9 : même après libération, les pointeurs gardent leur adresse
    return 0;
}
```

Sortie donnée par le cours :

```
1) adresse de i: 140732656702476
2) adresse dans p: 140732656702476
3) valeur pointée par p: 1
4) valeur pointée par p: 2
4bis) valeur de i: 2
5) adresse dans buffer: 93886705493680
6) adresse dans pb: 93886705493680
7) adresse dans pb: 93886705493681
8) adresse dans buffer: 93886705493680
9) adresse dans pb: 93886705493681
```

**Pile et tas.** Les variables locales (`i`, `p`, `pb`) sont rangées sur la [[Pile d'exécution|pile]] (*stack*) : elles sont créées à l'entrée du bloc et disparaissent automatiquement à sa sortie. Le bloc réservé par `malloc` est sur le **tas** (*heap*) : il existe jusqu'au `free`, quelle que soit la fonction en cours. Les deux zones font partie de l'[[Espace mémoire d'un processus]]. La sortie du cours le montre : converties en hexadécimal, l'adresse de `i` (0x7ffee002d40c) est tout en haut de l'espace d'adressage, là où se trouve la pile, celle du bloc alloué (0x5563b3bae6b0) beaucoup plus bas, dans le tas. [[Complément hors du cours|ⓘ]]

`malloc` renvoie `NULL` quand l'allocation échoue : on teste le résultat avant de s'en servir (`if (buffer == NULL) { … }`). En C, le `void *` qu'il renvoie se convertit seul vers `unsigned char *` ; en C++, il faut un transtypage explicite, et l'on préfère `new` et `delete` (`new unsigned char[10]`, puis `delete[]`). [[Complément hors du cours|ⓘ]]

**Pointeur pendant.** Les lignes 8 et 9 le montrent : après `free`, `buffer` et `pb` contiennent encore l'adresse du bloc libéré. Un tel pointeur est dit **pendant** (*dangling pointer*) : lire ou écrire à travers lui est un comportement indéfini, car le bloc peut avoir été réattribué. Bonne pratique : remettre le pointeur à `NULL` juste après le `free`, et ne jamais libérer deux fois le même bloc. Voir [[Pointeur pendant]]. [[Complément hors du cours|ⓘ]]

**Fuite mémoire.** À l'inverse, perdre l'adresse d'un bloc sans l'avoir libéré (oubli du `free`, pointeur écrasé) le rend inaccessible jusqu'à la fin du programme : c'est une [[Fuite mémoire|fuite mémoire]], grave dans un programme qui tourne longtemps. Des outils comme Valgrind les détectent. [[Complément hors du cours|ⓘ]]

Notions liées : [[Allocation dynamique]], [[Type primitif]] (`unsigned char`), [[Fonctions printf et scanf]].

## 6. Fonctions : paramètres par valeur, puis par adresse

### Version par valeur

```c
#include <stdio.h>

void echange(int a, int b);

int main(){
    int var1 = 10;
    int var2 = 20;
    printf("var1 : %d, var2 : %d \n", var1, var2);
    echange(var1, var2);
    printf("var 1 : %d , var2 : %d \n", var1, var2);
    return 0;
}

void echange(int a, int b){
    int temp;
    printf("a : %d , b : %d\n", a, b);
    temp = a;
    a = b;
    b = temp;
    printf("a : %d, b :%d \n", a, b);
}
```

Déroulé en mémoire, sur la [[Pile d'exécution|pile]] :

1. Au lancement, on entre dans la [[Fonction main (C et C++)|fonction `main`]] : `var1 = 10` et `var2 = 20` sont empilés.

![[Chp3 - pointeurs , tableaux, listes chainées, structures - image15.png]]

*Figure : la pile ne contient que `var1` (10) et `var2` (20).*

2. On entre dans `echange(var1, var2)` : un cadre est empilé avec les paramètres `a = 10`, `b = 20` (des **copies**) et la variable locale `temp`. La flèche est sur `temp = a;`. [[Erreurs du cours#^e-3-pointeurs-tableaux-listes-chainees-structures|✎]]

![[Chp3 - pointeurs , tableaux, listes chainées, structures - image36.png]]

*Figure : cadre `echange` (`temp` 10, `b` 20, `a` 10) au-dessus du cadre `main` (`var2` 20, `var1` 10).*

3. Après `a = b; b = temp;` : dans le cadre `echange`, `a = 20`, `b = 10`, `temp = 10`. Le cadre `main` n'a pas changé.

![[Chp3 - pointeurs , tableaux, listes chainées, structures - image35.png]]

*Figure : seules les copies `a` et `b` ont été échangées.*

4. Retour dans `main` : le cadre de `echange` est retiré de la pile. Le second `printf` affiche toujours `var1 : 10, var2 : 20`.

![[Chp3 - pointeurs , tableaux, listes chainées, structures - image28.png]]

*Figure : le cadre `echange` est barré ; `var1` et `var2` sont inchangés.*

À la fin de `main`, il ne reste que `var2` et `var1` dans la pile. C'est le [[Passage par valeur]].

### Version par adresse

```c
#include <stdio.h>

void echange(int *a, int *b);   // echange prend en paramètre des adresses

int main(){
    int var1 = 10;
    int var2 = 20;
    printf("var1 : %d, var2 : %d \n", var1, var2);
    echange(&var1, &var2);      // on passe les adresses de var1 et var2
    printf("var 1 : %d , var2 : %d \n", var1, var2);
    return 0;
}

void echange(int *a, int *b){
    int temp;
    printf("a : %d , b : %d\n", *a, *b);  // valeurs rangées aux adresses de a et b : 10 et 20
    temp = *a;                            // temp vaut la valeur pointée par a
    *a = *b;                              // échange des valeurs de var1 et var2
    *b = temp;
    printf("a : %d, b : %d \n", *a, *b);
}
```

1. Dans `main` : `var1 = 10` en 0xabdafa0, `var2 = 20` en 0xabdafa4.

![[Chp3 - pointeurs , tableaux, listes chainées, structures - image12.png]]

*Figure : cadre `main` avec les adresses de `var1` et `var2`.*

2. Appel `echange(&var1, &var2)` : `echange` reçoit les **adresses** de `var1` et `var2`, d'où la signature `echange(int *a, int *b)` : `a` et `b` sont des pointeurs qui contiennent 0xabdafa0 et 0xabdafa4.

![[Chp3 - pointeurs , tableaux, listes chainées, structures - image19.png]]

*Figure : `a` contient l'adresse de `var1`, `b` celle de `var2` ; la variable locale `temp` occupe sa propre case, au-dessus de `b` (0xabdafac), en 0xabdafb0.* [[Erreurs du cours#^e-3-pointeurs-tableaux-listes-chainees-structures|✎]]

3. Dans `echange`, l'échange se fait avec `*a` et `*b`, qui accèdent aux valeurs rangées aux adresses contenues dans `a` et `b` : `var1` vaut maintenant 20 et `var2` 10.

![[Chp3 - pointeurs , tableaux, listes chainées, structures - image26.png]]

*Figure : flèches de `a` vers `var1` et de `b` vers `var2` ; les valeurs de `main` sont échangées.*

En réalité, le C ne connaît que le passage par valeur : ici, ce sont les **adresses** qui sont copiées dans `a` et `b`, mais, comme la copie d'une adresse désigne toujours la même case, la fonction peut modifier l'original. C'est ce qu'on appelle couramment le passage « par adresse ». [[Complément hors du cours|ⓘ]]

En C++, le même échange s'écrit sans pointeurs, avec un passage par [[Référence (C++)|référence]] : `void echange(int &a, int &b) { int temp = a; a = b; b = temp; }`, appelé par `echange(var1, var2);`. La bibliothèque standard fournit d'ailleurs `std::swap` (en-tête `<utility>`). [[Complément hors du cours|ⓘ]]

## 7. Fonctions et tableaux : deux manières de faire

**Version pointeur** :

```c
#include <stdio.h>

void init_tab(float *t){            // voir commentaire 1
    for (int i=0; i<100; i++){
        *(t+i) = 1.0;               // accède à la case mémoire t+i
    }
}

void affiche_tab(float *t){         // affiche le tableau
    for (int i=0; i<100; i++){
        printf("%f\n", *(t+i));
    }
}

int main(){
    float tab[100];
    init_tab(tab);                  // voir commentaire 2
    affiche_tab(tab);
    return 0;
}
```

- **Commentaire 1** : `init_tab` remplit toutes les cases avec 1.0. Elle reçoit `(float *t)` : à l'appel, elle reçoit l'**adresse** du tableau grâce au pointeur sur `float`.
- **Commentaire 2** : pourquoi `init_tab(tab)` et non `init_tab(&tab)` ou `init_tab(tab[100])` ? Employé seul dans une expression, sans crochets, le nom `tab` subit la **décroissance du tableau en pointeur** (*array decay*) : il est converti en l'adresse de son premier élément, `&tab[0]`. Donc `init_tab(tab)` = `init_tab(&tab[0])`.

**Version tableau** :

```c
#include <stdio.h>

void init_tab(float t[]){
    for (int i = 0; i<100; i++){
        t[i] = 1.0;
    }
}

void affiche_tab(float t[]){
    for (int i=0; i<100; i++){
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

Équivalence : $t[i] \iff *(t + i)$.

Syntaxes équivalentes, la fonction reçoit l'adresse de la première case :

```c
void init_tab(float *t)      // OK : syntaxe pointeur
void init_tab(float t[])     // OK : syntaxe tableau sans taille
void init_tab(float t[100])  // OK : la taille 100 est ignorée par le C
```

Conséquence de la décroissance : la fonction ne reçoit qu'une adresse et ignore la taille du tableau. Dans `init_tab`, `sizeof(t)` donne la taille d'un pointeur (8 octets en 64 bits), pas $100 \times 4$. C'est pourquoi on passe en général la taille en second paramètre, `void init_tab(float *t, int n)`, au lieu d'écrire 100 en dur dans la boucle. [[Complément hors du cours|ⓘ]]

Comme la fonction travaille sur l'adresse du tableau d'origine, tout ce qu'elle écrit dans `t[i]` modifie `tab` lui-même : un tableau n'est jamais copié lors d'un appel. Pour promettre qu'une fonction ne le modifie pas, on écrit `const` : `void affiche_tab(const float *t)`. [[Complément hors du cours|ⓘ]]

Voir [[Tableau (programmation)]].

## 8. Structures

Une variable classique contient une seule valeur ; un tableau en contient plusieurs, mais du même type. Une **structure** ([[Structure (struct)|`struct`]]) regroupe sous un même nom plusieurs variables de **types différents**. Exemple : un élève a un âge (`int`) et une moyenne (`float`).

**Sans `typedef`** :

```c
#include <stdio.h>

struct Etudiant {
    int age;
    float note;
};

int main() {
    struct Etudiant eleve1;
    eleve1.age = 20;
    eleve1.note = 15.5;
    printf("L'étudiant a %d ans %f/20.\n", eleve1.age, eleve1.note);
}
```

Il faut écrire `struct Etudiant eleve1;` pour créer une variable.

**Avec `typedef`** (`typedef` = alias) :

```c
#include <stdio.h>

typedef struct Etudiant {
    int age;
    float note;
} Etudiant;   // on remet Etudiant : ce sera l'alias

int main() {
    Etudiant eleve1;
    eleve1.age = 20;
    eleve1.note = 15.5;
    printf("L'étudiant a %d ans %f/20.\n", eleve1.age, eleve1.note);
}
```

L'alias s'écrit à la fin de `struct Etudiant {...}` ; on crée ensuite la variable avec `Etudiant` seul. On accède aux champs par `.` : `eleve1.age`.

Une structure s'initialise aussi d'un coup, dans l'ordre des champs : `Etudiant eleve1 = {20, 15.5};`. Contrairement à un tableau, elle est **copiée** quand on la passe à une fonction ou qu'on l'affecte (`eleve2 = eleve1;` recopie tous les champs) ; pour éviter la copie ou modifier l'original, on passe son adresse, `void majorer(Etudiant *e)`, et on accède aux champs par `e->note` (voir l'opérateur flèche, partie 10). [[Complément hors du cours|ⓘ]]

La taille d'une structure peut dépasser la somme de ses champs : le compilateur insère des octets de remplissage (*padding*) pour **aligner** chaque champ sur une adresse multiple de sa taille. Ainsi `struct { char c; int i; }` occupe en général 8 octets et non 5 ; `sizeof` donne la taille réelle. [[Complément hors du cours|ⓘ]]

En C++, une `struct` est une [[Classe et objet|classe]] dont les membres sont publics par défaut, et le mot `struct` n'est plus nécessaire devant le nom : `Etudiant eleve1;` suffit sans `typedef`. [[Complément hors du cours|ⓘ]]

## 9. Listes chaînées d'entiers

- Les tableaux sont en mémoire contiguë : les adresses s'enchaînent.
- Les [[Liste chaînée|listes chaînées]] ont des adresses dispersées.

**Définition** : une liste chaînée simple est une structure dynamique composée d'éléments (**cellules** ou **nœuds**), chacun :

- rangé en mémoire à une certaine adresse ;
- contenant une donnée (valeur de type quelconque) ;
- contenant un pointeur, souvent nommé `suivant`, vers l'adresse de l'élément suivant.

![[Chp3 - pointeurs , tableaux, listes chainées, structures - image29.png]]

*Figure : liste `L` de cinq cellules (0, 1, 4, 9, 16) ; chaque cellule a une valeur et un pointeur `suivant` (le rond), le dernier pointe vers `NULL`.*

**Remarques** :

- Le pointeur du dernier élément vaut [[Pointeur NULL|`NULL`]].
- Une liste est définie par l'adresse de son premier élément.
- Pour une liste vide, le pointeur du premier élément vaut `NULL`.
- En C++ moderne (depuis C++11), le pointeur nul s'écrit `nullptr`, mieux typé que `NULL`. [[Complément hors du cours|ⓘ]]

Le choix entre tableau et liste chaînée est un compromis, mesuré en [[Complexité algorithmique|complexité]] ($n$ = nombre d'éléments) : [[Complément hors du cours|ⓘ]]

| Opération | Tableau | Liste chaînée simple |
|---|---|---|
| Accès à l'élément $i$ | $O(1)$, par calcul d'adresse | $O(n)$, il faut suivre les `suivant` depuis le début |
| Ajout ou suppression en tête | $O(n)$, il faut décaler les cases | $O(1)$ |
| Ajout au milieu, position connue | $O(n)$ | $O(1)$ une fois la cellule précédente atteinte |
| Taille | fixée à la déclaration | varie librement à l'exécution |
| Mémoire | les données seules, contiguës | un pointeur de plus par cellule, cellules dispersées |

Variantes classiques : la liste **doublement chaînée**, dont chaque cellule pointe aussi vers la précédente (parcours dans les deux sens), et la liste **circulaire**, dont la dernière cellule pointe vers la première au lieu de `NULL`. Une liste chaînée sert aussi à réaliser une [[Pile et file|pile ou une file]]. [[Complément hors du cours|ⓘ]]

## 10. Pointeur simple et double pointeur

Un **double pointeur** (pointeur de pointeur) est une variable qui contient l'adresse d'un pointeur. Il sert à manipuler des pointeurs avec souplesse, notamment pour la gestion dynamique de la mémoire ou les tableaux 2D.

```c
type **nom_double_pointeur;
int **doublePtr;   // double pointeur vers un int
```

Le type de `doublePtr` est « pointeur vers un pointeur vers un `int` ». Il est utile quand :

- on veut pointer vers une variable qui est déjà un pointeur ;
- on doit **modifier l'adresse contenue dans un pointeur depuis une fonction**.

| Pointeur | Double pointeur |
|---|---|
| Contient l'adresse d'une variable | Contient l'adresse d'un pointeur |
| Manipule directement des variables | Manipule des pointeurs |
| Accès via `*` | Accès via `**` |

**Précautions** :

1. **Initialisation obligatoire** des pointeurs et doubles pointeurs avant usage.
2. **Gestion de mémoire** : un `free` pour chaque `malloc`.
3. **Vérifier `NULL`** avant d'accéder à un double pointeur.

![[Chp3 - pointeurs , tableaux, listes chainées, structures - image39.png]]

*Figure : `x` (10) en 0x1000, `ptr` (contient 0x1000) en 0x1004, `dptr` (contient 0x1004) en 0x1008.*

```c
int main() {
    int x = 10;
    int *ptr = &x;
    int **dptr = &ptr;
    int ***tptr = &dptr;
}
```

Avec ces déclarations, `*dptr` vaut `ptr` (0x1000) et `**dptr` vaut `x` (10) : chaque `*` remonte d'un cran le long des flèches. Écrire `**dptr = 20;` modifie donc `x`. [[Complément hors du cours|ⓘ]]

Exemple courant de double pointeur : la signature `int main(int argc, char **argv)`. Une chaîne de caractères est un `char *` ; `argv` est un tableau de chaînes (les arguments de la ligne de commande), donc un `char **`. [[Complément hors du cours|ⓘ]]

### L'opérateur flèche

```c
// Les deux lignes suivantes font exactement la même chose :
nouveau->valeur = 30;    // syntaxe propre et lisible avec ->
(*nouveau).valeur = 30;  // syntaxe lourde (parenthèses obligatoires)
```

Voir [[Opérateur flèche]].

### Exemple complet : liste chaînée

```c
#include <stdio.h>
#include <stdlib.h>

// Définition d'un chaînon
typedef struct Chainon {
    int valeur;
    struct Chainon *suivant;   // pointeur vers le chaînon suivant
} Chainon;

// 1. Modifier 'premier' -> on utilise Chainon **
void ajouter_au_debut(Chainon **premier_ptr, int nouvelle_valeur) {
    // Étape A : créer un nouveau chaînon en mémoire
    Chainon *nouveau = malloc(sizeof(Chainon));
    nouveau->valeur = nouvelle_valeur;
    // Étape B : faire pointer 'suivant' vers l'ANCIEN premier chaînon
    nouveau->suivant = *premier_ptr;
    // Étape C : modifier 'premier' pour qu'il pointe vers le NOUVEAU chaînon
    *premier_ptr = nouveau;
}

// 2. Lire la liste sans la modifier -> on utilise Chainon *
void afficher_liste(Chainon *premier) {
    Chainon *courant = premier;   // pointeur temporaire pour se déplacer
    while (courant != NULL) {
        printf("[%d] -> ", courant->valeur);
        courant = courant->suivant;   // on saute au chaînon suivant grâce à son adresse
    }
    printf("NULL\n");
}

int main() {
    Chainon *premier = NULL;   // au départ, la liste est vide
    // On passe l'ADRESSE de premier (&premier) pour pouvoir le modifier
    ajouter_au_debut(&premier, 7);
    ajouter_au_debut(&premier, 12);
    // On passe juste le pointeur 'premier' pour lire
    afficher_liste(premier);
    return 0;
}
```

Méthode d'ajout en tête, étape par étape : (A) allouer le nouveau chaînon et y ranger la valeur ; (B) son `suivant` reçoit l'ancien premier ; (C) le premier devient le nouveau chaînon, d'où le passage de `&premier` et le type `Chainon **`. Le cours ne donne pas la sortie ; d'après le code, elle serait `[12] -> [7] -> NULL` (déduction, non écrite dans la note). Les chaînons alloués ne sont pas libérés par ce programme.

Pour libérer la liste, on parcourt les chaînons en gardant l'adresse du suivant **avant** le `free`, puisque après lui on ne doit plus lire `courant->suivant` (pointeur pendant) : [[Complément hors du cours|ⓘ]]

```c
void liberer_liste(Chainon **premier_ptr) {
    Chainon *courant = *premier_ptr;
    while (courant != NULL) {
        Chainon *suivant = courant->suivant;  // sauvegarde avant libération
        free(courant);
        courant = suivant;
    }
    *premier_ptr = NULL;   // la liste est vide, plus de pointeur pendant
}
// dans main, avant return 0 : liberer_liste(&premier);
```
