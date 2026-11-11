---
type: concept
tags: [year4]
aliases: [constructeur, constructor, constructeur par défaut, constructeur par paramètres, constructeur par copie, default constructor, copy constructor]
sources: ["[[Raw/Year 4/C++/chp4 C++.pdf|chp4 C++.pdf]]", "[[Raw/Year 4/C++/chp4 prise de note.pdf|chp4 prise de note.pdf]]"]
maj: 2026-11-08
---

**Définition** (d'après [[4 - C++]]) : un constructeur est une méthode spéciale **appelée automatiquement à la création d'un objet**. Il **porte le nom de la classe** et **n'a pas de type de retour**.

## Les trois constructeurs du cours

| Constructeur | Signature | Appel | Effet |
|---|---|---|---|
| par défaut | `Point()` | `Point p;` | aucun paramètre ; met l'objet dans un état connu, ici (0, 0) |
| par paramètres | `Point(int a, int b)` | `Point p1(3, 4);` ou `Point p2{5, 6};` | recopie les valeurs reçues dans les attributs |
| par copie | `Point(const Point& autre)` | `Point p2(p1);` ou `Point p2 = p1;` | crée un nouvel objet à partir d'un objet existant, reçu par [[Référence (C++)\|référence constante]] |

```cpp
class Point {
private:
    int x, y;
public:
    Point() { x = 0; y = 0; }
    Point(int a, int b) { x = a; y = b; }
    Point(const Point& autre) { x = autre.x; y = autre.y; }
};
```

Écriture équivalente du constructeur par défaut, par **liste d'initialisation** : `Point() : x(0), y(0) {}`.

## Règles à retenir

- **Sans constructeur**, les attributs ne sont pas initialisés et contiennent une valeur indéterminée (voir [[Variable non initialisée]]).
- **Le compilateur choisit** le constructeur d'après les arguments : `Point a;` appelle `Point()`, `Point b(3, 4);` appelle `Point(int, int)`.
- **Dès qu'on définit un constructeur, le compilateur ne génère plus de constructeur par défaut** : avec seulement `Point(int, int)`, `Point a;` ne compile plus.
- **Constructeur par copie implicite** : si on ne l'écrit pas, le compilateur en génère un qui recopie chaque attribut un par un. Les deux objets sont ensuite indépendants.
- **La copie a lieu** à l'initialisation (`Point p2 = p1;`), au passage par valeur d'un paramètre (voir [[Passage par valeur]]) et au retour d'une fonction par valeur.
- Dans les exercices, la consigne est d'écrire **toujours les trois constructeurs** dans une classe ([[4 - Prise de note]]).
- **Piège** relevé dans [[4 - Prise de note]] : écrire `int x = 0;` dans le constructeur déclare une variable locale qui masque l'attribut ; il faut `x = 0;`.

## Compléments (hors du cours)

- **`Point p;` s'écrit sans parenthèses** : `Point p();` ne crée pas d'objet, il déclare une fonction `p` sans paramètre qui renvoie un `Point`.
- **Liste d'initialisation ou corps** : la liste (`Point(int a, int b) : x(a), y(b) {}`) **initialise** les attributs, alors que le corps les **affecte** après coup, une fois qu'ils existent déjà. Elle est donc obligatoire pour un attribut `const` ou une référence, qui ne peuvent pas être affectés. Les attributs sont initialisés dans l'ordre de leur déclaration dans la classe, quel que soit l'ordre écrit dans la liste.
- **Initialisation uniforme** (C++11) : `Point p{5, 6};` refuse les conversions avec perte (*narrowing*) ; `Point p{5.7, 6};` ne compile pas, alors que `Point p(5.7, 6);` tronque `5.7` en `5`.
- **`Point() = default;`** redemande le constructeur par défaut généré par le compilateur quand un autre constructeur a été écrit.
- **Valeurs par défaut** : avec `Point(int a = 0, int b = 0)`, un seul constructeur accepte 0, 1 ou 2 arguments. Le choix du constructeur d'après les arguments relève de la surcharge de fonctions.
- **Le paramètre du constructeur par copie doit être une référence** : passé par valeur, il faudrait déjà copier l'argument pour l'appeler, donc rappeler le constructeur par copie, d'où une récursion infinie (le compilateur refuse).
- **Copie ou affectation** : `Point p2 = p1;` crée `p2`, donc appelle le constructeur par copie ; `p2 = p1;` entre deux objets déjà créés appelle l'opérateur d'affectation `operator=` (voir [[Surcharge d'opérateurs]]).
- **Copie superficielle** : la copie générée recopie les attributs un par un, donc recopie l'adresse d'un pointeur et non la zone pointée. Une classe qui gère de la mémoire dynamique a besoin d'une **copie profonde**, d'un [[Destructeur (programmation)|destructeur]] et d'un `operator=` écrits à la main (**règle de trois**).

Notion parente : [[Classe et objet]]. Voir aussi : [[Programmation orientée objet]], [[Destructeur (programmation)]], [[Allocation dynamique]], [[Méthode spéciale Python]] (`__init__` joue ce rôle en Python).

Résumés : [[4 - C++]], [[4 - Prise de note]]
