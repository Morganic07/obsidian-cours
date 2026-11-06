---
type: source
tags: [year4]
sources: ["[[Chp1 - basiques]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Chp1 - basiques]], dans [[C++ (matière)]]. Le contenu est du [[Langage C|langage C]] (mots réservés du C, `printf`, `scanf`, `malloc`), pas du C++. En cas d'écart, le cours et ses images font foi.

## Idée générale

Syntaxe de base du C, types, mémoire (pile), erreurs de compilation, puis une série de « questions pièges » sur des pièges classiques du langage.

Les quatre images de la note ne contiennent que du texte : leur contenu est recopié ci-dessous.

## 1. Syntaxe

- Finir chaque instruction par `;`.
- Les blocs d'instructions sont délimités par `{ }`.
- Indenter le code.
- Pas de nom de fonction qui commence par un chiffre.
- Pas d'espace dans les noms de variables ou de fonctions.
- Ne pas utiliser `-` dans un nom : il est interprété comme un « moins ».

### Mots réservés

Les [[Mot réservé|mots réservés]] sont les mots prédéfinis du langage C. Ils ne peuvent pas être réutilisés comme identifiants. Classés par concept :

| Catégorie | Mots |
|---|---|
| Type des données | `char const double float int long short signed unsigned void volatile` |
| Instructions de boucle | `do for while` |
| Sélections | `case default else if switch` |
| Ruptures de séquence | `break continue goto return` |
| Classes d'allocation (vues plus tard) | `auto extern register static` |
| Constructeurs (vus plus tard) | `enum struct typedef union` |
| Divers | `asm entry fortran sizeof` |

## 2. Types de base et variables

1. **`void`** : le type vide, introduit par la norme ANSI. Sert surtout à préciser les fonctions sans argument ou sans retour.
2. **`int`** : le type entier. Qualificatifs de taille (`long`, `short`) et de signe : `unsigned` (positif seulement) ou `signed` (positif et négatif). `signed` est appliqué par défaut : `int` et `signed int` sont identiques.
3. **`char`** : support du [[Code ASCII|code ASCII]] pour représenter les caractères ; peut aussi représenter un entier sur 8 bits. Peut être déclaré signé (`char`) ou non signé (`unsigned char`) (voir [[Type primitif]]).
4. **`float`** : représentation des réels (avec partie décimale).
5. **`double`** : comme `float`, avec une précision plus importante.
6. **`long double`** : comme `double`, avec une précision encore plus grande.

### `printf` et `scanf`

Les [[Fonctions printf et scanf|séquences de contrôle]] commencent par `%` suivi de :

| Séquence | Affiche |
|---|---|
| `%d` ou `%i` | un entier signé en décimal (`int`) |
| `%u` | un entier non signé en décimal |
| `%o` | un entier en octal |
| `%x` ou `%X` | un entier en [[Notation hexadécimale\|hexadécimal]] (lettres `abcdef` avec `x`, `ABCDEF` avec `X`) |
| `%f` | un réel (`float` et `double`) |
| `%c` | un caractère |
| `%s` | une chaîne de caractères |

D'autres séquences existent, non abordées dans le cours.

```c
printf("%d kilogramme équivaut à %d grammes", 1, 1000);
scanf("%d", &i);   /* lit un entier et le range à l'adresse de i */
```

Pour afficher une valeur numérique, des **modificateurs de format** ajustent la forme ou la longueur de l'affichage, par exemple `%3d` (largeur 3) et `%03d` (largeur 3 complétée par des zéros).

## 3. Gestion mémoire

Le C oblige à déclarer le type de chaque variable pour une raison physique : le compilateur ne devine rien, et la mémoire n'est qu'une suite de 0 et de 1. Pour la machine, `01000001` peut être l'entier 65, la lettre `'A'` ou le début d'un nombre à virgule. Le type remplit trois rôles.

### Savoir combien de place réserver

Le compilateur réserve une « boîte » en [[Mémoire vive|mémoire vive]] dont la taille dépend du type :

| Déclaration | Place réservée |
|---|---|
| `char c;` | 1 [[Octet\|octet]] (8 bits) |
| `int n;` | en général 4 octets (32 bits) |
| `double d;` | en général 8 octets (64 bits) |

Sans type, le compilateur ne saurait pas où commence et où finit la variable suivante.

### Savoir comment interpréter les bits

La même suite binaire change de sens selon le type :

- lue comme un **entier signé** (`int`) sur 4 octets : arithmétique en [[Complément à deux|complément à deux]] ;
- lue comme un **nombre à virgule** (`float`) : [[Norme IEEE 754|norme IEEE 754]] (signe, exposant, mantisse) ;
- lue comme un `char` sur 1 octet : la table ASCII donne le caractère affiché.

Le type est la « notice de lecture » qui indique au processeur quelles instructions machine exécuter (instruction arithmétique classique ou instruction de l'unité de calcul flottant, FPU).

### Garantir la sécurité à la compilation

Le C est un langage à [[Typage statique|typage statique]] : les vérifications sont faites **avant** l'exécution, à la compilation.

```c
int total = 10;
char *texte = "salut";
int resultat = total + texte; // Erreur ou avertissement direct du compilateur
```

D'après le cours, le compilateur bloque parce qu'additionner un entier et une [[Pointeur et adresse mémoire|adresse mémoire]] de chaîne n'a pas de sens ; détecter cela à la compilation évite des plantages (*[[Erreur de segmentation|segmentation fault]]*) ou des comportements imprévisibles à l'exécution (voir le point 3 à vérifier).

### Variables gérées en pile

Une variable déclarée normalement dans une fonction est placée sur la **pile** (*stack*), qui fonctionne en **LIFO** (*Last In, First Out*), comme une pile d'assiettes :

- **Empiler (*push*)** : à l'appel d'une fonction, un *[[Pile d'exécution|cadre de pile]]* (*stack frame*) est posé au sommet ; il contient les variables locales, les paramètres et l'adresse de retour.
- **Dépiler (*pop*)** : à la fin de la fonction (`return` ou accolade fermante), le processeur déplace un curseur (le registre *stack pointer*) ; tout le cadre est libéré instantanément.

```c
void calculer(void) {
    int a = 5;   // Empilé au sommet
    int b = 10;  // Empilé au-dessus de 'a'
}                // Sortie de fonction : 'b' puis 'a' sont dépilés automatiquement.
```

## 4. Erreurs du compilateur

Messages fréquents d'[[Erreur de compilation|erreur de compilation]] ([[GCC]]) :

| Message | Cause |
|---|---|
| `error: expected ';' before...` | un point-virgule oublié |
| `error: expected declaration or statement at end of input` | une accolade oubliée |
| `error: 'nom_variable' undeclared (first use in this function)` | variable non déclarée (ou mal orthographiée) |
| `a.c:(.text+0x19): undefined reference to 'nom_fonction'` puis `collect2: error: ld returned 1 exit status` | fonction inconnue du compilateur (mal orthographiée ?) |
| `fatal error: nom_fichier.h: Aucun fichier ou dossier de ce type` | fichier d'en-tête inclus mal orthographié |

## 5. Le type `char` : un entier déguisé

En C, `char` est un **entier sur 1 octet** (8 bits). L'ordinateur ne stocke que des nombres ; la correspondance nombre-lettre est donnée par la table ASCII. Écrire `'A'` ou `65` revient strictement au même pour le compilateur.

| Code écrit | Valeur stockée |
|---|---|
| `c = 65;` | 65 (binaire `01000001`) |
| `c = 'A';` | 65 (binaire `01000001`) |
| `c = 'B';` | 66 (binaire `01000010`) |

### Le rôle de `printf` : une question de lunettes

La variable ne sait pas si elle est texte ou nombre : c'est le **spécificateur de format** qui choisit comment lire les bits.

- `%d` : affiche la valeur comme entier ;
- `%c` : affiche le symbole correspondant dans la table ASCII.

```c
char lettre = 66;        // Équivalent à : char lettre = 'B';
printf("%d\n", lettre);  // Affiche : 66
printf("%c\n", lettre);  // Affiche : B
```

## 6. Spécificités du C : questions pièges

### Triple égalité `a == b == c`

L'expression ne teste pas que les trois variables sont égales. Avec `a = b = c = 5` :

1. Le compilateur groupe de gauche à droite : `(a == b) == c` (voir [[Associativité et ordre d'évaluation]]).
2. `a == b` : `5 == 5`, vrai.
3. En C, il n'y a pas de mot « vrai » : une condition vraie vaut `1`, fausse `0`. La première partie devient `1`.
4. `1 == c` : `1 == 5`.
5. Faux : l'expression vaut `0`.

Remplacements proposés par le cours :

```c
if (a == b && b == c)
if ( ((a==b) == 1) == (b==c) )   // voir le point 2 à vérifier
```

### Pas besoin d'accolades pour une seule instruction

Pour `if`, `else`, `for`, `while`, etc., les accolades sont facultatives quand il n'y a qu'une instruction (voir [[Structure conditionnelle]], [[Boucle (programmation)]]) :

```c
if (a==0) printf("bonjour");
```

### Affectation dans une condition

```c
int a = 10;
if (a=3) printf("bonjour");   // et pas (a==3)
```

Résultat : affiche « bonjour ». Le cours écrit que `if (a=3)` « teste si `a` peut prendre la valeur 3 » et renvoie 1 si oui, 0 sinon (explication à corriger, voir le point 1 à vérifier ; voir aussi [[Affectation]]).

### Point-virgule après un `if`

```c
int x = 0;
if (x==5);          // piège : le ';' termine le if, qui n'a pas d'instruction
{ printf("A"); }    // accolades inutiles : ça compile quand même
printf("B");
```

Résultat : `AB`. Le `;` forme une [[Instruction vide|instruction vide]].

### Le « OU » paresseux (*lazy operator*)

`||` lit la condition de gauche à droite et s'arrête dès qu'une partie est vraie ([[Évaluation en court-circuit]], [[Opérateur logique]]).

```c
int x = 10;
int y;
if (x>5 || (y=20)) {
    printf("vrai");
}
```

`x>5` est vrai, donc `(y=20)` n'est jamais évalué : `y` n'est pas affecté.

```c
int x = 10;
int y;
if ((y=20) || x>5) {
    printf("vrai");
}
printf("y = %d", y);
// Retourne : vrai y = 20
```

Ici `(y=20)` est évalué en premier (valeur 20, donc vrai) : inutile de tester `x>5`, « vrai » s'affiche, et `y` vaut 20.

### Afficher une variable non initialisée

```c
int y;
printf("y = %d", y);   // y = [valeur aléatoire]
```

Voir [[Variable non initialisée]].

### Boucle infinie

```c
int x = 5;
while(x<10);
x++;
```

Le `;` après le `while` donne une boucle dont le corps est vide : la condition reste toujours vraie (rien n'incrémente `x`), la boucle tourne à vide et `x++` n'est jamais exécuté.

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
9. **`malloc`** : l'introduction du résumé cite `malloc`, mais cette note n'en parle pas ; il apparaît dans les chapitres suivants (voir [[Chp3 - pointeurs , tableaux, listes chainées, structures (résumé)]]).
