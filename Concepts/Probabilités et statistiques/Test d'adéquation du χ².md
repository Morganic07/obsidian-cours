---
type: concept
tags: [year3]
aliases: [goodness of fit, goodness-of-fit test, chi-square goodness of fit, test d'ajustement du khi-deux, test d'adéquation du khi-deux, test du χ² à un échantillon]
sources: ["[[Raw/Year 3/Data analysis (Thanos)/Cours 8 : Chi²-Test.docx|Cours 8 - Chi²-Test]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : test du χ² de Pearson à **un échantillon**, qui compare les effectifs observés de $k$ catégories aux effectifs attendus sous une loi donnée.

- $H_0$ : les données suivent la loi donnée (probabilités $p_1, \dots, p_k$ des catégories) ; $H_1$ : elles ne la suivent pas.
- Effectifs attendus : $f_{e,i} = N\,p_i$, avec $N$ l'effectif total.
- Statistique :
$$\chi^2 = \sum_{i=1}^{k} \frac{(f_{o,i} - f_{e,i})^2}{f_{e,i}}$$
- Sous $H_0$, elle suit approximativement une [[Loi du khi-deux|loi du χ²]] à $k - 1$ degrés de liberté (les effectifs sont liés par leur somme $N$), moins un degré par paramètre de la loi estimé sur les données (par exemple $k - 2$ pour une [[Loi de Poisson]] dont on estime $\lambda$ par la moyenne).
- On rejette $H_0$ si $\chi^2$ dépasse la valeur critique ; le test est toujours unilatéral à droite.
- Condition : effectifs attendus d'au moins 5 environ dans chaque catégorie ; sinon, regrouper des catégories voisines.

**Exemple** : un dé lancé 60 fois est-il équilibré ? Sous $H_0$, $p_i = 1/6$ et $f_e = 10$ par face. On compare la statistique à la valeur critique du $\chi^2_5$, 11,07 à 5 %.

En R : `chisq.test(x, p = c(...))`, où `x` contient les effectifs observés et `p` les probabilités attendues (par défaut, toutes égales).

Le [[Test de Kolmogorov-Smirnov]] est un autre test d'adéquation, qui compare des fonctions de répartition et convient aux données continues sans les regrouper en classes.

## Dans le cours

Le cours ne le nomme pas : il traite le χ² d'indépendance sur un tableau croisé. C'est le khi-deux « à un échantillon » de l'organigramme des tests de [[7 - Z-Test]], et il apparaît dans les compléments de [[8 - Chi²-Test]].

Voir aussi : [[Test du χ²]], [[Loi du khi-deux]], [[Test de Kolmogorov-Smirnov]], [[Test paramétrique et non paramétrique]]

Résumés : [[8 - Chi²-Test]], [[7 - Z-Test]]
