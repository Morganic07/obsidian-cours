---
type: concept
tags: [year4]
aliases: [classe, objet, class, object, instance, instance de classe, attribut, fonction membre, méthode (programmation), opérateur de résolution de portée]
matieres: [C++]
sources: ["[[Raw/Year 4/C++/chp4 C++.pdf|chp4 C++.pdf]]", "[[Raw/Year 4/C++/chp4 prise de note.pdf|chp4 prise de note.pdf]]"]
maj: 2026-11-08
---

**Définition** (d'après [[4 - C++]]) : une **classe** est un modèle (un plan) qui décrit des données et des comportements. Un **objet** est une instance concrète de ce modèle. Analogie du cours : `class Voiture` est le plan de fabrication (marque, couleur, rouler…) ; `voiture1` et `voiture2` sont deux voitures réelles, chacune avec ses propres valeurs.

```cpp
class Voiture {
public:
    std::string marque;
};

Voiture voiture1;
Voiture voiture2;
voiture1.marque = "Peugeot";
```

- Une classe ressemble à une `struct` du C : elle permet de créer un type de variable ([[4 - Prise de note]] ; voir [[Structure (struct)]]). Elle contient en plus des **fonctions membres** (méthodes) et des droits d'accès `public` / `private` (voir [[Encapsulation (programmation)]]).
- On accède à un attribut ou à une méthode par le point : `voiture1.marque`, `p1.affiche()`.
- **Déclarer dans la classe, définir dehors** : la méthode est déclarée dans la classe (`void affiche();`), puis définie hors de la classe avec le préfixe `Point::`, qui signifie « s'applique à la classe `Point` » (la « portée », selon [[4 - Prise de note]]).

```cpp
void Point::affiche() {
    std::cout << "x: " << x << std::endl;
    std::cout << "y: " << y << std::endl;
}
```

À la création d'un objet, un [[Constructeur (programmation)|constructeur]] est appelé automatiquement.

Notion parente : [[Programmation orientée objet]]. Voir aussi : [[Langage C++]], [[Accesseur et mutateur]], [[Surcharge d'opérateurs]], [[Méthode spéciale Python]].

Résumés : [[4 - C++]], [[4 - Prise de note]]
