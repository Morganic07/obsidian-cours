---
type: matiere
tags:
  - year2
sources:
  - "[[1 - récursivité et complexité (résumé)|Chp1 - récursivité et complexité]]"
  - "[[2 - piles listes file (résumé)|chp2 - piles listes file]]"
  - "[[AVL momo (résumé)|AVL momo]]"
  - "[[qui dit quoi AVL (résumé)|qui dit quoi AVL]]"
  - "[[TD_Algo (résumé)|TD_Algo]]"
maj: 2026-11-06
---

Algorithmique et programmation en Python : récursivité, complexité, structures de données linéaires, puis arbres AVL. Les 5 notes sont intégrées. Il y a deux chapitres de cours et trois notes de DM ou de TD.

## Parcours

| Note | Sujet | Résumé |
|---|---|---|
| [[1 - récursivité et complexité (résumé)\|Chp1 - récursivité et complexité]] | Récursivité, pile de récursion, complexité, dichotomie | [[1 - récursivité et complexité (résumé)\|Résumé]] |
| [[2 - piles listes file (résumé)\|chp2 - piles listes file]] | Listes, piles, files | [[2 - piles listes file (résumé)\|Résumé]] |
| [[AVL momo (résumé)\|AVL momo]] | Notes sur l'exposé AVL : hauteur, rotations, code, complexité | [[AVL momo (résumé)\|Résumé]] |
| [[qui dit quoi AVL (résumé)\|qui dit quoi AVL]] | Scénario parlé de l'exposé AVL | [[qui dit quoi AVL (résumé)\|Résumé]] |
| [[TD_Algo (résumé)\|TD_Algo]] | Motifs de `#` en Python | [[TD_Algo (résumé)\|Résumé]] |

## Documents PDF

Cinq PDF complètent les notes : trois chapitres de cours sur les arbres (ils font suite aux chapitres 1 et 2 ; les « chapitres 3 à 5 » de l'enseignante), un sujet de projet et une fiche de cours sur l'AVL.

| Document | Contenu | Résumé |
|---|---|---|
| Chapitre3-Arbres ([[Raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf\|Chapitre3-Arbres.pdf]]) | Rappel sur les graphes, définition et vocabulaire des arbres | [[3 - Arbres (résumé)\|Résumé]] |
| Chapitre4-Preing2ID ([[Raw/Year 2/Algo/Cours/Chapitre4-Preing2ID.pdf\|Chapitre4-Preing2ID.pdf]]) | Arbres binaires : propriétés, parcours, code Python | [[4 - Arbres binaires (résumé)\|Résumé]] |
| Chapitre5-ABR ([[Raw/Year 2/Algo/Cours/Chapitre5-ABR.pdf\|Chapitre5-ABR.pdf]]) | Arbres binaires de recherche : insertion, recherche, suppression | [[5 - ABR (résumé)\|Résumé]] |
| Projet-Arbre-AVL-ID2 ([[Raw/Year 2/Algo/DM/Projet-Arbre-AVL-ID2.pdf\|Projet-Arbre-AVL-ID2.pdf]]) | Sujet du projet sur les arbres AVL | [[Projet-Arbre-AVL-ID2 (résumé)\|Résumé]] |
| ARBRE AVL ([[Raw/Year 2/Algo/DM/ARBRE AVL.pdf\|ARBRE AVL.pdf]]) | Fiche AVL : rotations, insertion, suppression, pseudo-code | [[6 - AVL (résumé)\|Résumé]] |

## Concepts

- **Récursivité** : [[Récursivité]], [[Récurrence]], [[Factorielle]], [[Pile d'exécution]], [[Diviser pour régner]]
- **Complexité** : [[Complexité algorithmique]], [[Calcul de complexité et théorème de résolution]], [[Classe de complexité]], [[Recherche dichotomique]], [[Partie entière]]
- **Structures de données linéaires** : [[Liste chaînée]], [[Pile et file]]
- **Rappels sur les graphes** : [[Graphe non orienté]], [[Graphe orienté]], [[Chemin (graphe)]], [[Cycle (graphe)]], [[Circuit (graphe)]], [[Sous-graphe]]
- **Arbres** : [[Arbre (théorie des graphes)]], [[Arborescence (graphe)]], [[Vocabulaire des arbres]], [[Hauteur d'un arbre]], [[Arbre m-aire]], [[B-arbre]], [[Arbre binaire]], [[Arbre binaire de recherche]], [[Méthode spéciale Python]], [[Arbre AVL]]

## À revoir en priorité avant un examen

- [[AVL momo (résumé)]] : la complexité de `rebalance` (annoncée $O(\log n)$) est en réalité $O(n)$ avec le code donné, car `hauteur` est recalculée à chaque appel ; elle contredit l'autre note ($O(1)$).
- [[qui dit quoi AVL (résumé)]] : la « hauteur d'un nœud » est définie comme le nombre de branches jusqu'à la racine, ce qui est la profondeur.
- [[AVL momo (résumé)]] et [[qui dit quoi AVL (résumé)]] : la convention de hauteur du vide ($-1$) ne correspond pas au code (0).
- [[1 - récursivité et complexité (résumé)]] : la dernière ligne de la substitution oublie que la base est $T(0)$.

## Liens avec les autres matières

- **[[Analyse (index)]]** : la notation $O$ rejoint la [[Comparaison asymptotique]] des fonctions et des suites.
- **C++** (Year 4) : la [[Liste chaînée]] est reprise avec des pointeurs dans [[3 - pointeurs , tableaux, listes chainées, structures (résumé)|le chapitre 3 de C++]]. La pile d'exécution est celle de la gestion mémoire en [[1 - basiques (résumé)|C++ chapitre 1]].
- **Graph theory** (Year 4) : le cours de théorie des graphes a sa propre page de [[Complexité algorithmique]]. Les rappels du chapitre 3 ([[Graphe non orienté]], [[Graphe orienté]], [[Chemin (graphe)]], [[Cycle (graphe)]], [[Sous-graphe]], [[Arbre (théorie des graphes)]]) y sont repris en détail : [[Graph theory (index)]].
- **[[Cours/Informatique (cours)/Algo (cours) 1/Algo (index)]]** : [[Récursivité]], [[Récurrence]] et [[Factorielle]] y sont introduites ; la [[Récurrence]] l'est aussi en [[Outil Maths (index)]].
