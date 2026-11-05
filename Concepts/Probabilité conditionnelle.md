---
type: concept
aliases: [conditional probability, probabilités totales, law of total probability, théorème de Bayes, Bayes' theorem, événements indépendants, independent events, règle de multiplication]
matieres: [Probability, Statistics]
sources: ["[[Chp 2 - Conditional proba and independence]]"]
maj: 2026-11-05
---

Pour $P(B) > 0$, $P(A|B) = P(A \cap B)/P(B)$ : conditionner sur $B$ prend $B$ comme nouvel espace d'échantillonnage.

**Règle de multiplication** : $P(A \cap B) = P(A|B)P(B)$, qui se généralise aux expériences en plusieurs étapes : $P(A_1 \cap A_2 \cap A_3) = P(A_3|A_1 \cap A_2)P(A_2|A_1)P(A_1)$.

**Probabilités totales** : si $A_1, \dots, A_n$ sont exclusifs et exhaustifs, $P(B) = \sum_i P(B|A_i)P(A_i)$.

**Bayes** : sous les mêmes hypothèses, $P(A_j|B) = \dfrac{P(B|A_j)P(A_j)}{\sum_i P(B|A_i)P(A_i)}$.

**Indépendance** : $A$ et $B$ sont indépendants si $P(A|B) = P(A)$, ou de façon équivalente si $P(A \cap B) = P(A)P(B)$. Alors $A^c$ et $B$, $A$ et $B^c$, $A^c$ et $B^c$ le sont aussi. Pour des variables aléatoires, voir [[Loi conjointe]].

Liens : [[Espace probabilisé]]

Résumé : [[Chp 2 - Conditional proba and independence (résumé)]]
