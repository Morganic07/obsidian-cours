---
type: concept
tags: [year2, year3]
aliases: [conditional probability, probabilités totales, law of total probability, théorème de Bayes, Bayes' theorem, règle de multiplication, multiplication rule]
matieres: [Probability, Statistics]
sources: ["[[Chp 2 - Conditional proba and independence]]", "[[probabilité statistiques utilitaire]]"]
maj: 2026-11-06
---

Pour $P(B) > 0$, $P(A|B) = P(A \cap B)/P(B)$ : conditionner sur $B$ prend $B$ comme nouvel espace d'échantillonnage.

**Règle de multiplication** : $P(A \cap B) = P(A|B)P(B)$, qui se généralise aux expériences en plusieurs étapes : $P(A_1 \cap A_2 \cap A_3) = P(A_3|A_1 \cap A_2)P(A_2|A_1)P(A_1)$.

**Probabilités totales** : si $A_1, \dots, A_n$ sont exclusifs et exhaustifs, $P(B) = \sum_i P(B|A_i)P(A_i)$.

**Bayes** : sous les mêmes hypothèses, $P(A_j|B) = \dfrac{P(B|A_j)P(A_j)}{\sum_i P(B|A_i)P(A_i)}$.

**Indépendance** (voir [[Indépendance d'événements]]) : $A$ et $B$ sont indépendants si $P(A|B) = P(A)$, ou de façon équivalente si $P(A \cap B) = P(A)P(B)$. Alors $A^c$ et $B$, $A$ et $B^c$, $A^c$ et $B^c$ le sont aussi. Pour des variables aléatoires, voir [[Loi conjointe]].

**Statistics** : l'aide-mémoire de troisième année rappelle les règles de l'union, de l'intersection (cas indépendant ou non) et la probabilité conditionnelle.

Liens : [[Espace probabilisé]], [[Événements incompatibles]], [[Équiprobabilité]], [[Dénombrement]]

## À vérifier

- Dans [[Chp 2 - Conditional proba and independence]], les bornes $n$ et $k$ sont mélangées dans la formule de Bayes, et la phrase « P(A) is the probability of A given B » semble une coquille (image non ouverte).
- Dans [[probabilité statistiques utilitaire]], « P(A∩B) = P(A|B)P(B) if not independent » : la formule vaut aussi dans le cas indépendant.

Résumés : [[Chp 2 - Conditional proba and independence (résumé)]], [[probabilité statistiques utilitaire (résumé)]]
