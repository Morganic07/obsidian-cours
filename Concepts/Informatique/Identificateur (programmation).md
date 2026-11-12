---
type: concept
tags: [year4]
aliases: [identifier, identifiant (programmation), identificateurs (programmation)]
sources: ["[[Raw/Year 4/C／C++/programmes C++/formation/4-Classe.cpp|4-Classe.cpp]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : un identificateur est le nom que le programmeur donne à une entité du programme : [[Variable (programmation)|variable]], fonction, [[Classe et objet|classe]], type, [[Constante (programmation)|constante]], [[Espace de noms (namespace)|espace de noms]]. Le compilateur s'en sert pour relier chaque usage d'un nom à sa [[Déclaration et définition|déclaration]], selon les règles de [[Portée d'une variable|portée]].

Règles en [[Langage C|C]] et en [[Langage C++|C++]] :

- il commence par une lettre ou un `_`, puis contient des lettres, des chiffres ou des `_` : `total2`, `_compteur`, `estAllumee` sont valides, `2total` ou `mon-nom` ne le sont pas ;
- il distingue majuscules et minuscules : `Total` et `total` sont deux noms différents ([[Sensibilité à la casse]]) ;
- il ne peut pas être un [[Mot réservé|mot réservé]] (`int`, `return`, `class`…) ;
- les noms qui commencent par `_` suivi d'une majuscule ou d'un second `_` sont réservés à l'implémentation (compilateur et bibliothèque standard), et en C++ tout nom qui contient `__` : on les évite.

Les deux langages admettent aussi des lettres [[Unicode]] (`allumée`, `π`) ; [[GCC]] les accepte écrites directement en UTF-8 depuis sa version 10. Les [[Règle de codage|règles de codage]] les déconseillent pourtant : certains outils, polices ou claviers les gèrent mal, et un même caractère accentué peut s'encoder de deux façons (é précomposé ou e suivi d'un accent combinant), ce qui donne deux identificateurs différents d'apparence identique.

Au-delà de la syntaxe, un bon identificateur dit ce que la donnée représente (`nbEtudiants` plutôt que `n2`) et suit une convention constante dans le projet : [[Casse chameau|casse chameau]] (`volumeCube`), *snake case* (`volume_cube`), majuscules pour les [[Macro (préprocesseur)|macros]] (`TAILLE_MAX`). Un nom bien choisi remplace souvent un [[Commentaire (programmation)|commentaire]] ([[Maintenabilité]]). Deux entités de même nom dans des portées emboîtées créent un [[Masquage de nom|masquage de nom]].

## Dans le cours

- [[formation C++]] : les attributs `allumée` et `estAllumée` de la classe `Television` (programme 4) contiennent un `é` ; le C++ l'accepte, mais la fiche conseille de s'en tenir à l'ASCII.
- [[1 - basiques]] : la liste des mots réservés du C, interdits comme identificateurs.

Voir aussi : [[Variable (programmation)]], [[Mot réservé]], [[Casse chameau]], [[Règle de codage]].
