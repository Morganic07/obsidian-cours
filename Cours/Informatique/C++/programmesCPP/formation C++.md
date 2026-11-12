---
type: source
tags: [year4]
sources:
  - "[[Raw/Year 4/C／C++/programmes C++/formation/1-variables.cpp|1-variables.cpp]]"
  - "[[Raw/Year 4/C／C++/programmes C++/formation/2-cout.cpp|2-cout.cpp]]"
  - "[[Raw/Year 4/C／C++/programmes C++/formation/3-conditions.cpp|3-conditions.cpp]]"
  - "[[Raw/Year 4/C／C++/programmes C++/formation/3-boucles.cpp|3-boucles.cpp]]"
  - "[[Raw/Year 4/C／C++/programmes C++/formation/4-Classe.cpp|4-Classe.cpp]]"
  - "[[Raw/Year 4/C／C++/programmes C++/formation/5-constructeurDefaut.cpp|5-constructeurDefaut.cpp]]"
  - "[[Raw/Year 4/C／C++/programmes C++/formation/6-constructeurParametre.cpp|6-constructeurParametre.cpp]]"
  - "[[Raw/Year 4/C／C++/programmes C++/formation/7-constructeurCopie.cpp|7-constructeurCopie.cpp]]"
  - "[[Raw/Year 4/C／C++/programmes C++/formation/8-méthodes.cpp|8-méthodes.cpp]]"
  - "[[Raw/Year 4/C／C++/programmes C++/formation/9-méthodes2.cpp|9-méthodes2.cpp]]"
  - "[[Raw/Year 4/C／C++/programmes C++/formation/10-SurchargeOpérateurs1.cpp|10-SurchargeOpérateurs1.cpp]]"
  - "[[Raw/Year 4/C／C++/programmes C++/formation/11-surchargeOperateurs2.cpp|11-surchargeOperateurs2.cpp]]"
  - "[[Raw/Year 4/C／C++/programmes C++/formation/12-operateursAffichage.cpp|12-operateursAffichage.cpp]]"
maj: 2026-11-12
complet: true
enrichi: 2026-11-12
---

Le dossier `programmes C++/formation` de [[Cours/Informatique/C++/_index|C++]] contient treize petits programmes numérotés de 1 à 12 (deux portent le numéro 3) qui forment une progression d'autoformation au [[Langage C++|C++]] : [[Variable (programmation)|variables]] et [[Type primitif|types]], affichage et saisie avec les [[Flux d'entrée-sortie (C++)|flux]] `std::cout` et `std::cin`, [[Structure conditionnelle|conditions]] et [[Boucle (programmation)|boucles]], puis la [[Programmation orientée objet|programmation orientée objet]] : [[Classe et objet|classe]], [[Encapsulation (programmation)|encapsulation]], [[Constructeur (programmation)|constructeurs]] par défaut, par paramètres et par copie, [[Accesseur et mutateur|accesseurs et mutateurs]], [[Surcharge d'opérateurs|surcharge d'opérateurs]] et opérateur d'affichage `<<` avec une [[Fonction amie (friend)|fonction amie]]. Elle suit pas à pas le diaporama [[4 - C++]] (sections 1 à 7, mêmes classes `Television`, `Point` et `Personne`) et reprend les bases du polycopié [[4 - Cours complet]]. Les commentaires des fichiers, qui portent l'essentiel des explications, sont remis au propre dans le texte ci-dessous ; tous les programmes ont été compilés avec [[GCC|g++]] 14 (`-std=c++17 -Wall -Wextra`) et exécutés.

## 1-variables

**Ce que fait le programme.** D'après le code, l'exercice présente les types de base du C++ et déclare deux [[Variable (programmation)|variables]] : un `float` calculé par une somme et une [[Chaîne de caractères|chaîne de caractères]] de type `std::string`. Il n'affiche rien.

Ses commentaires dressent la liste des [[Type primitif|types de base]], chacun avec une [[Valeur littérale|valeur littérale]] d'exemple ; le littéral de [[Type char|`char`]] s'écrit entre apostrophes, `'e'`, et non entre guillemets comme dans le fichier (`"e"` est une chaîne de deux caractères, `e` et le caractère nul final, et `char c = "e";` ne compile pas : `invalid conversion from 'const char*' to 'char'`) [[Erreurs du cours#^e-formation-c|✎]] :

| Type | Exemple de littéral | Contenu |
|---|---|---|
| [[Type char\|`char`]] | `'e'` | un caractère (un [[Octet\|octet]], son code [[Code ASCII\|ASCII]]) |
| [[Type entier\|`int`]] | `-8` | un entier signé |
| [[Nombre à virgule flottante\|`float`]] | `2.3f` | un flottant simple précision |
| [[Nombre à virgule flottante\|`double`]] | `2.3` | un flottant double précision |

```cpp
#include <iostream>

int main(){
    float nbFlottant = 10.0f+1.2f;
    std::string nom = "momo";
    return 0;
}
```

**Explications.**

- **Le suffixe `f`.** Un littéral à virgule écrit sans suffixe (`2.3`) est de type `double` ; il faut mettre le `f` après un nombre flottant pour obtenir un littéral `float` (`2.3f`). Sans lui, `float x = 2.3;` part d'un `double` qui est ensuite converti en `float` : une [[Transtypage|conversion implicite]] qui perd de la précision.
- **Les chaînes.** Le C++ gère les chaînes avec la [[Classe string (C++)|classe `std::string`]], bien plus simple que les tableaux de `char` du [[Langage C|C]] : on l'initialise directement avec un littéral `"momo"`.
- `g++ -Wall -Wextra` signale `unused variable 'nbFlottant'` : un simple [[Avertissement de compilation|avertissement]], la variable n'étant jamais lue.

Ce que vaut vraiment la conversion : le `double` le plus proche de 2,3 vaut 2,2999999999999998…, le `float` le plus proche 2,2999999523…, car ni l'un ni l'autre ne représente exactement 2,3 en binaire ([[Norme IEEE 754|norme IEEE 754]] : 24 bits de mantisse pour `float`, 53 pour `double`, soit environ 7 et 16 chiffres décimaux significatifs). En pratique, on utilise `double` par défaut et `float` seulement quand la mémoire compte (grands tableaux, [[Processeur graphique|GPU]]). [[Complément hors du cours|ⓘ]]

`std::string` est déclaré dans l'[[Fichier d'en-tête|en-tête]] `<string>` : le programme compile ici parce que `<iostream>` l'inclut indirectement avec GCC, mais la [[Norme du C++|norme]] ne le garantit pas ; pour la [[Portabilité (informatique)|portabilité]], ajouter `#include <string>` ([[Directive include]]). [[Complément hors du cours|ⓘ]]

## 2-cout

**Ce que fait le programme.** D'après le code, l'exercice affiche un nombre avec `std::cout`, demande deux nombres à l'utilisateur avec `std::cin` et les réaffiche.

```cpp
#include <iostream>

int main(){
    float nbFlottant = 10.0f+1.2f;
    double nbUser = 0;

    std::cout << "chiffre : " << nbFlottant<< std::endl;

    std::cout << "entrez 2 nombres : ";
    std::cin >> nbFlottant >> nbUser;   // >> et pas << : sens du flux
    std::cout << "chiffre : " << nbFlottant << "et : " << nbUser <<std::endl;

    return 0;
}
```

Sortie, avec l'entrée `3.5 7` :

```text
chiffre : 11.2
entrez 2 nombres : chiffre : 3.5et : 7
```

**Explications.**

- **Le préfixe `std::`.** `std` est l'[[Espace de noms (namespace)|espace de noms]] de la [[Bibliothèque standard du C++|bibliothèque standard]], et `cout` un objet (le [[Flux standard|flux de sortie standard]], de type `std::ostream`), pas une fonction ni une bibliothèque : `std::cout` désigne « le `cout` de l'espace de noms `std` ». L'idée du commentaire d'origine reste juste : ranger les noms dans un espace de noms évite les conflits entre noms identiques venus de bibliothèques différentes. [[Erreurs du cours#^e-formation-c|✎]]
- **Correspondances avec le C.** `std::cout` joue le rôle de `printf` et `std::cin` celui de `scanf` ([[Fonctions printf et scanf]]), sans chaîne de format (`%d`, `%f`) : le [[Typage statique|type]] de chaque valeur choisit l'affichage. `std::endl` insère un `'\n'` **et vide le [[Tampon (buffer)|tampon]]** de sortie (*flush*) : il n'équivaut donc pas exactement à `\n`. [[Erreurs du cours#^e-formation-c|✎]]
- **Le sens des chevrons.** On écrit `>>` pour lire (les données vont du flux vers la variable) et `<<` pour écrire (de la valeur vers le flux) : c'est l'ordre du flux. Les opérateurs s'enchaînent : `std::cin >> a >> b` lit deux valeurs séparées par des [[Espace blanc|espaces]] ou des retours à la ligne.
- Le programme affiche `3.5et : 7` : il manque une espace avant `et` dans le littéral `"et : "`.

`std::cin >> x` échoue si l'utilisateur tape autre chose qu'un nombre : le flux passe en état d'erreur, `x` reçoit 0 et les lectures suivantes sont ignorées. Un programme robuste teste le flux (`if (!(std::cin >> x)) { … }`), ce qui relève de la [[Validation des entrées|validation des entrées]]. [[Complément hors du cours|ⓘ]]

Remplacer `std::endl` par `'\n'` dans une boucle qui affiche beaucoup de lignes évite un vidage du tampon à chaque ligne, souvent bien plus rapide ; `std::cout` est de toute façon vidé avant chaque lecture sur `std::cin`, ce qui explique que l'invite `entrez 2 nombres :` s'affiche bien sans `endl`. [[Complément hors du cours|ⓘ]]

On voit souvent `using namespace std;` en tête de fichier pour écrire `cout` sans préfixe ; c'est déconseillé dans un [[Fichier d'en-tête|fichier d'en-tête]], où la directive s'imposerait à tous les fichiers qui l'incluent. [[Complément hors du cours|ⓘ]]

## 3-conditions

**Ce que fait le programme.** D'après le code, l'exercice montre la syntaxe de `if` / `else if` / `else` sur deux [[Booléen|booléens]], puis l'[[Opérateur conditionnel|opérateur ternaire]] pour calculer un maximum. Il n'affiche rien.

```cpp
#include <iostream>

int main(){
    bool condition = true;
    bool autre_condition = false;

    if (condition) {
        // code à exécuter si la condition est vraie
    }
    else if (autre_condition) {
        // code à exécuter si l'autre condition est vraie
    }
    else {
        // code à exécuter si aucune des conditions n'est vraie
    }

    int a = 5;
    int b = 10;
    int max = (a > b) ? a : b;

    return 0;
}
```

**Explications.**

- La [[Structure conditionnelle|structure conditionnelle]] s'écrit comme en C ; le type `bool` prend les valeurs `true` et `false`. Les branches sont testées dans l'ordre et une seule s'exécute.
- L'opérateur ternaire s'écrit `condition ? valeur_si_vraie : valeur_si_fausse`, avec un `?` puis un `:` ; le fichier l'écrivait sans le `:` (`(condition) ? "TRUE=valeur" "FAULSE=valeur"`), alors que le code, lui, l'emploie bien [[Erreurs du cours#^e-formation-c|✎]] : si `a` est supérieur à `b` ([[Opérateur de comparaison|comparaison]] `a > b`), `max` prend la valeur de `a`, sinon celle de `b`. Ici `max` vaut 10.
- `g++` signale `unused variable 'max'` : `max` n'est jamais lu.

Le ternaire est une [[Expression (programmation)|expression]] (il a une valeur), là où `if` est une [[Instruction (programmation)|instruction]] : c'est pourquoi il peut servir à [[Initialisation (programmation)|initialiser]] une variable. La bibliothèque standard fournit `std::max(a, b)` (en-tête `<algorithm>`), plus lisible pour ce cas précis. [[Complément hors du cours|ⓘ]]

Les conditions se combinent avec les [[Opérateur logique|opérateurs logiques]] `&&`, `||` et `!`, évalués en [[Évaluation en court-circuit|court-circuit]] ; et toute valeur numérique non nulle vaut `true` dans une condition, d'où le piège `if (x = 0)` ([[Affectation|affectation]] au lieu de comparaison), que `-Wall` signale. [[Complément hors du cours|ⓘ]]

## 3-boucles

**Ce que fait le programme.** D'après le code, l'exercice montre les trois [[Boucle (programmation)|boucles]] du C++, identiques à celles du C : `for`, `while` et `do … while`.

```cpp
#include <iostream>

int main(){
    for (int i = 0; i < 10; i++) {
        std::cout << "i : " << i << std::endl;
    }

    int condition = 0;
    while (condition) {
        //code
    }

    do{
        //code
    }while (condition);

    return 0;
}
```

Sortie : dix lignes, de `i : 0` à `i : 9`.

**Explications.**

- `for (initialisation; condition; incrémentation)` : le [[Compteur (programmation)|compteur]] `i` part de 0, la boucle tourne tant que `i < 10` et `i++` ([[Opérateur d'incrémentation|incrémentation]]) avance d'un pas ; `i` n'existe que dans la boucle ([[Portée d'une variable|portée]]).
- `while (condition)` teste **avant** chaque tour : avec `condition = 0` (faux), son [[Bloc d'instructions|bloc]] ne s'exécute jamais.
- `do { … } while (condition);` teste **après** le tour : son code est exécuté une fois quoi qu'il arrive, même ici où la condition est fausse. Le `;` final est obligatoire.

Le C++11 ajoute la boucle sur intervalle (*range-based for*), `for (int x : v)`, qui parcourt tous les éléments d'un conteneur comme un [[Classe vector (C++)|`std::vector`]] ou une `std::string` sans gérer d'indice ; avec `for (const auto& x : v)` ([[Mot-clé auto|`auto`]]), on évite en plus la copie de chaque élément. [[Complément hors du cours|ⓘ]]

## 4-Classe

**Ce que fait le programme.** D'après le code, l'exercice introduit la [[Programmation orientée objet|POO]] : il déclare une classe `Television` avec des attributs privés et un attribut public, crée un objet et modifie son attribut public.

Les commentaires du fichier posent le vocabulaire :

- La **POO** (programmation orientée objet, *OOP* en anglais) consiste à définir des [[Classe et objet|classes]] qui permettent de créer des **objets**, qui sont des **instances** de ces classes.
- Une classe contient des **attributs** (des variables) et des **méthodes** (des [[Fonction et procédure|fonctions]]) qui permettent de manipuler ces attributs.
- Un [[Constructeur (programmation)|constructeur]] est une méthode spéciale, appelée lors de la création d'un objet pour initialiser ses attributs (avec des valeurs par défaut dans le cas du constructeur par défaut, voir 5).
- L'[[Encapsulation (programmation)|encapsulation]] règle qui peut accéder à quoi :
  - `private` : attributs et méthodes accessibles uniquement dans la classe ;
  - `public` : accessibles depuis l'extérieur de la classe ;
  - `protected` : accessibles dans la classe et dans les classes dérivées ([[Héritage (programmation)|héritage]]).

Code du fichier, où les deux accesseurs `getVolume` et `getCanal` sont déclarés de type `int` au lieu de `void` : un accesseur sert à **renvoyer** la valeur d'un attribut, ce qu'une fonction `void` ne peut pas faire [[Erreurs du cours#^e-formation-c|✎]] :

```cpp
#include <iostream>

class Television{
    private:
        int volume;
        int canal;
        std::string marque;

    public:
        bool allumée;

        void setVolume(int v);
        int getVolume();
        void setCanal(int c);
        int getCanal();
};

int main(){
    Television tv1;
    tv1.allumée = true;   // objet.attribut = valeur

    return 0;
}
```

**Explications.**

- `Television tv1;` crée un objet (une instance) ; `objet.attribut = valeur` modifie l'attribut d'un objet, ce qui n'est permis que pour un attribut `public` : `tv1.volume = 5;` serait une [[Erreur de compilation|erreur de compilation]] (`'int Television::volume' is private within this context`).
- Les quatre méthodes sont seulement **déclarées** ([[Déclaration et définition|déclaration sans définition]]) : le programme compile et s'exécute parce qu'il ne les appelle pas ; un appel provoquerait une erreur d'[[Édition de liens|édition de liens]] (`undefined reference`).
- `setVolume` / `getVolume` sont le couple [[Accesseur et mutateur|mutateur / accesseur]] développé en 8 et 9.
- Ne pas oublier le `;` après l'accolade fermante d'une classe.

Le nom `allumée` contient un `é` : le C++ accepte les lettres [[Unicode]] dans un [[Identificateur (programmation)|identificateur]] (GCC depuis sa version 10), mais beaucoup d'outils et de [[Règle de codage|règles de codage]] l'évitent ; on écrit plutôt `allumee` ou `estAllume`. [[Complément hors du cours|ⓘ]]

La classe ne déclare aucun constructeur : le compilateur génère un constructeur par défaut qui ne fait rien pour les `int` et le `bool`. Après `Television tv1;`, `volume` et `canal` sont des [[Variable non initialisée|variables non initialisées]] et les lire serait un [[Comportement indéfini|comportement indéfini]] ; seule `marque`, de type `std::string`, est initialisée (chaîne vide) par son propre constructeur. D'où l'intérêt du constructeur de 5. [[Complément hors du cours|ⓘ]]

Un attribut public comme `allumée` brise l'encapsulation : n'importe quel code peut le mettre dans un état incohérent. La règle usuelle est « attributs privés, méthodes publiques ». En C++, `class` et [[Structure (struct)|`struct`]] ne diffèrent que par l'accès par défaut (`private` pour `class`, `public` pour `struct`). [[Complément hors du cours|ⓘ]]

## 5-constructeurDefaut

**Ce que fait le programme.** D'après le code, l'exercice ajoute à la [[Classe et objet|classe]] `Television` un [[Constructeur (programmation)|constructeur par défaut]] qui initialise tous les attributs, puis affiche l'attribut `allumée` d'un objet neuf.

```cpp
#include <iostream>

class Television{
    private:
        int volume;
        int canal;
        std::string marque;

    public:
        Television();   // constructeur par défaut

        bool allumée;;
};

Television::Television(){
    volume = 0;
    canal = 0;
    marque = "Samsung";
    allumée = false;
}

int main(){
    Television tv1;   // constructeur par défaut appelé automatiquement
    std::cout << tv1.allumée;
    return 0;
}
```

Sortie : `0` (sans retour à la ligne).

**Explications.**

- Un constructeur porte **le même nom que la classe**, n'a **pas de type de retour** (pas même `void`) et ne renvoie pas de valeur. Le constructeur **par défaut** est celui qui ne prend aucun paramètre ; il est appelé automatiquement par `Television tv1;`.
- On le **définit en dehors de la classe** en écrivant le nom de la classe, `::` ([[Opérateur de résolution de portée|opérateur de résolution de portée]]), puis le nom du constructeur : `Television::Television()`.
- Le commentaire disait que la ligne `std::cout << tv1.allumée;` « renvoie `false` » : l'attribut vaut bien `false` (initialisé par le constructeur), mais `cout` affiche un booléen sous forme de nombre, `0` pour `false` et `1` pour `true` ; pour lire `false`, il faut `std::cout << std::boolalpha << tv1.allumée;`.
- Le double `;` après `bool allumée` est une faute de frappe sans conséquence : un `;` isolé est une déclaration vide, permise dans une classe ([[Instruction vide]]).

Le style idiomatique initialise les attributs dans une [[Liste d'initialisation|liste d'initialisation]], `Television::Television() : volume(0), canal(0), marque("Samsung"), allumée(false) {}`, ou directement à leur déclaration (`int volume = 0;`, depuis le C++11). Le corps du constructeur ci-dessus fait une [[Affectation|affectation]] après coup : `marque` y est d'abord construite vide, puis réaffectée ; et les attributs `const` ou [[Référence (C++)|références]] ne peuvent être initialisés que par la liste. [[Complément hors du cours|ⓘ]]

Un constructeur peut contenir `return;` sans valeur, pour sortir plus tôt ; ce qui lui est interdit, c'est de renvoyer une valeur. [[Complément hors du cours|ⓘ]]

## 6-constructeurParametre

**Ce que fait le programme.** D'après le code, l'exercice définit une [[Classe et objet|classe]] `Point` avec deux constructeurs, un par défaut et un par paramètres, et crée un objet avec chacun.

Le **[[Constructeur (programmation)|constructeur par paramètres]]** reçoit des valeurs au moment de la création de l'objet et s'en sert pour initialiser directement ses attributs : on crée ainsi des objets avec des valeurs choisies dès le départ, plutôt qu'avec des valeurs par défaut. Une classe peut avoir **plusieurs constructeurs** à paramètres différents : c'est la **surcharge de constructeur**, cas particulier de la [[Surcharge de fonctions|surcharge de fonctions]], qui permet de créer des objets de différentes manières selon les besoins.

```cpp
#include <iostream>

class Point{
    private:
        int x, y;

    public:
        Point();               // constructeur par défaut
        Point(int x, int y);   // constructeur avec paramètres
};

Point::Point(){
    x = 0;
    y = 0;
}

Point::Point(int a, int b){
    x = a;
    y = b;
}

int main(){
    Point p1;      // constructeur par défaut : x = 0, y = 0
    Point p2(1,2); // constructeur avec paramètres : x = 1, y = 2

    return 0;
}
```

**Explications.**

- Le compilateur choisit le constructeur d'après les [[Argument et paramètre|arguments]] fournis : aucun pour `p1`, deux `int` pour `p2`. Pour `p2`, les paramètres sont obligatoires : `Point p3(1);` ne compile pas, aucun constructeur ne prenant un seul `int`.
- La déclaration nomme ses paramètres `x, y` et la définition `a, b` : c'est permis, seuls les types comptent pour faire correspondre déclaration et définition.
- Dès qu'une classe déclare un constructeur, le compilateur ne génère plus le constructeur par défaut : sans `Point();`, la ligne `Point p1;` ne compilerait plus.

Si la définition avait gardé les noms `x` et `y` pour ses paramètres, `x = x;` affecterait le paramètre à lui-même (il masque l'attribut) et l'attribut resterait non initialisé ; on écrirait alors `this->x = x;` avec le [[Pointeur this|pointeur `this`]], ou mieux la liste d'initialisation `Point(int x, int y) : x(x), y(y) {}`. [[Complément hors du cours|ⓘ]]

`Point p1();` avec des parenthèses vides ne crée pas d'objet : le compilateur y lit la [[Déclaration et définition|déclaration]] d'une fonction `p1` renvoyant un `Point` (*most vexing parse*). On écrit `Point p1;` ou, depuis le C++11, `Point p1{};`. [[Complément hors du cours|ⓘ]]

## 7-constructeurCopie

**Ce que fait le programme.** D'après le code, l'exercice crée un `Point` ([[Classe et objet|objet]]) puis une copie de ce point, et affiche les deux avec [[Flux d'entrée-sortie (C++)|`std::cout`]].

Le **[[Constructeur (programmation)|constructeur de copie]]** permet de créer un objet comme copie d'un objet existant, plutôt qu'avec des valeurs par défaut ou des valeurs choisies. Il s'écrit :

```cpp
ClassName(const ClassName& autreObjet);
```

Si on n'en déclare pas, le compilateur en génère un automatiquement. Le fichier le montre en laissant en commentaire la version écrite à la main :

```cpp
#include <iostream>

class Point{
    public:
        int x, y;

        Point();   // constructeur par défaut
//      Point(const Point& autrePoint);   // constructeur de copie
};

Point::Point(){
    x = 0;
    y = 0;
}

/*Point::Point(const Point& autrePoint){
    x = autrePoint.x;
    y = autrePoint.y;
}*/

int main(){
    Point p1;      // constructeur par défaut : x = 0, y = 0
    Point p2(p1);  // constructeur de copie généré par le compilateur : x = 0, y = 0

    std::cout << "p1 : (" << p1.x << ", " << p1.y << ")" << std::endl;
    std::cout << "p2 : (" << p2.x << ", " << p2.y << ")" << std::endl;

    return 0;
}
```

Sortie :

```text
p1 : (0, 0)
p2 : (0, 0)
```

**Explications.**

- Le paramètre est une [[Référence (C++)|référence]] constante, `const Point&` : passer l'objet [[Passage par valeur|par valeur]] exigerait… de le copier, donc d'appeler le constructeur de copie lui-même, à l'infini ; c'est pourquoi la forme `Point(Point autre)` est refusée par le compilateur. Le `const` garantit que l'original n'est pas modifié.
- Le constructeur de copie généré copie les attributs un à un (copie membre à membre) : ici exactement ce que fait la version commentée.
- `Point p2(p1);` et `Point p2 = p1;` appellent tous deux le constructeur de copie ; il est aussi appelé quand on passe un objet par valeur à une fonction.

La copie membre à membre ne copie que les pointeurs, pas ce qu'ils désignent : pour une classe qui gère de la mémoire obtenue par [[Allocation dynamique|allocation dynamique]] (`new`), les deux objets partageraient le même bloc, et le second [[Destructeur (programmation)|destructeur]] le libérerait une deuxième fois. Il faut alors écrire une [[Copie superficielle et copie profonde|copie profonde]] et respecter la [[Destructeur (programmation)|règle de trois]] (constructeur de copie, opérateur d'affectation `operator=` et destructeur écrits ensemble) ; mieux, utiliser `std::vector` ou `std::string`, qui se copient correctement d'eux-mêmes (règle de zéro). [[Complément hors du cours|ⓘ]]

## 8-méthodes

**Ce que fait le programme.** D'après le code, l'exercice donne à la [[Classe et objet|classe]] `Television` un [[Constructeur (programmation)|constructeur par défaut]] et trois méthodes, `allumer`, `setVolume` et `getVolume` ([[Accesseur et mutateur|mutateur et accesseur]]), puis les appelle sur un objet. Il n'affiche rien.

```cpp
#include <iostream>

class Television{
    private:
        int volume;
        bool estAllumée;

    public:
        Television();   // constructeur par défaut

        void setVolume(int vol);
        int getVolume();
        void allumer();
};

Television::Television(){
    volume = 0;
    estAllumée = false;
}

void Television::allumer(){
    estAllumée = true;
}
void Television::setVolume(int vol){
    volume = vol;
}
int Television::getVolume(){
    return volume;
}

int main(){
    Television tv1;      // constructeur par défaut
    tv1.allumer();       // estAllumée = true
    tv1.setVolume(10);   // volume = 10

    return 0;
}
```

**Explications.**

- Les méthodes sont **déclarées** dans la classe et **définies en dehors**, avec le nom de la classe, `::` et le nom de la méthode : `void Television::allumer()`. Le type de retour se place devant `Television::`.
- On appelle une méthode sur un objet avec le point : `tv1.allumer()`. Dans le corps d'une méthode, les attributs (`volume`, `estAllumée`) s'emploient sans préfixe : ce sont ceux de l'objet sur lequel la méthode est appelée.
- `allumer` modifie un attribut privé sans le montrer : c'est l'[[Encapsulation (programmation)|encapsulation]], l'extérieur ne passe que par les méthodes publiques.

Un mutateur peut [[Validation des entrées|contrôler]] la valeur reçue avant de l'accepter (`if (vol >= 0 && vol <= 100) volume = vol;`) : c'est ce qui le distingue d'un attribut public et garantit que l'objet reste cohérent (son invariant). [[Complément hors du cours|ⓘ]]

Un accesseur qui ne modifie rien se déclare `int getVolume() const;` ([[Méthode constante|méthode constante]]) : il devient appelable sur un objet `const` ou reçu par référence constante, comme `const Point& p` en 12. Une méthode définie directement dans la classe, comme `getX()` en 10, est implicitement [[Fonction inline|`inline`]]. [[Complément hors du cours|ⓘ]]

## 9-méthodes2

**Ce que fait le programme.** D'après le code, l'exercice écrit une [[Classe et objet|classe]] `Personne` avec un nom ([[Classe string (C++)|`std::string`]]) et un âge ([[Type entier|`int`]]) [[Encapsulation (programmation)|privés]], un [[Constructeur (programmation)|constructeur par défaut]] et des [[Accesseur et mutateur|accesseurs et mutateurs]] (`get` / `set`) pour chacun, puis les utilise et affiche le résultat. C'est l'exemple de la section 6 de [[4 - C++]].

```cpp
#include <iostream>

class Personne{
    private:
        std::string nom;
        int age;

    public:
        Personne();   // constructeur par défaut
        void setNom(std::string n);
        std::string getNom();
        void setAge(int a);
        int getAge();
};

Personne::Personne(){
    nom = "inconnu";
    age = 0;
};

void Personne::setNom(std::string n){
    nom = n;
};
std::string Personne::getNom(){
    return nom;
};
void Personne::setAge(int a){
    age = a;
};
int Personne::getAge(){
    return age;
};

int main(){
    Personne p1;   // constructeur par défaut
    p1.setNom("momo");
    p1.setAge(20);

    std::cout << p1.getNom() << std::endl;
    std::cout << p1.getAge() << std::endl;

    return 0;
}
```

Sortie :

```text
momo
20
```

**Explications.**

- Le `set` (mutateur) reçoit une valeur en [[Argument et paramètre|paramètre]] et la range dans l'attribut ; le `get` (accesseur) la renvoie avec `return`. Leur type de retour est donc `void` pour le premier, le type de l'attribut pour le second.
- Les `;` placés après l'accolade de chaque définition de fonction sont inutiles mais permis (déclarations vides) ; seul celui qui ferme la classe est obligatoire.

`setNom(std::string n)` reçoit sa chaîne [[Passage par valeur|par valeur]], donc en fait une copie ; pour un objet comme `std::string`, on préfère `setNom(const std::string& n)` ([[Passage de paramètres|passage]] par [[Référence (C++)|référence constante]]), et `std::string getNom() const;`. [[Complément hors du cours|ⓘ]]

## 10-SurchargeOpérateurs1

**Ce que fait le programme.** D'après le code, l'exercice surcharge l'[[Opérateur unaire et opérateur binaire|opérateur unaire]] `-` pour la [[Classe et objet|classe]] `Point`, dotée d'un [[Constructeur (programmation)|constructeur]] par paramètres et d'[[Accesseur et mutateur|accesseurs]] (il renvoie le point de coordonnées opposées) et montre en passant pourquoi une fonction ne peut pas renvoyer deux valeurs avec `return x, y;`.

La [[Surcharge d'opérateurs|surcharge d'opérateurs]] (*operator overloading*) consiste à apprendre à ses objets à réagir aux opérateurs : [[Opérateurs arithmétiques|arithmétiques]] (`+`, `-`, `*`, `/`), de [[Opérateur de comparaison|comparaison]] (`==`, `!=`, `<`, `>`, `<=`, `>=`) ou [[Opérateur logique|logiques]] (`&&`, `||`, `!`). Concrètement : pour `int somme = a + b;`, le compilateur sait tout seul additionner deux entiers ; mais pour une classe `Point` de coordonnées `x` et `y`, il ne sait pas ce que veut dire additionner deux `Point` ou en inverser un. Un opérateur **unaire** ne concerne qu'un seul objet (`-a`, ou les [[Opérateur d'incrémentation|incrémentations]] `++a`, `--a`) ; voir [[Opérateur unaire et opérateur binaire]].

```cpp
#include <iostream>

class Point{
    private:
        int x;
        int y;

    public:
        Point(int a, int b){x = a;y = b;};   // constructeur avec paramètres

        Point operator-();   // surcharge de l'opérateur unaire -

//      Point getPoint(){return Point(x, y);};

        int getCoord(){return x, y; };   // ATTENTION : ne renvoie que y

        int getX(){return x;};
        int getY(){return y;};
};

// renvoie un nouvel objet Point avec les coordonnées inversées
Point Point::operator-(){
        return Point(-x, -y);
    }

int main(){
    Point p1(1,2);   // x = 1, y = 2
    Point p2 = -p1;  // appel de operator- sur p1 : x = -1, y = -2

    std::cout << "p1 : " << p1.getCoord() << std::endl;   // n'affiche que y

    std::cout << "p1 : " << p1.getX() << "," << p1.getY() << std::endl;
    std::cout << "p2 : " << p2.getX() << "," << p2.getY() << std::endl;

    return 0;
}
```

Sortie :

```text
p1 : 2
p1 : 1,2
p2 : -1,-2
```

**Explications.**

- **L'opérateur unaire.** On déclare dans la classe une méthode nommée `operator-`, sans paramètre puisque son seul opérande est l'objet lui-même ; elle renvoie un **nouvel** `Point(-x, -y)` sans modifier `p1`. L'écriture `-p1` est traduite par le compilateur en `p1.operator-()`.
- **`return x, y;` ne renvoie qu'une valeur.** Une fonction C++ ne renvoie qu'une seule valeur. Dans `return x, y;`, la virgule est l'[[Opérateur virgule|opérateur virgule]] : il évalue `x`, jette le résultat, puis renvoie seulement `y`. Le code compile, mais `getCoord()` renvoie 2 pour `p1`, et `g++ -Wall` le signale : `left operand of comma operator has no effect`.
- **`getPoint` est, lui, correct.** Dans le fichier, l'explication sur l'opérateur virgule était accolée à la ligne commentée `Point getPoint(){return Point(x, y);};` ; elle ne la concerne pas : dans `Point(x, y)`, la virgule sépare les deux [[Argument et paramètre|arguments]] du constructeur, ce n'est pas l'opérateur virgule. `getPoint` compile et renvoie bien un `Point` contenant les deux coordonnées (vérifié : `1,2`) ; c'est justement la bonne façon de renvoyer « deux valeurs » : les regrouper dans un objet. [[Erreurs du cours#^e-formation-c|✎]]

Pour renvoyer plusieurs valeurs, la bibliothèque standard offre aussi `std::pair` et `std::tuple` ([[Paire et tuple (C++)]]) : `std::pair<int,int> getCoord() { return {x, y}; }`, et côté appelant, depuis le C++17, `auto [a, b] = p1.getCoord();` (liaison structurée). Autre solution, le passage par [[Référence (C++)|référence]] de deux paramètres de sortie. [[Complément hors du cours|ⓘ]]

L'opérateur `-` ne modifie pas l'objet : on le déclare `Point operator-() const;` ([[Méthode constante]]). Certains opérateurs ne peuvent pas être surchargés (`::`, `.`, `.*`, `?:`, `sizeof`), et la surcharge ne change ni la priorité ni l'[[Associativité et ordre d'évaluation|associativité]] d'un opérateur. Surcharger `&&`, `||` ou la virgule est déconseillé : les versions surchargées perdent l'[[Évaluation en court-circuit|évaluation en court-circuit]] ou l'ordre d'évaluation garanti. [[Complément hors du cours|ⓘ]]

## 11-surchargeOperateurs2

**Ce que fait le programme.** D'après le code, l'exercice [[Surcharge d'opérateurs|surcharge]] l'[[Opérateur unaire et opérateur binaire|opérateur binaire]] `+` pour additionner coordonnée par coordonnée deux objets `Point` ([[Classe et objet]]), puis affiche le résultat avec [[Flux d'entrée-sortie (C++)|`std::cout`]].

Un opérateur **binaire** relie deux objets : `+`, `==`, `<`, etc. ; dans `a+b`, `+` relie `a` et `b`.

```cpp
#include <iostream>

class Point{
    private:
        int x;
        int y;

    public:
        Point(int a, int b){x = a;y = b;};   // constructeur avec paramètres

        Point operator+(Point autrePoint);   // opérateur +

        int getX(){return x;};
        int getY(){return y;};
};

Point Point::operator+(Point autrePoint){
    return(Point(x + autrePoint.x, y + autrePoint.y));
};

int main(){
    Point p1(1, 2);
    Point p2(3, 4);
    Point p3 = p1+p2;   // additionne les coordonnées de p1 et p2

    std::cout << p3.getX() << p3.getY() << std::endl;

    return 0;
}
```

Sortie : `46`, c'est-à-dire `x = 4` et `y = 6` collés, faute de séparateur dans l'affichage (`<< "," <<` les séparerait).

**Explications.**

- Écrit comme méthode, l'opérateur binaire prend **un** [[Argument et paramètre|paramètre]], reçu ici [[Passage par valeur|par valeur]] : l'opérande de droite. L'opérande de gauche est l'objet sur lequel la méthode est appelée : `p1+p2` est traduit en `p1.operator+(p2)`.
- Dans `operator+`, on lit `autrePoint.x` alors que `x` est privé : c'est permis, car le contrôle d'accès se fait **par classe** et non par objet ; toute méthode de `Point` accède aux membres privés de n'importe quel `Point`.

Forme recommandée : `Point operator+(const Point& autre) const;`, avec une [[Référence (C++)|référence constante]] pour éviter la copie du paramètre et `const` parce que `p1` n'est pas modifié. On écrit souvent `+` comme fonction libre (hors de la classe), souvent à partir de `+=` : ainsi la conversion implicite s'applique aux deux opérandes de la même façon. [[Complément hors du cours|ⓘ]]

## 12-operateursAffichage

**Ce que fait le programme.** D'après le code, l'exercice permet d'écrire `std::cout << p1` pour un `Point`, en définissant l'opérateur de sortie `<<` comme [[Fonction amie (friend)|fonction amie]] de la classe.

Si on crée un point `p1` et qu'on écrit `std::cout << p1 << std::endl;`, cela ne compile pas : le C++ ne connaît pas `Point` comme il connaît un [[Type char|`char`]] ou un [[Type entier|`int`]] ([[Erreur de compilation|erreur de compilation]] `no match for 'operator<<'`). Il faut créer un *output operator*, c'est-à-dire définir le comportement de `<<` pour la classe `Point` ([[Surcharge d'opérateurs]]).

```cpp
#include <iostream>

class Point{
    private:
        int x;
        int y;

    public:
        Point(int a, int b);

        // l'output operator
        friend std::ostream& operator<<(std::ostream& os, const Point& p){
            os << p.x << "," << p.y ;
            return os;
        }
};

Point::Point(int a, int b){
    x = a;
    y = b;
};

int main(){
    Point p1(1,2);

    std::cout << p1 << std::endl;   // fonctionne : << sait maintenant afficher un Point

    return 0;
}
```

Sortie : `1,2`.

**Pourquoi `friend`.** Le fichier analyse longuement cet opérateur ; voici ses explications, dans l'ordre.

- `friend` veut dire « tu peux accéder aux `x` et `y` privés », car `<<` n'est **pas une méthode** de la classe `Point`. Dans `std::cout << p1`, l'opérande de gauche est `std::cout` : pour en faire une méthode, il faudrait théoriquement ajouter `operator<<` à l'intérieur de la classe `std::ostream` de la [[Bibliothèque standard du C++|bibliothèque standard]], ce qu'on ne peut pas faire.
- L'opérateur `<<` doit donc s'écrire en dehors de la classe, comme une fonction qui prend deux paramètres : le flux à gauche et le point à droite (`operator<<(os, p)`).
- Ou alors il peut s'écrire dans la classe, si on le déclare `friend`. Même écrit dans la classe, il reste une fonction libre et non une méthode : `friend` lui donne seulement l'accès aux membres privés.

**La signature en détail** : `friend std::ostream& operator<<(std::ostream& os, const Point& p)`.

- `operator<<` est le nom de la surcharge, comme `operator+` et `operator-` dans 10 et 11.
- `std::ostream` (*output stream*, flux de sortie) est une **classe** de la bibliothèque standard, qui gère la façon dont les données sont envoyées vers une destination, en général l'écran du terminal ; `std::cout` est un **objet** de cette classe. Le fichier disait que `ostream` est un objet et développait le nom en *Standard Output Stream*. [[Erreurs du cours#^e-formation-c|✎]]
- Le `&` fait un passage par [[Référence (C++)|référence]] : la fonction travaille directement sur le véritable flux actif (`std::cout`), sans en faire une copie inutile, et peut le renvoyer pour enchaîner les affichages. Image du fichier : une référence, c'est comme prêter le document original au lieu d'en donner une photocopie ; la fonction agit sur l'original qui est en mémoire.
- `std::ostream& os` (à gauche) représente le flux de sortie, ici `std::cout`.
- `const Point& p` (à droite) représente l'objet `Point` à afficher. Le `const` est là parce qu'on a seulement besoin de lire le point : il protège contre les modifications accidentelles.
- Le corps `os << p.x << "," << p.y; return os;` injecte dans le flux `os` le texte à afficher, ici `x,y`, puis renvoie le flux.

Une référence n'est pas, pour le programmeur, une adresse : c'est un autre nom (un alias) de l'objet d'origine, qui s'emploie sans `*` ni `&` ; le compilateur la réalise en général avec une adresse, mais il ne faut pas la confondre avec l'[[Opérateur d'adresse|opérateur d'adresse]] `&x` ni avec un [[Pointeur et adresse mémoire|pointeur]]. [[Complément hors du cours|ⓘ]]

Le passage par référence n'est pas seulement plus économique : il est **obligatoire** pour le flux, car `std::ostream` n'est pas copiable (son constructeur de copie est supprimé ; `std::ostream o2 = std::cout;` ne compile pas). Le retour par référence permet l'enchaînement : `std::cout << p1 << std::endl` se lit `(std::cout << p1) << std::endl`, l'opérateur `<<` étant associatif à gauche ([[Associativité et ordre d'évaluation]]). [[Complément hors du cours|ⓘ]]

`os` n'est pas forcément `std::cout` : le même opérateur écrit un `Point` dans `std::cerr`, dans un fichier (`std::ofstream`) ou dans une chaîne (`std::ostringstream`), qui dérivent tous de `std::ostream` ([[Héritage (programmation)|héritage]]). Et grâce au `const Point&`, on peut afficher un objet temporaire : `std::cout << Point(3, 4);`. [[Complément hors du cours|ⓘ]]

L'opérateur de lecture se construit de la même façon : `friend std::istream& operator>>(std::istream& is, Point& p) { return is >> p.x >> p.y; }`, avec cette fois un `Point&` non constant puisqu'il est modifié. Sans `friend`, l'opérateur `<<` peut aussi s'écrire hors de la classe en passant par les accesseurs publics (`os << p.getX() << "," << p.getY();`, avec des `get` déclarés `const`). [[Complément hors du cours|ⓘ]]

## À retenir

- Un [[Valeur littérale|littéral]] [[Type char|`char`]] s'écrit entre apostrophes (`'e'`), une [[Chaîne de caractères|chaîne]] entre guillemets (`"e"`) ; `2.3` est un `double`, `2.3f` un `float` ([[Nombre à virgule flottante]]).
- `std` est un [[Espace de noms (namespace)|espace de noms]], `std::cout` un objet ; `>>` pour lire avec `cin`, `<<` pour écrire avec `cout` ([[Flux d'entrée-sortie (C++)]]) ; `std::endl` = `'\n'` + vidage du [[Tampon (buffer)|tampon]].
- `do … while` s'exécute au moins une fois, `while` peut ne jamais s'exécuter ([[Boucle (programmation)]]) ; le ternaire s'écrit `c ? a : b` ([[Opérateur conditionnel]]).
- Attributs privés, méthodes publiques ([[Encapsulation (programmation)|encapsulation]]) ; une méthode se définit hors de la classe avec `Classe::methode` ([[Opérateur de résolution de portée]]) ; un [[Accesseur et mutateur|accesseur]] renvoie le type de l'attribut, pas `void`.
- Un [[Constructeur (programmation)|constructeur]] porte le nom de la classe et n'a pas de type de retour ; déclarer un constructeur supprime le constructeur par défaut implicite, et une classe sans constructeur laisse ses `int` [[Variable non initialisée|non initialisés]].
- Le constructeur de copie prend `const Classe&` ; celui que génère le compilateur copie membre à membre ([[Copie superficielle et copie profonde|copie superficielle]]), ce qui ne suffit plus dès que la classe possède de la mémoire allouée.
- `return x, y;` ne renvoie que `y` ([[Opérateur virgule|opérateur virgule]]) ; pour renvoyer plusieurs valeurs, les regrouper dans un objet (`Point`, `std::pair`).
- [[Opérateur unaire et opérateur binaire|Opérateur unaire]] en méthode : aucun paramètre ; binaire : un paramètre (l'opérande de droite) ; `<<` d'affichage : fonction libre, souvent [[Fonction amie (friend)|`friend`]], qui prend et renvoie `std::ostream&`.
- Passer les objets par `const&` ([[Référence (C++)|référence constante]] : paramètres de `operator+`, de `operator<<`, de `setNom`) et déclarer `const` les [[Méthode constante|méthodes qui ne modifient rien]].
- Compiler avec `-Wall -Wextra` ([[Option de compilation|options]] de [[GCC]]) : c'est l'[[Avertissement de compilation|avertissement]] du compilateur qui a révélé le piège de `getCoord`.
