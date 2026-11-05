---
type: matiere
sources: ["[[Chp1 - récursivité et complexité]]", "[[chp2 - piles listes file]]", "[[AVL momo]]", "[[qui dit quoi AVL]]", "[[TD_Algo]]"]
maj: 2026-11-05
---

Algorithmique et programmation en Python : récursivité, complexité, structures de données linéaires, puis arbres AVL. Les 5 notes sont intégrées. Il y a deux chapitres de cours et trois notes de DM ou de TD.

## Parcours

| Note | Sujet | Résumé |
|---|---|---|
| [[Chp1 - récursivité et complexité]] | Récursivité, pile de récursion, complexité, dichotomie | [[Chp1 - récursivité et complexité (résumé)\|Résumé]] |
| [[chp2 - piles listes file]] | Listes, piles, files | [[chp2 - piles listes file (résumé)\|Résumé]] |
| [[AVL momo]] | Notes sur l'exposé AVL : hauteur, rotations, code, complexité | [[AVL momo (résumé)\|Résumé]] |
| [[qui dit quoi AVL]] | Scénario parlé de l'exposé AVL | [[qui dit quoi AVL (résumé)\|Résumé]] |
| [[TD_Algo]] | Motifs de `#` en Python | [[TD_Algo (résumé)\|Résumé]] |

## Concepts

- **Récursivité et coût** : [[Récursivité]], [[Calcul de complexité et théorème de résolution]], [[Recherche dichotomique]]
- **Structures de données** : [[Pile et file]], [[Liste chaînée]], [[Arbre AVL]]

## À revoir en priorité avant un examen

- [[AVL momo (résumé)]] : la complexité de `rebalance` (annoncée $O(\log n)$) est en réalité $O(n)$ avec le code donné, car `hauteur` est recalculée à chaque appel ; elle contredit l'autre note ($O(1)$).
- [[qui dit quoi AVL (résumé)]] : la « hauteur d'un nœud » est définie comme le nombre de branches jusqu'à la racine, ce qui est la profondeur.
- [[AVL momo (résumé)]] et [[qui dit quoi AVL (résumé)]] : la convention de hauteur du vide ($-1$) ne correspond pas au code (0).
- [[Chp1 - récursivité et complexité (résumé)]] : la dernière ligne de la substitution oublie que la base est $T(0)$.

## Liens avec les autres matières

- **[[Year 2 - Analyse]]** : la notation $O$ rejoint la [[Comparaison asymptotique]] des fonctions et des suites.
- **C++** (Year 4) : la [[Liste chaînée]] est reprise avec des pointeurs dans [[Chp3 - pointeurs , tableaux, listes chainées, structures (résumé)|le chapitre 3 de C++]]. La pile d'exécution est celle de la gestion mémoire en [[Chp1 - basiques (résumé)|C++ chapitre 1]].
- **Graph theory** (Year 4) : le cours de théorie des graphes a sa propre page de [[Complexité algorithmique]].
