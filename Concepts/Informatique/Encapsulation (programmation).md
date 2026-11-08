---
type: concept
tags: [year4]
aliases: [encapsulation, données privées, données publiques, public et private, modificateur d'accès, access modifier]
matieres: [C++]
sources: ["[[Raw/Year 4/C++/chp4 C++.pdf|chp4 C++.pdf]]", "[[Raw/Year 4/C++/chp4 prise de note.pdf|chp4 prise de note.pdf]]"]
maj: 2026-11-08
---

**Définition** (d'après [[4 - C++]]) : dans une classe, chaque donnée est soit **publique**, soit **privée** :

| Mot-clé | Accès |
|---|---|
| `public` | accessible depuis l'extérieur de la classe : n'importe quel code peut lire ou modifier la donnée directement |
| `private` | accessible uniquement depuis l'intérieur de la classe : protège la donnée contre un accès ou une modification incontrôlés |

```cpp
class CompteBancaire {
public:
    std::string titulaire;
private:
    double solde;
};

CompteBancaire c;
c.titulaire = "Alice";   // OK — donnée publique
c.solde = 1000;          // Erreur : solde est privé !
```

Pour lire ou modifier une donnée privée, on passe par des méthodes publiques, l'[[Accesseur et mutateur|accesseur et le mutateur]] (get / set), qui peuvent vérifier la validité de la valeur. Une fonction extérieure à la classe peut recevoir le droit d'accéder aux membres privés si la classe la déclare [[Fonction amie (friend)|amie]].

Le cours lui-même laisse passer un accès interdit : voir l'erreur `std::cout << p3.x;` signalée dans [[4 - C++]].

Notion parente : [[Programmation orientée objet]]. À ne pas confondre avec [[Encapsulation 802.1Q]] (réseaux). Voir aussi : [[Classe et objet]].

Résumés : [[4 - C++]], [[4 - Prise de note]]
