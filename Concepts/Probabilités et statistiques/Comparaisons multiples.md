---
type: concept
tags: [year3]
aliases: [multiple comparisons, tests post hoc, post hoc, test post hoc, Tukey HSD, méthode de Tukey, correction de Bonferroni, Bonferroni correction]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 12 : ANOVA and F-statistic .docx|Cours 12 - ANOVA and F-statistic]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : quand on réalise $m$ tests chacun au [[Seuil de signification|seuil]] $\alpha$, le risque de commettre au moins une [[Erreur de type I et de type II|erreur de type I]] augmente. Pour des tests indépendants, il vaut

$$1 - (1 - \alpha)^m$$

soit environ 14 % pour 3 tests et 40 % pour 10 tests à $\alpha = 5\,\%$. Les procédures de comparaisons multiples corrigent ce risque global (*familywise error rate*) pour le ramener à $\alpha$.

**Après une ANOVA** : un $F$ significatif dit seulement qu'au moins une moyenne diffère. Les tests *post hoc* disent lesquelles. Avec $k$ groupes, il y a $\frac{k(k-1)}{2}$ paires à comparer (3 pour 3 groupes, 10 pour 5 groupes).

- **Méthode de Tukey** (HSD, *Honestly Significant Difference*) : compare toutes les paires de moyennes en contrôlant le risque global ; c'est la méthode usuelle après une ANOVA à un facteur. En R : `TukeyHSD(aov(y ~ groupe))`, qui donne pour chaque paire la différence, son intervalle de confiance et une p-value ajustée.
- **Correction de Bonferroni** : chaque test se fait au seuil $\alpha/m$ (ou, de façon équivalente, on multiplie chaque p-value par $m$). Elle garantit un risque global d'au plus $\alpha$ quelle que soit la dépendance entre les tests, mais elle est conservatrice : elle perd de la puissance quand $m$ est grand. En R : `pairwise.t.test(y, groupe, p.adjust.method = "bonferroni")` ou `p.adjust(p, method = "bonferroni")`.

**Pourquoi pas plusieurs [[Test t|tests t]] sans correction** : c'est précisément la situation où le risque d'erreur de type I gonfle ; d'où l'ANOVA d'abord, puis des comparaisons corrigées.

## Dans le cours

Le cours ne les nomme pas. Elles apparaissent dans les compléments de [[12 - ANOVA and F-statistic]], qui justifie l'ANOVA par le refus de multiplier les tests $t$ par paires.

Voir aussi : [[ANOVA]], [[Erreur de type I et de type II]], [[Test t]], [[Seuil de signification]], [[P-value]], [[Test de Kruskal-Wallis]].

Résumés : [[12 - ANOVA and F-statistic]]
