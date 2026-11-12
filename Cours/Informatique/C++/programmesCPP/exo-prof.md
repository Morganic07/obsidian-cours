---
type: source
tags: [year4]
sources:
  - "[[Raw/Year 4/C／C++/programmes C++/exo-prof/classePoint.cpp|classePoint.cpp]]"
  - "[[Raw/Year 4/C／C++/programmes C++/exo-prof/classePoint2.cpp|classePoint2.cpp]]"
  - "[[Raw/Year 4/C／C++/programmes C++/exo-prof/classeSegment.cpp|classeSegment.cpp]]"
maj: 2026-11-12
complet: true
enrichi: 2026-11-12
---

Programmes du dossier `exo-prof` (trois fichiers), dans [[Cours/Informatique/C++/_index|C++]] : la solution de l'« exercice type (I) » de [[4 - C++]], qui demande une [[Classe et objet|classe]] `Point` puis une classe `Segment` en [[Langage C++|C++]]. On y retrouve la [[Programmation orientée objet|programmation orientée objet]] du chapitre 4 : [[Encapsulation (programmation)|données privées]], les trois [[Constructeur (programmation)|constructeurs]] (par défaut, par paramètres, par copie), les [[Accesseur et mutateur|accesseurs et mutateurs]] (get et set), l'affichage, d'abord par [[Surcharge d'opérateurs|surcharge de l'opérateur]] `<<`, puis par une simple méthode. Les mêmes classes sont ensuite découpées en plusieurs fichiers dans [[compilation séparée (C++)]], qui illustre [[5 - Compilation séparée]].

## classePoint.cpp

D'après le code, l'exercice demande une classe `Point` à deux coordonnées entières privées, avec trois constructeurs, `set`, `getX`, `getY`, l'opérateur d'affichage `<<` et une méthode `distance_origine`, puis une [[Fonction main (C et C++)|fonction `main`]] qui teste le tout.

```cpp
#include <iostream>
#include <cmath>

class Point{
    private :
        int x;
        int y;

    public :
        // trois constructeurs
        Point();
        Point(int a, int b);
        Point(const Point& autrePoint);

        // get et set
        void set(int user_x, int user_y){x = user_x; y = user_y;}
        int getX(){return x;}
        int getY(){return y;}

        // opérateur d'affichage
        friend std::ostream& operator<<(std::ostream& os, const Point& p){
            os << p.x << "," << p.y ; return os;}

        // distance à l'origine
        float distance_origine(){
            return std::sqrt(x*x + y*y);
        }
};

// constructeur par défaut
Point::Point(){
    x = 0;
    y = 0;
}

// constructeur par paramètres
Point::Point(int a, int b){
    x = a;
    y = b;
}

// constructeur par copie
Point::Point(const Point& autrePoint){
    x = autrePoint.x;
    y = autrePoint.y;
}

int main(){
    // test des 3 constructeurs
    Point p1;
    std::cout << p1 << std::endl;

    Point p2(1,2);
    std::cout << p2 << std::endl;

    Point p3(p2);
    std::cout << p3 << std::endl;

    // test de set et get
    p3.set(2,2);
    std::cout << p3.getX() << "," << p3.getY() << std::endl;

    // test distance_origine
    std::cout << p3.distance_origine() << std::endl;

    return 0;
}
```

Sortie :

```text
0,0
1,2
1,2
2,2
2.82843
```

**Explications.**

- **`private :` / `public :`** : les attributs `x` et `y`, deux [[Variable (programmation)|variables]] propres à chaque objet, sont privés, inaccessibles hors de la classe ; on les lit par `getX()`, `getY()` et on les modifie par `set()`. C'est l'[[Encapsulation (programmation)|encapsulation]] du chapitre 4.
- **Déclaration dans la classe, définition dehors.** Les trois constructeurs sont seulement [[Déclaration et définition|déclarés]] dans la classe, puis définis après elle sous leur nom complet `Point::Point`, avec l'[[Opérateur de résolution de portée|opérateur de résolution de portée]] `::`. Les méthodes courtes (`set`, `getX`, `getY`, `distance_origine`) sont au contraire définies directement dans la classe.
- **Les trois constructeurs** assurent l'[[Initialisation (programmation)|initialisation]] de l'objet : `Point p1;` appelle le constructeur par défaut (0, 0) ; `Point p2(1,2);` le constructeur par paramètres ; `Point p3(p2);` le constructeur par copie, qui reçoit l'objet à copier par [[Référence (C++)|référence constante]] (`const Point&`).
- **`operator<<`** : déclaré [[Fonction amie (friend)|`friend`]], ce n'est pas une méthode de `Point` mais une fonction libre autorisée à lire `p.x` et `p.y`, qui sont privés. Il reçoit le [[Flux d'entrée-sortie (C++)|flux]] `os` par référence, écrit dedans et le renvoie, ce qui permet d'enchaîner `std::cout << p1 << std::endl;`. Le préfixe `std::` désigne l'[[Espace de noms (namespace)|espace de noms]] de la [[Bibliothèque standard du C++|bibliothèque standard]].
- **`distance_origine`** applique le [[Théorème de Pythagore|théorème de Pythagore]] : $\sqrt{x^2 + y^2}$, soit $\sqrt{2^2 + 2^2} = \sqrt 8 = 2\sqrt 2 \approx 2{,}82843$ pour $(2, 2)$. `std::sqrt` est la [[Racine carrée|racine carrée]] de la [[Bibliothèque cmath|bibliothèque `<cmath>`]].

Une méthode définie dans le corps de la classe est implicitement [[Fonction inline|`inline`]] : on peut la placer dans un [[Fichier d'en-tête|en-tête]] inclus par plusieurs fichiers sans violer la [[Règle de la définition unique|règle de la définition unique]]. C'est pourquoi les accesseurs d'une ligne s'écrivent souvent ainsi. [[Complément hors du cours|ⓘ]]

`std::sqrt(x*x + y*y)` reçoit un `int`, que la surcharge entière de `<cmath>` traite comme un `double`, et renvoie un `double` ; le `return` le convertit implicitement en `float` ([[Transtypage|conversion implicite]], avec perte de précision : un `float` garde environ 7 chiffres significatifs, un `double` environ 16, voir [[Nombre à virgule flottante]]). Renvoyer `double` est l'usage. Pour de grandes coordonnées, `x*x` peut aussi dépasser la capacité d'un `int` ([[Dépassement d'entier|dépassement d'entier]], dès 46 341 pour un `int` de 32 bits, puisque $46\,341^2 > 2^{31} - 1$) ; `std::hypot(x, y)` calcule $\sqrt{x^2+y^2}$ sans ce risque. [[Complément hors du cours|ⓘ]]

Les accesseurs qui ne modifient pas l'objet devraient être déclarés [[Méthode constante|constants]] : `int getX() const { return x; }`. Sans `const`, on ne peut pas les appeler sur un `const Point&`, par exemple dans `operator<<` (qui lit ici directement `p.x` grâce à `friend`). `classeSegment.cpp` corrige ce point. [[Complément hors du cours|ⓘ]]

Le constructeur par copie écrit ici fait exactement ce que ferait celui que le compilateur génère (copie attribut par attribut) : on peut l'omettre, ou l'écrire `Point(const Point&) = default;`. Les constructeurs s'écrivent aussi plus idiomatiquement avec une [[Liste d'initialisation|liste d'initialisation]] : `Point::Point(int a, int b) : x(a), y(b) {}`. [[Complément hors du cours|ⓘ]]

L'énoncé de [[4 - C++]] demande des coordonnées réelles ; le programme les déclare `int` ([[Type entier|entiers]]), si bien que `p.set(1.5, 2)` tronquerait 1,5 en 1. Avec `double x, y;`, le reste du code est inchangé.

## classePoint2.cpp

D'après le code, l'exercice est le même, avec une méthode `affiche()` à la place de l'opérateur `<<`. Le commentaire du fichier en donne la raison : le professeur juge la surcharge de l'opérateur d'affichage trop complexe à ce stade et demande une simple fonction d'affichage.

Seules les parties qui changent par rapport à `classePoint.cpp` (attributs, constructeurs, `set`, `get` et `distance_origine` identiques) :

```cpp
class Point{
    // ... attributs et autres méthodes identiques ...
    public :
        // fonction d'affichage (pas d'opérateur d'affichage)
        void affiche();
};

// fonction affiche
void Point::affiche(){
    std::cout << x << ","<< y << std::endl;
}

int main(){
    // test des 3 constructeurs
    Point p1;
    p1.affiche();

    Point p2(1,2);
    p2.affiche();

    Point p3(p2);
    p3.affiche();

    // test de set et get
    p3.set(2,2);
    p3.affiche();

    // test distance_origine
    std::cout << p3.distance_origine() << std::endl;

    return 0;
}
```

Sortie identique à celle de `classePoint.cpp` (`0,0`, `1,2`, `1,2`, `2,2`, `2.82843`).

**Explications.**

- **`affiche()` est une méthode** : déclarée dans la classe, définie dehors par `void Point::affiche()`. Elle a accès aux attributs privés sans `friend`, puisqu'elle est membre de la classe, et s'appelle sur un objet : `p1.affiche();`.
- **Différence avec `operator<<`** : `affiche()` écrit toujours sur `std::cout` et termine la ligne par `std::endl` ; on ne peut pas l'insérer au milieu d'une expression `std::cout << … << …`.
- Le test de `set` et `get` n'appelle plus `getX()` ni `getY()` : il affiche le point après `set(2,2)`.

`operator<<` reste la forme idiomatique en C++ : il marche avec tout flux (`std::cout`, `std::cerr`, les deux [[Flux standard|flux standard]] de sortie et d'erreur, un fichier `std::ofstream`, un `std::ostringstream`), s'enchaîne, et laisse l'appelant décider du saut de ligne ; la classe se borne à dire comment elle s'écrit, l'appelant choisit où ([[Principe de responsabilité unique|principe de responsabilité unique]]). Une méthode `affiche` peut garder la même souplesse en prenant le flux en paramètre : `void affiche(std::ostream& os = std::cout) const;`. [[Complément hors du cours|ⓘ]]

`std::endl` écrit un saut de ligne **et vide le [[Tampon (buffer)|tampon]]** du flux ; `'\n'` n'écrit que le saut de ligne. Dans une boucle qui affiche beaucoup de lignes, `'\n'` est nettement plus rapide. [[Complément hors du cours|ⓘ]]

## classeSegment.cpp

D'après le code, l'exercice demande une classe `Segment` formée de deux `Point` `A` et `B` et d'une longueur, avec ses trois constructeurs, ses accesseurs, une méthode d'affichage et le calcul de la longueur, puis un `main` de test.

La classe `Point` est reprise de `classePoint2.cpp`, avec deux changements : les accesseurs deviennent constants (`int getX() const`) et l'affichage s'appelle `affichePoint()`, au format `(x, y)`.

```cpp
#include <iostream>
#include <cmath>

// --- CLASSE POINT ---
class Point {
private:
    int x;
    int y;

public:
    Point();
    Point(int a, int b);
    Point(const Point& autrePoint);

    void set(int user_x, int user_y) { x = user_x; y = user_y; }
    int getX() const { return x; }
    int getY() const { return y; }

    // affichage simple (demandé par le prof)
    void affichePoint(){
        std::cout << "(" << x << ", " << y << ")" << std::endl;
    }
};

// constructeurs de Point : identiques à classePoint.cpp

// --- CLASSE SEGMENT ---
class Segment {
private:
    Point A;
    Point B;
    float longueur;

public:
    Segment();
    Segment(Point p1, Point p2);
    Segment(const Segment& autreSegment);

    Point getA(){ return A; }
    Point getB(){ return B; }
    float getLongueur(){ return calculerLongueur(); }

    void afficheSegment(){
        A.affichePoint();
        B.affichePoint();
        std::cout << calculerLongueur() << std::endl;
    }

    float calculerLongueur();
};

// constructeur par défaut
Segment::Segment(){A.set(0,0); B.set(0,0); longueur = calculerLongueur();}

// constructeur par paramètres
Segment::Segment(Point a, Point b){
    A.set(a.getX(), a.getY());
    B.set(b.getX(), b.getY());
    longueur = calculerLongueur();
}

// constructeur par copie
Segment::Segment(const Segment& autreSegment){
    A = autreSegment.A;
    B = autreSegment.B;
    longueur = autreSegment.longueur;
}

float Segment::calculerLongueur(){
        int dx = B.getX() - A.getX();
        int dy = B.getY() - A.getY();
        longueur = std::sqrt(dx * dx + dy * dy);
        return longueur;
    }

int main() {
    Point origine;
    Point point1(3, 4);
    Point point2(6, 8);

    std::cout << "Points : ";
    origine.affichePoint();
    std::cout << " et ";
    point1.affichePoint();
    std::cout << std::endl;

    Segment segmentDefaut;
    Segment segment(point1, point2);

    std::cout << "Segment par défaut : ";
    segmentDefaut.afficheSegment();
    std::cout << "Segment entre ";
    segment.afficheSegment();
    std::cout << "Longueur : " << segment.getLongueur() << std::endl;

    Segment copie(segment);
    std::cout << "Copie du segment : ";
    copie.afficheSegment();

    return 0;
}
```

Sortie :

```text
Points : (0, 0)
 et (3, 4)

Segment par défaut : (0, 0)
(0, 0)
0
Segment entre (3, 4)
(6, 8)
5
Longueur : 5
Copie du segment : (3, 4)
(6, 8)
5
```

**Explications.**

- **Un objet qui contient des objets** : `Segment` a pour attributs deux `Point`. À la création d'un `Segment`, `A` et `B` sont d'abord construits par le constructeur par défaut de `Point` (donc à (0, 0)), avant l'exécution du corps du constructeur de `Segment`, qui les modifie ensuite par `set`.
- **Constructeur par paramètres** : il reçoit deux `Point` **par valeur** ([[Argument et paramètre|paramètres]] copiés à l'[[Appel de fonction|appel]] par le constructeur par copie de `Point`) et recopie leurs coordonnées dans `A` et `B` par `set(getX(), getY())`. `getX()` et `getY()` étant publics, `Segment` n'a pas besoin d'accéder aux attributs privés de `Point`.
- **Constructeur par copie** : `A = autreSegment.A;` est une affectation entre deux `Point` déjà construits, qui utilise l'opérateur d'affectation `operator=` généré par le compilateur.
- **`calculerLongueur`** applique la [[Distance|distance euclidienne]] : $AB = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$. Pour $A(3, 4)$ et $B(6, 8)$ : $\sqrt{3^2 + 4^2} = 5$. Elle range le résultat dans l'attribut `longueur` et le renvoie.
- **L'attribut `longueur`** se déduit de `A` et `B` : c'est pourquoi le cours signale le `set` de `Longueur` par « /!\ ». Le programme n'en propose pas, et `getLongueur()` recalcule la longueur à chaque appel, si bien qu'elle ne peut pas être fausse.
- **La mise en page de la sortie** : `affichePoint()` termine chaque point par `std::endl`, d'où le passage à la ligne avant « et » et la ligne vide qui suit.

Avec `-Wall -Wextra`, [[GCC]] signale deux fois `implicitly-declared 'Point& Point::operator=(const Point&)' is deprecated [-Wdeprecated-copy]` ([[Avertissement de compilation|avertissement]], pas une erreur). Depuis C++11, la [[Norme du C++|norme]] déconseille de laisser le compilateur générer l'[[Opérateur d'affectation par copie|opérateur d'affectation par copie]] d'une classe dont le constructeur par copie est écrit à la main : si l'un des deux a besoin d'un code particulier, l'autre aussi (règle de trois, voir [[Destructeur (programmation)]]). La solution la plus simple est la [[Règle de zéro|règle de zéro]] : ne pas écrire le constructeur par copie de `Point`, puisque la version générée fait la même chose. Ces versions générées font une [[Copie superficielle et copie profonde|copie superficielle]], attribut par attribut, suffisante pour des `int`. [[Complément hors du cours|ⓘ]]

Que `Segment` contienne deux `Point` s'appelle la [[Composition (programmation)|composition]] (relation « a un »), à distinguer de l'[[Héritage (programmation)|héritage]] (relation « est un ») : un segment n'est pas un point. Les attributs objets s'initialisent idéalement dans la [[Liste d'initialisation|liste d'initialisation]], ce qui évite de les construire à (0, 0) pour les modifier aussitôt : `Segment::Segment(const Point& a, const Point& b) : A(a), B(b), longueur(0) { longueur = calculerLongueur(); }`. Passer les `Point` par référence constante évite aussi deux copies. [[Complément hors du cours|ⓘ]]

Garder `longueur` en attribut pose un problème d'[[Invariant de classe|invariant de classe]] : la propriété « `longueur` est la distance de `A` à `B` » doit rester vraie après chaque opération, donc tout futur `setA` ou `setB` devrait la recalculer. Ici `calculerLongueur()` et `getLongueur()` modifient l'attribut à chaque lecture, un [[Effet de bord|effet de bord]] qui les empêche d'être [[Méthode constante|constantes]]. Le plus sûr est de ne pas stocker la longueur et d'écrire `float longueur() const { … }`, qui la calcule à la demande. [[Complément hors du cours|ⓘ]]

`getA()` et `getB()` renvoient une **copie** du point (retour [[Passage par valeur|par valeur]]) : modifier le résultat ne modifie pas le segment, ce qui préserve l'encapsulation. Pour éviter la copie sans l'exposer, on renvoie une référence constante : `const Point& getA() const { return A; }`. [[Complément hors du cours|ⓘ]]

## Compilation et vérification

Les trois fichiers compilent avec `g++ -std=c++17 -Wall -Wextra fichier.cpp -o prog` ([[Option de compilation|options de compilation]] : version de la norme, avertissements) ; seul `classeSegment.cpp` produit les avertissements `-Wdeprecated-copy` décrits plus haut. Chaque fichier redéfinit sa propre classe `Point` : ce sont trois programmes indépendants, et le copier-coller de la classe nuit à la [[Maintenabilité|maintenabilité]] (une correction est à reporter trois fois). Pour réutiliser une même classe dans plusieurs programmes sans la recopier, on la place dans un couple `Point.h` / `Point.cpp`, ce que fait [[compilation séparée (C++)]] ([[Réutilisation de code|réutilisation de code]], [[Programmation modulaire|programmation modulaire]], séparation [[Interface et implémentation|interface et implémentation]]). [[Complément hors du cours|ⓘ]]

## À retenir

- Une classe se teste méthode par méthode dans `main` : chaque constructeur, chaque accesseur, l'affichage, chaque calcul, en vérifiant la sortie à la main ($\sqrt 8 \approx 2{,}83$, $AB = 5$).
- `operator<<` est une fonction amie qui renvoie le flux reçu ; une méthode `affiche()` est plus simple mais moins souple.
- Le constructeur par copie prend `const Point&` ; `A = autre.A;` entre objets existants est une affectation (`operator=`), pas une copie-construction. [[Complément hors du cours|ⓘ]]
- Les attributs objets sont construits **avant** le corps du constructeur : les initialiser dans la liste d'initialisation. [[Complément hors du cours|ⓘ]]
- Un accesseur qui ne modifie rien se déclare `const`. [[Complément hors du cours|ⓘ]]
- Une valeur qui se déduit des autres attributs (la longueur) se calcule plutôt qu'elle ne se stocke ; stockée, elle doit être recalculée à chaque modification.
- `-Wdeprecated-copy` signale un constructeur par copie écrit sans opérateur d'affectation : écrire les deux, ou aucun (règle de zéro). [[Complément hors du cours|ⓘ]]
- `std::sqrt` renvoie un `double` : préférer `double` à `float` pour une distance. [[Complément hors du cours|ⓘ]]
