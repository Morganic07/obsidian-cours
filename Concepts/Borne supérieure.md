---
type: concept
aliases: [borne supérieure, borne inférieure, bornes supérieure et inférieure, propriété de la borne supérieure, supremum, infimum, least upper bound]
matieres: [Analyse Maths]
sources: ["[[raw/Year 1/Analyse Maths/Cours/Chap1-reels.pdf|Chap1-reels]]", "[[raw/Year 1/Analyse Maths/Exos/TD1-numbres-reels.pdf|TD1-numbres-reels]]"]
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

Résumés : [[Chap1-reels (résumé)]], [[TD1-numbres-reels (résumé)]], [[DS1-Analyse-2022-corrigé (résumé)]].
