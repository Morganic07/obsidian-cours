---
type: concept
tags: [year1, year2]
aliases: [fonction partie entière, partie fractionnaire, floor, ceil]
matieres: [Analyse Maths, Algo, Analyse]
sources: ["[[Raw/Year 1/Analyse Maths/Cours/Chap1-reels.pdf|Chap1-reels.pdf]]", "[[Raw/Year 1/Analyse Maths/Exos/TD1-numbres-reels.pdf|TD1-numbres-reels.pdf]]", "[[Raw/Year 1/Analyse Maths/Exos/td1slides.pdf|td1slides.pdf]]", "[[Raw/Year 1/Analyse Maths/contrôles/DS1-Analyse-2022-corrigé.pdf|DS1-Analyse-2022-corrigé.pdf]]", "[[Raw/Year 2/Algo/DM/TD_Algo.docx|TD_Algo]]", "[[Raw/Year 2/Analyse/chp7/TD7-integration (1).pdf|TD7-integration (1).pdf]]"]
maj: 2026-11-06
---

$E(x)$ est l'unique entier tel que $E(x) \le x < E(x) + 1$, soit $E(x) = \max\{n \in \mathbb{Z} : n \le x\}$ ; par exemple $E(-3{,}5) = -4$.

**Analyse Maths (TD et DS)** : $E$ est croissante, $E(x) + E(y) \le E(x+y) \le E(x) + E(y) + 1$, $E(-x) = -E(x) - 1$ si $x \notin \mathbb{Z}$, $E(2x)$ s'exprime selon la partie fractionnaire ; on résout les équations en raisonnant sur l'entier $E(x)$. Elle est continue à droite mais pas à gauche aux entiers.

**Algo** : TD_Algo utilise `ceil` et `floor` du module `math` pour la moitié de `n`. **Analyse (Year 2)** : le TD7 fait intégrer des fonctions avec la partie entière $E$, en découpant en intervalles où elle est constante. Aucun de ces deux cours ne la définit.

Notion parente : [[Propriété d'Archimède]]. Voir aussi : [[Approximation décimale]], [[Identité d'Hermite]], [[Limite et continuité]], [[Intégrale]].

## À vérifier

- Erreur du corrigé (td1slides ex. 19 et DS1 2021 ex. 2) : $(2E(x)+1)^2 < 4$ a pour solution $[-1, 1[$, pas $]-1, 1[$.

Résumés : [[1 - Ensemble des Reels (résumé)]], [[0 - rappels pdf (résumé)]]
