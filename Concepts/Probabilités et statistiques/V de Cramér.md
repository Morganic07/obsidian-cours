---
type: concept
tags: [year3]
aliases: [Cramér's V, Cramer's V, V de Cramer, coefficient phi, coefficient φ, phi coefficient]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 8 : Chi²-Test.docx|Cours 8 - Chi²-Test]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : mesure de l'intensité du lien entre deux variables catégorielles, tirée de la statistique du [[Test du χ²]] calculée sur un [[Tableau de contingence]] à $r$ lignes et $c$ colonnes, et rendue indépendante de l'effectif total $N$ :

$$V = \sqrt{\frac{\chi^2}{N\,\bigl(\min(r, c) - 1\bigr)}}$$

- $V$ est compris entre 0 (indépendance : tableau observé égal au tableau attendu) et 1 (lien parfait : connaître une variable détermine l'autre).
- Le dénominateur $N(\min(r, c) - 1)$ est la plus grande valeur que peut prendre le $\chi^2$ pour ce tableau, d'où la normalisation.
- Pour un tableau $2 \times 2$, $\min(r, c) - 1 = 1$ et $V$ se réduit au **coefficient $\varphi$** : $\varphi = \sqrt{\chi^2/N}$. Sur un $2 \times 2$ de cellules $a, b, c, d$, $\varphi = \dfrac{ad - bc}{\sqrt{(a+b)(c+d)(a+c)(b+d)}}$, qui garde un signe ; c'est la corrélation de Pearson entre deux variables codées 0/1.
- Repères usuels de Cohen pour $\varphi$ : 0,1 lien faible, 0,3 moyen, 0,5 fort.

**Pourquoi il complète le test** : le $\chi^2$ croît avec $N$ à intensité de lien égale (doubler tous les effectifs double le $\chi^2$, sans changer $V$). Le test dit seulement si le lien est significatif ; $V$ dit s'il est important. C'est une taille d'effet, à rapporter avec la p-value.

**Exemple** (sur l'exemple du cours, homicides et ventes d'armes, $N = 25$, $\chi^2 = 2{,}00$) : $\varphi = \sqrt{2{,}00/25} \approx 0{,}28$, un lien proche de « moyen » qui n'est pourtant pas significatif, faute d'effectif.

En R : `sqrt(chisq.test(t, correct = FALSE)$statistic / (sum(t) * (min(dim(t)) - 1)))` pour un tableau `t`.

## Dans le cours

Le cours ne le nomme pas. Il dit seulement que le $\chi^2$ est sensible à la taille de l'échantillon et que « significatif ne veut pas dire important ». Le $V$ de Cramér apparaît dans les compléments de [[8 - Chi²-Test]].

Voir aussi : [[Test du χ²]], [[Tableau de contingence]], [[Covariance et corrélation]], [[P-value]]

Résumés : [[8 - Chi²-Test]]
