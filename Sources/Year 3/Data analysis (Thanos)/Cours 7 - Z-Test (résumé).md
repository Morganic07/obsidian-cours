---
type: source
sources: ["[[Cours 7 - Z-Test]]"]
maj: 2026-11-05
---

Résumé de [[Cours 7 - Z-Test]], dans [[Year 3 - Data analysis (Thanos)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Panorama des tests d'hypothèse (paramétriques ou non, appariés ou indépendants), puis le test $Z$ sur une proportion, avec un échantillon et avec deux.

## Contenu, dans l'ordre du cours

- **Statistique de test** : variable aléatoire calculée sur l'échantillon, utilisée pour décider du rejet de $H_0$ et pour calculer la p-value. Correspondances : z-test et statistique z, t-test et t, ANOVA et [[Statistique F|F]], test du χ² et χ².
- **Limites d'un test** : il aide la décision sans la prendre ; il n'explique pas pourquoi une différence existe ; il repose sur des probabilités, donc sans certitude complète.
- **Paramétrique ou non** : un test paramétrique suppose de l'information sur un paramètre de la population (« la moyenne vaut 15 »). Un test non paramétrique ne suppose pas que les données viennent d'une loi gaussienne.
- **Hiérarchie des tests** (organigramme du cours) : paramétriques, à un échantillon (t, z), à deux échantillons indépendants (t à deux groupes, z) ou appariés (t apparié) ; non paramétriques, à un échantillon (χ², Kolmogorov-Smirnov, runs, binomial), à deux échantillons indépendants (χ², Mann-Whitney, médiane, Kolmogorov-Smirnov) ou appariés (signe, Wilcoxon, McNemar, χ²).
- **Appariés ou indépendants** : exemple de l'insuline. Mesure avant et après traitement sur les mêmes 30 patients, données appariées. Mesure sur 30 patients sous placebo et 30 autres sous traitement, données indépendantes, test $t$ à deux groupes indépendants.
- **Procédure en cinq étapes** : poser $H_0$ et $H_1$, choisir le niveau de signification, identifier la statistique, formuler la règle de décision, prendre l'échantillon et décider (ne pas rejeter $H_0$, ou rejeter $H_0$ et accepter $H_1$).
- **Test $Z$ sur une proportion** : applicable quand $nP$ et $n(1-P)$ valent au moins 5, par approximation normale de la binomiale ($\mu = np$, $\sigma = \sqrt{np(1-p)}$). $Z = \dfrac{P_s - P}{\sqrt{P(1-P)/n}}$, avec $P_s$ proportion d'échantillon et $P$ proportion supposée (annotation de l'étudiant). Intervalle de confiance : $\hat{p} \pm Z_{\alpha/2}\sqrt{\hat{p}(1-\hat{p})/n}$. L'annotation précise : test bilatéral, donc $Z_{\alpha/2}$.
- **Exemple de la politicienne** : elle affirme que 70 % des habitants sont démocrates, l'échantillon de 100 en donne 50. $H_0 : P = 0{,}70$, $H_1 : P \ne 0{,}70$, $\alpha = 0{,}05$. Intervalle à 95 % : $0{,}50 \pm 1{,}96\sqrt{0{,}5 \times 0{,}5/100} = 0{,}50 \pm 0{,}10$, soit $[0{,}40 ; 0{,}60]$.
- **Deux proportions** : conditions $n_1p_1$, $n_1(1-p_1)$, $n_2p_2$, $n_2(1-p_2)$ tous au moins 5. $Z = \dfrac{P_{s1} - P_{s2}}{\sqrt{\bar{p}(1-\bar{p})(1/n_1 + 1/n_2)}}$ avec $P_{si} = X_i/n_i$ et $\bar{p} = \dfrac{X_1 + X_2}{n_1 + n_2}$ (proportion regroupée).

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Données appariées et « two-sample t-test »** : image lue directement, la diapositive écrit « an appropriate test … would be a two-sample t-test » pour le cas avant/après. L'organigramme du même cours donne « Paired t test » pour les échantillons appariés. C'est le test $t$ apparié qui convient (complément). **À corriger avant un examen.**
2. **Exemple de la politicienne** : le cours calcule l'intervalle mais pas la statistique. Avec la formule du cours, $Z = (0{,}50 - 0{,}70)/\sqrt{0{,}7 \times 0{,}3/100} \approx -4{,}4$, donc rejet de $H_0$ (complément). Cohérent avec l'intervalle, qui ne contient pas 0,70.
3. **« CIE »** : l'alerte de la transcription soupçonne une faute pour « CI ». C'est l'abréviation de *confidence interval estimator* dans les diapositives de ce cours, pas une faute (fausse alerte probable).
4. **Formule de l'intervalle coupée** : l'image de l'approximation normale se termine sur « Confidence Interval Estimator of P: ». La formule se trouve sur l'image suivante (dessin de l'étudiant), la phrase ne s'arrête donc pas en perdant du contenu.
5. **Condition d'approximation** : « $\ge 5$ » dans un cas, « $> 5$ » dans la dernière phrase de la diapositive.
