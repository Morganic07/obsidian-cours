---
type: concept
tags:
  - year3
aliases:
  - chi-squared distribution
  - chi-square distribution
  - loi du chi-deux
  - loi χ²
  - khi-deux
matieres:
  - Statistics
  - Data analysis (Thanos)
sources:
  - "[[4 - Inferential statistics 3|Chp4 Part3 - Inferential statistics]]"
  - "[[8 - Chi²-Test|Cours 8 - Chi²-Test]]"
maj: 2026-11-07
---

Pour $Z_1, \dots, Z_\nu$ normales centrées réduites iid, $X = Z_1^2 + \dots + Z_\nu^2$ suit la loi du khi-deux à $\nu$ degrés de liberté, $\chi^2_\nu$. C'est la gamma $(\nu/2, 2)$ ([[Loi exponentielle]], [[Fonction Gamma]]), de densité $\frac{1}{2^{\nu/2}\Gamma(\nu/2)}x^{\nu/2 - 1}e^{-x/2}$, $x > 0$. Sa moyenne vaut $\nu$, sa variance $2\nu$, et elle est asymétrique à droite.

**Additive** ([[Stabilité des lois par somme]]) : $\chi^2_{\nu_1} + \chi^2_{\nu_2}$ indépendantes donne $\chi^2_{\nu_1+\nu_2}$. **Soustractive** : si $X_3 = X_1 + X_2$ avec $X_1$ et $X_2$ indépendantes, $X_1 \sim \chi^2_{\nu_1}$ et $X_3 \sim \chi^2_{\nu_3}$, alors $X_2 \sim \chi^2_{\nu_3 - \nu_1}$.

**Échantillon normal** : $(n-1)S^2/\sigma^2 \sim \chi^2_{n-1}$ (preuve laissée en devoir dans le cours). Valeur critique $\chi^2_{\alpha,\nu}$ : aire $\alpha$ à sa droite. Sert à l'[[Intervalle de confiance]] pour $\sigma^2$.

**Test sur une variance** (Data analysis) : $\chi^{2*} = (n-1)s^2/\sigma_0^2$ ; la table n'est pas symétrique ([[Test du χ²]], [[8 - Chi²-Test]]).

Liens : [[Loi de Student]], [[Distribution d'échantillonnage]]

## Erreurs du cours

- [[8 - Chi²-Test|Cours 8 - Chi²-Test]] (vérifié sur l'image) part de « If $x_1 + \dots + x_n$ follows a Student's t-distribution with $(n-1)$ degrees of freedom » et conclut que « if X is normal », $x_1^2 + \dots + x_n^2$ « has a $\chi^2$ distribution with $(n-1)$ degrees of freedom » ; il faut $n$ degrés de liberté pour la somme des carrés de $n$ normales centrées réduites indépendantes (définition ci-dessus). Les $n-1$ degrés valent pour $(n-1)S^2/\sigma^2$, où la moyenne est estimée.
- [[8 - Chi²-Test|Cours 8 - Chi²-Test]] : dans l'extrait de table (vérifié sur l'image), la colonne 0.005 est fausse à partir de df = 2 (0.0001, 0.003, 0.018… et 6.08 pour df = 25) ; les valeurs usuelles sont environ 0.010, 0.072, 0.207… et 10.52 pour df = 25. Les autres colonnes concordent avec les tables usuelles (contrôle par sondage, hors du cours).

Résumés : [[4 - Inferential statistics 3]], [[8 - Chi²-Test]]
