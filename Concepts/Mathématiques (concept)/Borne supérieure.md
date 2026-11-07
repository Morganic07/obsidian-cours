---
type: concept
tags: [year1]
aliases: [borne supérieure, borne inférieure, bornes supérieure et inférieure, propriété de la borne supérieure, supremum, infimum, least upper bound]
matieres: [Analyse Maths, Outil Maths]
sources: ["[[Raw/Year 1/Analyse Maths/Cours/Chap1-reels.pdf|Chap1-reels.pdf]]", "[[Raw/Year 1/Analyse Maths/Exos/TD1-numbres-reels.pdf|TD1-numbres-reels.pdf]]", "[[Raw/Year 1/Analyse Maths/Exos/td1slides.pdf|td1slides.pdf]]", "[[Raw/Year 1/Analyse Maths/contrôles/DS1-Analyse-2022-corrigé.pdf|DS1-Analyse-2022-corrigé.pdf]]", "[[3 - Relation binaire (résumé)|Chapitre 3 - Relation binaire]]", "[[Raw/Year 1/Outil Maths/Cours/pdf du prof/Chapitre3-Relation binaire.pdf|Chapitre3-Relation binaire.pdf]]"]
maj: 2026-11-06
---

Pour une partie $A$ de $\mathbb{R}$, la **borne supérieure** $\sup A$ est, si elle existe, le plus petit des majorants de $A$. La **borne inférieure** $\inf A$ est le plus grand des minorants. Voir [[Relation d'ordre]] pour le cadre général.

## Propriété fondamentale de $\mathbb{R}$

Toute partie non vide majorée de $\mathbb{R}$ a une borne supérieure, et toute partie non vide minorée a une borne inférieure. Cette propriété distingue $\mathbb{R}$ de $\mathbb{Q}$. Le cours en déduit les grands théorèmes d'analyse : limite monotone, suites adjacentes, valeurs intermédiaires, bornes atteintes, Rolle et accroissements finis, construction de l'[[Intégrale]].

## Différence avec le maximum

- Le $\sup$ n'appartient pas forcément à $A$. Pour $[0, 1[$, $\sup = 1$ mais il n'y a pas de plus grand élément.
- Si $A$ a un plus grand élément, alors $\sup A = \max A$.
- Un $\sup$, quand il existe, est unique.

## Caractérisations de $s = \sup A$

1. $s$ majore $A$, et pour tout $y < s$ il existe $x \in A$ avec $y < x$.
2. $s$ majore $A$, et il existe une suite d'éléments de $A$ qui converge vers $s$.

Pour prouver un $\sup$ dans un exercice : vérifier que $s$ est un majorant, puis qu'aucun réel plus petit n'en est un (ou approcher $s$ par une suite de $A$). L'inf non atteint de $\{(-1)^n/n + 2/n\}$ se montre ainsi : $0$ minore l'ensemble et une suite de ses éléments tend vers $0$.

## Résultats classiques (TD)

- $\sup(-A) = -\inf A$ ; $\sup(x + A) = x + \sup A$ ; $\sup(A + B) = \sup A + \sup B$.
- $\sup(A \cup B) = \max(\sup A, \sup B)$ ; $\sup(A \cap B) \le \min(\sup A, \sup B)$.
- $\sup(A \cdot B) = \sup A \cdot \sup B$ est faux en général : il faut des ensembles de positifs.
- Si $x \le y$ pour tout $x \in A$ et $y \in B$, alors $\sup A \le \inf B$.
- Une suite croissante majorée converge vers $\sup\{u_n\}$ : voir [[Suite numérique]].
- $\inf \sqrt A = \sqrt{\inf A}$.

## Dans un ensemble ordonné quelconque (Outil Maths)

Pour un ordre $\preceq$, $\sup(A)$ est le plus petit des majorants : $\forall y \in A,\ y \preceq \sup(A)$, et $\sup(A) \preceq z$ pour tout majorant $z$. Symétriquement, $\inf(A)$ est le plus grand des minorants. Exemple : $]1, +\infty[$ a pour borne inférieure 1 et pas de borne supérieure dans $(\mathbb{R}, \leq)$.

Notion parente : [[Relation d'ordre]]. Voir aussi : [[Majorant et minorant]], [[Plus grand élément]], [[Ensembles de nombres]], [[Théorème des valeurs intermédiaires]].

## À vérifier

DS1 2022 ex. 6 : coquilles de l'énoncé ($x \in A$ au lieu de $a \in A$, $\sup(A+B)$ au lieu de $\sup(A+x)$).

Résumés : [[1 - Ensemble des Reels (résumé)]], [[0 - rappels pdf (résumé)]], [[3 - Relation binaire (résumé)]], [[3 - pdf (résumé)]].
