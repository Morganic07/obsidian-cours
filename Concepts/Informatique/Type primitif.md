---
type: concept
tags: [year1, year3, year4]
aliases: [Type de base, types de base, types primitifs, basic datatypes, primitive type, primitive types, type objet, types objets, unsigned char, long double, type void]
matieres: [Algo Maths, Java, C++]
sources: ["[[raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1]]", "[[Chp1 - Intro Java]]", "[[Chp1 - basiques]]"]
maj: 2026-11-06
---

Types élémentaires fournis par le langage, par opposition aux types structurés ou objets. Le type fixe la place réservée en mémoire et la façon d'interpréter les bits.

**Pseudo-code et Python** (Algo Maths) : `ENTIER` (opérateurs `+ - * DIV MOD`), `REEL`, `BOOLEEN` (`ET OU NON`), `CARACTERE`, `CHAINE` (concaténation `&`). Python : entiers, flottants, chaînes, booléens ; `type(x)` et `isinstance(x, float)`. L'examen de novembre 2022 oppose type structuré et type primitif.

**Java** : `byte` 8 bits, `short` 16, `int` 32, `long` 64, `float` 32, `double` 64, `char` 16 (Unicode), `boolean`. À côté, les types objets (classes, interfaces) et `void`. Hiérarchie des numériques de `double` à `int`, puis `short`, `char`, `byte`.

**C** (C++) : `void` (type vide, pour les fonctions sans argument ou sans retour), `int` (qualificatifs `short`, `long`, `signed` par défaut, `unsigned`), `char` (support du [[Code ASCII]], aussi entier sur 8 bits), `float`, `double` et `long double` (précision croissante). `char` occupe 1 octet, `int` en général 4, `double` en général 8. En C, `char` est un entier : `c = 65` et `c = 'A'` sont identiques.

Notion parente : [[Pseudo-code]]. Voir aussi : [[Chaîne de caractères]], [[Nombre à virgule flottante]], [[Structure (struct)]], [[Typage dynamique]], [[Typage statique]], [[Transtypage]], [[Variable (programmation)]], [[Complément à deux]], [[Norme IEEE 754]].

## À vérifier

- Java : « boolean 1 bit » est une simplification.
- C : le cours dit que `char` peut être signé (`char`) ou non (`unsigned char`) ; le signe d'un `char` seul dépend de l'implémentation (complément du résumé).
- C : Chp3 écrit qu'un entier fait 8 octets sur système 64 bits, ce qui contredit Chp1 (« généralement 4 octets »).

Résumés : [[AlgoID1 (résumé)]], [[Contrôles (résumé)]], [[Chp1 - Intro Java (résumé)]], [[Chp1 - basiques (résumé)]]
