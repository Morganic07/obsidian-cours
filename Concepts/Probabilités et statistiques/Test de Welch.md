---
type: concept
tags: [year3]
aliases: [Welch t-test, test t de Welch, Welch-Satterthwaite, Welch's t-test]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 6 : T-Test.docx|Cours 6 - T-Test]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : le test de Welch est une variante du [[Test t|test t]] à deux échantillons indépendants qui **ne suppose pas l'égalité des variances** des deux populations (pas d'[[Homoscédasticité|homoscédasticité]]). Il teste $H_0 : \mu_1 = \mu_2$ sans mettre les variances en commun.

Statistique de test :

$$t = \frac{\bar X_1 - \bar X_2}{\sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}}$$

Sous $H_0$, elle suit approximativement une [[Loi de Student|loi de Student]] dont les degrés de liberté sont donnés par la formule de **Welch-Satterthwaite** :

$$df \approx \frac{\left(\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}\right)^2}{\dfrac{(s_1^2/n_1)^2}{n_1 - 1} + \dfrac{(s_2^2/n_2)^2}{n_2 - 1}}$$

Ce nombre n'est en général pas entier ; il est compris entre $\min(n_1, n_2) - 1$ et $n_1 + n_2 - 2$.

- **Quand l'utiliser** : quand les écarts-types diffèrent nettement, surtout si les effectifs sont inégaux, cas où le test à variance commune peut se tromper de niveau. Les populations doivent rester à peu près normales (ou les échantillons assez grands).
- **En R** : `t.test(x, y)` fait un test de Welch par défaut ; `t.test(x, y, var.equal = TRUE)` donne le test à variance commune ($s^2_{pooled}$) du cours.

## Dans le cours

Le cours ne le nomme pas : il présente le test t à deux échantillons avec variance commune. Le test de Welch apparaît dans les compléments de [[6 - T-Test]].

Voir aussi : [[Test t]], [[Homoscédasticité]], [[Loi de Student]], [[Échantillons appariés et indépendants]], [[Test d'hypothèse]].

Résumés : [[6 - T-Test]]
