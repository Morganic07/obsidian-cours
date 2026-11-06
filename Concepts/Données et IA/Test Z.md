---
type: concept
tags: [year3]
aliases: [z-test, z test, test Z sur une proportion, test de deux proportions, proportion regroupée, pooled proportion]
matieres: [Data analysis (Thanos), Statistics]
sources: ["[[Cours 7 - Z-Test]]"]
maj: 2026-11-06
---

Test utilisé quand $\sigma$ est connu ou que les échantillons sont grands ; sinon, on passe au [[Test t]] ([[Cours 7 - Z-Test]]).

- **Sur une proportion**, applicable si $nP$ et $n(1-P)$ valent au moins 5 : $Z = \dfrac{P_s - P}{\sqrt{P(1-P)/n}}$.
- **Deux proportions** : $Z = \dfrac{P_{s1} - P_{s2}}{\sqrt{\bar p(1-\bar p)\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}$, avec la proportion regroupée $\bar p = \dfrac{X_1 + X_2}{n_1 + n_2}$.

Notion parente : [[Test d'hypothèse]]. Voir aussi : [[Test t]], [[Approximation normale]], [[Loi normale]], [[Intervalle de confiance]].

## À vérifier

- Condition « ≥ 5 », puis « > 5 » sur la même diapositive.

Résumés : [[Séance 7 - Z-Test (résumé)]], [[Séance 5 - Hypothesis Testing (résumé)]], [[Séance 6 - T-Test (résumé)]], [[probabilité statistiques utilitaire (résumé)]]
