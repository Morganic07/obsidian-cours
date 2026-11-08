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
maj: 2026-11-08
---

Pour $Z_1, \dots, Z_\nu$ normales centrées réduites iid, $X = Z_1^2 + \dots + Z_\nu^2$ suit la loi du khi-deux à $\nu$ degrés de liberté, $\chi^2_\nu$. C'est la gamma $(\nu/2, 2)$ ([[Loi exponentielle]], [[Fonction Gamma]]), de densité $\frac{1}{2^{\nu/2}\Gamma(\nu/2)}x^{\nu/2 - 1}e^{-x/2}$, $x > 0$. Sa moyenne vaut $\nu$, sa variance $2\nu$, et elle est asymétrique à droite.

**Additive** ([[Stabilité des lois par somme]]) : $\chi^2_{\nu_1} + \chi^2_{\nu_2}$ indépendantes donne $\chi^2_{\nu_1+\nu_2}$. **Soustractive** : si $X_3 = X_1 + X_2$ avec $X_1$ et $X_2$ indépendantes, $X_1 \sim \chi^2_{\nu_1}$ et $X_3 \sim \chi^2_{\nu_3}$, alors $X_2 \sim \chi^2_{\nu_3 - \nu_1}$.

**Échantillon normal** : la somme des carrés de $n$ normales centrées réduites indépendantes suit $\chi^2_n$ ; quand la moyenne est estimée par $\bar{X}$, on perd un degré de liberté : $(n-1)S^2/\sigma^2 \sim \chi^2_{n-1}$ (preuve laissée en devoir dans le cours). [[Erreurs du cours#^e-loi-du-khi-deux|✎]] Valeur critique $\chi^2_{\alpha,\nu}$ : aire $\alpha$ à sa droite. Sert à l'[[Intervalle de confiance]] pour $\sigma^2$.

**Test sur une variance** (Data analysis) : $\chi^{2*} = (n-1)s^2/\sigma_0^2$ ; la table n'est pas symétrique ([[Test du χ²]], [[8 - Chi²-Test]]). Valeurs laissant une aire de 0,005 à gauche : 0,010 pour 2 df, 0,072 pour 3, 0,207 pour 4, 10,52 pour 25. [[Erreurs du cours#^e-loi-du-khi-deux|✎]]

Liens : [[Loi de Student]], [[Distribution d'échantillonnage]]

Résumés : [[4 - Inferential statistics 3]], [[8 - Chi²-Test]]
