---
type: concept
tags: [year4]
aliases: [class invariant, invariant d'objet, invariants de classe]
sources: ["[[Raw/Year 4/C／C++/programmes C++/exo-prof/classeSegment.cpp|classeSegment.cpp]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : un invariant de classe est une propriété des attributs d'un objet qui doit être vraie pendant toute sa vie observable : juste après sa construction, puis avant et après chaque appel d'une méthode publique. Exemples : « la `longueur` d'un `Segment` est la distance de `A` à `B` », « le dénominateur d'une fraction n'est jamais nul », « `taille` est le nombre d'éléments réellement rangés ».

Répartition des rôles :

- le [[Constructeur (programmation)|constructeur]] **établit** l'invariant (il refuse ou corrige des valeurs qui le violeraient) ;
- chaque méthode publique le **préserve** : elle peut le rompre temporairement pendant son exécution, mais doit le rétablir avant de rendre la main ;
- l'[[Encapsulation (programmation)|encapsulation]] le **protège** : des attributs `private` ne peuvent être modifiés que par les méthodes de la classe, qui seules ont à garantir l'invariant. Un attribut public peut être changé par n'importe qui, et l'invariant ne peut plus être assuré.

```cpp
class Fraction {
    int num, den;                       // invariant : den != 0
public:
    Fraction(int n, int d) : num(n), den(d) {
        if (d == 0) throw std::invalid_argument("dénominateur nul");
    }
    void setDen(int d) { if (d != 0) den = d; }   // le mutateur le préserve
};
```

Stocker une donnée qu'on peut recalculer à partir des autres (une longueur, une somme) crée un invariant de plus à maintenir : chaque [[Accesseur et mutateur|mutateur]] doit la remettre à jour. Le plus sûr est souvent de la calculer à la demande, dans une [[Méthode constante|méthode constante]].

La notion vient de la **conception par contrat** de Bertrand Meyer et de son langage Eiffel (1986), où les invariants s'écrivent dans le code et sont vérifiés à l'exécution, avec les préconditions et les postconditions des méthodes. C'est l'analogue, pour un objet, de l'[[Invariant de boucle|invariant de boucle]] ; en C++, on peut le vérifier pendant les tests avec `assert`.

## Dans le cours

- [[exo-prof]] : l'attribut `longueur` de `Segment` doit rester égal à la distance de `A` à `B` ; tout futur `setA` ou `setB` devrait le recalculer, et `getLongueur()` le modifie à chaque lecture. La fiche conseille de calculer la longueur à la demande par `float longueur() const`.

Voir aussi : [[Encapsulation (programmation)]], [[Classe et objet]], [[Invariant de boucle]], [[Robustesse (informatique)]].
