---
type: concept
tags: [year4]
aliases: [constructeur, constructor, constructeur par défaut, constructeur par paramètres, constructeur par copie, default constructor, copy constructor, liste d'initialisation]
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

Notion parente : [[Classe et objet]]. Voir aussi : [[Programmation orientée objet]], [[Méthode spéciale Python]] (`__init__` joue ce rôle en Python).

Résumés : [[4 - C++]], [[4 - Prise de note]]
