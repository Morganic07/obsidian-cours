---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Java/Chp1 : Intro Java.docx|Chp1 - Intro Java]]"]
maj: 2026-11-07
complet: true
---

Résumé de [[Raw/Year 3/Java/Chp1 : Intro Java.docx|Chp1 - Intro Java]], dans [[Cours/Informatique/Java/_index|Java]]. En cas d'écart, le cours et ses images font foi. Voir [[Langage Java]].

## Idée générale

Les bases du langage : variables, types, opérateurs, structures de contrôle, méthode `main`, compilation et tableaux.

## 1. Variables

### Déclaration

Syntaxe ([[Variable (programmation)]]) :
```
<Type-donnée> <nom-de-variable>;
<Type-donnée> <nom-de-variable1>, <nom-de-variable2>, <nom-de-variable3>;
```
Exemples :
```java
int age;
char confirmation;
double pointx, pointy, deltax, deltay;
```

### Règles de nommage

- Un nom commence par une lettre, `_` ou `$` : `compteur` est valide, `3distance` non.
- Ce ne peut pas être un [[Mot réservé|mot-clé]] : `double` est interdit.
- Ensuite, une suite de lettres, chiffres, `_` ou `$` : `inc_delta`, `nombre3` sont valides.
- Java est **sensible à la casse** (majuscules ≠ minuscules).

### Constantes

Une [[Constante (programmation)|constante]] est une variable de valeur fixe, déclarée avec le mot-clé `final`, qui ne peut pas être modifiée pendant l'exécution. Par convention, on l'écrit en majuscules.
```java
public class Exemple {
   public static void main(String[] args) {
      final int MOIS = 12;   // écrire les constantes en majuscules
      System.out.print(MOIS);
      MOIS = 3;              // erreur de compilation
   }
}
```
Modifier une constante provoque une [[Erreur de compilation|erreur de compilation]].

### Types de données

- **Primitifs** ([[Type primitif]]) : les types les plus simples, présents par défaut.
- **Objets (références)** : définis par les classes et les interfaces ; chaque classe et chaque interface définit un type.
- **Type spécial** : `void`, aucun type.

| Type | Bits | Intervalle |
|---|---|---|
| `byte` | 8 | $[-128, 127]$ |
| `short` | 16 | $[-32768, 32767]$ |
| `int` | 32 | $[-2^{31}, 2^{31} - 1]$ |
| `long` | 64 | $[-2^{63}, 2^{63} - 1]$ |
| `float` | 32 | virgule flottante, de $-3{,}4 \times 10^{38}$ à $3{,}4 \times 10^{38}$ |
| `double` | 64 | virgule flottante, de $-1{,}7 \times 10^{308}$ à $1{,}7 \times 10^{308}$ |
| `char` | 16 | [[Unicode]] |
| `boolean` | 1 | `true`, `false` |

Ordre des types numériques, du plus large au plus étroit : `double` → `float` → `long` → `int` → `short` → `byte` (voir [[Nombre à virgule flottante]]).

### Portée (*scope*) d'une variable

La [[Portée d'une variable|portée]] est la région du code où la variable peut être écrite (affectation) ou lue. Dans une portée, tous les noms doivent être uniques : deux variables ne peuvent pas avoir le même nom. Les régions sont généralement délimitées par des paires d'accolades `{ … }`.

**Erreur de portée** :
```java
double y = 5;
do {
  int x = 10;
  y--;
  if (y > 0) x--;
  System.out.println("y= " + y);
} while (x < 10);   // x n'existe plus ici
```
`x` est déclarée dans le bloc `do { … }`, mais la condition `while (x < 10)` l'utilise hors du bloc : erreur de compilation.

## 2. Opérations de base

### Affichage

```java
System.out.print(<Message>);     // sans nouvelle ligne
System.out.println(<Message>);   // avec nouvelle ligne
```

### Comparaisons ([[Opérateur de comparaison]])

| Opérateur | Signification |
|---|---|
| `==` | égal à |
| `!=` | différent de |
| `>` | supérieur à |
| `<` | inférieur à |
| `>=` | supérieur ou égal à |
| `<=` | inférieur ou égal à |

### Opérateurs booléens ([[Opérateur logique]])

| Opérateur | Signification |
|---|---|
| `&` | et (*and*) |
| `\|` | ou (*or*) |
| `^` | ou exclusif (*xor*) |
| `\|\|` | ou court-circuit (*short-circuit*) |
| `&&` | et court-circuit |
| `!` | négation |

`&&` est en [[Évaluation en court-circuit|court-circuit]] : si une condition est fausse, l'évaluation s'arrête au lieu de continuer sur les autres.

### Caractères spéciaux ([[Caractère d'échappement]])

- `\n` : nouvelle ligne (*new line*) ;
- `\t` : tabulation (*tab*) ;
- `\r` : retour chariot (*carriage return*).

### Incrément et décrément

L'ordre importe ([[Opérateur d'incrémentation]]). Avec `x = 10` :
```java
y = ++x;   // y = 11, x = 11  (d'abord x = x + 1, puis y = x)
y = x++;   // y = 10, x = 11  (d'abord y = x, puis x = x + 1)
```

### Associativité et ordre d'évaluation

Voir [[Associativité et ordre d'évaluation]].
- L'associativité fixe l'ordre des opérations de **même précédence**.
- Toutes les opérations binaires s'associent **à gauche**, sauf l'affectation (`=`).
- Une opération binaire évalue d'abord son premier opérande, puis le second. C'est important en présence d'[[Effet de bord|effets de bord]] (*side effects*) :
```java
int a = 0;
int x = a + ++a;   // x = 1  (0 + 1)
```
```java
int a = 0;
int x = ++a + a;   // x = 2  (1 + 1)
```

### Opérateur conditionnel

Syntaxe ([[Opérateur conditionnel]]) :
```
condition ? <si-vrai-expression> : <si-faux-expression>;
```
Exemple :
```java
boolean test = false;
int valeur = test == true ? 10 : 20;   // valeur = 20
```

### Transtypage (*type casting*)

![[Chp1 - Intro Java - image9.png]]
*Figure : hiérarchie des types primitifs numériques, de haut en bas `double`, `float`, `long`, `int`, puis `short` et `char` sous `int`, et `byte` en bas.*

**Règle générale** ([[Transtypage]]) :
- si le type d'arrivée est suffisant → OK (exemple : `float` vers `double`) ;
- s'il n'est pas suffisant → attention aux valeurs (exemple : `double` vers `float` peut être correct ou non selon la valeur).

- **Implicite** : automatique.
- **Explicite** : fait par le programmeur, avec `(type)`.

Exemple du cours :
```java
int i;
float r;
r = i;                    // ok
i = r;                    // incorrect (float vers int sans cast)

double x, y;
int quotient;
quotient = (int)(x/y);    // marqué « incorrect » par le cours, voir « Erreurs du cours »
```

## 3. Structures de contrôle

### `if` / `else`

```
if (condition) instruction;

if (condition) {
  … séquence d'instructions …
}

if (condition) {
  … séquence d'instructions …
} else {
  … séquence d'instructions …
}
```
Le cours ajoute « ELSE IF N'EXISTE PAS EN JAVA » : c'est faux, voir « Erreurs du cours ». Voir [[Structure conditionnelle]].

### `switch`

```
switch (expression) {
    case valeur1 : … instructions …
                   break;
    case valeur2 : … instructions …
                   break;
    …
    default : … instructions …
              break;
}
```
- Types de valeurs acceptés selon le cours : `char`, `byte`, `short`, `int`.
- Le bloc `default` est optionnel ; « les `break` sont optionnels ».

### Boucles ([[Boucle (programmation)]])

**`while`** :
```
while (condition) instruction;

while (condition) {
   … séquence d'instructions …
}
```

**`do-while`** : s'exécute **au moins une fois**, même si la condition n'est pas vérifiée.
```
do {
   … séquence d'instructions …
} while (condition);
```

**`for`** : utilisée quand le nombre d'itérations est connu.
```
for (initialisation; condition; itération) {
    … séquence d'instructions …
}
```
- *Initialisation* : définit la ou les variables de contrôle ;
- *Condition* : condition d'exécution de la séquence ;
- *Itération* : modifie les variables de contrôle à chaque tour.

**Sauts** :
- `break` sort des boucles `for`, `while` et `do-while` ;
- `continue` saute la fin de l'itération en cours.

## 4. Fonctions : la méthode `main`

```java
public class Premier {
    public static void main(String[] args) {
        System.out.println("Bonjour Monde");
    }
}
```
1. Le programme est stocké dans le fichier `Premier.java` (même nom que la classe).
2. Toute application Java doit contenir une [[Méthode main|méthode `main()`]], exécutée en premier.

![[Chp1 - Intro Java - image25.png]]
*Figure : le programme `Premier` annoté : `class Premier` identifie une classe ; `public` (sur les deux lignes) et `static` sont désignés comme modificateurs ; `main` est le début de l'exécution ; `String[] args` est le tableau des éléments d'entrée ; `System.out.println` affiche un message à l'écran.*

### Compiler et exécuter

La compilation crée un fichier `.class` qui contient le [[Compilation et bytecode|bytecode]] ; l'exécution utilise ce fichier.
```
> javac Premier.java      → produit Premier.class
> java Premier
Bonjour Monde
```

## 5. Tableaux

Voir [[Tableau (programmation)]].

### Créer un tableau

```java
type nom[] = new type[taille];
type nom[][] = new type[taille1][taille2];
// ou
type[] nom = new type[taille];
type[][] nom = new type[taille1][taille2];
```
Exemples :
```java
int valeurs[] = new int[5];
int[][] matrice = new int[3][3];
```

### Initialiser un tableau

- Par indices, qui vont de **0 à taille − 1** dans chaque dimension :
```java
valeurs[2] = 4;
matrice[0][0] = 1;
```
- Par énumération dans la définition :
```java
int valeurs[] = { 5, 2, 4, 8, 9 };
int matrice[][] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
```

### Taille : `length`

```java
int valeurs[] = { 5, 2, 4, 8, 9 };
System.out.println(valeurs.length);       // le cours écrit 4 ; la bonne valeur est 5
int matrice[][] = { {1, 2, 3}, {4, 5, 6} };
System.out.println(matrice.length);       // 2 (nombre de lignes)
System.out.println(matrice[0].length);    // 3 (nombre de colonnes)
```

### Exemple : aire d'un cercle

```java
public class Aire {
    public static void main(String[] args) {
        double rayon = Double.parseDouble(args[0]);
        double pi = 3.1416;
        double aire = pi * rayon * rayon;
        System.out.print(" Aire d'un cercle avec rayon " + rayon);
        System.out.println(" est " + aire);
    }
}
```
- `args[0]` contient la valeur du premier paramètre passé au programme, `args[i]` celle du $i$-ème (indices à partir de 0) : `args` est l'entrée donnée par l'utilisateur.
- `Double.parseDouble` convertit une `String` en `double`.
- Exécution, par exemple : `java Aire 2` (complément : la commande n'est pas écrite dans le cours).

## Erreurs du cours

- [[Raw/Year 3/Java/Chp1 : Intro Java.docx|Chp1 - Intro Java]] écrit « ELSE IF N'EXISTE PAS EN JAVA » ; il faut « `else if` s'écrit en Java » : c'est un `else` suivi d'un `if`.
- Le cours écrit `valeurs.length` « → 4 » pour `{ 5, 2, 4, 8, 9 }` ; il faut 5. Les lignes suivantes (2 et 3 pour la matrice) sont justes.
- Le cours marque « incorrect » `quotient = (int)(x/y);` ; ce cast explicite est valide en Java. Seule `i = r;` (`float` vers `int` sans cast) est incorrecte.
- Coquilles du code, corrigées dans les blocs de cette fiche : le cours écrit `“Bonjour Monde”` (guillemets courbes) pour `"Bonjour Monde"`, `Systemt.out` pour `System.out`, `matrice[01.length` (ligne coupée sur l'image) pour `matrice[0].length`, et « while-do » pour `do-while`.
