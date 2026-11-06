---
type: source
tags: [year3]
sources: ["[[Cours 4 - Estimation]]"]
maj: 2026-11-05
---

Résumé de [[Cours 4 - Estimation]], dans [[Data analysis (Thanos) (matière)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Estimer un paramètre de population par un point, puis par un intervalle de confiance, et savoir lire cet intervalle.

## Contenu, dans l'ordre du cours

- **Mode, médiane, moyenne** : le mode est la valeur la plus fréquente, la médiane la valeur du milieu, la moyenne la valeur moyenne. Sur les courbes asymétriques à droite du cours, les trois ne coïncident pas.
- **Estimation ponctuelle** : une seule valeur, comme $\bar{X}$ pour estimer $\mu$.
- **Intervalle de confiance** : plus il est large, plus on a confiance qu'il contient $\mu$.

| Niveau de confiance | Exemple (revenu) | Note du cours |
|---|---|---|
| 100 % | de 0 à plus l'infini | certain, mais inutile |
| 95 % | de 35 000 à 41 000 € | niveau standard |
| 0 % | 38 000 € | estimation ponctuelle |

- **Formule** : $\bar{X} \pm Z \dfrac{\sigma}{\sqrt{n}}$. Si $\sigma$ est inconnu, on prend l'écart-type d'échantillon $s$, à condition que $n \ge 30$.
- **Interprétation correcte** : avec un intervalle à 95 %, dans 95 échantillons sur 100 la moyenne de la population se trouve dans les intervalles construits par la même procédure. Il est faux de dire qu'il y a 95 % de chances que $\mu$ « tombe » dans cet intervalle précis, car $\mu$ est fixe.
- **Réduire la largeur sans perdre de confiance** : augmenter $n$ (on divise par $\sqrt{n}$), ou réduire la variabilité par un meilleur échantillonnage, comme la stratification.
- **Percentile** : valeur sous laquelle se trouve un certain pourcentage de la population, $X = \mu + Z\sigma$.
- **Points clés** : la certitude à 100 % est impossible sur un échantillon (il faudrait un recensement) ; le niveau standard est 95 % ; $s^2$ est un estimateur sans biais de $\sigma^2$.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. L'image de la formule n'a pas été ouverte.

1. **Indice de $Z$** : la formule est transcrite avec $Z_{\alpha}$. Pour un intervalle bilatéral à $1-\alpha$, il faut $Z_{\alpha/2}$, comme dans [[Cours 7 - Z-Test (résumé)|Cours 7]] et dans le tableau récapitulatif de [[Cours 8 - Chi²-Test (résumé)|Cours 8]] (complément).
2. **Seuil $n \ge 30$** : le cours ne dit pas qu'on passe alors à la loi $t$ pour les petits échantillons, ce que fait [[Cours 6 - T-Test (résumé)|Cours 6]].
3. **Ligne 0 %** : à 0 % de confiance, l'« intervalle » se réduit à un point. Le cours donne 38 000 € sans dire d'où vient cette valeur (c'est l'estimation ponctuelle de l'exemple).
