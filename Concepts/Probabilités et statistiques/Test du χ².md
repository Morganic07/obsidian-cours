---
type: concept
tags:
  - year3
aliases:
  - chi-square test
  - chi square test
  - chi-square
  - test du khi-deux
  - test du chi-deux
  - loi du χ²
  - χ² test
  - chi-square statistic
  - test d'indépendance du χ²
  - test d'homogénéité du χ²
  - correction de Yates
  - test exact de Fisher
  - Fisher's exact test
matieres:
  - Data analysis (Thanos)
  - Statistics
sources:
  - "[[8 - Chi²-Test|Cours 8 - Chi²-Test]]"
  - "[[0 - proba&stats utilitaire|probabilité statistiques utilitaire]]"
maj: 2026-11-08
---

Test [[Test paramétrique et non paramétrique|non paramétrique]], fondé sur la [[Loi du khi-deux|loi du χ²]], qui vérifie si deux variables catégorielles sont indépendantes à partir d'un [[Tableau de contingence|tableau croisé]].

**Statistique** : $\chi^2 = \sum\dfrac{(f_o - f_e)^2}{f_e}$, avec $f_o$ l'effectif observé et $f_e = \dfrac{\text{marge de ligne} \times \text{marge de colonne}}{N}$ l'effectif attendu sous indépendance. Degrés de liberté : $(\text{lignes} - 1)(\text{colonnes} - 1)$. On rejette $H_0$ (indépendance) si $\chi^2$ dépasse la valeur critique. Exemple du cours : tableau 2 par 2, $\chi^2 = 2{,}00 < 3{,}841$, on ne rejette pas. L'aide-mémoire de Statistics ([[0 - proba&stats utilitaire|probabilité statistiques utilitaire]]) donne la même formule.

**Ce qu'il dit** : seulement si les variables sont indépendantes, pas la nature du lien. **Limites** : la statistique croît avec $N$ ; significatif n'est pas important. Conditions de validité citées : échantillonnage aléatoire simple, variables catégorielles, effectif attendu d'au moins 5 par cellule.

**Origine et usages (complément, hors du cours)** : la statistique a été proposée par Karl Pearson en 1900. Elle a trois usages, avec la même formule $\sum (f_o - f_e)^2/f_e$ :
- **indépendance** (le cas du cours) : deux variables catégorielles mesurées sur un même échantillon ;
- **homogénéité** : une variable catégorielle comparée entre plusieurs populations échantillonnées séparément ; même calcul, même $df = (r-1)(c-1)$ ;
- **adéquation** : un échantillon comparé à une loi donnée, voir [[Test d'adéquation du χ²]].

**D'où viennent $f_e$ et $df$ (complément, hors du cours)** : sous indépendance, $P(\text{ligne } i \text{ et colonne } j) = \dfrac{\text{marge } i}{N} \times \dfrac{\text{marge } j}{N}$ ; en multipliant par $N$, on retrouve $f_e$. Les marges étant fixées par les données, la dernière cellule de chaque ligne et de chaque colonne se déduit des autres : seules $(r-1)(c-1)$ cellules sont libres.

**Validité de l'approximation (complément, hors du cours)** : la loi du χ² n'est qu'une approximation de la loi de la statistique, valable pour des effectifs attendus assez grands. Règle de Cochran : aucun $f_e < 1$ et au plus 20 % des cellules sous 5. Sinon, on regroupe des modalités voisines ou, sur un tableau $2 \times 2$, on fait le **test exact de Fisher**, qui calcule la probabilité exacte des tableaux de mêmes marges. Sur un $2 \times 2$, on applique souvent la **correction de continuité de Yates** : $\sum \dfrac{(\lvert f_o - f_e \rvert - 0{,}5)^2}{f_e}$, plus prudente.

**Lien avec le test Z (complément, hors du cours)** : sur un tableau $2 \times 2$, le χ² d'indépendance est égal à $Z^2$, carré de la statistique du [[Test Z]] de comparaison de deux proportions (avec proportion regroupée) ; $1{,}96^2 = 3{,}84$ est la valeur critique du $\chi^2_1$ à 5 %.

**Intensité du lien (complément, hors du cours)** : le test ne dit pas si le lien est fort ; pour cela, on calcule le [[V de Cramér]] ($\varphi$ sur un $2 \times 2$). Sur l'exemple du cours, la p-value vaut $P(\chi^2_1 \ge 2{,}00) \approx 0{,}16$ et $\varphi \approx 0{,}28$.

**En R (complément, hors du cours)** : `chisq.test(tableau)` (correction de Yates par défaut sur un $2 \times 2$ ; `correct = FALSE` pour retrouver le calcul du cours), `chisq.test(x, p = ...)` pour l'adéquation, `fisher.test(tableau)` pour le test exact.

Dans la classification des tests de Data analysis, le χ² figure parmi les tests non paramétriques, à un échantillon comme à deux échantillons indépendants ou appariés, et χ² est sa statistique ([[5 - Hypothesis Testing|Cours 5]], [[7 - Z-Test|Cours 7]]).

**Loi du χ²** : continue, asymétrique à droite, de moyenne $k$ et de variance $2k$ ($k$ degrés de liberté). Si les $X_i$ sont normales, $\dfrac{(n-1)S^2}{\sigma^2}$ suit un χ² à $n-1$ degrés de liberté, d'où un intervalle de confiance et un test sur une variance : $\chi^{2*} = \dfrac{(n-1)s^2}{\sigma_0^2}$. Voir [[Loi du khi-deux]].

Voir aussi : [[Tableau de contingence]], [[Loi du khi-deux]], [[Test paramétrique et non paramétrique]], [[Test d'adéquation du χ²]], [[V de Cramér]], [[Test Z]]

Résumés : [[8 - Chi²-Test]], [[5 - Hypothesis Testing]], [[7 - Z-Test]], [[0 - proba&stats utilitaire]]
