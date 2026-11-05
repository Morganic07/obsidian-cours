---
type: source
sources: ["[[probabilité statistiques utilitaire]]"]
maj: 2026-11-05
---

Résumé de [[probabilité statistiques utilitaire]], dans [[Year 3 - Statistics]]. En cas d'écart, le cours et ses images font foi. Les deux images n'ont pas été ouvertes : seules leurs transcriptions ont été lues.

## Idée générale

Aide-mémoire de deux pages, sans commentaire. Il va plus loin que les chapitres intégrés : tests d'hypothèse, deux échantillons, régression, khi-deux. Le wiki ne reprend que les formules dont un chapitre intégré établit le sens.

## Contenu

**Page 1**

- Moyenne, écart interquartile, coefficient de variation $CV = s/\bar{X} \times 100\,\%$, moyenne et variance de population et d'échantillon (voir [[Variance et écart-type d'échantillon]]).
- Scores $Z$ : $(X - \bar{X})/s$, $(X - \mu)/\sigma$, $(\bar{X} - \mu)/(\sigma/\sqrt{n})$, $(\bar{X} - \mu)/(s/\sqrt{n})$.
- Règles de probabilité : union, intersection (cas indépendant et non indépendant), [[Probabilité conditionnelle]], $_nP_r = n!/(n-r)!$, $_nC_r = n!/(r!(n-r)!)$, [[Loi binomiale]] ($nP$ et $nP(1-P)$ pour la moyenne et la variance).
- Corrélation $r$ de l'échantillon, $t_{n-2} = r\sqrt{n-2}/\sqrt{1-r^2}$, droite de régression $\hat{Y} = a + bX$ avec $b = \frac{n\sum XY - \sum X\sum Y}{n\sum X^2 - (\sum X)^2}$ et $a = \bar{Y} - b\bar{X}$ ($a = b_0$, $b = b_1$).

**Page 2**

- Statistique de test et intervalle pour une moyenne ($z$ si $\sigma$ connu, $t_{n-1}$ sinon) et pour une proportion.
- Différence de deux moyennes (variances connues, estimées, ou variance poolée $S^2_{pooled} = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}$, $t_{n_1+n_2-2}$) et de deux proportions ($\bar{P} = (x_1 + x_2)/(n_1 + n_2)$).
- Tailles d'échantillon : $n = Z^2\sigma^2/e^2$ et $n = Z^2P(1-P)/e^2$.
- Khi-deux : $\chi^2 = \sum (f_o - f_e)^2/f_e$, $f_e = (\text{total ligne} \times \text{total colonne})/n$.

Les intervalles de la moyenne et de la proportion rejoignent le chapitre 4 : voir [[Chp4 Part3 - Inferential statistics (résumé)]].

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Notation $Z_\alpha$** : l'aide-mémoire écrit $\bar{X} \pm Z_\alpha\sigma/\sqrt{n}$, alors que le chapitre 4 écrit $z_{\alpha/2}$ pour un intervalle bilatéral. L'aide-mémoire désigne sans doute le quantile bilatéral sous le nom $Z_\alpha$ ; à lire avec le chapitre, sans quoi on se trompe d'un facteur 2 sur $\alpha$ (complément).
2. **Probabilité d'une intersection** : « $P(A \cap B) = P(A|B)P(B)$ if A and B are not independent » est vrai aussi dans le cas indépendant (complément).
3. **Formules de tests et de régression** : elles n'ont pas de chapitre intégré dans le wiki. Aucune explication n'est reprise.
