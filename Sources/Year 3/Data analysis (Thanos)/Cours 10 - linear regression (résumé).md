---
type: source
sources: ["[[Cours 10 - linear regression]]"]
maj: 2026-11-05
---

Résumé de [[Cours 10 - linear regression]], dans [[Year 3 - Data analysis (Thanos)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Régression linéaire simple : modèle, ajustement par les [[Moindres carrés|moindres carrés]], décomposition de la variation, conditions de validité vérifiées sur les résidus, test de la pente. Voir [[Régression linéaire]].

## Contenu, dans l'ordre du cours

- **Quatuor d'Anscombe** (1973) : quatre jeux de données avec les mêmes statistiques (moyenne de $x$ 9, de $y$ 7,50, variance de $x$ 11, de $y$ 4,13, corrélation 0,816, même droite) mais des nuages très différents : I linéaire propre, II courbe, III linéaire avec un point aberrant, IV un seul point isolé suffit à produire la corrélation. Leçon : toujours visualiser les données.
- **Modèles de régression** : répondent à « quelle est la relation entre les variables ? » et servent surtout à prédire et estimer. Une variable dépendante numérique, une ou plusieurs variables explicatives numériques ou catégorielles. Classement : simple (1 variable explicative) ou multiple (2 ou plus), chacun linéaire ou non linéaire.
- **Modèle linéaire simple** : $y = \beta_0 + \beta_1x + \varepsilon$, avec $\beta_0$ ordonnée à l'origine de la population, $\beta_1$ pente, $\varepsilon$ erreur aléatoire. La droite des moyennes est $E(y) = \beta_0 + \beta_1x$.
- **Moindres carrés** : les écarts positifs et négatifs se compensent, d'où la somme des carrés $SSE = \sum(y_i - \hat{y}_i)^2 = \sum\hat{\varepsilon}_i^2$, minimisée.
- **Méthode avec des dérivées partielles** : pour les points $(1,1)$, $(2,1)$, $(3,3)$, on minimise $f(b,m) = [1-(b+m)]^2 + [1-(b+2m)]^2 + [3-(b+3m)]^2$. Les dérivées donnent $6b + 12m = 10$ et $12b + 28m = 24$, d'où $(b,m) = (-1/3, 1)$. Le discriminant vaut $f_{bb}f_{mm} - f_{bm}^2 = 24 > 0$ et $f_{bb} = 6 > 0$ : minimum local, et global car la surface est une « cuvette parabolique ». Droite : $y = x - 1/3$.
- **Formules** : pente $\hat{\beta}_1 = \dfrac{SS_{xy}}{SS_{xx}}$, ordonnée $\hat{\beta}_0 = \bar{y} - \hat{\beta}_1\bar{x}$.
- **Exemple engrais et rendement** : $(4;3)$, $(6;5{,}5)$, $(10;6{,}5)$, $(12;9)$. Sommes 32, 24, 296, 218. $\hat{\beta}_1 = \dfrac{218 - 32 \times 24/4}{296 - 32^2/4} = 0{,}65$, $\hat{\beta}_0 = 6 - 0{,}65 \times 8 = 0{,}80$. Interprétation : +0,65 kg de rendement par kg d'engrais, et 0,8 kg attendu sans engrais.
- **Quatre conditions sur l'erreur** : moyenne nulle, variance constante, loi normale, erreurs indépendantes.
- **Erreur standard** : $s^2 = \dfrac{SSE}{n-2}$, $s = \sqrt{SSE/(n-2)}$, écart-type d'échantillon des erreurs. Elle intervient dans la significativité des paramètres et la précision des prédictions.
- **Décomposition** : $SST = \sum(y_i - \bar{y})^2$ (totale), $SSR = \sum(\hat{y}_i - \bar{y})^2$ (expliquée), $SSE = \sum(y_i - \hat{y}_i)^2$ (non expliquée).
- **Résidus** $e_i = Y_i - \hat{Y}_i$ : on vérifie linéarité (pas de motif courbe), indépendance (pas de bande montante ou ondulante), normalité (diagramme de probabilité normale à peu près droit) et variance constante (homoscédasticité, pas de forme d'entonnoir).
- **Test de la pente** : $H_0 : \beta_1 = 0$ (pas de relation linéaire), $H_a : \beta_1 \ne 0$. Statistique $t = \dfrac{\hat{\beta}_1}{S_{\hat{\beta}_1}}$ avec $S_{\hat{\beta}_1} = \dfrac{s}{\sqrt{SS_{xx}}}$ et $df = n-2$. La p-value de chaque variable teste l'absence de corrélation avec la variable dépendante.
- **Exemple publicité et ventes** : $(1,1)$, $(2,1)$, $(3,2)$, $(4,2)$, $(5,4)$, $\hat{\beta}_0 = -0{,}1$, $\hat{\beta}_1 = 0{,}7$, $s = 0{,}6055$. $S_{\hat{\beta}_1} = 0{,}6055/\sqrt{10} = 0{,}1914$, $t = 0{,}7/0{,}1914 = 3{,}657$, valeurs critiques $\pm 3{,}182$ ($df = 3$), donc rejet : il y a une relation.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Images non ouvertes ; calculs refaits à la main.

1. **Dérivée partielle $f_b$** : la transcription écrit « $-10 + 6b + 12 = 0$ ». Le terme $12m$ a perdu son $m$ : la forme correcte est $-10 + 6b + 12m = 0$ (complément).
2. **Somme de $y$ du jeu III d'Anscombe (82,50 contre 82,51)** : fausse alerte, la somme exacte des valeurs du tableau est 82,50, les autres sont arrondies.
3. **Points du graphique de l'exemple engrais** : la transcription note qu'ils semblent décalés par rapport au tableau. Le calcul, lui, est exact ; le graphique n'a pas été vérifié.
4. **« Dataset II is not distributed normally »** : le jeu II suit une courbe, c'est la relation qui n'est pas linéaire. La phrase du cours parle de distribution normale (complément).
5. **« Dataset IV : un point suffit à produire une forte corrélation »** : la corrélation de 0,816 est celle de tous les jeux. L'idée est correcte, la phrase la présente comme propre au jeu IV.
