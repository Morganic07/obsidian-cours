---
type: concept
tags: [year3]
aliases: [chi-square test, chi square test, chi-square, test du khi-deux, test du chi-deux, loi du χ², χ² test, chi-square statistic, test d'indépendance du χ²]
matieres: [Data analysis (Thanos), Statistics]
sources: ["[[Cours 8 - Chi²-Test]]", "[[probabilité statistiques utilitaire]]"]
maj: 2026-11-06
---

Test [[Test paramétrique et non paramétrique|non paramétrique]], fondé sur la [[Loi du khi-deux|loi du χ²]], qui vérifie si deux variables catégorielles sont indépendantes à partir d'un [[Tableau de contingence|tableau croisé]].

**Statistique** : $\chi^2 = \sum\dfrac{(f_o - f_e)^2}{f_e}$, avec $f_o$ l'effectif observé et $f_e = \dfrac{\text{marge de ligne} \times \text{marge de colonne}}{N}$ l'effectif attendu sous indépendance. Degrés de liberté : $(\text{lignes} - 1)(\text{colonnes} - 1)$. On rejette $H_0$ (indépendance) si $\chi^2$ dépasse la valeur critique. Exemple du cours : tableau 2 par 2, $\chi^2 = 2{,}00 < 3{,}841$, on ne rejette pas. L'aide-mémoire de Statistics ([[probabilité statistiques utilitaire (résumé)|probabilité statistiques utilitaire]]) donne la même formule.

**Ce qu'il dit** : seulement si les variables sont indépendantes, pas la nature du lien. **Limites** : la statistique croît avec $N$ ; significatif n'est pas important. Conditions de validité citées : échantillonnage aléatoire simple, variables catégorielles, effectif attendu d'au moins 5 par cellule.

Dans la classification des tests de Data analysis, le χ² figure parmi les tests non paramétriques, à un échantillon comme à deux échantillons indépendants ou appariés, et χ² est sa statistique ([[Séance 5 - Hypothesis Testing (résumé)|Cours 5]], [[Séance 7 - Z-Test (résumé)|Cours 7]]).

**Loi du χ²** : continue, asymétrique à droite, de moyenne $k$ et de variance $2k$ ($k$ degrés de liberté). Si les $X_i$ sont normales, $\dfrac{(n-1)S^2}{\sigma^2}$ suit un χ² à $n-1$ degrés de liberté, d'où un intervalle de confiance et un test sur une variance : $\chi^{2*} = \dfrac{(n-1)s^2}{\sigma_0^2}$. Voir [[Loi du khi-deux]].

Voir aussi : [[Tableau de contingence]], [[Loi du khi-deux]], [[Test paramétrique et non paramétrique]]

Résumés : [[Séance 8 - Chi²-Test (résumé)]], [[Séance 5 - Hypothesis Testing (résumé)]], [[Séance 7 - Z-Test (résumé)]], [[probabilité statistiques utilitaire (résumé)]]
