---
type: concept
tags: [year4]
aliases: [accesseur, mutateur, getter, setter, get et set, getteur, setteur]
sources: ["[[Raw/Year 4/C／C++/chp4 C++.pdf|chp4 C++.pdf]]", "[[Raw/Year 4/C／C++/chp4 prise de note.pdf|chp4 prise de note.pdf]]"]
maj: 2026-11-12
---

**Définition** (d'après [[4 - C++]]) : une donnée privée n'étant pas accessible directement (voir [[Encapsulation (programmation)]]), on définit des méthodes publiques dédiées : l'**accesseur** (*get*) pour la lire, et le **mutateur** (*set*) pour la modifier.

```cpp
class CompteBancaire {
private:
    double solde;
public:
    double getSolde() {          // renvoie la valeur, sans la modifier
        return solde;
    }
    void setSolde(double s) {    // met à jour, en pouvant vérifier la valeur
        solde = s;
    }
};
```

- Le mutateur peut **vérifier que la valeur est valide** avant de l'affecter. Exercice de [[4 - Prise de note]] : un `setrayon` qui refuse un rayon négatif (sans correction).
- Exemple de la classe `Personne` : on ne passe que par `setNom`, `setAge` et `getAge`, jamais directement par les attributs ; le cours précise que l'exemple est incomplet, faute de constructeurs.
- La prise de note les appelle « getteur » et « setteur », et les applique à `Cercle` (`getX()`, `setX(int w)`).

Notion parente : [[Classe et objet]]. Voir aussi : [[Programmation orientée objet]].

## Dans le cours

- [[formation C++]] : `setVolume` / `getVolume` de `Television` (programmes 4 et 8), `setNom`, `getNom`, `setAge`, `getAge` de `Personne` (programme 9) ; dans le programme 4, `getVolume` et `getCanal` étaient déclarés `void`, alors qu'un accesseur renvoie la valeur (corrigé en `int`).
- [[exo-prof]] : `getX`, `getY` et le mutateur `set` de `Point`, `getA`, `getB` et `getLongueur` de `Segment` ; `getLongueur` recalcule et modifie l'attribut `longueur` ([[Effet de bord|effet de bord]]), et seul `classeSegment.cpp` déclare ses accesseurs [[Méthode constante|`const`]].
- [[compilation séparée (C++)]] : les mêmes accesseurs et le mutateur, déclarés dans `Point.h` et `Segment.h`.

Résumés : [[4 - C++]], [[4 - Prise de note]]
