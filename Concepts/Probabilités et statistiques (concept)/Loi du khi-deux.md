---
type: concept
tags: [year3]
aliases: [chi-squared distribution, chi-square distribution, loi du chi-deux, loi χ², khi-deux]
matieres: [Statistics, Data analysis (Thanos)]
sources: ["[[chp 4 - Part 3 - Inferential statistics (résumé)|Chp4 Part3 - Inferential statistics]]", "[[Séance 8 - Chi²-Test (résumé)|Cours 8 - Chi²-Test]]"]
maj: 2026-11-06
---

Pour $Z_1, \dots, Z_\nu$ normales centrées réduites iid, $X = Z_1^2 + \dots + Z_\nu^2$ suit la loi du khi-deux à $\nu$ degrés de liberté, $\chi^2_\nu$. C'est la gamma $(\nu/2, 2)$ ([[Loi exponentielle]], [[Fonction Gamma]]), de densité $\frac{1}{2^{\nu/2}\Gamma(\nu/2)}x^{\nu/2 - 1}e^{-x/2}$, $x > 0$. Sa moyenne vaut $\nu$, sa variance $2\nu$, et elle est asymétrique à droite.

**Additive** ([[Stabilité des lois par somme]]) : $\chi^2_{\nu_1} + \chi^2_{\nu_2}$ indépendantes donne $\chi^2_{\nu_1+\nu_2}$. **Soustractive** : si $X_3 = X_1 + X_2$ avec $X_1$ et $X_2$ indépendantes, $X_1 \sim \chi^2_{\nu_1}$ et $X_3 \sim \chi^2_{\nu_3}$, alors $X_2 \sim \chi^2_{\nu_3 - \nu_1}$.

**Échantillon normal** : $(n-1)S^2/\sigma^2 \sim \chi^2_{n-1}$ (preuve laissée en devoir dans le cours). Valeur critique $\chi^2_{\alpha,\nu}$ : aire $\alpha$ à sa droite. Sert à l'[[Intervalle de confiance]] pour $\sigma^2$.

**Test sur une variance** (Data analysis) : $\chi^{2*} = (n-1)s^2/\sigma_0^2$ ; la table n'est pas symétrique ([[Test du χ²]], [[Séance 8 - Chi²-Test (résumé)]]).

Liens : [[Loi de Student]], [[Distribution d'échantillonnage]]

## À vérifier

- [[Séance 8 - Chi²-Test (résumé)|Cours 8 - Chi²-Test]] parle de « somme des carrés d'une loi de Student », et donne $n-1$ degrés de liberté pour $x_1^2 + \dots + x_n^2$ : à corriger avant un examen (la définition donne $n$ degrés pour $n$ normales centrées réduites).
- La colonne 0,005 de la table du même cours est fausse.

Résumés : [[chp 4 - Part 3 - Inferential statistics (résumé)]], [[Séance 8 - Chi²-Test (résumé)]]
