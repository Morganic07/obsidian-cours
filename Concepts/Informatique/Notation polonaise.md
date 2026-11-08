---
type: concept
tags: [year2]
aliases: [notation polonaise inverse, NPI, RPN, reverse Polish notation, Polish notation, notation préfixe, notation postfixe, notation infixe, arbre d'expression, expression tree]
matieres: [Algo]
sources: ["[[Raw/Year 2/Algo/Cours/Chapitre5-ABR.pdf|Chapitre5-ABR.pdf]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : la **notation polonaise** (ou préfixe), due au logicien polonais Jan Łukasiewicz, écrit une expression arithmétique en plaçant l'opérateur **avant** ses opérandes : $(3 + 4) \times 2$ s'écrit `* + 3 4 2`. La **notation polonaise inverse** (NPI, *RPN*, ou postfixe) place l'opérateur **après** ses opérandes : `3 4 + 2 *`. Ni l'une ni l'autre n'a besoin de parenthèses ni de règles de priorité : chaque opérateur ayant un nombre fixe d'opérandes, l'expression se lit d'une seule façon.

## Lien avec l'arbre d'expression

Une expression se représente par un **arbre d'expression** : les feuilles sont les nombres, les nœuds internes les opérateurs, chaque opérateur ayant ses opérandes pour sous-arbres. Ses trois parcours en profondeur donnent les trois écritures :

| Parcours | Écriture | Parenthèses nécessaires |
|---|---|---|
| préfixe (nœud, gauche, droite) | notation polonaise | non |
| infixe (gauche, nœud, droite) | écriture usuelle | oui |
| postfixe (gauche, droite, nœud) | notation polonaise inverse | non |

## Évaluation avec une pile

La NPI s'évalue de gauche à droite avec une [[Pile et file|pile]] :
1. un nombre : on l'empile ;
2. un opérateur : on dépile deux valeurs (la seconde dépilée est l'opérande de gauche), on calcule, on empile le résultat ;
3. à la fin, la pile contient une seule valeur : le résultat.

Exemple de l'exercice 1 de [[5 - ABR]], `3 4 2 / + 8 2 3 * - *` :

| Lu | Pile après |
|---|---|
| 3, 4, 2 | 3 4 2 |
| `/` | 3 2 |
| `+` | 5 |
| 8, 2, 3 | 5 8 2 3 |
| `*` | 5 8 6 |
| `-` | 5 2 |
| `*` | 10 |

Résultat : $(3 + 4/2) \times (8 - 2 \times 3) = 5 \times 2 = 10$.

La notation préfixe s'évalue de même en lisant l'expression de droite à gauche.

## Usages

Calculatrices Hewlett-Packard (saisie en NPI), langages à pile comme PostScript et Forth, et bytecode de machines virtuelles à pile, comme la JVM : un compilateur traduit souvent les expressions en forme postfixe.

## Dans le cours

Le cours ne nomme pas ces notations. L'exercice 1 de [[5 - ABR]] demande d'afficher un arbre d'expression en préfixe, infixe et postfixe sans parenthèses ; ses compléments relient ces écritures à la notation polonaise.

Voir aussi : [[Pile et file]], [[Arbre binaire]], [[Parcours en profondeur]], [[Compilation et bytecode]], [[Récursivité]].

Résumés : [[5 - ABR]]
