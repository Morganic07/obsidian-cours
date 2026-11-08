---
type: source
tags: [year3]
sources: ["[[Raw/Year 3/Java/Chp1 : Intro Java.docx|Chp1 - Intro Java]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 3/Java/Chp1 : Intro Java.docx|Chp1 - Intro Java]], dans [[Cours/Informatique/Java/_index|Java]]. Voir [[Langage Java]].

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
- Conventions d'usage (non imposées par le compilateur) : variables et méthodes en *camelCase* (`nombreEleves`, `calculerAire`), classes en *PascalCase* (`Premier`, `CompteBancaire`), constantes en majuscules séparées par `_` (`TAUX_TVA`). [[Complément hors du cours|ⓘ]]

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

**Littéraux.** Un entier écrit dans le code (`42`) est un `int`, un nombre à virgule (`3.14`) un `double`. Pour un `long` au-delà de $2^{31} - 1$, on ajoute le suffixe `L` (`long n = 3000000000L;`) ; pour un `float`, le suffixe `f` : `float r = 3.14;` ne compile pas (un `double` ne va pas dans un `float` sans cast), `float r = 3.14f;` oui. Un `char` s'écrit entre apostrophes (`'A'`), une chaîne entre guillemets (`"A"`). [[Complément hors du cours|ⓘ]]

**Dépassement d'entier.** Les entiers sont codés en [[Complément à deux|complément à deux]] : un calcul qui sort de l'intervalle ne provoque pas d'erreur, il « reboucle » de l'autre côté. Par exemple `Integer.MAX_VALUE + 1` vaut `Integer.MIN_VALUE`, soit $-2^{31}$. Voir [[Dépassement d'entier]]. [[Complément hors du cours|ⓘ]]

**Précision des flottants.** `float` et `double` suivent la [[Norme IEEE 754|norme IEEE 754]] et ne représentent la plupart des décimaux que de façon approchée : `0.1 + 0.2 == 0.3` vaut `false` en `double`. On compare donc deux flottants à une tolérance près (`Math.abs(a - b) < 1e-9`), et on évite `float`/`double` pour des montants d'argent (la classe `BigDecimal` existe pour cela). [[Complément hors du cours|ⓘ]]

**Primitif ou référence.** Une variable de type primitif contient directement sa valeur ; une variable de type objet (une `String`, un tableau, tout objet d'une classe) contient une **référence** vers l'objet, ou `null` si elle n'en désigne aucun. Chaque type primitif a une classe « enveloppe » (*wrapper*) : `Integer` pour `int`, `Double` pour `double`, `Character` pour `char`, `Boolean` pour `boolean`, etc. ; elles fournissent par exemple `Integer.parseInt` et `Double.parseDouble` (utilisé plus bas). [[Complément hors du cours|ⓘ]]

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

Correction : déclarer `x` avant la boucle (`int x;` au-dessus du `do`) et seulement l'affecter dans le bloc (`x = 10;`), pour qu'elle soit visible dans la condition ; la redéclarer dans le bloc serait refusé, Java interdisant deux variables locales de même nom dans des portées imbriquées. Par ailleurs, Java refuse de compiler la lecture d'une variable locale à laquelle aucune valeur n'a été donnée (`int z; System.out.println(z);` : *variable z might not have been initialized*), contrairement au C où elle contient une valeur indéterminée ([[Variable non initialisée]]). [[Complément hors du cours|ⓘ]]

## 2. Opérations de base

### Affichage

```java
System.out.print(<Message>);     // sans nouvelle ligne
System.out.println(<Message>);   // avec nouvelle ligne
```

L'opérateur `+` entre une chaîne et une autre valeur **concatène** : `"x = " + 5` donne `"x = 5"`. L'évaluation va de gauche à droite, donc `"a" + 1 + 2` donne `"a12"` alors que `1 + 2 + "a"` donne `"3a"`. [[Complément hors du cours|ⓘ]]

### Opérateurs arithmétiques

Le cours ne les liste pas : `+`, `-`, `*`, `/` et `%` (reste de la division). Entre deux entiers, `/` est la **division entière** : `7 / 2` vaut `3`, `7 % 2` vaut `1`, et `-7 / 2` vaut `-3` (troncature vers zéro). Dès qu'un opérande est flottant, la division est réelle : `7 / 2.0` vaut `3.5`. Diviser un entier par zéro lève une `ArithmeticException` ; un flottant divisé par zéro donne `Infinity` (ou `NaN` pour `0.0 / 0.0`). [[Complément hors du cours|ⓘ]]

Les affectations composées `x += 3`, `x -= 3`, `x *= 3`, `x /= 3`, `x %= 3` abrègent `x = x + 3`, etc. ; elles incluent un cast implicite vers le type de `x` (`byte b = 10; b += 5;` compile, `b = b + 5;` non, car `b + 5` est un `int`). [[Complément hors du cours|ⓘ]]

### Comparaisons ([[Opérateur de comparaison]])

| Opérateur | Signification |
|---|---|
| `==` | égal à |
| `!=` | différent de |
| `>` | supérieur à |
| `<` | inférieur à |
| `>=` | supérieur ou égal à |
| `<=` | inférieur ou égal à |

Sur des objets, `==` compare les **références** (s'agit-il du même objet ?) et non les contenus. Pour comparer deux chaînes, on écrit `s1.equals(s2)` : deux `String` de même texte construites séparément peuvent être différentes au sens de `==`. [[Complément hors du cours|ⓘ]]

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

Symétriquement, `||` s'arrête dès qu'une condition est vraie ; `&` et `|` évaluent toujours les deux côtés. Le court-circuit sert de garde : dans `if (t != null && t.length > 0)`, `t.length` n'est lu que si `t` existe, sinon on aurait une `NullPointerException`. Appliqués à des entiers, `&`, `|` et `^` opèrent bit à bit (`6 & 3` vaut `2`). [[Complément hors du cours|ⓘ]]

### Caractères spéciaux ([[Caractère d'échappement]])

- `\n` : nouvelle ligne (*new line*) ;
- `\t` : tabulation (*tab*) ;
- `\r` : retour chariot (*carriage return*).
- `\"`, `\'` et `\\` : guillemet, apostrophe et barre oblique inverse eux-mêmes, par exemple `"Il dit \"oui\""`. [[Complément hors du cours|ⓘ]]

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

L'affectation s'associe à droite : `a = b = 0;` se lit `a = (b = 0);`, l'affectation `b = 0` valant elle-même `0`. [[Complément hors du cours|ⓘ]]

La **précédence** (priorité) décide avant l'associativité, entre opérateurs différents. Du plus prioritaire au moins prioritaire, pour les opérateurs de ce chapitre : `++`, `--`, `!` et cast ; `*`, `/`, `%` ; `+`, `-` ; `<`, `>`, `<=`, `>=` ; `==`, `!=` ; `&` ; `^` ; `|` ; `&&` ; `||` ; `? :` ; `=` et affectations composées. Ainsi `a + b * c` vaut `a + (b * c)` et `x > 0 && y > 0 || z` vaut `(x > 0 && y > 0) || z` ; en cas de doute, des parenthèses. [[Complément hors du cours|ⓘ]]

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

Exemple du cours (la conversion explicite `(int)(x/y)` est valide) : [[Erreurs du cours#^e-1-intro-java|✎]]
```java
int i;
float r;
r = i;                    // ok
i = r;                    // incorrect (float vers int sans cast)

double x, y;
int quotient;
quotient = (int)(x/y);    // ok (cast explicite de double vers int)
```

Le compilateur exige un cast explicite pour toute conversion **rétrécissante** (vers un type plus étroit), parce qu'elle peut perdre de l'information. Ce qui se perd : un flottant converti en entier est **tronqué** vers zéro (`(int) 3.9` vaut `3`, `(int) -3.9` vaut `-3`), sans arrondi ; un entier converti en type plus petit ne garde que ses bits de poids faible (`(byte) 200` vaut `-56`, car $200 - 256 = -56$). Pour arrondir, on utilise `Math.round(3.9)`, qui renvoie `4`. [[Complément hors du cours|ⓘ]]

Une conversion élargissante peut, elle aussi, perdre de la précision sans erreur : un `float` n'a que 24 bits de mantisse, donc un grand `int` (au-delà de $2^{24}$) ou un grand `long` converti en `float` est arrondi. [[Complément hors du cours|ⓘ]]

Dans une expression, les opérandes plus petits qu'un `int` (`byte`, `short`, `char`) sont **promus** en `int` : `byte a = 1, b = 2; byte c = a + b;` ne compile pas, il faut `byte c = (byte)(a + b);`. Un `char` se convertit implicitement en `int` (son code [[Unicode]] : `int n = 'A';` donne 65), l'inverse demande un cast (`(char) 66` donne `'B'`). [[Complément hors du cours|ⓘ]]

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
`else if` existe en Java : c'est un `else` suivi d'un `if`, ce qui permet d'enchaîner `if / else if / else`. [[Erreurs du cours#^e-1-intro-java|✎]] Voir [[Structure conditionnelle]].

Enchaînement de conditions, où seul le premier bloc dont la condition est vraie s'exécute : [[Complément hors du cours|ⓘ]]
```java
if (note >= 16) {
    System.out.println("Très bien");
} else if (note >= 12) {
    System.out.println("Bien");
} else {
    System.out.println("À revoir");
}
```

Sans accolades, seule la première instruction dépend du `if` ; un `else` se rattache toujours au `if` le plus proche qui n'en a pas encore. Mettre des accolades partout évite ces deux pièges. [[Complément hors du cours|ⓘ]]

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
- Ce qu'un `break` absent change : l'exécution commence au `case` égal à l'expression puis **continue dans les `case` suivants** (*fall-through*) jusqu'au prochain `break` ou à la fin du `switch`. On s'en sert pour regrouper des cas (`case 'a': case 'e': … voyelle …; break;`), mais un oubli est une erreur classique. [[Complément hors du cours|ⓘ]]
- Les valeurs des `case` doivent être des constantes et toutes différentes. En plus des types cités, `switch` accepte les classes enveloppes correspondantes (`Character`, `Byte`, `Short`, `Integer`), les énumérations (`enum`, depuis Java 5) et les `String` (depuis Java 7) ; pas `long`, `float`, `double` ni `boolean`. Depuis Java 14, la forme fléchée `case 1 -> …` n'a pas de *fall-through* et peut renvoyer une valeur (expression `switch`). [[Complément hors du cours|ⓘ]]

### Boucles ([[Boucle (programmation)]])

**`while`** :
```
while (condition) instruction;

while (condition) {
   … séquence d'instructions …
}
```

**`do-while`** : s'exécute **au moins une fois**, même si la condition n'est pas vérifiée. [[Erreurs du cours#^e-1-intro-java|✎]]
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

Déroulement : l'initialisation a lieu une seule fois ; puis, à chaque tour, la condition est testée, le corps s'exécute si elle est vraie, et l'itération vient après le corps. Une boucle `for` équivaut donc à `initialisation; while (condition) { corps; itération; }`. Exemple : `for (int i = 0; i < 5; i++)` fait 5 tours, `i` valant de 0 à 4 ; la variable `i` déclarée dans l'en-tête n'existe que dans la boucle. [[Complément hors du cours|ⓘ]]

**Sauts** :
- `break` sort des boucles `for`, `while` et `do-while` ;
- `continue` saute la fin de l'itération en cours.

Dans des boucles imbriquées, `break` et `continue` n'agissent que sur la boucle la plus intérieure (et `break` sort aussi d'un `switch`). Pour sortir de plusieurs niveaux, on étiquette la boucle extérieure : `externe: for (…) { for (…) { if (trouve) break externe; } }`. [[Complément hors du cours|ⓘ]]

## 4. Fonctions : la méthode `main`

Premier programme (`System.out.println`, chaîne entre guillemets droits `"…"`) : [[Erreurs du cours#^e-1-intro-java|✎]]

```java
public class Premier {
    public static void main(String[] args) {
        System.out.println("Bonjour Monde");
    }
}
```
1. Le programme est stocké dans le fichier `Premier.java` (même nom que la classe).
2. Toute application Java doit contenir une [[Méthode main|méthode `main()`]], exécutée en premier.

Le sens de chaque mot de l'en-tête `public static void main(String[] args)` : `public`, la méthode est accessible de l'extérieur de la classe, donc par la machine virtuelle qui la lance ; `static`, elle appartient à la classe et s'appelle sans créer d'objet (au lancement, aucun objet n'existe encore) ; `void`, elle ne renvoie rien ; `String[] args`, les arguments de la ligne de commande, sous forme de chaînes. En Java, tout code se trouve dans une classe : il n'y a pas de fonction isolée comme en C, on parle de **méthodes** ([[Classe et objet]]). [[Complément hors du cours|ⓘ]]

![[Chp1 - Intro Java - image25.png]]
*Figure : le programme `Premier` annoté : `class Premier` identifie une classe ; `public` (sur les deux lignes) et `static` sont désignés comme modificateurs ; `main` est le début de l'exécution ; `String[] args` est le tableau des éléments d'entrée ; `System.out.println` affiche un message à l'écran.*

### Compiler et exécuter

La compilation crée un fichier `.class` qui contient le [[Compilation et bytecode|bytecode]] ; l'exécution utilise ce fichier.
```
> javac Premier.java      → produit Premier.class
> java Premier
Bonjour Monde
```

**La machine virtuelle Java (JVM).** Le bytecode n'est pas du code machine : c'est un code intermédiaire, le même pour tous les systèmes, que la commande `java` fait exécuter par la JVM. Il suffit qu'une JVM existe pour un système (Windows, Linux, macOS) pour que le même `.class` y tourne : c'est le principe « *write once, run anywhere* » de Java. La JVM interprète le bytecode et compile à la volée en code machine les parties souvent exécutées (compilation *JIT*, *just-in-time*), ce qui rapproche Java des langages compilés en vitesse. Voir [[Compilation et bytecode]]. [[Complément hors du cours|ⓘ]]

Pour développer, on installe un **JDK** (*Java Development Kit*), qui contient le compilateur `javac`, la JVM et la bibliothèque standard ; le **JRE** (*Java Runtime Environment*) désigne la seule partie nécessaire à l'exécution. Dans `java Premier`, on donne le nom de la classe, sans l'extension `.class`. [[Complément hors du cours|ⓘ]]

La JVM gère aussi la mémoire : les objets (dont les tableaux) sont créés par `new` et libérés automatiquement par le **[[Ramasse-miettes|ramasse-miettes]]** (*garbage collector*) quand plus aucune référence ne les désigne ; il n'y a pas de `free` ni de `delete` comme en C ou C++. [[Complément hors du cours|ⓘ]]

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

Un tableau créé par `new` sans énumération est rempli de **valeurs par défaut** : `0` pour les nombres, `false` pour `boolean`, le caractère de code 0 pour `char`, `null` pour les objets. Sa taille est fixée à la création et ne change plus (pour une collection de taille variable, Java fournit `ArrayList`). [[Complément hors du cours|ⓘ]]

Accéder à un indice hors de $[0, \text{taille} - 1]$ ne lit pas une case voisine comme en C : Java vérifie l'indice à l'exécution et lève une `ArrayIndexOutOfBoundsException`. [[Complément hors du cours|ⓘ]]

Un tableau est un objet : une variable tableau contient une référence. Après `int[] b = valeurs;`, `b` et `valeurs` désignent le **même** tableau, et `b[0] = 7;` modifie aussi `valeurs[0]` ; pour une vraie copie, `valeurs.clone()` ou `Arrays.copyOf(valeurs, valeurs.length)`. Pour afficher le contenu, `System.out.println(valeurs)` n'affiche qu'un identifiant d'objet ; il faut `Arrays.toString(valeurs)` (avec `import java.util.Arrays;`). [[Complément hors du cours|ⓘ]]

Une matrice est un tableau de tableaux : chaque ligne est un tableau à part, et les lignes peuvent avoir des longueurs différentes (`int[][] t = { {1}, {2, 3}, {4, 5, 6} };`), d'où l'intérêt de `matrice[i].length` plutôt que d'une taille fixe. [[Complément hors du cours|ⓘ]]

### Taille : `length`

`valeurs.length` vaut 5 pour un tableau de cinq éléments ; pour une matrice, `matrice.length` donne le nombre de lignes et `matrice[0].length` celui de colonnes. [[Erreurs du cours#^e-1-intro-java|✎]]

```java
int valeurs[] = { 5, 2, 4, 8, 9 };
System.out.println(valeurs.length);       // 5
int matrice[][] = { {1, 2, 3}, {4, 5, 6} };
System.out.println(matrice.length);       // 2 (nombre de lignes)
System.out.println(matrice[0].length);    // 3 (nombre de colonnes)
```

`length` est un attribut du tableau, sans parenthèses ; pour une `String`, c'est une méthode : `"abc".length()`. [[Complément hors du cours|ⓘ]]

### Parcourir un tableau

Parcours par indice, avec la condition `i < valeurs.length` (et non `<=`, qui sortirait du tableau au dernier tour), ou boucle « pour chaque » (*for-each*, depuis Java 5), quand l'indice est inutile : [[Complément hors du cours|ⓘ]]
```java
int somme = 0;
for (int i = 0; i < valeurs.length; i++) {
    somme += valeurs[i];
}
for (int v : valeurs) {          // v prend tour à tour chaque valeur
    System.out.println(v);
}
for (int i = 0; i < matrice.length; i++) {          // matrice : ligne par ligne
    for (int j = 0; j < matrice[i].length; j++) {
        System.out.print(matrice[i][j] + " ");
    }
    System.out.println();
}
```
Dans une boucle *for-each*, `v` est une copie de l'élément : lui affecter une valeur ne modifie pas le tableau. [[Complément hors du cours|ⓘ]]

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
- Exécution, par exemple : `java Aire 2`, qui affiche ` Aire d'un cercle avec rayon 2.0 est 12.5664`. [[Complément hors du cours|ⓘ]]
- Lancé sans argument, le programme s'arrête sur une `ArrayIndexOutOfBoundsException` (`args` est vide, `args[0]` n'existe pas) ; avec un argument non numérique (`java Aire deux`), `Double.parseDouble` lève une `NumberFormatException`. Un programme robuste teste `args.length` avant de lire `args[0]`. [[Complément hors du cours|ⓘ]]
- La bibliothèque standard fournit la constante `Math.PI` ($\pi$ en `double`, plus précise que `3.1416`) et des fonctions comme `Math.pow(r, 2)`, `Math.sqrt(x)`, `Math.abs(x)`. [[Complément hors du cours|ⓘ]]
- Pour lire une valeur au clavier pendant l'exécution plutôt qu'en argument, on utilise la classe `Scanner` : `Scanner sc = new Scanner(System.in); double rayon = sc.nextDouble();` (avec `import java.util.Scanner;`). [[Complément hors du cours|ⓘ]]
