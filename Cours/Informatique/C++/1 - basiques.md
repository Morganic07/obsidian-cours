---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/C／C++/Chp1 - basiques.docx|Chp1 - basiques]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 4/C／C++/Chp1 - basiques.docx|Chp1 - basiques]], dans [[Cours/Informatique/C++/_index|C++]]. Le contenu est du [[Langage C|langage C]] (mots réservés du C, `printf`, `scanf`, `malloc`), pas du C++.
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
- La règle générale des identifiants (noms de variables et de fonctions) : des lettres, des chiffres et le tiret bas `_`, sans commencer par un chiffre (`note_2` est permis, `2note` ne l'est pas) ; les lettres accentuées ne sont pas acceptées par tous les compilateurs, d'où l'usage de s'en tenir aux lettres sans accent. Le C distingue majuscules et minuscules : `total` et `Total` sont deux variables différentes. [[Complément hors du cours|ⓘ]]

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

Dans la ligne « Divers », `entry` est un vestige du tout premier C, réservé mais jamais utilisé, et `asm` (insérer de l'assembleur) et `fortran` sont des extensions de certains compilateurs, absentes de la norme ANSI. Le seul mot de cette ligne d'usage courant est `sizeof`, un opérateur qui donne la taille en octets d'un type ou d'une variable : `sizeof(int)` vaut en général 4. Les normes suivantes ont ajouté des mots, par exemple `inline` et `_Bool` en C99 ; en C23, `bool`, `true` et `false` deviennent eux aussi des mots réservés. [[Complément hors du cours|ⓘ]]

Deux qualificatifs de type de la table méritent une explication. `const` interdit de modifier une variable après son initialisation (`const int MAX = 100;`, voir [[Constante (programmation)]]). `volatile` prévient le compilateur que la valeur peut changer sans que le programme y touche (registre d'un périphérique, variable partagée avec une interruption) : il doit la relire en mémoire à chaque accès au lieu de garder une copie. [[Complément hors du cours|ⓘ]]

## 2. Types de base et variables

1. **`void`** : le type vide, introduit par la norme ANSI. Sert surtout à préciser les fonctions sans argument ou sans retour.
2. **`int`** : le type entier. Qualificatifs de taille (`long`, `short`) et de signe : `unsigned` (positif seulement) ou `signed` (positif et négatif). `signed` est appliqué par défaut : `int` et `signed int` sont identiques.
3. **`char`** : support du [[Code ASCII|code ASCII]] pour représenter les caractères ; peut aussi représenter un entier sur 8 bits. Peut être déclaré signé (`signed char`) ou non signé (`unsigned char`) ; un `char` sans qualificatif est signé ou non selon le compilateur et la machine (voir [[Type primitif]]). [[Erreurs du cours#^e-1-basiques|✎]]
4. **`float`** : représentation des réels (avec partie décimale).
5. **`double`** : comme `float`, avec une précision plus importante.
6. **`long double`** : comme `double`, avec une précision encore plus grande.

La norme du C ne fixe pas la taille exacte des types, seulement des minimums : `char` fait exactement 1 octet (`sizeof(char)` vaut 1 par définition), `short` et `int` au moins 16 bits, `long` au moins 32 bits, `long long` (ajouté en C99) au moins 64 bits. Les tailles réelles dépendent de la machine et du compilateur ; sur un PC actuel, `int` fait 32 bits et va de $-2^{31}$ à $2^{31}-1$ (environ $\pm 2{,}1$ milliards). Un `float` donne environ 7 chiffres significatifs, un `double` environ 15 ou 16 ; une constante écrite `3.14` est de type `double` (`3.14f` pour un `float`). [[Complément hors du cours|ⓘ]]

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

Les plus utiles parmi les autres : `%ld` pour un `long`, `%lld` pour un `long long`, `%e` pour un réel en notation scientifique (`1.5e+03`), `%p` pour une adresse (un pointeur), `%%` pour afficher le caractère `%` lui-même. [[Complément hors du cours|ⓘ]]

Piège classique : `printf` affiche un `double` avec `%f`, mais `scanf` doit le lire avec `%lf` ; `%f` dans `scanf` attend l'adresse d'un `float`. La différence vient de ce que `printf` reçoit des valeurs (un `float` y est automatiquement converti en `double`), alors que `scanf` reçoit des adresses et doit savoir combien d'octets écrire. [[Complément hors du cours|ⓘ]]

```c
printf("%d kilogramme équivaut à %d grammes", 1, 1000);
scanf("%d", &i);   /* lit un entier et le range à l'adresse de i */
```

Le `&` devant `i` est obligatoire : le C passe les arguments [[Passage par valeur|par valeur]], donc `scanf` recevrait une copie de `i` et ne pourrait pas le modifier. En lui donnant l'adresse de `i`, on lui permet d'écrire directement dans la variable. Oublier le `&` fait écrire `scanf` à une adresse quelconque, souvent avec une [[Erreur de segmentation|erreur de segmentation]] à la clé. Les deux fonctions sont déclarées dans `stdio.h`, d'où le `#include <stdio.h>` en tête du programme. [[Complément hors du cours|ⓘ]]

Pour afficher une valeur numérique, des **modificateurs de format** ajustent la forme ou la longueur de l'affichage, par exemple `%3d` (largeur 3) et `%03d` (largeur 3 complétée par des zéros).

Pour les réels, la **précision** s'écrit après un point : `%.2f` affiche deux décimales (`3.14159` devient `3.14`, arrondi), `%8.2f` affiche deux décimales sur 8 caractères au moins. Sans précision, `%f` affiche six décimales. Un `-` aligne à gauche (`%-5d`). [[Complément hors du cours|ⓘ]]

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

L'addition `total + texte` elle-même est permise : c'est de l'[[Arithmétique des pointeurs|arithmétique de pointeurs]], qui donne une [[Pointeur et adresse mémoire|adresse mémoire]] (`char *`). Le compilateur bloque parce qu'on range ce pointeur dans un `int` : `gcc` répond `initialization of 'int' from 'char *' makes integer from pointer without a cast` (erreur depuis GCC 14, simple avertissement avant). Détecter cela à la compilation évite des plantages (*[[Erreur de segmentation|segmentation fault]]*) ou des comportements imprévisibles à l'exécution. [[Erreurs du cours#^e-1-basiques|✎]]

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

Conséquence directe : une variable locale n'existe que pendant l'exécution de sa fonction. Renvoyer son adresse (`return &a;`) est une erreur classique, car le cadre est libéré et la case sera réutilisée par l'appel suivant. La pile est aussi de taille limitée (quelques mégaoctets en général) : une [[Récursivité|récursion]] trop profonde ou un très grand tableau local la font déborder (*stack overflow*). [[Complément hors du cours|ⓘ]]

L'autre zone où l'on range des données est le **tas** (*heap*) : on y réserve de la mémoire à la demande avec `malloc`, elle reste disponible après la fin de la fonction et doit être rendue explicitement avec `free` (voir [[Allocation dynamique]], vue au chapitre 3). Les variables globales et `static`, elles, sont placées dans une zone à part, réservée pour toute la durée du programme (voir [[Espace mémoire d'un processus]]). [[Complément hors du cours|ⓘ]]

## 4. Erreurs du compilateur

Messages fréquents d'[[Erreur de compilation|erreur de compilation]] ([[GCC]]) :

| Message | Cause |
|---|---|
| `error: expected ';' before...` | un point-virgule oublié |
| `error: expected declaration or statement at end of input` | une accolade oubliée |
| `error: 'nom_variable' undeclared (first use in this function)` | variable non déclarée (ou mal orthographiée) |
| `a.c:(.text+0x19): undefined reference to 'nom_fonction'` puis `collect2: error: ld returned 1 exit status` | fonction inconnue du compilateur (mal orthographiée ?) |
| `fatal error: nom_fichier.h: Aucun fichier ou dossier de ce type` | fichier d'en-tête inclus mal orthographié |

Ces messages viennent d'étapes différentes, car `gcc` enchaîne quatre phases ([[Chaîne de compilation]]) : le **préprocesseur** (traite les `#include` et `#define` ; c'est lui qui ne trouve pas le `.h`), la **compilation** proprement dite (vérifie la syntaxe et les types : `;` ou accolade oubliés, variable non déclarée), l'**assemblage** (produit un fichier objet `.o`), puis l'**édition de liens** (*linker*, programme `ld`), qui assemble les fichiers objets et les bibliothèques. L'erreur `undefined reference` vient de cette dernière étape : la fonction a pu être déclarée, mais `ld` ne trouve nulle part son code, d'où le message `ld returned 1 exit status`. [[Complément hors du cours|ⓘ]]

À côté des erreurs, qui bloquent la compilation, le compilateur émet des **avertissements** (*warnings*), qui la laissent passer. Compiler avec `gcc -Wall -Wextra prog.c -o prog` les active : beaucoup des pièges de la section 6 (affectation dans une condition, variable non initialisée, `;` après un `if`) sont alors signalés. [[Complément hors du cours|ⓘ]]

## 5. Le type `char` : un entier déguisé

En C, `char` est un **entier sur 1 octet** (8 bits). L'ordinateur ne stocke que des nombres ; la correspondance nombre-lettre est donnée par la table ASCII. Écrire `'A'` ou `65` revient strictement au même pour le compilateur.

| Code écrit | Valeur stockée |
|---|---|
| `c = 65;` | 65 (binaire `01000001`) |
| `c = 'A';` | 65 (binaire `01000001`) |
| `c = 'B';` | 66 (binaire `01000010`) |

Comme un `char` est un nombre, on peut calculer avec : les lettres et les chiffres se suivent dans la table ASCII, donc `'A' + 1` vaut `'B'`, `c - 'a' + 'A'` passe une minuscule en majuscule (l'écart est de 32), et `c - '0'` donne la valeur du chiffre écrit (`'7' - '0'` vaut 7, alors que `'7'` vaut 55). [[Complément hors du cours|ⓘ]]

Les guillemets ne sont pas interchangeables : `'A'` (apostrophes) est **un** caractère, de valeur 65 ; `"A"` (guillemets) est une [[Chaîne de caractères|chaîne de caractères]], c'est-à-dire un tableau de deux `char`, `'A'` puis le caractère nul `'\0'` qui marque la fin de toute chaîne en C. [[Complément hors du cours|ⓘ]]

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

Le même piège existe avec les encadrements : `0 < x < 10` se lit `(0 < x) < 10`, soit `0 < 10` ou `1 < 10`, toujours vrai quel que soit `x`. Il faut écrire `0 < x && x < 10`. [[Complément hors du cours|ⓘ]]

Remplacement correct : `if (a == b && b == c)`. La forme `if ( ((a==b) == 1) == (b==c) )` n'est pas équivalente : elle est aussi vraie quand `a != b` et `b != c`, puisqu'elle compare alors `0 == 0`. [[Erreurs du cours#^e-1-basiques|✎]]

### Pas besoin d'accolades pour une seule instruction

Pour `if`, `else`, `for`, `while`, etc., les accolades sont facultatives quand il n'y a qu'une instruction (voir [[Structure conditionnelle]], [[Boucle (programmation)]]) :

```c
if (a==0) printf("bonjour");
```

Seule la **première** instruction dépend alors du `if`, quelle que soit l'indentation : dans `if (a==0) printf("A"); printf("B");`, « B » s'affiche toujours. C'est pourquoi beaucoup de conventions de code imposent les accolades même pour une seule instruction. [[Complément hors du cours|ⓘ]]

### Affectation dans une condition

```c
int a = 10;
if (a=3) printf("bonjour");   // et pas (a==3)
```

Résultat : affiche « bonjour ». `if (a=3)` ne teste rien : l'[[Affectation|affectation]] met 3 dans `a`, et l'expression vaut 3, non nul donc vrai. La condition est toujours vraie, d'où l'affichage. [[Erreurs du cours#^e-1-basiques|✎]]

En C, une affectation est une expression qui a une valeur, celle qui vient d'être affectée : c'est ce qui permet `a = b = c = 5` (lu `a = (b = (c = 5))`). Une parade ancienne contre la confusion `=` / `==` consiste à écrire la constante à gauche, `if (3 == a)` : une faute de frappe `if (3 = a)` ne compile plus. Avec `-Wall`, `gcc` signale aussi l'affectation dans une condition et propose de la mettre entre doubles parenthèses si elle est voulue. [[Complément hors du cours|ⓘ]]

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

Le « ET » `&&` est paresseux de la même façon, dans l'autre sens : il s'arrête dès qu'une partie est **fausse**. Ce comportement est garanti par la norme et sert couramment de protection : dans `if (p != NULL && *p == 0)` ou `if (n != 0 && total / n > 10)`, la seconde partie, dangereuse, n'est évaluée que si la première est vraie. [[Complément hors du cours|ⓘ]]

### Afficher une variable non initialisée

```c
int y;
printf("y = %d", y);   // y = [valeur aléatoire]
```

Voir [[Variable non initialisée]].

Plus précisément, une variable locale non initialisée contient ce qui restait dans la case mémoire de la pile, et la norme range sa lecture parmi les **[[Comportement indéfini|comportements indéfinis]]** : le programme peut afficher n'importe quoi, et la valeur peut changer d'une exécution ou d'une compilation à l'autre. Les variables globales et `static`, elles, sont automatiquement initialisées à zéro. [[Complément hors du cours|ⓘ]]

### Boucle infinie

```c
int x = 5;
while(x<10);
x++;
```

Le `;` après le `while` donne une boucle dont le corps est vide : la condition reste toujours vraie (rien n'incrémente `x`), la boucle tourne à vide et `x++` n'est jamais exécuté.

Une boucle infinie peut aussi être voulue (serveur, menu qui attend une commande) : on l'écrit alors `while (1)` ou `for (;;)` et on en sort par un `break` ou un `return`. Dans un terminal, `Ctrl+C` interrompt un programme bloqué dans une boucle. [[Complément hors du cours|ⓘ]]
