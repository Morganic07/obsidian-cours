---
type: concept
tags: [year3]
aliases: [degré de liberté, ddl, degrees of freedom]
matieres: [Statistics, Data analysis (Thanos)]
sources: ["[[Raw/Year 3/Statistics/Chp4 Part2 : Inferential statistics.docx|Chp4 Part2 - Inferential statistics]]", "[[Raw/Year 3/Data analysis (Thanos)/Cours 6 : T-Test.docx|Cours 6 - T-Test]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : le nombre de degrés de liberté d'une statistique est le nombre de valeurs qui peuvent varier librement une fois imposées les contraintes du calcul. Il fixe la forme exacte des lois de [[Loi de Student|Student]], du [[Loi du khi-deux|khi-deux]] et de Fisher, et donc les valeurs critiques des tests.

**Exemple** : pour calculer la variance d'un échantillon de $n$ valeurs, on utilise les écarts à la moyenne $x_i - \bar{x}$. Leur somme est nulle : une fois $n-1$ écarts connus, le dernier est imposé. Il reste $n-1$ degrés de liberté, d'où le dénominateur $n-1$ de la variance corrigée :
$$s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2$$

**Valeurs à connaître** :

| Situation | Degrés de liberté |
|---|---|
| Test t sur une moyenne (un échantillon de taille $n$) | $n - 1$ |
| Test t de deux échantillons indépendants, variances égales | $n_1 + n_2 - 2$ |
| Test du khi-deux d'indépendance (tableau $r \times c$) | $(r-1)(c-1)$ |
| Test du khi-deux d'adéquation ($k$ classes, $m$ paramètres estimés) | $k - 1 - m$ |
| Régression linéaire à $p$ variables explicatives, $n$ observations (résidus) | $n - p - 1$ |
| ANOVA à $k$ groupes, $N$ observations | $k - 1$ (entre groupes) et $N - k$ (intra-groupes) |

Plus les degrés de liberté sont nombreux, plus la loi de Student se rapproche de la [[Loi normale|loi normale]].

## Dans le cours

Employés sans définition dans les fiches de Statistics et de Data analysis, pour lire les tables de Student et du khi-deux (voir [[4 - Inferential statistics 2]], [[6 - T-Test]]).

Voir aussi : [[Loi de Student]], [[Loi du khi-deux]], [[ANOVA]], [[Test du χ²]].

Résumés : [[4 - Inferential statistics 2]], [[6 - T-Test]]
