---
type: concept
tags:
  - year2
  - year3
aliases:
  - conditional probability
  - probabilités totales
  - law of total probability
  - théorème de Bayes
  - Bayes' theorem
  - règle de multiplication
  - multiplication rule
matieres:
  - Probability
  - Statistics
sources:
  - "[[2 - Conditional proba and independence|Chp 2 - Conditional proba and independence]]"
  - "[[0 - proba&stats utilitaire|probabilité statistiques utilitaire]]"
maj: 2026-11-07
---

Pour $P(B) > 0$, $P(A|B) = P(A \cap B)/P(B)$ : conditionner sur $B$ prend $B$ comme nouvel espace d'échantillonnage.

**Règle de multiplication** : $P(A \cap B) = P(A|B)P(B)$, qui se généralise aux expériences en plusieurs étapes : $P(A_1 \cap A_2 \cap A_3) = P(A_3|A_1 \cap A_2)P(A_2|A_1)P(A_1)$.

**Probabilités totales** : si $A_1, \dots, A_n$ sont exclusifs et exhaustifs, $P(B) = \sum_i P(B|A_i)P(A_i)$.

**Bayes** : sous les mêmes hypothèses, $P(A_j|B) = \dfrac{P(B|A_j)P(A_j)}{\sum_i P(B|A_i)P(A_i)}$.

**Indépendance** (voir [[Indépendance d'événements]]) : $A$ et $B$ sont indépendants si $P(A|B) = P(A)$, ou de façon équivalente si $P(A \cap B) = P(A)P(B)$. Alors $A^c$ et $B$, $A$ et $B^c$, $A^c$ et $B^c$ le sont aussi. Pour des variables aléatoires, voir [[Loi conjointe]].

**Statistics** : l'aide-mémoire de troisième année rappelle les règles de l'union, de l'intersection (cas indépendant ou non) et la probabilité conditionnelle. Il réserve $P(A \cap B) = P(A|B)P(B)$ au cas « not independent » ; cette formule vaut en fait dans tous les cas, et se réduit à $P(A)P(B)$ quand $A$ et $B$ sont indépendants.

Liens : [[Espace probabilisé]], [[Événements incompatibles]], [[Équiprobabilité]], [[Dénombrement]]

## Erreurs du cours

- [[2 - Conditional proba and independence|Chp 2 - Conditional proba and independence]] (vérifié sur l'image) pose $A_1, \dots, A_n$ puis écrit la formule de Bayes avec « $\sum_{i=1}^{k}$ » et « $j = 1, \dots, k$ » ; il faut $\sum_{i=1}^{n}$ et $j = 1, \dots, n$.
- [[2 - Conditional proba and independence|Chp 2 - Conditional proba and independence]] (vérifié sur l'image) écrit « We also say "P(A) is the probability of A given B" » ; il faut « P(A|B) is the probability of A given B ».
Résumés : [[2 - Conditional proba and independence]], [[0 - proba&stats utilitaire]]
