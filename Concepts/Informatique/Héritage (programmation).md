---
type: concept
tags: [year4]
aliases: [héritage, inheritance, classe dérivée, classe fille, classe de base, classe mère, protected, méthode virtuelle, virtual]
matieres: [C++]
sources: ["[[Raw/Year 4/C++/chp4 C++.pdf|chp4 C++.pdf]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : l'héritage permet de définir une classe **dérivée** (ou fille) à partir d'une classe **de base** (ou mère). La classe dérivée reçoit les attributs et les méthodes de la classe de base, peut en ajouter, et peut redéfinir certaines méthodes. Il exprime une relation **« est un »** : un `Cercle` est une `Forme`.

```cpp
class Forme {
protected:
    int x, y;
public:
    Forme(int a, int b) : x(a), y(b) {}
    virtual void affiche() const { std::cout << "Forme" << std::endl; }
    virtual ~Forme() {}
};

class Cercle : public Forme {
    int rayon;
public:
    Cercle(int a, int b, int r) : Forme(a, b), rayon(r) {}
    void affiche() const override { std::cout << "Cercle de rayon " << rayon << std::endl; }
};
```

- **Droits d'accès** : les membres `private` de la base restent inaccessibles à la classe dérivée ; les membres `protected` lui sont accessibles mais restent cachés à l'extérieur ; les membres `public` restent publics avec `class Cercle : public Forme`.
- **Constructeurs** : le constructeur de la classe dérivée appelle d'abord celui de la base, dans sa liste d'initialisation (`Cercle(...) : Forme(...) { ... }`). À la destruction, l'ordre est inverse : la partie dérivée d'abord, la base ensuite.
- **Polymorphisme** : avec une méthode `virtual`, un appel sur une référence ou un pointeur vers la base exécute la version de la classe réelle de l'objet. Avec `Forme* f = new Cercle(0, 0, 2);`, `f->affiche()` affiche « Cercle de rayon 2 » ; sans `virtual`, il afficherait « Forme ». `override` (C++11) fait vérifier par le compilateur qu'on redéfinit bien une méthode virtuelle. Une classe de base destinée au polymorphisme a un destructeur `virtual`, pour que `delete f` détruise bien un `Cercle`.
- **Composition** : à ne pas confondre avec l'héritage. La composition exprime une relation **« a un »** : un `Segment` a deux `Point` comme attributs, il n'est pas un `Point`.

## Dans le cours

Nommé seulement dans [[4 - C++]], dans l'énumération « classes, objets, héritage… » des notions de la programmation orientée objet, sans être développé.

Ne pas confondre avec l'[[Héritage en base de données]].

Notion parente : [[Programmation orientée objet]]. Voir aussi : [[Classe et objet]], [[Constructeur (programmation)]], [[Destructeur (programmation)]], [[Encapsulation (programmation)]].

Résumés : [[4 - C++]]
