---
type: concept
tags: [year4]
aliases: [interface (programmation), implémentation, implementation, séparation interface implémentation]
matieres: [C++]
sources: ["[[Raw/Year 4/C++/chp5 compilation séparée .pdf|chp5 compilation séparée .pdf]]"]
maj: 2026-11-11
---

**Définition** (d'après [[5 - Compilation séparée]]) : le [[Fichier d'en-tête|fichier d'en-tête]] `.h` est l'**interface**, ce que les autres fichiers ont besoin de connaître (classes, attributs, prototypes des méthodes) ; le [[Fichier source|fichier source]] `.cpp` est l'**implémentation**, le code des méthodes.

## Compléments (hors du cours)

- L'interface dit **ce que** fait un module, l'implémentation **comment** il le fait. Le code qui utilise un module ne doit dépendre que de son interface : on peut alors changer l'implémentation (un algorithme plus rapide, une autre représentation des données) sans toucher aux utilisateurs, à condition de garder les mêmes [[Déclaration et définition|déclarations]].
- C'est le principe commun à la [[Programmation modulaire|programmation modulaire]] et à l'[[Encapsulation (programmation)|encapsulation]] : les attributs privés et les [[Accesseur et mutateur|accesseurs]] cachent l'implémentation derrière une interface publique.
- En C++, la séparation n'est pas complète : les attributs privés figurent dans le `.h`, si bien que les modifier oblige à recompiler tous les fichiers qui l'incluent.
- En Java, le mot `interface` désigne en plus un type sans implémentation qu'une classe s'engage à respecter ; la notion est voisine.

Voir aussi : [[Compilation séparée]], [[Classe et objet]].

Résumés : [[5 - Compilation séparée]]
