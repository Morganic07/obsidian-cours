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
  - formule des probabilités composées
  - arbre pondéré
  - a priori
  - a posteriori
matieres:
  - Probability
  - Statistics
sources:
  - "[[2 - Conditional proba and independence|Chp 2 - Conditional proba and independence]]"
  - "[[0 - proba&stats utilitaire|probabilité statistiques utilitaire]]"
  - "[[Raw/Year 2/Probability/Chp 2 : Conditional proba and independence .docx|Chp 2 - Conditional proba and independence]]"
maj: 2026-11-08
---

Pour $P(B) > 0$, $P(A|B) = P(A \cap B)/P(B)$ est la probabilité de $A$ sachant $B$ (*probability of A given B*) [[Erreurs du cours#^e-probabilite-conditionnelle|✎]] : conditionner sur $B$ prend $B$ comme nouvel espace d'échantillonnage.

**Règle de multiplication** : $P(A \cap B) = P(A|B)P(B)$, qui se généralise aux expériences en plusieurs étapes : $P(A_1 \cap A_2 \cap A_3) = P(A_3|A_1 \cap A_2)P(A_2|A_1)P(A_1)$.

**Probabilités totales** : si $A_1, \dots, A_n$ sont exclusifs et exhaustifs, $P(B) = \sum_i P(B|A_i)P(A_i)$.

**Bayes** : sous les mêmes hypothèses, $P(A_j|B) = \dfrac{P(B|A_j)P(A_j)}{\sum_{i=1}^{n} P(B|A_i)P(A_i)}$, pour $j = 1, \dots, n$. [[Erreurs du cours#^e-probabilite-conditionnelle|✎]]

**Indépendance** (voir [[Indépendance d'événements]]) : $A$ et $B$ sont indépendants si $P(A|B) = P(A)$, ou de façon équivalente si $P(A \cap B) = P(A)P(B)$. Alors $A^c$ et $B$, $A$ et $B^c$, $A^c$ et $B^c$ le sont aussi. Pour des variables aléatoires, voir [[Loi conjointe]].

**Statistics** : l'aide-mémoire de troisième année rappelle les règles de l'union, de l'intersection et la probabilité conditionnelle. La règle de l'intersection $P(A \cap B) = P(A|B)P(B)$ vaut dans tous les cas, et se réduit à $P(A)P(B)$ quand $A$ et $B$ sont indépendants. [[Erreurs du cours#^e-probabilite-conditionnelle|✎]]

## Compléments (hors du cours)

- **Une probabilité à part entière** : à $B$ fixé ($P(B) > 0$), l'application $A \mapsto P(A|B)$ est une probabilité ; elle en a toutes les propriétés, par exemple $P(A^c|B) = 1 - P(A|B)$. En revanche, en général $P(A|B) \ne P(B|A)$ : confondre les deux est l'erreur la plus courante.
- **Formule des probabilités composées** à $n$ étapes, valable si $P(A_1 \cap \dots \cap A_{n-1}) > 0$ :
  $$P(A_1 \cap \dots \cap A_n) = P(A_1)\,P(A_2|A_1)\,P(A_3|A_1 \cap A_2)\cdots P(A_n|A_1 \cap \dots \cap A_{n-1}).$$
- **Arbre pondéré** : chaque branche porte une probabilité conditionnelle ; on **multiplie** le long d'un chemin (probabilités composées) et on **additionne** les chemins qui mènent à $B$ (probabilités totales). Cas courant, la partition $\{A, A^c\}$ : $P(B) = P(B|A)P(A) + P(B|A^c)P(A^c)$.
- **Vocabulaire de Bayes** : $P(A_j)$ est la probabilité **a priori**, $P(B|A_j)$ la **vraisemblance**, $P(A_j|B)$ la probabilité **a posteriori**. Le dénominateur ne dépend pas de $j$, donc a posteriori $\propto$ vraisemblance $\times$ a priori.
- **Exemple du dépistage** : prévalence $P(M) = 1\,\%$, sensibilité $P(+|M) = 99\,\%$, spécificité $P(-|M^c) = 95\,\%$. Alors $P(+) = 0{,}01 \times 0{,}99 + 0{,}99 \times 0{,}05 = 0{,}0594$ et
  $$P(M|+) = \frac{0{,}0099}{0{,}0594} = \frac16 \approx 17\,\%.$$
  Un test positif ne donne qu'une chance sur six d'être malade, parce que la maladie est rare : les faux positifs des 99 % de sains l'emportent sur les vrais positifs. Négliger la prévalence s'appelle l'**oubli du taux de base**.

Liens : [[Espace probabilisé]], [[Événements incompatibles]], [[Équiprobabilité]], [[Dénombrement]], [[Vraisemblance]]

Résumés : [[2 - Conditional proba and independence]], [[0 - proba&stats utilitaire]]
