---
type: concept
tags: [year4]
aliases: [opérateurs bit à bit, bitwise operator, bitwise operators, opérateur de décalage, décalage de bits, masque de bits]
sources: ["[[Raw/Year 4/C／C++/programmes C/tp2/2.8.c|2.8.c]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : en [[Langage C|C]] et en [[Langage C++|C++]], les opérateurs bit à bit agissent sur chaque [[Bit|bit]] de la représentation binaire d'un entier ([[Numération binaire]]), indépendamment des autres :

| Opérateur | Nom | Exemple (sur 4 bits) |
|---|---|---|
| `&` | ET bit à bit | `0110 & 0011` = `0010` (6 & 3 = 2) |
| `\|` | OU bit à bit | `0110 \| 0011` = `0111` (6 \| 3 = 7) |
| `^` | OU exclusif ([[Ou exclusif\|XOR]]) | `0110 ^ 0011` = `0101` (6 ^ 3 = 5) |
| `~` | NON (complément) | `~0110` = `1001` |
| `<<` | décalage à gauche | `0011 << 2` = `1100` (3 << 2 = 12) |
| `>>` | décalage à droite | `1100 >> 2` = `0011` (12 >> 2 = 3) |

Il ne faut pas les confondre avec les [[Opérateur logique|opérateurs logiques]] `&&`, `||`, `!`, qui travaillent sur des valeurs vrai/faux et pratiquent l'[[Évaluation en court-circuit|évaluation en court-circuit]] : `6 & 3` vaut 2, `6 && 3` vaut 1. Le C n'a pas d'opérateur de puissance : `2 ^ 3` vaut 1, pas 8 ([[Exponentiation]]).

Usages courants :

- `n & 1` donne le bit de poids faible, donc la [[Parité d'un entier|parité]] : `(n & 1) == 0` pour un nombre pair ;
- `1 << k` vaut $2^k$, et `x << k` multiplie par $2^k$ (`x >> k` divise par $2^k$ pour un non-signé) ;
- **masques** : `x | (1 << k)` met le bit $k$ à 1, `x & ~(1 << k)` le met à 0, `x & (1 << k)` le teste ; c'est ainsi qu'on range plusieurs options ([[Drapeau (programmation)|drapeaux]]) dans un seul entier, comme les [[Permissions Unix|permissions Unix]] (`0755`) ;
- l'échange de deux variables sans variable temporaire par `a ^= b; b ^= a; a ^= b;`, curiosité moins lisible et pas plus rapide sur un processeur moderne ([[Échange de deux variables]]).

Pièges : les opérateurs `&`, `^`, `|` sont **moins prioritaires** que `==`, si bien que `n & 1 == 0` se lit `n & (1 == 0)` ; il faut écrire `(n & 1) == 0` ([[Associativité et ordre d'évaluation]]). Décaler d'un nombre de positions négatif ou supérieur ou égal à la largeur du type, ou décaler à gauche un entier signé négatif, est un [[Comportement indéfini|comportement indéfini]] ; décaler à droite un négatif dépend de l'implémentation ([[Complément à deux]]). On réserve donc ces opérateurs aux types non signés (`unsigned`).

## Dans le cours

- [[2 - structures code]] : la section 1 présente les opérateurs bit à bit à côté des opérateurs logiques (`6 & 3` vaut 2, `6 && 3` vaut 1).
- [[tp2]] : complément au programme 2.8, échange de deux variables par le OU exclusif bit à bit.
- [[tp3]] : complément au programme 3.9, test de parité `(nombre & 1) == 0`.

Voir aussi : [[Ou exclusif]], [[Numération binaire]], [[Notation hexadécimale]], [[Opérateur unaire et opérateur binaire]].
